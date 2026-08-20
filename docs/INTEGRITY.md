# Integrity (tampering, injection, CBS)

> **Hatnote.** This is the encyclopedia article on **what the JPMI reporting shows about alteration**. It is not a general essay on every laptop copy on the internet. See [Scope](SCOPE.md).

## Bounded finding

> **No evidence of hacking is attributed to JPMI or to any other laptop-derived medium.** Later JPMI metadata is consistent with custody and forensic handling, not with intrusion or planted user files.

“No evidence identified” ≠ “undetectable change is logically impossible.”

## Where unknown-origin files *are* attributed (not this repo)

**Extra Found Files / 0728** (MEGA, Conan Hayes, after 28 July 2021) is a **completely separate corpus**. It is not a clone of JPMI, APFS, or GAI. The same bag contains blobs that match **all three**, each **pair**, each **singleton**, and **none** of those inventories. A large portion has **original names and metadata stripped**. See [Copy lineages](COPY_LINEAGES.md#0728-is-a-separate-corpus).

The author submitted an FBI source-attribution referral on 0728 as **potentially hacked** (`FBI_0728_Source_Attribution_Referral_FINAL_2026-07-28.pdf`, 28 July 2026). That referral is **outside this JPMI analysis**; it is described on [Author](AUTHOR.md). It is not a finding about Quote #7469, the Mac Shop recovery, the FBI-seized MacBook/WD pair, or the Crucial X6 / E01 reports.

**Marco Polo** analyzed **MPOLO**: a Hayes **bootable laptop with user files** (Jun 2021), a **degraded** copy missing password vaults. That machine is downstream of **HAYES ← TODD ← APFS ← TRIMARCO ← COSTELLO ← BOOT01**. It is **not** a descendant of examined JPMI `Untitled`, and Marco Polo **did not analyze JPMI**. Todd’s “altered to boot” describes the **Trimarco object he received**, not a finding that JPMI was hacked. See [Marco Polo v4](MARCO_POLO.md), [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md), and [Scope](SCOPE.md).

## Two independent layers

### 1. This repository’s JPMI tables

- Substantive user/application **modified** activity is concentrated **before** the April 2019 repair.
- After `modified_ts > 2019-03-31`, the inventory slice is **141 rows**: 11 in 2019, 18 in 2020, 82 in 2022, 30 in 2024.
- Those rows are dominated by `.DS_Store`, Spotlight, DocumentRevisions, directories, temporary/system state — not a later corpus of Hunter-authored documents.
- No JPMI report presently identifies malware establishing intrusion, a remote-access event, a bulk post-April import of external user files, or an identified injected email/photo/document/video.

Full row set: [reports catalog](catalog/reports.md) ([`04_post_2019_03_31_timeline.md`](../build/reports/04_post_2019_03_31_timeline.md)).

### 2. CBS / Computer Forensics Services (Nov 2022)

Brian Della Rocca supplied what he called an **“exact copy”** of data provided to federal investigators. CBS reported CFS found:

- no evidence user data was modified, fabricated, or tampered with;
- **no new files originating after April 2019**;
- accumulation consistent with normal use;
- ordinary use appearing to stop in March 2019, shortly before the repair.

https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/

This is **corroboration from the same Mac Isaac → FBI exact-copy *network***. Physical identity with serial `2145E498755E` is **established** from common attorney/purpose, not hash-proved. See [Copy lineages](COPY_LINEAGES.md).

## What later activity *does* show

The copy was **used as a disk** after Hunter-era authorship stopped:

| Marker | What it is consistent with | What it is not |
|---|---|---|
| 2020-10-15 Desktop `.DS_Store` (day after NY Post) | Finder opened/browsed the copied Desktop | Injected Hunter file |
| 2020-10-15 DocumentRevisions / TemporaryItems dirs | Volume mounted on a Mac around public break | New user documents |
| 2022-03 / 2022-04 **accessed** mass (~532k rows in Mar 2022) | Software-scale examination/indexing | Hunter sitting at the machine |
| Spotlight Store-V2 build Apr–Jun 2022 | mdworker / Spotlight on a mounted volume | Authorship of Mail/Photos |
| 2024-11-21 last-write | Later handling or mixed reports | Proof of 2019 content fabrication |

## Frequent confusions

**“Files exist from 2017, so the 2019 laptop is fake.”**  
A Mac home directory routinely contains migrated years. Creation on a prior Mac, restore from backup, or iPhone sync does not require the 2019 chassis to have existed in 2017.

**“October 2020 timestamps mean planted files.”**  
The **object type** matters. Finder and versioning directories changing in October 2020 is the expected signature of **someone opening the copy**, which Mac Isaac and later examiners had every reason to do once the story existed.

**“2022 access times mean the data was written in 2022.”**  
Accessed ≠ modified ≠ created. The 2022 access cluster is huge; the 2022 **modified** user-document population is not.

**“Empty deleted catalog means a wiped plant.”**  
Empty catalog ≠ no deletions ever. See [HFS+ volume](HFS_VOLUME_UNTITLED.md).

## What would actually move the finding

Examples of evidence *not* currently identified here: a post-April cluster of substantive user files with creation/modification inconsistent with copy/restore; tooling that injected Mail; hash mismatches against a first-generation 2019 manifest (no such first-generation hashes are held). Absence of those patterns is the finding.

## See also

- [Limits](07_limits_and_open_questions.md)
- [Timestamps](TIMESTAMPS.md)
- [2022/2024 discrepancy](2022_2024_DISCREPANCY.md)
