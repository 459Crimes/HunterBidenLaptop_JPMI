# Architecture

## Goal

Turn the received JPMI metadata/hash witness (source `122`) into a bounded,
reproducible, GitHub-ready evidence package without ever touching source bytes.

## Data sources

| Source | Role |
|---|---|
| PostgreSQL `rhb_forensics` (canonical master) | Authoritative inventory: `files`, `sources`, `hash_sources`, `jpmi_*` tables |
| `source/JPMI_metadata/` | Received reports and manifests (`HB-FileList-2022-04-v1.*`, `hb-report-5/`, `reports/`); held with the master corpus, not shipped |
| `docs/notes/` (OS-files, source characterization, hash-discrepancy notes) | Interpretive context, kept separate from exact-byte findings |

## Key tables used

| Table | Rows (approx.) | Used for |
|---|---|---|
| `jpmi_acquisition` | 1 | disk/device identity, partition map, volume identity |
| `files` (source 122) | 576,249 | inventory paths, sizes, hashes, mtimes |
| `jpmi_file_times` | 576,249 | created/modified/accessed distributions and timeline |
| `jpmi_sha256_allpaths` | 655,330 | per-path SHA-256 identity (rank-1 master manifest) |
| `jpmi_cnid_map` | 397,440 | CNID/parent hierarchy, directory vs file kinds |
| `jpmi_alias_map` | 655,330 | hard-link canonical/alias identity |
| `jpmi_hash_overlap` | 292,667 | cross-source SHA-256 matches (APFS=1, GAI=116, 0728=2) |
| `jpmi_path_overlap` | 461,450 | cross-source path matches with size/time alignment |
| `jpmi_tsk_timeline` | 1,259,300 | TSK event count and volume-level system-state entries |

## Pipeline stages

1. `10_export_file_tree.py` — build hierarchical tree from `files` paths; roll
   up per-directory counts, sizes, hash coverage, and modified-time ranges.
2. `20_export_hash_manifest.py` — per-CNID canonical SHA-256 manifest and
   cross-source match manifest.
3. `30_export_metadata.py` — time, extension, type, permission, CNID, and
   hard-link distributions.
4. `40_export_volume_disk.py` — volume and disk identity files.
5. `50_build_reports.py` — markdown forensic reports grounded in the above.
6. `60_archive_deep_exports.py` — partition gitignored `build/deep/` sections
   into `archives/deep_*_NNN.tar.gz.part` parts (byte-verified, deterministic).
7. `90_validate_exports.py` — size/checksum/row-count gate (also cross-checks
   `archives/_manifest.tsv`).

## Identity and provenance rules

- SHA-256 is blob identity; path, CNID, source ID, and size are separate
  provenance attributes.
- JPMI values are metadata-derived. A JPMI hash absent from APFS/GAI is not
  automatically a missing user file; generated/cache/system state is expected
  to vary across derivative branches.
- Byte-identical cross-source routes are reported as **leads** with the exact
  readable source and path; they are not byte copies in this package.

## Boundaries

- No source evidence is read beyond PostgreSQL metadata queries.
- Reports separate exact-byte findings, contextual relationships, and
  conclusions into distinct sections.
- `build/` artifacts are analysis products; `build/deep/` opt-in exports are
  local-only and gitignored.
