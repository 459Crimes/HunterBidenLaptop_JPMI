# Status

Updated: 2026-08-10

## Current state

`PIPELINE IMPLEMENTED — DRAFT ARTIFACTS GENERATED — NOT YET REVIEWED OR PUBLISHED`

| Gate | State |
|---|---|
| JPMI source characterization | Complete (see `docs/notes/2026-08-04_jpmi_source_characterization_report.md`) |
| PostgreSQL schema understood | Complete |
| Pipeline scripts | Implemented and run (`scripts/10`–`90`) |
| Artifact generation | Generated under `build/` |
| Deep exports published | `build/deep/` stays gitignored; full content archived as 5 `build/archives/deep_*_NNN.tar.gz.part` parts (all ≤ 50 MiB), byte-verified and deterministic |
| Size-budget validation | Passed — `90_validate_exports.py` gate clean (37 files, all within caps) |
| Report review | Pending — reports are drafts requiring investigator review |
| Git registration | Pending — `build/` not yet staged/committed |

## Open items

1. Investigator review of `reports/` before any publication.
2. Optional mounting of the readable APFS (`rhb_drive`) and GAI sources to
   resolve the byte-identical hardware-diagnostics routes cited in
   `reports/01_computer_information.md`.
3. Confirm canonical PostgreSQL reachability (`laptop.459.network`) for a
   full-corpus rebuild; the local socket copy was used for this draft.
4. Decide publication scope for `build/deep/` (produced locally, gitignored).
