# JPMI Datetime Evidence and 2019–2020 Custody Timeline

**Status: DRAFT for investigator review.**

## 1. Reported volume timestamps

- HFS+ volume creation (reported): **2019-09-26 22:59:02 CDT**
- E01 acquisition record: **2022-04-29** (`HB-IMAGE-2022-04-29.E01`)
- HFS+ volume last write (reported): **2024-11-21 17:40:22 CST**
- Deleted-file catalog report: **empty**

The 2022 acquisition record and 2024 last-write remain a separate report-lineage discrepancy: an immutable E01 acquired in 2022 cannot itself acquire a 2024 filesystem write.

## 2. File timestamp distribution by year

| Year | created | modified | accessed |
|---|---:|---:|---:|
| 1984 | 1 | 0 | 0 |
| 2007 | 1 | 0 | 0 |
| 2012 | 16 | 0 | 0 |
| 2013 | 15 | 0 | 0 |
| 2014 | 32 | 12 | 0 |
| 2015 | 353 | 317 | 0 |
| 2016 | 3,647 | 2,101 | 0 |
| 2017 | 107,817 | 106,873 | 0 |
| 2018 | 107,185 | 102,657 | 0 |
| 2019 | 353,677 | 360,756 | 8,130 |
| 2020 | 14 | 18 | 221 |
| 2022 | 82 | 82 | 564,453 |
| 2024 | 7 | 30 | 30 |

The broad substantive modified-time population is concentrated before the April 2019 repair event.

## 3. 2019–2020 historical custody sequence

| Date / period | Event | Forensic interpretation |
|---|---|---|
| **2019-04-12** | Delaware court record recounts **three damaged laptops** presented to The Mac Shop. One could be used with an external keyboard, one was considered unrecoverable, and one was left for recovery. | Principal repair-shop custody boundary. |
| **2019-04-13** | Biden returned with an external hard drive for the recovered data; Mac Isaac said recovery/transfer was completed. Mac Isaac later described first staging recoverable data on his store server. | Explains a plausible multi-stage recovery lineage. Store-server logs are not available here. |
| **2019-04-17** | $85 invoice sent; equipment not retrieved according to Mac Isaac's pleadings. | Separates completed repair from later custody. |
| **Late July 2019** | Court opinions place the start of Mac Isaac's FBI-related concern/contacts in this period. | Later copies are custody/preservation copies, not ongoing Hunter use. |
| **Sep–Oct 2019** | Mac Isaac later said he created a copy for his father to take to the FBI in Albuquerque. | JPMI's HFS+ creation date falls within this same general copy/FBI period. |
| **2019-09-26** | JPMI HFS+ `Untitled` volume reports creation. | Strong temporal correlation with Mac Isaac's described preservation-copy period; exact physical identity is not yet proved. |
| **2019-12-09** | FBI grand-jury subpoena; laptop, external hard drive, and paperwork surrendered. Delaware Supreme Court states Mac Isaac made an **exact copy** before surrendering the original. | Strongest public anchor for a retained Mac Isaac direct-copy lineage. |
| **Jan–Feb 2020** | Mac Isaac says he reviewed/retained his copy and contacted congressional offices during/after impeachment. | Later opening/review can generate custody metadata without adding Hunter-era content. |
| **2020-08-26** | Mac Isaac contacted Robert Costello; court record states a copy was provided to Costello. | Another direct Mac Isaac derivative before public release. |
| **2020-10-13** | Hunter Biden attorney George Mesires contacted Mac Isaac asking whether he still possessed the laptop. | Immediate pre-publication custody event. |
| **2020-10-14** | New York Post published first laptop story. | Public disclosure boundary. |
| **2020-10-15** | JPMI Desktop `.DS_Store` modified. | Consistent with Finder opening/browsing one day after the story; **not evidence of substantive file injection**. |

## 4. September 26, 2019 correlation

JPMI reports:

```text
HFS+ volume creation: 2019-09-26 22:59:02 CDT
```

Mac Isaac's later public accounts place creation/shipment of a preservation copy for his father's FBI approach in the **September–October 2019** period.

The correct conclusion is:

> **The JPMI volume-creation date is chronologically consistent with the period Mac Isaac says he was creating preservation/FBI copies.**

The evidence does not yet prove that `Untitled` is the exact physical drive his father carried or offered to the Albuquerque FBI office.

## 5. October 15, 2020 Finder activity

JPMI reports:

```text
Users/roberthunter/Desktop/.DS_Store
modified: 2020-10-15 21:18:17
```

`.DS_Store` is Finder metadata. It can change because a directory is opened or its view state changes.

Because the New York Post story broke on October 14, the timing is consistent with the direct-copy environment being opened or browsed after the story became public.

It does **not** establish that an email, photograph, video, or substantive document was injected or altered.

## 6. No identified post-dropoff hacking or external-file injection

The JPMI reporting analyzed here shows later custody and examination activity, but it does not presently identify:

- a hacking tool operating against the direct copy;
- malware or a remote-access intrusion;
- a bulk post-April import of external user files;
- a later cluster of substantive Hunter-created documents;
- an externally injected substantive file.

The correct finding is:

> **No evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting.**

This is independently consistent with CBS News' 2022 examination of an **exact-copy Mac Isaac/FBI-lineage dataset**, which reported no evidence of user-data modification, fabrication, or tampering and no new files originating after April 2019.

Reference: https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/

## 7. Accessed-time clusters

| Year-month | Rows |
|---|---:|
| 2022-03 | 532,375 |
| 2022-04 | 31,942 |
| 2019-09 | 8,130 |
| 2020-10 | 221 |
| 2022-06 | 136 |
| 2024-11 | 30 |

The 2022 access wave is software-scale activity consistent with examination, indexing, hashing, or acquisition—not a person manually opening hundreds of thousands of files.

## 8. Evidence-source limits

This repository does not contain the individual JPMI source-file bytes. It contains forensic reports/manifests sufficient to analyze paths, timestamps, file sizes, reported hashes, HFS+ catalog relationships, aliases, partition/volume identity, and system-state activity.

That is sufficient for accurate structural and provenance analysis within the reporting scope, but it does not allow this GitHub checkout to independently open every source file or recompute every reported source-object hash.

## 9. Sources for historical events

- Delaware Supreme Court, *Isaac v. Politico LLC*, Aug. 25, 2025: https://law.justia.com/cases/delaware/supreme-court/2025/448-2024.html
- Delaware Superior Court, *Mac Isaac v. Cable News Network, Inc.*, Sept. 30, 2024: https://law.justia.com/cases/delaware/superior-court/2024/s22c-10-012-rhr.html
- S.D. Florida, *Mac Isaac v. Twitter*, Aug. 30, 2021: https://law.justia.com/cases/federal/district-courts/florida/flsdce/1%3A2021cv20684/587211/59/
- CBS News exact-copy forensic review, Nov. 21, 2022: https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/
- Washington Post repair/copy chronology, Mar. 30, 2022: https://www.washingtonpost.com/technology/2022/03/30/hunter-biden-laptop-data-examined/
