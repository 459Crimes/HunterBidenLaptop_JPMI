# Forensic image HB-IMAGE-2022-04-29.E01

> **Hatnote.** Wrapper around the later custody disk. This GitHub repository **does not contain** the E01. It contains the **acquisition identity** and derived metadata. See [Source-byte boundary](07_limits_and_open_questions.md).

## Identity block

| Field | Value |
|---|---|
| Image name | `HB-IMAGE-2022-04-29.E01` |
| Format | E01 |
| Tool | ADI4.7.1.2 |
| Case | `HB-2022-04-29` |
| `reported_at` | 2022-04-29 |
| Image size | 500,107,862,016 bytes |
| MD5 | `682619c1884e6fe006664ba31deed698` |
| SHA-1 | `fe918f0cff3304ab52875b984c88fee78ec05197` |
| Manifest source | `rank2-uuid-manifest.txt` |
| Notes | `hb-reports-3 rank2 manifest from Todd Sanders (TSK 4.14.0)` |
| DB `created_at` | 2026-07-22 19:35:50 — **project ingest**, not imaging day |

Source: [`build/disk_info/01_acquisition.tsv`](../build/disk_info/01_acquisition.tsv).

## What E01 means here

An E01 is a forensic **container**. Two points clarify its role:

1. If the E01 is **immutable and actually acquired on 2022-04-29**, it cannot later grow a 2024 HFS+ last-write **inside itself**. A 2024 write implies another working copy, a later acquisition, mixed reports, or a mislabeled field — see [2022/2024](2022_2024_DISCREPANCY.md).
2. Image MD5/SHA-1 authenticate **this named image file as recorded**, not every historical ancestor copy back to April 2019.

## Hashes: three layers

| Layer | Algorithm | What it fingerprints | In this repo? |
|---|---|---|---|
| Image | MD5, SHA-1 | The E01 acquisition as recorded | Yes (acquisition table) |
| Object | SHA-256 | File/catalog content per received manifests | Yes, as **manifest evidence** (655,330 hashed paths; 180,046 distinct SHA-256) |
| Recomputed object | SHA-256 | Fresh hash from restricted source bytes in *this* checkout | **No** — source bytes unpublished |

The accurate statement: “The JPMI manifest reports this SHA-256,” not “this GitHub clone hashed the E01 file contents.”

## Coverage numbers

From [`build/reports/05_coverage_and_method.md`](../build/reports/05_coverage_and_method.md):

| Metric | Value |
|---|---:|
| Normalized inventory paths | 576,249 |
| Rank-1 hash-manifest paths | 655,330 |
| Distinct SHA-256 | 180,046 |
| CNID-map rows | 397,440 |
| Alias-map rows | 655,330 |
| TSK timeline rows | 1,259,300 |

These are different universes and are not summed as if they were one file count.

## Tooling named in notes

**TSK 4.14.0** (The Sleuth Kit) appears in the Sanders rank-2 note — a **report-generation** attribution. **ADI4.7.1.2** is the recorded **imager**. Neither is the April 2019 repair-shop copy utility.

## Missing worksheets

The complete acquisition worksheet package for `HB-IMAGE-2022-04-29.E01` is listed as highest-value missing evidence ([Limits](07_limits_and_open_questions.md)).

## See also

- [Reproducibility](08_reproducibility.md)
- [GitHub size policy](../GITHUB_SIZE_POLICY.md)
