# 9. Source Matrix — JPMI Custody and Integrity Claims

> **Encyclopedia.** Reading list: [Bibliography](BIBLIOGRAPHY.md). People: [People](PEOPLE.md). Sourcing: [Sourcing and terminology](MANUAL_OF_STYLE.md). [Index](INDEX.md).

This page shows **which source supports which part of the JPMI story**. It separates court-recited facts, Mac Isaac's own later technical account, contemporaneous reporting, independent forensic review, and this repository's internal forensic reporting.

## Source hierarchy

The repository gives the most weight to, in this order:

1. court opinions and incorporated pleadings/documents;
2. contemporaneous documentary records such as the repair authorization, invoice, subpoena, and acquisition manifests;
3. independent forensic examinations;
4. contemporaneous reporting quoting identified participants;
5. later participant recollections/interviews, clearly labeled as such.

A later interview can explain technical details absent from a court opinion. It is not, by itself, an independently verified fact.

## Claim matrix

| Claim | Best supporting source | Attribution |
|---|---|---|
| Three damaged laptops were presented in April 2019 | Delaware Supreme Court dissent summarizing Second Amended Complaint | **Court-recited pleaded history** |
| Mac Isaac supplied a keyboard for one laptop and another was unrecoverable | Delaware Supreme Court dissent | **Court-recited pleaded history** |
| One laptop remained for recovery | Delaware Supreme Court majority/dissent | **Court-recited pleaded history** |
| Biden returned the next day with an external hard drive | Delaware Supreme Court; Delaware Superior Court; S.D. Florida opinion | **Repeated in court records** |
| Recovery/transfer was completed and Biden was contacted | Delaware Supreme Court / Superior Court | **Repeated in court records** |
| Mac Isaac first staged recoverable data on his store server | Mac Isaac declaration/interviews | **Participant account; server logs not available for independent verification** |
| Mac Isaac began FBI-related efforts in summer 2019 | Delaware court opinions | **Court-recited history** |
| A copy was prepared/sent for Mac Isaac's father to approach the Albuquerque FBI office | Mac Isaac later accounts; attorney statements/reporting | **Participant/counsel account; exact drive identity unresolved** |
| JPMI HFS+ `Untitled` reports creation on Sept. 26, 2019 | JPMI `volume_info` / acquisition reporting | **Directly reported JPMI metadata** |
| Sept. 26 falls in the same general period as the father/FBI copy effort | Combined historical + JPMI chronology | **Correlation, not physical-device identification** |
| FBI subpoenaed and took the laptop, external drive, and paperwork Dec. 9, 2019 | Court opinions and subpoena reporting | **Strong custody anchor** |
| Mac Isaac made an exact copy before surrendering the original | Delaware Supreme Court 2025 opinion | **Strong court-recited custody fact** |
| Mac Isaac provided a copy to Robert Costello in Aug. 2020 | Delaware Supreme Court / Superior Court / S.D. Florida | **Repeated in court records** |
| That copy was **BOOT01**, not JPMI `Untitled` | 18G103 public 26 Sep 2019; JPMI has no `/System`; ColorSync 28–31 Aug 2020 on APFS/GAI only | **Interpretation** from comparative inventory + Apple release date; [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md) |
| Costello booted a drive to Apple login “Robert Hunter” | *New York* magazine, 12 Sep 2022 | **Contemporaneous journalism**; not a JPMI table |
| Complaint alleges Costello “booted up” FedEx drive and made “bootable copies” | C.D. Cal. 2:23-cv-8032 (Sep 2023; later dropped) | **Complaint allegation** |
| APFS/GAI have ColorSync iMac + two Dells and ByHost UUIDs dated 28–31 Aug 2020; JPMI does not | `rhb_forensics` `files` sources 1, 116, 122 | **Comparative inventory**; APFS/GAI bytes not in this GitHub tree |
| APFS `HB Boot Drive` constructed 12 Dec 2020 / CCC snapshots 5 Jan 2021 | APFS Spotlight/CCC paths; parent-project custody synthesis | **Comparative inventory** |
| GAI HFS+ volume activity 17 May 2021 with full OS | GAI volume/files inventory | **Comparative inventory** |
| Todd received a Trimarco copy that he had to alter to boot | CybrJstr chat 16 Jul 2026 | **Participant account (this project)**; not the Della Rocca mailing packet |
| Giuliani provided the material to the New York Post | Delaware Supreme Court | **Court-recited history** |
| New York Post first story published Oct. 14, 2020 | New York Post / Delaware Supreme Court | **Public event** |
| JPMI Desktop `.DS_Store` modified Oct. 15, 2020 | JPMI file-time reporting | **Directly reported JPMI metadata** |
| Oct. 15 `.DS_Store` is consistent with browsing, not proof of document injection | macOS artifact interpretation + object type | **Forensic interpretation** |
| CBS examined an “exact copy” supplied by Mac Isaac's lawyer | CBS News, Nov. 21, 2022 | **Independent media-commissioned forensic review** |
| CBS examiners found no user-data modification, fabrication, or tampering | CBS News / Computer Forensics Services | **Independent forensic result** |
| CBS examiners found no new files originating after April 2019 | CBS News / Computer Forensics Services | **Independent forensic result** |
| JPMI reporting does not identify post-dropoff hacking or bulk substantive-file injection | JPMI post-repair timeline/system-state analysis | **Finding from this repository's reporting** |
| JPMI acquisition note attributes rank-2 manifest to Todd Sanders | [disk catalog](catalog/disk_info.md) (`01_acquisition.tsv`) | **Internal source-delivery record** |
| Sanders received the drive copy from Della Rocca, who coordinated the shipment | Mailing-packet photograph `photo_20260716_120324.jpg` (Mac Isaac home address as sender, Sanders as recipient) + Sanders' account | **Direct custody/transfer record in this repository** |
| Todd Sanders was affiliated with the America Project | American Oversight public-record reporting | **Externally documented affiliation** |
| America Project supported/funded Mac Isaac's 2022 litigation | Public statements/reporting about the lawsuit | **Externally documented support relationship** |
| Della Rocca represented Mac Isaac and supplied CBS the exact-copy dataset | Delaware court record + CBS News | **Externally documented** |
| JPMI reports therefore sit in the same Mac Isaac-centered provenance network | Combined internal/external chain | **Supported provenance inference** |
| JPMI media is byte-identical or virtually byte-identical to the CBS-examined copy | Same attorney supplied both for the same purpose | **Established from common source and purpose; not independently hash-verified** |
| Any 2022–2024 data alteration occurred during analysis, a read-write mount on a Mac | Todd Sanders' communications with this project | **Participant account; only the FBI can verify** |
| This encyclopedia is authored by 459Crimes / Marc Aaron DeGiovanni | [Author](AUTHOR.md); *George News* 7 Feb 2024 (live + archive) | **Project identity**, not a JPMI table |
| DeGiovanni first downloaded 0728 from Hayes; was Marco Polo member from May 2021 | Author identification | **Project identity**; does not make Marco Polo's corpus into JPMI |
| Apelbaum tried to get a Mac Isaac copy to Fox / Tucker Carlson | 11 Mar 2025 Apelbaum–DeGiovanni recording; Mac Isaac book (Oct 2020 home imaging) | **JPMI lineage**, not 0728. Audio SHA-256 `6730dafbab412352…` |
| Carlson said Israelis / a Netanyahu-connected man pushed abuse-of-minors allegations to a Fox producer | Tucker Carlson Show interview with Hunter Biden, 10 Aug 2026 | Carlson’s account; he did not name Apelbaum |

## Primary legal sources

### Delaware Supreme Court — 2025

**John Paul Mac Isaac v. Politico LLC, et al., No. 448, 2024 (Aug. 25, 2025).**

Useful for:

- repair-shop history;
- next-day external hard drive;
- FBI notification;
- December subpoena;
- exact copy retained before surrender;
- Costello/Giuliani/New York Post chain;
- dissent's detailed three-laptop/keyboard account.

https://law.justia.com/cases/delaware/supreme-court/2025/448-2024.html

### Delaware Superior Court — 2024

**Mac Isaac v. Cable News Network, Inc., et al., C.A. No. S22C-10-012 RHR (Sept. 30, 2024).**

Useful for:

- April 2019 repair authorization;
- April 13 external drive;
- invoice;
- FBI contacts;
- December subpoena;
- retained copy;
- August 2020 Costello transfer.

https://law.justia.com/cases/delaware/superior-court/2024/s22c-10-012-rhr.html

### S.D. Florida — 2021

**Mac Isaac v. Twitter, Inc., No. 1:21-cv-20684 (Aug. 30, 2021).**

Useful for an earlier court recitation of:

- April 12 repair event;
- April 13 external drive;
- late-July-2019 through Oct.-2020 contacts;
- Dec. 9 subpoena;
- August 2020 Costello copy;
- Oct. 14 New York Post publication.

https://law.justia.com/cases/federal/district-courts/florida/flsdce/1%3A2021cv20684/587211/59/

## Independent forensic source

### CBS News / Computer Forensics Services — 2022

Brian Della Rocca supplied CBS with what he described as an **“exact copy”** of the laptop data provided to federal investigators.

CBS reported that the independent examination found:

- no evidence the user data was modified;
- no evidence it was fabricated;
- no evidence it was tampered with;
- no new files originating after April 2019;
- data accumulated over time consistent with normal use;
- ordinary use appearing to stop in March 2019.

https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/

## Participant technical account

### John Paul Mac Isaac — later store-server/FBI-copy description

Mac Isaac later described:

- one unrecoverable laptop;
- another usable with a keyboard;
- the retained damaged laptop;
- staging recoverable data on his store server;
- asking for a 1 TB external drive;
- making later preservation copies;
- sending a copy to his father for an FBI approach.

This material reconstructs the likely technical workflow. It is labeled as **Mac Isaac's account** because the original store-server logs and copy commands have not been produced here and cannot be independently verified.

https://www.breitbart.com/politics/2022/03/27/nolte-hunter-biden-laptop-whistleblower-john-paul-mac-isaac-the-breitbart-news-interview/

## America Project / Todd Sanders direct-transfer source

The JPMI acquisition record itself says:

```text
notes: hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)
```

**Direct transfer record.** Todd Sanders received the drive copy from Brian Della Rocca, Mac Isaac's attorney, who **coordinated the shipment**; Sanders states that Della Rocca arranged the delivery. The repository holds a photograph of the mailing packet in which the drive copy was shipped to Sanders ([`photo_20260716_120324.jpg`](../photo_20260716_120324.jpg)); the mailing label reflects Mac Isaac's home address as the sender and Todd Sanders as the direct recipient.

American Oversight's public-record reporting additionally identifies Todd Sanders as affiliated with Patrick Byrne's **America Project** and describes his operational role in America Project-funded efforts.

https://americanoversight.org/in-the-documents-patrick-byrnes-continued-involvement-in-election-denying-efforts/

https://americanoversight.org/co-defendants-and-unindicted-co-conspirators-what-public-records-reveal-about-trump-allies-election-denial-activities/

The America Project also publicly supported Mac Isaac's 2022 litigation. The direct Della Rocca → Sanders handoff, combined with the fact that the same attorney supplied CBS its exact-copy dataset for the same purpose, supports the position that the JPMI media and the CBS-examined copy are **byte-identical or virtually byte-identical**; that equivalence is not yet confirmed by an independent side-by-side hash comparison.

## Integrity finding

> **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.** No evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting. The later activity identified is consistent with opening, browsing, indexing, copying, and forensic examination. **0728 Extra Found Files** did not come from the laptop files per se (related collection; many unknown origin). **Marco Polo** analyzed **MPOLO** (Hayes bootable laptop, Jun 2021), not JPMI. **Dimitrelos** (**GUSTAV**) and **MARYMAN** used copies that correlate to **APFS structure**, not JPMI. The author's FBI 0728 referral is outside this analysis. Costello/Trimarco **bootable** handling is documented on APFS/GAI, not on examined `Untitled`: [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md).

## Byte-access limitation

> **This repository does not contain the individual JPMI source-file bytes, but the received forensic reports contain sufficient disk, filesystem, path, timestamp, hash, CNID, alias, and system-state reporting to support reproducible structural and provenance analysis.**

## Claims not established

The present record does not support:

- “Nothing could possibly have been changed.”
- “The laptop partition was sector-copied onto the examined `Untitled` volume.”
- “Todd Sanders had a hash-verified byte-identical copy of the disk CBS examined.”
- “Every post-April timestamp proves tampering.”
- “Extra Found Files / 0728 came from the laptop filesystem.”
- “Marco Polo analyzed the JPMI / Della Rocca / Sanders copy.”
- “Dimitrelos or Maryman examined the JPMI copy.”
- “Every historical artifact was created on the 2019 repair-shop Mac.”
- “The examined JPMI `Untitled` volume is the disk Costello booted in Manhasset.”
- “Todd’s Trimarco bootable is hash-identical to the Hayes SanDisk APFS image.”
- “Costello logged into Hunter’s account by mounting JPMI on his own Mac.”
- “Costello received the examined JPMI `Untitled` volume.”

Byte-identity with the CBS-examined copy is established from the common source and purpose, but is not independently hash-verified.
