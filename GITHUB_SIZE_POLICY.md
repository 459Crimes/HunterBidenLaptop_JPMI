# GitHub Size Policy (Conservative)

## Limits reference

| Boundary | Value | Source |
|---|---|---|
| GitHub hard per-file limit | 100 MB | GitHub |
| GitHub per-file warning | > 50 MB | GitHub |
| Repository pre-commit hook | 50 MB (50 * 1024 * 1024 B) | `.githooks/pre-commit` |
| **This project's per-file budget (default)** | **50 MiB (52,428,800 B)** | `config/limits.json` |
| **This project's hard cap (fail-safe)** | **90 MiB (94,371,840 B)** | `config/limits.json` |

The budget matches the conservative 50 MB posture: every committed file is
kept at or below 50 MiB, well under GitHub's 100 MB hard limit. The 90 MiB
hard cap is a static fail-safe ceiling; the sharding rules below mean it
should never be reached in practice.

## Sharding rule

Any export whose estimated size would exceed the per-file budget is written as
numbered shards:

```
artifact_name_00001.tsv
artifact_name_00002.tsv
...
```

Each shard is opened with the same header row. Shard boundaries are aligned to
row boundaries (no row is split across files). The `deep/` variants are produced
with the same budget.

## Enforcement

`90_validate_exports.py`:

1. Walks every file under `build/` (excluding the gitignored `deep/` tree).
2. Fails if any file exceeds the **budget** (50 MiB).
3. Cross-checks `archives/_manifest.tsv`: every archive part must exist, be at
   or below the budget, and match its recorded size and SHA-256.
4. Recomputes SHA-256 for every file into `build/manifest.tsv` and
   `build/manifest.sha256`.
5. Cross-checks recorded row counts against the per-section manifests and
   fails on mismatch.

Separately, the repository pre-commit hook (`.githooks/pre-commit`) rejects
any staged file over 50 MB (LFS-exempt), so the commit gate and the export
validator agree.

## What is not published

- `build/deep/` — full-volume per-file exports (file tree full, per-path hashes,
  full file times, full alias/CNID maps). These are generated for local analysis
  and excluded from git via the subproject `.gitignore`. Their full content is
  published in partitioned form under `build/archives/`.
- PostgreSQL/SQLite databases (`*.sqlite`, `*.db`) — excluded by the repository
  `.gitignore`.
- Source bytes — never shipped.
