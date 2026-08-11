# Repository Architecture

## Purpose

This repository documents **JPMI — the John Paul Mac Isaac copy — as a standalone evidence source**.

The architecture has three layers:

1. **Public narrative** — explain provenance and filesystem evidence to a reader with no digital-forensics background.
2. **Machine-readable evidence** — publish the JPMI-derived inventories and summaries that support the narrative.
3. **Reproducibility pipeline** — regenerate and validate those artifacts from the JPMI tables in the forensic database.

No other laptop-data corpus is required to explain or validate the internal JPMI presentation.

## Layer 1 — public narrative

The `docs/` directory is the recommended entry point.

| Document | Purpose |
|---|---|
| `01_what_is_jpmi.md` | Define the evidence source and the qualified `dd`-style analogy |
| `02_provenance_5ws.md` | Who, What, When, Where, Why, and How |
| `03_chain_of_custody.md` | Known custody stages and unresolved intermediate copy step(s) |
| `04_what_is_on_the_copy.md` | Explain the user, application, media, and filesystem populations |
| `05_filesystem_for_non_experts.md` | Explain GPT, EFI, HFS+, CNIDs, journals, Spotlight, hashes, and timestamps |
| `06_timeline_and_handling.md` | Separate original activity from destination creation and later handling |
| `07_limits_and_open_questions.md` | State evidentiary boundaries and missing records |
| `08_reproducibility.md` | Map public claims back to build artifacts and scripts |

The narrative rule is:

> **Observed fact → interpretation → limitation**

## Layer 2 — machine-readable JPMI evidence

The `build/` directory contains derived artifacts.

### `build/disk_info/`

Records the later custody device and forensic image:

- Crucial X6 device model and serial;
- E01 image name;
- acquisition hashes;
- sector count and size;
- GPT partition map.

### `build/volume_info/`

Records the HFS+ destination:

- volume name and identifier;
- filesystem type;
- sector offset;
- reported volume creation and last-write dates;
- HFS+ journal;
- Spotlight, DocumentRevisions, and other system-state summaries.

### `build/file_tree/`

Records the JPMI path hierarchy and rollups:

- directory tree;
- top-level user/system populations;
- `Users/roberthunter` home-directory populations.

### `build/hash_manifest/`

Records **JPMI-only** object identity and coverage:

- per-CNID SHA-256 identity;
- path/hash coverage statistics.

Cross-corpus match tables are outside the purpose of this repository.

### `build/metadata/`

Records:

- created/modified/accessed distributions;
- extension distributions;
- file types;
- permissions;
- CNID metrics;
- alias/hard-link metrics.

### `build/reports/`

Human-readable technical summaries generated from JPMI evidence only.

### `build/archives/`

Partitioned archives of large JPMI metadata exports. These preserve reproducibility while respecting GitHub file-size limits.

## Layer 3 — reproducibility pipeline

### Canonical data inputs

| Table / input | Role |
|---|---|
| `jpmi_acquisition` | custody device, image, disk and volume identity |
| `files` for the JPMI source | normalized path inventory |
| `jpmi_file_times` | created / modified / accessed timestamps |
| `jpmi_sha256_allpaths` | reported SHA-256 values by JPMI path |
| `jpmi_cnid_map` | HFS+ catalog identity and parent hierarchy |
| `jpmi_alias_map` | canonical/alias and hard-link relationships |
| `jpmi_tsk_timeline` | filesystem timeline and system-state events |

The source reports and manifests remain with the restricted master evidence collection; the raw JPMI E01 is not published here.

### Pipeline stages

1. `10_export_file_tree.py` — build JPMI hierarchy and directory rollups.
2. `20_export_hash_manifest.py` — build JPMI-only SHA-256 identity and coverage outputs.
3. `30_export_metadata.py` — build timestamp, extension, type, permission, CNID, and alias summaries.
4. `40_export_volume_disk.py` — build disk, partition, and HFS+ volume identity outputs.
5. `50_build_reports.py` — generate standalone JPMI reports.
6. `60_archive_deep_exports.py` — archive large deep JPMI metadata exports.
7. `90_validate_exports.py` — validate file sizes, section manifests, archive parts, and checksums.

## Identity rules

The repository treats these as separate concepts:

- **physical device identity** — model, serial, size;
- **forensic image identity** — image name and acquisition hashes;
- **volume identity** — filesystem, partition, volume identifier;
- **catalog identity** — CNID and parent relationship;
- **path identity** — human-readable location;
- **byte identity** — cryptographic hash;
- **time evidence** — created, modified, accessed, volume creation, and last write.

One field should never silently substitute for another.

## Provenance rules

- The Crucial X6 is a later custody device, not automatically the original laptop SSD.
- “`dd`-style” is a public explanatory analogy for a whole-volume/filesystem-preserving copy lineage, not proof that `dd` was literally used.
- The September 2019 HFS+ volume-creation event is separate from older file timestamps stored inside the destination.
- Later Finder, Spotlight, DocumentRevisions, and access-time activity is custody evidence; it is not automatically evidence of substantive document fabrication.
- Historical hardware diagnostics inside the user tree may be migrated data and should not automatically identify the 2019 repair-shop machine.
- Hash values in this GitHub repository are received JPMI-manifest values unless explicitly recomputed from source bytes.

## Publication boundary

This repository intentionally does **not** present cross-corpus comparisons.

Questions involving relationships between JPMI and other datasets belong in a separate comparative-analysis project. Keeping that work separate prevents a reader from needing to understand unrelated evidence sources before understanding JPMI itself.
