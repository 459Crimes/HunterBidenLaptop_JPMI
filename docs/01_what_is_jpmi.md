# 1. What Is JPMI?

> **Encyclopedia.** Main article: [README](../README.md). Index: [all pages](INDEX.md). Related: [Glossary](GLOSSARY.md) · [Crucial X6](CRUCIAL_X6.md) · [Scope](SCOPE.md).

**JPMI** is the shorthand used in this project for the **John Paul Mac Isaac copy**: the Mac Isaac-lineage copy of data recovered from the computer associated with Hunter Biden and left at a Wilmington, Delaware repair shop in 2019.

This repository is about that copy alone. It is a **laptop-derived** medium. **No hacking is attributed to JPMI.** **0728 Extra Found Files** did not come from the laptop files per se. **Marco Polo** analyzed **MPOLO** (Hayes **bootable laptop**, Jun 2021) on the **COSTELLO → TRIMARCO → APFS → TODD → HAYES** line — **not** a descendant of examined `Untitled`, and **not** this copy. See [Scope](SCOPE.md) · [BRANCH_DEVIATIONS](BRANCH_DEVIATIONS.md).

## A useful mental model

For a general reader, JPMI is a **copied Mac home on a later HFS+ disk**, not a folder of selected documents.

The destination has GPT, EFI, a journaled HFS+ volume, CNIDs, Spotlight, Mail/Library/Photos state, and unallocated space. A hand-curated PDF dump does not need those structures.

Volume `Untitled` was created **26 September 2019**; user-file created/modified times from 2016–March 2019 were preserved; the HFS+ hard-link private directories are empty; the home sits at volume root as `roberthunter`. That is a **file-aware copy onto a newly formatted volume**. The Crucial X6 is a 2020+ product, so the 2019 volume reached it by a later **volume clone**. The 2022 E01 is a **forensic image of that stick**. Evaluation: [How the files left the laptop](COPY_METHOD.md).

## Important technical qualification

The April 2019 recovery utility is **not** established. Mac Isaac’s account is store-server staging, then the customer drive. The accurate formulation is:

> **JPMI is a Mac Isaac-lineage copy: file-aware populate of HFS+ `Untitled` (26 Sep 2019), later volume-cloned onto a Crucial X6, represented here by a forensic E01 of that X6.**

## The physical medium described by the forensic record

The acquisition record describes the custody device as:

| Field | Reported value |
|---|---|
| Device | Micron Crucial X6 SSD USB Device |
| Serial | `2145E498755E` |
| Size | `500,107,862,016` bytes |
| Sector size | 512 bytes |
| Sector count | `976,773,168` |
| Source image | `HB-IMAGE-2022-04-29.E01` |
| Image format | E01 |
| Case number | `HB-2022-04-29` |
| Acquisition tool | `ADI4.7.1.2` |
| MD5 | `682619c1884e6fe006664ba31deed698` |
| SHA-1 | `fe918f0cff3304ab52875b984c88fee78ec05197` |

These values are published in the [disk-identity catalog](catalog/disk_info.md) ([`01_acquisition.tsv`](../build/disk_info/01_acquisition.tsv)).

The Crucial X6 is a **custody medium**. It is not the original internal storage hardware of the laptop left at the repair shop.

## What the repository actually possesses

The restricted source image itself is not published in this GitHub repository.

The project works from received forensic metadata and manifests that describe the image, including:

- partition reports;
- HFS+ catalog and CNID information;
- file-list reports;
- file timestamps;
- SHA-256 manifests;
- filesystem timelines;
- volume and disk identity records.

Accordingly, this repository speaks authoritatively about **reported structure, paths, hashes, timestamps, and filesystem relationships**. The GitHub project does not independently re-read every JPMI byte from the restricted E01; it is a metadata-and-hash witness.

## Why JPMI matters

Public discussion often collapses “the laptop” into a collection of emails, photographs, and documents. JPMI is useful because it preserves a much broader evidentiary context.

Instead of asking only:

> Is this document present?

JPMI allows questions such as:

- Where in the Mac user tree was it represented?
- What application or database surrounded it?
- What other files share the same directory context?
- What filesystem identifiers and timestamps are associated with it?
- Does the copied volume contain ordinary system-generated state around the user data?
- When was the destination filesystem created?
- What later handling or indexing activity is visible?

That is the distinction between **content evidence** and **provenance evidence**.
