# 3. JPMI Chain of Custody

> **Encyclopedia.** Narrative companion to [Copy lineages](COPY_LINEAGES.md) and [Timeline](TIMELINE.md). Full sourced chronology: [06](06_timeline_and_handling.md). Exhibit: [Mailing packet](MAILING_PACKET.md). [Index](INDEX.md).

A digital chain of custody identifies **which device or copy existed at each stage, what operation was performed, who handled it, and what evidence supports the transition**.

JPMI has a partially documented chain. The strongest public evidence comes from Delaware court opinions incorporating Mac Isaac's pleadings, Mac Isaac's own later accounts, the December 2019 FBI subpoena sequence, and a later independent forensic examination of an exact-copy Mac Isaac/FBI-lineage dataset.

This repository separates direct evidence from inference.

## Stage 1 — April 12, 2019: three damaged laptops arrive

The Delaware Supreme Court's 2025 opinion recounts the pleaded history that **three damaged laptops** were brought to John Paul Mac Isaac's Wilmington repair shop.

According to that record:

1. one laptop could be made usable with an external keyboard Mac Isaac supplied;
2. another was considered unrecoverable;
3. the remaining laptop was left with Mac Isaac for data recovery;
4. a repair authorization was signed.

This is the principal custody boundary for the direct-copy provenance examined here.

The JPMI reporting contains years of older material because a Mac user environment can include cloud-synchronized data, device backups, migrated files, email, application databases, and historical material from prior Macs. The presence of an older artifact does not prove that artifact was created on the one physical computer left for repair.

## Stage 2 — April 13, 2019: external hard drive and recovery completion

The next day, at Mac Isaac's request, Biden returned with an **external hard drive** onto which the recovered data was to be transferred. The Delaware opinions state that Mac Isaac completed the recovery/transfer and contacted Biden that day.

Mac Isaac later gave a more technical account: he first copied recoverable data from the damaged laptop to his **secure store server**, then transferred the recovered data from that server to the customer-supplied external hard drive.

That server-first account describes a multi-stage **file recovery**, not a proved sector copy of the internal SSD:

```text
Damaged laptop
     |
     v
Mac Isaac recovery / store server     [logs not held]
     |
     +--> customer-supplied external hard drive
     |
     +--> 26 Sep 2019: new HFS+ Untitled (file-aware copy of roberthunter)
               |
               v
          later volume clone onto Crucial X6 (after Aug 2020)
```

The present repository does not hold the store-server logs, original copy commands, or first-generation hashes. The server step is Mac Isaac's account. What JPMI **does** show is the September destination: a new volume, preserved user timestamps, empty hard-link directories — not a cloned laptop partition. See [COPY_METHOD](COPY_METHOD.md).

## Stage 3 — April–July 2019: completed repair, no pickup

Mac Isaac sent an $85 invoice on April 17. His pleadings state that the laptop and external drive were not reclaimed or paid for despite attempts to contact Biden.

The JPMI inventory's substantive user/application modifications are overwhelmingly concentrated before the repair-shop period. The later activity identified in the current reports is sparse by comparison and heavily dominated by system/application metadata.

Nothing in the JPMI reporting analyzed here establishes post-dropoff hacking or injection of substantive external user files during this period.

## Stage 4 — late July through fall 2019: FBI concern and preservation copies

Court opinions state that Mac Isaac became concerned in July 2019 and entered a period of contacts involving the FBI and others.

Mac Isaac later said that he made a copy for his father, retired Air Force Col. Richard “Steve” Mac Isaac, to take to the FBI in Albuquerque. Public accounts vary over whether the father's FBI visit occurred in September or October, but they consistently place the copy/FBI effort in the **September–October 2019** period.

This historical window matters because JPMI reports the HFS+ destination volume `Untitled` as created:

```text
2019-09-26 22:59:02 CDT
```

The timing is therefore **consistent with the period Mac Isaac was creating preservation/FBI copies**.

The current evidence does not prove that `Untitled` is the exact physical drive Mac Isaac sent to his father. That remains an open custody question.

## Stage 5 — December 9, 2019: FBI subpoena and exact preservation copy

This is the strongest public custody anchor.

The Delaware Supreme Court states that, after receiving a federal grand-jury subpoena, Mac Isaac turned over the laptop and external hard drive to the FBI. The court further states that **before he parted ways with the original, he made an exact copy of the hard drive**.

That fact is central to the meaning of JPMI.

> **JPMI belongs to a Mac Isaac direct-copy provenance lineage that existed before the original laptop and customer hard drive left Mac Isaac's possession.**

This distinguishes the source conceptually from later political/media datasets whose first documented custody event begins after broad public circulation.

## Stage 6 — 2020: retained copy reviewed and distributed

Mac Isaac continued to possess a preservation copy after the FBI took the original hardware.

During the first Trump impeachment proceedings and afterward, he attempted to alert members of Congress.

In August 2020, Mac Isaac contacted Robert Costello, attorney for Rudy Giuliani. Court records state that Mac Isaac supplied Costello with a copy of the recovered data and the repair authorization. That copy is **BOOT01**, not JPMI `Untitled`. *New York* magazine later reported that Costello **booted** that class of drive to a **Robert Hunter** Apple login. Comparative ColorSync/ByHost dates: [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md).

On October 13, 2020, Hunter Biden's attorney George Mesires contacted Mac Isaac asking whether he still possessed Biden's laptop.

On October 14, 2020, the New York Post published the first laptop story after receiving material through Giuliani.

The following day, JPMI records:

```text
JPMI://Users/roberthunter/Desktop/.DS_Store
modified: 2020-10-15 21:18:17
```

That is a useful custody marker. `.DS_Store` is Finder metadata and can change simply because a directory was opened or browsed.

The conclusion supported by that row is:

> **The direct-copy environment appears to have been opened or browsed around the time the story became public.**

It is **not** evidence that a Hunter document was injected on October 15. The JPMI metadata does not establish that.

## Stage 7 — independent examination of the Mac Isaac/FBI lineage

CBS News reported in November 2022 that Mac Isaac's attorney, **Brian Della Rocca**, supplied what he called an **“exact copy”** of the laptop data provided to federal investigators.

Computer Forensics Services performed an independent analysis. CBS reported that the examiners found:

- no evidence the user data had been modified;
- no evidence it had been fabricated;
- no evidence it had been tampered with;
- **no new files originating after April 2019**;
- a long-running data pattern consistent with ordinary computer use;
- normal use appearing to stop in March 2019, shortly before the repair event.

Reference: [CBS News, Nov. 21, 2022](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)

This does not prove that CBS examined the identical physical Crucial X6 in this repository. It does establish an independently examined **Mac Isaac → FBI exact-copy provenance lineage** whose findings are consistent with the JPMI reporting here. Because the same attorney, Brian Della Rocca, supplied both the CBS dataset and the drive delivered into this project's source chain (see Stage 8), the JPMI media is **byte-identical or virtually byte-identical** to the CBS-examined copy; the equivalence is source-derived and has not been confirmed by an independent side-by-side hash comparison.

## Stage 8 — JPMI reporting enters this project through Todd Sanders

The JPMI acquisition record in this repository includes the source note:

```text
hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)
```

**Direct transfer record.** Todd Sanders received the drive copy from **Brian Della Rocca**, Mac Isaac's attorney, who **coordinated the shipment**; Sanders states that Della Rocca arranged the delivery. This repository holds a photograph of the mailing packet in which the drive copy was shipped to Sanders ([`photo_20260716_120324.jpg`](../photo_20260716_120324.jpg)); the mailing label reflects Mac Isaac's home address as the sender and Todd Sanders as the direct recipient. That photograph is a physical-custody record of the Mac Isaac → Della Rocca → Sanders handoff.

Public reporting and public-record research additionally identify **Todd Sanders as affiliated with Patrick Byrne's America Project**. The America Project publicly funded/supported Mac Isaac's 2022 litigation, and Brian Della Rocca represented Mac Isaac in that litigation.

This provides a meaningful provenance bridge:

```text
Mac Isaac direct copy
       |
       +--> FBI exact-copy lineage
       |         |
       |         +--> Della Rocca → CBS independent forensic review
       |
       +--> Della Rocca → drive shipped directly to Todd Sanders
                 (mailing packet photo; Mac Isaac home address as sender)
                          |
                          +--> JPMI reports/manifests received here
```

The supported conclusion is:

> **The JPMI reports were delivered by Todd Sanders, who received the drive copy from Mac Isaac's attorney Brian Della Rocca, who coordinated the shipment (documented by the mailing-packet photograph held in this repository and Sanders' own account), placing this source within the same Mac Isaac-centered provenance network as the exact-copy dataset supplied by the same attorney to CBS. Given the common source and purpose, the JPMI media is byte-identical or virtually byte-identical to the CBS-examined copy.**

The remaining open link is the forensic one: no independent side-by-side hash comparison of the JPMI media with the CBS-examined media has been published, so byte-identity rests on the common-source relationship rather than a direct hash match.

References:

- [American Oversight — Todd Sanders / America Project affiliation](https://americanoversight.org/in-the-documents-patrick-byrnes-continued-involvement-in-election-denying-efforts/)
- [American Oversight — Sanders identified in America Project operations](https://americanoversight.org/co-defendants-and-unindicted-co-conspirators-what-public-records-reveal-about-trump-allies-election-denial-activities/)
- [CBS News — exact-copy forensic review](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)

## Stage 9 — forensic reports rather than source bytes in this GitHub repository

The GitHub repository does **not** contain the restricted source E01 or the individual source-file bytes.

What it does contain is extensive forensic reporting derived from that source lineage:

- disk and acquisition identity;
- image MD5 and SHA-1;
- partition map and GUIDs;
- HFS+ volume identity;
- HFS+ CNIDs and parent relationships;
- hundreds of thousands of paths;
- file sizes and timestamps;
- reported SHA-256 identities;
- aliases/hard-link mappings;
- filesystem journal/system-state records;
- Spotlight and DocumentRevisions state;
- a TSK timeline;
- deep exported metadata sets.

That distinction matters.

### What the absence of source bytes prevents

Without the restricted source bytes, this GitHub checkout cannot independently:

- open and display every JPMI file;
- recompute every reported SHA-256 from source content;
- perform fresh file-content carving;
- inspect file-internal metadata not present in the reports;
- prove byte-for-byte identity of every individual item from first principles.

### What the reporting is sufficient to do

The reporting is sufficiently detailed to perform **authentic, reproducible structural and provenance analysis within its evidentiary scope**, including:

- reconstructing the directory hierarchy;
- measuring file populations and represented sizes;
- identifying timestamp clusters;
- distinguishing user-era activity from later Finder/Spotlight/examination activity;
- following CNID and alias relationships;
- evaluating the partition and HFS+ layout;
- recording reported object hashes;
- identifying later system-state changes;
- testing whether the metadata contains evidence of bulk post-dropoff user-file insertion.

In other words:

> **JPMI is a metadata/hash forensic witness rather than a public byte dump. It contains enough forensic reporting to support accurate analysis of the copy's structure, chronology, and provenance, while leaving byte-content claims bounded to what the reports actually record.**

## No evidence of post-dropoff hacking or injected substantive files

This conclusion directly addresses a frequent provenance question.

The current JPMI reporting shows later opening, browsing, indexing, copying, and forensic examination.

It does **not** presently show:

- a hacking tool operating against the Mac Isaac copy;
- malware or remote-access evidence establishing an outside intrusion;
- a post-April bulk import of external user files;
- a later cluster of substantive Hunter-created documents;
- evidence that the October 2020 `.DS_Store` activity was anything more than Finder interaction;
- an identified externally injected email, photograph, document, or video.

The bounded conclusion is:

> **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.** No evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting. Later metadata is consistent with custody and forensic handling.

**0728 Extra Found Files** did not come from the laptop files per se (related collection; many unknown origin; some unknown to the laptop). **Marco Polo** analyzed **MPOLO** (Hayes **bootable laptop**, Jun 2021), not JPMI. Those matters are outside this analysis. See [Integrity](INTEGRITY.md) and [Scope](SCOPE.md).

This conclusion is independently consistent with CBS's examination of an exact-copy Mac Isaac/FBI-lineage dataset, which reported no tampering and no new files originating after April 2019.

## Chain diagram

```text
Three damaged laptops presented — Wilmington — 2019-04-12
                         |
                         v
  One retained for recovery; repair authorization signed
                         |
                         v
Customer external hard drive delivered — 2019-04-13
                         |
                         v
Mac Isaac stages recovery on store server
                         |
             [server logs not held]
                         |
                         v
Preservation / FBI-copy activity — Sep–Oct 2019
                         |
             JPMI HFS+ "Untitled" created 2019-09-26  [home-only]
             BOOT01 after 2019-09-26 [18G103; Costello's later object]
                         |
                         v
FBI subpoena and surrender — 2019-12-09
                         |
       Mac Isaac exact copy retained before surrender
                         |
                         v
Costello copy — Aug. 2020  (**BOOT01**, never JPMI)
     → Giuliani → New York Post
     (boot 28–31 Aug host/monitor writes on APFS/GAI)
                         |
                         v
NY Post story 2020-10-14
                         |
       JPMI Desktop .DS_Store modified 2020-10-15
             [opening/browsing, not file injection]
                         |
                         v
Mac Isaac/FBI exact-copy lineage independently examined
              Della Rocca → CBS / CFS
                         |
                         v
Della Rocca → drive shipped directly to Todd Sanders
              [mailing packet photo; Mac Isaac home address as sender]
                         |
                         v
JPMI forensic reports/manifests received by this project
```

## Remaining custody gaps

The most valuable missing records are specific:

1. original Mac Shop server logs or image;
2. first-generation copy commands or application logs;
3. hashes taken when the April 2019 recovery was completed;
4. the exact make/serial/hash of the drive sent to Mac Isaac's father;
5. records showing whether the September 26 `Untitled` HFS+ volume was that FBI-intended copy;
6. an independent side-by-side hash comparison establishing whether the CBS exact-copy media and the JPMI source image are byte-identical (currently established only from the common source);
7. how many copies were made in the preservation-copy period, and where each went;
8. the complete acquisition worksheets associated with `HB-IMAGE-2022-04-29.E01`;
9. reconciliation of the separate 2022 E01 date and reported 2024 HFS+ last-write (Sanders attributes any 2022–2024 alteration to analysis handling, likely a read-write mount on a Mac);
10. any FBI-side disclosure, including why the original laptop and external drive seized December 9, 2019 have not been returned to anyone; only the FBI can verify the FBI-side custody history;
11. which Mac Isaac copy Costello received (bootable OS clone vs home-only `Untitled`); host UUIDs `42800DC4-…` / `E139561C-…` are unnamed as to owner;
12. UUID/hash bridge from Todd’s Trimarco-made bootable to the Hayes SanDisk APFS image.

## Primary/public sources

- [Delaware Supreme Court, *Isaac v. Politico LLC*, Aug. 25, 2025](https://law.justia.com/cases/delaware/supreme-court/2025/448-2024.html)
- [Delaware Superior Court, *Mac Isaac v. Cable News Network, Inc.*, Sept. 30, 2024](https://law.justia.com/cases/delaware/superior-court/2024/s22c-10-012-rhr.html)
- [S.D. Florida, *Mac Isaac v. Twitter*, Aug. 30, 2021](https://law.justia.com/cases/federal/district-courts/florida/flsdce/1%3A2021cv20684/587211/59/)
- [CBS News, Nov. 21, 2022 — independent exact-copy forensic review](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)
- [Washington Post, Mar. 30, 2022 — repair and copy account from Della Rocca](https://www.washingtonpost.com/technology/2022/03/30/hunter-biden-laptop-data-examined/)
- [New York magazine, Sep. 12, 2022 — Costello login “Robert Hunter”](https://nymag.com/intelligencer/article/hunter-biden-laptop-investigation.html)
- [*Biden v. Giuliani* complaint, C.D. Cal. 2:23-cv-8032](https://storage.courtlistener.com/recap/gov.uscourts.cacd.899829/gov.uscourts.cacd.899829.1.0.pdf)
- [Mac Isaac interview, Mar. 27, 2022 — store-server and father/FBI account](https://www.breitbart.com/politics/2022/03/27/nolte-hunter-biden-laptop-whistleblower-john-paul-mac-isaac-the-breitbart-news-interview/)
