# John Paul Mac Isaac copy

> This page is the **landing article** for the Mac Isaac direct-copy lineage documented in this repository. Other laptop-data collections: [Scope](docs/SCOPE.md). How claims are labeled: [Sourcing and terminology](docs/MANUAL_OF_STYLE.md).

The **John Paul Mac Isaac copy** (**JPMI**) is one evidence lineage in the Hunter Biden laptop matter: a **file-aware copy of a Mac home** recovered at **The Mac Shop** in Wilmington, Delaware, in April 2019, preserved by **John Paul Mac Isaac**, and represented here by forensic reports from a later **500 GB Micron Crucial X6** USB SSD imaged as `HB-IMAGE-2022-04-29.E01`.

This GitHub repository is an **encyclopedia of that disk lineage**. It publishes disk identity, HFS+ catalog structure, path inventories, timestamps, reported hashes, and a sourced 2019–2020 custody history. It does **not** publish the E01 or individual source-file bytes.

| | |
|---|---|
| **Lineage** | Mac Isaac direct copy (repair-shop recovery → preservation copies → FBI-era exact copy → later forensic reports) |
| **Repair event** | 12–13 April 2019, Wilmington, Delaware |
| **HFS+ destination created** | 26 September 2019 (`Untitled`, id `dfe8079582e21400`) |
| **FBI subpoena / retained exact copy** | 9 December 2019 |
| **Custody medium** | Micron Crucial X6 USB SSD, serial `2145E498755E`, 500,107,862,016 bytes |
| **Forensic image** | `HB-IMAGE-2022-04-29.E01` (E01; ADI 4.7.1.2; case `HB-2022-04-29`) |
| **Image MD5 / SHA-1** | `682619c1884e6fe006664ba31deed698` / `fe918f0cff3304ab52875b984c88fee78ec05197` |
| **Filesystem** | GPT + EFI + journaled HFS+ |
| **Primary account** | `JPMI://Users/roberthunter` |
| **Inventory paths** | 576,249 (normalized) — [file-tree catalog](docs/catalog/file_tree.md) |
| **CNIDs / hash-manifest paths / distinct SHA-256** | 397,440 / 655,330 / 180,046 — [hash catalog](docs/catalog/hash_manifest.md) |
| **This tree contains** | Articles, exhibits, derived tables — **not** the E01 or user-file bytes |
| **Integrity (bounded)** | No hacking attributed to JPMI. **0728** is not laptop files per se. Marco Polo used **MPOLO**, not JPMI. |
| **Author** | **459Crimes / Marc Aaron DeGiovanni**. [Author](docs/AUTHOR.md) · [*Beyond the Diary*](https://BeyondTheDiary.com) · [diary release](https://ShowersWithMy.Dad) |

## Start here

| If you want… | Open |
|---|---|
| A one-page definition | [What is JPMI?](docs/01_what_is_jpmi.md) |
| The custody story | [Chain of custody](docs/03_chain_of_custody.md) · [Copy lineages](docs/COPY_LINEAGES.md) |
| What is on the disk | [What is on the copy](docs/04_what_is_on_the_copy.md) · [Contents census](docs/CONTENTS_CENSUS.md) |
| Dates and later handling | [Timeline](docs/TIMELINE.md) · [Integrity](docs/INTEGRITY.md) |
| Every article | [Article index](docs/INDEX.md) |
| The TSV / JSON / report files | **[Evidence catalog](docs/catalog/README.md)** |
| Diagrams | [Diagrams](docs/diagrams/README.md) |

## Lead finding

The JPMI reporting shows that the copied environment was later **opened, browsed, indexed, copied, and forensically examined**.

It does **not** presently show evidence that an outside actor hacked the Mac Isaac direct copy or injected substantive external user files into it after the April 2019 repair event.

Later modified rows are overwhelmingly Finder, filesystem, Spotlight, DocumentRevisions, directory, temporary, and other system/application metadata—not a later population of substantive Hunter-created documents. That is independently consistent with [CBS News' 21 November 2022](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/) examination of what Mac Isaac's lawyer **Brian Della Rocca** called an “exact copy” of the laptop data supplied to federal investigators.

> **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.** Later metadata is consistent with custody and forensic handling.

**0728 Extra Found Files** did **not** come from the laptop files per se. **Marco Polo** analyzed **MPOLO** (Hayes bootable laptop), not this copy. Dimitrelos (**GUSTAV**) and **MARYMAN** worked from **APFS-structure** copies, not JPMI. Full treatment: [Integrity](docs/INTEGRITY.md) · [Scope](docs/SCOPE.md) · [Marco Polo v4](docs/MARCO_POLO.md).

Row-level post-repair modified list: [reports catalog](docs/catalog/reports.md) (`04_post_2019_03_31_timeline.md`).

## What JPMI is

JPMI is a **copied Mac home on a later HFS+ disk**, not a hand-picked folder of documents. Volume `Untitled` was created **26 September 2019** (home-only, file-aware copy). The Crucial X6 did not exist until August 2020, so the 2019 volume reached that stick by a later **volume clone**. The 2022 E01 is a **forensic image of the X6**.

- Hardware: [Crucial X6](docs/CRUCIAL_X6.md) · [HFS+ volume Untitled](docs/HFS_VOLUME_UNTITLED.md) · [Forensic image](docs/FORENSIC_IMAGE.md)
- Method: [How the files left the laptop](docs/COPY_METHOD.md)
- Other copies that are **not** this disk: [Where the copies split](docs/BRANCH_DEVIATIONS.md)

The reports examined here were delivered through **Todd Sanders**, from **Della Rocca**. Photograph of the mailing packet: [`photo_20260716_120324.jpg`](photo_20260716_120324.jpg) ([exhibits catalog](docs/catalog/exhibits.md)). Because the same attorney supplied both this project's media and the CBS-examined copy for the same purpose, the two are **byte-identical or virtually byte-identical** — an inference, **not** a published side-by-side hash. See [Copy lineages](docs/COPY_LINEAGES.md) and [Mailing packet](docs/MAILING_PACKET.md).

## Historical timeline

Full sourced narrative: [Timeline and handling](docs/06_timeline_and_handling.md). Claim-by-claim sources: [Source matrix](docs/09_source_matrix.md). Compact list: [Timeline (index)](docs/TIMELINE.md).

| When | What | Evidence class |
|---|---|---|
| **12 Apr 2019** | Three damaged laptops at The Mac Shop. **Quote #7469** signed ($85; recover to store server). | Court exhibit — [scan](docs/EXHIBITS.md) |
| **13 Apr 2019** | Customer returned with an external hard drive. Recovery completed that day. Data first staged on the **store server** (Mac Isaac's account). | Court record + participant account |
| **17 Apr 2019** | $85 invoice to `rhbdc@icloud.com`. Laptop and drive not retrieved, per pleadings. | Court-recited |
| **26 Sep 2019** | JPMI HFS+ `Untitled` created (home-only). Apple 10.14.6 Supplemental Update 2 (**18G103**) ships the same day — **BOOT01** can exist only after this. | Volume field + Apple note — [splits](docs/BRANCH_DEVIATIONS.md) |
| **9 Dec 2019** | FBI subpoena **19-3-LFWS-V-136**. Mac Isaac made an **exact copy before parting with the original**. | Court photos — [Exhibits](docs/EXHIBITS.md) |
| **26 Aug 2020** | **BOOT01** to Robert Costello. **Not JPMI.** | Court-recited + [splits](docs/BRANCH_DEVIATIONS.md) |
| **14–15 Oct 2020** | *New York Post* story; JPMI Desktop `.DS_Store` modified (Finder browsing, not file injection). | Public event + JPMI metadata |
| **29 Apr 2022** | Acquisition record names `HB-IMAGE-2022-04-29.E01`. | [Disk catalog](docs/catalog/disk_info.md) |
| **21 Nov 2022** | CBS: no user-data tampering; no new files originating after April 2019. | Independent forensic review |
| **21 Nov 2024** | Delivered HFS+ last-write. Cannot be a write into an immutable 2022 E01 as labeled. | [2022/2024](docs/2022_2024_DISCREPANCY.md) |

## What is on the disk

The inventory contains **576,249 paths**. Under `Users`: about **572,743** file rows. Tables: [file-tree catalog](docs/catalog/file_tree.md).

| Home directory | File rows | Represented size (approx.) |
|---|---:|---:|
| `Library` | 251,863 | 54.8 GB |
| `Documents` | 119,794 | 23.2 GB |
| `Pictures` | 92,393 | 61.0 GB |
| `Movies` | 61,202 | 9.4 GB |
| `Downloads` | 23,415 | 19.8 GB |
| `Music` | 19,313 | 32.2 GB |
| `Desktop` | 4,654 | 15.1 GB |

A working Mac profile is Mail (on the order of **128k `.emlx` paths**), Contacts, Photos derivatives, caches, CloudKit, Dr.Fone tooling, Chrome, diagnostics, SQLite, `.DS_Store`, and HFS+ machinery. Unallocated *ranges* (~280 GB) are unused destination space, not “280 GB of deleted Hunter files.”

Path, CNID, and hash counts differ because aliases, slack records, and report layers multiply representations. See [Contents census](docs/CONTENTS_CENSUS.md) and [Glossary](docs/GLOSSARY.md).

## Evidence tables

Machine-readable appendix under `build/`. **Start with the catalogs**, then open the TSV:

| Catalog | Folder |
|---|---|
| [Disk identity](docs/catalog/disk_info.md) | `build/disk_info/` |
| [Volume identity](docs/catalog/volume_info.md) | `build/volume_info/` |
| [File tree](docs/catalog/file_tree.md) | `build/file_tree/` |
| [Hash manifest](docs/catalog/hash_manifest.md) | `build/hash_manifest/` |
| [Metadata](docs/catalog/metadata.md) | `build/metadata/` |
| [Reports](docs/catalog/reports.md) | `build/reports/` |
| [Deep archives](docs/catalog/archives.md) | `build/archives/` |
| [Exhibits](docs/catalog/exhibits.md) | `docs/exhibits/`, mailing photo, transcripts |

Checksum inventory: [`build/manifest.tsv`](build/manifest.tsv). How to check those files: [How to verify](docs/08_reproducibility.md).

## How to read this encyclopedia

Every public claim is traceable to JPMI disk/volume reporting; path/timestamp/CNID/hash/system-state reporting; a court opinion or pleading; an attributed participant account; an independent forensic review; or a sourced public-record link.

> **Observed fact → interpretation → limitation**

Court-recited facts, Mac Isaac's later technical account, JPMI-internal measurements, and CBS's exam are **not interchangeable**. The [source matrix](docs/09_source_matrix.md) is the claim index.

## All articles

**Numbered narrative** (stable IDs):

1. [What is JPMI?](docs/01_what_is_jpmi.md)
2. [Provenance — 5 Ws](docs/02_provenance_5ws.md)
3. [Chain of custody](docs/03_chain_of_custody.md)
4. [What is on the copy](docs/04_what_is_on_the_copy.md)
5. [Filesystem for non-experts](docs/05_filesystem_for_non_experts.md)
6. [Timeline and handling](docs/06_timeline_and_handling.md)
7. [Limits and open questions](docs/07_limits_and_open_questions.md)
8. [How to verify](docs/08_reproducibility.md)
9. [Source matrix](docs/09_source_matrix.md)

**Companions:** [Author](docs/AUTHOR.md) · [People](docs/PEOPLE.md) · [The Mac Shop](docs/THE_MAC_SHOP.md) · [Exhibits](docs/EXHIBITS.md) · [Congressional reports](docs/CONGRESS.md) · [Marco Polo v4](docs/MARCO_POLO.md) · [Copy lineages](docs/COPY_LINEAGES.md) · [Where the copies split](docs/BRANCH_DEVIATIONS.md) · [How the files left the laptop](docs/COPY_METHOD.md) · [Diagrams](docs/diagrams/README.md) · [Apelbaum, Fox, Tucker](docs/APELBAUM_FOX.md) · [Timestamps](docs/TIMESTAMPS.md) · [Integrity](docs/INTEGRITY.md) · [Glossary](docs/GLOSSARY.md) · **[full index](docs/INDEX.md)**

---

**Categories:** JPMI · Mac Isaac direct-copy lineage · HFS+ forensic reporting · 2019 Wilmington recovery · metadata/hash witness
