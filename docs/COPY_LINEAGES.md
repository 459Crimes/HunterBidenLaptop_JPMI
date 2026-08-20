# Copy lineages

> **Hatnote.** This article distinguishes **physical devices and copies**. JPMI is one named lineage. It is not a synonym for every file that later appeared in political circulation. See [Scope](SCOPE.md).

Digital provenance fails when people collapse JPMI, APFS, GAI, 0728, and press extracts into the phrase “the laptop.” This page keeps them separate.

## Objects that are not the same thing


| Object                        | What it is                                                                      | Status in this encyclopedia                                                                                                                                                            |
| ----------------------------- | ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Retained repair laptop**    | The one of three machines left 12 Apr 2019                                      | Original hardware; FBI took it 9 Dec 2019; not returned to anyone, per this project’s open-questions list                                                                              |
| **Customer external HDD**     | Drive brought 13 Apr 2019 for recovered data                                    | Surrendered to FBI 9 Dec 2019 with the laptop                                                                                                                                          |
| **Store server staging**      | Mac Isaac's intermediate step                                                   | His account; **logs not held**                                                                                                                                                         |
| **Father / Albuquerque copy** | Preservation copy Mac Isaac describes for Sep–Oct 2019 FBI approach             | Period consistent with HFS+ creation 26 Sep 2019; **physical identity unproved**                                                                                                       |
| **Pre-surrender exact copy**  | Copy Mac Isaac made **before** FBI pickup, per Delaware Supreme Court           | Strongest public anchor that a Mac Isaac direct copy existed independently of FBI custody                                                                                              |
| **BOOT01**                    | Shop copy containing Mojave **18G103**, created **after 26 Sep 2019**           | Ancestor of COSTELLO / APFS / GAI. Payload mtimes 19–21 Sep are Apple package dates, not create date. [Branch splits](BRANCH_DEVIATIONS.md)                                            |
| **Costello copy (COSTELLO)**  | Aug 2020 transfer of **BOOT01** (or a clone) to Giuliani’s attorney             | **Never JPMI.** NY Mag: Costello **booted** to login **Robert Hunter**. Host/monitor writes **28–31 Aug 2020** on APFS/GAI only                                                        |
| **TRIMARCO**                  | COSTELLO grandchild ~**1 Sep 2020+**; Burisma Desktop dump                     | Rose group with **APFS**, **MARYMAN**, **GUSTAV**. **TRIMARCO → APFS** volume **12 Dec 2020**. [Branch splits](BRANCH_DEVIATIONS.md)                                                     |
| **BLAP01**                    | COSTELLO grandchild ~**1 Sep 2020+**; no Burisma dump                          | Teal group; ancestor of **GAI** `Biden Lap 2` (**17 May 2021**). [Branch splits](BRANCH_DEVIATIONS.md)                                                                                  |
| **NY Post material**          | Published 14 Oct 2020 via Giuliani                                              | Public event; not a disk serial                                                                                                                                                        |
| **CBS / CFS “exact copy”**    | Della Rocca → CBS, examined 2022                                                | Independent forensic result on a Mac Isaac/FBI-lineage copy                                                                                                                            |
| **Sanders / JPMI media**      | Della Rocca → Sanders (mailing packet) → reports in this repo                   | Later custody medium is the **Crucial X6**; image `HB-IMAGE-2022-04-29.E01`                                                                                                            |
| **Apelbaum retained copy**    | Oct 2020 imaging of Mac Isaac’s still-held copy                                 | **JPMI lineage**, not hash-identical to the X6 E01. The copy Apelbaum tried to get to Fox / Tucker. **Not** 0728                                                                       |
| **Hayes APFS (**`APFS`**)**   | **TRIMARCO group.** Volume created **12 Dec 2020**; CCC snapshots **5 Jan 2021** | Not a clone of JPMI `Untitled`. [Branch splits](BRANCH_DEVIATIONS.md)                                                                                                                  |
| **MARYMAN**                   | Maryman imaged a related SanDisk **4 Apr 2021**                                 | APFS-family; serial `20142M400253`                                                                                                                                                     |
| **GUSTAV**                    | Dimitrelos / Washington Examiner **May–Jun 2022**                               | APFS-structure; not JPMI                                                                                                                                                               |
| **TODD** (APFS working copy)  | After **5 Jan 2021**                                                            | Distinct from Della Rocca→Sanders **JPMI** packet. Todd said he **altered it to boot**; graph color splits here from TRIMARCO/APFS/MARYMAN/GUSTAV                                       |
| **HAYES**                     | After **5 Jan 2021**, from TODD                                                 | Working copies Conan Hayes then distributed                                                                                                                                            |
| **MPOLO**                     | **Jun 2021** (their schematic)                                                  | Hayes **bootable laptop with user files** — a **degraded** copy missing key user files including **password vaults**. Dashed HAYES outbound; **not** JPMI                                                                 |
| **IPHONE**                    | iPhone backup present on **all** named copies                                   | Backup is on the copies; **password provided by Hayes on 2021-06-02**. Graph edges from **IPHONE** back to **HAYES** and **MPOLO**. Not a fifth volume clone. Out of scope for JPMI tables except as a named object |
| **APFS***                     | MEGA **13 Jun 2022** (file datestamp)                                           | Image file `RHB_Boot.imgc` to **Marc Aaron DeGiovanni**. When analyzed: APFS / Hayes’s APFS. Not a USB stick. Not JPMI                                                                                                                                     |
| **GAI HFS+**                  | Truncated `Biden Lap 2` image (`GAI://`); volume activity **17 May 2021**       | **BLAP01 / GAI** group. Full OS; same Aug 2020 ColorSync ICCs as APFS. Parallel bootable-branch rebuild. **Not** this GitHub tree                                                                              |
| **0728 Extra Found Files**    | Hayes MEGA bag after **28 July 2021**                                           | **Completely separate corpus** — not a clone of JPMI, APFS, or GAI. Blobs match **every combination** of those three (3, 2, 1, or none). Large share: original names and metadata stripped; provenance unknown. Out of scope for JPMI tables |
| **Marco Polo Report v4**      | Published compilation (4th printing 2024)                                       | Analyzed **MPOLO** (Hayes **bootable laptop**, Jun 2021 — degraded; missing password vaults) plus **0728**. **Did not analyze JPMI**                                                                                                          |
| **This GitHub repository**    | Metadata/hash witness by **459Crimes / Marc Aaron DeGiovanni**                  | **No source-file bytes**. [Author](AUTHOR.md)                                                                                                                                          |

## Family groups

**SHOP** has three equal children: **RHB_WD**, **JPMI**, and **BOOT01 → COSTELLO**. JPMI and BOOT01 sit at the same rank. Compact graph: [named copy graph](diagrams/named_graph.svg) · [investigative materials](diagrams/investigative_materials.svg).

| Group | Graph color | Nodes | Actions / dates |
|---|---|---|---|
| Shop / hardware | Blue | **LAPTOP**, **SHOP**, **RHB_WD** | Intake **12 Apr 2019**; customer WD **13 Apr 2019** (FBI **9 Dec 2019**) |
| JPMI family | Green | **JPMI**, **CBS / CFS**, Crucial X6 / E01 | Home-only `Untitled` **26–27 Sep 2019**. This encyclopedia |
| BOOT01 / Costello | Amber | **BOOT01**, **COSTELLO** | 18G103 after **26 Sep 2019**; Costello **26 Aug 2020**; live boot **28–31 Aug 2020**. Never JPMI |
| TRIMARCO group | Rose | **TRIMARCO**, **APFS**, **MARYMAN**, **GUSTAV** | Burisma Desktop ~**1 Sep 2020+**. **TRIMARCO → APFS** volume **12 Dec 2020**; CCC **5 Jan 2021**. Maryman **4 Apr 2021**; Gustav **May–Jun 2022** |
| BLAP01 / GAI | Teal | **BLAP01**, **GAI** | No Burisma dump. GAI `Biden Lap 2` **17 May 2021** |
| Todd-altered copies | Violet | **TODD**, **HAYES**, **APFS***, **MPOLO** | After **5 Jan 2021**. Todd **altered his copy to boot**. **MPOLO** is a dashed Hayes outbound (Jun 2021; degraded; missing password vaults). **APFS*** is MEGA **13 Jun 2022** (`RHB_Boot.imgc` image file) |
| IPHONE | Cyan | **IPHONE** | Backup present on the named copies. **Password provided by Hayes on 2021-06-02**. Edges to **HAYES** and **MPOLO** |
| 0728 | Gray dashed | **0728 Extra Found Files** | Hayes MEGA after **28 Jul 2021**. Dashed **MEGA bag; not identity** — not a volume clone |
| 459Crimes | Magenta | **459Crimes** | Investigative-materials graph only. Possession of **APFS*** · **0728** · **GAI** · **JPMI (E01)** · **IPHONE** |

## Diagram

<!-- diagram:named_graph -->
```mermaid
%% Canonical named copy graph.
%% JPMI is not an ancestor of COSTELLO, TRIMARCO, APFS, HAYES, MPOLO, or APFS*.
%% SHOP children: RHB_WD, JPMI, and BOOT01/COSTELLO at equal rank.
%% COSTELLO grandchildren: TRIMARCO group vs BLAP01/GAI.
%% TODD/HAYES/APFS*/MPOLO are a separate color: Todd altered his copy to boot.
%% 0728 is a separate corpus (Hayes MEGA bag). MPOLO is a degraded Hayes outbound.
%% IPHONE backup is on all copies; Hayes supplied the backup password 2021-06-02.
flowchart TB
  classDef shop fill:#dbeafe,stroke:#1d4ed8,color:#111
  classDef jpmi fill:#dcfce7,stroke:#15803d,color:#111
  classDef boot fill:#fef3c7,stroke:#b45309,color:#111
  classDef trim fill:#fecaca,stroke:#b91c1c,color:#111
  classDef gai fill:#ccfbf1,stroke:#0f766e,color:#111
  classDef todd fill:#ddd6fe,stroke:#5b21b6,color:#111
  classDef side fill:#f3f4f6,stroke:#111827,stroke-dasharray: 6 4,color:#111
  classDef phone fill:#e0f2fe,stroke:#0369a1,color:#111

  LAPTOP["LAPTOP<br/>user era to 2019-03<br/>intake 2019-04-12<br/>FVFXC2MMHV29"]:::shop
  SHOP["SHOP<br/>2019-04-12+ store server<br/>logs not held"]:::shop
  RHB_WD["RHB_WD<br/>2019-04-13 customer WD<br/>FBI 2019-12-09<br/>WX21A19ATFF3"]:::shop

  subgraph JP["JPMI family — this encyclopedia"]
    direction TB
    JPMI["JPMI Untitled<br/>2019-09-26/27 home-only<br/>no OS"]:::jpmi
    CBS["CBS / CFS<br/>exact-copy exam 2022"]:::jpmi
    X6["Crucial X6 / E01<br/>HB-IMAGE-2022-04-29"]:::jpmi
  end

  subgraph BOOT["BOOT01 / Costello — never JPMI"]
    direction TB
    BOOT01["BOOT01<br/>after 2019-09-26<br/>18G103 OS + home"]:::boot
    COSTELLO["COSTELLO<br/>2020-08-26<br/>boot 2020-08-28..31"]:::boot
  end

  subgraph TRIM["TRIMARCO group"]
    direction TB
    TRIMARCO["TRIMARCO<br/>~2020-09-01+<br/>Burisma Desktop"]:::trim
    APFS["APFS HB Boot Drive<br/>volume 2020-12-12<br/>CCC 2021-01-05"]:::trim
    MARYMAN["MARYMAN<br/>imaged 2021-04-04"]:::trim
    GUSTAV["GUSTAV<br/>Dimitrelos 2022-05–06"]:::trim
  end

  subgraph BLAPG["BLAP01 / GAI"]
    direction TB
    BLAP01["BLAP01<br/>~2020-09-01+<br/>no Burisma dump"]:::gai
    GAI["GAI Biden Lap 2<br/>volume 2021-05-17"]:::gai
  end

  subgraph TODDGRP["Todd-altered copies"]
    direction TB
    TODD["TODD<br/>after 2021-01-05<br/>altered to boot"]:::todd
    HAYES["HAYES<br/>after 2021-01-05"]:::todd
    MPOLO["MPOLO<br/>Jun 2021<br/>degraded copy; missing password vaults"]:::todd
    APFSstar["APFS*<br/>MEGA 2022-06-13 imgc<br/>to Marc Aaron DeGiovanni"]:::todd
  end

  subgraph PHONE["iPhone backup — present on all copies"]
    direction TB
    IPHONE["IPHONE<br/>iPhone backup on all copies"]:::phone
  end

  subgraph SIDE["0728 Extra Found Files — completely separate corpus"]
    direction TB
    EFF["0728 Extra Found Files<br/>Hayes MEGA after 2021-07-28<br/>not a volume clone of JPMI, APFS, or GAI<br/>blobs match every combo of 3 / 2 / 1 / none<br/>large share: names and metadata stripped"]:::side
  end

  LAPTOP -->|2019-04-12| SHOP
  SHOP -->|2019-04-13| RHB_WD
  SHOP -->|2019-09-26/27| JPMI
  JPMI --> CBS
  JPMI --> X6
  SHOP -->|after 2019-09-26| BOOT01
  BOOT01 -->|2020-08-26| COSTELLO
  COSTELLO --> TRIMARCO
  COSTELLO --> BLAP01
  TRIMARCO -->|2020-12-12| APFS
  BLAP01 --> GAI
  APFS --> MARYMAN
  APFS --> GUSTAV
  APFS --> TODD
  TODD --> HAYES
  HAYES -.->|bootable laptop with user files| MPOLO
  HAYES --> APFSstar
  HAYES -.->|MEGA bag; not identity| EFF
  IPHONE -->|password provided by Hayes on 2021-06-02| HAYES
  IPHONE --> MPOLO
  RHB_WD ~~~ EFF
```

Export: [SVG](diagrams/named_graph.svg) · [JPG](diagrams/named_graph.jpg)
<!-- /diagram:named_graph -->

## Provenance of investigative materials

The named copy graph above is the identity map. A **separate**, compact graph records which of those objects **459Crimes** holds and analyzes. Magenta edges run from **APFS***, **0728**, **GAI**, **JPMI (E01)**, and **IPHONE** into that holdings box. It is not a sixth volume and not a claim that the five sources are the same disk.

<!-- diagram:investigative_materials -->
```mermaid
%% Provenance of investigative materials held by 459Crimes.
%% Separate from named_graph.mmd (full named copy graph).
%% Compact SVG/JPG are hand-laid-out from this node set
%% (docs/diagrams/_render_investigative_materials.py), not mermaid-cli.
%% Possession edges: APFS*, 0728, GAI, JPMI (E01), IPHONE.
%%{init: {"flowchart": {"curve": "linear", "htmlLabels": true, "padding": 6, "nodeSpacing": 16, "rankSpacing": 24}}}%%
flowchart TB
  classDef shop fill:#dbeafe,stroke:#1d4ed8,color:#111
  classDef jpmi fill:#dcfce7,stroke:#15803d,color:#111
  classDef boot fill:#fef3c7,stroke:#b45309,color:#111
  classDef trim fill:#fecaca,stroke:#b91c1c,color:#111
  classDef gai fill:#ccfbf1,stroke:#0f766e,color:#111
  classDef todd fill:#ddd6fe,stroke:#5b21b6,color:#111
  classDef side fill:#f3f4f6,stroke:#111827,stroke-dasharray: 6 4,color:#111
  classDef phone fill:#e0f2fe,stroke:#0369a1,color:#111
  classDef hold fill:#fce7f3,stroke:#be185d,color:#111,stroke-width:2px

  LAPTOP["LAPTOP<br/>user era to 2019-03<br/>intake 2019-04-12<br/>FVFXC2MMHV29"]:::shop
  SHOP["SHOP<br/>2019-04-12+ store server<br/>logs not held"]:::shop
  RHB_WD["RHB_WD<br/>2019-04-13 customer WD<br/>FBI 2019-12-09<br/>WX21A19ATFF3"]:::shop

  subgraph JP["JPMI family — this encyclopedia"]
    direction TB
    JPMI["JPMI Untitled<br/>2019-09-26/27 home-only<br/>no OS"]:::jpmi
    CBS["CBS / CFS<br/>exact-copy exam 2022"]:::jpmi
    X6["JPMI (E01)<br/>Crucial X6 / HB-IMAGE-2022-04-29"]:::jpmi
  end

  subgraph BOOT["BOOT01 / Costello — never JPMI"]
    direction TB
    BOOT01["BOOT01<br/>after 2019-09-26<br/>18G103 OS + home"]:::boot
    COSTELLO["COSTELLO<br/>2020-08-26<br/>boot 2020-08-28..31"]:::boot
  end

  subgraph TRIM["TRIMARCO group"]
    direction TB
    TRIMARCO["TRIMARCO<br/>~2020-09-01+<br/>Burisma Desktop"]:::trim
    APFS["APFS HB Boot Drive<br/>volume 2020-12-12<br/>CCC 2021-01-05"]:::trim
    MARYMAN["MARYMAN<br/>imaged 2021-04-04"]:::trim
    GUSTAV["GUSTAV<br/>Dimitrelos 2022-05–06"]:::trim
  end

  subgraph BLAPG["BLAP01 / GAI"]
    direction TB
    BLAP01["BLAP01<br/>~2020-09-01+<br/>no Burisma dump"]:::gai
    GAI["GAI Biden Lap 2<br/>volume 2021-05-17"]:::gai
  end

  subgraph TODDGRP["Todd-altered copies"]
    direction TB
    TODD["TODD<br/>after 2021-01-05<br/>altered to boot"]:::todd
    HAYES["HAYES<br/>after 2021-01-05"]:::todd
    MPOLO["MPOLO<br/>Jun 2021<br/>degraded copy; missing password vaults"]:::todd
    APFSstar["APFS*<br/>MEGA 2022-06-13 imgc<br/>to Marc Aaron DeGiovanni"]:::todd
  end

  subgraph PHONE["iPhone backup — present on all copies"]
    direction TB
    IPHONE["IPHONE<br/>iPhone backup on all copies"]:::phone
  end

  subgraph SIDE["0728 Extra Found Files — completely separate corpus"]
    direction TB
    EFF["0728 Extra Found Files<br/>Hayes MEGA after 2021-07-28<br/>not a volume clone of JPMI, APFS, or GAI"]:::side
  end

  subgraph HOLD["Investigative materials"]
    direction TB
    CRIMES["459Crimes<br/>has possession of these five sources<br/>APFS* · 0728 · GAI · JPMI (E01) · IPHONE<br/>and has compiled the most in-depth<br/>analysis of the laptop ever conducted"]:::hold
  end

  LAPTOP -->|2019-04-12| SHOP
  SHOP -->|2019-04-13| RHB_WD
  SHOP -->|2019-09-26/27| JPMI
  JPMI --> CBS
  JPMI --> X6
  SHOP -->|after 2019-09-26| BOOT01
  BOOT01 -->|2020-08-26| COSTELLO
  COSTELLO --> TRIMARCO
  COSTELLO --> BLAP01
  TRIMARCO -->|2020-12-12| APFS
  BLAP01 --> GAI
  APFS --> MARYMAN
  APFS --> GUSTAV
  APFS --> TODD
  TODD --> HAYES
  HAYES -.->|bootable laptop with user files| MPOLO
  HAYES --> APFSstar
  HAYES -.->|MEGA bag; not identity| EFF
  IPHONE -->|password provided by Hayes on 2021-06-02| HAYES
  IPHONE --> MPOLO
  APFSstar --> CRIMES
  EFF --> CRIMES
  GAI --> CRIMES
  X6 --> CRIMES
  IPHONE --> CRIMES
```

Export: [SVG](diagrams/investigative_materials.svg) · [JPG](diagrams/investigative_materials.jpg)
<!-- /diagram:investigative_materials -->

## 0728 is a separate corpus

Treat **0728 Extra Found Files** as a **completely separate corpus**. The dashed edge from **HAYES** is a **MEGA distribution path** (after **28 July 2021**). It is not volume identity: 0728 is not a clone of JPMI `Untitled`, not a clone of APFS `HB Boot Drive`, and not a clone of GAI `Biden Lap 2`.

**Observed.** SHA-256 matching of 0728 blobs against those three inventories is **not** a single overlap class. The same bag contains media that matches **all three**, each **pair**, each **singleton**, and **none** of JPMI / APFS / GAI.

| 0728 blob vs JPMI, APFS, GAI | What that can mean |
|---|---|
| All three | Same bytes exist in JPMI, APFS, and GAI. Shared `roberthunter` ancestry at content level; 0728 is still not those disks |
| Each pair only | JPMI∩APFS, JPMI∩GAI, or APFS∩GAI, absent from the third. Content-level cousins, not a fourth volume |
| Exactly one | Present in JPMI only, APFS only, or GAI only |
| None of the three | Unknown to the three named laptop-derived inventories |

**Observed.** A large portion of 0728 files has **original names and filesystem metadata stripped**. Those rows do not carry a usable path/time provenance even when the bytes hash to a known object. When they also hash to none of the three, origin is unknown.

**Interpretation.** Mixing 0728 into a sentence about JPMI, APFS, or GAI as if it were “the laptop” is a category error. Marco Polo used this sidecar **plus** **MPOLO**, a Hayes **bootable laptop with user files** that is a **degraded** copy (missing key user files including **password vaults**). That still does not make 0728 a JPMI table.

**Limitation.** This encyclopedia does not republish 0728 inventories. The author’s FBI referral on 0728 as potentially hacked is **out of scope**. See [Scope](SCOPE.md) · [Integrity](INTEGRITY.md) · [Author](AUTHOR.md).



## What “direct copy” means here

**JPMI belongs to a Mac Isaac-made lineage that existed before the original laptop and customer drive left his possession** (court-recited exact copy on 9 Dec 2019). The destination HFS+ volume was created **26 Sep 2019** by **formatting** `Untitled` **and copying** `roberthunter` **as files**, then later **volume-cloned** onto the X6. That is not a serial-number chain from the 12 April laptop SSD to serial `2145E498755E`. Method: [COPY_METHOD](COPY_METHOD.md).

The Costello/Giuliani/Hayes **bootable** copies descend from **BOOT01** (18G103, after 26 Sep 2019), **not** from examined `Untitled`. **Costello never received JPMI.** Split points: [Where the copies split](BRANCH_DEVIATIONS.md).

## Byte-identity with CBS

**Established from the common source** (same attorney, same purpose: unadulterated Mac Isaac/FBI-lineage copy). **Not** established by a published side-by-side hash of the CBS media against `HB-IMAGE-2022-04-29.E01` MD5 `682619c1884e6fe006664ba31deed698` / SHA-1 `fe918f0cff3304ab52875b984c88fee78ec05197`.

## How many copies?

Unknown. Mac Isaac describes copies he made. The public record does not establish a complete inventory of every clone in the preservation-copy period. That is an explicit open question.

## See also

- [Diagrams](diagrams/README.md)
- [Evidence catalog](catalog/README.md)
- [Chain of custody](03_chain_of_custody.md)
- [How the files left the laptop](COPY_METHOD.md)
- [Where the copies split](BRANCH_DEVIATIONS.md)
- [Crucial X6](CRUCIAL_X6.md)
- [Mailing packet](MAILING_PACKET.md)
- [Marco Polo v4](MARCO_POLO.md)
- [Integrity](INTEGRITY.md)

