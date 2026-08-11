# JPMI/APFS/GAI Hash Discrepancy Report

**Date:** 2026-08-04  
**Database:** Local PostgreSQL `rhb_forensics`  
**Question:** Why do JPMI records contain SHA-256 values absent from the APFS and GAI inventories if all three derive from the same source lineage?

## Executive Assessment

The discrepancy is real at the exact-byte level, but it should not be interpreted as evidence that the JPMI device contained 53,727 additional substantive user documents.

The unmatched population is dominated by volatile or generated material: Photos Library proxies and thumbnails, cache files, CloudKit placeholders, application state, and system-support files. These objects are especially likely to differ between derivative copies and acquisition dates. The APFS and GAI objects are separate derivative branches, not verified byte-complete snapshots of the JPMI device at the same point in time.

The current evidence supports this conclusion:

> JPMI has 53,727 distinct SHA-256 values absent from the direct APFS and GAI hash inventories. Most of that population appears to consist of derivative, cache, or application-state material. The count is not a count of confirmed missing user-created files.

## Scope And Method

The baseline population was constructed from `jpmi_sha256_allpaths`, retaining one representative path per distinct JPMI SHA-256. A hash was classified as unmatched when it had no corresponding row in `hash_sources` for direct APFS source `1` or direct GAI source `116`.

The path/filename scan then compared those unmatched JPMI records against APFS and GAI readable source families, including their cataloged descendants:

- exact normalized path
- exact filename
- bounded fuzzy filename candidates using RapidFuzz

The fuzzy results are leads only. They are not hash matches and are not treated as confirmations.

The scan did not modify PostgreSQL tables or source evidence.

## Population Results

The JPMI inventory contains **180,046 distinct SHA-256 values**. Of those, **53,727** were absent from the direct APFS and GAI hash-source records used for the baseline.

| Result | Distinct JPMI hashes |
|---|---:|
| Exact SHA-256 absent from direct APFS and GAI | 53,727 |
| Exact normalized-path candidates | 626 |
| Exact-filename candidates | 1,095 |
| Fuzzy filename/path candidates | 6,799 |
| No candidate returned by the scan | 53,727 |

The candidate counts are matching categories produced by the path scan. Fuzzy results can have multiple target candidates per JPMI hash and should be reviewed before being described as matches.

The detailed candidate output is:

`forensics/reports/jpmi_unmatched_path_scan_20260804/matches.tsv`

The scan summary is:

`forensics/reports/jpmi_unmatched_path_scan_20260804/summary.txt`

## Unmatched Files By Path Group

The following groups are mutually exclusive classification buckets based on the representative JPMI path. The order of the path rules matters; for example, a Photos Library object is classified as Photos Library before a generic Library object.

| Group | Exploratory count | Aggregate recorded bytes |
|---|---:|---:|
| Photos Library | 31,882 | 4,237,783,114 |
| Caches | 23,006 | 2,474,530,903 |
| Documents | 3,807 | 792,268 |
| Library/system/application support | 2,317 | 533,578,840 |
| Movies | 690 | 118,604,905 |
| Mail | 389 | 164,154,327 |
| Other/unknown | 62 | 885,164,314 |
| Messages | 17 | 52,534,713 |
| Desktop, Downloads, Pictures, other user tree | 77 | 96,000 approximately |

These exploratory category counts are retained as directional evidence only and must not be summed to reconstruct the authoritative unmatched total. The path pattern is nevertheless clear: Photos Library and cache material overwhelmingly dominate the unmatched set. Conventional user-content locations are a small minority.

## File-Type Indicators

The most frequent extensions among unmatched representative paths were:

| Extension/type | Hashes |
|---|---:|
| No extension | 21,082 |
| `.jpg` | 19,505 |
| `.jpeg` | 12,949 |
| `.icloud` | 3,938 |
| `.photoscachefile` | 988 |
| `.txt` | 873 |
| `.vcf` | 417 |
| `.emlx` | 318 |
| `.plist` | 292 |
| `.png` | 150 |
| `.db` | 135 |
| `.db-shm` | 130 |
| `.calldump` | 90 |

The JPEG population is consistent with Photos proxy, thumbnail, and rendered derivative objects. The no-extension population is consistent with cache/database/blob stores and requires path-level interpretation before being labeled user content.

## Why The Hashes Can Differ

### Separate derivative branches

JPMI, APFS, and GAI are not three synchronized images of one filesystem. They represent separate custody and acquisition branches. A shared origin does not guarantee identical allocation, path selection, filesystem state, or later handling.

### Volatile system state

Caches, CloudKit records, database journals, WAL/SHM files, Photos proxies, and application support files can be created, removed, compacted, or rewritten between acquisitions. A small metadata or database change creates a wholly different SHA-256.

### Photos Library generation

Photos libraries intentionally contain many generated representations of the same visual asset. Proxy dimensions, rendering settings, cache keys, directory placement, and generated sidecars can differ across copies. A path or filename resemblance therefore does not imply byte identity.

### GAI coverage limitation

The GAI image is a truncated HFS+ volume and has a bounded forensic coverage region. Absence from its inventory cannot establish absence from the complete originating device.

### APFS is a derivative, not the original internal NVMe

The APFS source is a SanDisk external image and is not a direct image of the MacBook internal SSD. Its contents and filesystem state reflect the particular derivative delivered for examination.

### Acquisition and handling differences

The inventories were produced at different times and through different tools. Recovery exports, metadata-only lists, allocated-file walks, and derivative extraction databases do not describe identical object populations.

### Metadata-only JPMI coverage

JPMI contains metadata/hash records for material whose corresponding bytes are not available in this project. A JPMI hash can therefore be confidently recorded as an observed inventory object while remaining unavailable for byte-level re-verification or copying.

## Interpretation Of Path And Fuzzy Candidates

The 626 exact normalized-path candidates are the strongest non-hash leads, particularly where size also agrees. They may represent:

- a changed or rewritten object at the same logical path
- an inventory or path-normalization difference
- a stale or regenerated cache object

The 1,095 exact-filename candidates are weaker because names such as `pcs.db-shm`, `ChunkStoreDatabase-wal`, and generic Photos derivative names recur across applications and directories.

The 6,799 fuzzy candidates are investigative leads only. Initial samples show near-identical Photos derivative names whose hash and size differ. They should be ranked using full path similarity, extension, size, Photos derivative family, and directory context before any provenance conclusion is drawn.

## Limitations And Corrections

1. The unmatched baseline used direct source IDs `1` and `116`; the path scan searched readable APFS and GAI descendant source families. A final production statistic should use one consistent source-family definition.
2. The category exploration used for this report should be regenerated into a durable mutually exclusive TSV before category byte totals are cited in a formal report.
3. Filename and fuzzy candidates are not confirmed matches without byte-level or stronger provenance evidence.
4. JPMI is metadata-only for this project; its unmatched hashes cannot be copied or independently rehashed here.
5. The incorrectly cataloged APFS raw image is unrelated to this discrepancy and was excluded from the SHA-256 blob staging manifest.

## Recommended Follow-Up

1. Recompute the unmatched population using direct roots plus all formally linked descendants for both APFS and GAI.
2. Export a corrected mutually exclusive classification table with path, extension, size, and source metadata.
3. Promote exact path plus equal-size candidates for manual review first.
4. Rank fuzzy candidates only within the same extension, size band, application/container family, and normalized parent path.
5. Separate Photos derivatives, system/cache artifacts, and likely user-content candidates in the final review.
6. Do not describe an unmatched JPMI hash as a missing original file unless its path, object type, timestamps, and derivative lineage support that conclusion.
