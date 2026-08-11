#!/usr/bin/env python3
"""Stage 90 — validate and gate the export bundle.

Walks build/ (excluding build/deep/, which is gitignored), then for every
file:

  * enforces the hard size cap,
  * computes SHA-256,
  * counts TSV data rows (header-excluded),
  * cross-checks row counts and sizes against the per-section _manifest.json
    files written by stages 10-40,

and writes:

  build/manifest.tsv        path<TAB>size<TAB>sha256<TAB>rows
  build/manifest.sha256     sha256sum-style digest of manifest.tsv

Exits non-zero on any violation.
"""
import csv
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import BUILD, load_limits, sha256


def tsv_rows(path):
    n = 0
    with open(path, newline="", encoding="utf-8") as fh:
        for _ in csv.reader(fh, delimiter="\t"):
            n += 1
    return max(n - 1, 0)


def walk():
    skip = {BUILD / "deep"}
    skip_files = {BUILD / "manifest.tsv", BUILD / "manifest.sha256"}
    for p in sorted(BUILD.rglob("*")):
        if not p.is_file():
            continue
        if any(s in p.parents for s in skip):
            continue
        if p in skip_files:
            continue
        yield p


def load_section_manifests():
    out = {}
    for p in BUILD.rglob("_manifest.json"):
        if "deep" in p.relative_to(BUILD).parts:
            continue
        try:
            m = json.loads(p.read_text())
        except Exception:
            continue
        out[p.parent] = {rec["file"]: rec for rec in m.get("files", [])}
    return out


def check_archives(rows_meta, budget):
    errors = []
    manifest = BUILD / "archives" / "_manifest.tsv"
    if not manifest.exists():
        return errors
    with open(manifest, newline="", encoding="utf-8") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        for rec in rd:
            rel = rec["part_file"]
            size = int(rec["part_size"])
            digest = rec["part_sha256"]
            if size > budget:
                errors.append(f"{rel}: archive part exceeds budget {budget}")
            if rel not in rows_meta:
                errors.append(f"{rel}: recorded in archives/_manifest.tsv "
                              "but missing")
                continue
            a_size, a_digest, _ = rows_meta[rel]
            if a_size != size:
                errors.append(f"{rel}: size {a_size} != recorded {size}")
            if a_digest != digest:
                errors.append(f"{rel}: sha256 mismatch vs archive manifest")
    return errors


def main():
    limits = load_limits()
    budget = limits["per_file_budget_bytes"]
    manifests = load_section_manifests()

    rows_meta = {}  # rel -> (size, sha256, rows)
    errors = []

    for p in walk():
        rel = str(p.relative_to(BUILD))
        size = p.stat().st_size
        if size > budget:
            errors.append(f"{rel}: size {size} exceeds budget {budget}")
        rows = tsv_rows(p) if p.suffix == ".tsv" else 0
        rows_meta[rel] = (size, sha256(p), rows)

    errors.extend(check_archives(rows_meta, budget))

    for section, records in manifests.items():
        for rel, rec in records.items():
            if rel not in rows_meta:
                errors.append(f"{rel}: recorded in {section}/_manifest.json "
                              "but missing")
                continue
            size, digest, rows = rows_meta[rel]
            if size != rec["size"]:
                errors.append(f"{rel}: size {size} != recorded {rec['size']}")
            if digest != rec["sha256"]:
                errors.append(f"{rel}: sha256 mismatch vs recorded manifest")
            if rows != rec["rows"]:
                errors.append(f"{rel}: data rows {rows} != recorded "
                              f"{rec['rows']}")

    if errors:
        for e in errors:
            print("ERROR", e, file=sys.stderr)
        sys.exit(1)

    header = ["path", "size_bytes", "sha256", "data_rows"]
    manifest_path = BUILD / "manifest.tsv"
    with open(manifest_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(header)
        for rel in sorted(rows_meta):
            size, digest, rows = rows_meta[rel]
            w.writerow([rel, size, digest, rows])
    digest = sha256(manifest_path)
    (BUILD / "manifest.sha256").write_text(f"{digest}  manifest.tsv\n")

    print(f"validated {len(rows_meta)} files; all within caps and consistent")
    print(f"manifest.tsv sha256: {digest}")


if __name__ == "__main__":
    main()
