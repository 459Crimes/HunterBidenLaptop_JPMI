# 5. The JPMI Filesystem, Explained for Non-Experts

> **Encyclopedia.** Term list: [Glossary](GLOSSARY.md) (copy method). Objects: [HFS+ volume Untitled](HFS_VOLUME_UNTITLED.md) · [Forensic image](FORENSIC_IMAGE.md) · [Timestamps](TIMESTAMPS.md). Origin: [How the files left the laptop](COPY_METHOD.md). [Index](INDEX.md).

Digital-forensic reports often become unreadable because they start with filesystem terminology. This page explains only the terms needed to understand JPMI.

## Disk image

A **disk image** is a file that represents another storage device or volume.

The JPMI acquisition record identifies:

```text
HB-IMAGE-2022-04-29.E01
```

An **E01** is a common forensic-image format. It is designed to preserve a storage acquisition together with forensic metadata and integrity information.

The important public point is simple: the later JPMI custody disk was forensically preserved as an image rather than analyzed only by opening documents on the live external disk.

## Copy method

What this encyclopedia measured is **how the examined disk was built**, from HFS+ catalog identity, timestamps, empty hard-link directories, TSK slack pairs, and the Crucial X6 product date — not a named April 2019 command log.

Three operations, with different evidence:

| Operation | What it is | What JPMI shows |
|---|---|---|
| **File-aware copy** | Copy files and folders onto a formatted volume (new CNIDs; timestamps can be preserved) | `Untitled` created **26 Sep 2019**; `roberthunter` copied in; 2016–March 2019 created/modified times kept; hard-link private directories empty |
| **Volume clone** | Copy a whole already-formatted volume onto another disk (headers, allocated files, free space) | 2019 volume name/id/create date on a Crucial X6 that was **not sold until 2020** |
| **Forensic image (E01)** | Bit-stream image of a custody disk for later analysis | `HB-IMAGE-2022-04-29.E01` of that X6 (ADI), not of the 2019 laptop SSD |

GPT, EFI, and an HFS+ journal are created by **formatting a Mac disk**. They do not mean the laptop’s sectors were copied. Full evaluation: [How the files left the laptop](COPY_METHOD.md).

## GPT

**GPT** stands for GUID Partition Table.

A physical disk can be divided into partitions. GPT is the map that records where those partitions begin and end.

The JPMI custody disk contains GPT structure identifying, among other things:

- an EFI System Partition;
- a large HFS+ data partition.

That is disk-level context, not ordinary user-document metadata.

## EFI System Partition

The **EFI System Partition** is a small partition used by modern computers during boot and system management.

Its presence does not prove that the JPMI external disk was successfully booted at any particular historical moment. It does show that the disk was structured as a partitioned Mac-oriented storage device rather than merely as one folder containing exported files.

## HFS+

**HFS+** is an Apple filesystem used extensively by Macs before APFS became standard.

The JPMI data partition is reported as a **journaled HFS+ volume** named:

```text
Untitled
```

with volume identifier:

```text
dfe8079582e21400
```

The HFS+ destination reports a creation time of **2019-09-26 22:59:02 CDT**.

That creation time belongs to the **destination filesystem**. It does not mean every file inside the volume was created in September 2019.

## Journal

A **journaled** filesystem keeps a transaction log that helps it recover safely from crashes or interrupted writes.

JPMI reports a roughly **40 MB HFS+ journal**.

A journal is useful provenance evidence because it is part of the filesystem's operating machinery. It is not a user document and is not normally created by simply exporting a folder of PDFs or emails.

## CNID

HFS+ assigns catalog objects a **Catalog Node ID**, or **CNID**.

A CNID is closer to an internal filesystem identity than a filename is.

Why does that matter?

A file can be renamed or represented through different paths while still being related to the same underlying catalog object. Parent-CNID relationships also allow the filesystem hierarchy to be reconstructed.

The JPMI CNID map contains **397,440 unique catalog entries** after deduplication.

## Path

A **path** is the human-readable location of a file or directory, for example:

```text
JPMI://Users/roberthunter/Library/Mail/...
```

A path is not the same thing as byte identity. Two paths can point to identical content, and one underlying file can sometimes be represented by multiple paths.

## Hash

A cryptographic **hash** is a fingerprint of data.

JPMI manifests include SHA-256 values for hundreds of thousands of represented objects.

If two byte sequences have the same properly computed SHA-256 value, that is extremely strong evidence that the byte sequences are identical.

In this repository, however, hashes are being published from received forensic manifests. Because the restricted source image is not mounted in GitHub, the repository distinguishes:

- **a hash reported by the JPMI forensic manifest**, from
- **a hash freshly recomputed from source bytes by this checkout**.

That distinction is important.

## `.DS_Store`

Finder creates hidden files called `.DS_Store` to remember folder-view information such as icon positions and display settings.

A `.DS_Store` modification can therefore show that a folder was browsed or presented to Finder.

It does **not** mean that all documents inside that folder were edited.

This is why later `.DS_Store` dates in JPMI are treated as **handling indicators**, not automatically as evidence of later document insertion.

## Spotlight

**Spotlight** is macOS's search/indexing system.

When a Mac volume is mounted, Spotlight may create or update `.Spotlight-V100` index structures.

JPMI contains Spotlight activity from later custody periods, including 2022 and 2024.

That activity demonstrates that the volume was later processed by macOS indexing. It does not by itself identify the person who mounted it or establish that user documents were created at that time.

## DocumentRevisions

`.DocumentRevisions-V100` is macOS system state associated with document-versioning behavior.

Its appearance or modification can be another indicator that the volume was mounted and used by a Mac environment after the original user period.

Again, system metadata activity is not synonymous with substantive content manipulation.

## Allocated and unallocated space

**Allocated space** belongs to currently represented filesystem objects.

**Unallocated space** is storage that is not currently assigned to an active file. It may contain remnants of older data, overwritten fragments, or empty regions.

The JPMI source reports approximately **280 GB of unallocated ranges**.

That figure is relevant to forensic recovery, but it is not 280 GB of recoverable deleted Hunter Biden files. Unallocated space is a storage-state category, not a content classification.

## Created, modified, and accessed times

Filesystems commonly record multiple timestamps.

- **Created**: when an object was created on the relevant filesystem, depending on the field and copy history.
- **Modified**: when file content or a filesystem object's metadata was last changed, depending on the object.
- **Accessed**: when the object was read or traversed, if access-time tracking is active.

Copies, restores, migrations, mounting, indexing, antivirus tools, forensic tools, and Finder can all affect some timestamps.

That is why JPMI timestamp interpretation is done by **clusters and object type**, not by assuming every timestamp means “Hunter Biden used this file at this exact moment.”

## The practical rule

For public reading, the sequence is:

1. **What object is this?** User document, application database, filesystem metadata, index, cache, or partition structure?
2. **Where is it?** What path and directory context surround it?
3. **What identity does it have?** Size, CNID, hash, volume?
4. **Which timestamp is being examined?** Created, modified, accessed, volume creation, or last write?
5. **Could the timestamp have been produced by later handling?**
6. **What conclusion does the evidence actually support?**

This method is slower than treating every timestamp as self-explanatory, but far more defensible.
