# JPMI Source Analysis — GitHub-Ready Forensic Artifact Build

Status: **DRAFT — pipeline implemented, artifacts generated from PostgreSQL `rhb_forensics`**

This subproject analyzes the received **JPMI source files** (source ID `122`,
`JPMI Metadata HB-FileList-2022-04-v1`) and produces a self-contained,
**GitHub-ready repository** under `build/` whose every generated file stays
**conservatively under GitHub size limits**.

The JPMI source is a **metadata and hash witness**, not a byte-accessible image
in this project. Every artifact in `build/` is therefore derived from the
canonical PostgreSQL `rhb_forensics` inventory; the received source material
(`JPMI Metadata HB-FileList-2022-04-v1`, source ID `122`) and the readable
APFS/GAI/0728 sources remain with the master corpus and are **not shipped** in
this repository. No JPMI device bytes, no source evidence, and no database rows
were modified.

## What this repo produces

| Section | Contents |
|---|---|
| `file_tree/` | Hierarchical directory tree with per-directory rollups and coverage; top-level inventory summary |
| `hash_manifest/` | SHA-256 identity manifest (per canonical CNID), cross-source match manifest (JPMI ↔ APFS/GAI/0728), coverage statistics |
| `metadata/` | File-time distributions, extension/type/permission distributions, CNID hierarchy and hard-link summaries |
| `volume_info/` | HFS+ volume identity, filesystem metadata, and volume-level system state (`Spotlight`, `DocumentRevisions`, journal, GPT structural records) |
| `disk_info/` | Acquisition record, device identity, and GPT partition map |
| `reports/` | Forensic analysis reports: computer information, OS-version evidence, known datetime stamps of use, and the post-2019-03-31 timeline |
| `archives/` | Partitioned gzip-tar archives of the gitignored `deep/` full exports, so every byte of the deep sets is also GitHub-committable |
| `manifest.tsv` + `manifest.sha256` | Checksummed inventory of every committed artifact |

## Size policy (conservative)

GitHub rejects files above **100 MB** and warns above **50 MB**. This repository
targets the conservative 50 MB posture:

- **50 MiB** budget per committed file (default, configurable in `config/limits.json`).
- **90 MiB** hard cap — a static fail-safe ceiling; never reached in practice.
- The pre-commit hook blocks staged files over **50 MB**, so the commit gate and
  the export validator agree.
- Every export is **sharded** so no single committed file exceeds the budget.
- Optional high-volume exports (`build/deep/`) are generated locally for
  analysis and are **excluded from git** (`.gitignore`).
- Stage `60` partitions every `build/deep/` section into
  `archives/deep_*_NNN.tar.gz.part` parts at the 50 MiB budget, byte-verifies
  the round trip, and records each part in `archives/_manifest.tsv`. The
  `.part` suffix keeps the parts outside the repository's global `*.gz` ignore
  rule, so the deep content **can** live on GitHub.
- `90_validate_exports.py` recomputes sizes and SHA-256 checksums, cross-checks
  the archive manifest, and fails if any committed file exceeds the budget.

See [`GITHUB_SIZE_POLICY.md`](GITHUB_SIZE_POLICY.md).

## Reproduction

Prerequisites:

- Local PostgreSQL `rhb_forensics` (canonical master) with the JPMI tables
  populated. `RHB_PG_DSN` may point at the master on
  `laptop.459.network`; the default is `dbname=rhb_forensics` on the local
  socket.

```bash
export RHB_PG_DSN="dbname=rhb_forensics"        # or the canonical master
python3 scripts/10_export_file_tree.py
python3 scripts/20_export_hash_manifest.py
python3 scripts/30_export_metadata.py
python3 scripts/40_export_volume_disk.py
python3 scripts/50_build_reports.py
python3 scripts/60_archive_deep_exports.py      # partitioned archives of deep/
python3 scripts/90_validate_exports.py           # gate: must pass before publish
```

Run order is fixed; validation must pass before the `build/` tree is published.

## Source boundary and caveats

- The JPMI inventory in `rhb_forensics` is the `roberthunter` home directory
  plus GPT/EFI/HFS+ structural records. It does **not** include byte-accessible
  `System`, `Applications`, or `usr` trees.
- SHA-256 values come from the rank-1 rank-5 report set (`hb-report-5`); they
  identify the objects represented in the manifest, not bytes this project can
  re-read.
- The volume carries post-2019-03-31 system/metadata timestamps. These are
  custody-relevant activity indicators and are not treated as proof of new user
  content.
- See [`ARCHITECTURE.md`](ARCHITECTURE.md) and [`DATA_CONTRACT.md`](DATA_CONTRACT.md).

## Documents

- `STATUS.md` — current state and gates.
- `TASKS.md` — implementation backlog and acceptance criteria.
- `ARCHITECTURE.md` — pipeline stages, data sources, identity rules.
- `DATA_CONTRACT.md` — output schemas for every generated file.
- `GITHUB_SIZE_POLICY.md` — size budgets and enforcement.
