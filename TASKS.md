# JPMI Publication Tasks and Gates

## Public narrative

- [x] Define JPMI without assuming digital-forensics knowledge.
- [x] Explain the qualified `dd`-style / whole-volume clone analogy.
- [x] Spell out Who / What / When / Where / Why / How.
- [x] Explain the custody-device versus original-laptop distinction.
- [x] Explain why a September 2019 HFS+ destination can contain older files.
- [x] Explain post-2019 Finder, Spotlight, and examination activity.
- [x] Explain filesystem terminology for non-experts.
- [x] Publish limitations and unresolved custody questions.
- [x] Publish a JPMI-only reproducibility map.

## Technical cleanup

- [ ] Remove public cross-corpus hash-match exports.
- [ ] Rewrite `scripts/20_export_hash_manifest.py` to generate JPMI-only identity and coverage.
- [ ] Rewrite `scripts/50_build_reports.py` to generate standalone JPMI reports.
- [ ] Rewrite `build/reports/*.md` around the public evidence sequence.
- [ ] Update hash-manifest section metadata after removing comparison exports.
- [ ] Update `build/manifest.tsv` and `build/manifest.sha256` after build changes.
- [ ] Remove superseded comparison notes from `docs/notes/`.
- [ ] Confirm no public-facing document requires another corpus to make its JPMI argument.

## Provenance research backlog

Highest-value unresolved evidence:

- [ ] Locate original repair-shop recovery logs.
- [ ] Locate first-copy hashes, if they were recorded.
- [ ] Identify any repair-shop server or intermediate image/file-tree record.
- [ ] Identify device serial numbers for each intermediate custody medium.
- [ ] Locate copy-tool logs or command history.
- [ ] Locate complete acquisition worksheet for `HB-IMAGE-2022-04-29.E01`.
- [ ] Normalize timezone conventions across the received JPMI reports.
- [ ] Seek independent read-only verification of the restricted E01 where authorized.

## Publication acceptance criteria

Before merge/publication, all must hold:

- [ ] The README makes sense to a reader who has never heard of APFS, GAI, or the project's source IDs.
- [ ] No public conclusion claims Mac Isaac literally used `dd` without a source log proving it.
- [ ] The Crucial X6 is consistently described as a later custody medium.
- [ ] The September 2019 HFS+ volume-creation event is distinguished from original file dates.
- [ ] Later system metadata is not mislabeled as automatic evidence of later document fabrication.
- [ ] Historical hardware diagnostics are not automatically used to identify the 2019 repair-shop machine.
- [ ] Every quantitative statement traces to a JPMI build artifact.
- [ ] The report generator reproduces the same standalone framing.
- [ ] Cross-corpus comparison artifacts are absent from the public build.
- [ ] Size/checksum validation passes after cleanup.

## Repository philosophy

The public repository should answer one question well:

> **What does the John Paul Mac Isaac copy itself tell us?**

Comparative analysis belongs elsewhere.
