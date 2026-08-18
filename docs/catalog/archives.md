# Catalog: deep metadata archives

> Partitioned full-volume metadata. **Not** source-image bytes. Parent: [Evidence catalog](README.md).

Folder: [`build/archives/`](../../build/archives/) · part list: [`_manifest.tsv`](../../build/archives/_manifest.tsv)

These archives are the published form of large per-file tables (directory tree, times, SHA-256 by path, CNID map, alias map). Each set is one `.tar.gz` split into GitHub-safe parts (all currently a single part).

| Archive set | Part | Size | What extracts |
|---|---|---:|---|
| `deep_file_tree_full` | [`deep_file_tree_full_001.tar.gz.part`](../../build/archives/deep_file_tree_full_001.tar.gz.part) | 18.5 MB | Full directory-tree shards |
| `deep_file_times_full` | [`deep_file_times_full_001.tar.gz.part`](../../build/archives/deep_file_times_full_001.tar.gz.part) | 19.3 MB | Per-path created/modified/accessed |
| `deep_sha256_by_path` | [`deep_sha256_by_path_001.tar.gz.part`](../../build/archives/deep_sha256_by_path_001.tar.gz.part) | 22.4 MB | Path-level SHA-256 |
| `deep_cnid_map_full` | [`deep_cnid_map_full_001.tar.gz.part`](../../build/archives/deep_cnid_map_full_001.tar.gz.part) | 7.2 MB | HFS+ catalog map |
| `deep_alias_map_full` | [`deep_alias_map_full_001.tar.gz.part`](../../build/archives/deep_alias_map_full_001.tar.gz.part) | 21.8 MB | Path ↔ CNID (including TSK slack names) |

## Reassembly

```text
cat deep_<section>_*.tar.gz.part > deep_<section>.tar.gz
tar tzf deep_<section>.tar.gz
tar xzf deep_<section>.tar.gz
```

Each part’s size and SHA-256 are in `_manifest.tsv`. The summary tables in the other catalogs are enough for most reading; use these archives only when a row-level lookup is required.

See also: [How to verify](../08_reproducibility.md).
