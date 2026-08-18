#!/usr/bin/env python3
"""Stage 50 — standalone JPMI forensic reports.

Writes:
  build/reports/01_computer_information.md
  build/reports/02_os_version.md
  build/reports/03_known_datetime_stamps_of_use.md
  build/reports/04_post_2019_03_31_timeline.md
  build/reports/05_coverage_and_method.md

Despite legacy filenames, every report is JPMI-only. No comparative corpus or
cross-corpus route is required to explain the evidence.

Read-only against PostgreSQL. Reads Stage-10 rollups from build/file_tree/.
"""
import csv
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import BUILD, connect, load_limits, to_source_uri

REPORTS = BUILD / "reports"
SOURCE_ID = 122


def md_table(header, rows):
    out = [
        "| " + " | ".join(header) + " |",
        "|" + "|".join("---" for _ in header) + "|",
    ]
    for row in rows:
        out.append("| " + " | ".join(str(c) if c is not None else "" for c in row) + " |")
    return "\n".join(out) + "\n"


def fmt_ts(ts):
    return ts.strftime("%Y-%m-%d %H:%M:%S") if ts else ""


def read_tsv(path):
    with open(path, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def main():
    limits = load_limits()
    boundary = limits["post_2019_03_31_boundary"]
    pg = connect()
    data = {}

    with pg.cursor() as c:
        c.execute("SELECT * FROM jpmi_acquisition")
        cols = [d.name for d in c.description]
        data["acq"] = dict(zip(cols, c.fetchone()))

        c.execute(
            """
            SELECT count(*)
              FROM files
             WHERE source_id = %s
            """,
            (SOURCE_ID,),
        )
        data["inventory_paths"] = c.fetchone()[0]

        c.execute(
            """
            SELECT count(*) FILTER (WHERE sha256 IS NOT NULL AND sha256 <> ''),
                   count(DISTINCT sha256) FILTER (WHERE sha256 IS NOT NULL AND sha256 <> '')
              FROM jpmi_sha256_allpaths
            """
        )
        data["hash_counts"] = c.fetchone()

        c.execute("SELECT count(*) FROM jpmi_sha256_allpaths")
        data["hash_manifest_rows"] = c.fetchone()[0]

        c.execute("SELECT count(*) FROM jpmi_cnid_map")
        data["cnid_rows"] = c.fetchone()[0]

        c.execute("SELECT count(*) FROM jpmi_alias_map")
        data["alias_rows"] = c.fetchone()[0]

        c.execute("SELECT count(*) FROM jpmi_tsk_timeline")
        data["tsk_rows"] = c.fetchone()[0]

        c.execute(
            """
            SELECT count(*) FILTER (WHERE relative_path LIKE '%%.emlx%%'),
                   count(*) FILTER (WHERE relative_path LIKE '%%.vcf%%'),
                   count(*) FILTER (WHERE relative_path LIKE '%%.icloud%%')
              FROM files
             WHERE source_id = %s
            """,
            (SOURCE_ID,),
        )
        data["content_counts"] = c.fetchone()

        c.execute(
            """
            SELECT lower(coalesce(nullif(regexp_replace(filename, '^.*\\.', ''), filename), '[no extension]')) AS ext,
                   count(*) AS n
              FROM files
             WHERE source_id = %s
             GROUP BY 1
             ORDER BY n DESC
             LIMIT 20
            """,
            (SOURCE_ID,),
        )
        data["top_extensions"] = c.fetchall()

        c.execute(
            """
            SELECT 'created' AS event, extract(year FROM created_ts)::int AS yr, count(*)
              FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
             WHERE f.source_id = %s AND created_ts IS NOT NULL
             GROUP BY 2
            UNION ALL
            SELECT 'modified', extract(year FROM modified_ts)::int, count(*)
              FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
             WHERE f.source_id = %s AND modified_ts IS NOT NULL
             GROUP BY 2
            UNION ALL
            SELECT 'accessed', extract(year FROM accessed_ts)::int, count(*)
              FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
             WHERE f.source_id = %s AND accessed_ts IS NOT NULL
             GROUP BY 2
            """,
            (SOURCE_ID, SOURCE_ID, SOURCE_ID),
        )
        data["time_by_year"] = c.fetchall()

        c.execute(
            """
            SELECT to_char(accessed_ts, 'YYYY-MM') AS ym, count(*)
              FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
             WHERE f.source_id = %s AND accessed_ts IS NOT NULL
             GROUP BY 1
             ORDER BY count(*) DESC
             LIMIT 12
            """,
            (SOURCE_ID,),
        )
        data["access_clusters"] = c.fetchall()

        c.execute(
            """
            SELECT extract(year FROM modified_ts)::int AS yr, count(*)
              FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
             WHERE f.source_id = %s AND modified_ts > %s
             GROUP BY 1
             ORDER BY 1
            """,
            (SOURCE_ID, boundary),
        )
        data["post_by_year"] = c.fetchall()

        c.execute(
            """
            SELECT f.relative_path, f.size, t.created_ts, t.modified_ts, t.accessed_ts
              FROM jpmi_file_times t JOIN files f ON f.id = t.file_id
             WHERE f.source_id = %s AND t.modified_ts > %s
             ORDER BY t.modified_ts
            """,
            (SOURCE_ID, boundary),
        )
        data["post_rows"] = c.fetchall()

        c.execute(
            """
            SELECT count(*) FILTER (WHERE relative_path ~* 'roberts-macbook-air'),
                   count(*) FILTER (WHERE relative_path ~* 'C02S953UH3QF'),
                   count(*) FILTER (WHERE relative_path ~* 'WirelessDiagnostics')
              FROM files
             WHERE source_id = %s
            """,
            (SOURCE_ID,),
        )
        data["historical_diag_counts"] = c.fetchone()

    pg.close()

    data["home"] = read_tsv(BUILD / "file_tree" / "03_home_overview.tsv")
    data["top"] = read_tsv(BUILD / "file_tree" / "02_top_level_summary.tsv")

    REPORTS.mkdir(parents=True, exist_ok=True)
    report_01(data)
    report_02(data)
    report_03(data)
    report_04(data, boundary)
    report_05(data, limits)
    print("standalone JPMI reports written to", REPORTS)


def report_01(data):
    a = data["acq"]
    device_rows = [
        ("Custody device", a.get("drive_model")),
        ("Custody serial", a.get("drive_serial")),
        ("Image", a.get("source_image")),
        ("Format", a.get("image_format")),
        ("Image size", a.get("image_size_bytes")),
        ("MD5", a.get("image_md5")),
        ("SHA-1", a.get("image_sha1")),
        ("Acquisition tool", a.get("acquisition_tool")),
        ("Case number", a.get("case_number")),
    ]
    disk_rows = [
        ("Disk GUID", a.get("disk_guid")),
        ("EFI partition GUID", a.get("efi_partition_guid")),
        ("HFS+ partition GUID", a.get("hfs_partition_guid")),
        ("HFS+ sector offset", a.get("hfs_sector_offset")),
        ("Volume name", a.get("volume_name")),
        ("Volume identifier", a.get("volume_identifier")),
    ]
    mba, serial, wd = data["historical_diag_counts"]

    text = "# JPMI Device and Copy Identity\n\n"
    text += "## Observation — the later custody medium\n\n"
    text += "The forensic acquisition record describes a 500 GB-class external SSD. It is a **later custody medium, not the original laptop SSD**.\n\n"
    text += md_table(["Field", "Reported value"], device_rows)
    text += "\n## Observation — partition and volume identity\n\n"
    text += md_table(["Field", "Reported value"], disk_rows)
    text += (
        "\nThe destination is represented as a GPT-partitioned Mac-oriented disk with an EFI System Partition and a journaled HFS+ data volume. "
        "The acquisition record identifies an E01 image.\n\n"
        "## Interpretation\n\n"
        "The destination is a GPT-partitioned Mac-oriented disk with EFI and journaled HFS+ `Untitled`. "
        "Volume creation 26 September 2019, preserved 2016–March 2019 file timestamps, empty HFS+ hard-link private directories, and a `roberthunter` home at volume root support a **file-aware copy onto a newly formatted volume**. "
        "The Crucial X6 is a 2020+ product; the 2019 volume reached it by a later volume clone. The E01 is a forensic image of that stick. See docs/COPY_METHOD.md.\n\n"
        "## Historical hardware artifacts inside the user tree\n\n"
        f"The inventory contains {mba} path rows referencing `roberts-MacBook-Air`, {serial} referencing serial `C02S953UH3QF`, and {wd} referencing WirelessDiagnostics material. "
        "These are useful evidence that older Mac diagnostic data is represented inside the account. They are **not sufficient by themselves to identify the particular computer left for repair in 2019**, because Mac home data can be migrated, restored, or copied forward across machines.\n\n"
        "## Limitation\n\n"
        "The present project does not have the original repair-shop copy log or command history. The exact intermediate recovery/copy mechanism therefore remains unresolved.\n"
    )
    (REPORTS / "01_computer_information.md").write_text(text, encoding="utf-8")


def report_02(data):
    content = data["content_counts"]
    home_rows = []
    for r in data["home"]:
        home_rows.append((r["home_subdir"], f"{int(r['file_count']):,}", f"{int(r['size_bytes']):,}"))

    ext_rows = [(ext, f"{n:,}") for ext, n in data["top_extensions"]]
    text = "# The Mac Environment Represented by JPMI\n\n"
    text += "JPMI represents a broad macOS user environment, not merely selected documents.\n\n"
    text += "## `roberthunter` home-directory rollup\n\n"
    text += md_table(["Home directory", "File rows", "Represented bytes"], home_rows)
    text += "\n## Communications-oriented populations\n\n"
    text += md_table(
        ["Category", "Rows"],
        [
            ("Apple Mail `.emlx` paths", f"{content[0]:,}"),
            ("Contact `.vcf` paths", f"{content[1]:,}"),
            ("iCloud-related paths", f"{content[2]:,}"),
        ],
    )
    text += "\n## High-frequency filename extensions/types\n\n"
    text += md_table(["Extension / suffix", "Rows"], ext_rows)
    text += (
        "\n## Interpretation\n\n"
        "The large `Library`, Mail, Contacts, media, cloud, cache, database, and application-support populations are consistent with a copied working Mac account. "
        "They also explain why historical material can predate the destination volume: Apple users migrate data, sync cloud accounts, restore backups, and attach mobile devices over many years.\n\n"
        "## Limitation\n\n"
        "A file-path count is not a count of unique human-created items. Attachments, thumbnails, derivatives, caches, aliases, and repeated paths can multiply representations of the same underlying content.\n"
    )
    (REPORTS / "02_os_version.md").write_text(text, encoding="utf-8")


def report_03(data):
    by_year = {}
    for event, year, count in data["time_by_year"]:
        by_year.setdefault(year, {})[event] = count
    rows = []
    for year in sorted(by_year):
        d = by_year[year]
        rows.append((year, d.get("created", 0), d.get("modified", 0), d.get("accessed", 0)))

    a = data["acq"]
    text = "# JPMI Datetime Evidence\n\n"
    text += "## Key custody dates\n\n"
    text += md_table(
        ["Event", "Reported date"],
        [
            ("Repair-shop period", "April 2019 (historical context)"),
            ("HFS+ destination creation", "2019-09-26 22:59:02 CDT"),
            ("E01 acquisition record", a.get("reported_at")),
            ("Reported volume last write", "2024-11-21 17:40:22 CST"),
        ],
    )
    text += "\n## File-time distribution by year\n\n"
    text += md_table(["Year", "Created", "Modified", "Accessed"], rows)
    text += "\n## Largest accessed-time clusters\n\n"
    text += md_table(["Year-month", "Rows"], data["access_clusters"])
    text += (
        "\n## Interpretation\n\n"
        "The broad modified-time population is concentrated before the repair event. The March/April 2022 access wave is software-scale activity, not evidence that a person manually opened hundreds of thousands of files. "
        "The delivered records also pair a 2022 acquisition record with a 2024 HFS+ last-write. An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write, so that pair is an **unresolved source-chronology discrepancy**, not proof that the 2022 E01 itself changed in 2024.\n\n"
        "## Limitation\n\n"
        "The source reports use mixed timezone conventions, and the acquisition/report lineage needed to reconcile the 2022/2024 dates is incomplete. Exact sequencing should not be asserted until both issues are resolved.\n"
    )
    (REPORTS / "03_known_datetime_stamps_of_use.md").write_text(text, encoding="utf-8")


def report_04(data, boundary):
    text = "# Post-Repair Custody Activity\n\n"
    text += f"Boundary used for the technical slice: `modified_ts > {boundary}`.\n\n"
    text += f"**{len(data['post_rows']):,} inventory rows** fall after that boundary.\n\n"
    text += "## Summary by year\n\n"
    text += md_table(["Year", "Rows"], data["post_by_year"])
    text += (
        "\n## Interpretation\n\n"
        "The later population is dominated by filesystem and application metadata such as `.DS_Store`, Spotlight, DocumentRevisions, directories, and temporary/system state. "
        "It establishes that the represented copy lineage contains later system-state activity; it does not, by itself, prove wholesale insertion of substantive user documents or identify which physical/image stage produced every later timestamp. "
        "In particular, the 2024 rows must be reconciled with the separately reported 2022 E01 acquisition.\n\n"
        "## Complete modified-row set\n\n"
    )
    rows = []
    for path, size, created, modified, accessed in data["post_rows"]:
        rows.append((to_source_uri(path), size or "", fmt_ts(created),
                     fmt_ts(modified), fmt_ts(accessed)))
    text += md_table(["Path", "Size", "Created", "Modified", "Accessed"], rows)
    text += (
        "\n## Limitation\n\n"
        "A filesystem timestamp does not identify the human or process responsible for the event. Attribution requires object type, surrounding activity, logs, custody records, and a reconciled source chronology.\n"
    )
    (REPORTS / "04_post_2019_03_31_timeline.md").write_text(text, encoding="utf-8")


def report_05(data, limits):
    hashed_paths, distinct_hashes = data["hash_counts"]
    rows = [
        ("Normalized JPMI inventory paths", f"{data['inventory_paths']:,}"),
        ("Rank-1 JPMI hash-manifest paths", f"{data['hash_manifest_rows']:,}"),
        ("Hash-manifest paths with SHA-256", f"{hashed_paths:,}"),
        ("Distinct reported SHA-256 values", f"{distinct_hashes:,}"),
        ("CNID-map rows", f"{data['cnid_rows']:,}"),
        ("Alias-map rows", f"{data['alias_rows']:,}"),
        ("TSK timeline rows", f"{data['tsk_rows']:,}"),
    ]
    a = data["acq"]
    text = "# JPMI Coverage, Method, and Limits\n\n"
    text += "## Coverage\n\n"
    text += md_table(["Metric", "Value"], rows)
    text += (
        "\n## Method\n\n"
        "The pipeline performs read-only queries against JPMI tables, writes derived public artifacts under `build/`, shards large exports under the configured file-size budget, and validates section manifests and checksums. "
        "This standalone repository intentionally does not generate comparison tables.\n\n"
        "## Source boundary\n\n"
        "The GitHub project publishes received JPMI metadata/hash evidence and derived reports. The restricted E01 image itself is not published here. Therefore a reported manifest hash is distinguished from a hash freshly recomputed by this checkout from restricted source bytes.\n\n"
        "## Copy-method boundary\n\n"
        "Volume `Untitled` was formatted 26 September 2019 and populated by a timestamp-preserving file-aware copy of `roberthunter`. "
        "A later volume clone put that filesystem onto the Crucial X6 (a 2020+ product). "
        "The E01 is a forensic image of that X6. The April 2019 store-server utility remains unnamed. See docs/COPY_METHOD.md.\n\n"
        "## Acquisition chronology boundary\n\n"
        f"The acquisition record reports `{a.get('source_image')}` with date `{a.get('reported_at')}`, while delivered HFS+ metadata reports a 2024 last-write. An immutable E01 actually acquired in 2022 cannot later acquire a 2024 filesystem write. The relationship between those records is unresolved and requires the original acquisition/report lineage.\n\n"
        "## Size policy\n\n"
        f"Per-file budget: {limits['per_file_budget_bytes']:,} bytes. Hard cap: {limits['hard_cap_bytes']:,} bytes.\n"
    )
    (REPORTS / "05_coverage_and_method.md").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
