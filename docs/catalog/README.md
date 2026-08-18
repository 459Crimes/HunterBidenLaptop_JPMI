# Evidence catalog

This encyclopedia publishes **derived forensic tables and reports**, not the restricted E01 or user-file bytes. Each catalog page lists one family of files, what it measures, and how it relates to the articles.

Checksums for every published `build/` object: [`build/manifest.tsv`](../../build/manifest.tsv) · [`build/manifest.sha256`](../../build/manifest.sha256).

| Catalog | What it covers | Typical articles |
|---|---|---|
| [Disk identity](disk_info.md) | Custody device, E01, GPT partitions | [Crucial X6](../CRUCIAL_X6.md) · [Forensic image](../FORENSIC_IMAGE.md) |
| [Volume identity](volume_info.md) | HFS+ `Untitled`, journal, Spotlight, system-area rollups | [HFS+ volume Untitled](../HFS_VOLUME_UNTITLED.md) |
| [File tree](file_tree.md) | Directory and home-folder counts (576,249 inventory paths) | [What is on the copy](../04_what_is_on_the_copy.md) · [Contents census](../CONTENTS_CENSUS.md) |
| [Hash manifest](hash_manifest.md) | SHA-256 by CNID; coverage metrics | [Forensic image](../FORENSIC_IMAGE.md) · [Integrity](../INTEGRITY.md) |
| [Metadata](metadata.md) | Time, extension, type, permission, CNID, alias summaries | [Timestamps](../TIMESTAMPS.md) · [Copy method](../COPY_METHOD.md) |
| [Reports](reports.md) | Human-readable forensic summaries | [Timeline](../TIMELINE.md) · [Integrity](../INTEGRITY.md) |
| [Deep archives](archives.md) | Partitioned full-volume metadata (not source bytes) | [How to verify](../08_reproducibility.md) |
| [Exhibits](exhibits.md) | Court/shop/FBI scans, mailing packet, transcripts | [Exhibits](../EXHIBITS.md) · [Mailing packet](../MAILING_PACKET.md) |

## How to read a table

TSV files are UTF-8, tab-separated, with a header row. Shards of the same export share columns. Path, CNID, hash, and timestamp are **different identity systems** — see [Glossary](../GLOSSARY.md) and [Sourcing](../MANUAL_OF_STYLE.md).

The articles state a claim in prose. The catalog names the file that holds the rows. The TSV is the appendix.

## What is not here

- The E01 `HB-IMAGE-2022-04-29.E01`
- Individual Mail/Photos/document bytes
- Rebuild scripts and operator notes (local only)
