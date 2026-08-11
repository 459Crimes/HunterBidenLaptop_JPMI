# Status

Updated: 2026-08-11

## Current state

`PUBLIC-PROVENANCE REWRITE IN REVIEW`

The repository has been reframed as a **standalone JPMI evidence repository for general readers**.

The public presentation no longer requires readers to understand APFS, GAI, 0728, or the project's larger forensic database before understanding the John Paul Mac Isaac copy.

## Completed in this rewrite

- [x] Defined JPMI in plain English as the John Paul Mac Isaac copy lineage.
- [x] Added the qualified **`dd`-style / whole-volume clone** explanation without claiming the literal `dd` command was proven.
- [x] Added Who / What / When / Where / Why / How provenance treatment.
- [x] Separated the original repair-shop computer from the later Crucial X6 custody medium.
- [x] Separated original user timestamps from the September 2019 HFS+ destination-creation event and later custody activity.
- [x] Reframed historical Mac hardware diagnostics as potentially migrated artifacts rather than automatic identification of the 2019 repair-shop machine.
- [x] Added a general-public explanation of GPT, EFI, HFS+, journals, CNIDs, hashes, Spotlight, `.DS_Store`, and timestamps.
- [x] Added a custody-gap section identifying the missing intermediate recovery/copy records.
- [x] Rewrote repository architecture and data contract around JPMI-only evidence.
- [x] Added a standalone reproducibility guide.

## Technical evidence already generated

| Area | State |
|---|---|
| JPMI path inventory | Generated |
| File-tree rollups | Generated |
| Timestamp distributions | Generated |
| HFS+ CNID and alias summaries | Generated |
| Disk and partition identity | Generated |
| HFS+ volume identity | Generated |
| Deep metadata archives | Generated |
| Size/checksum validation | Existing build previously passed |

## Work remaining before merge/publication

- [ ] Remove legacy cross-corpus comparison outputs from the public build.
- [ ] Update `scripts/20_export_hash_manifest.py` so future builds produce JPMI-only hash coverage.
- [ ] Update `scripts/50_build_reports.py` so regenerated reports preserve the public JPMI-only framing.
- [ ] Rewrite the five generated reports under `build/reports/`.
- [ ] Regenerate or update build section manifests/checksums after the public-output changes.
- [ ] Remove superseded comparison notes under `docs/notes/`.
- [ ] Run final search for references that require another evidence corpus to explain JPMI.
- [ ] Review wording of historical custody statements against source records before publication.

## Publication standard

A public JPMI claim should be traceable to one of:

1. the JPMI acquisition record;
2. the JPMI partition/volume record;
3. the JPMI file/timestamp/CNID/hash manifests;
4. an explicitly labeled public historical source.

Where the evidence does not establish an exact mechanism or actor, the repository should say so.
