#!/usr/bin/env python3
"""Stage 55 — publish the sourced public JPMI custody timeline.

Stage 50 produces database-derived technical reports. This stage intentionally
replaces the legacy datetime report with the sourced public narrative from
`docs/06_timeline_and_handling.md`, so a normal rebuild cannot silently erase
the 2019-2020 court/news custody history or the bounded no-injection finding.

The underlying machine-readable timestamp distributions remain in
`build/metadata/01_time_distribution.tsv` and the complete post-repair row set
remains in `build/reports/04_post_2019_03_31_timeline.md`.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "docs" / "06_timeline_and_handling.md"
TARGET = ROOT / "build" / "reports" / "03_known_datetime_stamps_of_use.md"


def main():
    body = SOURCE.read_text(encoding="utf-8")
    notice = (
        "<!-- GENERATED/PUBLISHED BY scripts/55_publish_custody_timeline.py. "
        "Edit docs/06_timeline_and_handling.md, not this generated copy. -->\n\n"
    )
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(notice + body, encoding="utf-8")
    print(f"published sourced custody timeline: {TARGET}")


if __name__ == "__main__":
    main()
