# 3. JPMI Chain of Custody

A chain of custody is not simply a list of names. For digital evidence, it should identify **which physical device or image existed at each stage, what operation was performed, and what evidence supports the transition from one stage to the next.**

JPMI has a partially documented chain. This repository distinguishes what is known from what remains unresolved.

## Stage 1 — The repair-shop computer

Public reporting places the repair event in **April 2019 at John Paul Mac Isaac's computer repair shop in Wilmington, Delaware**. Mac Isaac has described receiving damaged Apple laptops for data recovery and retaining one computer after it was not reclaimed.

For the purposes of this repository, the important provenance fact is not the political history of the story. It is that **the Mac Isaac custody event is the claimed origin of the copy lineage documented here.**

The original repair-shop computer and its internal storage are not the same physical object as the later Crucial X6 described in the JPMI acquisition record.

## Stage 2 — Recovery and copying under Mac Isaac custody

Data was recovered from the repair-shop computer and preserved outside the original machine.

The current JPMI evidence strongly indicates that the resulting lineage retained a broad Mac environment rather than only a selection of documents. The represented copy contains:

- a normal `roberthunter` home directory;
- large application-state populations;
- filesystem catalog relationships;
- HFS+ journal structures;
- Spotlight and DocumentRevisions state;
- GPT and EFI structures on the later destination;
- unallocated space and filesystem-level metadata.

### What remains unknown at this stage

The present repository does **not** establish:

- the literal recovery command Mac Isaac used;
- whether the first recovery target was a server, image file, external disk, or a combination of those;
- whether the first copy was sector-for-sector, file-by-file, filesystem-aware, or hybrid;
- every intermediate device serial number;
- the exact date each intermediate copy was created.

This is why the repository uses **“`dd`-style”** only as a plain-English analogy for a whole-volume or filesystem-preserving copy lineage, not as a claim about the exact software command.

## Stage 3 — Creation or reconstruction of the later HFS+ destination

The JPMI volume identity reports:

- volume name: `Untitled`;
- filesystem: journaled HFS+;
- volume identifier: `dfe8079582e21400`;
- reported creation: **2019-09-26 22:59:02 CDT**.

That date is important because it is after the April 2019 repair event.

It means the HFS+ destination represented by JPMI should not be described as an untouched physical snapshot whose filesystem itself dates to the moment the laptop was left at the shop. The destination volume was created or reconstructed later.

At the same time, files inside that later volume retain much older timestamps and application structures. That combination is exactly what one expects when an older Mac environment is copied, restored, or reconstructed onto a newly created destination filesystem.

## Stage 4 — Later mounting, browsing, and handling

The JPMI metadata shows later activity after the HFS+ destination was created.

Examples include:

- 2020 `.DS_Store` and application/document-state changes;
- a dominant 2022 accessed-time cluster;
- 2022 Spotlight and DocumentRevisions activity;
- 2024 Spotlight/index structures associated with the reported last-write date.

These events matter to custody because they prove the copy was not permanently frozen after 2019.

They do **not** automatically prove that later handlers inserted substantive user documents. Much of the observed later activity is characteristic of macOS mounting, Finder browsing, Spotlight indexing, and forensic examination.

## Stage 5 — The forensic E01 acquisition

The acquisition record identifies the later custody device as:

- **Micron Crucial X6 SSD USB Device**;
- serial `2145E498755E`;
- size `500,107,862,016` bytes.

It records the image:

```text
HB-IMAGE-2022-04-29.E01
```

with:

```text
MD5   682619c1884e6fe006664ba31deed698
SHA-1 fe918f0cff3304ab52875b984c88fee78ec05197
```

This is the clearest formal forensic-preservation event in the material available to the project.

## Stage 6 — Metadata delivery and this repository

The GitHub project does not publish or independently mount the restricted JPMI E01 image.

Instead, it contains a structured forensic witness derived from received reports and manifests, including:

- acquisition identity;
- partition map;
- file inventory;
- HFS+ CNID hierarchy;
- timestamps;
- SHA-256 object identities;
- alias/hard-link relationships;
- filesystem-system-state summaries;
- deep metadata exports.

The project database records were later normalized into the public tables under `build/`.

## Chain diagram

```text
Computer left for repair — Wilmington, Delaware — April 2019
                         |
                         v
       Data recovery / copy under Mac Isaac custody
                         |
              [intermediate step(s) unresolved]
                         |
                         v
      Later HFS+ destination / Mac Isaac-lineage copy
      volume "Untitled" — reported created 2019-09-26
                         |
                         v
       Later mounting / browsing / indexing / handling
                         |
                         v
       Micron Crucial X6 SSD — serial 2145E498755E
                         |
                         v
       E01 forensic image HB-IMAGE-2022-04-29.E01
                         |
                         v
       Received metadata, reports, and hash manifests
                         |
                         v
        This repository's derived public artifacts
```

## Public historical reference

CBS News reported in November 2022 that Mac Isaac's lawyer supplied what he described as an **“exact copy”** of the laptop data provided to federal investigators, and that an independent forensic review found no evidence that the user data in that copy had been modified, fabricated, or tampered with. That public report provides useful historical context for the existence of a Mac Isaac-preserved copy lineage, but the technical claims in this repository are grounded in the JPMI acquisition and filesystem records published here.

Reference: [CBS News, November 21, 2022 — forensic analysis of a Mac Isaac copy](https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/)

## The unresolved provenance gap

The most important missing evidence remains the **intermediate recovery/copy record between the original repair-shop storage and the later HFS+ custody medium**.

The best evidence to close that gap would be:

1. original repair-shop imaging/recovery logs;
2. source and destination device serial numbers;
3. server-side file or image records, if a server was used;
4. copy-tool logs or command history;
5. hashes recorded at the first recovery stage;
6. dated photographs or inventories of the intermediate devices;
7. contemporaneous custody notes.

Until those records are produced, the repository should state the gap rather than invent a cleaner chain than the evidence supports.
