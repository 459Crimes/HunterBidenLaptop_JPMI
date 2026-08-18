# Timeline (index)

> **Hatnote.** Compact event index. The **canonical sourced narrative** (court + participant + JPMI timestamps interleaved) remains [Timeline and handling](06_timeline_and_handling.md), republished to `build/reports/03_known_datetime_stamps_of_use.md`. Row-level post-repair mtimes: [04_post_2019_03_31_timeline.md](../build/reports/04_post_2019_03_31_timeline.md). Distributions: [01_time_distribution.tsv](../build/metadata/01_time_distribution.tsv).

## Layers of time

1. **User/application era** — years of `roberthunter` activity, heavily 2017–March 2019.
2. **Repair/recovery** — 12–13 April 2019.
3. **Destination volume creation** — 26 September 2019 HFS+ `Untitled`.
4. **Law-enforcement / preservation** — summer–December 2019.
5. **Public circulation** — August–October 2020.
6. **Forensic examination of copies** — especially March–June 2022 access clusters; April 2022 E01 name.
7. **Later report-lineage / mount activity** — November 2024 last-write (unreconciled with a 2022 immutable E01).
8. **Repository ingest** — `jpmi_acquisition.created_at` 22 July 2026 (recordkeeping, not a disk event).

## Index of dated events

| Date | Layer | Event | Article |
|---|---|---|---|
| 2010-03-02 | 2 | The Mac Shop, Inc. Delaware file 4794855 | [The Mac Shop](THE_MAC_SHOP.md) |
| Years ≤ 2018 | 1 | Account content, migrations, backups accumulate | [Contents census](CONTENTS_CENSUS.md) |
| 2019-01 … 2019-03 | 1 | Created/modified counts peak (e.g. Feb 2019: ~241k created rows) | [Timestamps](TIMESTAMPS.md) |
| 2019-04-12 | 2 | Three laptops; one retained | [The Mac Shop](THE_MAC_SHOP.md) |
| 2019-04-13 | 2 | External drive; recovery completed | [The Mac Shop](THE_MAC_SHOP.md) |
| 2019-04-17 | 2 | $85 invoice | [The Mac Shop](THE_MAC_SHOP.md) |
| 2019-05-10 | 5/2 | Two user-tree `.DS_Store` mtimes (Desktop subfolder; Pictures) — still metadata | [Integrity](INTEGRITY.md) |
| Late 2019-07 | 4 | FBI-related concern/contacts | [Chain of custody](03_chain_of_custody.md) |
| 2019-09-13 … 09-27 | 3 | Mail directory / `.DS_Store` around volume creation | [HFS+ volume](HFS_VOLUME_UNTITLED.md) |
| 2019-09-26 22:59:02 CDT | 3 | HFS+ `Untitled` created | [HFS+ volume](HFS_VOLUME_UNTITLED.md) |
| Sep–Oct 2019 | 4 | Father / Albuquerque copy effort (account) | [People](PEOPLE.md) |
| 2019-12-09 | 4 | FBI subpoena; exact copy retained | [Copy lineages](COPY_LINEAGES.md) |
| 2020-01-01 | 5 | Home / Library `.DS_Store` cluster | [Timestamps](TIMESTAMPS.md) |
| 2020-08-26 | 5 | Costello copy | [Copy lineages](COPY_LINEAGES.md) |
| 2020-10-13 | 5 | Mesires inquiry | [People](PEOPLE.md) |
| Oct 2020 | 5 | Apelbaum at Mac Isaac home; retained JPMI-lineage copy; later Fox/Tucker attempt | [Apelbaum, Fox, Tucker](APELBAUM_FOX.md) |
| 2020-10-20 | 5 | Marco Polo: Costello copy to New Castle County PD (not JPMI) | [Marco Polo v4](MARCO_POLO.md) |
| 2020-10-15 ~21:16–21:20 | 5 | Desktop/Documents/Public `.DS_Store`; DocumentRevisions dirs; TemporaryItems | [Integrity](INTEGRITY.md) |
| 2020-10-26 | 5 | `.com.apple.timemachine.donotpresent` | [HFS+ volume](HFS_VOLUME_UNTITLED.md) |
| 2022-03-31 … 2022-04-12 | 6 | Volume root, Spotlight Store-V2 build, huge **accessed** cluster (~532k rows in Mar 2022) | [Timestamps](TIMESTAMPS.md) |
| 2022-04-29 | 6 | E01 name / `reported_at` | [Forensic image](FORENSIC_IMAGE.md) |
| 2022-06-01 | 6 | fseventsd / further Spotlight live indexes | [HFS+ volume](HFS_VOLUME_UNTITLED.md) |
| 2022-11-21 | 6 | CBS publishes CFS results | [Integrity](INTEGRITY.md) |
| 2024-11-21 | 7 | Volume last-write / Spotlight+DocumentRevisions | [2022/2024 discrepancy](2022_2024_DISCREPANCY.md) |
| 2025-03-11 | 5 | Apelbaum–DeGiovanni call: JPMI copy to Fox/Tucker | [11 Mar 2025 call](APELBAUM_TUCKER_2025-03-11.md) |
| 2026-07-22 | 8 | Project DB acquisition-row `created_at` | [Forensic image](FORENSIC_IMAGE.md) |
| 2026-08-10 | 5 | Carlson interviews Hunter Biden; Israeli-source CSAM *allegation* | [Apelbaum, Fox, Tucker](APELBAUM_FOX.md) |

## Post-repair modified-row census

Technical slice `modified_ts > 2019-03-31 23:59:59`: **141 inventory rows**.

| Year | Rows |
|---|---:|
| 2019 | 11 |
| 2020 | 18 |
| 2022 | 82 |
| 2024 | 30 |

Interpretation: metadata/system-state dominance, not a new user-document corpus. Full paths in the generated report.

## See also

- [Timestamps](TIMESTAMPS.md)
- [Source matrix](09_source_matrix.md)
