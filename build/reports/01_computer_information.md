# JPMI Device and Copy Identity

## 1. Observation — the later custody medium

The forensic acquisition record describes a GPT-partitioned external SSD. This device is a **later custody medium** and should not be described as the original internal storage hardware of the laptop left for repair.

| Field | Reported value |
|---|---|
| Custody device | Micron Crucial X6 SSD USB Device |
| Custody device serial | `2145E498755E` |
| Device/image size | `500,107,862,016` bytes |
| Sector size | 512 bytes |
| Sector count | `976,773,168` |
| Forensic image | `HB-IMAGE-2022-04-29.E01` |
| Image format | E01 |
| MD5 | `682619c1884e6fe006664ba31deed698` |
| SHA-1 | `fe918f0cff3304ab52875b984c88fee78ec05197` |
| Acquisition tool | `ADI4.7.1.2` |
| Case number | `HB-2022-04-29` |

These fields come from `build/disk_info/01_acquisition.tsv` / the normalized `jpmi_acquisition` record.

## 2. Observation — disk, partition, and HFS+ identity

The custody disk is represented with a GPT partition map containing an EFI System Partition and a journaled HFS+ data partition.

| Field | Reported value |
|---|---|
| Disk GUID | `c93db56d-6e88-4965-94e5-8585a013d086` |
| EFI partition GUID | `54bcfba5-c609-44c0-a45d-b07090d2c996` |
| HFS+ partition GUID | `cf0fd7cc-b0c0-4667-affd-d1627e93c654` |
| HFS+ sector offset | `409634` |
| Volume name | `Untitled` |
| Volume identifier | `dfe8079582e21400` |
| Filesystem | Journaled HFS+ |
| Reported volume creation | `2019-09-26 22:59:02 CDT` |
| Reported volume last write | `2024-11-21 17:40:22 CST` |

The HFS+ destination also contains filesystem journal state, Spotlight state, DocumentRevisions state, and unallocated ranges.

## 3. Interpretation — what kind of copy is JPMI?

For a general reader, the evidence is best explained as a **whole-volume / `dd`-style copy lineage**, not a folder containing only selected emails or documents.

That analogy is supported by the broad storage context preserved in the JPMI witness:

- GPT and EFI structures;
- a journaled HFS+ volume;
- an HFS+ journal;
- CNID and parent-CNID catalog relationships;
- allocated and unallocated representations;
- Spotlight and document-revision metadata;
- a conventional `Users/roberthunter` home hierarchy;
- application databases and machine-generated state.

### Important qualification

The phrase **`dd`-style** does not mean that this project has proved John Paul Mac Isaac literally used the Unix `dd` command.

The exact original repair-shop copy utility, any intermediate server/image step, and the complete source-to-destination device history remain unresolved.

The later forensic preservation is clearer: the custody device is represented by the E01 image `HB-IMAGE-2022-04-29.E01`.

## 4. Historical hardware diagnostics inside the user tree

The JPMI user tree contains historical WirelessDiagnostics packages with filenames referencing:

- host name `roberts-MacBook-Air`;
- serial `C02S953UH3QF`;
- diagnostic captures from November 2016.

Those artifacts are real provenance clues, but the correct conclusion is bounded:

> They show that data from an older Mac environment is represented inside the `roberthunter` data tree.

They do **not** independently establish that the older MacBook Air was the specific computer later left at the repair shop in 2019.

A Mac user account can contain migrated home-directory data, copied diagnostics, restored backups, cloud-synchronized files, and material carried forward from earlier Macs. Historical hardware artifacts must therefore be distinguished from identification of the later repair-shop hardware.

## 5. What JPMI alone establishes about the storage environment

The JPMI metadata supports these observations without using another dataset:

1. The later custody medium is a 500 GB-class Crucial X6 USB SSD.
2. It was represented in a forensic E01 acquisition with recorded MD5 and SHA-1 values.
3. The disk has GPT/EFI/HFS+ structure rather than merely a loose user-document directory.
4. The HFS+ destination volume is named `Untitled` and reports a September 2019 creation event.
5. The user data is arranged as a broad macOS home environment under `roberthunter`.
6. The copied volume later experienced additional mounting/indexing/handling activity.

## 6. Limitation

The project currently publishes a metadata/hash witness rather than the restricted JPMI E01 bytes themselves.

The metadata can document the reported device, image, filesystem, paths, catalog identities, hashes, and timestamps. It cannot, by itself, reconstruct every undocumented intermediate custody operation between the original repair-shop storage and the later Crucial X6.
