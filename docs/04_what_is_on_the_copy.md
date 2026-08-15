# 4. What Is on the JPMI Copy?

> **Encyclopedia.** Nerd-depth census: [Contents census](CONTENTS_CENSUS.md). Generated rollup: [environment report](../build/reports/02_os_version.md). [Index](INDEX.md).

JPMI is best understood as a **Mac user environment inside a later HFS+ custody volume**, not as a folder containing only the files that later became newsworthy.

The current inventory contains **576,249 paths**.

## The top-level picture

The inventory is divided between the user tree and filesystem/disk structures.

From [`build/file_tree/02_top_level_summary.tsv`](../build/file_tree/02_top_level_summary.tsv):

| Area | File rows | Approx. bytes represented |
|---|---:|---:|
| `Users` | 572,743 | 215.5 GB |
| HFS+ data-partition structures | 3,435 | 283.0 GB |
| EFI System Partition | 6 | 209.7 MB |
| GPT/unpartitioned structures | 7 | 134.3 MB |

The large HFS+ structural byte total includes filesystem-level objects and unallocated-space representations; it should not be added to the user-tree total and described as unique user content.

## The `roberthunter` home directory

The principal user environment has the familiar layout of a Mac home folder.

From [`build/file_tree/03_home_overview.tsv`](../build/file_tree/03_home_overview.tsv):

| Directory | File rows | Approx. represented size |
|---|---:|---:|
| `Library` | 251,863 | 54.8 GB |
| `Documents` | 119,794 | 23.2 GB |
| `Pictures` | 92,393 | 61.0 GB |
| `Movies` | 61,202 | 9.4 GB |
| `Downloads` | 23,415 | 19.8 GB |
| `Music` | 19,313 | 32.2 GB |
| `Desktop` | 4,654 | 15.1 GB |
| Other home-level entries | smaller populations | — |

This distribution is important. The Desktop is only one part of the copy. Most of the file population lives where a working Mac normally stores application and user state: especially `Library`, `Documents`, and `Pictures`.

## Communications and contacts

The JPMI file inventory contains large populations of Apple communications artifacts.

The source characterization reports approximately:

- **128,842 `.emlx`** Apple Mail message files;
- **77,907 `.vcf`** contact files;
- substantial Mail database and attachment state;
- message databases and archived chat material;
- account and cloud-related state under the user Library.

An `.emlx` file is Apple's on-disk representation of an individual Mail message. The presence of large Mail directory structures is materially different from receiving a flat export of selected emails.

## Photographs, videos, and media

The copy contains large `Pictures`, `Movies`, and media populations. These include user media as well as application-generated derivatives such as thumbnails, proxies, databases, and cached representations.

A forensic count should therefore distinguish:

- an original photograph;
- a thumbnail of that photograph;
- a Photos-library derivative;
- a message attachment containing the same image;
- a cached or exported copy;
- a hard-linked or aliased representation.

Raw file counts are not the same as counts of unique human-created items.

## Mobile-device and cloud material

The Mac user environment contains data associated with Apple mobile-device backups, iCloud/CloudKit state, downloaded cloud material, and third-party recovery software.

That explains why files in JPMI can predate the particular laptop or destination volume on which they were eventually stored. Apple users routinely migrate data forward across Macs and restore or synchronize data from iPhones, iPads, iCloud, Mail providers, and backups.

This is also why a historical diagnostic package from an older Mac should not automatically be treated as proof that the older Mac was the computer later brought to the repair shop.

## Application state

A large fraction of the copy lives under `Library` because macOS applications store their working state there.

Examples include:

- Apple Mail stores and message files;
- Contacts/address-book material;
- Photos databases and derivatives;
- CloudKit/iCloud state;
- preferences and property lists;
- SQLite databases and their WAL/SHM companions;
- caches;
- application support directories;
- saved application state;
- browser/application metadata;
- device synchronization and backup records.

These machine-generated artifacts are often more useful for provenance than a standalone document because they show how files were embedded in a functioning application environment.

## Filesystem-level structures

Outside the ordinary user folders, JPMI also represents storage structures that are not normal “documents” at all:

- GPT partition records;
- EFI System Partition records;
- HFS+ journal and journal-information block;
- `.Spotlight-V100` indexes;
- `.DocumentRevisions-V100` state;
- `.DS_Store` Finder metadata;
- `.Trashes` and temporary-item structures;
- filesystem catalog and CNID relationships;
- unallocated ranges.

Those structures help answer questions about copying, mounting, browsing, indexing, and later handling.

## Hash coverage

The published inventory reports **331,906 inventory paths with SHA-256 values**. The deeper rank-1 manifest contains **655,330 path-level hash records**, while the CNID mapping contains **397,440 unique catalog entries**.

Those numbers differ because a filesystem can represent the same underlying object through multiple paths, aliases, hard links, or report layers. The repository therefore avoids using one raw row count as though it were a count of unique files.

## What is not byte-accessible in this GitHub repository

The public project is a metadata/hash witness. It does not publish the restricted JPMI E01 image.

Accordingly, the repository can directly publish:

- reported paths;
- sizes;
- timestamps;
- hashes from the received manifests;
- CNIDs and hierarchy;
- partition and volume identity;
- aggregate counts;
- later filesystem-state indicators.

It should not pretend that every object in the source image has been independently opened and parsed from bytes in this GitHub checkout.

## Bottom line

The JPMI copy looks like a **broad Mac data environment with filesystem context**, not a small collection assembled only for publication.

That does not answer every authenticity or custody question by itself. It does, however, provide the structural context needed to ask those questions correctly.
