# Status

Updated: 2026-08-11

## Current state

`PUBLIC-PROVENANCE REWRITE COMPLETE — DATABASE-BACKED REBUILD PENDING`

The repository has been reframed as a **standalone JPMI evidence repository for general readers**. The public presentation explains the John Paul Mac Isaac copy from its own acquisition, disk, volume, filesystem, path, timestamp, CNID, and hash evidence.

## Completed in this rewrite

- [x] Defined JPMI in plain English as the John Paul Mac Isaac copy lineage.
- [x] Added the qualified **`dd`-style / whole-volume clone** explanation without claiming the literal `dd` command was proven.
- [x] Added Who / What / When / Where / Why / How provenance treatment.
- [x] Separated the original repair-shop computer from the later Crucial X6 custody medium.
- [x] Separated original user timestamps from the September 2019 HFS+ destination-creation event.
- [x] Flagged the reported **2022 E01 acquisition versus 2024 HFS+ last-write** as an unresolved source-chronology discrepancy.
- [x] Reframed historical Mac hardware diagnostics as potentially migrated artifacts rather than automatic identification of the 2019 repair-shop machine.
- [x] Added a general-public explanation of GPT, EFI, HFS+, journals, CNIDs, hashes, Spotlight, `.DS_Store`, and timestamps.
- [x] Added a custody-gap section identifying missing intermediate recovery/copy records.
- [x] Rewrote repository architecture and data contract around JPMI-only evidence.
- [x] Added a standalone reproducibility guide.
- [x] Removed public comparison hash exports and superseded comparison notes.
- [x] Rewrote the hash generator to produce JPMI-only identity/coverage outputs.
- [x] Rewrote the report generator so future reports use standalone JPMI framing.
- [x] Reworked generated reports that previously depended on comparison evidence or over-attributed historical hardware diagnostics.
- [x] Refreshed the hash-section manifest, top-level build manifest, and `manifest.sha256` for the branch's public artifact set.

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
| Public narrative | Rewritten |
| Static build manifests/checksums | Refreshed |

## Validation still required in the project environment

The GitHub connector cannot execute the repository against the private/local `rhb_forensics` PostgreSQL database. Before merge/publication, run the normal pipeline in the project environment:

```bash
python3 scripts/10_export_file_tree.py
python3 scripts/20_export_hash_manifest.py
python3 scripts/30_export_metadata.py
python3 scripts/40_export_volume_disk.py
python3 scripts/50_build_reports.py
python3 scripts/60_archive_deep_exports.py
python3 scripts/90_validate_exports.py
```

The purpose of that final run is to verify that the regenerated artifacts reproduce the branch's static JPMI-only structure and to let `90_validate_exports.py` regenerate/check the manifests from the canonical database.

## Publication standard

A public JPMI claim should be traceable to one of:

1. the JPMI acquisition record;
2. the JPMI partition/volume record;
3. the JPMI file/timestamp/CNID/hash manifests;
4. an explicitly labeled historical source used only for custody context.

Where the evidence does not establish an exact mechanism, date relationship, or actor, the repository should say so.
