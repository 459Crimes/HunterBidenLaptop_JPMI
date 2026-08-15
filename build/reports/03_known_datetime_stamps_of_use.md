<!-- GENERATED/PUBLISHED BY scripts/55_publish_custody_timeline.py. Edit docs/06_timeline_and_handling.md, not this generated copy. -->

# 6. Timeline and Handling

> **Encyclopedia.** Compact index: [Timeline](TIMELINE.md). Integrity: [Integrity](INTEGRITY.md). 2022 vs 2024: [discrepancy](2022_2024_DISCREPANCY.md). Sources: [Source matrix](09_source_matrix.md). This file is the canonical sourced narrative, also published as `build/reports/03_known_datetime_stamps_of_use.md`.

The JPMI records contain multiple layers of time. The most important task is to distinguish **original user/application activity**, **the repair-shop recovery**, **creation of later copies**, **later opening/indexing of those copies**, and **the chronology of the forensic reports themselves**.

This page interweaves two classes of evidence:

1. **JPMI-internal forensic reporting** — filesystem dates, paths, catalog metadata, hashes, and system-state records contained in this repository; and
2. **public custody history** — court findings based on the pleadings, John Paul Mac Isaac's own accounts, contemporaneous reporting, and later forensic review of a Mac Isaac/FBI-lineage copy.

Where those two lines meet in time, the correlation is identified. A correlation is not automatically proof that two physical drives are the same object.

## The central finding

Nothing in the JPMI reporting analyzed here has established that an outside actor hacked the Mac Isaac copy or injected substantive external user files into it after the April 2019 repair-shop event.

That conclusion, stated precisely:

> **The JPMI metadata shows later handling of the copied filesystem, but the later events identified so far are overwhelmingly Finder, filesystem, indexing, and examination artifacts—not evidence of post-dropoff insertion of substantive user files.**

That JPMI finding is consistent with a separate 2022 CBS-commissioned examination of what Mac Isaac's attorney Brian Della Rocca described as an **“exact copy”** of the laptop data supplied to federal investigators. CBS reported that the examiners found **no evidence that the user data had been modified, fabricated, or tampered with, and no new files originating after April 2019**.

That CBS result is important corroboration from the same **Mac Isaac → FBI copy provenance lineage**. Consistent with the source chain, the JPMI media and the CBS-examined copy are **byte-identical or virtually byte-identical**: the same attorney, Brian Della Rocca, provided both copies for the same purpose — an original, unadulterated copy of the Mac Isaac/FBI-lineage data for each party. That equivalence rests on the common source and purpose; an independent side-by-side hash comparison of the two media has not been published.

## Detailed 2019–2020 timeline

| Date / period | Historical custody event | JPMI forensic significance |
|---|---|---|
| **April 12, 2019** | The Delaware Supreme Court record recounts Mac Isaac's allegation that Hunter Biden brought **three damaged laptops** to The Mac Shop. Mac Isaac provided a keyboard that made one usable, determined another was unrecoverable, and retained the remaining laptop for data recovery after a repair authorization was signed. Court Exhibit A is **Quote #7469** ($85; recover to store server). Scan: [Exhibits](EXHIBITS.md). | This is the principal repair-shop custody boundary. Ordinary user activity in the JPMI inventory is heavily concentrated before this date. |
| **April 13, 2019** | At Mac Isaac's request, Biden returned with an **external hard drive** for the recovered data. The court record states that Mac Isaac completed the recovery/transfer that day and called Biden. Mac Isaac later described an intermediate step in which recoverable data was first copied to his **store server** and then transferred to the customer-supplied drive. **Scatter:** Marco Polo v4 (citing Nolte) puts the WD drop and completed recovery on **17 April** instead. The Delaware opinions are the default. | The server account explains why later Mac Isaac copies need not preserve the original laptop's native disk geometry while still preserving a broad user environment. The server step is based on Mac Isaac's account, not an imaging log held here. |
| **April 17, 2019** | Mac Isaac sent an $85 electronic invoice. The laptop and external drive were not retrieved, according to his pleadings. The signed paper form is Quote #7469; the **emailed** invoice later appears as gun-trial **GTX 40** (to `rhbdc@icloud.com`). The GTX 40 image is not on public RECAP; the exhibit list is. [Exhibits](EXHIBITS.md). | Helps separate completed repair work from later custody activity. |
| **Late July 2019** | Court opinions describe Mac Isaac becoming concerned about material he had encountered and beginning a period of contacts involving the FBI, congressional staff, and later Robert Costello. | By this point the repair was months old; any new copy made for law-enforcement or safekeeping purposes is a custody copy rather than Hunter's ongoing use of the laptop. |
| **September–October 2019** | In later interviews and statements, Mac Isaac said he made a copy for his father, retired Air Force Col. Richard “Steve” Mac Isaac, to take to the FBI in Albuquerque. Accounts vary on whether the FBI approach occurred in September or October, but consistently place the copy/FBI effort in this general period. | **JPMI reports its HFS+ destination as created September 26, 2019.** The timing falls inside the same window Mac Isaac described creating and circulating a copy for an FBI approach. This is a strong chronology correlation, but the present evidence does **not** prove that the `Untitled` HFS+ volume is the exact physical drive carried to Albuquerque. |
| **Mid-to-late 2019** | Mac Isaac's accounts say the Albuquerque approach did not result in the FBI taking the drive, after which FBI personnel later contacted the Mac Isaac family and then John Paul Mac Isaac directly. | Provides historical context for why multiple preservation copies may have existed before the formal December seizure. |
| **December 9, 2019** | A federal grand-jury subpoena (**19-3-LFWS-V-136**, AUSA Lesley F. Wolf; proof of service SA Joshua Wilson) required Mac Isaac to turn over the laptop (`FVFXC2MMHV29`), Western Digital drive (`WX21A19ATFF3`), and related paperwork. Photographs: [Exhibits](EXHIBITS.md). Court records state that he complied. The Delaware Supreme Court opinion further states that **before parting with the original, he made an exact copy of the hard drive**. | This is the strongest judicially recited anchor for a preserved Mac Isaac copy existing before the original laptop and customer drive left his custody. It also supports treating later Mac Isaac-lineage forensic material separately from more widely circulated derivative collections. |
| **January–February 2020** | During and after the first Trump impeachment proceedings, Mac Isaac said he became frustrated that the laptop material had not surfaced and attempted to contact members of Congress. | Continued possession/review of a preserved copy is consistent with later Finder/application metadata without implying that new Hunter-created content was added. |
| **August 26, 2020** | Mac Isaac emailed Robert Costello, Rudy Giuliani's attorney, saying he possessed copies of the hard drive. Court records state that Mac Isaac provided Costello a copy of the recovered data and the repair authorization. Marco Polo v4 dates the handoff **28 August 2020**. | Establishes another Mac Isaac-origin derivative before the New York Post publication. |
| **October 13, 2020** | The Delaware Supreme Court record states that Hunter Biden's attorney George Mesires contacted Mac Isaac asking whether he still possessed Biden's laptop. Marco Polo: Mesires conveyed a **2017** drop-off date; Quote #7469 is **April 2019**. | Immediately precedes the public break of the story and provides a concrete custody-context event. |
| **October 14, 2020** | The **New York Post** published its first laptop story at approximately 5:00 a.m. after receiving material through Giuliani. | Public disclosure date. It provides a useful external marker against the JPMI filesystem metadata. |
| **October 15, 2020** | — | JPMI shows `Users/roberthunter/Desktop/.DS_Store` modified **one day after the New York Post story**. Finder can change `.DS_Store` simply from browsing a directory. The timing is therefore consistent with someone opening/examining the direct copy after the story broke. It is **not evidence that substantive Hunter files were injected or edited**. |
| **October 20, 2020** | Marco Polo v4 chain-of-custody schematic: Costello/Giuliani gave a copy to **New Castle County (DE) police**. Not a JPMI acquisition fact. | Another Costello-line derivative. Marco Polo's working machine was Hayes's later **APFS** bootable descendant of JPMI, plus 0728 — not the JPMI reports here. |
| **Late October 2020** | Mac Isaac's lawyer publicly sought to clarify his account to media organizations. | Supports the inference that the direct-copy lineage was being actively reviewed and documented during this period. |

## April 12–13: why the three-laptop story matters

The most authoritative public recitation now appears in the Delaware Supreme Court's 2025 decision. Its dissent summarizes the underlying pleaded facts this way:

- three damaged laptops were brought to the shop;
- a keyboard allowed one machine to be used;
- another machine was considered unrecoverable;
- one laptop remained for recovery;
- the next day an external hard drive was supplied for the recovered data;
- Mac Isaac completed the transfer and notified Biden.

The majority opinion likewise treats the next-day external-drive delivery, same-day recovery completion, invoice, FBI notification, December subpoena, and later exact copy as part of the record.

This matters because “the laptop” is shorthand for a **data-recovery event involving several pieces of hardware**, not proof that every historical file visible in the recovered `roberthunter` environment originated only on one physical Mac.

## The store-server step

Mac Isaac has repeatedly described copying the recoverable data to a **secure store server** during the repair process and then transferring the recovered data from that server to the customer-supplied external drive.

That account is technically significant because it creates a multi-stage chain:

```text
Damaged repair-shop laptop
        |
        v
Mac Isaac store server / recovery workspace
        |
        +--> customer-supplied external hard drive
        |
        +--> later preservation / FBI / safekeeping copies
```

The present repository does not have the server logs, server disk image, copy command, or contemporaneous hashes needed to prove the exact implementation of that step.

Accordingly, Mac Isaac **first copied the recoverable data to his store server**. The step is not independently reconstructed from JPMI metadata, and no contradictory evidence has surfaced; independent verification would require the server logs or the server-side image.

## September 26, 2019: the copy date and the FBI chronology

The JPMI HFS+ volume reports:

```text
HFS+ volume creation: 2019-09-26 22:59:02 CDT
```

Associated filesystem structures include a newly created HFS+ journal and initial Spotlight volume state.

That date now has a meaningful historical context. Mac Isaac's accounts place the creation/shipment of a copy intended for an FBI approach by his father in the **September–October 2019** period.

Therefore:

> **The September 26 JPMI volume-creation date is chronologically consistent with the period in which Mac Isaac was creating preservation/FBI copies.**

The second, equally important sentence:

> **The current records do not establish that the September 26 `Untitled` volume is the exact physical copy his father presented to the Albuquerque FBI office.**

This is a lead for provenance reconstruction, not a completed chain-of-custody finding.

## December 9, 2019: the FBI seizure and the preserved exact copy

The December event provides the cleanest custody anchor in the public legal record.

The Delaware Supreme Court states that, after a federal grand-jury subpoena, Mac Isaac turned over the original laptop and external hard drive to the FBI and **made an exact copy before he parted with the original**.

That preserved-copy event is central to this repository's terminology. JPMI is best understood as belonging to the **Mac Isaac direct-copy lineage**, rather than as a later political/media compilation whose provenance begins after public circulation.

## October 14–15, 2020: public disclosure and an immediate filesystem trace

On October 14, 2020, the New York Post broke the laptop story.

JPMI then records this modification:

```text
Users/roberthunter/Desktop/.DS_Store
modified: 2020-10-15 21:18:17
```

`.DS_Store` is Finder metadata. A modification can occur from opening a directory, changing Finder view state, or other routine browsing activity.

The one-day temporal proximity makes this a useful custody marker:

> **The direct-copy environment appears to have been opened or browsed around the time the story became public.**

It does **not** show a newly inserted Hunter document, altered email, fabricated photograph, or externally injected user file.

## No identified hacking on laptop-derived media

The public record contains many allegations about “hacked,” “infected,” “tampered,” or politically circulated laptop data. Those allegations often concern later copies that moved through different people and organizations.

This repository is narrower, and the attribution rule is:

> **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.**

Files of **non-laptop provenance**, in related 459Crimes investigative work, are attributed **solely** to **Extra Found Files**, a MEGA share from **Conan Hayes after 28 July 2021** (**0728**). A tip and a later FBI report on that corpus are **outside this analysis**.

For the **JPMI direct-copy reporting** available here:

- the dominant substantive user-file activity predates the repair-shop event;
- later modified rows are few compared with the full corpus;
- the later rows identified in the current post-March-2019 slice are dominated by `.DS_Store`, Spotlight, DocumentRevisions, directory, temporary, and other system/application metadata;
- no identified later row has been established here as an externally injected substantive Hunter-created document;
- no JPMI report presently identifies a hacking tool, malware infection, remote-access event, or bulk post-April import of external user files.

The public formulation:

> **The evidence shows the Mac Isaac copy was opened, browsed, indexed, copied, and forensically examined. The JPMI reporting does not show evidence that substantive external files were hacked into or injected into the copy after Hunter Biden's data was left for recovery. No hacking is attributed to this or any other laptop-derived medium; non-laptop provenance is 0728 Extra Found Files only, which is out of scope here.**

This is an evidentiary finding, not a metaphysical claim that no undetectable alteration could ever have occurred.

## Independent corroboration from the Mac Isaac/FBI copy lineage

CBS News reported on November 21, 2022 that Brian Della Rocca, Mac Isaac's lawyer, supplied what he called an **“exact copy”** of the laptop data that had been provided to federal investigators.

Computer Forensics Services examined that copy. CBS reported that the examiners found:

- no evidence that user data had been modified, fabricated, or tampered with;
- no new files originating after April 2019;
- data accumulated over time in a pattern consistent with normal computer use;
- ordinary use appearing to stop abruptly in March 2019, shortly before the repair event.

That is unusually strong public corroboration for the direct Mac Isaac/FBI lineage.

Reference: [CBS News — November 21, 2022](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)

## Connection to this JPMI source delivery

The JPMI acquisition record in this repository contains the note:

```text
hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)
```

Public records independently identify **Todd Sanders as affiliated with Patrick Byrne's America Project**. The America Project also publicly supported/funded John Paul Mac Isaac's 2022 defamation litigation, in which Brian Della Rocca represented Mac Isaac.

**Direct transfer record.** Todd Sanders received the drive copy **directly from Brian Della Rocca**, Mac Isaac's attorney. The repository holds a photograph of the mailing packet in which the drive copy was shipped to Todd Sanders ([`photo_20260716_120324.jpg`](../photo_20260716_120324.jpg), committed with this source-analysis record); the mailing label reflects Mac Isaac's home address as the sender and Todd Sanders as the direct recipient. The photograph provides a direct physical-custody record of the Mac Isaac → Della Rocca → Sanders handoff.

This creates an important provenance bridge:

```text
Mac Isaac direct-copy / FBI lineage
              |
              +--> Della Rocca → CBS forensic examination (exact copy)
              |
              +--> Della Rocca → drive shipped directly to Todd Sanders
                    (mailing packet photo, Mac Isaac home address as sender)
                          |
                          +--> JPMI reports/manifests received here
```

The bounded conclusion is:

> **The JPMI reports come from the same Mac Isaac-centered provenance lineage as the clean copy later supplied by Mac Isaac's lawyer for independent CBS examination.**

Because the same attorney, Brian Della Rocca, supplied both the drive shipped to Todd Sanders and the exact-copy dataset examined by CBS — both for the same purpose of preserving an original, unadulterated copy of the Mac Isaac/FBI-lineage data for each party — the JPMI media is **byte-identical or virtually byte-identical** to the CBS-examined copy. That equivalence is source-derived rather than a published hash comparison; the two sets of media have not been subject to an independent side-by-side hash comparison.

References:

- [Delaware Supreme Court, *Isaac v. Politico LLC*, Aug. 25, 2025](https://law.justia.com/cases/delaware/supreme-court/2025/448-2024.html)
- [Delaware Superior Court, *Mac Isaac v. Cable News Network, Inc.*, Sept. 30, 2024](https://law.justia.com/cases/delaware/superior-court/2024/s22c-10-012-rhr.html)
- [S.D. Florida, *Mac Isaac v. Twitter*, Aug. 30, 2021](https://law.justia.com/cases/federal/district-courts/florida/flsdce/1%3A2021cv20684/587211/59/)
- [CBS News, Oct. 16, 2020 — early Mac Isaac timeline](https://www.cbsnews.com/news/hunter-biden-laptop-new-york-post-story/)
- [CBS News, Nov. 21, 2022 — independent forensic review](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)
- [Washington Post, Mar. 30, 2022 — Della Rocca's description of the repair/recovery and custody sequence](https://www.washingtonpost.com/technology/2022/03/30/hunter-biden-laptop-data-examined/)
- [Mac Isaac interview, Mar. 27, 2022 — store-server and father/FBI account](https://www.breitbart.com/politics/2022/03/27/nolte-hunter-biden-laptop-whistleblower-john-paul-mac-isaac-the-breitbart-news-interview/)

## Limited post-2020 note

The later metadata is useful primarily because it shows that a Mac Isaac direct-copy descendant was **opened, analyzed, indexed, and used to generate forensic reports**.

The important point is that later forensic handling occurred and can create access/index/Finder metadata without implying that Hunter-era substantive content was fabricated.

## The separate 2022/2024 chronology issue

One delivered chronology remains unresolved: the acquisition record identifies `HB-IMAGE-2022-04-29.E01`, while delivered volume metadata reports a November 2024 last-write. An immutable E01 acquired in 2022 cannot itself acquire a 2024 filesystem write.

Sanders states that the only alteration of the data between 2022 and 2024 occurred in the course of **analyzing the data — a mistaken read-write mount on a Mac**. That is a coherent explanation for the later filesystem write: analysis handling of the image in a writable mount can update filesystem metadata without any content fabrication. Only the FBI, or forensic examination of the acquired image, can verify the actual cause.

That later reporting discrepancy must be reconciled separately. It does not alter the 2019–2020 finding that the post-dropoff activity identified in JPMI is principally custody/system-state activity rather than evidence of substantive external-file injection.

## Open FBI-side questions

The FBI has not returned the original laptop or external drive to anyone, and the FBI-side record of the December 2019 seizure, the preservation copy, and subsequent custody has not been publicly disclosed. Only the FBI can verify the FBI-side history — including whether the data it holds matches the JPMI/CBS media. Whether and how many copies were made at the time of the preservation-copy period likewise remains open; Mac Isaac's account describes the copies he made, but the total number of copies created in that period is not established by the public record.

## What the timeline supports

The combined JPMI and public-custody record supports these bounded conclusions:

1. Hunter Biden's data entered Mac Isaac custody through an April 2019 repair/recovery event involving three damaged laptops and a customer-supplied external hard drive.
2. Mac Isaac staged recoverable data on his store server before transfer; the underlying server logs are not presently available here.
3. Mac Isaac was creating/preserving copies for FBI/safekeeping purposes by the September–October 2019 period.
4. JPMI reports a new HFS+ destination created September 26, 2019—chronologically consistent with that copy-creation period, although exact physical identity remains unproven.
5. The FBI subpoenaed and took the original laptop and external drive on December 9, 2019; the Delaware Supreme Court record states Mac Isaac made an exact copy before surrendering them.
6. Mac Isaac provided a copy to Robert Costello in August 2020; Giuliani later supplied material to the New York Post.
7. The New York Post story broke October 14, 2020; JPMI's Desktop `.DS_Store` changed the following day, consistent with opening/browsing the copy.
8. That Finder metadata is **not evidence of injected substantive files**.
9. No hacking is attributed to JPMI. No malware or post-April bulk external-file injection has been identified in the JPMI reporting analyzed here. 0728 Extra Found Files did not come from the laptop files per se (related collection; many unknown origin). Marco Polo analyzed a Hayes bootable APFS later copy of the JPMI disk, not JPMI. Dimitrelos and Maryman used APFS-structure copies. The author's FBI 0728 referral is outside this analysis.
10. CBS's independent examination of an exact-copy Mac Isaac/FBI-lineage dataset likewise reported no tampering and no new files originating after April 2019.
11. The repository's manifest delivery is attributed internally to Todd Sanders, who received the drive copy directly from Mac Isaac's attorney Brian Della Rocca (mailing-packet photograph in this repository); the same attorney supplied CBS its exact-copy dataset, and the two media are byte-identical or virtually byte-identical, an equivalence not yet confirmed by an independent hash comparison.

The detailed JPMI row set remains available in [`build/reports/04_post_2019_03_31_timeline.md`](../build/reports/04_post_2019_03_31_timeline.md).
