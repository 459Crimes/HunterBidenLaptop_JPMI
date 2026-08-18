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
| **Complaint allegation** | C.D. Cal. 2:23-cv-8032 | Pleading language; not an affidavit |
| **Contemporaneous journalism** | *New York* magazine 2022; Washington Post 2022; Raw Story; LA Times | Named reporter observation or attributed quote |
| **Participant account** | Mac Isaac interviews; Todd Sanders communications with this project | “Mac Isaac later said…” / “Sanders’ account…” |
| **Comparative inventory** | APFS/GAI rows in `rhb_forensics` (not this GitHub tree) | Cite source_id; do not call the row `JPMI://` |
| **Independent forensic** | CBS / Computer Forensics Services, Nov 2022 | CBS and CFS are separate from JPMI tables |
| **Public-record affiliation** | American Oversight on Sanders / America Project | Affiliation is not hash identity |
| **Interpretation** | macOS artifact knowledge (`.DS_Store`, Spotlight) | “Consistent with…” rather than “proves the person was…” |
| **Inference** | Byte-identity JPMI ↔ CBS media | Labeled as inference; no side-by-side hash is published |
| **Project identity** | [Author](AUTHOR.md); *George News* essay | Who published this repo. Distinct from JPMI CNID/hash/timestamp tables |

## The three-layer sentence

**Observed fact → interpretation → limitation** appear as adjacent sentences.

Example:

> JPMI reports `JPMI://Users/roberthunter/Desktop/.DS_Store` modified 2020-10-15 21:18:17. `.DS_Store` is Finder folder-view metadata. The timing is consistent with browsing the copied Desktop the day after the *New York Post* story. It is not evidence that a Hunter document was injected.

The sentence “On October 15 someone tampered with the Desktop” is not supported by that row.

## Claims not established by the present record

The following are **not** findings of this encyclopedia:

- that the laptop partition was sector-copied onto the examined `Untitled` volume;
- that `jpmi_alias_map` records Unix hard links (it records TSK file + slack);
- that the Crucial X6 is the original laptop SSD, or the disk formatted on 26 September 2019;
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
| **APFS** (459Crimes corpus name) | TRIMARCO conversion of the Costello-line boot volume (`HB Boot Drive`). Date unknown; CCC snapshots **5 Jan 2021**. **Not** a clone of JPMI `Untitled` |
| **APFS*** | **Jun 2022** Hayes image (`RHB_Boot.imgc`) sent to Marc Aaron DeGiovanni. Downstream of **HAYES**, not JPMI |
| **MPOLO** | Marco Polo’s claimed **Jun 2021** receipt: Hayes **bootable laptop**, not JPMI |
| **Custody medium** | The physical device later imaged (here: Crucial X6) |
| **Source bytes** | Contents of the restricted E01; **not** in this GitHub tree |

Articles expand JPMI on first use. “The laptop” is not used as a serial-number identifier.

## Source URIs

File citations name the **corpus root**, then the path inside that copy. The working inventory prefix `jpmi_metadata/` is rewritten to `JPMI://` on export.

| Scheme | Copy |
|---|---|
| `JPMI://` | This copy (Mac Isaac direct-copy lineage as examined here) |
| `APFS://` | TRIMARCO→APFS bootable family (`HB Boot Drive`). Sibling of JPMI, not a descendant of examined `Untitled` |
| `GAI://` | Government Accountability Institute truncated HFS+ image (`hb.img`) |
| `0728://` | Extra Found Files (Hayes MEGA share after 28 July 2021) |

Example: `JPMI://Users/roberthunter/Desktop/.DS_Store`. Do not cite an APFS, GAI, or 0728 path as if it were a JPMI inventory row.

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
