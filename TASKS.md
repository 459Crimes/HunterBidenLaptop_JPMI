# JPMI Publication Tasks and Gates

## Public narrative

- [x] Define JPMI without assuming digital-forensics knowledge.
- [x] Explain the qualified `dd`-style / whole-volume clone analogy.
- [x] Spell out Who / What / When / Where / Why / How.
- [x] Explain the custody-device versus original-laptop distinction.
- [x] Explain why a September 2019 HFS+ destination can contain older files.
- [x] Explain later Finder, Spotlight, and examination/system-state activity without automatically attributing it to document fabrication.
- [x] Explain filesystem terminology for non-experts.
- [x] Publish limitations and unresolved custody questions.
- [x] Flag the 2022 acquisition / 2024 last-write discrepancy.
- [x] Publish a JPMI-only reproducibility map.

## Technical cleanup

- [x] Remove public comparison hash-match exports.
- [x] Rewrite `scripts/20_export_hash_manifest.py` to generate JPMI-only identity and coverage.
- [x] Rewrite `scripts/50_build_reports.py` to generate standalone JPMI reports.
- [x] Reframe `build/reports/*.md` so the public reports stand on JPMI evidence alone.
- [x] Update hash-manifest section metadata after removing comparison exports.
- [x] Update `build/manifest.tsv` and `build/manifest.sha256` after build changes.
- [x] Remove superseded comparison notes from `docs/notes/`.
- [x] Separate historical hardware diagnostics from identification of the 2019 repair-shop machine.

## Project-environment validation

- [ ] Run the complete pipeline against the canonical `rhb_forensics` PostgreSQL database.
- [ ] Run `scripts/90_validate_exports.py` after regeneration and confirm a clean gate.
- [ ] Confirm regenerated report/hash-manifest contents match the public standalone scope.

These checks require the project database/runtime and cannot be executed through the GitHub repository connector alone.

## Provenance research backlog

Highest-value unresolved evidence:

- [ ] Reconcile the acquisition/report lineage that pairs `HB-IMAGE-2022-04-29.E01` with the reported 2024 HFS+ last-write.
- [ ] Locate original repair-shop recovery logs.
- [ ] Locate first-copy hashes, if they were recorded.
- [ ] Identify any repair-shop server or intermediate image/file-tree record.
- [ ] Identify device serial numbers for each intermediate custody medium.
- [ ] Locate copy-tool logs or command history.
- [ ] Locate the complete acquisition worksheet for `HB-IMAGE-2022-04-29.E01`.
- [ ] Normalize timezone conventions across the received JPMI reports.
- [ ] Seek independent read-only verification of the restricted E01 where authorized.

## Publication acceptance criteria

- [x] The README is understandable without prior knowledge of the broader laptop-data ecosystem.
- [x] No public conclusion claims Mac Isaac literally used `dd` without a source log proving it.
- [x] The Crucial X6 is consistently described as a later custody medium.
- [x] The September 2019 HFS+ volume-creation event is distinguished from original file dates.
- [x] The 2022/2024 chronology conflict is explicitly disclosed rather than silently harmonized.
- [x] Later system metadata is not mislabeled as automatic evidence of later document fabrication.
- [x] Historical hardware diagnostics are not automatically used to identify the 2019 repair-shop machine.
- [x] Quantitative public claims trace to JPMI build artifacts.
- [x] The report generator uses the same standalone framing.
- [x] Comparison artifacts are absent from the public build.
- [ ] Full database-backed regeneration and validator pass completed in the project environment.

## Repository philosophy

The public repository should answer one question well:

> **What does the John Paul Mac Isaac copy itself tell us?**

Comparative analysis belongs in a separate project.
