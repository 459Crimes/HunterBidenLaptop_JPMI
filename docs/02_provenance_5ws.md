# 2. JPMI Provenance — The 5 Ws and How

> **Encyclopedia.** [People](PEOPLE.md) · [The Mac Shop](THE_MAC_SHOP.md) · [Exhibits](EXHIBITS.md) · [Congressional reports](CONGRESS.md) · [Copy lineages](COPY_LINEAGES.md) · [Source matrix](09_source_matrix.md) · [Index](INDEX.md).

Provenance means the history and identity of evidence: **who handled it, what it is, when relevant events occurred, where those events occurred, why the copy exists, and how the copy was made or preserved.**

For JPMI, some of those answers are established directly by the forensic records. Others are known only at a broader historical level. A few remain unresolved.

## Who?

### Original user context

The copied Mac environment is organized principally around the account:

```text
JPMI://Users/roberthunter/
```

The account contains the ordinary mixture expected from a long-used Apple environment: Mail, contacts, documents, photographs, movies, downloads, messages, application support, iCloud-related state, mobile-device material, preferences, and caches.

The user-tree structure is evidence about the account and the copied environment. It is not proof that one human personally created every file represented inside that environment. Email attachments, cloud downloads, mobile-device backups, application caches, and migrated material can all be stored inside one user account.

### Repair-shop custodian

John Paul Mac Isaac operated the Wilmington, Delaware computer repair shop associated with the April 2019 recovery event. JPMI is named for the copy lineage attributed to his custody.

### Later forensic custody

The acquisition metadata supplied to this project identifies a later physical source as a **Micron Crucial X6 SSD**, serial `2145E498755E`, represented by the forensic image record `HB-IMAGE-2022-04-29.E01`.

The restricted source image is retained outside this GitHub repository. This repository publishes derived metadata, manifests, reports, and validation artifacts.

## What?

JPMI is not a loose directory of selected newsworthy files.

It is a **partitioned Mac storage environment** with:

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

There is no single “JPMI date.” Different dates describe different events, and one pair of dates in the delivered records is not presently reconciled.

| Date / period | What the record reports | Evidentiary meaning |
|---|---|---|
| Years before 2019 | User, application, cloud, device, and migrated data represented inside the account | Historical content can predate the computer or destination volume that ultimately stored it |
| April 2019 | Repair-shop period publicly associated with the computer | Historical custody event; not a universal cutoff for every filesystem timestamp |
| 2019-09-26 | Reported HFS+ volume creation: `2019-09-26 22:59:02 CDT` | Supports creation or reconstruction of the later HFS+ destination after the April repair event |
| 2020 | Limited later metadata changes, including `.DS_Store` activity | Evidence of later interaction with a represented working volume or copy stage |
| 2022-03 / 2022-04 | Very large accessed-time clusters | Consistent with broad software examination/acquisition activity; not original-user activity |
| 2022-04-29 | Reported acquisition date / image name | The acquisition record identifies `HB-IMAGE-2022-04-29.E01` |
| 2024-11-21 | Reported HFS+ last-write and Spotlight/index activity | **Chronology discrepancy:** this cannot be a later write to an immutable E01 actually acquired in 2022; the source/report lineage must be reconciled |
| 2026-07-22 | Project database acquisition-record creation time | Project ingestion/recordkeeping date, not the date the physical evidence was originally copied |

### The 2022/2024 discrepancy

The delivered metadata simultaneously reports an E01 acquisition associated with April 29, 2022 and a volume last-write on November 21, 2024.

Those facts cannot both describe a simple chronology in which one immutable E01 was acquired in 2022 and never regenerated. At least one additional fact is missing—for example, a later acquisition, later examination of the source device, regenerated reports from a later working copy, or a mislabeled/mixed report field.

The current evidence does **not** establish which explanation is correct.

A provenance analysis therefore preserves both reported values and flags the conflict. The 2024 value is not converted into “activity after the 2022 E01 acquisition.”

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

The questions it answers:

1. What storage object was examined?
2. What Mac filesystem structure does it contain?
3. What user and application environment does it preserve?
4. What timestamps describe original activity versus later custody or report activity?
5. Which conclusions are direct observations and which remain inferences?

## How?

Three operations, not one command. Full evaluation: [How the files left the laptop](COPY_METHOD.md).

1. **April 2019.** Quote #7469 and Mac Isaac’s account: recover to the **store server**, then the customer external drive. Tool unnamed; server logs not held. Not reconstructed as a sector copy of the laptop partition.
2. **26 September 2019.** New HFS+ `Untitled`. Timestamp-preserving **file-aware** copy of `roberthunter` (created times remain 2016–March 2019; only ~15 September-created objects). Symlinks preserved; destination hard-link private directories empty.
3. **After August 2020.** **Volume clone** of `Untitled` onto the Crucial X6 (product announced 25 August 2020). **29 April 2022** E01 of that X6 (ADI). The E01 is a forensic image of the **custody stick**, not of the 2019 laptop SSD.

The exact relationship between that 2022-labeled image record and the separately reported 2024 volume last-write remains unresolved.

## Provenance confidence table

| Proposition | Confidence from current JPMI records |
|---|---|
| The analyzed custody device is a 500 GB-class Crucial X6 USB SSD | **Directly reported** |
| The acquisition record identifies `HB-IMAGE-2022-04-29.E01` | **Directly reported** |
| The destination uses GPT + EFI + journaled HFS+ | **Directly reported** |
| The primary user tree is `JPMI://Users/roberthunter` | **Directly observed in inventory** |
| The HFS+ destination was created after the April 2019 repair event | **Supported by reported 2019-09-26 volume creation** |
| The represented copy lineage contains post-2019 system-state timestamps | **Directly reported** |
| The 2024 last-write occurred inside an immutable E01 actually acquired in 2022 | **Not supported; chronology is internally unresolved** |
| The final external SSD is the original laptop SSD | **Not supported; it is a later custody medium** |
| The laptop partition was sector-copied onto `Untitled` | **Contradicted for the examined volume** (new format date, empty hard-link dirs, home-only tree) |
| `Untitled` was formatted 26 Sep 2019 and populated by a file-aware copy | **Supported by volume header + preserved user timestamps + empty hard-link dirs** |
| The Crucial X6 is the original 26 Sep 2019 format target | **Not supported; X6 is a 2020+ product — later volume clone** |
| Every file timestamp represents Hunter Biden activity | **Not supported** |
| Every pre-2019 artifact originated on the particular 2019 repair-shop Mac | **Not established; migration, cloud sync, backups, and older devices can preserve earlier material** |
