# Status

Updated: 2026-08-15

## Current state

`PUBLIC JPMI ENCYCLOPEDIA — WIKI LAYER ADDED ON VALIDATED PROVENANCE`

The repository is a **standalone JPMI evidence encyclopedia**. The 2026-08-12 database-backed rewrite remains the evidentiary baseline. The 2026-08-15 work reorganizes that material so the Git tree reads like a technically literate Wikipedia: main-article lead and infobox, article index, hatnotes, people/hardware/lineage/timestamp/integrity companions, and the same bounded integrity language.

Entry points: [`README.md`](README.md), [`docs/INDEX.md`](docs/INDEX.md).

## Completed in this rewrite

- [x] Defined JPMI in plain English as the John Paul Mac Isaac direct-copy lineage.
- [x] Added the qualified **`dd`-style / whole-volume clone** explanation without claiming the literal `dd` command was proven.
- [x] Added Who / What / When / Where / Why / How provenance treatment.
- [x] Added the April 2019 **three-laptop / keyboard / unrecoverable-laptop / external-hard-drive** sequence from the Delaware court record.
- [x] Added Mac Isaac's account that recoverable data was first staged on his **store server**, accepted by this project as the operative account and labeled as such, with the note that server logs are not presently available for independent verification.
- [x] Added the September–October 2019 father/FBI preservation-copy chronology.
- [x] Identified the JPMI **September 26, 2019 HFS+ creation date** as chronologically consistent with that preservation-copy period while explicitly stopping short of claiming physical-device identity.
- [x] Added the **December 9, 2019 FBI subpoena** and the Delaware Supreme Court's recitation that Mac Isaac made an **exact copy before surrendering the original**.
- [x] Added the August 2020 Costello transfer, October 14 New York Post publication, and October 15 JPMI Desktop `.DS_Store` modification.
- [x] Explained the October 15 `.DS_Store` event as evidence consistent with Finder opening/browsing, **not substantive-file injection**.
- [x] Added CBS News' independent examination of an exact-copy Mac Isaac/FBI-lineage dataset and its reported findings of **no user-data modification/fabrication/tampering and no new files originating after April 2019**.
- [x] Added the internal JPMI source note identifying **Todd Sanders** and the **direct transfer record**: Sanders received the drive copy directly from Brian Della Rocca, documented by the mailing-packet photograph (`photo_20260716_120324.jpg`, Mac Isaac home address as sender, Sanders as recipient).
- [x] Recorded the source-derived assumption that the JPMI media is **byte-identical or virtually byte-identical** to the CBS-examined copy (same attorney, same purpose), explicitly noting that no independent side-by-side hash comparison has been published.
- [x] Recorded Todd Sanders' participant account of the 2022/2024 discrepancy — any alteration occurred during analysis, probably a read-write mount on a Mac — labeled as unverified, with only the FBI able to verify.
- [x] Added the open FBI-side questions: why the original laptop/external drive have not been returned to anyone, and how many copies were made in the preservation-copy period.
- [x] Added `docs/09_source_matrix.md` separating court-recited facts, participant accounts, JPMI-internal findings, and independent forensic results.
- [x] Added repeated, bounded integrity language: **no evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting**.
- [x] Expanded the explanation that the public repository lacks individual source-file bytes but contains enough disk/filesystem/hash/timestamp/CNID/system-state reporting for accurate, reproducible structural and provenance analysis.
- [x] Added `scripts/55_publish_custody_timeline.py` so a future database rebuild republishes the sourced custody narrative after the database-derived report stage.
- [x] Preserved the separate reported 2022 E01 / 2024 HFS+ last-write chronology discrepancy as an unresolved later report-lineage issue rather than making it the center of the 2019–2020 story.
- [x] Reorganized the public Git tree as an encyclopedia (2026-08-15): `README` main article + infobox; `docs/INDEX.md`; Manual of Style; glossary; people; Mac Shop; copy lineages; Crucial X6; HFS+ `Untitled`; forensic image; mailing packet; contents census; timestamps; integrity; 2022/2024 discrepancy; scope; bibliography; compact timeline index. Numbered `01`–`09` IDs retained (Stage 55 still publishes `06`).

## Technical evidence in the branch

| Area | State |
|---|---|
| JPMI path inventory | Generated |
| File-tree rollups | Generated |
| Timestamp distributions | Generated |
| HFS+ CNID and alias summaries | Generated |
| Disk and partition identity | Generated |
| HFS+ volume identity | Generated |
| JPMI-only hash identity/coverage | Published |
| Deep metadata archives | Preserved |
| Public 2019–2020 custody narrative | Expanded and sourced |
| Source-claim matrix | Added |
| Static build reports | Regenerated from canonical database |
| Build manifests/checksums | Refreshed and verified (`sha256sum -c` clean) |

## Project-environment validation

Completed 2026-08-12 against the canonical `rhb_forensics` PostgreSQL database:

```bash
python3 scripts/10_export_file_tree.py
python3 scripts/20_export_hash_manifest.py
python3 scripts/30_export_metadata.py
python3 scripts/40_export_volume_disk.py
python3 scripts/50_build_reports.py
python3 scripts/55_publish_custody_timeline.py
python3 scripts/60_archive_deep_exports.py
python3 scripts/90_validate_exports.py
```

- [x] Complete pipeline run, read-only against `rhb_forensics`.
- [x] Stage 55 republished the sourced 2019–2020 custody timeline into `build/reports/03_known_datetime_stamps_of_use.md`.
- [x] Stage 90 passed clean: 35 files validated, all within caps, all section manifests and archive parts consistent.
- [x] Regenerated reports retain the bounded no-hacking/no-injection language.
- [x] Manifests/checksums refreshed; `build/manifest.sha256` verified with `sha256sum -c`.
- [x] JPMI-only scope confirmed: no cross-corpus comparison outputs generated or present.
- [x] Deterministic deep-export ordering fixed in `scripts/10_export_file_tree.py` (`ORDER BY relative_path`) so regenerated archives are byte-stable.

The regenerated counts match the canonical tables: 576,249 normalized inventory paths; 655,330 rank-1 hash-manifest paths; 397,440 CNID-map entries; 1,259,300 TSK timeline rows.

## Publication standard

A public JPMI claim should be traceable to one of:

1. JPMI acquisition/disk/volume reporting;
2. JPMI path/timestamp/CNID/hash/system-state reporting;
3. a court opinion or incorporated pleading/document;
4. an explicitly attributed participant account;
5. an independently attributed forensic review;
6. a sourced public-record provenance connection.

Where the evidence does not establish an exact mechanism, physical-media identity, or actor, the repository should say so.
