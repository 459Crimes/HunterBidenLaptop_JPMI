<!-- GENERATED/PUBLISHED BY scripts/55_publish_custody_timeline.py. Edit docs/06_timeline_and_handling.md, not this generated copy. -->

# 6. Timeline and Handling

The JPMI records contain multiple layers of time. The most important task is to distinguish **original user/application activity**, **the repair-shop recovery**, **creation of later copies**, **later opening/indexing of those copies**, and **the chronology of the forensic reports themselves**.

This page deliberately interweaves two classes of evidence:

1. **JPMI-internal forensic reporting** — filesystem dates, paths, catalog metadata, hashes, and system-state records contained in this repository; and
2. **public custody history** — court findings based on the pleadings, John Paul Mac Isaac's own accounts, contemporaneous reporting, and later forensic review of a Mac Isaac/FBI-lineage copy.

Where those two lines meet in time, the correlation is identified. A correlation is not automatically proof that two physical drives are the same object.

## The central finding

Nothing in the JPMI reporting analyzed here has established that an outside actor hacked the Mac Isaac copy or injected substantive external user files into it after the April 2019 repair-shop event.

That conclusion should be stated precisely:

> **The JPMI metadata shows later handling of the copied filesystem, but the later events identified so far are overwhelmingly Finder, filesystem, indexing, and examination artifacts—not evidence of post-dropoff insertion of substantive user files.**

That JPMI finding is consistent with a separate 2022 CBS-commissioned examination of what Mac Isaac's attorney Brian Della Rocca described as an **“exact copy”** of the laptop data supplied to federal investigators. CBS reported that the examiners found **no evidence that the user data had been modified, fabricated, or tampered with, and no new files originating after April 2019**.

That CBS result is important corroboration from the same **Mac Isaac → FBI copy provenance lineage**. It should not be represented as proof that CBS examined the identical physical Crucial X6 described by this repository unless an additional custody record establishes that fact.

## Detailed 2019–2020 timeline

| Date / period | Historical custody event | JPMI forensic significance |
|---|---|---|
| **April 12, 2019** | The Delaware Supreme Court record recounts Mac Isaac's allegation that Hunter Biden brought **three damaged laptops** to The Mac Shop. Mac Isaac provided a keyboard that made one usable, determined another was unrecoverable, and retained the remaining laptop for data recovery after a repair authorization was signed. | This is the principal repair-shop custody boundary. Ordinary user activity in the JPMI inventory is heavily concentrated before this date. |
| **April 13, 2019** | At Mac Isaac's request, Biden returned with an **external hard drive** for the recovered data. The court record states that Mac Isaac completed the recovery/transfer that day and called Biden. Mac Isaac later described an intermediate step in which recoverable data was first copied to his **store server** and then transferred to the customer-supplied drive. | The server account provides a plausible explanation for why later Mac Isaac copies need not preserve the original laptop's native disk geometry while still preserving a broad user environment. The server step is based on Mac Isaac's later account, not an imaging log presently held here. |
| **April 17, 2019** | Mac Isaac sent an $85 electronic invoice. The laptop and external drive were not retrieved, according to his pleadings. | Helps separate completed repair work from later custody activity. |
| **Late July 2019** | Court opinions describe Mac Isaac becoming concerned about material he had encountered and beginning a period of contacts involving the FBI, congressional staff, and later Robert Costello. | By this point the repair was months old; any new copy made for law-enforcement or safekeeping purposes is a custody copy rather than Hunter's ongoing use of the laptop. |
| **September–October 2019** | In later interviews and statements, Mac Isaac said he made a copy for his father, retired Air Force Col. Richard “Steve” Mac Isaac, to take to the FBI in Albuquerque. Accounts vary on whether the FBI approach occurred in September or October, but consistently place the copy/FBI effort in this general period. | **JPMI reports its HFS+ destination as created September 26, 2019.** The timing is notable because it falls inside the same window Mac Isaac described creating and circulating a copy for an FBI approach. This is a strong chronology correlation, but the present evidence does **not** prove that the `Untitled` HFS+ volume is the exact physical drive carried to Albuquerque. |
| **Mid-to-late 2019** | Mac Isaac's accounts say the Albuquerque approach did not result in the FBI taking the drive, after which FBI personnel later contacted the Mac Isaac family and then John Paul Mac Isaac directly. | Provides historical context for why multiple preservation copies may have existed before the formal December seizure. |
| **December 9, 2019** | A federal grand-jury subpoena required Mac Isaac to turn over the laptop, external hard drive, and related paperwork. Court records state that he complied. The Delaware Supreme Court opinion further states that **before parting with the original, he made an exact copy of the hard drive**. | This is the strongest judicially recited anchor for a preserved Mac Isaac copy existing before the original laptop and customer drive left his custody. It also supports treating later Mac Isaac-lineage forensic material separately from more widely circulated derivative collections. |
| **January–February 2020** | During and after the first Trump impeachment proceedings, Mac Isaac said he became frustrated that the laptop material had not surfaced and attempted to contact members of Congress. | Continued possession/review of a preserved copy is consistent with later Finder/application metadata without implying that new Hunter-created content was added. |
| **August 26, 2020** | Mac Isaac emailed Robert Costello, Rudy Giuliani's attorney, saying he possessed copies of the hard drive. Court records state that Mac Isaac provided Costello a copy of the recovered data and the repair authorization. | Establishes another Mac Isaac-origin derivative before the New York Post publication. |
| **October 13, 2020** | The Delaware Supreme Court record states that Hunter Biden's attorney George Mesires contacted Mac Isaac asking whether he still possessed Biden's laptop. | Immediately precedes the public break of the story and provides a concrete custody-context event. |
| **October 14, 2020** | The **New York Post** published its first laptop story at approximately 5:00 a.m. after receiving material through Giuliani. | Public disclosure date. It provides a useful external marker against the JPMI filesystem metadata. |
| **October 15, 2020** | — | JPMI shows `Users/roberthunter/Desktop/.DS_Store` modified **one day after the New York Post story**. Finder can change `.DS_Store` simply from browsing a directory. The timing is therefore consistent with someone opening/examining the direct copy after the story broke. It is **not evidence that substantive Hunter files were injected or edited**. |
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

That account is technically significant because it creates a plausible multi-stage chain:

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

Accordingly, the repository should say **“Mac Isaac states that he first copied the recoverable data to his store server”**, rather than presenting the server operation as independently reconstructed fact.

## September 26, 2019: the copy date and the FBI chronology

The JPMI HFS+ volume reports:

```text
HFS+ volume creation: 2019-09-26 22:59:02 CDT
```

Associated filesystem structures include a newly created HFS+ journal and initial Spotlight volume state.

That date now has a meaningful historical context. Mac Isaac's accounts place the creation/shipment of a copy intended for an FBI approach by his father in the **September–October 2019** period.

Therefore:

> **The September 26 JPMI volume-creation date is chronologically consistent with the period in which Mac Isaac says he was creating preservation/FBI copies.**

But the next sentence is equally important:

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

That distinction should be repeated whenever the 2020 timestamp is discussed.

## No identified post-dropoff hacking or external-file injection

The public record contains many allegations about “hacked,” “infected,” “tampered,” or politically circulated laptop data. Those allegations often concern later copies that moved through different people and organizations.

This repository is narrower.

For the **JPMI direct-copy reporting** available here:

- the dominant substantive user-file activity predates the repair-shop event;
- later modified rows are few compared with the full corpus;
- the later rows identified in the current post-March-2019 slice are dominated by `.DS_Store`, Spotlight, DocumentRevisions, directory, temporary, and other system/application metadata;
- no identified later row has been established here as an externally injected substantive Hunter-created document;
- no JPMI report presently identifies a hacking tool, malware infection, remote-access event, or bulk post-April import of external user files.

The correct public formulation is therefore:

> **We found evidence that the Mac Isaac copy was opened, browsed, indexed, copied, and forensically examined. We did not find evidence in the JPMI reporting that substantive external files were hacked into or injected into the copy after Hunter Biden's data was left for recovery.**

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

This creates an important provenance bridge:

```text
Mac Isaac direct-copy / FBI lineage
              |
              +--> Della Rocca → CBS forensic examination
              |
              +--> Mac Isaac-aligned custody/reporting network
                         |
                         +--> Todd Sanders / America Project affiliation
                                      |
                                      +--> JPMI reports/manifests received here
```

The bounded conclusion is:

> **The JPMI reports come from the same Mac Isaac-centered provenance lineage as the clean copy later supplied by Mac Isaac's lawyer for independent CBS examination.**

What is **not yet proved** is that Todd Sanders received the identical physical disk or identical E01 file that CBS's examiners inspected. That final equivalence requires a direct transfer record or matching acquisition hash.

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

This repository does not need a long post-2020 political history to explain JPMI. The important point is simply that later forensic handling occurred and can create access/index/Finder metadata without implying that Hunter-era substantive content was fabricated.

## The separate 2022/2024 chronology issue

One delivered chronology remains unresolved: the acquisition record identifies `HB-IMAGE-2022-04-29.E01`, while delivered volume metadata reports a November 2024 last-write. An immutable E01 acquired in 2022 cannot itself acquire a 2024 filesystem write.

That later reporting discrepancy must be reconciled separately. It does not alter the 2019–2020 finding that the post-dropoff activity identified in JPMI is principally custody/system-state activity rather than evidence of substantive external-file injection.

## What the timeline supports

The combined JPMI and public-custody record supports these bounded conclusions:

1. Hunter Biden's data entered Mac Isaac custody through an April 2019 repair/recovery event involving three damaged laptops and a customer-supplied external hard drive.
2. Mac Isaac states that recoverable data was staged on his store server before transfer; the underlying server logs are not presently available here.
3. Mac Isaac was creating/preserving copies for FBI/safekeeping purposes by the September–October 2019 period.
4. JPMI reports a new HFS+ destination created September 26, 2019—chronologically consistent with that copy-creation period, although exact physical identity remains unproven.
5. The FBI subpoenaed and took the original laptop and external drive on December 9, 2019; the Delaware Supreme Court record states Mac Isaac made an exact copy before surrendering them.
6. Mac Isaac provided a copy to Robert Costello in August 2020; Giuliani later supplied material to the New York Post.
7. The New York Post story broke October 14, 2020; JPMI's Desktop `.DS_Store` changed the following day, consistent with opening/browsing the copy.
8. That Finder metadata is **not evidence of injected substantive files**.
9. No hacking, malware, or post-April bulk external-file injection has been identified in the JPMI reporting analyzed here.
10. CBS's independent examination of an exact-copy Mac Isaac/FBI-lineage dataset likewise reported no tampering and no new files originating after April 2019.
11. The repository's manifest delivery is attributed internally to Todd Sanders, who is publicly documented as affiliated with the America Project; this ties the delivered reports to the broader Mac Isaac-aligned provenance network without proving physical identity with the CBS examination media.

The detailed JPMI row set remains available in [`build/reports/04_post_2019_03_31_timeline.md`](../build/reports/04_post_2019_03_31_timeline.md).
