#!/usr/bin/env python3
"""Stage 20 — JPMI-only SHA-256 identity and coverage export.

Writes:
  build/hash_manifest/01_sha256_by_cnid_*.tsv
  build/hash_manifest/04_coverage.tsv
  build/deep/sha256_by_path/                 (optional full per-path export)

This standalone JPMI repository intentionally does not generate cross-corpus
match tables. Comparative analysis belongs in a separate project.

Read-only against PostgreSQL.
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import (BUILD, Sink, connect, load_limits, section_manifest,
                        write_single)

ALIAS_QUERY = """
SELECT a.cnid, c.size, c.alloc, max(a.n_paths) AS n_paths, a.sha256,
       (SELECT a2.relative_path
          FROM jpmi_alias_map a2
         WHERE a2.cnid = a.cnid AND a2.role = 'canonical'
         LIMIT 1) AS canonical_path
  FROM jpmi_alias_map a
  JOIN jpmi_cnid_map c ON c.cnid = a.cnid
 WHERE c.kind = 'file'
 GROUP BY a.cnid, c.size, c.alloc, a.sha256
 ORDER BY a.cnid
"""

DEEP_QUERY = """
SELECT a.sha256, a.cnid, a.size, a.volume_path, a.relative_path
  FROM jpmi_sha256_allpaths a
 ORDER BY a.cnid, a.volume_path
"""

COUNTS_QUERY = """
SELECT
  (SELECT count(*)
     FROM jpmi_sha256_allpaths) AS total_paths,
  (SELECT count(*)
     FROM jpmi_sha256_allpaths
    WHERE sha256 IS NOT NULL AND sha256 <> '') AS hashed_paths,
  (SELECT count(DISTINCT cnid)
     FROM jpmi_sha256_allpaths
    WHERE sha256 IS NOT NULL AND sha256 <> '') AS distinct_cnids,
  (SELECT count(DISTINCT sha256)
     FROM jpmi_sha256_allpaths
    WHERE sha256 IS NOT NULL AND sha256 <> '') AS distinct_hashes,
  (SELECT count(*) FROM jpmi_alias_map) AS alias_rows
"""


def remove_legacy_comparison_outputs(out_dir: Path) -> None:
    """Prevent a JPMI-only rebuild from leaving stale comparison artifacts."""
    for pattern in (
        "02_cross_source_matches*.tsv",
        "03_cross_source_unaligned*.tsv",
    ):
        for path in out_dir.glob(pattern):
            path.unlink()


def main():
    limits = load_limits()
    budget = limits["per_file_budget_bytes"]
    deep = limits["deep_exports"]

    out_dir = BUILD / "hash_manifest"
    out_dir.mkdir(parents=True, exist_ok=True)
    remove_legacy_comparison_outputs(out_dir)

    pg = connect()
    deep_sink = None
    with pg.cursor() as c:
        c.execute(ALIAS_QUERY)
        alias_rows = c.fetchall()

        c.execute(COUNTS_QUERY)
        counts = c.fetchone()

        if deep:
            deep_sink = Sink(
                BUILD / "deep" / "sha256_by_path",
                "sha",
                ["sha256", "cnid", "size", "volume_path", "relative_path"],
                budget,
            )
            c.execute(DEEP_QUERY)
            for row in c:
                deep_sink.row(row)
    pg.close()

    cnid_out = Sink(
        out_dir,
        "01_sha256_by_cnid",
        ["cnid", "size", "alloc", "n_paths", "sha256", "canonical_path"],
        budget,
    )
    for cnid, size, alloc, n_paths, sha, canon in alias_rows:
        cnid_out.row((cnid, size or "", alloc or "", n_paths, sha, canon or ""))
    cnid_files, cnid_rows = cnid_out.close()

    total_paths, hashed_paths, distinct_cnids, distinct_hashes, alias_count = counts
    coverage_rows = [
        ("total_paths", total_paths),
        ("hashed_paths", hashed_paths),
        ("distinct_cnids_hashed", distinct_cnids),
        ("distinct_hashes", distinct_hashes),
        ("alias_map_rows", alias_count),
        ("canonical_cnid_hash_rows", cnid_rows),
    ]
    write_single(out_dir, "04_coverage.tsv", ["metric", "value"], coverage_rows)

    outputs = [
        ("01_sha256_by_cnid.tsv", cnid_rows),
        ("04_coverage.tsv", len(coverage_rows)),
    ]

    if deep_sink:
        deep_files, deep_rows = deep_sink.close()
        deep_dir = BUILD / "deep" / "sha256_by_path"
        (deep_dir / "_manifest.json").write_text(
            json.dumps(
                {
                    "section": "deep/sha256_by_path",
                    "rows": deep_rows,
                    "files": [
                        {"file": str(p.relative_to(BUILD)), "size": s}
                        for p, s in deep_files
                    ],
                },
                indent=2,
                sort_keys=True,
            ),
            encoding="utf-8",
        )
        outputs.append(("(deep/sha256_by_path)", deep_rows))

    section_manifest(
        out_dir,
        outputs,
        source_rows={
            "alias_rows": len(alias_rows),
            "total_paths": total_paths,
            "hashed_paths": hashed_paths,
        },
    )

    print(f"JPMI canonical CNID hashes: {cnid_rows:,} in {len(cnid_files)} shards")
    print(f"JPMI hashed paths: {hashed_paths:,} / {total_paths:,}")
    print(f"JPMI distinct SHA-256 values: {distinct_hashes:,}")
    if deep_sink:
        print(f"deep JPMI SHA-by-path rows: {deep_rows:,} in {len(deep_files)} shards")


if __name__ == "__main__":
    main()
