# Manual of Style

> **Hatnote.** This is the house MOS for the JPMI encyclopedia. It is not a court opinion and not a filesystem measurement. See also [Source matrix](09_source_matrix.md) and [Scope](SCOPE.md).

This repository is written so a technically literate stranger can audit it like a Wikipedia article: **lead, sources, infobox facts, limitations, see-also**. The difference from Wikipedia is that we do not crowd-edit contested politics into the lead. We publish **one lineage**, with labeled evidence classes.

## The one question

> **What does the John Paul Mac Isaac direct-copy lineage itself show?**

Comparative analysis of other laptop datasets belongs in a different project ([Scope](SCOPE.md)).

## Evidence classes (do not mix silently)

| Class | Typical sources | How to write it |
|---|---|---|
| **Direct JPMI report** | `build/disk_info`, `volume_info`, file times, CNIDs, hashes | “JPMI reports…” / “the acquisition record identifies…” |
| **Court-recited** | Delaware Supreme Court 2025; Superior Court 2024; S.D. Florida 2021 | “The court recounts…” / “the opinion states…” |
| **Participant account** | Mac Isaac interviews; Todd Sanders communications with this project | “Mac Isaac later said…” / “Sanders’ account, unverified, is…” |
| **Independent forensic** | CBS / Computer Forensics Services, Nov 2022 | Attribute CBS and CFS separately from JPMI tables |
| **Public-record affiliation** | American Oversight on Sanders / America Project | Affiliation is not the same as hash identity |
| **Interpretation** | macOS artifact knowledge (`.DS_Store`, Spotlight) | “Consistent with…” never “proves the person was…” |
| **Assumption** | Byte-identity JPMI ↔ CBS media | Label as assumption; state that no side-by-side hash is published |

## The three-layer sentence

Keep **observed fact → interpretation → limitation** as adjacent sentences, not as one mushy paragraph.

Good:

> JPMI reports `Users/roberthunter/Desktop/.DS_Store` modified 2020-10-15 21:18:17. `.DS_Store` is Finder folder-view metadata. The timing is consistent with browsing the copied Desktop the day after the *New York Post* story. It is not evidence that a Hunter document was injected.

Bad:

> On October 15 someone tampered with the Desktop.

## Words that are banned in the lead (unless proved)

Do not write these as settled fact:

- “Mac Isaac used `dd`.”
- “The Crucial X6 is the original laptop SSD.”
- “`Untitled` is the Albuquerque FBI drive.”
- “JPMI and the CBS disk are hash-identical.”
- “Nothing could possibly have been changed.”
- “Every timestamp is Hunter Biden.”
- “Every pre-2019 file was created on the 2019 repair-shop Mac.”
- “280 GB of deleted files.”
- “The empty deleted catalog means nothing was ever deleted.”

Preferred integrity language is in [Integrity](INTEGRITY.md).

## Names and abbreviations

| Term | Meaning in this repo |
|---|---|
| **JPMI** | John Paul Mac Isaac **copy lineage** as examined here — not Mac Isaac the person |
| **The laptop** | Informal shorthand; the recovery involved **three** damaged machines plus an external drive |
| **Direct copy** | A Mac Isaac-made copy existing before/at FBI surrender, as distinct from later mixed political dumps |
| **Custody medium** | The physical device later imaged (here: Crucial X6) |
| **Source bytes** | Contents of the restricted E01; **not** in this GitHub tree |

On first use in an article, expand JPMI. Do not use “the laptop” as if it identified a serial number.

## Dates and timezones

Do not silently equate CDT/CST labeled volume fields, unlabeled database timestamps, and TSK UTC-oriented rows. See [Timestamps](TIMESTAMPS.md). Minute-level cross-family sequencing needs explicit timezone work.

## Counts

Never treat path count, CNID count, hash count, and “unique human documents” as the same. See [Contents census](CONTENTS_CENSUS.md).

## Photographs and personal data

The mailing-packet photograph is a **custody exhibit**, not decoration. Caption what the label shows (sender/recipient) without expanding into biographical essay.

This encyclopedia describes **structure and provenance**. It is not a gallery of user content.

## See also

- [Source matrix](09_source_matrix.md)
- [Limits](07_limits_and_open_questions.md)
- [Reproducibility](08_reproducibility.md)
