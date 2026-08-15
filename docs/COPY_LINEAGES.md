# Copy lineages

> **Hatnote.** This article distinguishes **physical devices and copies**. JPMI is one named lineage. It is not a synonym for every file that later appeared in political circulation. See [Scope](SCOPE.md).

Digital provenance fails when people collapse five objects into the phrase “the laptop.” This page keeps them separate.

## Objects that are not the same thing

| Object | What it is | Status in this encyclopedia |
|---|---|---|
| **Retained repair laptop** | The one of three machines left 12 Apr 2019 | Original hardware; FBI took it 9 Dec 2019; not returned to anyone, per this project’s open-questions list |
| **Customer external HDD** | Drive brought 13 Apr 2019 for recovered data | Surrendered to FBI 9 Dec 2019 with the laptop |
| **Store server staging** | Mac Isaac’s stated intermediate | Account accepted; **logs not held** |
| **Father / Albuquerque copy** | Preservation copy Mac Isaac describes for Sep–Oct 2019 FBI approach | Period consistent with HFS+ creation 26 Sep 2019; **physical identity unproved** |
| **Pre-surrender exact copy** | Copy Mac Isaac made **before** FBI pickup, per Delaware Supreme Court | Strongest public anchor that a Mac Isaac direct copy existed independently of FBI custody |
| **Costello copy** | Aug 2020 transfer to Giuliani’s attorney | Court-recited derivative; **not** automatically the Crucial X6 |
| **NY Post material** | Published 14 Oct 2020 via Giuliani | Public event; not a disk serial |
| **CBS / CFS “exact copy”** | Della Rocca → CBS, examined 2022 | Independent forensic result on a Mac Isaac/FBI-lineage copy |
| **Sanders / JPMI media** | Della Rocca → Sanders (mailing packet) → reports in this repo | Later custody medium is the **Crucial X6**; image `HB-IMAGE-2022-04-29.E01` |
| **This GitHub repository** | Metadata/hash witness | **No source-file bytes** |

## Diagram

```text
Three damaged laptops — Wilmington — 2019-04-12
        |
        +-- keyboard-usable machine (not the recovery subject)
        +-- unrecoverable machine
        +-- retained laptop --+
                              |
                              v
                    store server (Mac Isaac account)
                              |
              +---------------+----------------+
              v                                v
   customer external HDD              later preservation copies
   (to FBI 2019-12-09)                         |
                                               |
                    exact copy retained before FBI surrender
                                               |
              +--------------------------------+------------------+
              v                                v                  v
     Costello (Aug 2020)              Della Rocca “exact copy”    (other copies: count unknown)
              |                                |
              v                                +--> CBS / CFS (2022)
     Giuliani -> NY Post 2020-10-14            +--> Sanders (mailing packet)
                                                      |
                                                      v
                                               Crucial X6 / E01
                                                      |
                                                      v
                                               JPMI reports (this repo)
```

## What “direct copy” means here

**JPMI belongs to a Mac Isaac-made lineage that existed before the original laptop and customer drive left his possession** (court-recited exact copy on 9 Dec 2019), with a destination HFS+ volume created **26 Sep 2019** in the same general period as his described FBI-copy activity.

That is a **conceptual** distinction from collections whose first documented custody event is after broad public circulation. It is **not** a completed serial-number chain from the 12 April laptop SSD to serial `2145E498755E`.

## Byte-identity with CBS

**Assumed** (same attorney, same purpose: unadulterated Mac Isaac/FBI-lineage copy). **Not** established by a published side-by-side hash of the CBS media against `HB-IMAGE-2022-04-29.E01` MD5 `682619c1884e6fe006664ba31deed698` / SHA-1 `fe918f0cff3304ab52875b984c88fee78ec05197`.

## How many copies?

Unknown. Mac Isaac describes copies he made. The public record does not establish a complete inventory of every clone in the preservation-copy period. That is an explicit open question.

## See also

- [Chain of custody](03_chain_of_custody.md)
- [Crucial X6](CRUCIAL_X6.md)
- [Mailing packet](MAILING_PACKET.md)
- [Integrity](INTEGRITY.md)
