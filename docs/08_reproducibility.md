# 8. Reproducibility

> **Encyclopedia.** [Architecture](../ARCHITECTURE.md) · [Data contract](../DATA_CONTRACT.md) · [Forensic image](FORENSIC_IMAGE.md) · [Index](INDEX.md). Historical claims are not generated from PostgreSQL; they live in `06` / `09` and the wiki articles.

The public narrative in this repository is backed by machine-readable JPMI tables **and a separately sourced historical custody record**.

The technical pipeline should rebuild the JPMI-derived summaries without using another laptop-data corpus. Historical custody events—court decisions, the FBI subpoena sequence, the New York Post publication date, and the independent CBS review—are maintained as cited public-source material rather than fabricated from filesystem timestamps.

## Evidence boundary

The pipeline reads JPMI-related tables in the project's forensic PostgreSQL database and writes derived artifacts under `build/`.

The restricted JPMI E01 image is not stored in GitHub.

The project therefore has two reproducible evidence layers:

1. **forensic-report layer** — database-derived paths, hashes, timestamps, CNIDs, disk/volume identity, and system-state records;
2. **historical-source layer** — sourced public custody chronology maintained in `docs/06_timeline_and_handling.md` and `docs/09_source_matrix.md`.

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
55_publish_custody_timeline.py
        |
        v
60_archive_deep_exports.py
        |
        v
90_validate_exports.py
```

### Stage 10 — file tree

Produces directory and user-home rollups from JPMI paths.

### Stage 20 — JPMI hash identities

Produces JPMI-only SHA-256 identity tables. Reported hashes are distinguished from hashes independently recomputed from restricted source bytes.

### Stage 30 — metadata

Produces timestamp, extension, type, permission, CNID, and alias summaries.

### Stage 40 — disk and volume identity

Produces acquisition, partition, disk, HFS+ volume, and filesystem-system-state summaries.

### Stage 50 — database-derived reports

Produces technical reports from the JPMI database.

These reports follow:

> **Observation → interpretation → limitation**

### Stage 55 — sourced public custody timeline

`55_publish_custody_timeline.py` publishes the sourced narrative in `docs/06_timeline_and_handling.md` into the legacy generated datetime-report location:

```text
build/reports/03_known_datetime_stamps_of_use.md
```

This stage exists so a database rebuild does **not** erase the sourced 2019–2020 custody history or revert to a filesystem-only timeline.

The underlying machine-readable timestamp data remains in:

- `build/metadata/01_time_distribution.tsv`;
- `build/reports/04_post_2019_03_31_timeline.md`.

Historical assertions in Stage 55 are not generated from PostgreSQL. They remain tied to the sources listed in `docs/09_source_matrix.md`.

### Stage 60 — deep metadata archives

Large detailed exports remain partitioned into GitHub-safe archive parts.

### Stage 90 — validation

The validator checks per-file limits, manifests, archive integrity, published checksums, and expected row counts.

## Reproduction commands

```bash
export RHB_PG_DSN="dbname=rhb_forensics"
python3 scripts/10_export_file_tree.py
python3 scripts/20_export_hash_manifest.py
python3 scripts/30_export_metadata.py
python3 scripts/40_export_volume_disk.py
python3 scripts/50_build_reports.py
python3 scripts/55_publish_custody_timeline.py
python3 scripts/60_archive_deep_exports.py
python3 scripts/90_validate_exports.py
```

## Claims that should be reproducible from JPMI reporting

| Public claim | Evidence artifact |
|---|---|
| Custody device is a Crucial X6 | `build/disk_info/01_acquisition.tsv` |
| E01 image name and acquisition hashes | `build/disk_info/01_acquisition.tsv` |
| JPMI source note identifies Todd Sanders | `build/disk_info/01_acquisition.tsv` |
| HFS+ volume name and identifier | `build/volume_info/01_volume_identity.tsv` |
| Sept. 26, 2019 HFS+ creation | `build/volume_info/01_volume_identity.tsv` |
| GPT/EFI/HFS+ partition layout | `build/disk_info/02_partition_map.tsv` |
| Home-folder populations | `build/file_tree/03_home_overview.tsv` |
| Overall user/system populations | `build/file_tree/02_top_level_summary.tsv` |
| Timestamp clusters | `build/metadata/01_time_distribution.tsv` |
| Oct. 15, 2020 Desktop `.DS_Store` modification | `build/reports/04_post_2019_03_31_timeline.md` / underlying file-time data |
| CNID population | `build/metadata/05_cnid_summary.tsv` |
| Alias/hard-link population | `build/metadata/06_alias_summary.tsv` |
| JPMI hash identities | `build/hash_manifest/01_sha256_by_cnid_*.tsv` |
| Later activity is dominated by system/application metadata | post-repair report + row set |

## Claims that require historical/public sources

The following should **not** be presented as if PostgreSQL itself proved them:

- three damaged laptops were presented April 12, 2019;
- the keyboard/unrecoverable-laptop sequence;
- Mac Isaac's store-server account;
- the father/FBI Albuquerque copy effort;
- the Dec. 9 FBI subpoena and Mac Isaac's retained exact copy;
- the Costello/Giuliani/New York Post chain;
- CBS's independent exact-copy forensic findings;
- Todd Sanders' external affiliation with the America Project.

Those claims are sourced in [`docs/09_source_matrix.md`](09_source_matrix.md).

## No-hacking finding: laptop media vs 0728

The repository attributes **no hacking** to JPMI or any other **laptop-derived** medium. That rests on two JPMI/CBS layers. **0728 Extra Found Files** is a separate collection (not from the laptop files per se) and is not examined here:

1. **JPMI reporting:** later changed rows are dominated by Finder/Spotlight/system/application metadata rather than a substantive later user-file population.
2. **Independent Mac Isaac/FBI-lineage examination:** CBS reported that Computer Forensics Services found no user-data modification/fabrication/tampering and no new files originating after April 2019 on the exact-copy dataset supplied by Mac Isaac's lawyer.

Those layers reinforce each other and remain separately attributed. Extra Found Files / 0728 is not a laptop filesystem copy.

## No source bytes: what reproducibility means here

A reproducible analysis of the received metadata can prove that analysts reach the same structural/timeline conclusions from the same reports.

It does **not** prove that this GitHub checkout independently re-read every source byte.

Without the restricted source image, the repository cannot freshly recompute every source-object hash or inspect every file's internal contents. It can still accurately reproduce the disk structure, file-tree populations, timestamps, catalog relationships, reported hashes, and system-state patterns contained in the forensic reporting.

That higher byte-level verification question depends on the original acquisition records and independent read-only access to the restricted source image.
