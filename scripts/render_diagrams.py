#!/usr/bin/env python3
"""Render docs/diagrams/*.mmd to SVG and JPG via mermaid-cli."""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIAGRAMS = ROOT / "docs" / "diagrams"
CONFIG = DIAGRAMS / "mermaid.json"


def mmdc() -> list[str]:
    local = shutil.which("mmdc")
    if local:
        return [local]
    npx = shutil.which("npx")
    if not npx:
        raise SystemExit("need mmdc or npx")
    return [npx, "-y", "@mermaid-js/mermaid-cli"]


def magick() -> list[str] | None:
    for name in ("magick", "convert"):
        p = shutil.which(name)
        if p:
            return [p]
    return None


def main() -> None:
    cmd = mmdc()
    conv = magick()
    for mmd in sorted(DIAGRAMS.glob("*.mmd")):
        svg = mmd.with_suffix(".svg")
        png = mmd.with_suffix(".png")
        jpg = mmd.with_suffix(".jpg")
        subprocess.run(
            cmd
            + [
                "-i",
                str(mmd),
                "-o",
                str(svg),
                "-b",
                "white",
                "-c",
                str(CONFIG),
                "-s",
                "2",
            ],
            check=True,
        )
        subprocess.run(
            cmd
            + [
                "-i",
                str(mmd),
                "-o",
                str(png),
                "-b",
                "white",
                "-c",
                str(CONFIG),
                "-s",
                "2",
            ],
            check=True,
        )
        if conv:
            subprocess.run(
                conv + [str(png), "-background", "white", "-flatten", str(jpg)],
                check=True,
            )
        else:
            # Chromium PNG is the raster fallback if ImageMagick is absent.
            shutil.copyfile(png, jpg)
        png.unlink(missing_ok=True)
        print(f"rendered {mmd.stem}")


if __name__ == "__main__":
    main()
