# 1. What Is JPMI?

> **Encyclopedia.** Main article: [README](../README.md). Index: [all pages](INDEX.md). Related: [Glossary](GLOSSARY.md) · [Crucial X6](CRUCIAL_X6.md) · [Scope](SCOPE.md).

**JPMI** is the shorthand used in this project for the **John Paul Mac Isaac copy**: the Mac Isaac-lineage copy of data recovered from the computer associated with Hunter Biden and left at a Wilmington, Delaware repair shop in 2019.

This repository is about that copy alone.

## A useful mental model

For a general reader, JPMI is best understood as a **disk/volume copy**, not a folder of selected documents.

A common technical analogy is a `dd`-style clone. The Unix utility `dd` can copy storage at the block level, producing a destination that represents the structure of the source rather than merely copying visible documents one by one.

That analogy is useful here because the JPMI evidence contains features expected from a copied Mac storage environment:

- a GPT partition map;
- an EFI System Partition;
- a journaled HFS+ data volume;
- an HFS+ journal;
- a filesystem volume identifier;
- CNID and parent-CNID relationships;
- Spotlight indexing structures;
- DocumentRevisions state;
- allocated and unallocated space;
- a normal macOS user-home hierarchy under `roberthunter`;
- application databases, Mail state, Photos state, contacts, caches, preferences, and device-backup material.

A hand-curated document dump does not need most of those structures.

## Important technical qualification

Calling JPMI “`dd`-style” does **not** establish that John Paul Mac Isaac literally used the `dd` program or that the final 500 GB external disk was made in one direct sector-for-sector operation from the original laptop SSD.

The exact original recovery/copy command is not established by the source material available to this project.

The safer formulation is:

> **JPMI is a Mac Isaac-lineage, filesystem-preserving or block-oriented copy represented to this project by a later forensic E01 acquisition.**

## The physical medium described by the forensic record

The acquisition record describes the custody device as:

| Field | Reported value |
|---|---|
| Device | Micron Crucial X6 SSD USB Device |
| Serial | `2145E498755E` |
| Size | `500,107,862,016` bytes |
| Sector size | 512 bytes |
| Sector count | `976,773,168` |
| Source image | `HB-IMAGE-2022-04-29.E01` |
| Image format | E01 |
| Case number | `HB-2022-04-29` |
| Acquisition tool | `ADI4.7.1.2` |
| MD5 | `682619c1884e6fe006664ba31deed698` |
| SHA-1 | `fe918f0cff3304ab52875b984c88fee78ec05197` |

These values are published in [`build/disk_info/01_acquisition.tsv`](../build/disk_info/01_acquisition.tsv).

The Crucial X6 is a **custody medium**. It should not be confused with the original internal storage hardware of the laptop left at the repair shop.

## What the repository actually possesses

The restricted source image itself is not published in this GitHub repository.

The project works from received forensic metadata and manifests that describe the image, including:

- partition reports;
- HFS+ catalog and CNID information;
- file-list reports;
- file timestamps;
- SHA-256 manifests;
- filesystem timelines;
- volume and disk identity records.

Accordingly, this repository can make strong statements about **reported structure, paths, hashes, timestamps, and filesystem relationships**, while remaining explicit about the fact that the GitHub project is not independently re-reading every JPMI byte from the restricted E01.

## Why JPMI matters

Public discussion often collapses “the laptop” into a collection of emails, photographs, and documents. JPMI is useful because it preserves a much broader evidentiary context.

Instead of asking only:

> Is this document present?

JPMI allows questions such as:

- Where in the Mac user tree was it represented?
- What application or database surrounded it?
- What other files share the same directory context?
- What filesystem identifiers and timestamps are associated with it?
- Does the copied volume contain ordinary system-generated state around the user data?
- When was the destination filesystem created?
- What later handling or indexing activity is visible?

That is the distinction between **content evidence** and **provenance evidence**.
