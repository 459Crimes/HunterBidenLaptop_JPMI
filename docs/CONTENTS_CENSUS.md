# Contents census

> **Hatnote.** Populations on the JPMI copy. Path counts are **not** unique-document counts. Companion: [What is on the copy](04_what_is_on_the_copy.md). Generated OS/environment rollup: [`02_os_version.md`](../build/reports/02_os_version.md).

## Top-level inventory

From [`02_top_level_summary.tsv`](../build/file_tree/02_top_level_summary.tsv):

| Area | File rows | Represented bytes | SHA-256 coverage |
|---|---:|---:|---:|
| `Users` | 572,743 | 215.5 GB | 331,906 paths (58%) |
| HFS+ data-partition structures | 3,435 | 283.0 GB | 0% (includes unallocated representations) |
| EFI System Partition | 6 | 209.7 MB | 0% |
| GPT / unpartitioned | 7 | 134.3 MB | 0% |

Do **not** add 215 GB + 283 GB and call it “Hunter’s unique files.” The structural byte total includes filesystem objects and unallocated-range accounting.

User-tree `max_modified_ts` in that rollup is **2020-10-15 21:20:53** — the Finder cluster, not a 2022 authorship date. Structural partition `max_modified_ts` runs to **2024-11-21**.

## Home directory (`Users/roberthunter`)

| Directory | Rows | Bytes | Notes |
|---|---:|---:|---|
| Library | 251,863 | 54.8 GB | Mail, Contacts, app state; mtimes into 2020-01-01 `.DS_Store` |
| Documents | 119,794 | 23.2 GB | Includes large **Dr.Fone** recovery trees |
| Pictures | 92,393 | 61.0 GB | Originals + Photos derivatives; one `.DS_Store` mtime 2019-05-10 |
| Movies | 61,202 | 9.4 GB | |
| Downloads | 23,415 | 19.8 GB | Last mtime in rollup 2019-03-18 (pre-repair) |
| Music | 19,313 | 32.2 GB | **0** hash_count in home overview — coverage gap, not “no files” |
| Desktop | 4,654 | 15.1 GB | `.DS_Store` 2020-10-15 |
| Public | 4 | 6,148 | `.DS_Store` 2020-10-15 |
| messages / voice memo | small | — | |
| Wondershare | 6 | — | Recovery-tool vendor crumbs |
| `F22DECB2-…pvt` | 2 | 5.3 MB | Packed blob at home level |

## System-area rollup (different cutter)

[`03_volume_system_state.tsv`](../build/volume_info/03_volume_system_state.tsv) uses **category** rules, so numbers will not match home-folder rows 1:1:

| Area | Object count | Notes |
|---|---:|---|
| mail | 139,113 | Mail + `.emlx` under Library |
| drfone_tooling | 116,889 | Wondershare Dr.Fone support — **tooling**, not “native Mail” |
| photos | 92,356 | |
| home_library (remainder) | 96,486 | |
| icloud_cloudkit | 27,833 | Placeholders and cloud state |
| movies | 61,202 | |
| music | 19,284 | 0 hashes in this rollup too |
| spotlight | 90 | ~453 MB indexes |
| chrome | 3,842 | |
| 090_diagnostics | 1,782 | Desktop wireless/system diagnostics |
| hfs_journal | 2 | ~40 MB |
| document_revisions | 11 | |

Characterization report additionally: **~128,847 `.emlx` paths**, **~77,891 `.vcf` paths**, **~12,911 iCloud-related paths**. Extension TSV splits `.emlx` vs `.emlx-slack` and will look “smaller” if you only sum the unsuffixed `.emlx` line (15,487) — that is a **different census**. Always name the table.

## Identity math

| Universe | Count | Meaning |
|---|---:|---|
| Normalized paths | 576,249 | Inventory locations |
| CNIDs | 397,440 | Catalog objects |
| Canonical hashed CNIDs | 332,097 | Files with SHA-256 in CNID hash export |
| Alias-map rows | 655,330 | Path↔CNID including aliases |
| Distinct SHA-256 | 180,046 | Distinct **reported** contents |
| TSK events | 1,259,300 | Timeline events, not files |

**180k distinct hashes vs 332k hashed files** is duplicate content (copies, attachments, derivatives), not a contradiction.

## Mobile / cloud / migration

Dr.Fone trees named like `Hunter's iPad 10-30-2018…` show **device-recovery tooling** inside Documents. iCloud `.icloud` placeholders show cloud-backed names without local bytes. WirelessDiagnostics / `roberts-MacBook-Air` / serial `C02S953UH3QF` show **older Mac diagnostic packages** in the account ([device report](../build/reports/01_computer_information.md): 33 / 1,090 / 1,298 path rows respectively). None of those, alone, serializes the 2019 drop-off chassis.

## What this GitHub tree cannot show you

It cannot open the JPEG. It can tell you the path, size, timestamps, CNID, and **reported** SHA-256. That is still enough to ask provenance questions correctly. See [Limits](07_limits_and_open_questions.md).

## See also

- [Glossary](GLOSSARY.md) (slack, alias, path)
- [Data contract](../DATA_CONTRACT.md)
