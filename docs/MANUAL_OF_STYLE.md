# Sourcing and terminology

> **Hatnote.** How this encyclopedia labels evidence. It is not a court opinion and not a filesystem measurement. See also [Source matrix](09_source_matrix.md) and [Scope](SCOPE.md).

This repository is written so a technically literate reader can audit it like a Wikipedia article: **lead, sources, infobox facts, limitations, see-also**. Contested politics are not edited into the lead. The publication covers **one lineage**, with labeled evidence classes.

## The one question

> **What does the John Paul Mac Isaac direct-copy lineage itself show?**

Comparative analysis of other laptop datasets belongs in a different project ([Scope](SCOPE.md)).

## Evidence classes

These classes are kept distinct:

| Class | Typical sources | Attribution |
|---|---|---|
| **Direct JPMI report** | `build/disk_info`, `volume_info`, file times, CNIDs, hashes | “JPMI reports…” / “the acquisition record identifies…” |
| **Court-recited** | Delaware Supreme Court 2025; Superior Court 2024; S.D. Florida 2021 | “The court recounts…” / “the opinion states…” |
| **Participant account** | Mac Isaac interviews; Todd Sanders communications with this project | “Mac Isaac later said…” / “Sanders’ account…” |
| **Independent forensic** | CBS / Computer Forensics Services, Nov 2022 | CBS and CFS are separate from JPMI tables |
| **Public-record affiliation** | American Oversight on Sanders / America Project | Affiliation is not hash identity |
| **Interpretation** | macOS artifact knowledge (`.DS_Store`, Spotlight) | “Consistent with…” rather than “proves the person was…” |
| **Inference** | Byte-identity JPMI ↔ CBS media | Labeled as inference; no side-by-side hash is published |
| **Project identity** | [Author](AUTHOR.md); *George News* essay | Who published this repo. Distinct from JPMI CNID/hash/timestamp tables |

## The three-layer sentence

**Observed fact → interpretation → limitation** appear as adjacent sentences.

Example:

> JPMI reports `Users/roberthunter/Desktop/.DS_Store` modified 2020-10-15 21:18:17. `.DS_Store` is Finder folder-view metadata. The timing is consistent with browsing the copied Desktop the day after the *New York Post* story. It is not evidence that a Hunter document was injected.

The sentence “On October 15 someone tampered with the Desktop” is not supported by that row.

## Claims not established by the present record

The following are **not** findings of this encyclopedia:

- that Mac Isaac used the Unix `dd` command;
- that the Crucial X6 is the original laptop SSD;
- that volume `Untitled` is the Albuquerque FBI drive;
- that JPMI and the CBS disk are hash-identical;
- that undetectable alteration is logically impossible;
- that Marco Polo analyzed the JPMI / Della Rocca / Sanders copy;
- that Dimitrelos or Maryman examined the JPMI / Crucial X6 reports;
- that JPMI or the FBI-seized MacBook is the source of the 0728 corpus;
- that every timestamp is Hunter Biden;
- that every pre-2019 file was created on the 2019 repair-shop Mac;
- that unallocated ranges equal “280 GB of deleted files”;
- that an empty deleted catalog means nothing was ever deleted.

Integrity wording used in the articles is in [Integrity](INTEGRITY.md).

## Names and abbreviations

| Term | Meaning in this repo |
|---|---|
| **JPMI** | John Paul Mac Isaac **copy lineage** as examined here — not Mac Isaac the person |
| **The laptop** | Informal shorthand; the recovery involved **three** damaged machines plus an external drive |
| **Direct copy** | A Mac Isaac-made copy existing before/at FBI surrender, as distinct from later mixed political dumps |
| **0728 / Extra Found Files** | Sidecar MEGA corpus (Hayes, after 28 July 2021). Not from the laptop files per se; related collection; many unknown origin; some unknown to the laptop |
| **APFS** (459Crimes corpus name) | Later, more altered **copy of the JPMI disk**, as a Hayes **bootable laptop**. Not the JPMI reports here. What Marco Polo analyzed |
| **Custody medium** | The physical device later imaged (here: Crucial X6) |
| **Source bytes** | Contents of the restricted E01; **not** in this GitHub tree |

Articles expand JPMI on first use. “The laptop” is not used as a serial-number identifier.

## Dates and timezones

CDT/CST labeled volume fields, unlabeled database timestamps, and TSK UTC-oriented rows are different families. See [Timestamps](TIMESTAMPS.md). Minute-level cross-family sequencing requires explicit timezone work.

## Counts

Path count, CNID count, hash count, and “unique human documents” are different quantities. See [Contents census](CONTENTS_CENSUS.md).

## Photographs and personal data

The mailing-packet photograph is a **custody exhibit**. Captions record sender and recipient. This encyclopedia describes **structure and provenance**; it is not a gallery of user content.

## See also

- [Source matrix](09_source_matrix.md)
- [Limits](07_limits_and_open_questions.md)
- [Reproducibility](08_reproducibility.md)
