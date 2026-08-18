# Catalog: forensic reports

> Human-readable summaries derived from the same JPMI reporting as the TSVs. Parent: [Evidence catalog](README.md).

Folder: [`build/reports/`](../../build/reports/)

Each generated technical report is written as **observation → interpretation → limitation**.

| File | What it is | Linked from |
|---|---|---|
| [`01_computer_information.md`](../../build/reports/01_computer_information.md) | Device/diagnostic path rows (`roberts-MacBook-Air`, serial `C02S953UH3QF`, …) | [The Mac Shop](../THE_MAC_SHOP.md) · [Contents census](../CONTENTS_CENSUS.md) |
| [`02_os_version.md`](../../build/reports/02_os_version.md) | Environment / OS rollup | [What is on the copy](../04_what_is_on_the_copy.md) |
| [`03_known_datetime_stamps_of_use.md`](../../build/reports/03_known_datetime_stamps_of_use.md) | Published copy of the sourced 2019–2020 narrative | Canonical text: [Timeline and handling](../06_timeline_and_handling.md) |
| [`04_post_2019_03_31_timeline.md`](../../build/reports/04_post_2019_03_31_timeline.md) | **141** post-repair **modified** rows (Finder, Spotlight, DocumentRevisions, …) | [Integrity](../INTEGRITY.md) · [Timeline index](../TIMELINE.md) |
| [`05_coverage_and_method.md`](../../build/reports/05_coverage_and_method.md) | Path / CNID / hash / TSK-event universes | [Forensic image](../FORENSIC_IMAGE.md) |

## How to use the post-repair timeline

When an article says later activity is metadata-dominated, the row set is [`04_post_2019_03_31_timeline.md`](../../build/reports/04_post_2019_03_31_timeline.md). Year buckets: 11 (2019), 18 (2020), 82 (2022), 30 (2024).

Edit the sourced chronology in [`docs/06_timeline_and_handling.md`](../06_timeline_and_handling.md). The `03_known_datetime_stamps_of_use.md` copy exists so the narrative sits next to the generated reports.
