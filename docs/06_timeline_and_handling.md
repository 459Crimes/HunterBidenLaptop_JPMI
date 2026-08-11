# 6. Timeline and Later Handling

The JPMI copy contains multiple layers of time. The most important task is to distinguish **original user/application activity** from **creation of the later copy** and from **later custody activity**.

## Timeline at a glance

| Period | What the JPMI records show | How to interpret it |
|---|---|---|
| 2014–2018 and earlier historical material | User files, application state, migrated/cloud/device material, diagnostics, documents, media | Historical data represented inside the Mac account; not all of it necessarily originated on the particular 2019 repair-shop machine |
| Jan–Mar 2019 | Very large modified-time population | Strongest broad cluster associated with the last ordinary user period represented by the inventory |
| April 2019 | Publicly reported repair-shop custody event | Historical boundary; not the creation date of the later HFS+ destination |
| May 2019 | A small number of `.DS_Store` changes | Limited post-repair filesystem interaction |
| September 2019 | HFS+ destination creation and journal/Spotlight initialization | Creation or reconstruction of the later JPMI destination volume |
| 2020 | Limited Finder/application/system metadata changes | Later browsing/mounting/handling indicators |
| March–April 2022 | Dominant access-time cluster and Spotlight activity | Examination/acquisition period |
| November 2024 | Spotlight/index changes and reported volume last write | Later indexing/handling activity |

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

It means the HFS+ volume itself was created or reconstructed **after** the April 2019 repair event.

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

This pattern is consistent with later mounting, Finder browsing, indexing, migration, and forensic handling.

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

It should be described as evidence of later interaction with the copied volume, not automatically as proof that document contents were edited.

## 2022 examination cluster

The accessed-time distribution is dominated by:

| Month | Accessed rows |
|---|---:|
| 2022-03 | 532,375 |
| 2022-04 | 31,942 |

A half-million-file access wave is not a plausible pattern of ordinary human document reading. It is consistent with software traversing the volume during examination, indexing, hashing, or acquisition.

This is an example of why access timestamps cannot be interpreted without scale and context.

## 2024 Spotlight/index activity

The volume reports a last-write time of:

```text
2024-11-21 17:40:22 CST
```

The later records cluster in Spotlight/index structures. This is evidence that the volume or a working representation of it was still being processed after the 2022 acquisition period.

The metadata available to this project does not identify the human operator responsible for that activity.

## Timestamp timezone caveat

The received reports use multiple timezone conventions. Some file-list fields appear stored without timezone while volume reports label CDT/CST, and the TSK timeline uses UTC-oriented values.

For that reason, this project should avoid making minute-level accusations from an unnormalized timestamp unless the original field's timezone convention is known.

Broad event clusters—February 2019, September 2019, October 2020, March/April 2022, November 2024—are considerably more reliable for public explanation than overprecision about an ambiguous two-hour offset.

## What the timeline proves

The current JPMI metadata supports these bounded conclusions:

1. The copy preserves a large body of user/application activity predating the April 2019 repair event.
2. The later HFS+ destination reports a September 2019 creation event.
3. The destination experienced later filesystem interaction.
4. The dominant later events are characteristic of mounting, browsing, indexing, and forensic examination.
5. The copy was therefore **not a completely untouched time capsule after April 2019**.
6. The later metadata identified so far does **not** by itself demonstrate wholesale insertion of later substantive user files.

The detailed row set remains available in [`build/reports/04_post_2019_03_31_timeline.md`](../build/reports/04_post_2019_03_31_timeline.md).
