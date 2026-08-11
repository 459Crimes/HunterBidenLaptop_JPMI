# 6. Timeline and Handling

The JPMI records contain multiple layers of time. The most important task is to distinguish **original user/application activity**, **creation of the later HFS+ destination**, **later filesystem/system-state activity**, and **the chronology of the forensic reports themselves**.

One delivered chronology is internally unresolved: the acquisition record identifies `HB-IMAGE-2022-04-29.E01`, while the delivered volume metadata reports a November 2024 last-write. An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write. This page therefore reports both values without pretending that their relationship is settled.

## Timeline at a glance

| Period | What the JPMI records show | How to interpret it |
|---|---|---|
| 2014–2018 and earlier historical material | User files, application state, migrated/cloud/device material, diagnostics, documents, media | Historical data represented inside the Mac account; not all of it necessarily originated on the particular 2019 repair-shop machine |
| Jan–Mar 2019 | Very large modified-time population | Strongest broad cluster associated with the last ordinary user period represented by the inventory |
| April 2019 | Publicly reported repair-shop custody event | Historical boundary; not the creation date of the later HFS+ destination |
| May 2019 | A small number of `.DS_Store` changes | Limited post-repair filesystem interaction represented by the metadata |
| September 2019 | HFS+ destination creation and journal/Spotlight initialization | Creation or reconstruction of the later JPMI HFS+ destination volume |
| 2020 | Limited Finder/application/system metadata changes | Evidence of interaction with a working copy or destination stage |
| March–April 2022 | Dominant access-time cluster and Spotlight activity | Consistent with broad software examination, indexing, hashing, or acquisition |
| April 29, 2022 | Acquisition record / image name `HB-IMAGE-2022-04-29.E01` | Reported forensic-image event |
| November 2024 | Spotlight/index changes and reported volume last write | **Must be reconciled with the 2022 acquisition record; it cannot simply be a later write inside an immutable 2022 E01** |
| July 2026 | Project acquisition-record creation/ingestion field | Later project recordkeeping, not original evidence creation |

## Original-user activity cluster

The inventory's modified-time distribution is heavily concentrated before the repair-shop event.

The current report counts roughly **360,700 modified rows in January through March 2019**, with approximately **241,000 in February alone**.

That pattern is more informative than one isolated file timestamp. It shows a broad application/user environment whose ordinary modification activity is concentrated before the repair-shop period.

## The September 2019 destination-creation event

The JPMI volume reports:

```text
HFS+ volume creation: 2019-09-26 22:59:02 CDT
```

Associated filesystem structures cluster around the same window, including:

- `.journal`;
- `.journal_info_block`;
- initial Spotlight volume state.

This is one of the most important provenance findings in the repository.

It supports the conclusion that the represented HFS+ volume was created or reconstructed **after** the April 2019 repair event.

That does not make the older files in the volume “fake.” A copy or restore can place years of older files onto a newly created destination filesystem. It does mean the destination's own creation event must be separated from the original creation/modification history preserved for files inside it.

## The 141 post-March-2019 modified rows

Using the boundary:

```text
modified_ts > 2019-03-31 23:59:59
```

the current inventory identifies **141 rows**.

They break down as:

| Year | Rows |
|---|---:|
| 2019 | 11 |
| 2020 | 18 |
| 2022 | 82 |
| 2024 | 30 |

The important point is not merely that later timestamps exist. It is **what kind of objects carry them**.

The later rows are dominated by:

- `.DS_Store`;
- Spotlight structures;
- DocumentRevisions structures;
- directories and filesystem state;
- temporary/system metadata.

This pattern is consistent with mounting, Finder browsing, indexing, migration, or forensic processing at one or more later copy stages.

It is **not**, by itself, evidence that 141 substantive user documents were inserted after the repair-shop event.

## 2020 Finder and metadata activity

Among the 2020 records are modifications to:

- `Users/roberthunter/.DS_Store`;
- `Users/roberthunter/Library/.DS_Store`;
- `Users/roberthunter/Desktop/.DS_Store`;
- `Users/roberthunter/Documents/.DS_Store`;
- Dr.Fone-related `.DS_Store` and directory state;
- `.DocumentRevisions-V100` structures;
- `.TemporaryItems` structures.

The Desktop `.DS_Store` modification on **2020-10-15** is particularly useful as a custody marker because Finder metadata can be changed simply by opening/browsing folders.

It should be described as evidence of interaction with the copied environment, not automatically as proof that document contents were edited.

## 2022 examination cluster

The accessed-time distribution is dominated by:

| Month | Accessed rows |
|---|---:|
| 2022-03 | 532,375 |
| 2022-04 | 31,942 |

A half-million-file access wave is not a plausible pattern of ordinary human document reading. It is consistent with software traversing the volume during examination, indexing, hashing, or acquisition.

This is an example of why access timestamps cannot be interpreted without scale and context.

## The 2024 chronology problem

The delivered volume metadata reports:

```text
HFS+ volume last write: 2024-11-21 17:40:22 CST
```

and the 2024 modified rows cluster in Spotlight/index structures.

Standing alone, those fields indicate that the represented filesystem state includes 2024-era indexing metadata. But the same acquisition record identifies an E01 image associated with **April 29, 2022**.

Those two reported facts require an additional custody or reporting step that is not presently documented in this repository. Possible classes of explanation include:

1. the physical/source device was examined or acquired again after 2022;
2. the delivered volume metadata came from a later working copy rather than the immutable 2022 E01;
3. the E01/image date or the volume-report provenance has been mislabeled or mixed during later reporting;
4. another intermediate image/copy exists but has not yet been documented.

The current evidence does **not** choose among those explanations.

Therefore the repository should not say simply that “the 2022 E01 was later indexed in 2024.” It should say that the delivered evidence contains a **2022/2024 chronology discrepancy requiring source-level reconciliation**.

## Timestamp timezone caveat

The received reports use multiple timezone conventions. Some file-list fields appear stored without timezone while volume reports label CDT/CST, and the TSK timeline uses UTC-oriented values.

For that reason, this project should avoid making minute-level accusations from an unnormalized timestamp unless the original field's timezone convention is known.

Broad event clusters—February 2019, September 2019, October 2020, March/April 2022, and the separately reported November 2024 system-state cluster—are more reliable for public explanation than overprecision about an ambiguous offset.

## What the timeline supports

The current JPMI metadata supports these bounded conclusions:

1. The copy lineage preserves a large body of user/application activity predating the April 2019 repair event.
2. The represented HFS+ destination reports a September 2019 creation event.
3. The represented filesystem includes later system/application metadata after the original user period.
4. The large 2022 access cluster is characteristic of broad software traversal rather than ordinary manual reading.
5. The delivered records are **not** a simple untouched-April-2019 time capsule.
6. The later metadata identified so far does **not** by itself demonstrate wholesale insertion of later substantive user files.
7. The reported 2022 E01 acquisition and 2024 volume last-write **cannot yet be placed into one verified custody chronology**.

The detailed row set remains available in [`build/reports/04_post_2019_03_31_timeline.md`](../build/reports/04_post_2019_03_31_timeline.md).
