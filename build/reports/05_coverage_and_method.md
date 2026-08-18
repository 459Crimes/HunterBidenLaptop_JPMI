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

These figures are derived from the JPMI forensic reports published in this repository. Large tables are split into shards. Checksums are in `build/manifest.tsv`. This standalone publication does not include comparison tables against other laptop-data corpora. See [How to verify](../../docs/08_reproducibility.md) and the [evidence catalog](../../docs/catalog/README.md).

## Source boundary

The GitHub project publishes received JPMI metadata/hash evidence and derived reports. The restricted E01 image itself is not published here. Therefore a reported manifest hash is distinguished from a hash freshly recomputed by this checkout from restricted source bytes.

## Copy-method boundary

Volume `Untitled` was formatted 26 September 2019 and populated by a timestamp-preserving file-aware copy of `roberthunter`. A later volume clone put that filesystem onto the Crucial X6 (a 2020+ product). The E01 is a forensic image of that X6. The April 2019 store-server utility remains unnamed. See docs/COPY_METHOD.md.

## Acquisition chronology boundary

The acquisition record reports `HB-IMAGE-2022-04-29.E01` with date `2022-04-29`, while delivered HFS+ metadata reports a 2024 last-write. An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write. The relationship between those records is unresolved and requires the original acquisition/report lineage.

## Size policy

Published files in this tree are kept under 50 MiB so they can be hosted on GitHub without Git LFS.
