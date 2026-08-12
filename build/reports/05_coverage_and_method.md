# JPMI Coverage, Method, and Limits

## Coverage

| Metric | Value |
|---|---|
| Normalized JPMI inventory paths | 576,249 |
| Rank-1 JPMI hash-manifest paths | 655,330 |
| Hash-manifest paths with SHA-256 | 655,330 |
| Distinct reported SHA-256 values | 180,046 |
| CNID-map rows | 397,440 |
| Alias-map rows | 655,330 |
| TSK timeline rows | 1,259,300 |

## Method

The pipeline performs read-only queries against JPMI tables, writes derived public artifacts under `build/`, shards large exports under the configured file-size budget, and validates section manifests and checksums. This standalone repository intentionally does not generate comparison tables.

## Source boundary

The GitHub project publishes received JPMI metadata/hash evidence and derived reports. The restricted E01 image itself is not published here. Therefore a reported manifest hash is distinguished from a hash freshly recomputed by this checkout from restricted source bytes.

## Copy-method boundary

The evidence supports describing JPMI as a whole-volume/filesystem-preserving copy lineage for public explanation. It does not establish the literal original repair-shop copy command or every intermediate storage device.

## Acquisition chronology boundary

The acquisition record reports `HB-IMAGE-2022-04-29.E01` with date `2022-04-29`, while delivered HFS+ metadata reports a 2024 last-write. An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write. The relationship between those records is unresolved and requires the original acquisition/report lineage.

## Size policy

Per-file budget: 52,428,800 bytes. Hard cap: 94,371,840 bytes.
