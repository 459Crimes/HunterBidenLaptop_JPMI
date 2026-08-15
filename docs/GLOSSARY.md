# Glossary

> **Hatnote.** Terms of art used in the JPMI encyclopedia. For a tutorial in reading order, see [Filesystem for non-experts](05_filesystem_for_non_experts.md). For evidence classes and terminology, see [Sourcing and terminology](MANUAL_OF_STYLE.md).

## 459Crimes

Publisher of this encyclopedia. **Marc Aaron DeGiovanni** (also **Marc De Giovanni**). Also *[Beyond the Diary](https://BeyondTheDiary.com)* and the [digital diary release](https://ShowersWithMy.Dad). See [Author](AUTHOR.md). Not a JPMI filesystem term.

## Acquisition

The recorded forensic imaging event. JPMI’s acquisition record names tool **ADI4.7.1.2**, case **HB-2022-04-29**, image **HB-IMAGE-2022-04-29.E01**, and image hashes. `created_at` in the same table is this **project’s database ingest time** (2026-07-22), not the 2019 copy date.

## Alias / hard link

Multiple paths can name one catalog object. The alias map has **655,330** rows: **332,097** canonical and **323,233** alias rows; `max_paths_for_cnid` is **2**. This is why path counts exceed CNID counts.

## Allocated / unallocated

Allocated space belongs to currently represented filesystem objects. JPMI reports ~**280 GB** of unallocated *ranges*. That is a storage-state category, not a count of recoverable deleted user files.

## APFS (459Crimes corpus name)

In other 459Crimes reports, **APFS** names a **later, more altered copy of the JPMI disk**, used as a **bootable laptop** produced by **Conan Hayes**. Marco Polo analyzed that machine. **Dimitrelos** and **Maryman** used copies whose structure **correlates to this corpus**. It is **not** the JPMI HFS+ volume `Untitled` / E01 in this repo. The corpus label is distinct from Apple’s APFS format in the abstract.

## CNID (Catalog Node ID)

HFS+ internal identity for a catalog object, more stable than a filename. JPMI’s CNID map: **397,440** unique entries after deduplication (**65,343** directories, **332,097** files, max depth **19**).

## `dd`-style

Public analogy: whole-volume / filesystem-preserving copy rather than a folder dump. **Not** proof that the Unix `dd` program was used.

## `.DS_Store`

Hidden Finder folder-view file. A later `.DS_Store` mtime is a **handling indicator** (directory opened or view state changed). It is not, by itself, an edited document.

## DocumentRevisions (`.DocumentRevisions-V100`)

macOS document-versioning system state. Later writes here show the volume was mounted in a Mac environment. They are not automatically new Hunter documents.

## E01

A common forensic disk-image container (Expert Witness / EnCase format family). It is meant to wrap an acquisition with metadata and integrity information. See [Forensic image](FORENSIC_IMAGE.md).

## EFI System Partition

Small GPT partition used for firmware/boot machinery. JPMI has one (GUID `54bcfba5-c609-44c0-a45d-b07090d2c996`). Presence shows partitioned Mac-oriented layout, not that this USB disk was booted at a particular moment.

## Extra Found Files (0728)

Out of scope. MEGA share from **Conan Hayes after 28 July 2021**. Did **not** come from the laptop files per se: a large collection **related to** laptop material, with many items of unknown origin and some **completely unknown to the laptop**. Marco Polo had this sidecar set in addition to Hayes’s bootable APFS machine; it did **not** analyze JPMI. Author’s FBI referral (`FBI_0728_Source_Attribution_Referral_FINAL_2026-07-28.pdf`) is **not** analyzed here. See [Scope](SCOPE.md) and [Author](AUTHOR.md).

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

Human-readable location (`Users/roberthunter/Library/Mail/...`). Not the same as byte identity or CNID.

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

- [Filesystem for non-experts](05_filesystem_for_non_experts.md)
- [Data contract](../DATA_CONTRACT.md)
