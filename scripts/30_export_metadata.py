#!/usr/bin/env python3
"""Stage 30 — metadata distributions and summaries.

Writes:
  build/metadata/01_time_distribution.tsv
  build/metadata/02_extension_distribution.tsv
  build/metadata/03_type_distribution.tsv
  build/metadata/04_permission_distribution.tsv
  build/metadata/05_cnid_summary.tsv
  build/metadata/06_alias_summary.tsv
  build/deep/{file_times_full,cnid_map_full,alias_map_full}/  (opt-in)

Read-only against PostgreSQL.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import (BUILD, Sink, connect, load_limits, section_manifest,
                        sha256, write_single)

TIME_YEAR_QUERY = """
SELECT 'created' AS event, extract(year FROM created_ts)::int AS bucket,
       count(*) AS n, COALESCE(sum(f.size), 0) AS bytes
FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
WHERE created_ts IS NOT NULL GROUP BY 2
UNION ALL
SELECT 'modified', extract(year FROM modified_ts)::int, count(*), COALESCE(sum(f.size), 0)
FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
WHERE modified_ts IS NOT NULL GROUP BY 2
UNION ALL
SELECT 'accessed', extract(year FROM accessed_ts)::int, count(*), COALESCE(sum(f.size), 0)
FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
WHERE accessed_ts IS NOT NULL GROUP BY 2
"""

TIME_MONTH_QUERY = """
SELECT 'created' AS event,
       to_char(created_ts, 'YYYY-MM') AS bucket, count(*) AS n,
       COALESCE(sum(f.size), 0) AS bytes
FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
WHERE created_ts IS NOT NULL
  AND extract(year FROM created_ts) IN (2019, 2020, 2022, 2024) GROUP BY 2
UNION ALL
SELECT 'modified', to_char(modified_ts, 'YYYY-MM'), count(*),
       COALESCE(sum(f.size), 0)
FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
WHERE modified_ts IS NOT NULL
  AND extract(year FROM modified_ts) IN (2019, 2020, 2022, 2024) GROUP BY 2
UNION ALL
SELECT 'accessed', to_char(accessed_ts, 'YYYY-MM'), count(*),
       COALESCE(sum(f.size), 0)
FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
WHERE accessed_ts IS NOT NULL
  AND extract(year FROM accessed_ts) IN (2019, 2020, 2022, 2024) GROUP BY 2
"""

EXT_QUERY = """
SELECT COALESCE(NULLIF(r.file_extension, ''), '[none]') AS extension,
       count(*) AS n, COALESCE(sum(f.size), 0) AS bytes, count(f.sha256) AS hashes
FROM jpmi_file_report r LEFT JOIN files f ON f.id = r.file_id
GROUP BY 1 ORDER BY n DESC
"""

TYPE_QUERY = """
SELECT COALESCE(NULLIF(r.file_type, ''), '[unknown]') AS file_type,
       count(*) AS n, COALESCE(sum(f.size), 0) AS bytes
FROM jpmi_file_report r LEFT JOIN files f ON f.id = r.file_id
GROUP BY 1 ORDER BY n DESC
"""

PERM_QUERY = """
SELECT COALESCE(NULLIF(r.permissions, ''), '[unknown]') AS permissions,
       count(*) AS n, COALESCE(sum(f.size), 0) AS bytes
FROM jpmi_file_report r LEFT JOIN files f ON f.id = r.file_id
GROUP BY 1 ORDER BY n DESC
"""

CNID_METRICS = """
SELECT
  (SELECT count(*) FROM jpmi_cnid_map) AS total_entries,
  (SELECT count(*) FROM jpmi_cnid_map WHERE kind = 'dir') AS directories,
  (SELECT count(*) FROM jpmi_cnid_map WHERE kind = 'file') AS files,
  (SELECT count(*) FROM jpmi_cnid_map WHERE alloc = 'allocated') AS allocated,
  (SELECT count(*) FROM jpmi_cnid_map WHERE alloc = 'unallocated') AS unallocated,
  (SELECT count(*) FROM jpmi_cnid_map WHERE file_id IS NOT NULL) AS with_file_id,
  (SELECT count(*) FROM jpmi_cnid_map WHERE parent_cnid IS NULL) AS no_parent,
  (SELECT count(DISTINCT parent_cnid) FROM jpmi_cnid_map) AS distinct_parents,
  (SELECT max(array_length(regexp_split_to_array(parent_path, '/'), 1))
     FROM jpmi_cnid_map) AS max_depth
"""

ALIAS_METRICS = """
SELECT
  (SELECT count(*) FROM jpmi_alias_map) AS total_rows,
  (SELECT count(*) FROM jpmi_alias_map WHERE role = 'canonical') AS canonical_rows,
  (SELECT count(*) FROM jpmi_alias_map WHERE role = 'alias') AS alias_rows,
  (SELECT count(DISTINCT cnid) FROM jpmi_alias_map) AS distinct_cnids,
  (SELECT count(DISTINCT sha256) FROM jpmi_alias_map) AS distinct_hashes,
  (SELECT count(*) FROM (SELECT cnid FROM jpmi_alias_map GROUP BY cnid
     HAVING count(*) > 1) x) AS multi_path_cnids,
  (SELECT max(n_paths) FROM jpmi_alias_map) AS max_paths_for_cnid
"""

DEEP = {
    "file_times_full": """
        SELECT f.relative_path, f.size, f.sha256,
               t.created_ts, t.modified_ts, t.accessed_ts, t.is_deleted
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 ORDER BY f.relative_path
    """,
    "cnid_map_full": """
        SELECT cnid, parent_cnid, name, parent_path, kind, size, alloc, file_id
        FROM jpmi_cnid_map ORDER BY cnid
    """,
    "alias_map_full": """
        SELECT cnid, sha256, n_paths, role, volume_path, relative_path, file_id
        FROM jpmi_alias_map ORDER BY cnid, role, volume_path
    """,
}


def main():
    limits = load_limits()
    budget = limits["per_file_budget_bytes"]
    deep = limits["deep_exports"]
    pg = connect()
    deep_sinks = {}
    with pg.cursor() as c:
        c.execute(TIME_YEAR_QUERY)
        time_year = c.fetchall()
        c.execute(TIME_MONTH_QUERY)
        time_month = c.fetchall()
        c.execute(EXT_QUERY)
        ext_rows = c.fetchall()
        c.execute(TYPE_QUERY)
        type_rows = c.fetchall()
        c.execute(PERM_QUERY)
        perm_rows = c.fetchall()
        c.execute(CNID_METRICS)
        cnid_metrics = c.fetchone()
        c.execute(ALIAS_METRICS)
        alias_metrics = c.fetchone()
        if deep:
            for name, query in DEEP.items():
                sink = Sink(BUILD / "deep" / name, "rows",
                            ["relative_path", "size", "sha256", "created_ts",
                             "modified_ts", "accessed_ts", "is_deleted"]
                            if name == "file_times_full" else
                            ["cnid", "parent_cnid", "name", "parent_path",
                             "kind", "size", "alloc", "file_id"]
                            if name == "cnid_map_full" else
                            ["cnid", "sha256", "n_paths", "role", "volume_path",
                             "relative_path", "file_id"], budget)
                c.execute(query)
                for row in c:
                    sink.row(row)
                deep_sinks[name] = sink
    pg.close()

    time_rows = []
    for event, bucket, n, bytes_ in sorted(time_year):
        time_rows.append((event, f"year-{int(bucket)}", n, bytes_))
    for event, bucket, n, bytes_ in sorted(time_month):
        time_rows.append((event, f"month-{bucket}", n, bytes_))
    time_out = write_single(BUILD / "metadata", "01_time_distribution.tsv",
                            ["event_type", "bucket", "row_count", "size_bytes"],
                            time_rows)

    ext_out = write_single(BUILD / "metadata", "02_extension_distribution.tsv",
                           ["extension", "file_count", "size_bytes",
                            "hash_count"], ext_rows)
    type_out = write_single(BUILD / "metadata", "03_type_distribution.tsv",
                            ["file_type", "file_count", "size_bytes"],
                            type_rows)
    perm_out = write_single(BUILD / "metadata", "04_permission_distribution.tsv",
                            ["permissions", "file_count", "size_bytes"],
                            perm_rows)

    cnid_names = ["total_entries", "directories", "files", "allocated",
                  "unallocated", "with_file_id", "no_parent", "distinct_parents",
                  "max_depth"]
    cnid_summary = list(zip(cnid_names, cnid_metrics))
    cnid_out = write_single(BUILD / "metadata", "05_cnid_summary.tsv",
                            ["metric", "value"], cnid_summary)

    alias_names = ["total_rows", "canonical_rows", "alias_rows", "distinct_cnids",
                   "distinct_hashes", "multi_path_cnids", "max_paths_for_cnid"]
    alias_summary = list(zip(alias_names, alias_metrics))
    alias_out = write_single(BUILD / "metadata", "06_alias_summary.tsv",
                             ["metric", "value"], alias_summary)

    outputs = [
        ("01_time_distribution.tsv", len(time_rows)),
        ("02_extension_distribution.tsv", len(ext_rows)),
        ("03_type_distribution.tsv", len(type_rows)),
        ("04_permission_distribution.tsv", len(perm_rows)),
        ("05_cnid_summary.tsv", len(cnid_summary)),
        ("06_alias_summary.tsv", len(alias_summary)),
    ]
    deep_info = []
    for name, sink in deep_sinks.items():
        deep_files, deep_rows = sink.close()
        (BUILD / "deep" / name / "_manifest.json").write_text(
            json.dumps({"section": f"deep/{name}", "rows": deep_rows,
                        "files": [{"file": str(p.relative_to(BUILD)), "size": s,
                                   "sha256": sha256(p)} for p, s in deep_files]},
                       indent=2, sort_keys=True))
        deep_info.append((name, deep_rows))
    section_manifest(BUILD / "metadata", outputs,
                     source_rows={"time_year": len(time_year),
                                  "time_month": len(time_month)})
    for name, rows in deep_info:
        print(f"deep {name}: {rows:,} rows")
    print(f"time rows: {len(time_rows):,}")


if __name__ == "__main__":
    main()
