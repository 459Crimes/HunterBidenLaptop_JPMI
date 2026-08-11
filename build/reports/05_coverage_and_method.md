# JPMI Coverage, Method, and Limits

## 1. Source boundary

This repository publishes a **metadata and hash witness for JPMI**, the John Paul Mac Isaac direct-copy lineage.

The restricted JPMI E01 image is not published or independently mounted by this GitHub checkout. The project works from received forensic reports/manifests normalized into JPMI-specific database tables and derived public artifacts.

That means this repository does **not** contain the individual source-file bytes. It does contain enough reporting to perform reproducible analysis of the storage structure, chronology, reported hashes, catalog relationships, and later system-state activity.

## 2. Coverage figures

| Metric | Value |
|---|---:|
| Normalized JPMI inventory paths | 576,249 |
| Inventory paths with SHA-256 | 331,906 |
| Rank-1 hash-manifest path rows | 655,330 |
| HFS+ CNID map entries | 397,440 |
| TSK timeline rows | 1,259,300 |
| Apple Mail `.emlx` path population | ~128,842 |
| Contact `.vcf` path population | ~77,907 |
| iCloud-related path population | ~12,337 |

The differing row counts represent different forensic dimensions. A path count, CNID count, timeline-event count, and hash-manifest count should not be treated as interchangeable “number of files” figures.

## 3. Integrity finding

The JPMI reporting analyzed here shows later **opening, browsing, indexing, copying, and forensic examination** of the direct-copy environment.

It does **not** presently identify:

- a hacking tool operating against the Mac Isaac direct copy;
- malware or a remote-access event establishing outside intrusion;
- a bulk post-April-2019 import of external user files;
- a later cluster of substantive Hunter-created documents;
- an identified externally injected email, photograph, video, or document.

The later changed rows are overwhelmingly Finder, Spotlight, DocumentRevisions, directory, temporary, and other system/application metadata.

The bounded conclusion is:

> **No evidence of post-dropoff hacking or external substantive-file injection has been identified in the JPMI reporting. Later metadata is consistent with custody and forensic handling.**

That conclusion is independently consistent with CBS News' 2022 examination of an **exact-copy Mac Isaac/FBI-lineage dataset** supplied by Mac Isaac's lawyer Brian Della Rocca. CBS reported that Computer Forensics Services found no evidence that user data had been modified, fabricated, or tampered with and no new files originating after April 2019.

Reference: https://www.cbsnews.com/news/hunter-biden-laptop-data-analysis/

## 4. Hash method

The public hash export is JPMI-only.

`build/hash_manifest/01_sha256_by_cnid_*.tsv` records canonical HFS+ catalog identities together with reported SHA-256 values and paths.

A SHA-256 value in this repository is a **reported JPMI-manifest value** unless the repository explicitly states that the hash was recomputed from source bytes.

Because the restricted E01 is not mounted here, the correct wording is:

> “The JPMI forensic manifest reports SHA-256 X for this represented object.”

That is different from claiming that the current GitHub checkout independently read the source object and calculated the value itself.

## 5. What the reports can accurately establish without source bytes

The forensic reporting is detailed enough to support accurate analysis of:

- disk model, serial, sector geometry, and acquisition identifiers;
- partition map, GPT/EFI/HFS+ structure, GUIDs, and volume identity;
- directory hierarchy and user-home structure;
- file populations and represented sizes;
- created/modified/accessed timestamp distributions;
- post-repair changed-row populations;
- HFS+ CNIDs, parent relationships, and aliases/hard links;
- reported SHA-256 identities;
- Spotlight, DocumentRevisions, `.DS_Store`, journal, and other system-state records;
- whether the reporting contains evidence of a bulk later substantive-user-file population.

This is sufficient for **structural, timeline, and provenance analysis**.

## 6. What cannot be independently established without source bytes

This GitHub checkout cannot independently:

- open and display every JPMI source file;
- recompute every source-object hash;
- freshly carve unallocated space;
- inspect file-internal metadata not present in the reports;
- prove byte-for-byte identity of every individual source object from first principles.

The absence of source bytes therefore limits fresh content-level verification. It does not erase the evidentiary value of the extensive forensic reporting.

## 7. Reproducibility method

The pipeline performs read-only PostgreSQL queries and writes derived artifacts under `build/`.

Stages:

1. file-tree export;
2. JPMI-only hash identity export;
3. metadata distributions;
4. disk/partition/volume identity export;
5. database-derived JPMI reports;
6. publication of the sourced 2019–2020 custody timeline;
7. deep metadata archives;
8. size/checksum validation.

Historical custody claims are sourced separately in `docs/09_source_matrix.md` rather than manufactured from database timestamps.

## 8. Copy-method boundary

The structure supports describing JPMI to the public as a **whole-volume or filesystem-preserving, `dd`-style copy lineage**.

That phrase does not prove:

- that John Paul Mac Isaac literally used `dd`;
- that the final Crucial X6 was cloned directly from the original internal SSD in one operation;
- that no intermediate server, image, restore, or filesystem-aware copy step existed.

Mac Isaac has described staging recoverable data on his store server before transfer. The present project does not possess those server logs or first-generation copy commands.

## 9. September 2019 custody correlation

JPMI reports the HFS+ `Untitled` destination created on **September 26, 2019**.

Mac Isaac's later accounts place creation/shipment of a preservation copy for his father's FBI approach in the **September–October 2019** period.

The dates are chronologically consistent, but current records do not prove `Untitled` was the exact physical FBI-intended copy.

## 10. Mac Isaac/FBI exact-copy anchor

The Delaware Supreme Court's 2025 opinion states that before Mac Isaac surrendered the original laptop and external hard drive to the FBI under subpoena on December 9, 2019, he made an **exact copy** of the hard drive.

That is the strongest public anchor for a direct Mac Isaac preservation-copy lineage before broad public distribution.

## 11. Todd Sanders / America Project source-delivery bridge

The JPMI acquisition record includes:

```text
hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)
```

Public-record reporting identifies Todd Sanders as affiliated with Patrick Byrne's America Project. The America Project supported/funded Mac Isaac's 2022 litigation, and Brian Della Rocca represented Mac Isaac and later supplied CBS with an exact-copy Mac Isaac/FBI-lineage dataset.

This places the JPMI reports in the **same Mac Isaac-centered provenance network**, while not yet proving that Sanders possessed the literal same physical media CBS examined.

## 12. Timestamp and acquisition boundary

The acquisition record separately identifies `HB-IMAGE-2022-04-29.E01` and reports April 29, 2022. The delivered volume metadata reports a November 21, 2024 last-write.

An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write. The repository therefore treats that pair as an **unresolved source-chronology discrepancy**.

That later report-lineage issue is separate from the 2019–2020 direct-copy integrity finding.

## 13. Core conclusion

JPMI can be characterized from its own internal forensic witness and its sourced custody history:

> **It is a Mac Isaac direct-copy lineage containing a broad `roberthunter` Mac user/application environment. The reporting shows later custody and forensic handling but no identified post-dropoff hacking or substantive external-file injection. Although the public repository lacks source-file bytes, the reports contain sufficient filesystem, timestamp, hash, catalog, and acquisition detail for accurate structural and provenance analysis.**

The strongest remaining gaps are the undocumented first recovery/server-copy records, proof tying the September 26 HFS+ volume to a specific 2019 physical copy, the exact transfer route into Todd Sanders' custody/reporting, byte-identity proof between the JPMI source and the CBS exact-copy media, and reconciliation of the later 2022/2024 report chronology.
