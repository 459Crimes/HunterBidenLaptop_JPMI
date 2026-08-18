# Catalog: metadata summaries

> Timestamp, extension, type, permission, CNID, and alias rollups. Articles: [Timestamps](../TIMESTAMPS.md) · [Copy method](../COPY_METHOD.md) · [Glossary](../GLOSSARY.md). Parent: [Evidence catalog](README.md).

Folder: [`build/metadata/`](../../build/metadata/) · [`_manifest.json`](../../build/metadata/_manifest.json)

| File | Rows | Size | Notes |
|---|---:|---:|---|
| [`01_time_distribution.tsv`](../../build/metadata/01_time_distribution.tsv) | 51 | 1.7 KB | Created / modified / accessed by year and selected year-month |
| [`02_extension_distribution.tsv`](../../build/metadata/02_extension_distribution.tsv) | 1,702 | 63 KB | Extension census (`.emlx` vs `.emlx-slack` are separate lines) |
| [`03_type_distribution.tsv`](../../build/metadata/03_type_distribution.tsv) | 5 | 90 B | Coarse type buckets |
| [`04_permission_distribution.tsv`](../../build/metadata/04_permission_distribution.tsv) | 19 | 466 B | POSIX mode strings |
| [`05_cnid_summary.tsv`](../../build/metadata/05_cnid_summary.tsv) | 9 | 164 B | Catalog/CNID metrics (397,440 CNIDs in the articles) |
| [`06_alias_summary.tsv`](../../build/metadata/06_alias_summary.tsv) | 7 | 161 B | Canonical vs alias path metrics; two-path CNIDs are file + slack |

## Columns

**Time:** `event_type` (`created` / `modified` / `accessed`), `bucket`, `row_count`, `size_bytes`.

**Extension:** `extension`, `file_count`, `size_bytes`, `hash_count`.

**Type / permissions:** `file_type` or `permissions`, `file_count`, `size_bytes`.

**CNID / alias summaries:** `metric`, `value`.

## Counts cited in the articles

| Figure | File |
|---|---|
| Created 2017: 107,817 · 2018: 107,185 · Jan–Mar 2019 heavy; September 2019: 15 | time distribution |
| Post-repair **modified** activity is sparse (see reports catalog) | time distribution + [post-repair report](reports.md) |
| `.emlx` vs `.emlx-slack` split (do not sum only the unsuffixed line) | extension distribution |
| Alias `max_paths_for_cnid` = 2, all slack pairs | alias summary |

Timezone labels differ across report families. Read [Timestamps](../TIMESTAMPS.md) before treating a three-hour offset as a story.
