# Article index

This directory is the **JPMI encyclopedia**: everything this project currently knows—and explicitly does not know—about the disk lineage that came from John Paul Mac Isaac's repair shop.

Main article: [README](../README.md).

## How to use this like Wikipedia

- **Lead articles** answer “what is this object?”
- **Event articles** answer “what happened when?”
- **Hardware / image articles** answer “what physical and forensic objects exist?”
- **Census articles** answer “what populations are on the volume?”
- **Method articles** answer “how was this published, and what can it prove?”
- Every strong sentence should have a **source class**. If it does not, it does not belong in the lead.

## Portal

| If you want… | Read |
|---|---|
| A one-page definition | [What is JPMI?](01_what_is_jpmi.md) |
| Who / what / when / where / why / how | [Provenance — 5 Ws](02_provenance_5ws.md) |
| The custody story as a chain | [Chain of custody](03_chain_of_custody.md) |
| The full sourced chronology | [Timeline and handling](06_timeline_and_handling.md) · [Timeline index](TIMELINE.md) |
| Who wrote this encyclopedia | [Author](AUTHOR.md) |
| Who the people are (father, uncle, FBI agents, Della Rocca, Apelbaum) | [People](PEOPLE.md) |
| Yaacov Apelbaum / XRVision | [Apelbaum](APELBAUM.md) |
| Attempt to get a copy to Tucker Carlson at Fox | [Fox / Tucker](FOX_TUCKER.md) |
| Marco Polo 4th printing (shop/FBI extract only) | [Marco Polo v4](MARCO_POLO.md) |
| Photos of the men and the shop (links only) | [Portraits and premises](PORTRAITS.md) |
| Signed quote, invoice email, FBI subpoena photos | [Exhibits](EXHIBITS.md) |
| House Judiciary / Oversight laptop reports | [Congressional reports](CONGRESS.md) |
| The shop address and three laptops | [The Mac Shop](THE_MAC_SHOP.md) |
| How many copies and which is which | [Copy lineages](COPY_LINEAGES.md) |
| The USB SSD in the acquisition record | [Crucial X6](CRUCIAL_X6.md) |
| The HFS+ volume `Untitled` | [HFS+ volume Untitled](HFS_VOLUME_UNTITLED.md) |
| The E01 and hashes | [Forensic image](FORENSIC_IMAGE.md) |
| The Della Rocca → Sanders shipment | [Mailing packet](MAILING_PACKET.md) |
| File populations | [What is on the copy](04_what_is_on_the_copy.md) · [Contents census](CONTENTS_CENSUS.md) |
| GPT, HFS+, CNID, Spotlight | [Filesystem for non-experts](05_filesystem_for_non_experts.md) · [Glossary](GLOSSARY.md) |
| Created / modified / accessed clusters | [Timestamps](TIMESTAMPS.md) |
| Tampering / injection / CBS / 0728 boundary | [Integrity](INTEGRITY.md) · [Scope](SCOPE.md) |
| The 2022 E01 vs 2024 last-write | [2022/2024 discrepancy](2022_2024_DISCREPANCY.md) |
| What this repo is *not* | [Scope](SCOPE.md) |
| What remains unproved | [Limits and open questions](07_limits_and_open_questions.md) |
| Which source supports which claim | [Source matrix](09_source_matrix.md) · [Bibliography](BIBLIOGRAPHY.md) |
| How tables are generated | [Reproducibility](08_reproducibility.md) · [Architecture](../ARCHITECTURE.md) · [Data contract](../DATA_CONTRACT.md) |
| House rules for wording | [Manual of Style](MANUAL_OF_STYLE.md) |
| Project checklist | [STATUS](../STATUS.md) · [TASKS](../TASKS.md) |

## Numbered narrative (stable IDs)

These nine files are the original public-narrative sequence. Stage 55 of the build republishes `06` as `build/reports/03_known_datetime_stamps_of_use.md`. Those IDs are stable in this repository.

| ID | Article |
|---|---|
| 01 | [What is JPMI?](01_what_is_jpmi.md) |
| 02 | [Provenance — 5 Ws](02_provenance_5ws.md) |
| 03 | [Chain of custody](03_chain_of_custody.md) |
| 04 | [What is on the copy](04_what_is_on_the_copy.md) |
| 05 | [Filesystem for non-experts](05_filesystem_for_non_experts.md) |
| 06 | [Timeline and handling](06_timeline_and_handling.md) |
| 07 | [Limits and open questions](07_limits_and_open_questions.md) |
| 08 | [Reproducibility](08_reproducibility.md) |
| 09 | [Source matrix](09_source_matrix.md) |

## Machine-readable appendices

| Path | What it is |
|---|---|
| [`build/disk_info/`](../build/disk_info/) | Device, image, partition identity |
| [`build/volume_info/`](../build/volume_info/) | HFS+ volume and system-state objects |
| [`build/file_tree/`](../build/file_tree/) | Directory / home rollups |
| [`build/hash_manifest/`](../build/hash_manifest/) | SHA-256 identities (JPMI-only) |
| [`build/metadata/`](../build/metadata/) | Time, extension, type, CNID, alias summaries |
| [`build/reports/`](../build/reports/) | Generated forensic summaries |
| [`build/archives/`](../build/archives/) | Partitioned deep metadata |

## Categories

- **Provenance:** 02, 03, 06, 09, PEOPLE, AUTHOR, PORTRAITS, THE_MAC_SHOP, EXHIBITS, CONGRESS, COPY_LINEAGES, MAILING_PACKET
- **Storage objects:** CRUCIAL_X6, HFS_VOLUME_UNTITLED, FORENSIC_IMAGE
- **Contents:** 04, CONTENTS_CENSUS, 05, GLOSSARY, TIMESTAMPS
- **Integrity:** INTEGRITY, 2022_2024_DISCREPANCY, 07, SCOPE
- **Method:** 08, ARCHITECTURE, DATA_CONTRACT, MANUAL_OF_STYLE, SCOPE
