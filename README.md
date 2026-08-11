# JPMI — The John Paul Mac Isaac Copy

This repository documents one specific evidence source from the Hunter Biden laptop story: the **John Paul Mac Isaac copy**, abbreviated **JPMI**.

The purpose of this repository is narrow. It does not ask readers to understand other laptop datasets, competing exports, or our larger forensic database. It asks a simpler question:

> **What is the JPMI copy, where did it come from, what does it contain, and what can its filesystem tell us about its history?**

## The short version

In April 2019, a Mac computer associated with Hunter Biden was left for data recovery at John Paul Mac Isaac's computer repair shop in Wilmington, Delaware. The data recovered from that repair-shop custody became the source of later copies.

**JPMI is our name for the Mac Isaac-lineage copy examined in this repository.**

For a non-specialist, the easiest way to understand JPMI is as a **whole-volume, `dd`-style forensic copy rather than a hand-picked folder of documents**. That analogy describes the form of the evidence: the JPMI material preserves a partitioned Mac volume, filesystem structures, application state, a normal user home directory, timestamps, catalog identifiers, and hundreds of thousands of file records.

It does **not** mean that we have proven John Paul Mac Isaac literally ran the Unix `dd` command. The exact repair-shop copy utility and every intermediate custody step remain unresolved.

The later forensic acquisition represented in this project is an **E01 forensic image** named `HB-IMAGE-2022-04-29.E01`, made from a 500,107,862,016-byte Micron Crucial X6 USB SSD. The image is identified by MD5 and SHA-1 values in the source acquisition record. The Crucial X6 is a later custody medium; it is not the original internal laptop SSD.

## The 5 Ws of JPMI

| Question | Answer supported by this repository |
|---|---|
| **Who?** | The user data is organized primarily under the macOS account `roberthunter` and contains the ordinary personal, communications, application, media, and device-backup state associated with that account. John Paul Mac Isaac is the repair-shop custodian from whose recovery/copy lineage JPMI takes its name. |
| **What?** | A GPT-partitioned Mac-oriented storage image containing an EFI partition and a journaled HFS+ data volume named `Untitled`, plus the `roberthunter` home tree, filesystem metadata, application state, and hash/timestamp inventories. |
| **When?** | The important dates are different events: original user data spans years before the 2019 repair; the repair-shop event occurred in April 2019; the JPMI HFS+ destination reports a creation date of September 26, 2019; the E01 acquisition is reported as April 29, 2022; later indexing/handling metadata exists after those dates. |
| **Where?** | The historical repair event was in Wilmington, Delaware. The physical custody medium described by the forensic acquisition record is a Micron Crucial X6 USB SSD. This GitHub repository itself contains metadata, hashes, reports, and derived inventories—not the restricted source image bytes. |
| **Why?** | The copy lineage exists because data was recovered from the repair-shop computer and preserved for later custody, review, and forensic examination. This repository exists to make the provenance and internal structure of that copy understandable and reproducible. |

A sixth question matters just as much:

**How?** The exact original repair-shop copy method is not established by the evidence presently in this repository. The resulting JPMI structure is much richer than a curated document dump: it includes GPT/EFI structure, an HFS+ journal, filesystem catalog relationships, Spotlight and document-revision state, and a normal macOS user hierarchy. Those features are consistent with a filesystem-level or block-oriented recovery/copy lineage. The later forensic acquisition itself was made as an E01 image.

## What is actually on JPMI?

The current inventory contains **576,249 paths**. The user-tree rollup contains approximately **572,743 file rows** under `Users`, including a conventional macOS home directory:

| Home directory | Files |
|---|---:|
| `Library` | 251,863 |
| `Documents` | 119,794 |
| `Pictures` | 92,393 |
| `Movies` | 61,202 |
| `Downloads` | 23,415 |
| `Music` | 19,313 |
| `Desktop` | 4,654 |

This matters because a real Mac user profile is not just PDFs, photographs, and emails. It also contains Mail databases, contacts, caches, preferences, application support, device backups, Cloud/iCloud state, Photos data, message databases, thumbnail and derivative files, `.DS_Store` records, SQLite journals, and other machine-generated artifacts.

The JPMI inventory includes, among other categories, large populations of Apple Mail `.emlx` messages, `.vcf` contacts, photographs, property-list files, and iCloud-related objects.

## Why the filesystem matters

A loose export can tell you that a file exists. A filesystem can tell you much more about **context**.

JPMI preserves evidence of:

- a GPT partition map;
- an EFI System Partition;
- a journaled HFS+ data volume;
- an HFS+ volume identifier and sector offset;
- CNID and parent-CNID directory relationships;
- filesystem journal structures;
- Spotlight indexing state;
- DocumentRevisions state;
- allocated and unallocated regions;
- a normal `Users/roberthunter` hierarchy;
- created, modified, and accessed timestamps;
- hard-link/alias relationships;
- SHA-256 identities for hundreds of thousands of represented objects.

These artifacts make JPMI useful not only for asking **what files are present**, but also **how the copied Mac environment was organized and later handled**.

## The timeline is not one timestamp

A central rule of this repository is that different timestamps answer different questions.

- **Pre-April 2019 timestamps** can describe original user or application activity.
- **September 2019 filesystem timestamps** are associated with creation/reconstruction of the HFS+ destination volume.
- **2020 metadata changes** show later browsing or interaction with parts of the copied volume.
- **2022 accessed-time clusters** are dominated by examination/acquisition activity.
- **2024 Spotlight/index timestamps** show later filesystem/index handling.

The repository currently identifies **141 inventory rows with modified timestamps after March 31, 2019**. Those rows are dominated by filesystem and application metadata. They demonstrate that the copied volume was not frozen after the repair-shop period, but they do **not** by themselves establish wholesale insertion of later user documents.

See [`docs/06_timeline_and_handling.md`](docs/06_timeline_and_handling.md).

## What this repository does not claim

This project deliberately separates observations from conclusions.

It does **not** presently claim that:

- John Paul Mac Isaac used the literal `dd` command;
- the 500 GB Crucial X6 was Hunter Biden's original internal SSD;
- every timestamp on the later HFS+ copy is an original-user timestamp;
- every historical hardware diagnostic inside the user folders identifies the particular laptop left for repair in 2019;
- the project has byte-level access to the restricted JPMI E01 image;
- the metadata can identify the human who caused every post-2019 filesystem event.

## Start here

For the public-facing narrative, read these in order:

1. [`docs/01_what_is_jpmi.md`](docs/01_what_is_jpmi.md) — the evidence source in plain English.
2. [`docs/02_provenance_5ws.md`](docs/02_provenance_5ws.md) — Who, What, When, Where, Why, and How.
3. [`docs/03_chain_of_custody.md`](docs/03_chain_of_custody.md) — the known and unknown custody steps.
4. [`docs/04_what_is_on_the_copy.md`](docs/04_what_is_on_the_copy.md) — the contents of the HFS+ copy.
5. [`docs/05_filesystem_for_non_experts.md`](docs/05_filesystem_for_non_experts.md) — HFS+, GPT, CNIDs, journals, Spotlight, hashes, and timestamps explained.
6. [`docs/06_timeline_and_handling.md`](docs/06_timeline_and_handling.md) — original activity versus later custody activity.
7. [`docs/07_limits_and_open_questions.md`](docs/07_limits_and_open_questions.md) — what remains unproven.
8. [`docs/08_reproducibility.md`](docs/08_reproducibility.md) — how the published tables and reports are generated.

## Technical evidence

The `build/` directory contains the underlying reproducibility artifacts:

- `disk_info/` — custody device, image, and partition identity;
- `volume_info/` — HFS+ volume identity and system-state summaries;
- `file_tree/` — directory and user-home rollups;
- `hash_manifest/` — JPMI SHA-256 identities and coverage;
- `metadata/` — timestamp, extension, type, permission, CNID, and alias summaries;
- `reports/` — human-readable forensic summaries;
- `archives/` — partitioned deep metadata exports;
- `manifest.tsv` / `manifest.sha256` — validation inventory.

The raw JPMI source image is not published here.

## Evidence rule

Throughout this repository:

> **Observed fact → interpretation → limitation**

are kept separate.

That is intentional. Provenance is strongest when the reader can see exactly which parts are measured, which parts are inferred, and which parts remain unknown.
