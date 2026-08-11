# JPMI Publication Tasks and Gates

## Public narrative

- [x] Define JPMI without assuming digital-forensics knowledge.
- [x] Explain the qualified `dd`-style / whole-volume clone analogy.
- [x] Spell out Who / What / When / Where / Why / How.
- [x] Add the April 2019 three-laptop / keyboard / external-hard-drive recovery sequence.
- [x] Add Mac Isaac's store-server account with attribution and evidence boundary.
- [x] Add the September–October 2019 father/FBI preservation-copy chronology.
- [x] Correlate the September 26, 2019 JPMI HFS+ creation date with that period without overstating physical identity.
- [x] Add the December 9 FBI subpoena and retained exact-copy event.
- [x] Add the August 2020 Costello transfer and October 14 New York Post publication.
- [x] Explain the October 15, 2020 Desktop `.DS_Store` modification as browsing/Finder evidence, not substantive-file injection.
- [x] Add CBS's independent exact-copy Mac Isaac/FBI-lineage forensic findings.
- [x] Add the Todd Sanders / America Project source-delivery provenance bridge with the correct same-network/not-yet-same-media limitation.
- [x] Repeatedly state the bounded integrity conclusion: no evidence of post-dropoff hacking or external substantive-file injection has been identified in JPMI reporting.
- [x] Explain why report-level metadata/hash evidence remains sufficient for accurate structural/timeline/provenance analysis despite the absence of public source-file bytes.
- [x] Add a claim/source matrix.
- [x] Keep post-2020 discussion limited mainly to evidence that the direct-copy lineage was opened, analyzed, indexed, and used for forensic reporting.

## Technical publication workflow

- [x] Remove public comparison hash-match exports.
- [x] Produce JPMI-only hash identity/coverage.
- [x] Generate standalone JPMI technical reports.
- [x] Add `scripts/55_publish_custody_timeline.py` so the sourced public timeline survives a normal rebuild.
- [x] Update architecture and reproducibility documentation for the sourced-history layer.
- [x] Reframe historical hardware diagnostics so they are not automatically treated as identification of the 2019 repair-shop machine.

## Project-environment validation

- [ ] Run the complete pipeline against the canonical `rhb_forensics` PostgreSQL database, including Stage 55.
- [ ] Run `scripts/90_validate_exports.py` after regeneration and confirm a clean gate.
- [ ] Regenerate `build/manifest.tsv`, `build/manifest.sha256`, and section manifests after the latest report changes.
- [ ] Confirm `build/reports/03_known_datetime_stamps_of_use.md` is republished from `docs/06_timeline_and_handling.md` by Stage 55.
- [ ] Confirm generated reports retain the bounded no-hacking/no-injection language.

These checks require the project database/runtime and cannot be executed through the GitHub repository connector alone.

## Highest-value unresolved provenance evidence

- [ ] Locate Mac Shop server logs or a forensic image of the store server.
- [ ] Locate original April 2019 copy-tool logs / command history.
- [ ] Locate first-generation recovery/copy hashes.
- [ ] Identify the device serial/hash for the copy sent to Mac Isaac's father.
- [ ] Prove or disprove that the September 26 `Untitled` HFS+ volume was the father/FBI-intended physical copy.
- [ ] Locate the direct transfer/custody record showing how Todd Sanders obtained the JPMI image/report lineage.
- [ ] Compare source-image/acquisition hashes to determine whether the JPMI source and the exact-copy media supplied by Della Rocca to CBS were byte-identical.
- [ ] Locate the complete acquisition worksheet for `HB-IMAGE-2022-04-29.E01`.
- [ ] Reconcile the later 2022 acquisition / 2024 HFS+ last-write report chronology.
- [ ] Normalize timezone conventions across JPMI report families.
- [ ] Seek independent read-only verification of the restricted source image where authorized.

## Publication acceptance criteria

- [x] The README is understandable without prior knowledge of the broader laptop-data ecosystem.
- [x] Court-recited facts, participant accounts, JPMI-internal findings, and independent forensic findings are clearly distinguished.
- [x] No public conclusion claims Mac Isaac literally used `dd` without a source log proving it.
- [x] The Crucial X6 is consistently described as a later custody medium.
- [x] The September 26, 2019 HFS+ creation date is presented as a strong chronology correlation with the FBI-copy period, not as proved physical-device identity.
- [x] The December 9, 2019 retained exact-copy event is used as the strongest direct-copy custody anchor.
- [x] Later Finder/Spotlight/system metadata is not mislabeled as substantive-file fabrication.
- [x] The no-hacking/no-injection finding is stated as “no evidence identified,” not as an impossible-to-falsify absolute.
- [x] The absence of public source bytes is explained without understating the value of the forensic reports.
- [x] The Todd Sanders/America Project connection is presented as a provenance-network bridge, not proof of identical CBS/JPMI physical media.
- [ ] Full database-backed regeneration and validator pass completed in the project environment.

## Repository philosophy

The public repository should answer one question well:

> **What does the John Paul Mac Isaac direct-copy lineage itself show?**

The answer presently supported by the reporting is that it preserves a broad pre-repair Mac user environment, was copied and later examined, and **does not show identified evidence of post-dropoff hacking or substantive external-file injection**.
