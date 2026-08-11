#!/usr/bin/env python3
"""Stage 20 — SHA-256 identity and cross-source match manifest.

Writes:
  build/hash_manifest/01_sha256_by_cnid_*.tsv          (sharded canonical identity)
  build/hash_manifest/02_cross_source_matches_*.tsv    (sharded, aggregated)
  build/hash_manifest/03_cross_source_unaligned_*.tsv  (sharded size-mismatch)
  build/hash_manifest/04_coverage.tsv
  build/deep/sha256_by_path/                           (opt-in full per-path)

Read-only against PostgreSQL.
"""
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import (BUILD, Sink, connect, load_limits, section_manifest,
                        write_single)

ROOT_NAMES = {1: "APFS", 2: "0728", 116: "GAI"}

ALIAS_QUERY = """
SELECT a.cnid, c.size, c.alloc, max(a.n_paths) AS n_paths, a.sha256,
       (SELECT a2.relative_path FROM jpmi_alias_map a2
        WHERE a2.cnid = a.cnid AND a2.role = 'canonical' LIMIT 1) AS canonical_path
FROM jpmi_alias_map a
JOIN jpmi_cnid_map c ON c.cnid = a.cnid
WHERE c.kind = 'file'
GROUP BY a.cnid, c.size, c.alloc, a.sha256
ORDER BY a.cnid
"""

MATCH_QUERY = """
WITH RECURSIVE fam(id, root) AS (
  SELECT id, id FROM sources WHERE id IN (1, 2, 116)
  UNION ALL
  SELECT s.id, fam.root FROM sources s JOIN fam ON s.parent_source_id = fam.id
),
jpmi AS (
  SELECT DISTINCT ON (a.sha256) a.sha256, a.relative_path AS jpmi_path,
         a.size AS jpmi_size
  FROM jpmi_sha256_allpaths a
  WHERE a.sha256 IS NOT NULL AND a.sha256 <> ''
  ORDER BY a.sha256, a.file_id NULLS LAST
)
SELECT h.sha256, fam.root,
       count(*) AS n,
       count(*) FILTER (WHERE f.size IS NOT NULL AND j.jpmi_size IS NOT NULL
                        AND f.size <> j.jpmi_size) AS size_mismatch
FROM hash_sources h
JOIN fam ON fam.id = h.source_id
JOIN jpmi j ON j.sha256 = h.sha256
LEFT JOIN files f ON f.id = h.file_id
GROUP BY h.sha256, fam.root
"""

JPMI_QUERY = """
SELECT DISTINCT ON (a.sha256) a.sha256, a.relative_path, a.size
FROM jpmi_sha256_allpaths a
WHERE a.sha256 IS NOT NULL AND a.sha256 <> ''
ORDER BY a.sha256, a.file_id NULLS LAST
"""

DEEP_QUERY = """
SELECT a.sha256, a.cnid, a.size, a.volume_path, a.relative_path
FROM jpmi_sha256_allpaths a
ORDER BY a.cnid, a.volume_path
"""

COUNTS_QUERY = """
SELECT
  (SELECT count(*) FROM jpmi_sha256_allpaths) AS total_paths,
  (SELECT count(*) FROM jpmi_sha256_allpaths WHERE sha256 IS NOT NULL AND sha256 <> '')
    AS hashed_paths,
  (SELECT count(DISTINCT cnid) FROM jpmi_sha256_allpaths WHERE sha256 IS NOT NULL AND sha256 <> '')
    AS distinct_cnids,
  (SELECT count(DISTINCT sha256) FROM jpmi_sha256_allpaths WHERE sha256 IS NOT NULL AND sha256 <> '')
    AS distinct_hashes,
  (SELECT count(*) FROM jpmi_alias_map) AS alias_rows,
  (SELECT count(*) FROM jpmi_hash_overlap) AS hash_overlap_rows,
  (SELECT count(*) FROM jpmi_path_overlap) AS path_overlap_rows
"""


def main():
    limits = load_limits()
    budget = limits["per_file_budget_bytes"]
    deep = limits["deep_exports"]
    pg = connect()
    deep_sink = None
    with pg.cursor() as c:
        c.execute(ALIAS_QUERY)
        alias = c.fetchall()
        c.execute(MATCH_QUERY)
        match = c.fetchall()
        c.execute(JPMI_QUERY)
        jpmi = c.fetchall()
        c.execute(COUNTS_QUERY)
        counts = c.fetchone()
        if deep:
            deep_sink = Sink(BUILD / "deep" / "sha256_by_path", "sha",
                             ["sha256", "cnid", "size", "volume_path",
                              "relative_path"], budget)
            c.execute(DEEP_QUERY)
            for row in c:
                deep_sink.row(row)
    pg.close()

    sha_to_jpmi = {s: (p, sz) for s, p, sz in jpmi}
    matches = defaultdict(dict)
    for sha, root, n, mismatch in match:
        matches[sha][root] = (n, mismatch)

    cnid_out = Sink(BUILD / "hash_manifest", "01_sha256_by_cnid",
                    ["cnid", "size", "alloc", "n_paths", "sha256",
                     "canonical_path"], budget)
    for cnid, size, alloc, n_paths, sha, canon in alias:
        cnid_out.row((cnid, size or "", alloc or "", n_paths, sha, canon or ""))
    cnid_files, cnid_rows = cnid_out.close()

    match_out = Sink(BUILD / "hash_manifest", "02_cross_source_matches",
                     ["sha256", "jpmi_canonical_path", "jpmi_size",
                      "match_count", "match_sources", "size_mismatch_count"],
                     budget)
    unaligned_out = Sink(BUILD / "hash_manifest", "03_cross_source_unaligned",
                         ["sha256", "jpmi_canonical_path", "jpmi_size",
                          "match_sources", "match_count", "size_mismatch_count"],
                         budget)
    per_root_match = defaultdict(int)
    matched_hashes = set()
    unaligned_hashes = set()
    for sha, (jpath, jsize) in sorted(sha_to_jpmi.items()):
        root_map = matches.get(sha, {})
        if not root_map:
            continue
        matched_hashes.add(sha)
        total = 0
        total_mismatch = 0
        parts = []
        for root in (1, 2, 116):
            if root not in root_map:
                continue
            n, mm = root_map[root]
            total += n
            total_mismatch += mm
            per_root_match[root] += n
            if n:
                parts.append(f"{ROOT_NAMES[root]}={n}")
        if total_mismatch:
            unaligned_hashes.add(sha)
            unaligned_out.row((sha, jpath or "", jsize or "", ",".join(parts),
                               total, total_mismatch))
        match_out.row((sha, jpath or "", jsize or "", total, ",".join(parts),
                       total_mismatch))
    match_files, match_rows = match_out.close()
    unaligned_files, unaligned_rows = unaligned_out.close()

    total_paths, hashed_paths, distinct_cnids, distinct_hashes, alias_rows, \
        hash_overlap_rows, path_overlap_rows = counts
    exclusive = distinct_hashes - len(matched_hashes)
    coverage_rows = [
        ("total_paths", total_paths),
        ("hashed_paths", hashed_paths),
        ("distinct_cnids_hashed", distinct_cnids),
        ("distinct_hashes", distinct_hashes),
        ("hashes_matched_to_apfs_family", per_root_match[1]),
        ("hashes_matched_to_gai_family", per_root_match[116]),
        ("hashes_matched_to_0728_family", per_root_match[2]),
        ("distinct_hashes_with_any_cross_source_match", len(matched_hashes)),
        ("distinct_hashes_with_size_mismatch", len(unaligned_hashes)),
        ("distinct_hashes_exclusive_to_jpmi", exclusive),
        ("alias_map_rows", alias_rows),
        ("jpmi_hash_overlap_rows", hash_overlap_rows),
        ("jpmi_path_overlap_rows", path_overlap_rows),
    ]
    coverage_out = write_single(BUILD / "hash_manifest", "04_coverage.tsv",
                                ["metric", "value"], coverage_rows)

    outputs = [
        ("01_sha256_by_cnid.tsv", cnid_rows),
        ("02_cross_source_matches.tsv", match_rows),
        ("03_cross_source_unaligned.tsv", unaligned_rows),
        ("04_coverage.tsv", len(coverage_rows)),
    ]
    if deep_sink:
        deep_files, deep_rows = deep_sink.close()
        import json
        (BUILD / "deep" / "sha256_by_path" / "_manifest.json").write_text(
            json.dumps({"section": "deep/sha256_by_path", "rows": deep_rows,
                        "files": [{"file": str(p.relative_to(BUILD)), "size": s}
                                  for p, s in deep_files]},
                       indent=2, sort_keys=True))
        outputs.append(("(deep/sha256_by_path)", deep_rows))
    section_manifest(BUILD / "hash_manifest", outputs,
                     source_rows={"alias_rows": len(alias),
                                  "match_rows": len(match),
                                  "jpmi_rows": len(jpmi)})

    print(f"cnid hashes: {cnid_rows:,} in {len(cnid_files)} shards")
    print(f"cross-source matches: {match_rows:,} in {len(match_files)} shards")
    print(f"unaligned: {unaligned_rows:,} in {len(unaligned_files)} shards")
    print(f"exclusive hashes: {exclusive:,}")
    if deep_sink:
        print(f"deep sha-by-path rows: {deep_rows:,} in {len(deep_files)} shards")


if __name__ == "__main__":
    main()
