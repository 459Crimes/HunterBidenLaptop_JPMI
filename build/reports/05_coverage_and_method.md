# Coverage And Method

## 1. Source boundary

- Source ID **122** `JPMI Metadata HB-FileList-2022-04-v1`.
- The project holds metadata/hash reports, not JPMI device bytes.
- Inventory in PostgreSQL: `roberthunter` home directory plus GPT/EFI/HFS+ structural records. System/Application/usr trees are not byte-accessible from this source.

## 2. Coverage figures


| Metric | Value |
|---|---|
| inventory_paths | 576,249 |
| inventory_paths_with_sha256 | 331,906 |
| hash_manifest_rows (rank-1 allpaths) | 655,330 |
| cnid_map_entries | 397,440 |
| tsk_timeline_rows | 1,259,300 |
| home_counts_emlx_vcf_icloud | 128,847 / 77,891 / 12,911 |
| cross_source_hash_overlap_rows | 292,667 |
| cross_source_path_overlap_rows | 461,450 |


## 3. Size policy applied

- Per-file budget: 52,428,800 bytes (8 MiB), hard cap 20 MiB.
- Every export is sharded under the budget; `90_validate_exports.py` regenerates `manifest.tsv` + `manifest.sha256` and fails on any violation.
- `build/deep/` opt-in exports are gitignored.

## 4. Limitations

- JPMI SHA-256 values identify the objects in the manifest, not bytes this project can re-read.
- The TSK timeline (rank-5) is present as a row count; the ingestion did not parse mtime into `jpmi_tsk_timeline`, so timeline analysis uses `jpmi_file_times`.
- Exact-byte cross-source matches are leads; mounting the readable APFS/GAI sources is required for content-level confirmation.
- No source evidence was modified. The pipeline performs read-only PostgreSQL queries and writes only under `build/`.

