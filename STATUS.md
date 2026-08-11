# Status

Updated: 2026-08-11

## Current state

`PUBLIC-PROVENANCE + 2019–2020 CUSTODY REWRITE COMPLETE — DATABASE-BACKED REBUILD PENDING`

The repository is now a **standalone JPMI evidence repository for general readers**. It combines JPMI's own disk/filesystem reporting with a separately sourced 2019–2020 custody history drawn from court opinions, contemporaneous reporting, participant accounts, and independent forensic review.

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
| Static build reports | Updated for review |
| Build manifests/checksums | **Require regeneration after latest report edits** |

## Validation still required in the project environment

The GitHub connector cannot execute the repository against the private/local `rhb_forensics` PostgreSQL database. Before merge/publication, run:

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

The final run should regenerate the reports and manifests from the canonical database, republish the sourced custody timeline at Stage 55, and let `90_validate_exports.py` regenerate/check all checksums.

## Publication standard

A public JPMI claim should be traceable to one of:

1. JPMI acquisition/disk/volume reporting;
2. JPMI path/timestamp/CNID/hash/system-state reporting;
3. a court opinion or incorporated pleading/document;
4. an explicitly attributed participant account;
5. an independently attributed forensic review;
6. a sourced public-record provenance connection.

Where the evidence does not establish an exact mechanism, physical-media identity, or actor, the repository should say so.
