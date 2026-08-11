# JPMI Source Characterization Report

**Date:** 2026-08-04  
**Project:** RHB Extra  
**Authoritative database:** PostgreSQL `rhb_forensics`  
**Primary source:** PostgreSQL source `122`, `JPMI Metadata HB-FileList-2022-04-v1`  
**Related source materials:** `source/JPMI_metadata/`

## Executive Summary

The JPMI material available to this project is a metadata and hash witness for a GPT-partitioned Mac storage device attributed to the Mac Isaac custody lineage. It is not a byte-accessible image in this project, but the supplied partition reports, HFS+ catalog exports, file lists, timeline, and SHA-256 manifests provide substantial structural evidence.

The source is best characterized as a **large, conventional macOS HFS+ volume containing a normal `roberthunter` home directory and substantial system/application state**. It is not merely a flat collection of user files and it does not resemble the later Trimarco-style copy described as having everything placed on the Desktop.

The partition and filesystem evidence is more consistent with a **filesystem-level or metadata-preserving copy/reconstruction of a Mac volume**, followed by later mounting, indexing, copying, or forensic handling, than with an ordinary Finder drag-and-drop of `Users/roberthunter` into an otherwise empty partition.

The evidence does not prove the exact copy tool or custody event. It does establish that:

- the volume has GPT and EFI structures;
- the data partition is journaled HFS+;
- the HFS+ catalog has a coherent CNID and parent relationship structure;
- system metadata, Spotlight, document-revision, journal, Mail, Photos, CloudKit, and application-support material are present;
- the user data is organized as a normal macOS home tree;
- the volume contains later system and metadata activity after the main 2017-2019 user-data period;
- the JPMI source was not an untouched, post-April-2019 time capsule.

## Source And Evidentiary Boundary

The project does not possess the JPMI device bytes. Todd Sanders retains the restricted source image, and the project holds metadata deliveries and derived manifests. The current evidence therefore supports different conclusions at different levels:

| Evidence type | What it can establish | What it cannot establish alone |
|---|---|---|
| Partition report | GPT layout, partition identities, offsets, device and volume identifiers | Full content authenticity or exact copy operation |
| HFS+ catalog/CNID export | Directory relationships, allocated entries, filesystem organization | Whether every catalog entry was present at an earlier custody date |
| File-list report | Paths, sizes, timestamps, types, permissions, selected status fields | Byte identity without hashes |
| SHA-256 manifest | Exact identity of the hashed objects represented in the manifest | Identity of objects omitted from the manifest or unavailable as bytes |
| TSK timeline | Broad mtime distribution and system-state timing | Which person or tool caused each timestamp |
| Later 2022/2024 system entries | Evidence of later filesystem or examiner activity | User intent or substantive document creation |

The report therefore uses phrases such as “consistent with,” “supports,” and “does not prove” deliberately.

## Physical And Partition Structure

The later acquisition and partition report identifies the JPMI physical source as:

| Field | Reported value |
|---|---|
| Device | Micron Crucial X6 SSD, USB |
| Serial | `2145E498755E` |
| Reported source image | `HB-IMAGE-2022-04-29.E01` |
| Acquisition reported in source material | 2026-07-22 |
| Disk size | 476,940 MB / 976,773,168 sectors |
| Sector size | 512 bytes |
| Disk GUID | `c93db56d-6e88-4965-94e5-8585a013d086` |
| EFI partition GUID | `54bcfba5-c609-44c0-a45d-b07090d2c996` |
| HFS+ partition GUID | `cf0fd7cc-b0c0-4667-affd-d1627e93c654` |
| HFS+ sector offset | `409,634` |
| Main volume | `Untitled` |
| HFS+ volume identifier | `dfe8079582e21400` |
| Filesystem | Journaled HFS+ |
| Reported volume creation | 2019-09-26 22:59:02 CDT |
| Reported last write | 2024-11-21 17:40:22 CST |

The partition map is reported as:

1. A small EFI System Partition.
2. A large HFS+ data partition named `Untitled`.
3. GPT and protective/structural records in unpartitioned space.

The initial file-list analysis counted:

| Partition/area | Rows |
|---|---:|
| HFS+ `Untitled` data partition | 576,219 |
| EFI System Partition | 8 |
| GPT/unpartitioned structural records | 8 |
| Malformed or shifted rows | 147 |

The presence of an EFI partition does not independently prove that the device was bootable at the relevant custody date. It does show that the inventory represents a partitioned Mac-oriented storage layout rather than only a copied directory tree.

## HFS+ Filesystem Evidence

The supplied TSK reports provide several indicators of a native or metadata-preserving HFS+ filesystem representation:

- journaled HFS+ filesystem type;
- HFS+ journal and journal information block;
- volume identifier and partition offset;
- CNID values;
- parent CNID relationships;
- allocated and unallocated catalog representations;
- Spotlight stores;
- DocumentRevisions databases;
- volume-level filesystem metadata;
- a normal directory hierarchy extending below `roberthunter`.

The CNID report contains:

| Metric | Value |
|---|---:|
| Total rank-3 entries | 397,440 |
| Regular files | 325,103 |
| Directories | 65,343 |
| Entries under `roberthunter/` | 397,320 |
| CNID-map rows before deduplication | 728,348 |
| Unique CNIDs after deduplication | 397,440 |
| Allocated rows | 727,668 |
| Unallocated pseudo-ranges | 680 |

The rank-5 TSK timeline contains 1,259,300 rows, including approximately 1,259,079 under `roberthunter/`. The timeline is broader than the narrower file-list inventory because it includes system files, slack companions, unallocated pseudo-entries, and other filesystem-level records.

The reports also state that the deleted-file catalog is empty. That does not prove that no files were ever deleted. On journaled HFS+, catalog records can be destroyed or become unavailable, and the source report specifically notes that an empty deleted catalog is normal in this context. Approximately 280 GB of unallocated ranges and a 40 MB HFS+ journal remain relevant to any future carving or journal-replay work.

## User-Home Layout

The principal path is:

```text
Basic data partition (2)\Untitled [HFS+]\Untitled\roberthunter\
```

The top-level home-directory distribution is:

| Directory | Files |
|---|---:|
| `Library` | 251,864 |
| `Documents` | 119,795 |
| `Pictures` | 92,394 |
| `Movies` | 61,203 |
| `Downloads` | 23,416 |
| `Music` | 19,314 |
| `Desktop` | 4,655 |
| Other | fewer than 100 each |

This is a conventional macOS home layout. The `Library` count is consistent with a complete or broad application environment rather than a user-content-only export. It includes Mail, Contacts, Photos, application support, caches, CloudKit state, databases, and related generated objects.

The Desktop is comparatively small. It contains a recovery-style `090*` subtree of approximately 1,783 entries, but that subtree is located **inside the original Desktop**. It is not evidence that the entire source was flattened onto the Desktop.

The initial source analysis specifically distinguished this inventory from the later Trimarco-derived copy described as “bootable, everything dropped on the Desktop.” The JPMI layout is not that Desktop-only arrangement.

## Does The Source Contain System Files?

Yes. The source contains both filesystem-level system structures and macOS application/system-state files.

Examples include:

- EFI partition records;
- GPT and protective-MBR structures;
- `.journal`;
- `.journal_info_block`;
- `.Spotlight-V100`;
- Spotlight `Store-V1` and `Store-V2` data;
- Spotlight index and vector-index structures;
- `.DocumentRevisions-V100`;
- `ChunkStoreDatabase` and related WAL/slack files;
- Mail V6 and `.emlx` content;
- Contacts and `.vcf` records;
- Photos databases, proxies, and derivative files;
- CloudKit and iCloud state;
- `.DS_Store` files;
- database journals, WAL files, SHM files, and application caches;
- system/application support paths under `Library`.

The file-list extension distribution also shows the system/application character of the volume:

| Extension/type | Rows |
|---|---:|
| No extension | 150,022 |
| `.emlx` | 128,842 |
| `.vcf` | 77,907 |
| `.jpg`/`.jpeg` | 99,902 |
| `.png` | 19,665 |
| `.plist` | 14,365 |
| `.icloud` | 12,337 |

The large no-extension population is not evidence that the files are all user documents. It includes application stores, cache blobs, database components, filesystem objects, and other records whose useful identity comes from path and container context.

## Assessment Of The Copy Method

### Ordinary drag-and-drop hypothesis

An ordinary Finder drag-and-drop of a home directory into a new partition would normally be expected to produce a destination directory tree. It would not, by itself, reproduce:

- the source GPT partition map;
- an EFI partition;
- the HFS+ volume journal;
- the HFS+ catalog’s original-style CNID/parent structure;
- native volume identifiers;
- filesystem-level unallocated regions;
- native Spotlight and document-revision state in a way that explains the complete volume structure.

The JPMI evidence therefore does not resemble a simple user-space drag-and-drop package.

### Filesystem-aware or block-level copy hypothesis

The observed structure is more consistent with one of the following classes of operation:

1. a block-level clone or image of an HFS+ volume;
2. a filesystem-aware copy that preserved extensive metadata and system state;
3. a restored or reconstructed HFS+ destination populated from a prior Mac volume while retaining a broad set of native filesystem structures.

The precise operation is not established because the project does not have the JPMI bytes, acquisition logs, imaging tool logs, or a complete chain showing the source and destination at each stage.

### Relationship to the APFS branch

The APFS source documentation describes a separate external APFS branch whose construction is consistent with an HFS+ source being copied to an APFS destination through a cloning or migration mechanism. The APFS branch has its own APFS container, Preboot/Recovery/VM structures, later Spotlight boundaries, and snapshots.

That relationship should not be projected backward as proof that JPMI itself was created by a particular tool. It does, however, reinforce the broader model that this corpus contains multiple filesystem-level derivative branches rather than one directory tree repeatedly renamed.

### Water damage, proprietary SSD access, and the repair-shop server

Additional reported facts materially affect the copy-method assessment:

- the original laptop suffered water damage;
- an external, mechanical copy was reportedly made using the removable Apple SSD/NVMe blade;
- files were reportedly copied first to the repair shop's internal server rather than directly to a final external disk;
- the MacBookPro14,1 storage uses an Apple-proprietary removable SSD format and connector, not a conventional 2.5-inch drive or ordinary consumer M.2 module.

These facts make a multi-stage recovery and copying chain more plausible than a direct whole-device clone from the laptop SSD to the JPMI Crucial X6:

```text
Water-damaged MacBook
        |
        +-- Apple SSD blade accessed mechanically or through a compatible reader
        |
        +-- Recovery, imaging, or logical copy to repair-shop internal server
        |
        +-- Later external HFS+ derivative created from server-side material
             +-- JPMI / Untitled HFS+ witness
             +-- APFS / HB Boot Drive branch
             +-- Other recovery and export branches
```

The phrase “mechanical copy” should not be treated as synonymous with a direct `dd` clone to the final JPMI disk. It could describe hardware-assisted access to the removed SSD followed by one of several downstream operations:

1. A sector-level hardware clone to an intermediate image or server.
2. Hardware-assisted reading followed by a logical filesystem copy to the server.
3. A forensic image acquisition written to a server-side image store.
4. A Mac backup, migration, or filesystem-aware restore performed from the recovered data.
5. A hybrid process combining sector access, server staging, and later external-volume population.

The server-first report is significant because it removes the need for the JPMI external disk to match the original SSD geometry. The server could have held a larger image, a logical file tree, a backup set, or a recovered working copy. The later HFS+ destination could then have been freshly partitioned, formatted, resized, and populated from that intermediate source.

This model explains how the JPMI device can contain a conventional Mac tree and substantial system/application state without being a whole-device clone of the original internal SSD. It also explains why the JPMI volume can have its own 2019 creation date, journal, Spotlight stores, volume identifier, and later application metadata.

### Revised capacity-aware assessment

The original internal SSD capacity remains unresolved. The external JPMI device is approximately 500 GB decimal (`500,107,862,016` bytes), while a marketed 512 GB SSD generally means approximately `512,000,000,000` bytes rather than 512 GiB. The labels alone therefore do not prove that a source-to-destination raw clone was impossible, but a direct whole-device clone would require compatible source geometry or a source partition that fit the destination.

If the original was 256 GB, a server-mediated logical copy or filesystem-aware restore could populate a 500 GB external HFS+ volume without leaving the unused second half as a raw unallocated clone region. If the original was a 512 GB-class device, the server could likewise have held the recovered content while the external destination was created or resized independently. Neither scenario requires a direct 512-to-500 GB `dd` operation.

The updated ranking is:

- **Most supported:** proprietary SSD access followed by server-side staging and filesystem-aware HFS+ restore or clone.
- **Also plausible:** proprietary SSD access followed by a server-side forensic image and later external restoration.
- **Also plausible:** server-side logical copy followed by creation of a new HFS+ destination.
- **Possible but not established:** direct partition-level or whole-device hardware clone if the relevant source geometry fit.
- **Poorly supported:** ordinary drag-and-drop of only the home directory.

The decisive missing evidence is the repair-shop server artifact and its logs. Specifically, it would be important to determine whether the server held a sector image, a mounted logical filesystem copy, a Mac backup/migration set, or an ordinary file-tree copy. That distinction controls how much original filesystem geometry and metadata could have survived into JPMI.

### Assessment

**Most supported:** filesystem-level or metadata-preserving derivative of a Mac volume, later handled and indexed.  
**Possible but less supported:** a carefully reconstructed HFS+ filesystem populated from a user-home copy.  
**Poorly supported:** an ordinary drag-and-drop of `Users/roberthunter` into a blank partition.  
**Not proven:** the exact copy program, operator, date of copy, and whether all source blocks were preserved.

### Capacity constraint and copy-method options

The JPMI device is reported as `500,107,862,016` bytes, approximately `465.8 GiB`, which is a normal marketed 500 GB external SSD. The device size describes the later custody medium; it does not establish the capacity of the original MacBook internal NVMe.

A raw whole-device `dd` clone would require the source device to be no larger than the JPMI target. However, the capacity labels require care: a marketed 512 GB SSD generally means approximately `512,000,000,000` bytes, not 512 GiB. That is only modestly larger than a 500 GB-class device. A raw clone would still require compatible source partition geometry or a source partition that fit within the destination, but the labels alone do not establish that a raw clone was impossible.

More importantly, the observed evidence does not require a whole-device clone. Plausible mechanisms include:

1. **Filesystem-aware clone with destination resizing.** A cloning tool could copy HFS+ contents, recreate the destination partition, and resize the destination filesystem.
2. **Partition-level clone.** An operator could create a new GPT layout, create a suitably sized HFS+ partition, and restore the source data partition into it.
3. **HFS+ filesystem restore or migration.** A backup or restore tool could recreate the HFS+ volume and restore the user tree, permissions, metadata, Mail, Photos, Library, and application state.
4. **Sparse or image-based restoration.** A sparse image or backup set could be restored onto a differently sized destination without preserving the source device’s unused sectors.
5. **Copy from an earlier external HFS+ derivative.** JPMI may have been populated from an already-created external branch rather than directly from the MacBook internal NVMe.

A 256 GB source restored to a 500 GB destination would not leave the second half of the destination necessarily unused. The destination filesystem could be created larger than the source and populated through a filesystem-aware restore or copy. Conversely, a 512 GB-class source could fit a 500 GB-class destination only if the relevant source partition/used region fit or if the operation was filesystem-aware rather than a raw whole-device copy.

The reported HFS+ volume creation date, `2019-09-26`, supports the possibility that the volume was created or reconstructed on the external device. It is not proof that the complete physical layout of the original internal NVMe was retained.

**Capacity-aware assessment:**

- Most supported: filesystem-aware HFS+ clone or restore with destination sizing/resizing.
- Also plausible: copy from an earlier external HFS+ derivative.
- Also plausible: sparse/image-based restore or partition-level clone.
- Whole-device `dd`: possible only if the source geometry or copied partition fit the JPMI device; not established.
- Ordinary drag-and-drop of only the home directory: poorly supported by the filesystem evidence.

The original internal drive could have been 256 GB or 512 GB-class, depending on the exact Mac configuration. Current JPMI metadata cannot distinguish those capacities because the source NVMe geometry is not present.

## Dates And Activity After April 1, 2019

The initial file-list report states that most user-file mtimes cluster in 2017-2019:

| Modified year | Rows |
|---|---:|
| 2014 | 12 |
| 2015 | 317 |
| 2016 | 2,101 |
| 2017 | 106,877 |
| 2018 | 102,658 |
| 2019 | 360,757 |
| 2020 | 18 |
| 2022 | 120 |
| 2024 | 30 |

Using the `jpmi_file_report` table and a threshold of `2019-04-01`, there are `139` rows with later modified timestamps:

| Year | Rows after 2019-04-01 |
|---|---:|
| 2019 | 16 |
| 2020 | 13 |
| 2022 | 72 |
| 2024 | 38 |

These records require different interpretation by period.

### April through December 2019

The 2019 post-April records are primarily `.DS_Store` files and HFS+ filesystem metadata:

- Desktop `.DS_Store` records;
- Pictures `.DS_Store` records;
- Mail and Library `.DS_Store` records;
- `.journal_info_block`;
- `.journal`;
- Spotlight `VolumeConfig.plist`.

Examples include:

```text
Users/roberthunter/Desktop/New Folder With Items/.DS_Store
Users/roberthunter/Pictures/.DS_Store
Users/roberthunter/Library/Mail/V6/.DS_Store
vol_vol5/.journal_info_block
vol_vol5/.journal
vol_vol5/.Spotlight-V100/Store-V1/VolumeConfig.plist
```

The journal and Spotlight dates cluster around `2019-09-26`, which is also the reported HFS+ volume creation date. This is consistent with volume creation, initialization, mounting, copying, or indexing activity on or around that date. It is not evidence, by itself, of a broad new user-content creation event.

### 2020

The 2020 records include application/document-state artifacts and `.DS_Store` activity. The initial analysis identifies a Desktop `.DS_Store` modified on `2020-10-15`, one day after the New York Post story. This indicates that the volume or a derivative representation was likely mounted, browsed, indexed, or otherwise handled after the main 2019 user-data period.

The timestamp does not identify the operator or establish what was viewed. It is a custody-relevant activity indicator, not proof of content alteration.

### 2022

The 2022 rows are largely system metadata and indexing structures, including Spotlight and DocumentRevisions objects. Examples include:

- Spotlight stores;
- Spotlight index files;
- `.DocumentRevisions-V100` databases;
- `ChunkStoreDatabase` and WAL files;
- application metadata created or touched during later system use or acquisition.

These are more consistent with later filesystem use, mounting, indexing, or examination than with ordinary 2019 laptop-user activity.

### 2024

The 2024 rows are concentrated in `.Spotlight-V100` and related index structures. The reported last-write time of the volume is `2024-11-21 17:40:22 CST`, and the latest entries cluster at that time.

Examples include:

- `live.0.indexHead`;
- `journalAttr.5`;
- `tmp.spotlight.state`;
- `0.ivf-vector-indexes`;
- `permStore`;
- `.store.db`;
- `live.0.indexIds`;
- `live.0.directoryStoreFile`;
- `dbStr-*` index files.

These records strongly suggest later Spotlight/indexing or filesystem processing. They do not, without additional acquisition logs, establish that user documents were newly authored in 2024.

## What The Post-2019 Files Tell Us

The post-April-2019 files support several bounded conclusions:

1. **The volume was not quiescent after April 2019.** Filesystem metadata and application-state timestamps continue after that date.
2. **Most later activity is system or application state.** The later records are dominated by journals, Spotlight, DocumentRevisions, `.DS_Store`, and database sidecars.
3. **The HFS+ volume was created or reconstructed around September 2019.** The journal and Spotlight initialization timestamps align closely with the reported volume creation date.
4. **There was later handling around October 2020.** The Desktop `.DS_Store` event is consistent with mounting or browsing after the main 2019 activity period.
5. **There was later indexing or examination in 2022 and 2024.** The system metadata clusters are consistent with later handling and processing.
6. **The timestamps do not prove user-content insertion.** The evidence does not show a corresponding broad wave of post-2019 Documents, Pictures, Movies, or Desktop content.
7. **Custody and content identity must be separated.** Later metadata activity can affect the custody narrative without making all underlying 2017-2019 user content inauthentic.

## Relationship To The JPMI Hash Discrepancy

The current JPMI SHA-256 reconciliation contains approximately `180,046` distinct JPMI hashes. The exact reconciliation reports show substantial overlap with the other corpora but also an exclusive population. A later scan found that the exact-unmatched population is heavily concentrated in Photos proxies, caches, CloudKit placeholders, application state, and similar generated material.

This matters for interpreting the partition evidence:

- system and application state is expected to vary across copy dates;
- Photos-generated files can be regenerated with different bytes and paths;
- Spotlight, WAL, SHM, and cache objects are particularly poor indicators of substantive user-content absence;
- a JPMI hash absent from APFS or GAI is not automatically an original user file missing from those branches;
- a path or filename candidate must not be promoted to an exact content match without stronger evidence.

The JPMI source’s broad system state helps explain why its hash population cannot be treated as a clean set of immutable user documents.

## Data Quality And Interpretation Limits

Several limitations should remain attached to any report or testimony using these findings:

1. The project does not possess the JPMI source bytes.
2. The original v1 file list has `147` malformed or column-shifted rows.
3. The v1 inventory has incomplete or absent acquisition metadata; later reports supply additional identifiers but do not replace the missing custody history.
4. The hash manifest is not necessarily coextensive with every filesystem entry in the TSK timeline.
5. The TSK timeline uses a single mtime field and includes system, slack, and unallocated pseudo-entries.
6. Empty deleted-file results do not prove that no files were deleted.
7. The reported 2022 E01 acquisition date and the embedded volume dates describe different events and must not be conflated.
8. A filesystem last-write time identifies metadata activity, not necessarily substantive user activity.
9. The HFS+ volume creation timestamp may describe the destination volume or reconstruction, not the origin of every user file.
10. The exact imaging, cloning, migration, or copy tool remains unproven.

## Findings By Confidence

### High confidence

- JPMI represents a GPT-partitioned storage device with an EFI partition and a journaled HFS+ data partition.
- The volume is named `Untitled` and contains a conventional `roberthunter` home directory.
- The inventory includes extensive system and application-support files.
- The volume has native-looking HFS+ journal, catalog, CNID, parent, Spotlight, and document-revision structures in the supplied reports.
- The JPMI layout is not a Desktop-only export.
- The source contains post-April-2019 modified records, including later system metadata.

### Moderate confidence

- The volume was created or reconstructed around September 2019.
- The source was copied, restored, mounted, indexed, or otherwise handled after the main 2017-2019 user-data period.
- The structure is more consistent with a filesystem-level or metadata-preserving operation than ordinary drag-and-drop.

### Not established

- The exact copy or imaging tool.
- Whether the destination was a sector-for-sector clone or a filesystem-aware reconstruction.
- The identity of the operator responsible for each post-2019 timestamp.
- Whether every JPMI cataloged object existed on the originating laptop at the same time.
- Whether any individual post-2019 system artifact represents user-driven activity rather than automated indexing or examiner processing.

## Recommended Follow-Up

1. Obtain the complete acquisition log and tool metadata for `HB-IMAGE-2022-04-29.E01`.
2. Obtain the original E01 and verify its image hashes independently if permitted.
3. Preserve the HFS+ journal and perform bounded journal replay analysis.
4. Analyze the approximately 280 GB of unallocated ranges with documented carving provenance.
5. Separate volume-creation metadata, user-file mtimes, application-state mtimes, and examiner/export timestamps in all future reports.
6. Build a post-2019 file table with exact path, size, created time, modified time, accessed time, CNID, system classification, and hash availability.
7. Compare post-2019 JPMI entries with APFS and GAI system-state trees rather than treating them as ordinary content mismatches.
8. Treat Photos, cache, Spotlight, WAL/SHM, and document-revision records as generated or volatile classes unless independent evidence shows otherwise.
9. Keep the JPMI metadata witness separate from the byte-accessible APFS and GAI sources in all provenance diagrams.

## Conclusion

The JPMI source appears to be a substantial HFS+ Mac-volume witness containing both a conventional user home directory and extensive native/system/application state. Its partition map, HFS+ journal, CNID hierarchy, parent relationships, system metadata, and normal macOS directory layout weigh strongly against describing it as a simple drag-and-drop of a home folder into a blank partition.

The most defensible characterization is a **Mac filesystem-level or metadata-preserving derivative, later mounted or processed, with user data whose principal timestamps cluster in the 2017-2019 period and system/application metadata continuing through 2024**.

The post-April-2019 records are significant for custody and handling. They show that the volume was created, touched, indexed, or examined after the main user-data period. They do not, by themselves, establish broad post-2019 insertion of substantive user files or invalidate the earlier user-content history.
