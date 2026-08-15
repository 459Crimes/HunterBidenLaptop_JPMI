# HFS+ volume Untitled

> **Hatnote.** Destination filesystem on the JPMI custody disk. Creation time belongs to **this volume**, not to every file inside it. See [Filesystem for non-experts](05_filesystem_for_non_experts.md) and [Timestamps](TIMESTAMPS.md).

The data partition is a **journaled HFS+** volume:

| Field | Reported value |
|---|---|
| Name | `Untitled` |
| Volume identifier | `dfe8079582e21400` |
| Filesystem | HFS+ (journaled) |
| Sector offset | 409,634 |
| Volume creation | **2019-09-26 22:59:02 CDT** |
| Volume last-write (delivered metadata) | **2024-11-21 17:40:22 CST** |
| Deleted-file catalog | empty |
| Unallocated ranges | ~280 GB |
| Journal size | 41,943,040 bytes (`.journal`) |

Source: [`build/volume_info/01_volume_identity.tsv`](../build/volume_info/01_volume_identity.tsv).

## Why 26 September 2019 matters

Mac Isaac’s accounts place preservation/FBI-copy work in **September–October 2019**. The volume-creation timestamp falls in that window and is accompanied by a **new journal** and **Spotlight Store-V1** (`VolumeConfig.plist` at 2019-09-27 01:59:04 in the volume-metadata export — note timezone labeling differences across report families).

**Supported:** a new HFS+ destination was created after the April repair, in the FBI-copy period.

**Not supported by that date alone:** this volume *is* the physical drive Col. Mac Isaac took to Albuquerque.

## Native filesystem machinery (not user documents)

Selected objects from [`02_volume_metadata.tsv`](../build/volume_info/02_volume_metadata.tsv):

| Object | Forensic role | Notable times |
|---|---|---|
| `.journal` / `.journal_info_block` | HFS+ journaling | Created with the volume (Sep 2019) |
| `.Spotlight-V100/Store-V1/` | Initial index store | Volume-creation era |
| `.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/` | Later Spotlight store | Heavy 2022-04-11 … 2022-06-01; some 2024-11-21 |
| `.DocumentRevisions-V100/` | Versioning system state | Dirs 2020-10-15; later 2022/2024 DB writes |
| `.DS_Store` (volume root) | Finder | 2022-03-31 |
| `.TemporaryItems/` | macOS temp | 2020-10-15; nested 2024 |
| `.Trashes/` | Trash folder | 2022-03-31 |
| `.fseventsd/` | FSEvents | 2022-06-01 |
| `.com.apple.timemachine.donotpresent` | Time Machine hint on external disks | 2020-10-26 |

A folder dump of emails does not need this kit. That is the empirical basis for the **`dd`-style / whole-volume** analogy.

## Empty deleted catalog

An empty deleted-file catalog is **not** proof that nothing was ever deleted. HFS+ does not reliably present a complete deletion history as a neat catalog. Unallocated ranges are a separate measurement.

## Last-write 2024

An immutable E01 acquired in April 2022 cannot itself pick up a November 2024 filesystem write. The pairing is a **report-lineage problem**. See [2022/2024 discrepancy](2022_2024_DISCREPANCY.md).

## See also

- [Crucial X6](CRUCIAL_X6.md)
- [Integrity](INTEGRITY.md)
