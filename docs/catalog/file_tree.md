# Catalog: file tree

> Directory and home-folder rollups for the JPMI inventory. Articles: [What is on the copy](../04_what_is_on_the_copy.md) · [Contents census](../CONTENTS_CENSUS.md). Parent: [Evidence catalog](README.md).

These tables answer **where files sit**, not **how many unique documents** exist. Path, CNID, and hash counts are different numbers ([hash catalog](hash_manifest.md)).

Folder: [`build/file_tree/`](../../build/file_tree/) · [`_manifest.json`](../../build/file_tree/_manifest.json)

Underlying inventory: **576,249** normalized paths (`source_rows.query_rows` in the section manifest).

| File | Rows | Size | Notes |
|---|---:|---:|---|
| [`01_directory_tree.tsv`](../../build/file_tree/01_directory_tree.tsv) | 71,905 | 19.6 MB | One row per represented directory; child counts and size/hash coverage |
| [`02_top_level_summary.tsv`](../../build/file_tree/02_top_level_summary.tsv) | 4 | 341 B | `Users` vs HFS+ structures vs EFI vs GPT |
| [`03_home_overview.tsv`](../../build/file_tree/03_home_overview.tsv) | 15 | 1.2 KB | Direct children of `JPMI://Users/roberthunter` |

## Columns

`path` / `top_path` / `home_subdir`, `depth` (directory tree only), `parent_path` (directory tree), `dir_count`, `file_count`, `size_bytes`, `hash_count`, `hash_pct`, `min_modified_ts`, `max_modified_ts`.

## Counts cited in the articles

| Article figure | Source row |
|---|---|
| 572,743 file rows under `Users` | top-level summary |
| Library 251,863 · Documents 119,794 · Pictures 92,393 · Movies 61,202 · Downloads 23,415 · Music 19,313 · Desktop 4,654 | home overview |
| Music `hash_count` = 0 | coverage gap in this rollup, not “no files” |
| Desktop `max_modified_ts` 2020-10-15 | Finder `.DS_Store` cluster |

The ~280 GB “unallocated ranges” line is unused space on the 500 GB destination, not cloned laptop slack. See [Contents census](../CONTENTS_CENSUS.md) and [Copy method](../COPY_METHOD.md).
