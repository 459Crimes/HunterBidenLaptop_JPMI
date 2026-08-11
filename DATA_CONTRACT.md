# Data Contract

All TSV files are UTF-8, LF-terminated, header row on the first line, and tab-
separated. All shard files share an identical header. Timestamps are rendered
`YYYY-MM-DD HH:MM:SS` in the time zone recorded by the source report (CDT/CST
for the file list, UTC for the TSK timeline); no conversion is applied.

## file_tree/

### `01_directory_tree.tsv`

Columns: `path`, `depth`, `parent_path`, `dir_count`, `file_count`,
`size_bytes`, `hash_count`, `hash_pct`, `min_modified_ts`, `max_modified_ts`

One row per directory in the inventory tree (derived from `files` paths for
source `122`). `dir_count` counts immediate child directories; `file_count` and
`size_bytes` count regular files under the directory (not recursive); `hash_pct`
is the fraction of those files with a SHA-256.

### `02_top_level_summary.tsv`

Columns: `top_path`, `file_count`, `size_bytes`, `hash_count`, `hash_pct`,
`min_modified_ts`, `max_modified_ts`

Rollup for each first-level inventory branch (`Users`, `Basic data partition
(2)`, `EFI System Partition (1)`, `Unpartitioned Space [GPT]`, malformed rows).

### `03_home_overview.tsv`

Columns: `home_subdir`, `file_count`, `size_bytes`, `hash_count`, `hash_pct`,
`min_modified_ts`, `max_modified_ts`

Rollup for the direct children of `Users/roberthunter` (`Library`, `Documents`,
`Pictures`, `Movies`, `Downloads`, `Music`, `Desktop`, others).

## hash_manifest/

### `01_sha256_by_cnid_*.tsv`

Columns: `cnid`, `size`, `n_paths`, `sha256`, `canonical_path`, `alloc`

One row per distinct allocated CNID with a SHA-256 (rank-1 master manifest,
canonical identity). Sharded.

### `02_cross_source_matches_*.tsv`

Columns: `sha256`, `jpmi_canonical_path`, `jpmi_size`, `match_count`,
`match_sources`, `sample_match_path`

One row per distinct JPMI SHA-256 that has at least one exact SHA-256 match in
another corpus (`hash_sources`), with aggregate match counts per source family
and one sample matched path. Sharded.

### `03_cross_source_unaligned_*.tsv`

Columns: `sha256`, `jpmi_canonical_path`, `jpmi_size`, `match_sources`,
`match_count`

JPMI hashes that have matches in other corpora but with a **size mismatch**
(exact-hash/size contradiction requiring review). Sharded.

### `04_coverage.tsv`

Columns: `metric`, `value`

Coverage counts: paths total, paths hashed, distinct CNIDs, distinct hashes,
hashes matched to each corpus family, exclusive hashes, and the 2019-03-31
boundary definition.

## metadata/

### `01_time_distribution.tsv`

Columns: `event_type` (`created`/`modified`/`accessed`), `bucket`,
`row_count`, `size_bytes`

Year bucket and (for 2019) month bucket counts from `jpmi_file_times`.

### `02_extension_distribution.tsv`

Columns: `extension`, `file_count`, `size_bytes`, `hash_count`

### `03_type_distribution.tsv`

Columns: `file_type`, `file_count`, `size_bytes`

### `04_permission_distribution.tsv`

Columns: `permissions`, `file_count`, `size_bytes`

### `05_cnid_summary.tsv`

Columns: `metric`, `value`

CNID hierarchy metrics from `jpmi_cnid_map`.

### `06_alias_summary.tsv`

Columns: `metric`, `value`

Hard-link/alias statistics from `jpmi_alias_map`.

## volume_info/

### `01_volume_identity.tsv`

Columns: `field`, `value`

Volume name, HFS+ volume identifier, filesystem, sector offset, reported
creation and last-write dates.

### `02_volume_metadata.tsv`

Columns: `object`, `size_bytes`, `modified_ts`, `note`

Volume-level metadata objects: `.journal`, `.journal_info_block`,
`.Spotlight-V100/*`, `.DocumentRevisions-V100/*`, `.DS_Store`, GPT structural
records.

### `03_volume_system_state.tsv`

Columns: `system_area`, `object_count`, `size_bytes`, `note`

Rollups for Spotlight, DocumentRevisions, GPT/EFI structures, and home system
libraries.

## disk_info/

### `01_acquisition.tsv`

Columns: `field`, `value`

The `jpmi_acquisition` record verbatim (image, format, MD5/SHA1, size, sectors,
tool, case number, drive model/serial).

### `02_partition_map.tsv`

Columns: `partition`, `type`, `guid`, `byte_start`, `byte_length`, `note`

GPT/EFI/HFS+ partition identity.

### `03_disk_identity.tsv`

Columns: `field`, `value`

Consolidated device identity (reported device, serial, disk GUID, volume
identifier).

## reports/

Markdown reports. Section policy:

- **Exact-byte findings**: only statements supportable from the manifest/hash
  records.
- **Contextual relationships**: labeled as interpretive.
- **Conclusions**: separately labeled and bounded.
