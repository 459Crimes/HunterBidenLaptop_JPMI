# JPMI Coverage, Method, and Limits

## 1. Source boundary

This repository publishes a **metadata and hash witness for JPMI**, the John Paul Mac Isaac copy lineage.

The restricted JPMI E01 image is not published or independently mounted by this GitHub checkout. The project therefore works from received forensic reports/manifests normalized into JPMI-specific database tables and derived public artifacts.

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

## 3. Hash method

The public hash export is JPMI-only.

`build/hash_manifest/01_sha256_by_cnid_*.tsv` records canonical HFS+ catalog identities together with reported SHA-256 values and paths.

The public coverage table records JPMI's own hash population. This repository does not require another evidence corpus to characterize JPMI.

### Important limitation

A SHA-256 value in this repository is a **reported JPMI-manifest value** unless the repository explicitly states that the hash was recomputed from source bytes.

Because the restricted E01 is not mounted here, the correct wording is:

> “The JPMI forensic manifest reports SHA-256 X for this represented object.”

That is different from claiming that the current GitHub checkout independently read the source object and calculated the value itself.

## 4. Reproducibility method

The pipeline performs read-only PostgreSQL queries and writes derived artifacts under `build/`.

Stages:

1. file-tree export;
2. JPMI-only hash identity export;
3. metadata distributions;
4. disk/partition/volume identity export;
5. standalone JPMI reports;
6. deep metadata archives;
7. size/checksum validation.

The pipeline uses JPMI evidence only for this repository's public analysis.

## 5. Size policy

The configured publication limits are:

- per-file budget: **52,428,800 bytes (50 MiB)**;
- hard cap: **94,371,840 bytes (90 MiB)**.

Large exports are sharded at row boundaries. Deep metadata sets are archived into partitioned parts so that the repository can preserve detailed evidence without exceeding GitHub's practical file-size limits.

## 6. Copy-method boundary

The structure supports describing JPMI to the public as a **whole-volume or filesystem-preserving, `dd`-style copy lineage**.

That phrase does not prove:

- that John Paul Mac Isaac literally used `dd`;
- that the final Crucial X6 was cloned directly from the original internal SSD in one operation;
- that no intermediate server, image, restore, or filesystem-aware copy step existed.

The exact original copy utility and intermediate custody steps remain open provenance questions.

## 7. Timestamp and acquisition boundary

The represented HFS+ destination reports creation on September 26, 2019 and contains later system-state timestamps in 2020, 2022, and 2024.

The acquisition record separately identifies `HB-IMAGE-2022-04-29.E01` and reports April 29, 2022. The delivered volume metadata reports a November 21, 2024 last-write.

An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write. The repository therefore treats that pair as an **unresolved source-chronology discrepancy**. It does not claim the 2022 E01 itself was modified in 2024.

The later timestamps also do not automatically transform older user content into post-2019 content, nor do Spotlight/Finder timestamps automatically prove substantive document insertion.

## 8. Historical hardware boundary

Older WirelessDiagnostics packages inside the `roberthunter` data tree reference a MacBook Air and older serial-bearing captures.

Those artifacts establish that historical Mac data exists in the copied account. They should not automatically be used to identify the particular 2019 repair-shop machine because user data can migrate across Apple hardware.

## 9. Core conclusion

JPMI can be characterized from its own internal forensic witness:

> It is a later GPT/HFS+ Mac custody-volume lineage containing a broad `roberthunter` user/application environment, represented by a forensic acquisition record and carrying older user data plus later filesystem/system-state metadata.

The strongest remaining provenance gaps are the undocumented intermediate step between the original repair-shop storage and the later HFS+ custody medium, and the unresolved relationship between the reported 2022 acquisition and 2024 last-write.
