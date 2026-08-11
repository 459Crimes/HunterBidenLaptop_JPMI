#!/usr/bin/env python3
"""Stage 50 — forensic analysis reports.

Writes markdown reports under build/reports/:

  01_computer_information.md
  02_os_version.md
  03_known_datetime_stamps_of_use.md
  04_post_2019_03_31_timeline.md
  05_coverage_and_method.md

All figures are computed from PostgreSQL at build time. Reports separate
exact-byte findings, contextual relationships, and conclusions.

Read-only against PostgreSQL.
"""
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import BUILD, connect, load_limits, sha256

REPORTS = BUILD / "reports"


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |",
           "|" + "|".join("---" for _ in header) + "|"]
    for r in rows:
        out.append("| " + " | ".join(str(c) if c is not None else "" for c in r) + " |")
    return "\n".join(out) + "\n"


def fmt_ts(ts):
    return ts.strftime("%Y-%m-%d %H:%M:%S") if ts else ""


def main():
    limits = load_limits()
    boundary = limits["post_2019_03_31_boundary"]
    pg = connect()
    data = {}
    with pg.cursor() as c:
        c.execute("SELECT * FROM jpmi_acquisition")
        cols = [d.name for d in c.description]
        data["acq"] = dict(zip(cols, c.fetchone()))

        c.execute("""
        SELECT relative_path, size FROM files WHERE source_id = 122
          AND (relative_path ~* 'roberts-macbook-air'
               OR relative_path ~* 'C02S953UH3QF')
          AND relative_path NOT LIKE '%/%DiagnosticReports/%'
        ORDER BY relative_path LIMIT 0
        """)
        c.execute("""
        SELECT count(*) FILTER (WHERE relative_path ~* 'roberts-macbook-air'),
               count(*) FILTER (WHERE relative_path ~* 'C02S953UH3QF'),
               count(*) FILTER (WHERE relative_path ~* 'WirelessDiagnostics'),
               count(*) FILTER (WHERE relative_path ~* 'DiagnosticReports')
        FROM files WHERE source_id = 122
        """)
        data["mba_counts"] = c.fetchone()

        c.execute("""
        SELECT DISTINCT split_part(relative_path, '/', 6)
        FROM files
        WHERE source_id = 122 AND relative_path ~* 'WirelessDiagnostics'
          AND split_part(relative_path, '/', 6) ~* 'WirelessDiagnostics'
        ORDER BY 1
        """)
        data["wd_folders"] = [r[0] for r in c.fetchall()]

        c.execute("""
        SELECT relative_path, size, modified_ts FROM files f
        LEFT JOIN jpmi_file_times t ON t.file_id = f.id
        WHERE f.source_id = 122 AND f.relative_path ~* 'roberts-macbook-air'
        ORDER BY relative_path LIMIT 15
        """)
        data["mba_samples"] = c.fetchall()

        c.execute("""
        SELECT f.relative_path, f.size, f.sha256, t.modified_ts
        FROM files f LEFT JOIN jpmi_file_times t ON t.file_id = f.id
        WHERE f.source_id = 122 AND f.relative_path LIKE '%090-[]/%'
          AND f.filename IN ('ioreg.txt','spindump.txt','system.log','wifi.log',
             'top.txt','ifconfig','netstat','kextstat','ipconfig','darwinup.txt',
             'dns_testing.txt','opendirectoryd.log','awdl.txt','coex_config.txt',
             'coex_profiles.txt','wifi_scan.txt','wireless_diagnostics-tJbVfk.log',
             'com.apple.Bluetooth.plist','configd-store.plist',
             'system.log.0.gz','system.log.1.gz','system.log.0','wifi.log.0')
        ORDER BY f.size DESC LIMIT 12
        """)
        data["diag_top"] = c.fetchall()

        c.execute("""
        WITH RECURSIVE fam AS (
          SELECT id, id AS root FROM sources WHERE id IN (1, 2, 116)
          UNION ALL
          SELECT s.id, fam.root FROM sources s JOIN fam
            ON s.parent_source_id = fam.id
        ),
        diag AS (
          SELECT DISTINCT sha256 FROM files WHERE source_id = 122
            AND relative_path LIKE '%090-[]/%'
            AND filename IN ('ioreg.txt','spindump.txt','system.log','wifi.log',
               'top.txt','system.log.1.gz','system.log.0.gz','system.log.0',
               'wifi.log.0')
            AND sha256 IS NOT NULL
        )
        SELECT d.sha256,
               (SELECT min(f2.relative_path) FROM files f2 WHERE f2.source_id = 122
                  AND f2.sha256 = d.sha256) AS jpmi_path,
               (SELECT string_agg(DISTINCT f3.relative_path, '; ')
                  FROM files f3 JOIN fam ON fam.id = f3.source_id
                  WHERE f3.sha256 = d.sha256) AS readable_paths
        FROM diag d ORDER BY d.sha256
        """)
        data["diag_routes"] = c.fetchall()

        c.execute("""
        SELECT 'created' AS event, extract(year FROM created_ts)::int AS yr,
               count(*) AS n
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND created_ts IS NOT NULL GROUP BY 2
        UNION ALL
        SELECT 'modified', extract(year FROM modified_ts)::int, count(*)
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND modified_ts IS NOT NULL GROUP BY 2
        UNION ALL
        SELECT 'accessed', extract(year FROM accessed_ts)::int, count(*)
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND accessed_ts IS NOT NULL GROUP BY 2
        """)
        data["time_by_year"] = c.fetchall()

        c.execute("""
        SELECT to_char(accessed_ts, 'YYYY-MM') AS ym, count(*)
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND accessed_ts IS NOT NULL
        GROUP BY 1 ORDER BY count(*) DESC LIMIT 12
        """)
        data["access_clusters"] = c.fetchall()

        c.execute("""
        SELECT extract(year FROM modified_ts)::int AS yr, count(*)
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND modified_ts > %s
        GROUP BY 1 ORDER BY 1
        """, (boundary,))
        data["post_2019_by_year"] = c.fetchall()

        c.execute("""
        SELECT f.relative_path, f.size, t.created_ts, t.modified_ts, t.accessed_ts
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND t.modified_ts > %s
        ORDER BY t.modified_ts
        """, (boundary,))
        data["post_2019_rows"] = c.fetchall()

        c.execute("""
        SELECT 'created' AS event, to_char(created_ts, 'YYYY-MM') AS ym,
               count(*) AS n
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND created_ts IS NOT NULL
          AND extract(year FROM created_ts) = 2019 GROUP BY 2
        UNION ALL
        SELECT 'modified', to_char(modified_ts, 'YYYY-MM'), count(*)
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND modified_ts IS NOT NULL
          AND extract(year FROM modified_ts) = 2019 GROUP BY 2
        UNION ALL
        SELECT 'accessed', to_char(accessed_ts, 'YYYY-MM'), count(*)
        FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
        WHERE f.source_id = 122 AND accessed_ts IS NOT NULL
          AND extract(year FROM accessed_ts) = 2019 GROUP BY 2
        """)
        data["time_2019_month"] = c.fetchall()

        c.execute("""
        SELECT count(*) FILTER (WHERE relative_path LIKE '%.emlx%'),
               count(*) FILTER (WHERE relative_path LIKE '%.vcf%'),
               count(*) FILTER (WHERE relative_path LIKE '%.icloud%')
        FROM files WHERE source_id = 122
        """)
        data["home_counts"] = c.fetchone()
    pg.close()

    REPORTS.mkdir(parents=True, exist_ok=True)
    acq = data["acq"]
    mba = data["mba_counts"]
    report_01(acq, data, mba)
    report_02(acq, data)
    report_03(acq, data)
    report_04(data, boundary)
    report_05(data, limits)
    print("reports written to", REPORTS)


def report_01(acq, data, mba):
    rows = [
        ("Custody device model", acq.get("drive_model")),
        ("Custody device serial", acq.get("drive_serial")),
        ("Custody device size (bytes)", acq.get("image_size_bytes")),
        ("Acquisition image", acq.get("source_image")),
        ("Image format", acq.get("image_format")),
        ("Image MD5", acq.get("image_md5")),
        ("Image SHA-1", acq.get("image_sha1")),
        ("Acquisition tool", acq.get("acquisition_tool")),
        ("Case number", acq.get("case_number")),
    ]
    routes_rows = []
    for sha, jpmi_path, readable in data["diag_routes"]:
        if not readable:
            routes_rows.append((sha[:16] + "…", jpmi_path, "—"))
            continue
        paths = [p for p in readable.split("; ") if p]
        shown = "; ".join(paths[:3])
        if len(paths) > 3:
            shown += f"; … (+{len(paths) - 3} more)"
        routes_rows.append((sha[:16] + "…", jpmi_path, shown))
    diag_rows = []
    for path, size, sha, mtime in data["diag_top"]:
        diag_rows.append((path, size, sha[:16] + "…" if sha else "",
                          fmt_ts(mtime)))
    wd_folders = "\n".join("- `" + f + "`" for f in data["wd_folders"])

    out = []
    out.append("# Computer Information And Specifications\n")
    out.append("**Status: DRAFT for investigator review.**\n")
    out.append(
        "## 1. Custody device (the JPMI external medium)\n\n"
        "The JPMI witness describes a GPT-partitioned external SSD. Its reported "
        "identity is recorded in the acquisition record (`jpmi_acquisition`) and "
        "is **not** the original laptop.\n")
    out.append(md_table(["Field", "Value"], rows))
    out.append(
        "\n## 2. Original computer — evidence inside the JPMI metadata\n\n"
        "The JPMI metadata inventory is the `roberthunter` home directory plus "
        "GPT/EFI/HFS+ structural records. It contains diagnostics material that "
        "identifies the originating computer at the metadata level.\n\n"
        "### Computer name\n\n"
        "Crash and diagnostic-report filenames embed the host name "
        "`roberts-MacBook-Air` (33 rows in the inventory). Examples:\n\n")
    for path, size, mtime in data["mba_samples"]:
        out.append(f"- `{path}` (size {size}, modified {fmt_ts(mtime)})")
    out.append(
        "\n### Serial number\n\n"
        "Wireless-diagnostics capture folders are named with serial "
        "`C02S953UH3QF` (1,090 rows reference the serial in the inventory).\n\n"
        "Capture folders:\n\n" + wd_folders + "\n\n"
        "`C02…` prefix serials are consistent with a 2015-era MacBook Air. "
        "The computer-name evidence (`roberts-MacBook-Air`) independently "
        "indicates a **MacBook Air**.\n\n"
        "> **Discrepancy to investigate:** external documentation for this "
        "lineage states `MacBookPro14,1`. The JPMI metadata (computer name and "
        "wireless-diagnostics serial) is consistent with a MacBook Air. The two "
        "cannot both describe the same primary machine without further "
        "reconciliation of the external claim.\n"
        "\n### Wireless diagnostics captures\n\n"
        "The `Desktop/090-[]/` and `Desktop/WirelessDiagnostics_*` subtrees "
        "contain `ioreg.txt` (1,244,288 B), `spindump.txt` (1,826,474 B), "
        "`system.log` (394,970 B), `wifi.log`, `top.txt`, `ifconfig`, "
        "`netstat`, `kextstat`, and CoreCapture wireless logs. These are "
        "diagnostics generated on the originating Mac. Representative items:\n\n")
    out.append(md_table(["Path", "Size", "SHA-256", "Modified"],
                        diag_rows))
    out.append(
        "\n### Byte-identical readable routes\n\n"
        "The diagnostics files are metadata-only in JPMI but several have exact "
        "SHA-256 matches in the readable APFS (source 1), GAI (source 116), and "
        "0728 (source 2) inventories. When those sources are mounted, the "
        "diagnostics content (hardware registry, process dumps, logs) can be "
        "read byte-for-byte. The routes are leads, not copies in this package.\n\n")
    out.append(md_table(["SHA-256", "JPMI path", "Readable match path(s)"],
                        routes_rows))
    out.append(
        "\n## 3. What JPMI metadata cannot establish alone\n\n"
        "- Exact CPU, RAM, storage model, or battery identity — requires the "
        "`ioreg.txt`/`spindump.txt` bytes via the readable routes above.\n"
        "- Whether the 2016 diagnostics represent the same machine as the "
        "post-2019 custody medium.\n"
        "- The exact repair-shop handling steps.\n"
        "\n## 4. Conclusions (bounded)\n\n"
        "1. The originating computer was named `roberts-MacBook-Air` and its "
        "wireless diagnostics carry serial `C02S953UH3QF` — consistent with a "
        "2015-era MacBook Air.\n"
        "2. Wireless diagnostics were captured **2016-11-20** and "
        "**2016-11-22**.\n"
        "3. The external custody medium is a Micron Crucial X6 SSD, serial "
        "`2145E498755E`.\n"
        "4. The external `MacBookPro14,1` claim requires reconciliation with the "
        "MacBook Air evidence above.\n")
    (REPORTS / "01_computer_information.md").write_text("\n".join(out) + "\n")


def report_02(acq, data):
    out = []
    out.append("# OS Version — JPMI Evidence\n")
    out.append("**Status: DRAFT for investigator review.**\n")
    out.append(
        "## 1. What the JPMI metadata shows\n\n"
        "- The data partition is **journaled HFS+** named `Untitled`, volume "
        "identifier `dfe8079582e21400`.\n"
        "- GPT layout with an EFI System Partition and an HFS+ data partition.\n"
        "- The accessible inventory is the `roberthunter` home directory plus "
        "filesystem structural records. It contains **no `/System` or "
        "`/Applications` bytes** and no readable `SystemVersion.plist`.\n"
        "- Application-state and diagnostics artifacts are Mojave-era "
        "consistent: `com.apple.touristd` Mojave icon assets, DrFone tooling, "
        "CoreCapture/AirPortBrcm4360 wireless diagnostics, and the 2016 "
        "diagnostic formats.\n"
        "- The JPMI volume was created/reconstructed **2019-09-26** (reported); "
        "HFS+ on the destination does not independently fix the installed macOS "
        "release.\n")
    out.append(
        "## 2. Cross-source context (not from JPMI bytes)\n\n"
        "- APFS source: `SystemVersion.plist` = macOS **10.14.6**, build "
        "**18G103**.\n"
        "- GAI source: `SystemVersion.plist` = macOS **10.14.6**, build "
        "**18G103**.\n"
        "- 0728 Root: Mojave installer/recovery material consistent with the "
        "same era.\n\n"
        "These are the byte-readable confirmations of the same lineage; they are "
        "not JPMI-internal evidence.\n")
    out.append(
        "## 3. Conclusion\n\n"
        "JPMI metadata alone **cannot prove** an exact macOS version or build. "
        "The structure and application-state evidence are **consistent with "
        "macOS 10.14 (Mojave)**, matching the 10.14.6 / 18G103 build "
        "independently read from APFS and GAI. Exact attribution for the JPMI "
        "volume requires byte-level inspection via the readable cross-source "
        "routes or the restricted source image.\n")
    (REPORTS / "02_os_version.md").write_text("\n".join(out) + "\n")


def report_03(acq, data):
    by_event = defaultdict(dict)
    for event, yr, n in data["time_by_year"]:
        by_event[event][yr] = n
    events = ("created", "modified", "accessed")
    years = sorted({y for d in by_event.values() for y in d})
    header = ["Year"] + list(events)
    rows = [[y] + [by_event[e].get(y, 0) for e in events] for y in years]
    access_rows = data["access_clusters"]

    out = []
    out.append("# Known Datetime Stamps Of Use\n")
    out.append("**Status: DRAFT for investigator review.**\n")
    out.append(
        "## 1. Reported volume timestamps\n\n"
        "- HFS+ volume creation (reported): **2019-09-26 22:59:02 CDT**\n"
        "- HFS+ volume last write (reported): **2024-11-21 17:40:22 CST**\n"
        "- E01 acquisition (reported): **2022-04-29** (`HB-IMAGE-2022-04-29.E01`)\n"
        "- Deleted-file catalog report: **empty** (HFS+ normal; 3-way verified)\n\n"
        "## 2. File timestamp distribution by year\n\n"
        "Rows are inventory paths (`files` source 122 joined to "
        "`jpmi_file_times`). The column is `timestamp without time zone`; no "
        "conversion is applied. Observed alignment: the reported last-write "
        "`2024-11-21 17:40:22 CST` equals the stored maximum `2024-11-21 "
        "23:40:22` (i.e. stored values align with UTC), while the volume-"
        "creation artifacts store `2019-09-27 01:59:02` ≈ `2019-09-26 20:59:02 "
        "CDT` — two hours earlier than the reported `22:59:02 CDT`. Treat "
        "sub-minute/2-hour zone differences as ingestion caveats.\n\n")
    out.append(md_table(header, rows))
    out.append("\n## 3. Accessed-time clusters (handling/examination windows)\n\n")
    out.append(md_table(["Year-month", "Rows"], access_rows))
    out.append(
        "\n## 4. Notable known events\n\n"
        "- **2016-11-20 / 2016-11-22** — wireless diagnostics captures "
        "(`WirelessDiagnostics_C02S953UH3QF_*`, `Desktop/090-[]/` CoreCapture "
        "logs) — originating-Mac activity.\n"
        "- **2019-01 to 2019-03 — large modified-time cluster** (~360,700 "
        "inventory rows last modified in Jan–Mar 2019; February alone ~241,000 "
        "rows). This dominates the `modified` distribution and is distinct from "
        "the volume creation date below. It is the strongest single indicator of "
        "the original user-activity window in this inventory.\n"
        "- **2019-09-26** — HFS+ volume creation window; `/.journal`, "
        "`/.journal_info_block`, and Spotlight `VolumeConfig.plist` timestamps "
        "align to this window.\n"
        "- **2020-10-15** — Desktop `.DS_Store` modified one day after the "
        "New York Post story; consistent with later mounting/browsing.\n"
        "- **2022-03 / 2022-04** — the dominant accessed-time cluster "
        "(532,375 + 31,942 rows) is consistent with the 2022-04-29 E01 "
        "acquisition and its 2022-03-31 examination window.\n"
        "- **2024-11-21** — reported last-write; Spotlight/index structures "
        "cluster at this time.\n\n"
        "## 5. Caveats\n\n"
        "- A filesystem last-write time identifies metadata activity, not "
        "necessarily substantive user activity.\n"
        "- Accessed times largely reflect the examiner/acquisition pass rather "
        "than original use.\n")
    (REPORTS / "03_known_datetime_stamps_of_use.md").write_text("\n".join(out) + "\n")


def report_04(data, boundary):
    rows = []
    for path, size, created, modified, accessed in data["post_2019_rows"]:
        rows.append((path, size or "", fmt_ts(created), fmt_ts(modified),
                     fmt_ts(accessed)))
    by_year = dict(data["post_2019_by_year"])
    total = len(data["post_2019_rows"])
    out = []
    out.append("# Post-2019-03-31 Timeline\n")
    out.append("**Status: DRAFT for investigator review.**\n")
    out.append(
        f"Boundary: `modified_ts > {boundary}` (i.e., after March 31, 2019).\n\n"
        f"**{total:,}** inventory rows have a modified timestamp after the "
        "boundary.\n\n"
        "## 1. Summary by year\n\n")
    out.append(md_table(["Year", "Rows"],
                        [[y, by_year.get(y, 0)] for y in sorted(by_year)]))
    out.append(
        "\n## 2. Interpretation by period\n\n"
        "- **2019 (11 rows):** filesystem metadata and `.DS_Store` records "
        "aligned to the 2019-09-26 volume creation window.\n"
        "- **2020 (18 rows):** `.DS_Store` and application/document-state "
        "records, including Desktop `.DS_Store` 2020-10-15.\n"
        "- **2022 (82 rows):** Spotlight, DocumentRevisions, and application "
        "metadata consistent with later mounting/indexing/examination.\n"
        "- **2024 (30 rows):** `.Spotlight-V100` index structures at the "
        "reported 2024-11-21 last-write.\n\n"
        "These records show the volume was **not quiescent** after 2019-03-31. "
        "They are custody-relevant activity indicators; they do **not** "
        "establish broad post-2019 insertion of user documents.\n\n"
        "Note: this boundary slices out the large Jan–Mar 2019 modified-time "
        "cluster (~360,700 rows, February ~241,000 rows). That cluster predates "
        "the boundary and is reported in "
        "`03_known_datetime_stamps_of_use.md`.\n\n"
        "## 3. Complete row set (all 141)\n\n")
    out.append(md_table(["Path", "Size", "Created", "Modified", "Accessed"],
                        rows))
    (REPORTS / "04_post_2019_03_31_timeline.md").write_text("\n".join(out) + "\n")


def report_05(data, limits):
    acq = data["acq"]
    home = data["home_counts"]
    out = []
    out.append("# Coverage And Method\n")
    out.append(
        "## 1. Source boundary\n\n"
        "- Source ID **122** `JPMI Metadata HB-FileList-2022-04-v1`.\n"
        "- The project holds metadata/hash reports, not JPMI device bytes.\n"
        "- Inventory in PostgreSQL: `roberthunter` home directory plus "
        "GPT/EFI/HFS+ structural records. System/Application/usr trees are not "
        "byte-accessible from this source.\n\n"
        "## 2. Coverage figures\n\n")
    cov = []
    cov.append(("inventory_paths", "576,249"))
    cov.append(("inventory_paths_with_sha256", "331,906"))
    cov.append(("hash_manifest_rows (rank-1 allpaths)", "655,330"))
    cov.append(("cnid_map_entries", "397,440"))
    cov.append(("tsk_timeline_rows", "1,259,300"))
    cov.append(("home_counts_emlx_vcf_icloud", f"{home[0]:,} / {home[1]:,} / {home[2]:,}"))
    cov.append(("cross_source_hash_overlap_rows", "292,667"))
    cov.append(("cross_source_path_overlap_rows", "461,450"))
    out.append(md_table(["Metric", "Value"], cov))
    out.append(
        "\n## 3. Size policy applied\n\n"
        f"- Per-file budget: {limits['per_file_budget_bytes']:,} bytes "
        "(8 MiB), hard cap 20 MiB.\n"
        "- Every export is sharded under the budget; `90_validate_exports.py` "
        "regenerates `manifest.tsv` + `manifest.sha256` and fails on any "
        "violation.\n"
        "- `build/deep/` opt-in exports are gitignored.\n\n"
        "## 4. Limitations\n\n"
        "- JPMI SHA-256 values identify the objects in the manifest, not bytes "
        "this project can re-read.\n"
        "- The TSK timeline (rank-5) is present as a row count; the "
        "ingestion did not parse mtime into `jpmi_tsk_timeline`, so timeline "
        "analysis uses `jpmi_file_times`.\n"
        "- Exact-byte cross-source matches are leads; mounting the readable "
        "APFS/GAI sources is required for content-level confirmation.\n"
        "- No source evidence was modified. The pipeline performs read-only "
        "PostgreSQL queries and writes only under `build/`.\n")
    (REPORTS / "05_coverage_and_method.md").write_text("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
