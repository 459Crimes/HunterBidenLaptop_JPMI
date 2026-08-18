#!/usr/bin/env python3
"""Stage 10 — file tree.

Builds the hierarchical inventory tree from the JPMI metadata inventory
(`files` source 122 + `jpmi_file_times`) and writes:

  build/file_tree/01_directory_tree.tsv   (recursive subtree rollups per dir)
  build/file_tree/02_top_level_summary.tsv
  build/file_tree/03_home_overview.tsv
  build/deep/file_tree_full/              (opt-in full per-file listing)

Read-only against PostgreSQL.
"""
import json
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from lib.common import (BUILD, INVENTORY_ROOT, Sink, connect, load_limits,
                        section_manifest, sha256, to_source_uri, write_single)

QUERY = """
SELECT f.relative_path, f.size, f.sha256, t.modified_ts
FROM files f
JOIN jpmi_file_times t ON t.file_id = f.id
WHERE f.source_id = 122
ORDER BY f.relative_path
"""


def main():
    limits = load_limits()
    budget = limits["per_file_budget_bytes"]
    deep = limits["deep_exports"]
    pg = connect()
    rows = []
    with pg.cursor() as c:
        c.execute(QUERY)
        rows = c.fetchall()
    pg.close()

    parent_direct = defaultdict(lambda: {
        "file_count": 0, "size": 0, "hash_count": 0, "min_m": None, "max_m": None,
    })
    dirs_set = set()
    child_dir_sets = defaultdict(set)

    deep_sink = None
    if deep:
        deep_dir = BUILD / "deep" / "file_tree_full"
        deep_sink = Sink(deep_dir, "files", ["relative_path", "size", "sha256",
                                             "modified_ts"], budget)

    for rel_path, size, sha, mtime in rows:
        parts = [p for p in rel_path.rstrip("/").split("/") if p]
        if not parts:
            continue
        if rel_path.endswith("/"):
            dirs_set.add("/".join(parts))
            continue
        mtime_s = mtime.strftime("%Y-%m-%d %H:%M:%S") if mtime else None
        if deep_sink:
            deep_sink.row((to_source_uri(rel_path), size or "", sha or "",
                           mtime_s or ""))
        parent = "/".join(parts[:-1])
        d = parent_direct[parent]
        d["file_count"] += 1
        if size:
            d["size"] += size
        if sha:
            d["hash_count"] += 1
        if mtime:
            if d["min_m"] is None or mtime < d["min_m"]:
                d["min_m"] = mtime
            if d["max_m"] is None or mtime > d["max_m"]:
                d["max_m"] = mtime
        for i in range(1, len(parts)):
            dirs_set.add("/".join(parts[:i]))
        for i in range(1, len(parts) - 1):
            child_dir_sets["/".join(parts[:i])].add(parts[i])

    dir_count = {d: len(child_dir_sets[d]) for d in dirs_set}

    rec = {}
    for d in dirs_set:
        sd = parent_direct[d]
        rec[d] = {
            "file_count": sd["file_count"], "size": sd["size"],
            "hash_count": sd["hash_count"],
            "min_m": sd["min_m"], "max_m": sd["max_m"],
        }
    for d in sorted(dirs_set, key=lambda x: -x.count("/")):
        if "/" not in d:
            continue
        parent = d.rsplit("/", 1)[0]
        r, p = rec[d], rec[parent]
        p["file_count"] += r["file_count"]
        p["size"] += r["size"]
        p["hash_count"] += r["hash_count"]
        if r["min_m"] and (p["min_m"] is None or r["min_m"] < p["min_m"]):
            p["min_m"] = r["min_m"]
        if r["max_m"] and (p["max_m"] is None or r["max_m"] > p["max_m"]):
            p["max_m"] = r["max_m"]

    tree_rows = []
    for d in sorted(dirs_set):
        r = rec[d]
        depth = d.count("/")
        parent = d.rsplit("/", 1)[0] if "/" in d else ""
        pct = (round(100.0 * r["hash_count"] / r["file_count"], 1)
               if r["file_count"] else 0.0)
        tree_rows.append((to_source_uri(d), depth,
                          to_source_uri(parent) if parent else "",
                          dir_count[d], r["file_count"],
                          r["size"], r["hash_count"], pct,
                          r["min_m"].strftime("%Y-%m-%d %H:%M:%S") if r["min_m"] else "",
                          r["max_m"].strftime("%Y-%m-%d %H:%M:%S") if r["max_m"] else ""))

    tree_out = write_single(
        BUILD / "file_tree", "01_directory_tree.tsv",
        ["path", "depth", "parent_path", "dir_count", "file_count",
         "size_bytes", "hash_count", "hash_pct", "min_modified_ts",
         "max_modified_ts"], tree_rows)

    def subtree(path):
        r = rec.get(path)
        if not r:
            return None
        pct = (round(100.0 * r["hash_count"] / r["file_count"], 1)
               if r["file_count"] else 0.0)
        return (r["file_count"], r["size"], r["hash_count"], pct,
                r["min_m"].strftime("%Y-%m-%d %H:%M:%S") if r["min_m"] else "",
                r["max_m"].strftime("%Y-%m-%d %H:%M:%S") if r["max_m"] else "")

    top_keys = {}
    home_keys = {}
    for parent, d in parent_direct.items():
        parts = parent.split("/")
        if len(parts) >= 2:
            top_keys[parts[1]] = None
        if len(parts) >= 3 and parts[1] == "Users" and parts[2] == "roberthunter":
            home_keys[parts[3] if len(parts) > 3 else ""] = None
    top_rows = [(k, *subtree(f"{INVENTORY_ROOT}/{k}"))
                for k in sorted(top_keys) if k]
    home_rows = [(k, *subtree(f"{INVENTORY_ROOT}/Users/roberthunter/{k}"))
                 for k in sorted(home_keys) if k]

    top_out = write_single(
        BUILD / "file_tree", "02_top_level_summary.tsv",
        ["top_path", "file_count", "size_bytes", "hash_count", "hash_pct",
         "min_modified_ts", "max_modified_ts"], top_rows)
    home_out = write_single(
        BUILD / "file_tree", "03_home_overview.tsv",
        ["home_subdir", "file_count", "size_bytes", "hash_count", "hash_pct",
         "min_modified_ts", "max_modified_ts"], home_rows)

    outputs = [
        ("01_directory_tree.tsv", len(tree_rows)),
        ("02_top_level_summary.tsv", len(top_rows)),
        ("03_home_overview.tsv", len(home_rows)),
    ]
    if deep_sink:
        deep_files, deep_rows = deep_sink.close()
        deep_manifest = {
            "section": "deep/file_tree_full",
            "rows": deep_rows,
            "files": [{"file": str(p.relative_to(BUILD)), "size": s,
                       "sha256": sha256(p)} for p, s in deep_files],
        }
        (BUILD / "deep" / "file_tree_full" / "_manifest.json").write_text(
            json.dumps(deep_manifest, indent=2, sort_keys=True))
        outputs.append(("(deep/file_tree_full)", deep_rows))
    section_manifest(BUILD / "file_tree", outputs,
                     source_rows={"query_rows": len(rows)})

    print(f"directory rows: {len(tree_rows):,}")
    print(f"top-level rows: {len(top_rows):,}")
    print(f"home overview rows: {len(home_rows):,}")
    if deep_sink:
        print(f"deep file rows: {deep_rows:,} in {len(deep_files)} shards")


if __name__ == "__main__":
    main()
