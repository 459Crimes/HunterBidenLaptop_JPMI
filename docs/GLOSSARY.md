# Glossary

> **Hatnote.** Terms of art used in the JPMI encyclopedia. For a tutorial in reading order, see [Filesystem for non-experts](05_filesystem_for_non_experts.md). For evidence classes and terminology, see [Sourcing and terminology](MANUAL_OF_STYLE.md).

## 459Crimes

Publisher of this encyclopedia. **Marc Aaron DeGiovanni** (also **Marc De Giovanni**). Also *[Beyond the Diary](https://BeyondTheDiary.com)* and the [digital diary release](https://ShowersWithMy.Dad). See [Author](AUTHOR.md). Not a JPMI filesystem term.

## Acquisition

The recorded forensic imaging event. JPMI’s acquisition record names tool **ADI4.7.1.2**, case **HB-2022-04-29**, image **HB-IMAGE-2022-04-29.E01**, and image hashes. `created_at` in the same table is this **project’s database ingest time** (2026-07-22), not the 2019 copy date.

## Alias / hard link

Multiple paths can name one catalog object. The alias map has **655,330** rows: **332,097** canonical and **323,233** alias rows; `max_paths_for_cnid` is **2**.

Those two-path CNIDs are **all** TSK `file` + `file-*-slack` (same CNID, slack size 0). They are **not** Unix hard links. HFS+ `^^^^HFS+ Private Data` and `.HFS+ Private Directory Data` exist at volume root and have **zero children**, so this volume has **no live file or directory hard links**. Duplicate SHA-256 on different CNIDs is repeated content (Dr.Fone dumps, iMovie templates, Mail attachments), not a map of broken `ln` pairs. Evaluation: [COPY_METHOD](COPY_METHOD.md).

## BOOT01

Project name for the Mac Isaac **bootable** copy that contains macOS **10.14.6 / 18G103**. Created **after 26 Sep 2019** (the public ship date of that build). The 19–21 Sep mtimes on `SystemVersion.plist` and ~26k System/Applications files are **Apple payload dates**, not BOOT01’s create date. **COSTELLO** received this lineage, **not JPMI**. See [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md).

## Allocated / unallocated

Allocated space belongs to currently represented filesystem objects. JPMI reports ~**280 GB** of unallocated *ranges*. That is a storage-state category, not a count of recoverable deleted user files.

## APFS (459Crimes corpus name)

Hayes SanDisk **bootable** macOS (`HB Boot Drive`). **TRIMARCO → APFS** conversion date unknown; CCC snapshots **5 Jan 2021**. After that date the node fans out to **MARYMAN**, **GUSTAV**, and **TODD → HAYES**. Not a clone of JPMI `Untitled`. See [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md).

## APFS*

**Jun 2022** / MEGA **13 Jun 2022** Hayes `RHB_Boot.imgc` sent to **Marc Aaron DeGiovanni**. Downstream of **HAYES**. Not JPMI.

## GUSTAV

**Gus Dimitrelos** APFS-family examination for the Washington Examiner (**May–Jun 2022**). After **5 Jan 2021**. Not JPMI.

## HAYES

Conan Hayes working copies, after **5 Jan 2021**, from **TODD**. Splits to **MPOLO** (Jun 2021 bootable laptop) and **APFS*** (Jun 2022 to DeGiovanni).

## MARYMAN

Maryman & Associates imaging **4 Apr 2021** of SanDisk `20142M400253`. APFS-family, after **5 Jan 2021**. Not JPMI.

## MPOLO

Marco Polo’s claimed receipt **Jun 2021** (report p. 579): Hayes **bootable laptop**, not JPMI.

## TODD

Sanders’s APFS-family working copy after **5 Jan 2021**, distinct from the Della Rocca **JPMI** packet. Points to **HAYES**.

## CNID (Catalog Node ID)

HFS+ internal identity for a catalog object, more stable than a filename. JPMI’s CNID map: **397,440** unique entries after deduplication (**65,343** directories, **332,097** files, max depth **19**).

## Copy method

How the examined JPMI disk was built, in three operations. See [COPY_METHOD](COPY_METHOD.md).

| Term | Meaning here |
|---|---|
| **File-aware copy** | Files and folders written onto a formatted volume. New catalog IDs. Created/modified times can be preserved. This is how `Untitled` received `roberthunter` on **26 Sep 2019**. |
| **Volume clone** | The whole formatted volume copied onto another disk (headers, files, free space). This is how the 2019 `Untitled` header appears on the Crucial X6, a **2020+** product. |
| **Forensic image (E01)** | Bit-stream image of the custody stick for analysis. `HB-IMAGE-2022-04-29.E01` images the **X6**, not the laptop SSD. |

Formatting a Mac disk as journaled HFS+ always creates GPT, EFI, and a journal; that is destination machinery, not a sector copy of the laptop.

## `.DS_Store`

Hidden Finder folder-view file. A later `.DS_Store` mtime is a **handling indicator** (directory opened or view state changed). It is not, by itself, an edited document.

## DocumentRevisions (`.DocumentRevisions-V100`)

macOS document-versioning system state. Later writes here show the volume was mounted in a Mac environment. They are not automatically new Hunter documents.

## E01

A common forensic disk-image container (Expert Witness / EnCase format family). It is meant to wrap an acquisition with metadata and integrity information. See [Forensic image](FORENSIC_IMAGE.md).

## EFI System Partition

Small GPT partition used for firmware/boot machinery. JPMI has one (GUID `54bcfba5-c609-44c0-a45d-b07090d2c996`). Presence shows partitioned Mac-oriented layout, not that this USB disk was booted at a particular moment.

## Extra Found Files (0728)

**Completely separate corpus** from JPMI, APFS, and GAI. Hayes MEGA bag after **28 July 2021** (dashed distribution edge from **HAYES**, not volume identity). Blobs match **every combination** of those three inventories (all three, each pair, each singleton, and none). A large share has **original names and metadata stripped**, so path provenance is unknown. Out of scope. See [Copy lineages](COPY_LINEAGES.md#0728-is-a-separate-corpus).

## `.emlx`

Apple Mail on-disk message file. Characterization reports ~**128,847** `.emlx` **paths**. Extension-distribution TSV counts differ because of slack rows, path vs extension rules, and Mail attachments living beside `.emlx` files.

## GPT

GUID Partition Table — the map of partitions on the disk. JPMI disk GUID: `c93db56d-6e88-4965-94e5-8585a013d086`.

## Hash (SHA-256, MD5, SHA-1)

A cryptographic fingerprint. **Image** MD5/SHA-1 are acquisition hashes of the E01. **Object** SHA-256 values in this repo are **received manifest evidence**, not hashes this GitHub checkout recomputed from restricted source bytes.

## HFS+

Hierarchical File System Plus, Apple’s journaled filesystem used here for the data volume named `Untitled`. APFS is **not** the destination filesystem in the JPMI acquisition record.

## Journal

HFS+ transaction log. JPMI reports `.journal` at **41,943,040** bytes, created with the volume in September 2019. Ordinary PDF/email folder copies do not need a native HFS+ journal.

## JPMI

**John Paul Mac Isaac copy** — this project’s name for the examined direct-copy **lineage**, not the person.

## Path

Human-readable location inside a named copy (`JPMI://Users/roberthunter/Library/Mail/...`). Not the same as byte identity or CNID.

## Source URI

Published file citations use a corpus-root scheme rather than a working-tree prefix:

| Scheme | Copy |
|---|---|
| `JPMI://` | This copy. Rewritten from inventory `jpmi_metadata/` |
| `APFS://` | Hayes bootable APFS descendant |
| `GAI://` | GAI truncated HFS+ image (`hb.img`) |
| `0728://` | Extra Found Files / 0728 |

This repository’s tables are JPMI-only. The other schemes exist so a path from another copy is not mistaken for a JPMI row.

## Rank-1 / rank-2 manifest

Internal report-layer labels in the acquisition notes. The note `hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)` is a **delivery attribution**, not a description of Hunter-era activity. TSK = The Sleuth Kit.

## Slack (`*.jpg-slack`, etc.)

Filesystem slack / remnant representations in some inventories. Slack rows often have size 0 and inflate extension counts. They are not included in photograph counts.

## Spotlight (`.Spotlight-V100`)

macOS search index. Store-V1 appears at volume creation (Sep 2019). Store-V2 UUID `3DEE7E1E-F78C-4768-B492-D2485F7ADCBA` is heavily written in **2022** and **2024** — examination/indexing, not original-user authorship.

## Timestamp (created / modified / accessed)

Three different fields. Copies, restores, Finder, Spotlight, AV, and forensic tools can move some of them. Interpret by **cluster and object type**. See [Timestamps](TIMESTAMPS.md).

## TSK timeline

The Sleuth Kit bodyfile-style event stream. JPMI has **1,259,300** TSK timeline rows. That is not 1.26 million unique user files.

## Volume identifier

HFS+ volume id reported as `dfe8079582e21400` for `Untitled`.

## See also

- [Filesystem for non-experts](05_filesystem_for_non_experts.md) (copy method)
- [How the files left the laptop](COPY_METHOD.md)
- [Data contract](../DATA_CONTRACT.md)
