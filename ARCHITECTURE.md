# Repository Architecture

## Purpose

This repository documents **JPMI — the John Paul Mac Isaac copy — as a standalone evidence source**.

The architecture has four layers:

1. **Public encyclopedia** — Wikipedia-style articles (lead, infobox, hatnotes, source classes) so a technically literate stranger can find *any* fact about this disk lineage without already knowing the numbered tutorial order.
2. **Historical source record** — maintain court/news/participant sources for the 2019–2020 custody story separately from filesystem-derived facts.
3. **Machine-readable JPMI evidence** — publish the inventories and summaries that support the technical narrative.
4. **Reproducibility pipeline** — regenerate and validate the technical artifacts and republish the sourced custody timeline.

No comparative laptop-data corpus is required to explain JPMI.

## Layer 1 — public encyclopedia

The recommended entry points are [`README.md`](README.md) (main article) and [`docs/INDEX.md`](docs/INDEX.md) (all pages).

Numbered files `docs/01`–`09` remain the **stable narrative IDs** (Stage 55 still republishes `06`). Companion articles cover people, hardware, copy lineages, timestamps, integrity, and glossary without renaming those IDs.

| Document | Purpose |
|---|---|
| `README.md` | Main article: infobox, lead finding, timeline digest, portal |
| `docs/INDEX.md` | Article index / categories |
| `docs/MANUAL_OF_STYLE.md` | Evidence classes and banned overclaims |
| `docs/GLOSSARY.md` | Terms of art |
| `docs/PEOPLE.md` / `THE_MAC_SHOP.md` | Actors and the April 2019 recovery |
| `docs/COPY_LINEAGES.md` / `MAILING_PACKET.md` | Devices vs copies vs this GitHub tree |
| `docs/CRUCIAL_X6.md` / `HFS_VOLUME_UNTITLED.md` / `FORENSIC_IMAGE.md` | Storage objects |
| `docs/CONTENTS_CENSUS.md` / `TIMESTAMPS.md` / `INTEGRITY.md` | Populations, time, tampering |
| `docs/2022_2024_DISCREPANCY.md` | Later report-lineage collision |
| `docs/SCOPE.md` / `BIBLIOGRAPHY.md` | Boundary and sources |
| `docs/TIMELINE.md` | Compact event index into `06` |
| `01_what_is_jpmi.md` | Define the evidence source and qualified `dd`-style analogy |
| `02_provenance_5ws.md` | Who, What, When, Where, Why, and How |
| `03_chain_of_custody.md` | April repair, FBI-copy lineage, Costello/New York Post route, Todd Sanders delivery bridge |
| `04_what_is_on_the_copy.md` | Explain user, application, media, and filesystem populations |
| `05_filesystem_for_non_experts.md` | Explain GPT, EFI, HFS+, CNIDs, journals, Spotlight, hashes, and timestamps |
| `06_timeline_and_handling.md` | Sourced 2019–2020 timeline interwoven with JPMI timestamps |
| `07_limits_and_open_questions.md` | State evidentiary boundaries, no-injection finding, and missing records |
| `08_reproducibility.md` | Map technical claims back to build artifacts and scripts |
| `09_source_matrix.md` | Identify which legal/news/forensic source supports each historical custody claim |

The narrative rule is:

> **Observed fact → interpretation → limitation**

## Layer 2 — historical source record

Historical custody assertions are **not generated from PostgreSQL**.

The principal sources are maintained in `docs/09_source_matrix.md` and include:

- Delaware Supreme Court and Superior Court opinions;
- the earlier S.D. Florida opinion reciting the Mac Isaac timeline;
- the December 2019 FBI subpoena sequence;
- Mac Isaac's later store-server/FBI-copy account;
- the October 14, 2020 New York Post publication event;
- CBS's 2022 independent examination of an exact-copy Mac Isaac/FBI-lineage dataset;
- public-record evidence connecting Todd Sanders to Patrick Byrne's America Project.

This separation prevents a participant recollection or news report from being presented as if it were a filesystem-derived fact.

## Layer 3 — machine-readable JPMI evidence

The `build/` directory contains derived artifacts.

### `build/disk_info/`

Records the later custody device and forensic image, including the internal source note attributing the rank-2 manifest to Todd Sanders.

### `build/volume_info/`

Records the HFS+ destination, including the reported **September 26, 2019** creation event and later system-state metadata.

### `build/file_tree/`

Records the JPMI path hierarchy and `Users/roberthunter` rollups.

### `build/hash_manifest/`

Records **JPMI-only** object identity and coverage. Hashes are received manifest evidence unless explicitly recomputed from restricted source bytes.

### `build/metadata/`

Records created/modified/accessed distributions, extensions, types, permissions, CNID metrics, and alias/hard-link metrics.

### `build/reports/`

Human-readable technical summaries. `03_known_datetime_stamps_of_use.md` is republished after Stage 50 from the sourced custody timeline so a rebuild does not erase the historical narrative.

### `build/archives/`

Partitioned archives of large JPMI metadata exports.

## Layer 4 — reproducibility pipeline

### Canonical technical inputs

| Table / input | Role |
|---|---|
| `jpmi_acquisition` | custody device, image, disk and volume identity |
| `files` for the JPMI source | normalized path inventory |
| `jpmi_file_times` | created / modified / accessed timestamps |
| `jpmi_sha256_allpaths` | reported SHA-256 values by JPMI path |
| `jpmi_cnid_map` | HFS+ catalog identity and parent hierarchy |
| `jpmi_alias_map` | canonical/alias and hard-link relationships |
| `jpmi_tsk_timeline` | filesystem timeline and system-state events |

The raw JPMI E01 is not published here.

### Pipeline stages

1. `10_export_file_tree.py` — build JPMI hierarchy and directory rollups.
2. `20_export_hash_manifest.py` — build JPMI-only SHA-256 identity and coverage outputs.
3. `30_export_metadata.py` — build timestamp, extension, type, permission, CNID, and alias summaries.
4. `40_export_volume_disk.py` — build disk, partition, and HFS+ volume identity outputs.
5. `50_build_reports.py` — generate database-derived JPMI reports.
6. `55_publish_custody_timeline.py` — publish the sourced 2019–2020 custody narrative into the legacy datetime-report location.
7. `60_archive_deep_exports.py` — archive large deep JPMI metadata exports.
8. `90_validate_exports.py` — validate file sizes, section manifests, archive parts, and checksums.

## Integrity and provenance rules

- The Crucial X6 is a later custody device, not automatically the original laptop SSD.
- “`dd`-style” is an explanatory analogy, not proof that `dd` was literally used.
- Mac Isaac's store-server step is attributed to his account until server logs are produced.
- The September 26, 2019 HFS+ creation date is chronologically consistent with his described preservation/FBI-copy period, but does not by itself identify the exact physical FBI-intended drive.
- The Delaware Supreme Court's recitation that Mac Isaac made an **exact copy before the December 9, 2019 FBI surrender** is the strongest public anchor for the direct-copy lineage.
- Later `.DS_Store`, Spotlight, DocumentRevisions, and software-scale access activity is custody/system-state evidence, not automatically evidence of substantive document injection.
- **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.** Non-laptop provenance is **0728 Extra Found Files** only (out of scope here).
- CBS's separate exact-copy Mac Isaac/FBI-lineage review is corroborating external forensic evidence and remains separately attributed.
- The JPMI acquisition note identifying Todd Sanders, combined with public evidence of his America Project affiliation, supports a Mac Isaac-centered provenance-network inference but not yet physical identity with CBS's media.
- Historical hardware diagnostics may be migrated data and should not automatically identify the 2019 repair-shop machine.
- Reported hashes remain manifest evidence unless recomputed from source bytes.

## Source-byte boundary

The public repository does not contain the individual JPMI source-file bytes.

It can reproduce accurate structural/timeline/provenance analysis from the forensic reports—paths, timestamps, CNIDs, aliases, partition/volume identity, reported hashes, and system-state records—but cannot independently open every source object or recompute every source hash.

## Publication boundary

This repository intentionally does **not** present comparative laptop-dataset analysis.

Questions involving relationships between JPMI and other datasets belong in a separate comparative project. This repository asks one question: **what does the Mac Isaac direct-copy lineage itself show?**
