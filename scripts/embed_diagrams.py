#!/usr/bin/env python3
"""Insert mermaid + SVG/JPG links between <!-- diagram:NAME --> markers."""

from __future__ import annotations

from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
DIAGRAMS = ROOT / "docs" / "diagrams"
BEGIN = re.compile(r"<!-- diagram:([a-z0-9_]+) -->")
END = "<!-- /diagram:{name} -->"


def rel_prefix(md_path: Path) -> str:
    if md_path.parent == ROOT:
        return "docs/diagrams"
    if md_path.parent == ROOT / "docs":
        return "diagrams"
    if md_path.parent == ROOT / "build" / "reports":
        return "../../docs/diagrams"
    raise SystemExit(f"no diagram prefix for {md_path}")


def block(name: str, prefix: str) -> str:
    src = (DIAGRAMS / f"{name}.mmd").read_text()
    src = src.strip() + "\n"
    return (
        f"<!-- diagram:{name} -->\n"
        f"```mermaid\n{src}```\n\n"
        f"Export: [SVG]({prefix}/{name}.svg) · [JPG]({prefix}/{name}.jpg)\n"
        f"<!-- /diagram:{name} -->"
    )


def embed_file(md_path: Path) -> bool:
    text = md_path.read_text()
    prefix = rel_prefix(md_path)
    changed = False

    def repl(m: re.Match) -> str:
        nonlocal changed
        name = m.group(1)
        end = END.format(name=name)
        rest = text[m.end() :]
        idx = rest.find(end)
        if idx < 0:
            raise SystemExit(f"{md_path}: missing {end}")
        changed = True
        return block(name, prefix)

    # Replace each begin..end pair from the original text iteratively.
    out = []
    pos = 0
    for m in BEGIN.finditer(text):
        name = m.group(1)
        end = END.format(name=name)
        end_idx = text.find(end, m.end())
        if end_idx < 0:
            raise SystemExit(f"{md_path}: missing {end}")
        out.append(text[pos : m.start()])
        out.append(block(name, prefix))
        pos = end_idx + len(end)
        changed = True
    out.append(text[pos:])
    new = "".join(out)
    if new != text:
        md_path.write_text(new)
        return True
    return changed and False


def main() -> None:
    names = {p.stem for p in DIAGRAMS.glob("*.mmd")}
    updated = []
    for md in list((ROOT / "docs").glob("*.md")) + [ROOT / "README.md"]:
        if md.name == "README.md" and md.parent == DIAGRAMS:
            continue
        raw = md.read_text()
        if "<!-- diagram:" not in raw:
            continue
        for m in BEGIN.finditer(raw):
            if m.group(1) not in names:
                raise SystemExit(f"{md}: unknown diagram {m.group(1)}")
        if embed_file(md):
            updated.append(str(md.relative_to(ROOT)))
    print("embedded:", ", ".join(updated) if updated else "(unchanged)")


if __name__ == "__main__":
    main()
