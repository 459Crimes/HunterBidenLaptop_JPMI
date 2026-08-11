# JPMI — The John Paul Mac Isaac Copy

This repository documents one specific evidence source from the Hunter Biden laptop story: the **John Paul Mac Isaac copy**, abbreviated **JPMI**.

The purpose of this repository is narrow. It does not ask readers to understand other laptop datasets or competing exports. It asks:

> **What is the JPMI copy, where did it come from, what does it contain, and what can its filesystem reporting tell us about its history?**

## The short version

In April 2019, Hunter Biden's data entered John Paul Mac Isaac's repair-shop custody in Wilmington, Delaware through a data-recovery event involving damaged Apple laptops.

The Delaware Supreme Court's 2025 opinion recounts the pleaded history that **three damaged laptops** were presented on April 12, 2019: one could be used with a keyboard Mac Isaac supplied, another was considered unrecoverable, and one was left for recovery. The next day, at Mac Isaac's request, Biden returned with an external hard drive for the recovered data. Mac Isaac later described first staging recoverable data on his **store server** before transferring it to the customer drive.

**JPMI is our name for the Mac Isaac direct-copy provenance lineage examined in this repository.**

For a non-specialist, the easiest way to understand JPMI is as a **whole-volume, `dd`-style forensic copy rather than a hand-picked folder of documents**. That analogy describes the evidentiary form: JPMI preserves a partitioned Mac volume, filesystem structures, application state, a normal user home directory, timestamps, catalog identifiers, and hundreds of thousands of file records.

It does **not** mean that we have proved Mac Isaac literally used the Unix `dd` command. The exact repair-shop copy utility and every intermediate custody step remain unresolved.

## The most important provenance finding

The JPMI reporting shows that the copied environment was later **opened, browsed, indexed, copied, and forensically examined**.

It does **not** presently show evidence that an outside actor hacked the Mac Isaac direct copy or injected substantive external user files into it after the April 2019 repair event.

The later modified rows identified in JPMI are overwhelmingly Finder, filesystem, Spotlight, DocumentRevisions, directory, temporary, and other system/application metadata—not a later population of substantive Hunter-created documents.

That finding is independently consistent with CBS News' 2022 examination of what Mac Isaac's lawyer Brian Della Rocca called an **“exact copy”** of the laptop data supplied to federal investigators. CBS reported that independent examiners found **no evidence that the user data had been modified, fabricated, or tampered with and no new files originating after April 2019**.

Reference: [CBS News, Nov. 21, 2022](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)

The correct formulation throughout this repository is therefore:

> **No evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting. Later metadata is consistent with custody and forensic handling.**

That is an evidentiary finding, not a claim that undetectable alteration is philosophically impossible.

## The 2019–2020 custody story in ten steps

1. **April 12, 2019 — three damaged laptops.** According to the Delaware court record, three damaged laptops were presented. One worked with a supplied keyboard, one was unrecoverable, and one remained for recovery.
2. **April 13 — external hard drive.** Biden returned with an external drive for the recovered data. Mac Isaac said the recovery was completed that day.
3. **Store server.** Mac Isaac later said recoverable data was first copied to his secure store server and then transferred to the customer drive. The server logs are not presently available here.
4. **Late July 2019 — FBI concern.** Court opinions place the start of Mac Isaac's FBI-related contacts in this period.
5. **September–October 2019 — preservation/FBI copy.** Mac Isaac later said he created a copy for his father to take to the FBI in Albuquerque.
6. **September 26, 2019 — JPMI HFS+ volume creation.** JPMI reports the `Untitled` HFS+ destination created on this date. This falls within the same general period as Mac Isaac's described FBI-copy activity. The timing is significant, but physical identity is not yet proved.
7. **December 9, 2019 — FBI subpoena.** The FBI took the laptop, customer hard drive, and paperwork. The Delaware Supreme Court states that Mac Isaac **made an exact copy before parting with the original**.
8. **August 2020 — Costello copy.** Mac Isaac provided a copy to Robert Costello, Rudy Giuliani's attorney.
9. **October 14, 2020 — New York Post story.** The first laptop story became public.
10. **October 15, 2020 — JPMI Finder metadata.** JPMI's Desktop `.DS_Store` was modified the next day, consistent with someone opening/browsing the copied environment. This is **not evidence that a Hunter file was injected or altered**.

See [`docs/06_timeline_and_handling.md`](docs/06_timeline_and_handling.md) for the sourced timeline.

## The provenance bridge to this repository

The JPMI acquisition record contains this note:

```text
hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)
```

Public records identify **Todd Sanders as affiliated with Patrick Byrne's America Project**. The America Project publicly supported/funded Mac Isaac's 2022 litigation; Brian Della Rocca represented Mac Isaac in that litigation and later supplied CBS with the exact-copy dataset it independently examined.

That supports this bounded conclusion:

> **The JPMI reports come from the same Mac Isaac-centered provenance network as the clean Mac Isaac/FBI-lineage copy later supplied by Mac Isaac's lawyer for independent CBS examination.**

It does **not yet prove** that Todd Sanders possessed the identical physical drive or identical E01 file examined by CBS. A direct transfer record or matching acquisition hash is still needed for that stronger statement.

See [`docs/03_chain_of_custody.md`](docs/03_chain_of_custody.md).

## The 5 Ws of JPMI

| Question | Answer supported by this repository |
|---|---|
| **Who?** | The copied environment is organized primarily under the macOS account `roberthunter`. John Paul Mac Isaac is the repair-shop custodian from whose recovery/copy lineage JPMI takes its name. Later JPMI reporting supplied to this project is attributed internally to Todd Sanders. |
| **What?** | A GPT-partitioned Mac-oriented storage environment containing an EFI partition and a journaled HFS+ data volume named `Untitled`, plus the `roberthunter` home tree, filesystem metadata, application state, and hash/timestamp inventories. |
| **When?** | User data spans years before the repair; the repair occurred in April 2019; the JPMI HFS+ destination reports creation on September 26, 2019; the FBI took the original laptop/drive on December 9, 2019; the direct copy was publicly distributed in 2020; later forensic examination/reporting followed. |
| **Where?** | The repair event occurred in Wilmington, Delaware. The later custody medium described in the acquisition record is a Micron Crucial X6 USB SSD. This GitHub repository contains reports/manifests rather than the restricted source bytes. |
| **Why?** | Data was recovered for a repair customer, then preserved in copies after the customer did not retrieve it and Mac Isaac sought FBI/law-enforcement attention. This repository exists to document the direct-copy provenance and structure. |
| **How?** | Mac Isaac describes a recovery involving his store server and later preservation copies. The exact first-copy software/command is unresolved. The resulting JPMI reporting is consistent with a broad filesystem-preserving copy lineage rather than a curated document dump. |

## What is actually on JPMI?

The current inventory contains **576,249 paths**. The user-tree rollup contains approximately **572,743 file rows** under `Users`:

| Home directory | Files |
|---|---:|
| `Library` | 251,863 |
| `Documents` | 119,794 |
| `Pictures` | 92,393 |
| `Movies` | 61,202 |
| `Downloads` | 23,415 |
| `Music` | 19,313 |
| `Desktop` | 4,654 |

A real Mac user profile is not just PDFs, photographs, and emails. It contains Mail databases, contacts, caches, preferences, application support, device backups, Cloud/iCloud state, Photos data, message databases, thumbnails, `.DS_Store`, SQLite journals, and other machine-generated artifacts.

That context is one reason JPMI is useful for provenance analysis.

## Why the filesystem matters

JPMI preserves reporting for:

- GPT partition structure;
- an EFI System Partition;
- a journaled HFS+ data volume;
- an HFS+ volume identifier and sector offset;
- CNID and parent-CNID relationships;
- filesystem journal structures;
- Spotlight indexing state;
- DocumentRevisions state;
- allocated and unallocated regions;
- `Users/roberthunter` hierarchy;
- created, modified, and accessed timestamps;
- alias/hard-link relationships;
- reported SHA-256 identities for hundreds of thousands of represented objects.

These records allow analysis of **structure, chronology, and custody activity**, even though this public repository does not contain the individual JPMI source-file bytes.

## No source bytes does not mean no forensic value

This GitHub repository is a **metadata/hash forensic witness**, not a public byte dump of the restricted source image.

It cannot independently open every JPMI file or recompute every source-object hash.

It can accurately and reproducibly analyze what the received forensic reports record, including:

- directory hierarchy;
- file populations and represented sizes;
- timestamps and event clusters;
- partition/volume identity;
- HFS+ catalog relationships;
- aliases/hard links;
- reported object hashes;
- later Finder/Spotlight/system-state activity;
- whether the reporting contains evidence of bulk post-dropoff substantive-file insertion.

So the evidentiary scope is clear:

> **JPMI contains enough forensic reporting to support accurate structural, timeline, and provenance analysis. Byte-content claims remain limited to what the reports actually record or what an independently examined copy establishes.**

## Important later-report chronology issue

The acquisition record represented in this project identifies `HB-IMAGE-2022-04-29.E01`, while delivered HFS+ volume metadata reports a November 21, 2024 last-write.

An immutable E01 actually acquired in 2022 cannot subsequently acquire a 2024 filesystem write. This repository therefore treats the 2022/2024 pairing as an **open report-lineage discrepancy**, not as proof that the 2022 E01 itself changed later.

That later issue is separate from the 2019–2020 direct-copy timeline.

## Start here

For the public-facing narrative, read these in order:

1. [`docs/01_what_is_jpmi.md`](docs/01_what_is_jpmi.md) — the evidence source in plain English.
2. [`docs/02_provenance_5ws.md`](docs/02_provenance_5ws.md) — Who, What, When, Where, Why, and How.
3. [`docs/03_chain_of_custody.md`](docs/03_chain_of_custody.md) — repair, FBI copy, media copy, and project-delivery provenance.
4. [`docs/04_what_is_on_the_copy.md`](docs/04_what_is_on_the_copy.md) — the contents of the HFS+ copy.
5. [`docs/05_filesystem_for_non_experts.md`](docs/05_filesystem_for_non_experts.md) — HFS+, GPT, CNIDs, journals, Spotlight, hashes, and timestamps explained.
6. [`docs/06_timeline_and_handling.md`](docs/06_timeline_and_handling.md) — detailed 2019–2020 chronology and later handling.
7. [`docs/07_limits_and_open_questions.md`](docs/07_limits_and_open_questions.md) — what remains unproven.
8. [`docs/08_reproducibility.md`](docs/08_reproducibility.md) — how the published tables and reports are generated.

## Technical evidence

The `build/` directory contains:

- `disk_info/` — custody device, image, and partition identity;
- `volume_info/` — HFS+ volume identity and system-state summaries;
- `file_tree/` — directory and user-home rollups;
- `hash_manifest/` — JPMI-reported SHA-256 identities and coverage;
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
