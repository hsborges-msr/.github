"""Generates the hsborges-msr logo (avatar + wordmark) as font-independent SVG and PNG."""

import sys
from pathlib import Path

import cairosvg
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from vein import vein

HERE = Path(__file__).parent
OUT = HERE / "out"
OUT.mkdir(exist_ok=True)

BASALT = "#1E1E22"
GOLD = "#D4A017"
QUARTZ = "#F4F1EA"


def text_path(font_file, text, size, x, y):
    """Returns (svg path d, advance width) for text with baseline at (x, y)."""
    font = TTFont(font_file)
    gs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    pen = SVGPathPen(gs)
    cursor = 0
    for ch in text:
        name = cmap[ord(ch)]
        tpen = TransformPen(pen, (scale, 0, 0, -scale, x + cursor * scale, y))
        gs[name].draw(tpen)
        cursor += gs[name].width
    return pen.getCommands(), cursor * scale


EXTRA = HERE / "jbm/fonts/ttf/JetBrainsMono-ExtraBold.ttf"


def avatar(dark=True):
    bg, fg = (BASALT, QUARTZ) if dark else (QUARTZ, BASALT)
    size = 512
    # "hsb" sits in the upper-left triangle, "msr" in the lower-right one,
    # split by the gold vein that doubles as the path separator: hsb/msr.
    hsb, hsb_w = text_path(EXTRA, "hsb", 120, 58, 178)
    msr, msr_w = text_path(EXTRA, "msr", 150, 0, 0)
    msr_x = size - 50 - msr_w
    msr, _ = text_path(EXTRA, "msr", 150, msr_x, 440)
    VEIN = vein(452, 50, 72, 462, [4, 17, 24, 21, 15, 4], [4, 14, 21, 24, 18, 4], [0, 0.16, 0.4, 0.6, 0.84, 1])
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {size} {size}" width="{size}" height="{size}">
  <title>hsborges-msr</title>
  <rect width="{size}" height="{size}" rx="104" fill="{bg}"/>
  <path d="{hsb}" fill="{fg}"/>
  <path d="{VEIN}" fill="{GOLD}"/>
  <path d="{msr}" fill="{fg}"/>
</svg>
"""


def wordmark(dark=True):
    bg, fg = (BASALT, QUARTZ) if dark else (QUARTZ, BASALT)
    h = 160
    name, name_w = text_path(EXTRA, "hsborges", 96, 48, 114)
    gap = 18
    slash_x = 48 + name_w + gap
    VEIN = vein(slash_x + 58, 22, slash_x, 138, [2, 8, 9, 2], [2, 7, 9, 2], [0, 0.35, 0.6, 1])
    msr, msr_w = text_path(EXTRA, "msr", 96, slash_x + 58 + gap, 114)
    w = round(slash_x + 58 + gap + msr_w + 48)
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <title>hsborges-msr</title>
  <rect width="{w}" height="{h}" rx="28" fill="{bg}"/>
  <path d="{name}" fill="{fg}"/>
  <path d="{VEIN}" fill="{GOLD}"/>
  <path d="{msr}" fill="{fg}"/>
</svg>
"""


if __name__ == "__main__":
    files = {
        "avatar": avatar(),
        "avatar-light": avatar(dark=False),
        "wordmark": wordmark(),
        "wordmark-light": wordmark(dark=False),
    }
    for name, svg in files.items():
        (OUT / f"{name}.svg").write_text(svg)
        width = 512 if name.startswith("avatar") else 1200
        cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / f"{name}.png"), output_width=width)
    cairosvg.svg2png(bytestring=files["avatar"].encode(), write_to=str(OUT / "avatar-40.png"), output_width=40)
    print("ok", *sys.argv[1:])
