# Timestamps

> **Hatnote.** How to read time in JPMI. Distributions: [`build/metadata/01_time_distribution.tsv`](../build/metadata/01_time_distribution.tsv). Event index: [Timeline](TIMELINE.md).

## Three fields

| Field | Rough meaning | Easily perturbed by |
|---|---|---|
| **Created** | Object birth *on the relevant filesystem*, depending on copy history | Copy tools, restore, archive extract |
| **Modified** | Content or metadata change, depending on object | Edits, some directory updates, indexers sometimes |
| **Accessed** | Read/traverse if atime tracking is live | Finder, Spotlight, forensic walkers, AV |

A timestamp is **not a person**. It does not name Hunter Biden, Mac Isaac, a reporter, or `mds`. Attribution needs object type, cluster shape, and custody context.

## Timezone trap

Reports mix **CDT/CST labels**, unlabeled DB fields, and TSK conventions. Example: volume creation `2019-09-26 22:59:02 CDT` vs journal objects at `2019-09-27 01:59:02` in another export. A three-hour offset is not a narrative until the families are normalized (see [Limits](07_limits_and_open_questions.md)).

## User-era shape (created / modified)

Created-year row counts (inventory time table):

| Year | Created rows | Modified rows |
|---|---:|---:|
| 2016 | 3,647 | 2,101 |
| 2017 | 107,817 | 106,873 |
| 2018 | 107,185 | 102,657 |
| 2019 | 353,677 | 360,756 |
| 2020 | 14 | 18 |
| 2022 | 82 | 82 |
| 2024 | 7 | 30 |

2019 created **months** (same table): January 55,462; **February 241,603**; March 56,597; September 15. That is a living account heading into the repair, then a cliff — consistent with CBS's “use stops around March 2019,” without treating every February row as a unique document.

Oddities such as a **year-1984 created** row (count 1, size 0) are classic filesystem/sentinel noise. They are not a 1984 user biography.

## Access-era shape (the examiner's footprint)

| Bucket | Accessed rows | Approx. represented bytes |
|---|---:|---:|
| year-2019 | 8,130 | 273 KB |
| year-2020 | 221 | 63 MB |
| **year-2022** | **564,453** | **~216 GB** |
| year-2024 | 30 | 59 MB |
| month-2022-03 | 532,375 | ~215 GB |
| month-2022-04 | 31,942 | ~218 MB |

**Interpretation:** 2022 is when something walked nearly the whole user tree. That matches forensic imaging/indexing, not a return of the original user.

## 15 October 2020 cluster (Finder-scale, not authorship-scale)

From the post-repair modified list, within minutes:

- Dr.Fone recovery-folder `.DS_Store` files ~21:16
- `Users/roberthunter/Desktop/.DS_Store` **21:18:17**
- `Public/.DS_Store` 21:18:42
- `.DocumentRevisions-V100` subdirs and `.TemporaryItems` 21:19:22
- `Documents/.DS_Store` 21:20:53

The *New York Post* story was **14 October 2020**. The supported sentence is: **the copied environment appears to have been opened**. The unsupported sentence is: **Hunter files were planted the next day**.

## Volume vs file time

HFS+ **volume creation** (26 Sep 2019) is the birthday of `Untitled`. Files inside can be years older (copied in) or metadata-younger (indexes). Volume last-write (2024) is not evidence that the data was authored in 2024.

## See also

- [Integrity](INTEGRITY.md)
- [HFS+ volume Untitled](HFS_VOLUME_UNTITLED.md)
- [Sourcing and terminology](MANUAL_OF_STYLE.md)
