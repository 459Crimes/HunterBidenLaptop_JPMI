# 2. JPMI Provenance — The 5 Ws and How

Provenance means the history and identity of evidence: **who handled it, what it is, when relevant events occurred, where those events occurred, why the copy exists, and how the copy was made or preserved.**

For JPMI, some of those answers are established directly by the forensic records. Others are known only at a broader historical level. A few remain unresolved.

## Who?

### Original user context

The copied Mac environment is organized principally around the account:

```text
Users/roberthunter/
```

The account contains the ordinary mixture expected from a long-used Apple environment: Mail, contacts, documents, photographs, movies, downloads, messages, application support, iCloud-related state, mobile-device material, preferences, and caches.

The user-tree structure is evidence about the account and the copied environment. It should not be confused with proof that one human personally created every file represented inside that environment. Email attachments, cloud downloads, mobile-device backups, application caches, and migrated material can all be stored inside one user account.

### Repair-shop custodian

John Paul Mac Isaac operated the Wilmington, Delaware computer repair shop associated with the April 2019 recovery event. JPMI is named for the copy lineage attributed to his custody.

### Later forensic custody

The acquisition metadata supplied to this project identifies a later physical source as a **Micron Crucial X6 SSD**, serial `2145E498755E`, represented by the forensic image `HB-IMAGE-2022-04-29.E01`.

The project metadata notes that the restricted source image is retained outside this GitHub repository. This repository publishes derived metadata, manifests, reports, and validation artifacts.

## What?

JPMI is not presented here as a loose directory of selected newsworthy files.

It is represented as a **partitioned Mac storage environment** with:

- GPT disk structure;
- EFI System Partition;
- journaled HFS+ data partition;
- HFS+ volume identifier `dfe8079582e21400`;
- main volume name `Untitled`;
- HFS+ sector offset `409634`;
- HFS+ journal and journal-information block;
- filesystem catalog hierarchy;
- CNIDs and parent relationships;
- Spotlight and DocumentRevisions structures;
- a conventional `roberthunter` home tree;
- file hashes and timestamp inventories.

The inventory presently contains **576,249 paths**.

## When?

There is no single “JPMI date.” Different dates describe different events.

| Date / period | What it represents | Evidentiary meaning |
|---|---|---|
| Years before 2019 | User, application, cloud, device, and migrated data represented inside the account | Historical content can predate the computer or destination volume that ultimately stored it |
| April 2019 | Repair-shop period publicly associated with the computer | Historical custody event; not a universal cutoff for every filesystem timestamp |
| 2019-09-26 | Reported HFS+ volume creation: `2019-09-26 22:59:02 CDT` | Strong evidence that the later HFS+ destination was created or reconstructed after the April repair event |
| 2020 | Limited later metadata changes, including `.DS_Store` activity | Evidence that the copied volume was later mounted/browsed or otherwise interacted with |
| 2022-03 / 2022-04 | Very large accessed-time clusters | Consistent with later examination/acquisition activity; not original-user activity |
| 2022-04-29 | Reported E01 acquisition date / image name | The later forensic preservation event represented by `HB-IMAGE-2022-04-29.E01` |
| 2024-11-21 | Reported HFS+ last-write and Spotlight/index activity | Evidence of still later filesystem/index handling |
| 2026-07-22 | Project database acquisition-record creation time | Project ingestion/recordkeeping date, not the date the physical evidence was originally copied |

A provenance analysis fails if those events are collapsed into one timeline.

## Where?

The public historical repair event is associated with **Wilmington, Delaware**.

The later forensic acquisition record identifies the physical custody medium by device model and serial number, not by a public geographic location.

This GitHub repository contains **derived forensic records**, not the restricted E01 image itself.

## Why?

There are two separate “why” questions.

### Why does the copy lineage exist?

Because data was recovered from a computer brought to a repair shop and later preserved outside that original hardware.

### Why does this repository exist?

To document that specific copy as an evidence source without requiring the reader to know the rest of the broader laptop-data ecosystem.

The goal is to answer:

1. What storage object was examined?
2. What Mac filesystem structure does it contain?
3. What user and application environment does it preserve?
4. What timestamps describe original activity versus later custody activity?
5. Which conclusions are direct observations and which remain inferences?

## How?

The exact original repair-shop copy utility is unresolved.

The evidence does support a more bounded statement: the JPMI lineage preserved far more than a curated user-document folder. The represented destination includes native Mac filesystem and indexing structures, a normal home hierarchy, filesystem catalog relationships, and unallocated space.

For non-specialists, **“`dd`-style clone”** is therefore a useful analogy for the evidentiary form, provided it is immediately qualified:

> The phrase means a whole-volume or filesystem-preserving copy lineage. It does not assert that the Unix `dd` command was literally used or that every block on the final Crucial X6 came directly from the original laptop SSD in one operation.

The later preservation step is clearer: the custody device is represented by an **E01 forensic image** with recorded acquisition hashes.

## Provenance confidence table

| Proposition | Confidence from current JPMI records |
|---|---|
| The analyzed custody device is a 500 GB-class Crucial X6 USB SSD | **Directly reported** |
| The forensic image is `HB-IMAGE-2022-04-29.E01` | **Directly reported** |
| The destination uses GPT + EFI + journaled HFS+ | **Directly reported** |
| The primary user tree is `Users/roberthunter` | **Directly observed in inventory** |
| The HFS+ destination was created after the April 2019 repair event | **Supported by reported 2019-09-26 volume creation** |
| The volume experienced later handling/indexing | **Supported by 2020, 2022, and 2024 metadata** |
| The final external SSD is the original laptop SSD | **Not supported; it is a later custody medium** |
| Mac Isaac literally used `dd` | **Not established** |
| Every file timestamp represents Hunter Biden activity | **Not supported** |
| Every pre-2019 artifact originated on the particular 2019 repair-shop Mac | **Not established; migration, cloud sync, backups, and older devices can preserve earlier material** |
