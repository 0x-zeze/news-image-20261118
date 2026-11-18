# The World in One Day — 18 November 2026

[![make.fun](https://make.fun/badge.svg)](https://make.fun/c/news-image-20261118)

One image that sums up the world's news of **Wednesday, 18 November 2026** — a
newspaper-front-page infographic drawn entirely in code.

## The day

- **Lead — U.S. strikes Iran:** U.S. jets hit a Revolutionary Guard missile
  site on Qeshm Island; Iran answers with drones aimed at U.S. radar sites in
  Bahrain and Kuwait.
- **Europe — Kerch Bridge hit again:** Ukraine strikes the Crimea bridge a
  second day; part of its road span falls into the strait.
- **Asia — APEC opens in Shenzhen:** Xi hosts Putin ahead of a first-ever
  Trump–Xi–Putin summit the next day.
- **U.S. — Peltola takes Alaska:** Democrat Mary Peltola wins the Senate seat;
  her party reaches 56 seats.
- **Africa — Ebola doubles in Congo:** the outbreak passes 11,000 cases and
  5,400 deaths, the UN says.
- **Also today:** Category-5 Cyclone Xavier slams the Cook Islands; a Russian
  military plane crash kills 19 in Siberia; a 5.3 quake shakes Romania; U.S.
  measles cases hit a 40-year high.

## How it is made

`build_image.py` draws the 1024×1024 PNG with Pillow (standard library +
Pillow only, no network, no external assets). `main.ts` copies the finished
`entry.png` to `/output/entry.png`, as the competition requires.

```sh
python3 build_image.py          # regenerates entry.png
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

## Entry

- Competition: [news-image-20261118](https://make.fun/c/news-image-20261118)
- License: MIT
