# 8. Reproducibility

The public narrative in this repository is backed by machine-readable JPMI tables.

The technical pipeline should be able to rebuild the published summaries without using any other laptop-data source.

## Evidence boundary

The pipeline reads the JPMI-related tables in the project's forensic PostgreSQL database and writes derived artifacts under `build/`.

The published repository requires **JPMI evidence only** to explain and reproduce its JPMI analysis.

The restricted JPMI E01 image is not stored in GitHub.

## Core JPMI tables

| Table | Role |
|---|---|
| `jpmi_acquisition` | Custody device, E01 identity, partition and volume identity |
| `files` for the JPMI source | Normalized path inventory |
| `jpmi_file_times` | Created / modified / accessed timestamps |
| `jpmi_sha256_allpaths` | Reported SHA-256 values and paths |
| `jpmi_cnid_map` | HFS+ catalog identity and parent relationships |
| `jpmi_alias_map` | Canonical/alias and hard-link relationships |
| `jpmi_tsk_timeline` | TSK filesystem timeline and system-state events |

Comparative overlap tables are outside the scope of this standalone JPMI publication.

## Build stages

```text
10_export_file_tree.py
        |
        v
20_export_hash_manifest.py
        |
        v
30_export_metadata.py
        |
        v
40_export_volume_disk.py
        |
        v
50_build_reports.py
        |
        v
60_archive_deep_exports.py
        |
        v
90_validate_exports.py
```

### Stage 10 — file tree

Produces directory and user-home rollups from JPMI paths.

Key outputs:

- `build/file_tree/01_directory_tree.tsv`
- `build/file_tree/02_top_level_summary.tsv`
- `build/file_tree/03_home_overview.tsv`

### Stage 20 — JPMI hash identities

Produces JPMI-only SHA-256 identity tables.

The public build should answer:

- how many paths have reported hashes;
- how many distinct hashes are represented;
- how many CNIDs have hashes;
- which canonical path is associated with a CNID;
- how aliases/hard links affect path counts.

It should not require a match against another corpus to establish JPMI's own inventory.

### Stage 30 — metadata

Produces:

- timestamp distributions;
- extension distributions;
- type distributions;
- permission distributions;
- CNID summaries;
- alias summaries.

### Stage 40 — disk and volume identity

Produces:

- acquisition record;
- partition map;
- disk identity;
- HFS+ volume identity;
- filesystem-system-state summaries.

### Stage 50 — human-readable reports

Produces the human-readable forensic reports in `build/reports/`.

These reports should follow the same rule as the public docs:

> **Observation → interpretation → limitation**

No report should rely on another dataset to explain what JPMI is.

### Stage 60 — deep metadata archives

Large detailed exports remain partitioned into GitHub-safe archive parts.

These are reproducibility artifacts, not the recommended starting point for a general reader.

### Stage 90 — validation

The validator checks:

- per-file size limits;
- section manifests;
- archive-part integrity;
- published artifact checksums;
- expected row counts.

## Reproduction commands

```bash
export RHB_PG_DSN="dbname=rhb_forensics"
python3 scripts/10_export_file_tree.py
python3 scripts/20_export_hash_manifest.py
python3 scripts/30_export_metadata.py
python3 scripts/40_export_volume_disk.py
python3 scripts/50_build_reports.py
python3 scripts/60_archive_deep_exports.py
python3 scripts/90_validate_exports.py
```

## What should be reproducible from the public repository

A reviewer should be able to trace public claims to specific evidence tables.

Examples:

| Public claim | Evidence artifact |
|---|---|
| Custody device is a Crucial X6 | `build/disk_info/01_acquisition.tsv` |
| E01 image name and acquisition hashes | `build/disk_info/01_acquisition.tsv` |
| HFS+ volume name and identifier | `build/volume_info/01_volume_identity.tsv` |
| Volume creation and last-write dates | `build/volume_info/01_volume_identity.tsv` |
| GPT/EFI/HFS+ partition layout | `build/disk_info/02_partition_map.tsv` |
| Home-folder populations | `build/file_tree/03_home_overview.tsv` |
| Overall user/system row populations | `build/file_tree/02_top_level_summary.tsv` |
| Timestamp clusters | `build/metadata/01_time_distribution.tsv` and reports |
| CNID population | `build/metadata/05_cnid_summary.tsv` |
| Alias/hard-link population | `build/metadata/06_alias_summary.tsv` |
| JPMI hash identities | `build/hash_manifest/01_sha256_by_cnid_*.tsv` |

## Reproducibility does not eliminate provenance limits

A perfectly reproducible analysis of received metadata can prove that analysts reached the same result from the same metadata.

It does **not** automatically prove that the received metadata perfectly represents every byte of the original repair-shop storage.

That higher-level question depends on the custody chain, the original acquisition records, and—ideally—independent read-only access to the restricted source image.
