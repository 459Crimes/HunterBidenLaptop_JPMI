# Data Contract

All published tables in this repository describe **JPMI only**.

TSV files are UTF-8, LF-terminated, tab-separated, and contain a header row. Shards of the same logical export use identical columns.

Timestamp fields preserve the convention supplied by the originating forensic report except where a file states that normalization has been applied. Timestamps from different report families are not interchangeable as if every field used the same timezone.

## `build/file_tree/`

### `01_directory_tree.tsv`

Columns:

`path`, `depth`, `parent_path`, `dir_count`, `file_count`, `size_bytes`, `hash_count`, `hash_pct`, `min_modified_ts`, `max_modified_ts`

One row per directory represented in the JPMI inventory tree. Immediate-child directory/file counts and size/hash coverage are rolled up from the JPMI path inventory.

### `02_top_level_summary.tsv`

Columns:

`top_path`, `file_count`, `size_bytes`, `hash_count`, `hash_pct`, `min_modified_ts`, `max_modified_ts`

Top-level rollup for the user tree and disk/filesystem structural areas.

### `03_home_overview.tsv`

Columns:

`home_subdir`, `file_count`, `size_bytes`, `hash_count`, `hash_pct`, `min_modified_ts`, `max_modified_ts`

Rollup for direct children of `JPMI://Users/roberthunter`.

## `build/hash_manifest/`

### `01_sha256_by_cnid_*.tsv`

Columns:

`cnid`, `size`, `alloc`, `n_paths`, `sha256`, `canonical_path`

One row per represented JPMI CNID with a reported SHA-256 identity. The canonical path is selected from the JPMI alias map.

### `04_coverage.tsv`

Columns:

`metric`, `value`

JPMI-only coverage metrics, including:

- total reported hash-manifest paths;
- paths with SHA-256;
- distinct hashed CNIDs;
- distinct SHA-256 values;
- alias-map row count;
- canonical hashed-CNID export row count.

The public JPMI repository does not publish cross-corpus match tables.

## `build/metadata/`

### `01_time_distribution.tsv`

Columns:

`event_type`, `bucket`, `row_count`, `size_bytes`

`event_type` is `created`, `modified`, or `accessed`. Buckets are year and selected year-month values.

### `02_extension_distribution.tsv`

Columns:

`extension`, `file_count`, `size_bytes`, `hash_count`

### `03_type_distribution.tsv`

Columns:

`file_type`, `file_count`, `size_bytes`

### `04_permission_distribution.tsv`

Columns:

`permissions`, `file_count`, `size_bytes`

### `05_cnid_summary.tsv`

Columns:

`metric`, `value`

HFS+ catalog/CNID metrics from `jpmi_cnid_map`.

### `06_alias_summary.tsv`

Columns:

`metric`, `value`

Canonical/alias path metrics from `jpmi_alias_map`. Two-path CNIDs in the current table are TSK file + `*-slack`, not Unix hard links. See [COPY_METHOD](docs/COPY_METHOD.md).

## `build/volume_info/`

### `01_volume_identity.tsv`

Columns:

`field`, `value`

Contains the reported JPMI destination-volume identity, including volume name, identifier, filesystem type, HFS+ sector offset, source-image name, image size, volume-creation date, volume last-write date, deleted-catalog status, unallocated-range estimate, and journal size.

### `02_volume_metadata.tsv`

Columns:

`object`, `size_bytes`, `modified_ts`, `note`

Selected filesystem/system metadata objects, including HFS+ journal state, Spotlight, DocumentRevisions, `.DS_Store`, and GPT-related records.

### `03_volume_system_state.tsv`

Columns:

`system_area`, `object_count`, `size_bytes`, `note`

Rollups for filesystem and application/system-state areas represented by JPMI.

## `build/disk_info/`

### `01_acquisition.tsv`

Columns:

`field`, `value`

Verbatim normalized fields from the JPMI acquisition record, including device model/serial, image identity, acquisition hashes, image size, sector geometry, case number, tool version, partition identifiers, and volume identifier.

### `02_partition_map.tsv`

Columns:

`partition`, `type`, `guid`, `byte_start`, `byte_length`, `note`

GPT/EFI/HFS+ partition identity for the later JPMI custody medium.

### `03_disk_identity.tsv`

Columns:

`field`, `value`

Consolidated device, disk, partition, and volume identity.

## `build/reports/`

Markdown reports are generated from JPMI evidence only.

Every report separates:

1. **Observation** — what the JPMI record directly reports.
2. **Interpretation** — what that observation is consistent with or supports.
3. **Limitation** — what the observation does not establish by itself.

## `build/archives/`

Deep metadata exports are partitioned into deterministic archive parts when they exceed repository file-size limits.

Archive parts are derived JPMI metadata. They are not source-image bytes.

## Evidence terminology

The following terms are not interchangeable:

- **path** — a represented filesystem location, published as a source URI (`JPMI://…`; likewise `APFS://`, `GAI://`, `0728://` for those copies);
- **CNID** — an HFS+ catalog identity;
- **hash** — reported byte-content fingerprint;
- **device** — a physical custody medium;
- **image** — a forensic representation of a device;
- **volume** — a filesystem instance inside the device/image;
- **timestamp** — a field whose meaning depends on event type and copy history.

The repository keeps these dimensions separate so that provenance conclusions remain auditable.
