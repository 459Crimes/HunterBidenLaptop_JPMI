# Catalog: hash manifest

> Reported SHA-256 identities for JPMI catalog objects. Articles: [Forensic image](../FORENSIC_IMAGE.md) · [Contents census](../CONTENTS_CENSUS.md) · [How to verify](../08_reproducibility.md). Parent: [Evidence catalog](README.md).

Hashes here are **manifest evidence** received with the forensic reports. This GitHub tree does not recompute them from unpublished source bytes.

Folder: [`build/hash_manifest/`](../../build/hash_manifest/) · [`_manifest.json`](../../build/hash_manifest/_manifest.json)

| File | Rows | Size | Notes |
|---|---:|---:|---|
| [`01_sha256_by_cnid_00001.tsv`](../../build/hash_manifest/01_sha256_by_cnid_00001.tsv) | 221,807 | 50.9 MB | Shard 1 of CNID → SHA-256 |
| [`01_sha256_by_cnid_00002.tsv`](../../build/hash_manifest/01_sha256_by_cnid_00002.tsv) | 110,314 | 24.5 MB | Shard 2 (same columns) |
| [`04_coverage.tsv`](../../build/hash_manifest/04_coverage.tsv) | 6 | 158 B | Totals used in the infobox |

Both CNID shards share a header. Together they are **332,121** data rows (221,807 + 110,314). Coverage metrics:

| Metric | Value |
|---|---:|
| Hash-manifest paths | 655,330 |
| Paths with SHA-256 | 655,330 |
| Distinct hashed CNIDs | 332,097 |
| Distinct SHA-256 | 180,046 |
| Alias-map rows | 655,330 |
| Canonical hashed-CNID export rows | 332,097 |

## Columns (`01_sha256_by_cnid_*.tsv`)

`cnid`, `size`, `alloc`, `n_paths`, `sha256`, `canonical_path`

## How to use this with the file tree

- **576,249** = normalized inventory paths ([file tree](file_tree.md))
- **397,440** = CNID map rows ([metadata](metadata.md))
- **180,046** = distinct reported contents
- Extra alias-map paths are TSK **slack** siblings, not Unix hard links ([Copy method](../COPY_METHOD.md))

Cross-corpus match tables are **not** in this repository ([Scope](../SCOPE.md)).
