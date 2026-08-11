# Computer Information And Specifications

**Status: DRAFT for investigator review.**

## 1. Custody device (the JPMI external medium)

The JPMI witness describes a GPT-partitioned external SSD. Its reported identity is recorded in the acquisition record (`jpmi_acquisition`) and is **not** the original laptop.

| Field | Value |
|---|---|
| Custody device model | Micron Crucial X6 SSD USB Device |
| Custody device serial | 2145E498755E |
| Custody device size (bytes) | 500107862016 |
| Acquisition image | HB-IMAGE-2022-04-29.E01 |
| Image format | E01 |
| Image MD5 | 682619c1884e6fe006664ba31deed698 |
| Image SHA-1 | fe918f0cff3304ab52875b984c88fee78ec05197 |
| Acquisition tool | ADI4.7.1.2 |
| Case number | HB-2022-04-29 |


## 2. Original computer — evidence inside the JPMI metadata

The JPMI metadata inventory is the `roberthunter` home directory plus GPT/EFI/HFS+ structural records. It contains diagnostics material that identifies the originating computer at the metadata level.

### Computer name

Crash and diagnostic-report filenames embed the host name `roberts-MacBook-Air` (33 rows in the inventory). Examples:


- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14 2.14/DiagnosticReports/callservicesd_2016-11-20-071251_roberts-MacBook-Air.cpu_resource.diag` (size 68649, modified 2016-11-20 12:12:51)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14 2.14/DiagnosticReports/com.apple.WebKit.Networking_2016-11-20-092956_roberts-MacBook-Air.crash` (size 81529, modified 2016-11-20 14:29:56)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14 2.14/DiagnosticReports/com.apple.WebKit.WebContent_2016-11-20-090240_roberts-MacBook-Air.cpu_resource.diag` (size 51872, modified 2016-11-20 14:02:40)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 2/DiagnosticReports/callservicesd_2016-11-20-071251_roberts-MacBook-Air.cpu_resource.diag` (size 68649, modified 2016-11-20 12:12:51)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 2/DiagnosticReports/com.apple.WebKit.Networking_2016-11-20-092956_roberts-MacBook-Air.crash` (size 81529, modified 2016-11-20 14:29:56)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 2/DiagnosticReports/com.apple.WebKit.WebContent_2016-11-20-090240_roberts-MacBook-Air.cpu_resource.diag` (size 51872, modified 2016-11-20 14:02:40)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3/DiagnosticReports/callservicesd_2016-11-20-071251_roberts-MacBook-Air.cpu_resource.diag` (size 68649, modified 2016-11-20 12:12:51)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3/DiagnosticReports/com.apple.WebKit.Networking_2016-11-20-092956_roberts-MacBook-Air.crash` (size 81529, modified 2016-11-20 14:29:56)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3/DiagnosticReports/com.apple.WebKit.WebContent_2016-11-20-090240_roberts-MacBook-Air.cpu_resource.diag` (size 51872, modified 2016-11-20 14:02:40)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14/DiagnosticReports/callservicesd_2016-11-20-071251_roberts-MacBook-Air.cpu_resource.diag` (size 68649, modified 2016-11-20 12:12:51)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14/DiagnosticReports/com.apple.WebKit.Networking_2016-11-20-092956_roberts-MacBook-Air.crash` (size 81529, modified 2016-11-20 14:29:56)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14/DiagnosticReports/com.apple.WebKit.WebContent_2016-11-20-090240_roberts-MacBook-Air.cpu_resource.diag` (size 51872, modified 2016-11-20 14:02:40)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-22_03.46.09/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3/DiagnosticReports/callservicesd_2016-11-20-071251_roberts-MacBook-Air.cpu_resource.diag` (size 68649, modified 2016-11-20 12:12:51)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-22_03.46.09/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3/DiagnosticReports/com.apple.WebKit.Networking_2016-11-20-092956_roberts-MacBook-Air.crash` (size 81529, modified 2016-11-20 14:29:56)
- `jpmi_metadata/Users/roberthunter/Desktop/WirelessDiagnostics_C02S953UH3QF_2016-11-22_03.46.09/WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3/DiagnosticReports/com.apple.WebKit.WebContent_2016-11-20-090240_roberts-MacBook-Air.cpu_resource.diag` (size 51872, modified 2016-11-20 14:02:40)

### Serial number

Wireless-diagnostics capture folders are named with serial `C02S953UH3QF` (1,090 rows reference the serial in the inventory).

Capture folders:

- `WirelessDiagnostics_C02S953UH3QF_2016-11-20_21.14.14 3`
- `WirelessDiagnostics_C02S953UH3QF_2016-11-22_03.46.09 2`

`C02…` prefix serials are consistent with a 2015-era MacBook Air. The computer-name evidence (`roberts-MacBook-Air`) independently indicates a **MacBook Air**.

> **Discrepancy to investigate:** external documentation for this lineage states `MacBookPro14,1`. The JPMI metadata (computer name and wireless-diagnostics serial) is consistent with a MacBook Air. The two cannot both describe the same primary machine without further reconciliation of the external claim.

### Wireless diagnostics captures

The `Desktop/090-[]/` and `Desktop/WirelessDiagnostics_*` subtrees contain `ioreg.txt` (1,244,288 B), `spindump.txt` (1,826,474 B), `system.log` (394,970 B), `wifi.log`, `top.txt`, `ifconfig`, `netstat`, `kextstat`, and CoreCapture wireless logs. These are diagnostics generated on the originating Mac. Representative items:


| Path | Size | SHA-256 | Modified |
|---|---|---|---|
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 8/spindump.txt | 1826474 | 39278ac39f37c473… | 2016-11-22 08:44:26 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 6/spindump.txt | 1826474 |  | 2016-11-22 08:44:26 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/spindump.txt | 1826474 | 39278ac39f37c473… | 2016-11-22 08:44:26 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 6/ioreg.txt | 1244288 |  | 2016-11-22 08:44:52 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/ioreg.txt | 1244288 | 3d877173da279662… | 2016-11-22 08:44:52 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 8/ioreg.txt | 1244288 | 3d877173da279662… | 2016-11-22 08:44:52 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 6/system.log | 394970 |  | 2016-11-22 08:46:09 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/system.log | 394970 | ec616c273c4009bd… | 2016-11-22 08:46:09 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 8/system.log | 394970 | ec616c273c4009bd… | 2016-11-22 08:46:09 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 5/system.log.0 | 214871 |  | 2018-05-31 08:17:33 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 2/system.log.0 | 214871 | e46aa52215e4593e… | 2018-12-19 10:40:40 |
| jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 6/wifi.log | 155095 |  | 2016-11-22 08:43:52 |


### Byte-identical readable routes

The diagnostics files are metadata-only in JPMI but several have exact SHA-256 matches in the readable APFS (source 1), GAI (source 116), and 0728 (source 2) inventories. When those sources are mounted, the diagnostics content (hardware registry, process dumps, logs) can be read byte-for-byte. The routes are leads, not copies in this package.


| SHA-256 | JPMI path | Readable match path(s) |
|---|---|---|
| 0be4121167999a39… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 2/wifi.log.0 | 0728/Extra Found Files/Document/Text Document/0052474.txt; 0728/Extra Found Files/Document/Text Document/0052475.txt; 0728/Extra Found Files/Document/Text Document/0052581.txt; … (+35 more) |
| 2cbb0834ed467917… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 10/system.log.0.gz | 0728/Extra Found Files/Archive/GZip Archive/0052427.gz; 0728/Extra Found Files/Archive/GZip Archive/0052462.gz; 0728/Extra Found Files/Archive/GZip Archive/0052500.gz; … (+78 more) |
| 39278ac39f37c473… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/spindump.txt | 0728/Extra Found Files/Document/Text Document/0052660.txt; 0728/Extra Found Files/Document/Text Document/0053055.txt; 0728/Extra Found Files/Document/Text Document/0053126.txt; … (+14 more) |
| 3d877173da279662… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/ioreg.txt | 0728/Extra Found Files/Document/Text Document/0053051.txt; 0728/Extra Found Files/Document/Text Document/0053122.txt; 0728/Extra Found Files/Document/Text Document/0053190.txt; … (+12 more) |
| 48b4c20b62be24d3… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/system.log.1.gz | 0728/Extra Found Files/Archive/GZip Archive/0052667.gz; 0728/Extra Found Files/Archive/GZip Archive/0053058.gz; 0728/Extra Found Files/Archive/GZip Archive/0053129.gz; … (+14 more) |
| e0c0140183613e36… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 10/top.txt | 0728/Extra Found Files/Document/Text Document/0052437.txt; 0728/Extra Found Files/Document/Text Document/0052472.txt; 0728/Extra Found Files/Document/Text Document/0052509.txt; … (+78 more) |
| e113e0c08cac4e8a… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/wifi.log | 0728/Extra Found Files/Document/Text Document/0052674.txt; 0728/Extra Found Files/Document/Text Document/0053070.txt; 0728/Extra Found Files/Document/Text Document/0053141.txt; … (+14 more) |
| e46aa52215e4593e… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 2/system.log.0 | 0728/Extra Found Files/Document/Text Document/0052499.txt; 0728/Extra Found Files/Document/Text Document/0052919.txt; cache/gai_archive_extract/6231349_system.log.0.gz_a2baf7d51c3b49a1/system.log.0; … (+24 more) |
| ec616c273c4009bd… | jpmi_metadata/Users/roberthunter/Desktop/090-[]/ 11 5/system.log | 0728/Extra Found Files/Document/Text Document/0052663.txt; 0728/Extra Found Files/Document/Text Document/0053056.txt; 0728/Extra Found Files/Document/Text Document/0053127.txt; … (+14 more) |


## 3. What JPMI metadata cannot establish alone

- Exact CPU, RAM, storage model, or battery identity — requires the `ioreg.txt`/`spindump.txt` bytes via the readable routes above.
- Whether the 2016 diagnostics represent the same machine as the post-2019 custody medium.
- The exact repair-shop handling steps.

## 4. Conclusions (bounded)

1. The originating computer was named `roberts-MacBook-Air` and its wireless diagnostics carry serial `C02S953UH3QF` — consistent with a 2015-era MacBook Air.
2. Wireless diagnostics were captured **2016-11-20** and **2016-11-22**.
3. The external custody medium is a Micron Crucial X6 SSD, serial `2145E498755E`.
4. The external `MacBookPro14,1` claim requires reconciliation with the MacBook Air evidence above.

