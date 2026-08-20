#!/usr/bin/env python3
"""Compact SVGs: named copy graph + investigative-materials provenance."""
from pathlib import Path

FONT = "Helvetica, Arial, sans-serif"
EDGE = "#374151"
HOLD_C = "#be185d"

SHOP = ("#dbeafe", "#1d4ed8")
JP = ("#dcfce7", "#15803d")
BOOT = ("#fef3c7", "#b45309")
TRIM = ("#fecaca", "#b91c1c")
GAI_C = ("#ccfbf1", "#0f766e")
TODD_C = ("#ddd6fe", "#5b21b6")
SIDE = ("#f3f4f6", "#111827")
HOLD = ("#fce7f3", "#be185d")
PHONE = ("#e0f2fe", "#0369a1")


def esc(t: str) -> str:
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


class Box:
    def __init__(self, x, y, w, h, lines, fill, stroke, dash=None, sw=1.2):
        self.x, self.y, self.w, self.h = x, y, w, h
        self.lines, self.fill, self.stroke, self.dash, self.sw = lines, fill, stroke, dash, sw

    @property
    def cx(self):
        return self.x + self.w / 2

    @property
    def cy(self):
        return self.y + self.h / 2

    @property
    def right(self):
        return self.x + self.w

    @property
    def bottom(self):
        return self.y + self.h

    def svg(self) -> str:
        dash = ' stroke-dasharray="6 4"' if self.dash else ""
        t = [
            f'<rect x="{self.x:.1f}" y="{self.y:.1f}" width="{self.w:.1f}" height="{self.h:.1f}" '
            f'rx="6" fill="{self.fill}" stroke="{self.stroke}" stroke-width="{self.sw}"{dash}/>'
        ]
        n = len(self.lines)
        lh = 14
        y0 = self.cy - (n - 1) * lh / 2 + 4
        for i, line in enumerate(self.lines):
            weight = "700" if i == 0 else "400"
            size = 13 if i == 0 else 11.5
            t.append(
                f'<text x="{self.cx:.1f}" y="{y0 + i * lh:.1f}" text-anchor="middle" '
                f'font-family="{FONT}" font-size="{size}" font-weight="{weight}" fill="#111">'
                f"{esc(line)}</text>"
            )
        return "\n".join(t)


def cluster(x, y, w, h, title, fill="#f8fafc", stroke="#c7d2fe") -> str:
    return (
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="10" fill="{fill}" '
        f'stroke="{stroke}" stroke-width="1.2"/>\n'
        f'<text x="{x + w / 2:.1f}" y="{y + 18}" text-anchor="middle" font-family="{FONT}" '
        f'font-size="12" font-weight="700" fill="#1e3a5f">{esc(title)}</text>'
    )


def edge(x1, y1, x2, y2, label=None, dashed=False, color=EDGE, sw=1.15, d=None,
         lx=None, ly=None, marker="url(#arrow)"):
    dash = ' stroke-dasharray="5 4"' if dashed else ""
    d = d or f"M{x1:.1f},{y1:.1f} L{x2:.1f},{y2:.1f}"
    parts = [
        f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{sw}"{dash} marker-end="{marker}"/>'
    ]
    if label:
        lines = [ln for part in label.split("\n") for ln in part.split("|") if ln]
        mx = x1 + (x2 - x1) * 0.5 if lx is None else lx
        my = y1 + (y2 - y1) * 0.5 if ly is None else ly
        tw = max(52, max(len(ln) for ln in lines) * 6.15)
        th = 14 + (len(lines) - 1) * 12
        parts.append(
            f'<rect x="{mx - tw / 2:.1f}" y="{my - th / 2:.1f}" width="{tw:.1f}" '
            f'height="{th:.1f}" rx="3" fill="#f3e8ff" opacity="0.94"/>'
        )
        y0 = my - (len(lines) - 1) * 6 + 4
        for i, ln in enumerate(lines):
            parts.append(
                f'<text x="{mx:.1f}" y="{y0 + i * 12:.1f}" text-anchor="middle" font-family="{FONT}" '
                f'font-size="10.5" fill="#111">{esc(ln)}</text>'
            )
    return "\n".join(parts)


# --- shared geometry: SHOP children BOOT01 and JPMI at the same rank ---
laptop = Box(610, 12, 178, 76, ["LAPTOP", "user era to 2019-03", "intake 2019-04-12", "FVFXC2MMHV29"], *SHOP)
shop = Box(594, 118, 210, 66, ["SHOP", "2019-04-12+ store server", "logs not held"], *SHOP)
rhb = Box(1188, 108, 196, 76, ["RHB_WD", "2019-04-13 customer WD", "FBI 2019-12-09", "WX21A19ATFF3"], *SHOP)

boot01 = Box(214, 228, 198, 64, ["BOOT01", "after 2019-09-26", "18G103 OS + home"], *BOOT)
costello = Box(214, 322, 198, 64, ["COSTELLO", "2020-08-26", "boot 2020-08-28..31"], *BOOT)

jpmi = Box(860, 228, 220, 64, ["JPMI Untitled", "2019-09-26/27 home-only", "no OS"], *JP)
cbs = Box(780, 324, 176, 52, ["CBS / CFS", "exact-copy exam 2022"], *JP)

trimarco = Box(28, 448, 186, 64, ["TRIMARCO", "~2020-09-01+", "Burisma Desktop"], *TRIM)
apfs = Box(16, 544, 230, 64, ["APFS HB Boot Drive", "volume 2020-12-12", "CCC 2021-01-05"], *TRIM)
maryman = Box(16, 644, 176, 52, ["MARYMAN", "imaged 2021-04-04"], *TRIM)
gustav = Box(208, 644, 200, 52, ["GUSTAV", "Dimitrelos 2022-05–06"], *TRIM)

blap = Box(500, 448, 196, 64, ["BLAP01", "~2020-09-01+", "no Burisma dump"], *GAI_C)
gai = Box(500, 548, 196, 56, ["GAI Biden Lap 2", "volume 2021-05-17"], *GAI_C)

todd = Box(320, 744, 196, 64, ["TODD", "after 2021-01-05", "altered to boot"], *TODD_C)
hayes = Box(320, 840, 196, 52, ["HAYES", "after 2021-01-05"], *TODD_C)
mpolo = Box(16, 924, 210, 80, ["MPOLO", "Jun 2021", "degraded copy", "missing password vaults"], *TODD_C, dash=True)
apfsstar = Box(248, 932, 256, 64, ["APFS*", "Jun 2022 / MEGA 2022-06-13", "to Marc Aaron DeGiovanni"], *TODD_C)

iphone = Box(780, 704, 500, 80, ["IPHONE", "iPhone backup", "present on all copies"], *PHONE)

hold_kw = dict(color=HOLD_C, sw=1.4, marker="url(#arrow-hold)")

markers = f'''  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{EDGE}"/>
    </marker>
    <marker id="arrow-hold" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="{HOLD_C}"/>
    </marker>
  </defs>'''

lineage_clusters = f'''  {cluster(188, 208, 250, 196, "BOOT01 / Costello — never JPMI", "#fffbeb", "#f59e0b")}
  {cluster(752, 208, 456, 196, "JPMI family — this encyclopedia", "#f0fdf4", "#86efac")}
  {cluster(8, 420, 428, 296, "TRIMARCO group", "#fff1f2", "#fda4af")}
  {cluster(468, 420, 260, 208, "BLAP01 / GAI", "#f0fdfa", "#5eead4")}
  {cluster(8, 720, 516, 300, "Todd-altered copies", "#f5f3ff", "#c4b5fd")}'''

lineage_edges = f'''  {edge(laptop.cx, laptop.bottom, shop.cx, shop.y, "2019-04-12")}
  {edge(shop.right, shop.cy, rhb.x, rhb.cy, "2019-04-13")}
  {edge(shop.x + 36, shop.bottom, boot01.cx, boot01.y, "after 2019-09-26", lx=430, ly=204)}
  {edge(shop.right - 24, shop.bottom, jpmi.cx, jpmi.y, "2019-09-26/27", lx=780, ly=204)}
  {edge(jpmi.cx - 40, jpmi.bottom, cbs.cx, cbs.y)}
  {edge(boot01.cx, boot01.bottom, costello.cx, costello.y, "2020-08-26")}
  {edge(costello.x + 40, costello.bottom, trimarco.cx, trimarco.y)}
  {edge(costello.right - 20, costello.bottom, blap.cx, blap.y)}
  {edge(trimarco.cx, trimarco.bottom, apfs.cx, apfs.y, "2020-12-12")}
  {edge(blap.cx, blap.bottom, gai.cx, gai.y)}
  {edge(apfs.cx - 40, apfs.bottom, maryman.cx, maryman.y)}
  {edge(apfs.cx + 40, apfs.bottom, gustav.cx, gustav.y)}
  {edge(apfs.right, apfs.bottom, todd.cx, todd.y,
        d=f"M{apfs.right:.1f},{apfs.bottom:.1f} H{todd.cx:.1f} V{todd.y:.1f}")}
  {edge(todd.cx, todd.bottom, hayes.cx, hayes.y)}
  {edge(hayes.x, hayes.cy, mpolo.right, mpolo.y + 16,
        "bootable laptop|with user files", dashed=True, lx=121, ly=858,
        d=f"M{hayes.x:.1f},{hayes.cy:.1f} H{mpolo.right + 8:.1f} V{mpolo.y + 8:.1f}")}
  {edge(hayes.cx, hayes.bottom, apfsstar.cx, apfsstar.y)}
  {edge(iphone.x, iphone.bottom, mpolo.right, mpolo.y,
        d=f"M{iphone.x:.1f},{iphone.bottom:.1f} V916 H{mpolo.right:.1f} V{mpolo.y:.1f}")}
  {edge(iphone.x, iphone.cy, hayes.right, hayes.cy,
        "password provided by Hayes|on 2021-06-02", lx=640, ly=820)}'''

nodes_core = f'''  {laptop.svg()}
  {shop.svg()}
  {rhb.svg()}
  {boot01.svg()}
  {costello.svg()}
  {trimarco.svg()}
  {apfs.svg()}
  {maryman.svg()}
  {gustav.svg()}
  {blap.svg()}
  {gai.svg()}
  {todd.svg()}
  {hayes.svg()}
  {mpolo.svg()}
  {apfsstar.svg()}
  {jpmi.svg()}
  {cbs.svg()}
  {iphone.svg()}'''

# --- investigative materials (with 459Crimes) ---
W, H = 1440, 1048
x6 = Box(980, 320, 200, 60, ["JPMI (E01)", "Crucial X6", "HB-IMAGE-2022-04-29"], *JP)
crimes = Box(780, 424, 500, 148, [
    "459Crimes",
    "has possession of these five sources",
    "APFS*  ·  0728  ·  GAI  ·  JPMI (E01)  ·  IPHONE",
    "and has compiled the most in-depth",
    "analysis of the laptop ever conducted",
], *HOLD, sw=2)
eff = Box(780, 592, 500, 76, [
    "0728 Extra Found Files",
    "Hayes MEGA after 2021-07-28",
    "not a volume clone of JPMI, APFS, or GAI",
], *SIDE, dash=True)

inv = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {W} {H}" role="img"
     aria-label="Provenance of investigative materials held by 459Crimes">
  <title>Provenance of investigative materials</title>
  <rect width="{W}" height="{H}" fill="#ffffff"/>
{markers}
{lineage_clusters}
  {cluster(752, 404, 556, 284, "Investigative materials", "#fdf2f8", "#f9a8d4")}
  {cluster(752, 684, 556, 116, "iPhone backup — present on all copies", "#f0f9ff", "#7dd3fc")}

{lineage_edges}
  {edge(jpmi.cx + 40, jpmi.bottom, x6.cx, x6.y)}
  {edge(hayes.right, hayes.y, eff.x, 652,
        "MEGA bag; not identity", dashed=True, lx=620, ly=640,
        d=f"M{hayes.right:.1f},{hayes.y:.1f} V652 H{eff.x:.1f}")}

  {edge(x6.cx, x6.bottom, x6.cx, crimes.y, **hold_kw)}
  {edge(gai.right, gai.cy, crimes.x, crimes.y + 48, **hold_kw)}
  {edge(eff.cx, eff.y, crimes.cx, crimes.bottom, **hold_kw)}
  {edge(iphone.right, iphone.cy, crimes.right, crimes.cy + 28, **hold_kw,
        d=f"M{iphone.right:.1f},{iphone.cy:.1f} H1292 V{crimes.cy + 28:.1f} H{crimes.right:.1f}")}
  {edge(apfsstar.right, apfsstar.cy, crimes.right, crimes.cy - 28, **hold_kw,
        d=f"M{apfsstar.right:.1f},{apfsstar.cy:.1f} H1318 V{crimes.cy - 28:.1f} H{crimes.right:.1f}")}

{nodes_core}
  {x6.svg()}
  {eff.svg()}
  {crimes.svg()}
</svg>
'''

out = Path(__file__).with_name("investigative_materials.svg")
out.write_text(inv)
print(f"wrote {out} ({out.stat().st_size} bytes)")

# --- named copy graph (no 459Crimes) ---
NW, NH = 1440, 1048
named_x6 = Box(980, 320, 200, 60, ["Crucial X6 / E01", "HB-IMAGE-2022-04-29"], *JP)
named_eff = Box(780, 424, 500, 100, [
    "0728 Extra Found Files",
    "Hayes MEGA after 2021-07-28",
    "not a volume clone of JPMI, APFS, or GAI",
    "blobs match every combo of 3 / 2 / 1 / none",
], *SIDE, dash=True)

named = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" width="100%" viewBox="0 0 {NW} {NH}" role="img"
     aria-label="Named copy graph">
  <title>Named copy graph</title>
  <rect width="{NW}" height="{NH}" fill="#ffffff"/>
{markers}
{lineage_clusters}
  {cluster(752, 404, 556, 140, "0728 Extra Found Files — completely separate corpus", "#f9fafb", "#9ca3af")}
  {cluster(752, 684, 556, 116, "iPhone backup — present on all copies", "#f0f9ff", "#7dd3fc")}

{lineage_edges}
  {edge(jpmi.cx + 40, jpmi.bottom, named_x6.cx, named_x6.y)}
  {edge(hayes.right, hayes.y, named_eff.x, named_eff.cy,
        "MEGA bag; not identity", dashed=True, lx=600, ly=628,
        d=f"M{hayes.right:.1f},{hayes.y:.1f} V640 H700 V{named_eff.cy:.1f} H{named_eff.x:.1f}")}

{nodes_core}
  {named_x6.svg()}
  {named_eff.svg()}
</svg>
'''

named_out = Path(__file__).with_name("named_graph.svg")
named_out.write_text(named)
print(f"wrote {named_out} ({named_out.stat().st_size} bytes)")
