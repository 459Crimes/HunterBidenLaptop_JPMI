# Catalog: volume identity

> HFS+ volume `Untitled` and selected filesystem/system-state objects. Articles: [HFS+ volume Untitled](../HFS_VOLUME_UNTITLED.md) · [Filesystem for non-experts](../05_filesystem_for_non_experts.md). Parent: [Evidence catalog](README.md).

Folder: [`build/volume_info/`](../../build/volume_info/) · [`_manifest.json`](../../build/volume_info/_manifest.json)

The source inventory that produced these rollups has **576,249** path rows.

| File | Rows | Size | Notes |
|---|---:|---:|---|
| [`01_volume_identity.tsv`](../../build/volume_info/01_volume_identity.tsv) | 15 | 436 B | Name `Untitled`, id `dfe8079582e21400`, journaled HFS+, create **2019-09-26**, last-write **2024-11-21**, ~280 GB unallocated, journal ~40 MB |
| [`02_volume_metadata.tsv`](../../build/volume_info/02_volume_metadata.tsv) | 116 | 17 KB | Journal, Spotlight stores, DocumentRevisions, `.DS_Store`, GPT-related objects |
| [`03_volume_system_state.tsv`](../../build/volume_info/03_volume_system_state.tsv) | 20 | 1.3 KB | Category rollups (mail, photos, Dr.Fone tooling, Spotlight, …) — **not** 1:1 with home-folder rows |

## Columns

**Identity:** `field`, `value`.

**Volume metadata:** `object`, `size_bytes`, `modified_ts`, `note`.

**System state:** `system_area`, `object_count`, `size_bytes`, `note`.

## How this relates to file counts

[`03_volume_system_state.tsv`](../../build/volume_info/03_volume_system_state.tsv) uses **category rules**. Home-folder counts live in the [file-tree catalog](file_tree.md). Do not add the two tables together.

The 2024 last-write on the volume is a [report-lineage issue](../2022_2024_DISCREPANCY.md), not a user-authorship date.
