# Deep metadata archives (partitioned)

Full per-file exports are too large to keep as loose TSVs in git. The files in this folder are the published, partitioned form.

**Catalog (what each set contains, sizes, reassembly):** [Deep archives](../../docs/catalog/archives.md).

Integrity: each part is listed in [`_manifest.tsv`](_manifest.tsv) with size and SHA-256. The tree-wide checksum list is [`../manifest.tsv`](../manifest.tsv).

These archives are derived JPMI **metadata**. They are not source-image bytes.
