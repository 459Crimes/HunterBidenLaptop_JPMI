#!/usr/bin/env python3
"""Stage 60 — partition the gitignored deep exports into GitHub-trackable archives.

`build/deep/` (full per-file exports, ~769 MiB) is gitignored. This stage turns
each deep section into a partitioned gzip tar archive under `build/archives/`:

  build/archives/deep_<section>_<NNN>.tar.gz.part

Part sizes stay at or below the per-file budget from config/limits.json
(8 MiB), far under the repo hard cap (20 MiB) and GitHub limits. The `.part`
suffix keeps the files outside the repo's global `*.gz` ignore rule.

The stage also verifies the archives before writing the manifest: every part
set is reassembled, decompressed, and every tar member's SHA-256 and byte size
must match the source deep shard. Nothing is written to PostgreSQL.

Layout produced:
  build/archives/README.md
  build/archives/_manifest.tsv        per-part records
  build/archives/deep_<section>_NNN.tar.gz.part
"""
import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import BUILD, load_limits, sha256

ARCHIVES = BUILD / "archives"
DEEP = BUILD / "deep"


class SplitWriter:
    """File-like object that starts a new part file when the budget is hit."""

    def __init__(self, out_dir, stem, part_bytes):
        self.out_dir = out_dir
        self.stem = stem
        self.part_bytes = part_bytes
        self.parts = []
        self.closed = False
        self._idx = 0
        self._fh = None
        self._path = None
        self._size = 0

    def _next(self):
        self._idx += 1
        self._path = self.out_dir / f"{self.stem}_{self._idx:03d}.tar.gz.part"
        self._fh = open(self._path, "wb")
        self._size = 0
        self.parts.append(self._path)

    def write(self, data):
        if self._fh is None or self._size + len(data) > self.part_bytes:
            if self._fh is not None:
                self._fh.close()
            self._next()
        self._fh.write(data)
        self._size += len(data)

    def flush(self):
        if self._fh is not None:
            self._fh.flush()

    def tell(self):
        return self._size

    def close(self):
        if not self.closed:
            if self._fh is not None:
                self._fh.close()
            self.closed = True


def archive_section(section_dir, budget):
    section = section_dir.name
    shards = sorted(section_dir.glob("*.tsv"))
    stem = f"deep_{section}"
    sw = SplitWriter(ARCHIVES, stem, budget)
    with tarfile.open(fileobj=sw, mode="w|gz") as tar:
        for shard in shards:
            ti = tar.gettarinfo(name=shard, arcname=f"{section}/{shard.name}")
            ti.mtime = 0
            ti.uid = 0
            ti.gid = 0
            ti.uname = ""
            ti.gname = ""
            with open(shard, "rb") as fh:
                tar.addfile(ti, fh)
    sw.close()
    parts = sw.parts
    _zero_gzip_mtime(parts[0])
    return parts, shards


def _zero_gzip_mtime(first_part):
    """Zero the gzip MTIME field (RFC 1952 header bytes 4-7) for
    deterministic archive bytes across rebuilds. Readers ignore MTIME."""
    with open(first_part, "r+b") as fh:
        fh.seek(4)
        if fh.read(4) == b"\x00" * 4:
            return
        fh.seek(4)
        fh.write(b"\x00" * 4)


def verify_section(parts, shards, section):
    """Reassemble parts, decompress, and compare every member to its source."""
    cat = ARCHIVES / f"deep_{section}_reassembled.tar.gz"
    if len(parts) == 1:
        cat = parts[0]
    else:
        with open(cat, "wb") as out:
            for part in parts:
                out.write(part.read_bytes())
    try:
        sha = hashlib.sha256()
        with open(cat, "rb") as fh:
            for chunk in iter(lambda: fh.read(1 << 20), b""):
                sha.update(chunk)
        tar_sha = sha.hexdigest()

        expected = {s.name: (sha256(s), s.stat().st_size) for s in shards}
        with tarfile.open(cat, "r:gz") as tar:
            members = tar.getmembers()
            assert len(members) == len(shards), (
                f"{section}: {len(members)} members != {len(shards)} shards")
            for m in members:
                info = tar.extractfile(m)
                if info is None:
                    raise AssertionError(f"{section}: {m.name} has no data")
                h = hashlib.sha256()
                size = 0
                for chunk in iter(lambda: info.read(1 << 20), b""):
                    h.update(chunk)
                    size += len(chunk)
                name = m.name.split("/", 1)[1] if "/" in m.name else m.name
                exp_sha, exp_size = expected[name]
                if h.hexdigest() != exp_sha or size != exp_size:
                    raise AssertionError(
                        f"{section}: {name} mismatch after round-trip")
        return tar_sha
    finally:
        if len(parts) > 1:
            cat.unlink(missing_ok=True)


def main():
    limits = load_limits()
    budget = limits["per_file_budget_bytes"]
    ARCHIVES.mkdir(parents=True, exist_ok=True)
    if not DEEP.exists():
        print("no build/deep/ present; nothing to archive")
        return

    sections = sorted(d for d in DEEP.iterdir() if d.is_dir())
    records = []
    for section_dir in sections:
        section = section_dir.name
        parts, shards = archive_section(section_dir, budget)
        tar_sha = verify_section(parts, shards, section)
        for i, part in enumerate(parts, 1):
            records.append({
                "set": f"deep_{section}",
                "part_index": i,
                "part_count": len(parts),
                "part_file": f"archives/{part.name}",
                "part_size": part.stat().st_size,
                "part_sha256": sha256(part),
                "set_tar_sha256": tar_sha,
                "source_shards": len(shards),
                "source_section": f"deep/{section}",
            })
        print(f"{section}: {len(shards)} shards -> {len(parts)} part(s), "
              f"tar.gz sha256 {tar_sha[:16]}…")

    header = ["set", "part_index", "part_count", "part_file", "part_size",
              "part_sha256", "set_tar_sha256", "source_shards",
              "source_section"]
    with open(ARCHIVES / "_manifest.tsv", "w", newline="", encoding="utf-8") as fh:
        fh.write("\t".join(header) + "\n")
        for r in records:
            fh.write("\t".join(str(r[h]) for h in header) + "\n")

    (ARCHIVES / "README.md").write_text(
        "# Deep Export Archives (partitioned)\n\n"
        "`build/deep/` is intentionally gitignored (full per-file exports, "
        f"~{sum(p.stat().st_size for p in DEEP.rglob('*.tsv')) // 1024 // 1024}"
        " MiB). These parts are the GitHub-trackable form.\n\n"
        "## Reassembly\n\n"
        "For each set, concatenate parts then extract (or stream directly):\n\n"
        "```\n"
        "cat deep_<section>_*.tar.gz.part > deep_<section>.tar.gz\n"
        "tar tzf deep_<section>.tar.gz      # list\n"
        "tar xzf deep_<section>.tar.gz      # extract\n"
        "```\n\n"
        "Extraction recreates `deep/<section>/<shard>.tsv`.\n\n"
        "## Integrity\n\n"
        f"- Every part is at or below the {budget // 1024 // 1024} MiB "
        "per-file budget (repo hard cap from `config/limits.json`) — verified "
        "by `90_validate_exports.py` and the pre-commit hook.\n"
        "- Each part is recorded in `_manifest.tsv` with size and SHA-256.\n"
        "- Each set's `set_tar_sha256` covers the full reassembled `.tar.gz`; "
        "`90_validate_exports.py` regenerates and cross-checks this file.\n"
        "- Reassembly is tested at build time: every member of every set is "
        "decompressed and byte-compared (SHA-256 + size) to its source shard "
        "in `build/deep/`.\n"
        "- Archives are deterministic: tar members carry zeroed mtime/uid/gid "
        "and the gzip MTIME field is zeroed, so identical source shards "
        "reproduce byte-identical parts across rebuilds.\n"
        "- `build/deep/` itself stays local and gitignored; the archive is the "
        "published version.\n")

    print(f"archived {len(sections)} sections into {len(records)} parts under "
          f"{ARCHIVES.relative_to(BUILD.parent)}")


if __name__ == "__main__":
    main()
