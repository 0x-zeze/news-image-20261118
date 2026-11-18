#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news summary image (1024x1024 PNG)."""
from PIL import Image, ImageDraw, ImageFont
import math, os

W = H = 1024
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")

SERIF = "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf"
SERIF_R = "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf"
SANS = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
SANS_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=fnt) <= max_w:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines

img = Image.new("RGB", (W, H), (247, 243, 234))
d = ImageDraw.Draw(img)

NAVY = (20, 33, 61)
GOLD = (212, 175, 55)
INK = (24, 24, 24)
RED = (178, 34, 34)
TEAL = (14, 110, 110)
PAPER = (247, 243, 234)
CARD = (255, 255, 255)
GREY = (90, 90, 90)

# ---------- Masthead ----------
d.rectangle([0, 0, W, 158], fill=NAVY)
d.rectangle([0, 158, W, 163], fill=GOLD)
f_title = font(SERIF, 62)
t = "THE WORLD IN ONE DAY"
tw = d.textlength(t, font=f_title)
d.text(((W - tw) / 2, 22), t, font=f_title, fill=(255, 255, 255))
f_date = font(SANS_B, 34)
t2 = "WEDNESDAY  ·  18 NOVEMBER 2026"
tw2 = d.textlength(t2, font=f_date)
d.text(((W - tw2) / 2, 102), t2, font=f_date, fill=GOLD)

# ---------- Lead story card ----------
LX, LY, LW, LH = 24, 178, 976, 296
d.rectangle([LX, LY, LX + LW, LY + LH], fill=CARD, outline=(200, 192, 175), width=2)
# tag
d.rectangle([LX, LY, LX + 330, LY + 40], fill=RED)
f_tag = font(SANS_B, 24)
d.text((LX + 16, LY + 6), "MIDDLE EAST  •  LEAD", font=f_tag, fill=(255, 255, 255))
# illustration on right: Qeshm strait scene
IX, IY, IW, IH = LX + 640, LY + 40, 336, 256
# sky
d.rectangle([IX, IY, IX + IW, IY + IH], fill=(176, 208, 232))
# sun glow
d.ellipse([IX + 250, IY + 18, IX + 310, IY + 78], fill=(255, 214, 120))
# sea
d.rectangle([IX, IY + 170, IX + IW, IY + IH], fill=(38, 98, 140))
# island
d.polygon([(IX + 20, IY + 170), (IX + 90, IY + 118), (IX + 210, IY + 118),
           (IX + 300, IY + 170)], fill=(94, 110, 72))
# missile launcher + missile
d.rectangle([IX + 130, IY + 96, IX + 138, IY + 118], fill=(60, 60, 60))
d.polygon([(IX + 128, IY + 96), (IX + 140, IY + 96), (IX + 134, IY + 70)], fill=(200, 200, 200))
# explosion burst
cx, cy = IX + 134, IY + 52
for ang in range(0, 360, 30):
    r1, r2 = 10, 30
    x1 = cx + r1 * math.cos(math.radians(ang)); y1 = cy + r1 * math.sin(math.radians(ang))
    x2 = cx + r2 * math.cos(math.radians(ang)); y2 = cy + r2 * math.sin(math.radians(ang))
    d.line([x1, y1, x2, y2], fill=(255, 140, 0), width=6)
d.ellipse([cx - 14, cy - 14, cx + 14, cy + 14], fill=(255, 200, 40))
# jet silhouette
jx, jy = IX + 220, IY + 46
d.polygon([(jx, jy), (jx + 46, jy + 8), (jx, jy + 16), (jx + 8, jy + 8)], fill=(40, 40, 40))
d.polygon([(jx + 8, jy + 2), (jx + 18, jy + 8), (jx + 8, jy + 14)], fill=(40, 40, 40))
# drones over the sea
for dx, dy in [(IX + 40, IY + 205), (IX + 150, IY + 225), (IX + 260, IY + 210)]:
    d.ellipse([dx - 5, dy - 3, dx + 5, dy + 3], fill=(30, 30, 30))
    d.line([dx - 12, dy, dx + 12, dy], fill=(30, 30, 30), width=2)
# illustration on right: Qeshm strait scene (kept inside the card)

# lead text (left)
TX = LX + 24
f_h = font(SERIF, 54)
d.text((TX, LY + 52), "U.S. STRIKES IRAN", font=f_h, fill=INK)
f_sub = font(SANS_B, 27)
lines = wrap(d, "Jets hit a Revolutionary Guard missile site on Qeshm Island.", f_sub, 600)
y = LY + 128
for ln in lines:
    d.text((TX, y), ln, font=f_sub, fill=RED)
    y += 34
f_body = font(SANS, 25)
lines = wrap(d, "Iran answers with drones aimed at U.S. radar sites in Bahrain and Kuwait — its third attack there in under a week.", f_body, 600)
y += 8
for ln in lines:
    d.text((TX, y), ln, font=f_body, fill=INK)
    y += 32

# ---------- 2x2 grid ----------
GX, GY = 24, 490
CW, CH, GAP = 480, 178, 16
cells = [
    ("EUROPE  •  UKRAINE", (20, 60, 120), "Kerch Bridge hit again",
     "Ukraine strikes the Crimea bridge a second day; part of its road span falls into the strait.", "bridge"),
    ("ASIA  •  CHINA", (150, 60, 30), "APEC opens in Shenzhen",
     "Xi hosts Putin ahead of a first-ever Trump–Xi–Putin summit tomorrow.", "skyline"),
    ("U.S.  •  POLITICS", (30, 90, 120), "Peltola takes Alaska",
     "Democrat Mary Peltola wins the Senate seat; her party reaches 56 seats.", "ballot"),
    ("AFRICA  •  HEALTH", (120, 40, 40), "Ebola doubles in Congo",
     "Outbreak passes 11,000 cases and 5,400 deaths, the UN says.", "virus"),
]
for i, (tag, color, head, body, icon) in enumerate(cells):
    cx = GX + (i % 2) * (CW + GAP)
    cy = GY + (i // 2) * (CH + GAP)
    d.rectangle([cx, cy, cx + CW, cy + CH], fill=CARD, outline=(200, 192, 175), width=2)
    d.rectangle([cx, cy, cx + CW, cy + 34], fill=color)
    f_ct = font(SANS_B, 20)
    d.text((cx + 14, cy + 6), tag, font=f_ct, fill=(255, 255, 255))
    f_ch = font(SERIF, 28)
    d.text((cx + 14, cy + 46), head, font=f_ch, fill=INK)
    f_cb = font(SANS, 21)
    lines = wrap(d, body, f_cb, CW - 118)
    yy = cy + 90
    for ln in lines[:3]:
        d.text((cx + 14, yy), ln, font=f_cb, fill=(50, 50, 50))
        yy += 27
    # icon, bottom-right corner (clear of the text)
    ix, iy = cx + CW - 88, cy + CH - 100
    if icon == "bridge":
        d.line([ix, iy + 60, ix + 80, iy + 60], fill=(90, 90, 90), width=6)
        for px in (ix + 8, ix + 68):
            d.line([px, iy + 60, px, iy + 92], fill=(90, 90, 90), width=5)
        d.line([ix + 30, iy + 60, ix + 50, iy + 60], fill=(200, 60, 40), width=6)
        d.polygon([(ix + 30, iy + 60), (ix + 40, iy + 84), (ix + 50, iy + 60)], fill=(200, 60, 40))
        d.line([ix + 14, iy + 20, ix + 40, iy + 60], fill=(120, 120, 120), width=3)
        d.line([ix + 66, iy + 20, ix + 40, iy + 60], fill=(120, 120, 120), width=3)
    elif icon == "skyline":
        for bx, bw, bh in [(ix, 16, 66), (ix + 20, 20, 88), (ix + 44, 16, 56), (ix + 64, 14, 76)]:
            d.rectangle([bx, iy + 96 - bh, bx + bw, iy + 96], fill=(70, 90, 120))
        d.line([ix, iy + 96, ix + 80, iy + 96], fill=(70, 90, 120), width=4)
    elif icon == "ballot":
        d.rectangle([ix + 6, iy + 30, ix + 74, iy + 92], fill=(240, 240, 235), outline=(70, 90, 120), width=4)
        d.rectangle([ix + 22, iy + 18, ix + 58, iy + 34], fill=(70, 90, 120))
        d.line([ix + 18, iy + 66, ix + 34, iy + 82], fill=(30, 140, 60), width=6)
        d.line([ix + 34, iy + 82, ix + 64, iy + 44], fill=(30, 140, 60), width=6)
    elif icon == "virus":
        vx, vy = ix + 40, iy + 56
        for ang in range(0, 360, 45):
            x2 = vx + 34 * math.cos(math.radians(ang)); y2 = vy + 34 * math.sin(math.radians(ang))
            d.line([vx, vy, x2, y2], fill=(150, 40, 40), width=5)
            d.ellipse([x2 - 5, y2 - 5, x2 + 5, y2 + 5], fill=(150, 40, 40))
        d.ellipse([vx - 24, vy - 24, vx + 24, vy + 24], fill=(178, 60, 60))
        d.ellipse([vx - 10, vy - 12, vx + 2, vy], fill=(255, 255, 255))
        d.ellipse([vx + 6, vy + 6, vx + 14, vy + 14], fill=(255, 255, 255))

# ---------- Also today strip ----------
AY = 490 + 2 * CH + GAP + 4  # 490+356+16+4 = 866
d.rectangle([24, AY, 1000, AY + 84], fill=NAVY)
f_at = font(SANS_B, 22)
d.text((40, AY + 8), "ALSO TODAY", font=f_at, fill=GOLD)
f_ai = font(SANS, 21)
items = ("Cat-5 Cyclone Xavier slams the Cook Islands  •  Russian military plane crash kills 19 in Siberia  •  "
         "5.3 quake shakes Romania  •  U.S. measles cases hit a 40-year high")
lines = wrap(d, items, f_ai, 976 - 32)
yy = AY + 38
for ln in lines:
    d.text((40, yy), ln, font=f_ai, fill=(255, 255, 255))
    yy += 26

# ---------- Footer ----------
f_ft = font(SANS, 18)
ft = "One day's world news  •  Wednesday 18 November 2026  •  make.fun"
twf = d.textlength(ft, font=f_ft)
d.text(((W - twf) / 2, 972), ft, font=f_ft, fill=GREY)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes")
