#!/usr/bin/env python3
"""Shared helpers for the JPMI source-analysis build pipeline.

Read-only against PostgreSQL. Writes sharded, budget-bounded TSV exports.
"""
import csv
import hashlib
import json
import os
from pathlib import Path

import psycopg2

ROOT = Path(__file__).resolve().parent.parent.parent  # subproject root
BUILD = ROOT / "build"
CONFIG = ROOT / "config" / "limits.json"

DEFAULT_DSN = "dbname=rhb_forensics"

# Published corpus roots. Inventory rows still store jpmi_metadata/ in
# PostgreSQL; exports and citations rewrite that prefix to JPMI://.
SOURCE_URI = {
    "JPMI": "JPMI://",
    "APFS": "APFS://",
    "GAI": "GAI://",
    "0728": "0728://",
}
INVENTORY_ROOT = "jpmi_metadata"


def to_source_uri(path, source="JPMI"):
    """Map an inventory path onto the published source URI.

    jpmi_metadata/Users/roberthunter/Desktop/.DS_Store becomes
    JPMI://Users/roberthunter/Desktop/.DS_Store. Already-schemed paths
    (APFS://, GAI://, 0728://, JPMI://) are left unchanged.
    """
    if path is None:
        return None
    s = str(path)
    if s == "":
        return s
    for scheme in SOURCE_URI.values():
        if s.startswith(scheme):
            return s
    scheme = SOURCE_URI[source]
    prefix = INVENTORY_ROOT + "/"
    if s in (INVENTORY_ROOT, prefix):
        return scheme
    if s.startswith(prefix):
        return scheme + s[len(prefix):]
    return s


def inventory_relpath(path):
    """Strip JPMI:// or the jpmi_metadata/ inventory prefix for matching."""
    if path is None:
        return ""
    s = str(path)
    if s.startswith(SOURCE_URI["JPMI"]):
        return s[len(SOURCE_URI["JPMI"]):]
    prefix = INVENTORY_ROOT + "/"
    if s.startswith(prefix):
        return s[len(prefix):]
    if s in (INVENTORY_ROOT, SOURCE_URI["JPMI"]):
        return ""
    return s


def dsn():
    return os.environ.get("RHB_PG_DSN", DEFAULT_DSN)


def connect():
    return psycopg2.connect(dsn())


def load_limits():
    with open(CONFIG) as fh:
        return json.load(fh)


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


class Sink:
    """Writes tab-separated rows into numbered shards under a byte budget.

    The first line of every shard is the header. Shard boundaries fall between
    rows. Returns (files, total_rows) on close().
    """

    def __init__(self, out_dir, stem, header, budget, prefix="", pad=5):
        self.out_dir = Path(out_dir)
        self.out_dir.mkdir(parents=True, exist_ok=True)
        self.stem = stem
        self.header = header
        self.budget = budget
        self.prefix = prefix
        self.pad = pad
        self.files = []
        self.total_rows = 0
        self._fh = None
        self._path = None
        self._bytes = 0
        self._index = 0

    def _start(self):
        self._index += 1
        name = f"{self.stem}_{self._index:0{self.pad}d}.tsv"
        self._path = self.out_dir / (self.prefix + name)
        self._fh = open(self._path, "w", newline="", encoding="utf-8")
        line = "\t".join(self.header) + "\n"
        self._fh.write(line)
        self._bytes = len(line.encode("utf-8"))

    def row(self, values):
        line = "\t".join(str(v) if v is not None else "" for v in values) + "\n"
        size = len(line.encode("utf-8"))
        if self._fh is None:
            self._start()
        elif self._bytes + size > self.budget:
            self._fh.close()
            self.files.append((self._path, self._bytes))
            self._start()
        self._fh.write(line)
        self._bytes += size
        self.total_rows += 1

    def write_many(self, rows):
        for r in rows:
            self.row(r)

    def close(self):
        if self._fh is not None:
            self._fh.close()
            self.files.append((self._path, self._bytes))
            self._fh = None
        return self.files, self.total_rows


def write_single(out_dir, name, header, rows):
    out_dir = Path(out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / name
    with open(path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        w.writerows(rows)
    return path, len(rows)


def tsv_data_rows(path):
    n = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for _ in csv.reader(fh, delimiter="\t"):
            n += 1
    return max(n - 1, 0)


def section_manifest(out_dir, outputs, source_rows=None):
    """Write a per-section manifest recording produced files and row counts.

    Each output name may refer to a single file or to a Sink's shard stem
    (e.g. `01_stem.tsv` for `01_stem_00001.tsv`, ...). Shards are expanded
    into one record per physical file; data rows are counted from the file
    itself so the manifest is self-consistent.
    """
    out_dir = Path(out_dir)
    records = []
    for name, _rows in outputs:
        if name.startswith("("):
            continue
        paths = [out_dir / name]
        if not paths[0].exists() and name.endswith(".tsv"):
            shards = sorted(out_dir.glob(name[:-4] + "_[0-9]*.tsv"))
            paths = shards
        for path in paths:
            records.append({
                "file": str(path.relative_to(BUILD)),
                "rows": tsv_data_rows(path),
                "size": path.stat().st_size,
                "sha256": sha256(path),
            })
    manifest = {
        "section": out_dir.name,
        "source_rows": source_rows or {},
        "files": records,
    }
    with open(out_dir / "_manifest.json", "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, sort_keys=True)
    return manifest


def null(x):
    return None if x is None or x == "" else x
