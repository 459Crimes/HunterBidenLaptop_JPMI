# JPMI Device and Copy Identity

## Observation — the later custody medium

The forensic acquisition record describes a 500 GB-class external SSD. It is a **later custody medium, not the original laptop SSD**.

| Field | Reported value |
|---|---|
| Custody device | Micron Crucial X6 SSD USB Device |
| Custody serial | 2145E498755E |
| Image | HB-IMAGE-2022-04-29.E01 |
| Format | E01 |
| Image size | 500107862016 |
| MD5 | 682619c1884e6fe006664ba31deed698 |
| SHA-1 | fe918f0cff3304ab52875b984c88fee78ec05197 |
| Acquisition tool | ADI4.7.1.2 |
| Case number | HB-2022-04-29 |

## Observation — partition and volume identity

| Field | Reported value |
|---|---|
| Disk GUID | c93db56d-6e88-4965-94e5-8585a013d086 |
| EFI partition GUID | 54bcfba5-c609-44c0-a45d-b07090d2c996 |
| HFS+ partition GUID | cf0fd7cc-b0c0-4667-affd-d1627e93c654 |
| HFS+ sector offset | 409634 |
| Volume name | Untitled |
| Volume identifier | dfe8079582e21400 |

The destination is represented as a GPT-partitioned Mac-oriented disk with an EFI System Partition and a journaled HFS+ data volume. The acquisition record identifies an E01 image.

## Interpretation

The destination is a GPT-partitioned Mac-oriented disk with EFI and journaled HFS+ `Untitled`. Volume creation 26 September 2019, preserved 2016–March 2019 file timestamps, empty HFS+ hard-link private directories, and a `roberthunter` home at volume root support a **file-aware copy onto a newly formatted volume**. The Crucial X6 is a 2020+ product; the 2019 volume reached it by a later volume clone. The E01 is a forensic image of that stick. See docs/COPY_METHOD.md.

## Historical hardware artifacts inside the user tree

The inventory contains 33 path rows referencing `roberts-MacBook-Air`, 1090 referencing serial `C02S953UH3QF`, and 1298 referencing WirelessDiagnostics material. These are useful evidence that older Mac diagnostic data is represented inside the account. They are **not sufficient by themselves to identify the particular computer left for repair in 2019**, because Mac home data can be migrated, restored, or copied forward across machines.

## Limitation

The present project does not have the original repair-shop copy log or command history. The exact intermediate recovery/copy mechanism therefore remains unresolved.
