# 8. How to verify the published tables

> **Encyclopedia.** The articles are the entry point; the [evidence catalog](catalog/README.md) names the files behind them. [Forensic image](FORENSIC_IMAGE.md) · [Index](INDEX.md). Historical claims are cited public sources; they are not generated from filesystem timestamps.

This repository is a **metadata and hash witness**. A reader can check that the published tables match the checksums in this tree. A reader **cannot** re-open the restricted E01 from this GitHub checkout.

## Two evidence layers

1. **Forensic-report layer** — paths, hashes, timestamps, CNIDs, disk/volume identity, and system-state records, published under `build/` and listed in the catalogs.
2. **Historical-source layer** — court, news, and participant chronology in [Timeline and handling](06_timeline_and_handling.md) and [Source matrix](09_source_matrix.md).

## Checksums

| File | Role |
|---|---|
| [`build/manifest.tsv`](../build/manifest.tsv) | Path, size, SHA-256, and data-row count for every published `build/` object |
| [`build/manifest.sha256`](../build/manifest.sha256) | Same hashes in `sha256sum` form |
| Section `_manifest.json` files | Per-folder file list (disk, volume, file tree, hash, metadata) |
| [`build/archives/_manifest.tsv`](../build/archives/_manifest.tsv) | Deep-archive part sizes and hashes |

To verify a checkout, recompute SHA-256 of each path in `manifest.tsv` and compare.

## Claim → catalog

| Public claim | Catalog | File |
|---|---|---|
| Custody device is a Crucial X6 | [Disk identity](catalog/disk_info.md) | `01_acquisition.tsv` |
| E01 name and acquisition hashes | [Disk identity](catalog/disk_info.md) | `01_acquisition.tsv` |
| Sanders named on the rank-2 manifest | [Disk identity](catalog/disk_info.md) | `01_acquisition.tsv` |
| HFS+ `Untitled`, 26 Sep 2019 creation | [Volume identity](catalog/volume_info.md) | `01_volume_identity.tsv` |
| GPT / EFI / HFS+ layout | [Disk identity](catalog/disk_info.md) | `02_partition_map.tsv` |
| Home-folder populations | [File tree](catalog/file_tree.md) | `03_home_overview.tsv` |
| Top-level Users vs unallocated vs EFI | [File tree](catalog/file_tree.md) | `02_top_level_summary.tsv` |
| Timestamp clusters | [Metadata](catalog/metadata.md) | `01_time_distribution.tsv` |
| Oct. 15, 2020 Desktop `.DS_Store` | [Reports](catalog/reports.md) | `04_post_2019_03_31_timeline.md` |
| CNID / alias populations | [Metadata](catalog/metadata.md) | `05_cnid_summary.tsv`, `06_alias_summary.tsv` |
| Reported SHA-256 identities | [Hash manifest](catalog/hash_manifest.md) | `01_sha256_by_cnid_*.tsv` |
| Later activity is system/application metadata | [Reports](catalog/reports.md) | `04_post_2019_03_31_timeline.md` |

Row-level path/time/hash/CNID dumps: [Deep archives](catalog/archives.md).

## Claims that rest on historical sources

Court sequence, store-server account, father/FBI copy, Costello/Giuliani/*New York Post* chain, CBS findings, and Sanders' America Project affiliation are **not** filesystem derivations. They are sourced in [Source matrix](09_source_matrix.md).

## No-hacking finding: laptop media vs 0728

The repository attributes **no hacking** to JPMI or any other **laptop-derived** medium. That rests on JPMI post-repair rows plus CBS/CFS. **0728 Extra Found Files** is a separate collection and is not examined here. See [Integrity](INTEGRITY.md).

## What “reproducible” means without source bytes

Checking checksums and re-reading the published TSVs can show that two analysts reach the same structural and timeline conclusions from the same reports.

It does **not** prove this GitHub checkout independently re-read every source byte or recomputed every object hash. That depends on the original acquisition records and read-only access to the restricted image.
