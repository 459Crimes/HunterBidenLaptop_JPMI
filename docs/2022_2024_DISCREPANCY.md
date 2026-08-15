# 2022/2024 chronology discrepancy

> **Hatnote.** This is a **later report-lineage** problem. It is **not** the 2019–2020 direct-copy story. Do not import it into April 2019. See [Integrity](INTEGRITY.md) and [Forensic image](FORENSIC_IMAGE.md).

## The collision

The acquisition record identifies:

```text
source_image: HB-IMAGE-2022-04-29.E01
reported_at:  2022-04-29
```

Delivered HFS+ volume metadata also reports:

```text
volume_last_write_reported: 2024-11-21 17:40:22 CST
```

**An immutable E01 actually acquired in April 2022 cannot subsequently acquire a November 2024 filesystem write inside itself.**

At least one additional fact is missing, for example:

- a later acquisition of the same (or another) working disk;
- examination of a live/mounted copy after 2022;
- regenerated or mixed report fields;
- a mislabeled date.

The current evidence does **not** establish which explanation is correct. Preserve **both** reported values.

## Participant account (unverified)

Per this project’s communications with **Todd Sanders**, any alteration between 2022 and 2024 would have occurred while **analyzing the data**, **probably a mistaken read-write mount on a Mac**. A writable mount can update Spotlight, DocumentRevisions, FSEvents, and volume last-write **without fabricating Mail/Photos/Documents**.

This is recorded as **Sanders’ account**. It is **not independently verified**. This encyclopedia states that **only the FBI** (or forensic examination of the acquired image with a complete worksheet) can verify the FBI-side history and the actual cause.

## What 2024 rows look like

Post-repair **modified** slice: **30 rows in 2024**, coinciding with Spotlight live indexes, DocumentRevisions SQLite/WAL, TemporaryItems, and similar system state — the same class of objects a read-write Mac mount would touch. See the 2024 tail of [`04_post_2019_03_31_timeline.md`](../build/reports/04_post_2019_03_31_timeline.md).

That pattern is **consistent with** Sanders’ mount story. Consistency is not verification.

## What this discrepancy does not do

- It does not move Hunter-era authorship into 2024.
- It does not, by itself, prove 2019 content was planted.
- It does not license ignoring the December 2019 exact-copy court recitation.
- It does not let you treat `reported_at` 2022-04-29 as false without a better acquisition worksheet.

## See also

- [HFS+ volume Untitled](HFS_VOLUME_UNTITLED.md)
- [Limits](07_limits_and_open_questions.md)
- [People](PEOPLE.md) (Sanders)
