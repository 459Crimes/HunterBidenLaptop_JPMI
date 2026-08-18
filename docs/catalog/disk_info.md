# Catalog: disk identity

> Device, forensic image, and GPT layout of the later JPMI custody medium. Articles: [Crucial X6](../CRUCIAL_X6.md) · [Forensic image](../FORENSIC_IMAGE.md) · [What is JPMI?](../01_what_is_jpmi.md). Parent: [Evidence catalog](README.md).

These files describe **the stick that was imaged**, not the 2019 laptop SSD.

Folder: [`build/disk_info/`](../../build/disk_info/) · section checksums: [`_manifest.json`](../../build/disk_info/_manifest.json)

| File | Rows | Size | Notes |
|---|---:|---:|---|
| [`01_acquisition.tsv`](../../build/disk_info/01_acquisition.tsv) | 24 | 800 B | Model, serial `2145E498755E`, E01 name, MD5/SHA-1, ADI tool, case `HB-2022-04-29`, Sanders rank-2 note |
| [`02_partition_map.tsv`](../../build/disk_info/02_partition_map.tsv) | 3 | 355 B | GPT / EFI / HFS+ start offsets and GUIDs |
| [`03_disk_identity.tsv`](../../build/disk_info/03_disk_identity.tsv) | 11 | 407 B | Consolidated device + partition + volume identifiers |

## Columns

**Acquisition / disk identity** (`field`, `value`) — one row per reported field.

**Partition map:** `partition`, `type`, `guid`, `byte_start`, `byte_length`, `note`.

## Claims these files support

| Claim | File |
|---|---|
| Custody device is a Micron Crucial X6, 500,107,862,016 bytes | acquisition |
| Image `HB-IMAGE-2022-04-29.E01` MD5 / SHA-1 | acquisition |
| Rank-2 manifest attributed to Todd Sanders (TSK 4.14.0) | acquisition |
| EFI and HFS+ partition GUIDs and byte starts | partition map |

Limitation: these rows identify **this** imaged medium. They do not prove the X6 was formatted on 26 September 2019. See [Copy method](../COPY_METHOD.md).
