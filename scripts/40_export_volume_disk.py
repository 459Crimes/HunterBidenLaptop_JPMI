#!/usr/bin/env python3
"""Stage 40 — volume and disk information.

Writes:
  build/volume_info/01_volume_identity.tsv
  build/volume_info/02_volume_metadata.tsv
  build/volume_info/03_volume_system_state.tsv
  build/disk_info/01_acquisition.tsv
  build/disk_info/02_partition_map.tsv
  build/disk_info/03_disk_identity.tsv

Read-only against PostgreSQL.
"""
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import BUILD, connect, section_manifest, write_single

VOLUME_OBJECTS = """
SELECT f.relative_path, f.size, t.modified_ts
FROM files f LEFT JOIN jpmi_file_times t ON t.file_id = f.id
WHERE f.source_id = 122
  AND f.relative_path LIKE '%Basic data partition (2)/Untitled [HFS+]/Untitled/%'
  AND f.relative_path NOT LIKE '%/roberthunter/%'
ORDER BY f.relative_path
"""

ALL_FILES = """
SELECT f.relative_path, f.size, f.sha256, f.mtime
FROM files f WHERE f.source_id = 122
"""

BUCKET_RULES = [
    ("spotlight", lambda p: ".spotlight-v100" in p),
    ("document_revisions", lambda p: ".documentrevisions-v100" in p),
    ("hfs_journal", lambda p: p.endswith("/.journal") or p.endswith("/.journal_info_block")),
    ("efi_partition", lambda p: "efi system partition" in p),
    ("gpt_structural", lambda p: "unpartitioned space" in p or "backup gpt" in p
                                 or "protective mbr" in p or "partition entry array" in p),
    ("volume_structural", lambda p: "basic data partition" in p and "/roberthunter/" not in p),
    ("090_diagnostics", lambda p: "/desktop/090-[]/" in p),
    ("mail", lambda p: "library/mail" in p),
    ("photos", lambda p: "photos library" in p or "com.apple.photolibrary" in p),
    ("drfone_tooling", lambda p: "drfoneapps" in p or "/dr.fone" in p or "dr.fone" in p),
    ("chrome", lambda p: "application support/google/chrome" in p),
    ("icloud_cloudkit", lambda p: "icloud" in p or "cloudkit" in p
                                  or "com.apple.cloud" in p or "icloudphotos" in p),
    ("home_library", lambda p: "/library/" in p),
    ("desktop", lambda p: "/desktop/" in p),
    ("documents", lambda p: "/documents/" in p),
    ("downloads", lambda p: "/downloads/" in p),
    ("movies", lambda p: "/movies/" in p),
    ("music", lambda p: "/music/" in p),
    ("pictures", lambda p: "/pictures/" in p),
]

VOLUME_REPORTED = [
    ("volume_creation_reported", "2019-09-26 22:59:02 CDT",
     "reported HFS+ volume creation from source characterization"),
    ("volume_last_write_reported", "2024-11-21 17:40:22 CST",
     "reported last write from source characterization"),
    ("deleted_catalog_status", "empty",
     "HFS+ deleted-file catalog report returned no entries (verified 3 ways)"),
    ("unallocated_ranges", "~280 GB",
     "unallocated regions reported in source; carve of 262.5 GiB yielded 792 files"),
    ("hfs_journal_bytes", "41943040", "CNID 16 HFS+ journal preserved (rank4-hfs-journal.bin)"),
]


def classify(path):
    low = ("/" + path.lstrip("jpmi_metadata/")).lower()
    for name, rule in BUCKET_RULES:
        if rule(low):
            return name
    return "other"


def main():
    vol_dir = BUILD / "volume_info"
    disk_dir = BUILD / "disk_info"
    pg = connect()
    with pg.cursor() as c:
        c.execute("SELECT * FROM jpmi_acquisition")
        acq = c.fetchone()
        cols = [d.name for d in c.description]
        c.execute(VOLUME_OBJECTS)
        vol_objects = c.fetchall()
        c.execute(ALL_FILES)
        all_files = c.fetchall()
    pg.close()

    acq = dict(zip(cols, acq))

    identity = [
        ("volume_name", acq.get("volume_name")),
        ("volume_identifier", acq.get("volume_identifier")),
        ("main_volume", acq.get("main_volume")),
        ("filesystem", acq.get("fs_type")),
        ("hfs_sector_offset", acq.get("hfs_sector_offset")),
        ("source_image", acq.get("source_image")),
        ("image_format", acq.get("image_format")),
        ("image_size_bytes", acq.get("image_size_bytes")),
        ("sector_size", acq.get("sector_size")),
        ("sector_count", acq.get("sector_count")),
    ]
    identity += [(f, v) for f, v, _ in VOLUME_REPORTED]
    id_out = write_single(vol_dir, "01_volume_identity.tsv",
                          ["field", "value"], identity)

    vol_rows = []
    for path, size, mtime in vol_objects:
        note = "HFS+ journal" if path.endswith(".journal") else (
            "HFS+ journal info block" if path.endswith(".journal_info_block") else "")
        vol_rows.append((path, size or "", mtime.strftime("%Y-%m-%d %H:%M:%S")
                         if mtime else "", note))
    vol_out = write_single(vol_dir, "02_volume_metadata.tsv",
                           ["object", "size_bytes", "modified_ts", "note"],
                           vol_rows)

    buckets = defaultdict(lambda: {"n": 0, "bytes": 0, "hashes": 0})
    for path, size, sha, mtime in all_files:
        b = buckets[classify(path)]
        b["n"] += 1
        if size:
            b["bytes"] += size
        if sha:
            b["hashes"] += 1
    order = ["spotlight", "document_revisions", "hfs_journal", "efi_partition",
             "gpt_structural", "volume_structural", "090_diagnostics", "mail",
             "photos", "drfone_tooling", "chrome", "icloud_cloudkit",
             "home_library", "desktop", "documents", "downloads", "movies",
             "music", "pictures", "other"]
    state_rows = []
    for name in order:
        b = buckets.get(name)
        if not b:
            continue
        note = {
            "spotlight": "Spotlight index stores under the HFS+ volume",
            "document_revisions": "DocumentRevisions-V100 version stores",
            "hfs_journal": "HFS+ journal and journal info block",
            "efi_partition": "EFI System Partition FAT32 records",
            "gpt_structural": "GPT headers, entry arrays, protective MBR",
            "volume_structural": "Volume-root structural records below Untitled",
            "090_diagnostics": "Desktop 090-[] wireless/system diagnostics capture",
            "mail": "Mail and .emlx stores under home Library",
            "photos": "Photos Library objects and proxies",
            "drfone_tooling": "DrFone application-support tooling",
            "chrome": "Google Chrome profile data",
            "icloud_cloudkit": "iCloud/CloudKit placeholders and state",
            "home_library": "Remaining home Library system/application state",
            "desktop": "Home Desktop files",
            "documents": "Home Documents",
            "downloads": "Home Downloads",
            "movies": "Home Movies",
            "music": "Home Music",
            "pictures": "Home Pictures",
            "other": "Remaining inventory rows",
        }.get(name, "")
        state_rows.append((name, b["n"], b["bytes"], b["hashes"], note))
    state_out = write_single(vol_dir, "03_volume_system_state.tsv",
                             ["system_area", "object_count", "size_bytes",
                              "hash_count", "note"], state_rows)

    acq_out = write_single(disk_dir, "01_acquisition.tsv",
                           ["field", "value"], sorted(acq.items()))

    partition_rows = [
        ("GPT disk", "GUID", acq.get("disk_guid"), "", "entire device GUID"),
        ("EFI System Partition", "GUID",
         acq.get("efi_partition_guid"), "",
         "small EFI FAT32 partition (VBR + FAT tables + unallocated)"),
        ("HFS+ data partition", "GUID",
         acq.get("hfs_partition_guid"),
         int(acq.get("hfs_sector_offset") or 0) * int(acq.get("sector_size") or 512),
         f"named Untitled; journaled HFS+; sector offset "
         f"{acq.get('hfs_sector_offset')}"),
    ]
    pm_out = write_single(disk_dir, "02_partition_map.tsv",
                          ["partition", "type", "guid", "byte_start", "note"],
                          partition_rows)

    disk_rows = [
        ("drive_model", acq.get("drive_model")),
        ("drive_serial", acq.get("drive_serial")),
        ("disk_guid", acq.get("disk_guid")),
        ("volume_identifier", acq.get("volume_identifier")),
        ("acquisition_tool", acq.get("acquisition_tool")),
        ("case_number", acq.get("case_number")),
        ("reported_at", acq.get("reported_at")),
        ("manifest_source", acq.get("manifest_source")),
        ("image_md5", acq.get("image_md5")),
        ("image_sha1", acq.get("image_sha1")),
        ("image_size_bytes", acq.get("image_size_bytes")),
    ]
    disk_out = write_single(disk_dir, "03_disk_identity.tsv",
                            ["field", "value"], disk_rows)

    section_manifest(vol_dir, [
        ("01_volume_identity.tsv", len(identity)),
        ("02_volume_metadata.tsv", len(vol_rows)),
        ("03_volume_system_state.tsv", len(state_rows)),
    ], source_rows={"vol_objects": len(vol_objects), "all_files": len(all_files)})
    section_manifest(disk_dir, [
        ("01_acquisition.tsv", len(acq)),
        ("02_partition_map.tsv", len(partition_rows)),
        ("03_disk_identity.tsv", len(disk_rows)),
    ], source_rows={"acquisition_rows": 1})
    print(f"volume objects: {len(vol_rows):,}")
    print(f"system-state buckets: {len(state_rows)}")


if __name__ == "__main__":
    main()
