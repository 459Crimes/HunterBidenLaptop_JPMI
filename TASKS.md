# JPMI Source Analysis — Tasks and Gates

## Done

- [x] Locate and characterize the received JPMI source material
      (`source/JPMI_metadata/`, source ID `122`).
- [x] Map the `rhb_forensics` PostgreSQL schema for JPMI tables.
- [x] Confirm cross-source hash overlap tables (`jpmi_hash_overlap`,
      `jpmi_path_overlap`) and readable-source routes.
- [x] Implement pipeline scripts `10`–`90`.
- [x] Run the pipeline end-to-end; `90_validate_exports.py` gate passed
      (37 files, all within caps and consistent with section manifests).
- [x] Partition every gitignored `build/deep/` section into
      `archives/deep_*_NNN.tar.gz.part` parts (50 MiB budget) with
      byte-verified round trips; `90_validate_exports.py` cross-checks
      `archives/_manifest.tsv`.
- [x] Archive parts are deterministic (zeroed tar member mtimes and gzip MTIME):
      rebuilds reproduce byte-identical parts for identical source shards.

## Acceptance criteria (all must hold before publish)

- [x] Every file under `build/` is below the 50 MiB budget (hard cap 90 MiB).
- [x] `90_validate_exports.py` passes and regenerates `manifest.tsv` +
      `manifest.sha256`.
- [x] Row counts in each shard manifest match the PostgreSQL source queries.
- [ ] Investigator review of every `reports/*.md`; drafts marked as such.
- [x] `build/deep/` remains gitignored, yet its full content is published via
      the partitioned `build/archives/` sets.
- [x] This subproject is a standalone repository (`BidenLaptop_JPMI`) with its
      own README, size policy, and size gate.
- [x] No source evidence modified; no database rows written by the pipeline
      (read-only queries only).

## Backlog

- [ ] Resolve byte-identical hardware-diagnostics routes (ioreg/spindump/system
      logs) against mounted readable APFS and GAI sources.
- [ ] Produce a date-bounded TSK timeline slice for the 090-[] diagnostics
      window if the raw `rank5-timeline.csv` mtime ingestion is repaired.
- [ ] Optionally export `build/deep/` full shards for a bounded local review.
