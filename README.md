# John Paul Mac Isaac copy

> This article is about the **Mac Isaac direct-copy lineage** documented in this repository. For other laptop-data collections that circulated after October 2020, see [Scope](docs/SCOPE.md). For how claims are sourced, see the [Manual of Style](docs/MANUAL_OF_STYLE.md).

The **John Paul Mac Isaac copy** (**JPMI**) is this project's name for one specific evidence lineage in the Hunter Biden laptop matter: a **filesystem-preserving copy** of data recovered at **The Mac Shop** in Wilmington, Delaware, in April 2019, later preserved by the shop's proprietor **John Paul Mac Isaac**, and represented here by forensic reports from a later **500 GB Micron Crucial X6** USB SSD imaged as `HB-IMAGE-2022-04-29.E01`.

This GitHub repository is an **encyclopedia of that disk lineage**, not a dump of the restricted source bytes. It publishes disk identity, HFS+ catalog structure, path inventories, timestamps, reported hashes, and a sourced 2019–2020 custody history. The intended reader is anyone who wants the full technical story of *this* copy: where it came from, what is on it, which dates mean what, and what the metadata does and does not prove.

| JPMI (this repository) | |
|---|---|
| **Lineage** | Mac Isaac direct copy (repair-shop recovery → preservation copies → FBI-era exact copy → later forensic reports) |
| **Repair event** | 12–13 April 2019, Wilmington, Delaware |
| **HFS+ destination created** | 26 September 2019 (`Untitled`, id `dfe8079582e21400`) |
| **FBI subpoena / retained exact copy** | 9 December 2019 |
| **Custody medium described here** | Micron Crucial X6 USB SSD, serial `2145E498755E`, 500,107,862,016 bytes |
| **Forensic image** | `HB-IMAGE-2022-04-29.E01` (E01; ADI 4.7.1.2; case `HB-2022-04-29`) |
| **Image MD5 / SHA-1** | `682619c1884e6fe006664ba31deed698` / `fe918f0cff3304ab52875b984c88fee78ec05197` |
| **Filesystem** | GPT + EFI + journaled HFS+ |
| **Primary account** | `Users/roberthunter` |
| **Inventory paths** | 576,249 (normalized) |
| **CNIDs / hash-manifest paths / distinct SHA-256** | 397,440 / 655,330 / 180,046 |
| **This GitHub tree contains** | Reports, manifests, derived tables — **not** the E01 or individual source-file bytes |
| **Integrity finding (bounded)** | No hacking attributed to JPMI. **0728** is not laptop files per se. Marco Polo used Hayes **APFS** laptop, not JPMI. |
| **Author** | **459Crimes / Marc Aaron DeGiovanni**. [Author](docs/AUTHOR.md) · [*Beyond the Diary*](https://BeyondTheDiary.com) · [diary release](https://ShowersWithMy.Dad) |

**Contents**

- [Lead finding](#lead-finding)
- [What JPMI is](#what-jpmi-is)
- [Historical timeline](#historical-timeline)
- [What is on the disk](#what-is-on-the-disk)
- [How to read this encyclopedia](#how-to-read-this-encyclopedia)
- [Technical evidence](#technical-evidence)
- [All articles](#all-articles)

## Lead finding

The JPMI reporting shows that the copied environment was later **opened, browsed, indexed, copied, and forensically examined**.

It does **not** presently show evidence that an outside actor hacked the Mac Isaac direct copy or injected substantive external user files into it after the April 2019 repair event.

Later modified rows identified in JPMI are overwhelmingly Finder, filesystem, Spotlight, DocumentRevisions, directory, temporary, and other system/application metadata—not a later population of substantive Hunter-created documents. That finding is independently consistent with [CBS News' 21 November 2022](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/) examination of what Mac Isaac's lawyer **Brian Della Rocca** called an “exact copy” of the laptop data supplied to federal investigators.

The formulation used throughout this encyclopedia:

> **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.** No evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting. Later metadata is consistent with custody and forensic handling.

**0728 Extra Found Files** did **not** come from the laptop files per se. It is a large related collection (many unknown origin; some completely unknown to the laptop). The author’s FBI referral on 0728 as potentially hacked is **outside this analysis**. **Marco Polo** analyzed Hayes’s **bootable APFS** descendant of JPMI, not this copy. Dimitrelos and Maryman worked from **APFS-structure** copies, not JPMI. Full treatment: [Integrity](docs/INTEGRITY.md) · [Scope](docs/SCOPE.md) · [Marco Polo v4](docs/MARCO_POLO.md) · [Author](docs/AUTHOR.md).

That is an evidentiary finding, not a claim that undetectable alteration is philosophically impossible.

## What JPMI is

For a non-specialist, the easiest analogy is a **whole-volume, `dd`-style forensic copy rather than a hand-picked folder of documents**. The analogy describes *form*: JPMI preserves a partitioned Mac volume, catalog identifiers, application state, a normal home directory, timestamps, and hundreds of thousands of file records.

It does **not** mean Mac Isaac has been proved to have typed the Unix `dd` command. The exact repair-shop copy utility and every intermediate custody step remain unresolved. Mac Isaac's own account is that recoverable data was first staged on his **store server**, then written to a customer external drive. Server logs are not held here.

The **Crucial X6** described in the acquisition record is a **later custody medium**, not the original internal SSD of the laptop left for repair. See [Crucial X6](docs/CRUCIAL_X6.md), [HFS+ volume Untitled](docs/HFS_VOLUME_UNTITLED.md), and [Forensic image](docs/FORENSIC_IMAGE.md).

The reports examined here were delivered through **Todd Sanders**, who received a drive copy **directly from Della Rocca**. This repository holds a photograph of the mailing packet ([`photo_20260716_120324.jpg`](photo_20260716_120324.jpg)). Because the same attorney supplied both this project's media and the CBS-examined copy for the same purpose, the project **assumes** the two are byte-identical or virtually so. That assumption is **not** a published side-by-side hash comparison. See [Copy lineages](docs/COPY_LINEAGES.md) and [Mailing packet](docs/MAILING_PACKET.md).

## Historical timeline

Full sourced narrative: [Timeline and handling](docs/06_timeline_and_handling.md). Claim-by-claim sources: [Source matrix](docs/09_source_matrix.md). Compact event list: [Timeline (index)](docs/TIMELINE.md).

| When | What | Evidence class |
|---|---|---|
| **12 Apr 2019** | Three damaged laptops presented at The Mac Shop. One usable with a supplied keyboard; one unrecoverable; one left for recovery; **Quote #7469** signed ($85; recover to store server). | Court exhibit — [scan](docs/EXHIBITS.md) |
| **13 Apr 2019** | Customer returned with an external hard drive. Recovery/transfer completed that day. Mac Isaac later said data was first staged on the **store server**. | Court record + participant account (server logs not held) |
| **17 Apr 2019** | $85 electronic invoice sent to `rhbdc@icloud.com` (later **GTX 40** at the 2024 gun trial). Laptop and drive not retrieved, per pleadings. | Court-recited + trial exhibit list |
| **Late Jul 2019** | Mac Isaac's FBI-related contacts begin. | Court-recited |
| **Sep–Oct 2019** | Mac Isaac says he made a copy for his father, Col. Richard “Steve” Mac Isaac, to take to the FBI in Albuquerque. | Participant account; exact physical drive unproved |
| **26 Sep 2019** | JPMI reports HFS+ volume `Untitled` created `2019-09-26 22:59:02 CDT`. | Direct JPMI metadata; **chronology correlation**, not physical-device ID |
| **9 Dec 2019** | FBI subpoena **19-3-LFWS-V-136** (SA Wilson / AUSA Wolf): MacBook Pro `FVFXC2MMHV29`, WD `WX21A19ATFF3`. Delaware Supreme Court: Mac Isaac made an **exact copy before parting with the original**. | Court photos — [Exhibits](docs/EXHIBITS.md) |
| **26 Aug 2020** | Copy provided to Robert Costello (Giuliani's attorney). | Court-recited |
| **13 Oct 2020** | George Mesires contacted Mac Isaac about the laptop. | Court-recited |
| **14 Oct 2020** | *New York Post* first laptop story. | Public event |
| **15 Oct 2020** | JPMI: `Users/roberthunter/Desktop/.DS_Store` modified. Consistent with Finder browsing, **not** file injection. | Direct JPMI metadata + forensic interpretation |
| **29 Apr 2022** | Acquisition record names `HB-IMAGE-2022-04-29.E01`. | Direct acquisition field |
| **21 Nov 2022** | CBS reports independent exam: no user-data tampering; no new files originating after April 2019. | Independent forensic review |
| **21 Nov 2024** | Delivered HFS+ last-write. **Cannot** be a write into an immutable E01 actually acquired in 2022; report-lineage issue, with a participant (Sanders) read-write-mount account that is **unverified**. | Open discrepancy — [2022/2024](docs/2022_2024_DISCREPANCY.md) |

## What is on the disk

The current inventory contains **576,249 paths**. Under `Users`: about **572,743** file rows.

| Home directory | File rows | Represented size (approx.) |
|---|---:|---:|
| `Library` | 251,863 | 54.8 GB |
| `Documents` | 119,794 | 23.2 GB |
| `Pictures` | 92,393 | 61.0 GB |
| `Movies` | 61,202 | 9.4 GB |
| `Downloads` | 23,415 | 19.8 GB |
| `Music` | 19,313 | 32.2 GB |
| `Desktop` | 4,654 | 15.1 GB |

A working Mac profile is not “the newsworthy PDFs.” It is Mail (on the order of **128k `.emlx` paths** in the characterization reports), Contacts (tens of thousands of `.vcf` paths), Photos derivatives, caches, CloudKit, Dr.Fone recovery tooling, Chrome, diagnostics, SQLite, `.DS_Store`, and HFS+ machinery (journal ~40 MB; ~280 GB unallocated *ranges*, which are a storage-state category, not “280 GB of deleted Hunter files”).

Counts of paths, CNIDs, and hashes are **different numbers** because aliases, hard links, slack records, and report layers multiply representations. See [Contents census](docs/CONTENTS_CENSUS.md) and [Glossary](docs/GLOSSARY.md).

## How to read this encyclopedia

Every public claim is supposed to be traceable to one of: JPMI disk/volume reporting; path/timestamp/CNID/hash/system-state reporting; a court opinion or incorporated pleading; an attributed participant account; an independently attributed forensic review; or a sourced public-record provenance link.

The editorial rule is:

> **Observed fact → interpretation → limitation**

Court-recited facts, Mac Isaac's later technical account, JPMI-internal measurements, and CBS's exam are **not interchangeable**. The [source matrix](docs/09_source_matrix.md) is the claim index. The [manual of style](docs/MANUAL_OF_STYLE.md) records how evidence classes are labeled.

Start with articles, not with `build/` TSVs, unless you already know which measurement you want.

## Technical evidence

The `build/` directory is the machine-readable appendix:

- `disk_info/` — custody device, image, partitions
- `volume_info/` — HFS+ identity and system-state objects
- `file_tree/` — directory and home rollups
- `hash_manifest/` — JPMI-reported SHA-256 identities
- `metadata/` — timestamp, extension, CNID, alias summaries
- `reports/` — human-readable forensic summaries
- `archives/` — partitioned deep metadata
- `manifest.tsv` / `manifest.sha256` — validation inventory

How those files are regenerated: [Reproducibility](docs/08_reproducibility.md), [Architecture](ARCHITECTURE.md), [Data contract](DATA_CONTRACT.md).

## All articles

See the **[article index](docs/INDEX.md)** for the full map. Core reading order:

1. [What is JPMI?](docs/01_what_is_jpmi.md)
2. [Provenance — 5 Ws](docs/02_provenance_5ws.md)
3. [Chain of custody](docs/03_chain_of_custody.md)
4. [What is on the copy](docs/04_what_is_on_the_copy.md)
5. [Filesystem for non-experts](docs/05_filesystem_for_non_experts.md)
6. [Timeline and handling](docs/06_timeline_and_handling.md)
7. [Limits and open questions](docs/07_limits_and_open_questions.md)
8. [Reproducibility](docs/08_reproducibility.md)
9. [Source matrix](docs/09_source_matrix.md)

Nerd-depth companions: [Author](docs/AUTHOR.md) · [People](docs/PEOPLE.md) · [The Mac Shop](docs/THE_MAC_SHOP.md) · [Exhibits](docs/EXHIBITS.md) · [Congressional reports](docs/CONGRESS.md) · [Marco Polo v4](docs/MARCO_POLO.md) · [Copy lineages](docs/COPY_LINEAGES.md) · [Timestamps](docs/TIMESTAMPS.md) · [Integrity](docs/INTEGRITY.md) · [Glossary](docs/GLOSSARY.md)

---

**Categories:** JPMI · Mac Isaac direct-copy lineage · HFS+ forensic reporting · 2019 Wilmington recovery · metadata/hash witness
