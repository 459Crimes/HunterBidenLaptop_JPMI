# Status

Updated: 2026-08-12

## Current state

`PUBLIC JPMI PROVENANCE REWRITE VALIDATED — READY FOR MERGE`

The repository is a **standalone JPMI evidence repository for general readers**. It combines JPMI's own disk/filesystem reporting with a separately sourced 2019–2020 custody history drawn from court opinions, contemporaneous reporting, participant accounts, and independent forensic review. The full pipeline was regenerated from the canonical `rhb_forensics` database and passed the local validation gate.

## Completed in this rewrite

- [x] Defined JPMI in plain English as the John Paul Mac Isaac direct-copy lineage.
- [x] Added the qualified **`dd`-style / whole-volume clone** explanation without claiming the literal `dd` command was proven.
- [x] Added Who / What / When / Where / Why / How provenance treatment.
- [x] Added the April 2019 **three-laptop / keyboard / unrecoverable-laptop / external-hard-drive** sequence from the Delaware court record.
- [x] Added Mac Isaac's later account that recoverable data was first staged on his **store server**, clearly labeled as his account because the server logs are not presently available here.
- [x] Added the September–October 2019 father/FBI preservation-copy chronology.
- [x] Identified the JPMI **September 26, 2019 HFS+ creation date** as chronologically consistent with that preservation-copy period while explicitly stopping short of claiming physical-device identity.
- [x] Added the **December 9, 2019 FBI subpoena** and the Delaware Supreme Court's recitation that Mac Isaac made an **exact copy before surrendering the original**.
- [x] Added the August 2020 Costello transfer, October 14 New York Post publication, and October 15 JPMI Desktop `.DS_Store` modification.
- [x] Explained the October 15 `.DS_Store` event as evidence consistent with Finder opening/browsing, **not substantive-file injection**.
- [x] Added CBS News' independent examination of an exact-copy Mac Isaac/FBI-lineage dataset and its reported findings of **no user-data modification/fabrication/tampering and no new files originating after April 2019**.
- [x] Added the internal JPMI source note identifying **Todd Sanders** and a sourced provenance bridge to his public affiliation with Patrick Byrne's **America Project**.
- [x] Bounded that bridge correctly: same Mac Isaac-centered provenance network is supported; literal identity of the CBS media and JPMI physical/image media is **not yet established**.
- [x] Added `docs/09_source_matrix.md` separating court-recited facts, participant accounts, JPMI-internal findings, and independent forensic results.
- [x] Added repeated, bounded integrity language: **no evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting**.
- [x] Expanded the explanation that the public repository lacks individual source-file bytes but contains enough disk/filesystem/hash/timestamp/CNID/system-state reporting for accurate, reproducible structural and provenance analysis.
- [x] Added `scripts/55_publish_custody_timeline.py` so a future database rebuild republishes the sourced custody narrative after the database-derived report stage.
- [x] Preserved the separate reported 2022 E01 / 2024 HFS+ last-write chronology discrepancy as an unresolved later report-lineage issue rather than making it the center of the 2019–2020 story.

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
