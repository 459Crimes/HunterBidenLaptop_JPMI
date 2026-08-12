# Post-Repair Custody Activity

Boundary used for the technical slice: `modified_ts > 2019-03-31 23:59:59`.

**141 inventory rows** fall after that boundary.

## Summary by year

| Year | Rows |
|---|---|
| 2019 | 11 |
| 2020 | 18 |
| 2022 | 82 |
| 2024 | 30 |

## Interpretation

The later population is dominated by filesystem and application metadata such as `.DS_Store`, Spotlight, DocumentRevisions, directories, and temporary/system state. It establishes that the represented copy lineage contains later system-state activity; it does not, by itself, prove wholesale insertion of substantive user documents or identify which physical/image stage produced every later timestamp. In particular, the 2024 rows must be reconciled with the separately reported 2022 E01 acquisition.

## Complete modified-row set

| Path | Size | Created | Modified | Accessed |
|---|---|---|---|---|
| jpmi_metadata/Users/roberthunter/Desktop/New Folder With Items/.DS_Store | 6148 | 2019-02-06 11:35:52 | 2019-05-10 16:14:25 | 2022-03-31 16:49:36 |
| jpmi_metadata/Users/roberthunter/Pictures/.DS_Store | 10244 | 2018-11-11 08:36:50 | 2019-05-10 16:15:53 | 2022-03-31 17:44:29 |
| jpmi_metadata/Users/roberthunter/Library/Mail |  | 2018-10-21 12:52:31 | 2019-09-13 16:41:10 | 2022-04-12 03:23:54 |
| jpmi_metadata/Users/roberthunter/Library/Mail/V6 |  | 2018-10-22 11:38:52 | 2019-09-27 01:56:35 | 2022-04-12 03:23:54 |
| jpmi_metadata/Users/roberthunter/Library/Mail/V6/.DS_Store | 10244 | 2019-09-27 01:56:35 | 2019-09-27 01:56:41 | 2022-03-31 18:20:23 |
| jpmi_metadata/Users/roberthunter/Library/Mail/.DS_Store | 6148 | 2019-09-13 16:41:10 | 2019-09-27 01:56:47 | 2022-03-31 18:20:25 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.journal_info_block | 4096 | 2019-09-27 01:59:02 | 2019-09-27 01:59:02 |  |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.journal | 41943040 | 2019-09-27 01:59:03 | 2019-09-27 01:59:03 |  |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V1/ |  | 2019-09-27 01:59:04 | 2019-09-27 01:59:04 | 2019-09-27 04:50:49 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V1/VolumeConfig.plist | 348 | 2019-09-27 01:59:04 | 2019-09-27 01:59:04 | 2019-09-27 15:02:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/ |  | 2019-09-27 01:59:04 | 2019-09-27 01:59:04 | 2019-09-27 04:50:49 |
| jpmi_metadata/Users/roberthunter/Library |  | 2017-06-23 21:24:35 | 2020-01-01 00:04:25 | 2022-04-28 16:09:32 |
| jpmi_metadata/Users/roberthunter |  | 2018-10-21 12:52:26 | 2020-01-01 00:04:25 | 2022-06-01 02:35:36 |
| jpmi_metadata/Users/roberthunter/.DS_Store | 22532 | 2018-10-21 12:55:05 | 2020-01-01 00:04:30 | 2022-06-01 02:35:36 |
| jpmi_metadata/Users/roberthunter/Library/.DS_Store | 18436 | 2018-10-22 22:06:36 | 2020-01-01 00:04:30 | 2022-04-28 16:09:32 |
| jpmi_metadata/Users/roberthunter/Documents/dr.fone/dr.fone-Recover/Hunter's iPad 10-30-2018 at 06.43.46/.DS_Store | 6148 | 2018-10-30 21:09:49 | 2020-10-15 21:16:11 | 2022-03-31 16:56:38 |
| jpmi_metadata/Users/roberthunter/Documents/dr.fone/dr.fone-Recover/.DS_Store | 16388 | 2018-10-30 10:33:09 | 2020-10-15 21:16:11 | 2022-04-28 16:09:12 |
| jpmi_metadata/Users/roberthunter/Documents/dr.fone/dr.fone-Recover/Hunter's iPad 10-30-2018 at 06.33.03 |  | 2018-10-30 10:33:06 | 2020-10-15 21:16:20 | 2022-04-28 16:09:13 |
| jpmi_metadata/Users/roberthunter/Documents/dr.fone/dr.fone-Recover/Hunter's iPad 10-30-2018 at 06.33.03/.DS_Store | 6148 | 2020-10-15 21:16:20 | 2020-10-15 21:16:20 | 2022-03-31 16:56:29 |
| jpmi_metadata/Users/roberthunter/Desktop/.DS_Store | 45060 | 2018-10-21 14:00:50 | 2020-10-15 21:18:17 | 2022-04-28 16:09:08 |
| jpmi_metadata/Users/roberthunter/Public/.DS_Store | 6148 | 2019-01-07 10:32:42 | 2020-10-15 21:18:42 | 2022-03-31 18:08:34 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/.cs/ |  | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/purgatory/ |  | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/db-V1/ |  | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.TemporaryItems/folders.0/ |  | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 | 2020-10-26 13:43:17 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/staging/ |  | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.TemporaryItems/ |  | 2020-10-15 21:19:22 | 2020-10-15 21:19:22 | 2020-10-26 13:43:17 |
| jpmi_metadata/Users/roberthunter/Documents/.DS_Store | 14340 | 2018-10-22 12:12:05 | 2020-10-15 21:20:53 | 2022-04-28 16:09:12 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.com.apple.timemachine.donotpresent |  | 2020-10-26 13:18:59 | 2020-10-26 13:18:59 | 2020-10-26 13:18:59 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/ |  | 2019-09-27 01:59:02 | 2022-03-31 16:48:20 | 2022-06-01 02:41:45 |
| jpmi_metadata/598 |  | 2017-11-05 11:06:24 | 2022-03-31 16:51:15 |  |
| jpmi_metadata/239 |  | 2017-11-12 09:35:39 | 2022-03-31 16:54:28 |  |
| jpmi_metadata/602 |  | 2017-11-12 09:35:41 | 2022-03-31 16:54:28 |  |
| jpmi_metadata/207 |  | 2017-06-01 00:29:44 | 2022-03-31 16:54:32 |  |
| jpmi_metadata/278 |  | 2017-06-01 00:29:44 | 2022-03-31 16:54:32 |  |
| jpmi_metadata/406 |  | 2017-06-01 00:29:44 | 2022-03-31 16:54:32 |  |
| jpmi_metadata/607 |  | 2017-06-05 03:08:26 | 2022-03-31 16:55:17 |  |
| jpmi_metadata/342 |  | 2017-11-25 17:12:41 | 2022-03-31 16:56:02 |  |
| jpmi_metadata/279 |  | 2015-10-02 17:33:30 | 2022-03-31 17:00:23 |  |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DS_Store | 8196 | 2019-09-27 02:04:14 | 2022-03-31 17:47:13 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Trashes/ |  | 2019-09-27 01:59:04 | 2022-03-31 18:21:15 | 2019-09-27 04:50:55 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.assisted_import_pre/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.live_user/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cab.created |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Lion.created |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/store_generation | 4 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/tmp.Cab |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.migration_secondchance/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.live_priority/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.corespotlight/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.migration/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.live/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.assisted_import_post/ |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/VolumeConfiguration.plist | 4009 | 2019-09-27 01:59:04 | 2022-04-11 22:34:01 | 2019-09-27 15:02:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journalExclusion |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/tmp.SnowLeopard |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/tmp.Lion |  | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/metadata | 303 | 2022-04-11 22:34:02 | 2022-04-11 22:34:02 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/ |  | 2019-09-27 01:59:04 | 2022-04-11 22:35:32 | 2019-09-27 04:50:49 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0000/ |  | 2022-04-11 22:42:32 | 2022-04-11 22:42:32 | 2022-04-11 22:42:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/ |  | 2022-04-11 22:42:32 | 2022-04-11 22:42:32 | 2022-04-11 22:42:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/ |  | 2022-04-11 22:42:32 | 2022-04-11 22:42:32 | 2022-04-11 22:42:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0001/ |  | 2022-04-11 22:47:10 | 2022-04-11 22:47:10 | 2022-04-11 22:47:10 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0002/ |  | 2022-04-11 22:52:19 | 2022-04-11 22:52:19 | 2022-04-11 22:52:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0003/ |  | 2022-04-11 22:57:33 | 2022-04-11 22:57:33 | 2022-04-11 22:57:33 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0004/ |  | 2022-04-11 22:57:55 | 2022-04-11 22:57:55 | 2022-04-11 22:57:55 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0005/ |  | 2022-04-11 22:59:18 | 2022-04-11 22:59:18 | 2022-04-11 22:59:18 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0006/ |  | 2022-04-11 23:00:43 | 2022-04-11 23:00:43 | 2022-04-11 23:00:43 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0007/ |  | 2022-04-11 23:01:06 | 2022-04-11 23:01:06 | 2022-04-11 23:01:06 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/0008/ |  | 2022-04-11 23:01:07 | 2022-04-11 23:01:07 | 2022-04-11 23:01:07 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cache/0000/0000/ |  | 2022-04-11 22:42:32 | 2022-04-11 23:01:07 | 2022-04-11 22:42:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexGroups | 419431 | 2022-04-11 22:34:01 | 2022-04-11 23:02:29 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.scan/retire.363296 |  | 2022-04-11 23:02:29 | 2022-04-11 23:02:29 | 2022-04-11 23:02:29 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.scan/ |  | 2022-04-11 22:34:01 | 2022-04-11 23:02:30 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/reverseDirectoryStore.shadow | 1703936 | 2022-04-11 22:34:19 | 2022-04-11 23:02:31 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexBigDates | 1453176 | 2022-04-11 22:34:01 | 2022-04-11 23:02:31 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexCompactDirectory | 17896374 | 2022-04-11 23:02:31 | 2022-04-11 23:02:42 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexPostings | 64252934 | 2022-04-11 23:02:31 | 2022-04-11 23:02:42 | 2022-06-01 04:01:22 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexIds | 2906352 | 2022-04-11 22:34:01 | 2022-04-11 23:02:42 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexArrays | 109908608 | 2022-04-11 23:02:31 | 2022-04-11 23:02:42 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexDirectory | 3483892 | 2022-04-11 23:02:31 | 2022-04-11 23:02:42 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexPositions | 185523358 | 2022-04-11 23:02:31 | 2022-04-11 23:02:42 | 2022-04-11 23:02:42 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.directoryStoreFile.shadow | 1310720 | 2022-04-11 23:02:43 | 2022-04-11 23:02:43 | 2022-04-11 23:02:43 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.repair/ |  | 2022-04-28 16:08:27 | 2022-04-28 16:08:27 | 2022-04-28 16:08:27 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/Cab.modified |  | 2022-04-28 16:08:27 | 2022-04-28 16:08:27 | 2022-04-28 16:08:27 |
| jpmi_metadata/0 |  | 2019-01-30 07:40:05 | 2022-04-28 16:09:27 |  |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.health_check/ |  | 2022-04-11 22:34:01 | 2022-06-01 02:44:09 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/tmp.spotlight.loc | 239971 | 2022-04-11 22:34:19 | 2022-06-01 02:48:32 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexUpdates |  | 2022-06-01 03:39:43 | 2022-06-01 03:39:43 | 2022-06-01 03:39:43 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexCompactDirectory | 1748 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexDirectory | 10280 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexGroups | 17645 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journals.live_system/ |  | 2022-04-11 22:34:01 | 2022-06-01 03:39:43 | 2022-04-11 22:34:01 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.directoryStoreFile.shadow | 56640 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/store.updates | 3 | 2022-06-01 03:39:43 | 2022-06-01 03:39:43 | 2022-06-01 03:39:43 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexHead | 4096 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexArrays | 4194304 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/indexState | 28 | 2022-04-11 22:34:01 | 2022-06-01 03:39:43 | 2022-06-01 02:35:33 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexPositionTable | 1205648 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.shadowIndexHead | 4096 | 2022-04-11 23:02:42 | 2022-06-01 03:39:43 | 2022-04-11 23:02:42 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.shadowIndexTermIds | 1205648 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/reverseStore.updates | 1 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/store.db | 20516864 | 2022-04-11 22:34:01 | 2022-06-01 03:39:43 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.shadowIndexGroups | 290636 | 2022-04-11 22:34:19 | 2022-06-01 03:39:43 | 2022-04-11 22:34:19 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.indexHead | 4096 | 2022-04-11 23:02:42 | 2022-06-01 03:39:43 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.fseventsd/ffffffffd0400b32 | 74 | 2022-06-01 08:05:02 | 2022-06-01 08:05:02 | 2022-06-01 08:05:02 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.fseventsd/ |  | 2019-09-27 01:59:04 | 2022-06-01 08:05:02 | 2022-06-01 02:35:32 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/db-V1/db.sqlite | 77824 | 2020-10-15 21:19:22 | 2022-06-01 08:05:02 | 2022-06-01 02:38:40 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/shutdown_time | 4 | 2022-04-11 22:34:18 | 2022-06-01 08:05:02 | 2022-04-11 22:34:18 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.fseventsd/ffffffffd0400b31 | 234 | 2022-06-01 08:05:02 | 2022-06-01 08:05:02 | 2022-06-01 08:05:02 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.fseventsd/fseventsd-uuid | 36 | 2022-06-01 02:35:32 | 2022-06-01 08:05:02 | 2022-06-01 08:05:02 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.directoryStoreFile | 2097152 | 2022-04-11 23:02:31 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexCompactDirectory | 2048 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexPostings | 2097152 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2022-06-01 04:01:22 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/dbStr-6.map.header | 84 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexTermIds | 2097152 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.directoryStoreFile | 65536 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexGroups | 26215 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/.store.db | 20516864 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexBigDates | 131072 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexIds | 262144 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/dbStr-6.map.offsets | 16368 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexPositionTable | 2097152 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/dbStr-6.map.buckets |  | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexArrays | 4194304 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexPositions | 1048576 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2022-06-01 03:39:43 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexDirectory | 16448 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/reverseDirectoryStore | 2097152 | 2022-04-11 22:34:01 | 2024-11-21 23:40:20 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/.cs/ChunkStoreDatabase | 98304 | 2020-10-15 21:19:22 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.ivf-vector-indexes | 8 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/ |  | 2020-10-15 21:19:22 | 2024-11-21 23:40:21 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/.cs/ChunkStoreDatabase-wal | 20632 | 2020-10-15 21:19:22 | 2024-11-21 23:40:21 | 2020-10-15 21:40:26 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/db-V1/db.sqlite-wal | 32 | 2020-10-15 21:19:22 | 2024-11-21 23:40:21 | 2022-06-01 08:05:02 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/permStore | 118630 | 2022-04-12 03:24:02 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.DocumentRevisions-V100/LibraryStatus | 234 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/0.ivf-vector-indexes | 8 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 | 2024-11-21 23:40:21 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.TemporaryItems/folders.0/TemporaryItems/ |  | 2020-10-15 21:19:22 | 2024-11-21 23:40:21 | 2020-10-26 13:43:17 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/live.0.indexHead | 4096 | 2022-04-11 22:34:01 | 2024-11-21 23:40:22 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/journalAttr.5 |  | 2024-11-21 23:40:22 | 2024-11-21 23:40:22 | 2024-11-21 23:40:22 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/tmp.spotlight.state | 4096 | 2022-04-11 22:34:01 | 2024-11-21 23:40:22 | 2024-11-21 23:40:20 |
| jpmi_metadata/Basic data partition (2)/Untitled [HFS+]/Untitled/.Spotlight-V100/Store-V2/3DEE7E1E-F78C-4768-B492-D2485F7ADCBA/ |  | 2019-09-27 01:59:05 | 2024-11-21 23:40:22 | 2024-11-21 23:40:21 |

## Limitation

A filesystem timestamp does not identify the human or process responsible for the event. Attribution requires object type, surrounding activity, logs, custody records, and a reconciled source chronology.
