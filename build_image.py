#!/usr/bin/env python3
"""Draw the 18 November 2026 world-news front page (1024x1024 PNG).

31 real stories from Wednesday 18 November 2026, verified against that
day's reporting (Just Security Early Edition, One Turn, AP/Reuters via
Horizon, Nvidia Q3 coverage): a lead story, a world map with 12 datelines,
6 feature cards and 24 one-line briefings, plus a markets strip.
Drawn entirely with Pillow; no network, no external assets.
"""
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
PAPER = (247, 243, 234)
CARD = (255, 255, 255)
GREY = (90, 90, 90)
BORDER = (200, 192, 175)
OCEAN = (188, 214, 232)
LAND = (122, 154, 105)
LAND2 = (150, 170, 120)

# ---------- Masthead ----------
d.rectangle([0, 0, W, 104], fill=NAVY)
d.rectangle([0, 104, W, 109], fill=GOLD)
f_title = font(SERIF, 56)
t = "THE WORLD IN ONE DAY"
tw = d.textlength(t, font=f_title)
d.text(((W - tw) / 2, 12), t, font=f_title, fill=(255, 255, 255))
f_date = font(SANS_B, 25)
t2 = "WEDNESDAY  ·  18 NOVEMBER 2026  ·  31 STORIES"
tw2 = d.textlength(t2, font=f_date)
d.text(((W - tw2) / 2, 72), t2, font=f_date, fill=GOLD)

# ---------- Lead story card ----------
LX, LY, LW, LH = 24, 122, 976, 176
d.rectangle([LX, LY, LX + LW, LY + LH], fill=CARD, outline=BORDER, width=2)
d.rectangle([LX, LY, LX + 330, LY + 36], fill=RED)
d.text((LX + 14, LY + 5), "MIDDLE EAST  •  LEAD", font=font(SANS_B, 22), fill=(255, 255, 255))
# illustration: Qeshm strait scene, right side
IX, IY, IW, IH = LX + 648, LY + 36, 328, 132
d.rectangle([IX, IY, IX + IW, IY + IH], fill=(176, 208, 232))
d.ellipse([IX + 268, IY + 8, IX + 312, IY + 52], fill=(255, 214, 120))
d.rectangle([IX, IY + 92, IX + IW, IY + IH], fill=(38, 98, 140))
d.polygon([(IX + 16, IY + 92), (IX + 86, IY + 52), (IX + 200, IY + 52),
           (IX + 290, IY + 92)], fill=(94, 110, 72))
d.rectangle([IX + 124, IY + 38, IX + 131, IY + 52], fill=(60, 60, 60))
d.polygon([(IX + 122, IY + 38), (IX + 133, IY + 38), (IX + 127, IY + 16)], fill=(220, 220, 220))
cx, cy = IX + 127, IY + 8
for ang in range(0, 360, 30):
    x1 = cx + 8 * math.cos(math.radians(ang)); y1 = cy + 8 * math.sin(math.radians(ang))
    x2 = cx + 22 * math.cos(math.radians(ang)); y2 = cy + 22 * math.sin(math.radians(ang))
    d.line([x1, y1, x2, y2], fill=(255, 140, 0), width=5)
d.ellipse([cx - 10, cy - 10, cx + 10, cy + 10], fill=(255, 200, 40))
jx, jy = IX + 210, IY + 22
d.polygon([(jx, jy), (jx + 42, jy + 7), (jx, jy + 14), (jx + 7, jy + 7)], fill=(40, 40, 40))
d.polygon([(jx + 7, jy + 2), (jx + 16, jy + 7), (jx + 7, jy + 12)], fill=(40, 40, 40))
for dx, dy in [(IX + 40, IY + 106), (IX + 150, IY + 118), (IX + 250, IY + 108)]:
    d.ellipse([dx - 5, dy - 3, dx + 5, dy + 3], fill=(30, 30, 30))
    d.line([dx - 11, dy, dx + 11, dy], fill=(30, 30, 30), width=2)
# lead text (left)
TX = LX + 22
d.text((TX, LY + 42), "U.S. STRIKES IRAN", font=font(SERIF, 44), fill=INK)
y = LY + 94
for ln in wrap(d, "Jets hit a Revolutionary Guard missile site on Qeshm Island.",
               font(SANS_B, 22), 600):
    d.text((TX, y), ln, font=font(SANS_B, 22), fill=RED)
    y += 27
y += 4
for ln in wrap(d, "Iran hits back: drones at U.S. sites in Bahrain and Kuwait.",
               font(SANS, 20), 600):
    d.text((TX, y), ln, font=font(SANS, 20), fill=INK)
    y += 26

# ---------- World map ----------
MX, MY, MW, MH = 24, 310, 976, 128
d.rectangle([MX, MY, MX + MW, MY + MH], fill=OCEAN, outline=BORDER, width=2)
d.text((MX + MW - 218, MY + 6), "WHERE IT HAPPENED", font=font(SANS_B, 16),
       fill=(20, 60, 90))
def proj(lon, lat):
    # equirectangular: lon -180..180 -> x, lat 75..-58 -> y
    x = MX + 8 + (lon + 180) / 360.0 * (MW - 16)
    y = MY + 20 + (75 - lat) / 133.0 * (MH - 28)
    return (x, y)
def land_poly(points, fill=LAND):
    d.polygon([proj(lo, la) for lo, la in points], fill=fill)
# North America
land_poly([(-168, 66), (-150, 70), (-130, 71), (-115, 69), (-100, 69),
           (-90, 68), (-82, 66), (-76, 62), (-70, 58), (-65, 49), (-70, 42),
           (-75, 35), (-80, 30), (-84, 30), (-90, 21), (-95, 18), (-105, 20),
           (-110, 24), (-115, 30), (-125, 40), (-125, 49), (-135, 58),
           (-150, 60), (-165, 60)])
# Greenland
land_poly([(-55, 60), (-45, 60), (-32, 68), (-25, 70), (-30, 76), (-50, 76),
           (-58, 70)], fill=LAND2)
# South America
land_poly([(-80, 9), (-72, 11), (-62, 9), (-52, 5), (-50, 0), (-44, -3),
           (-35, -8), (-38, -15), (-40, -22), (-48, -28), (-54, -34),
           (-58, -38), (-62, -41), (-65, -45), (-68, -50), (-70, -55),
           (-73, -50), (-73, -40), (-72, -30), (-70, -20), (-75, -15),
           (-80, -5), (-81, 2)])
# Africa
land_poly([(-17, 15), (-16, 20), (-10, 30), (-5, 35), (0, 36), (10, 37),
           (12, 34), (20, 32), (30, 31), (32, 31), (35, 28), (38, 22),
           (43, 12), (48, 11), (51, 11), (48, 2), (41, -2), (40, -10),
           (38, -18), (35, -25), (32, -29), (28, -33), (20, -35), (16, -32),
           (14, -22), (12, -15), (13, -8), (9, 4), (0, 5), (-8, 5),
           (-13, 8), (-17, 12)])
# Eurasia
land_poly([(-10, 36), (-9, 43), (-2, 48), (0, 50), (4, 52), (8, 55),
           (10, 58), (15, 56), (18, 56), (21, 58), (24, 60), (28, 61),
           (30, 63), (32, 68), (40, 68), (50, 69), (60, 69), (70, 72),
           (80, 73), (90, 75), (100, 77), (110, 76), (120, 73), (130, 72),
           (140, 72), (150, 70), (160, 69), (170, 67), (178, 65), (172, 62),
           (165, 60), (158, 53), (156, 50), (150, 59), (142, 52), (141, 45),
           (140, 39), (135, 34), (130, 33), (127, 35), (122, 31), (120, 25),
           (114, 22), (109, 18), (105, 9), (103, 7), (100, 8), (98, 12),
           (95, 16), (92, 21), (89, 22), (86, 20), (82, 17), (80, 13),
           (77, 8), (74, 13), (72, 20), (68, 23), (64, 25), (60, 25),
           (57, 26), (54, 27), (51, 28), (49, 30), (46, 29), (43, 28),
           (40, 30), (38, 32), (36, 36), (33, 36), (30, 36), (27, 37),
           (23, 36), (19, 40), (15, 40), (12, 38), (8, 37), (4, 37),
           (0, 36), (-5, 36)])
# Australia
land_poly([(113, -22), (114, -30), (115, -35), (118, -35), (124, -33),
           (130, -32), (135, -35), (138, -35), (140, -38), (145, -38),
           (150, -37), (153, -27), (150, -22), (146, -19), (142, -11),
           (137, -12), (132, -12), (127, -14), (122, -17), (118, -20)])
# dateline dots + labels (lon, lat, label, dx, dy)
dots = [
    (56, 27, "Qeshm", 6, -18), (34, 45, "", 0, 0),
    (114, 22, "Shenzhen", -8, 12), (-150, 64, "Alaska", 2, 10),
    (23, 0, "Congo", -6, 12), (-160, -21, "Cook Is.", -14, 12),
    (34, 31, "Gaza", 6, 4), (25, 46, "", 0, 0),
    (87, 55, "Siberia", -10, -16), (147, -6, "Papua N.G.", -16, 12),
    (2, 49, "Paris", 4, -14), (30, 37, "Antalya", 4, -16),
]
f_lab = font(SANS_B, 12)
for lon, lat, label, dx, dy in dots:
    x, y = proj(lon, lat)
    d.ellipse([x - 5, y - 5, x + 5, y + 5], fill=RED, outline=(255, 255, 255), width=1)
    if not label:
        continue
    lx, ly = x + dx, y + dy
    # white halo for legibility
    for ox, oy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        d.text((lx + ox, ly + oy), label, font=f_lab, fill=(255, 255, 255))
    d.text((lx, ly), label, font=f_lab, fill=NAVY)

# ---------- Feature cards: 3 cols x 2 rows ----------
def icon_bridge(d, x, y, s=1.0):
    d.line([x, y + 46, x + 62, y + 46], fill=(90, 90, 90), width=5)
    for px in (x + 6, x + 52):
        d.line([px, y + 46, px, y + 70], fill=(90, 90, 90), width=4)
    d.line([x + 24, y + 46, x + 38, y + 46], fill=(200, 60, 40), width=5)
    d.polygon([(x + 24, y + 46), (x + 31, y + 66), (x + 38, y + 46)], fill=(200, 60, 40))
    d.line([x + 10, y + 16, x + 31, y + 46], fill=(120, 120, 120), width=3)
    d.line([x + 52, y + 16, x + 31, y + 46], fill=(120, 120, 120), width=3)

def icon_skyline(d, x, y):
    for bx, bw, bh in [(x, 12, 44), (x + 15, 15, 60), (x + 33, 12, 38), (x + 48, 10, 52)]:
        d.rectangle([bx, y + 70 - bh, bx + bw, y + 70], fill=(70, 90, 120))
    d.line([x, y + 70, x + 62, y + 70], fill=(70, 90, 120), width=3)

def icon_ballot(d, x, y):
    d.rectangle([x + 4, y + 22, x + 58, y + 70], fill=(240, 240, 235),
                outline=(70, 90, 120), width=3)
    d.rectangle([x + 16, y + 12, x + 46, y + 26], fill=(70, 90, 120))
    d.line([x + 14, y + 50, x + 26, y + 62], fill=(30, 140, 60), width=5)
    d.line([x + 26, y + 62, x + 50, y + 34], fill=(30, 140, 60), width=5)

def icon_virus(d, x, y):
    vx, vy = x + 31, y + 38
    for ang in range(0, 360, 45):
        x2 = vx + 26 * math.cos(math.radians(ang)); y2 = vy + 26 * math.sin(math.radians(ang))
        d.line([vx, vy, x2, y2], fill=(150, 40, 40), width=4)
        d.ellipse([x2 - 4, y2 - 4, x2 + 4, y2 + 4], fill=(150, 40, 40))
    d.ellipse([vx - 18, vy - 18, vx + 18, vy + 18], fill=(178, 60, 60))
    d.ellipse([vx - 8, vy - 9, vx + 1, vy - 1], fill=(255, 255, 255))
    d.ellipse([vx + 4, vy + 4, vx + 11, vy + 11], fill=(255, 255, 255))

def icon_chip(d, x, y):
    d.rectangle([x + 12, y + 14, x + 50, y + 56], fill=(30, 60, 90),
                outline=(212, 175, 55), width=3)
    d.rectangle([x + 24, y + 26, x + 38, y + 44], fill=(212, 175, 55))
    for px in (x + 18, x + 31, x + 44):
        d.line([px, y + 4, px, y + 14], fill=(90, 90, 90), width=3)
        d.line([px, y + 56, px, y + 66], fill=(90, 90, 90), width=3)
    for py in (y + 22, y + 35, y + 48):
        d.line([x + 2, py, x + 12, py], fill=(90, 90, 90), width=3)
        d.line([x + 50, py, x + 60, py], fill=(90, 90, 90), width=3)

def icon_cyclone(d, x, y):
    cx, cy = x + 31, y + 36
    for r, a0 in [(26, 0), (19, 60), (12, 120), (6, 180)]:
        a1 = a0 + 200
        d.arc([cx - r, cy - r, cx + r, cy + r], a0, a1, fill=(20, 90, 140), width=4)
    d.ellipse([cx - 4, cy - 4, cx + 4, cy + 4], fill=(20, 90, 140))

ICONS = {"bridge": icon_bridge, "skyline": icon_skyline, "ballot": icon_ballot,
         "virus": icon_virus, "chip": icon_chip, "cyclone": icon_cyclone}

cards = [
    ("EUROPE  •  UKRAINE", (20, 60, 120), "Kerch Bridge hit again",
     "Ukraine strikes the Crimea bridge a second day; part of its road span falls into the strait.", "bridge"),
    ("ASIA  •  CHINA", (150, 60, 30), "Xi hosts Putin in Shenzhen",
     "Leaders meet at APEC a day before the first-ever Trump–Xi–Putin summit.", "skyline"),
    ("U.S.  •  POLITICS", (30, 90, 120), "Peltola takes Alaska",
     "Democrat beats Sen. Sullivan; her party reaches 56 Senate seats.", "ballot"),
    ("AFRICA  •  HEALTH", (120, 40, 40), "Ebola doubles in Congo",
     "Outbreak passes 11,000 cases and 5,400 deaths, the UN says.", "virus"),
    ("MARKETS  •  TECH", (30, 60, 90), "Nvidia doubles revenue",
     "Q3 sales hit $115.8bn; shares jump as interim chief Kress steadies the firm.", "chip"),
    ("PACIFIC  •  WEATHER", (14, 110, 110), "Cyclone Xavier slams Cook Is.",
     "Category 5 storm brings gusts of 315 km/h to the Northern Cook Islands.", "cyclone"),
]
GX, GY = 24, 450
CW, CH, GAP = 318, 146, 11
for i, (tag, color, head, body, icon) in enumerate(cards):
    cx = GX + (i % 3) * (CW + GAP)
    cy = GY + (i // 3) * (CH + GAP)
    d.rectangle([cx, cy, cx + CW, cy + CH], fill=CARD, outline=BORDER, width=2)
    d.rectangle([cx, cy, cx + CW, cy + 28], fill=color)
    d.text((cx + 10, cy + 5), tag, font=font(SANS_B, 16), fill=(255, 255, 255))
    f_ch = font(SERIF, 21)
    lines = wrap(d, head, f_ch, CW - 20)
    yy = cy + 34
    for ln in lines[:2]:
        d.text((cx + 10, yy), ln, font=f_ch, fill=INK)
        yy += 25
    f_cb = font(SANS, 15)
    lines = wrap(d, body, f_cb, CW - 92)
    yy = cy + 34 + 25 * min(2, len(wrap(d, head, f_ch, CW - 20)))
    for ln in lines[:3]:
        d.text((cx + 10, yy), ln, font=f_cb, fill=(50, 50, 50))
        yy += 19
    ICONS[icon](d, cx + CW - 78, cy + CH - 82)

# ---------- Briefings: 3 columns x 8 ----------
BY = 762
d.rectangle([24, BY, 1000, BY + 28], fill=NAVY)
d.text((40, BY + 4), "MORE FROM AROUND THE WORLD  —  24 BRIEFINGS",
       font=font(SANS_B, 17), fill=GOLD)
briefs = [
    "Russian plane crash in Siberia kills 19",
    "5.3 quake shakes Romania",
    "6.0 quake strikes Papua New Guinea",
    "U.S. loses measles-free status",
    "Kahana elected Knesset speaker",
    "Board of Peace: Gaza truce may collapse",
    "Houthis fire drones at Saudi pipeline",
    "UK sanctions 8 West Bank firms",
    "EU states plan Rwanda return hubs",
    "140,000 join French pay protests",
    "Turkey takes over Sozcu TV",
    "Serbia parliament opens, students lead",
    "Tigray clashes raise war fears",
    "U.S. soldier in UK spy case moved home",
    "27 years for Iran-linked plot vs Trump",
    "World Court to rule on Myanmar case",
    "COP31 draft: $120bn climate finance",
    "U.S. tightens chip rules for China",
    "Anthropic to list on Nasdaq Nov 19",
    "Fiji declares disaster over drought",
    "Fela Kuti enters Rock Hall of Fame",
    "Pattinson named new James Bond",
    "\u2018Human\u2019 is Word of the Year 2026",
    "Zverev into ATP Finals knockouts",
]
f_b = font(SANS, 14)
f_bb = font(SANS_B, 14)
col_w = 318
row_h = 21
for j, item in enumerate(briefs):
    col = j // 8
    row = j % 8
    bx = 24 + col * (col_w + GAP)
    by = BY + 28 + 6 + row * row_h
    # fit check: shrink not needed; warn if too wide
    if d.textlength(item, font=f_b) > col_w - 18:
        print("WARN too wide:", item)
    d.text((bx, by), "•", font=f_bb, fill=RED)
    d.text((bx + 14, by), item, font=f_b, fill=INK)

# ---------- Markets strip + footer ----------
FY = BY + 28 + 6 + 8 * row_h + 4  # ~968
d.rectangle([24, FY, 1000, FY + 26], fill=(235, 230, 218), outline=BORDER, width=1)
f_m = font(SANS_B, 14)
mk = "MARKETS:  S&P 500 7,341  ▼1.03%   •   FTSE 100 10,690  ▼1.76%   •   Brent $92.47  ▼0.72%   •   Gold ▼2.05%"
twm = d.textlength(mk, font=f_m)
d.text(((W - twm) / 2, FY + 5), mk, font=f_m, fill=NAVY)
f_ft = font(SANS, 13)
ft = "Wednesday 18 November 2026  •  The World in One Day  •  make.fun"
twf = d.textlength(ft, font=f_ft)
d.text(((W - twf) / 2, FY + 30), ft, font=f_ft, fill=GREY)

img.save(OUT, "PNG", optimize=True)
print("saved", OUT, os.path.getsize(OUT), "bytes")
