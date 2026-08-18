# Deep Export Archives (partitioned)

`build/deep/` is intentionally gitignored (full per-file exports, ~751 MiB). These parts are the GitHub-trackable form.

## Reassembly

For each set, concatenate parts then extract (or stream directly):

```
cat deep_<section>_*.tar.gz.part > deep_<section>.tar.gz
tar tzf deep_<section>.tar.gz      # list
tar xzf deep_<section>.tar.gz      # extract
```

Extraction recreates `deep/<section>/<shard>.tsv`.

## Integrity

- Every part is at or below the 50 MiB per-file budget (repo hard cap from `config/limits.json`) — verified by `90_validate_exports.py` and the pre-commit hook.
- Each part is recorded in `_manifest.tsv` with size and SHA-256.
- Each set's `set_tar_sha256` covers the full reassembled `.tar.gz`; `90_validate_exports.py` regenerates and cross-checks this file.
- Reassembly is tested at build time: every member of every set is decompressed and byte-compared (SHA-256 + size) to its source shard in `build/deep/`.
- Archives are deterministic: tar members carry zeroed mtime/uid/gid and the gzip MTIME field is zeroed, so identical source shards reproduce byte-identical parts across rebuilds.
- `build/deep/` itself stays local and gitignored; the archive is the published version.
