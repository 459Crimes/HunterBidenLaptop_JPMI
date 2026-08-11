# Known Datetime Stamps Of Use

**Status: DRAFT for investigator review.**

## 1. Reported volume timestamps

- HFS+ volume creation (reported): **2019-09-26 22:59:02 CDT**
- HFS+ volume last write (reported): **2024-11-21 17:40:22 CST**
- E01 acquisition (reported): **2022-04-29** (`HB-IMAGE-2022-04-29.E01`)
- Deleted-file catalog report: **empty** (HFS+ normal; 3-way verified)

## 2. File timestamp distribution by year

Rows are inventory paths (`files` source 122 joined to `jpmi_file_times`). The column is `timestamp without time zone`; no conversion is applied. Observed alignment: the reported last-write `2024-11-21 17:40:22 CST` equals the stored maximum `2024-11-21 23:40:22` (i.e. stored values align with UTC), while the volume-creation artifacts store `2019-09-27 01:59:02` ≈ `2019-09-26 20:59:02 CDT` — two hours earlier than the reported `22:59:02 CDT`. Treat sub-minute/2-hour zone differences as ingestion caveats.


| Year | created | modified | accessed |
|---|---|---|---|
| 1984 | 1 | 0 | 0 |
| 2007 | 1 | 0 | 0 |
| 2012 | 16 | 0 | 0 |
| 2013 | 15 | 0 | 0 |
| 2014 | 32 | 12 | 0 |
| 2015 | 353 | 317 | 0 |
| 2016 | 3647 | 2101 | 0 |
| 2017 | 107817 | 106873 | 0 |
| 2018 | 107185 | 102657 | 0 |
| 2019 | 353677 | 360756 | 8130 |
| 2020 | 14 | 18 | 221 |
| 2022 | 82 | 82 | 564453 |
| 2024 | 7 | 30 | 30 |


## 3. Accessed-time clusters (handling/examination windows)


| Year-month | Rows |
|---|---|
| 2022-03 | 532375 |
| 2022-04 | 31942 |
| 2019-09 | 8130 |
| 2020-10 | 221 |
| 2022-06 | 136 |
| 2024-11 | 30 |


## 4. Notable known events

- **2016-11-20 / 2016-11-22** — wireless diagnostics captures (`WirelessDiagnostics_C02S953UH3QF_*`, `Desktop/090-[]/` CoreCapture logs) — originating-Mac activity.
- **2019-01 to 2019-03 — large modified-time cluster** (~360,700 inventory rows last modified in Jan–Mar 2019; February alone ~241,000 rows). This dominates the `modified` distribution and is distinct from the volume creation date below. It is the strongest single indicator of the original user-activity window in this inventory.
- **2019-09-26** — HFS+ volume creation window; `/.journal`, `/.journal_info_block`, and Spotlight `VolumeConfig.plist` timestamps align to this window.
- **2020-10-15** — Desktop `.DS_Store` modified one day after the New York Post story; consistent with later mounting/browsing.
- **2022-03 / 2022-04** — the dominant accessed-time cluster (532,375 + 31,942 rows) is consistent with the 2022-04-29 E01 acquisition and its 2022-03-31 examination window.
- **2024-11-21** — reported last-write; Spotlight/index structures cluster at this time.

## 5. Caveats

- A filesystem last-write time identifies metadata activity, not necessarily substantive user activity.
- Accessed times largely reflect the examiner/acquisition pass rather than original use.

