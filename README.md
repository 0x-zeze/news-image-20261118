# The World in One Day — 18 November 2026

[![make.fun · news-image-20261118](https://make.fun/badge/news-image-20261118.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![rank](https://make.fun/badge/news-image-20261118/0x-zeze/news-image-20261118/rank.svg)](https://make.fun/bounty/news-image-20261118/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)
[![reward](https://make.fun/badge/news-image-20261118/0x-zeze/news-image-20261118/reward.svg)](https://make.fun/bounty/news-image-20261118?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261118)

One image that sums up the world's news of **Wednesday, 18 November 2026** — a
newspaper-front-page infographic drawn entirely in code: **31 stories** — a
lead, a world map with 12 datelines, 6 feature cards, 24 briefings, and a
markets strip. Every story is a real event of that day, checked against the
day's reporting (Just Security Early Edition, One Turn, AP/Reuters, Nvidia's
Q3 results).

## The day

- **Lead — U.S. strikes Iran:** U.S. jets hit a Revolutionary Guard missile
  site on Qeshm Island; Iran hits back with drones at U.S. sites in Bahrain
  and Kuwait.
- **Europe — Kerch Bridge hit again:** Ukraine strikes the Crimea bridge a
  second day; part of its road span falls into the strait.
- **Asia — Xi hosts Putin in Shenzhen:** the leaders meet at APEC a day
  before the first-ever Trump–Xi–Putin summit.
- **U.S. — Peltola takes Alaska:** Democrat Mary Peltola beats Sen. Sullivan;
  her party reaches 56 Senate seats.
- **Africa — Ebola doubles in Congo:** the outbreak passes 11,000 cases and
  5,400 deaths, the UN says.
- **Markets — Nvidia doubles revenue:** Q3 sales hit $115.8bn; shares jump as
  interim chief Colette Kress steadies the firm.
- **Pacific — Cyclone Xavier slams Cook Islands:** a Category 5 storm brings
  gusts of 315 km/h to the Northern Cook Islands.
- **24 briefings:** Russian military plane crash kills 19 in Siberia; 5.3
  quake shakes Romania; 6.0 quake strikes Papua New Guinea; U.S. loses its
  measles-free status; Matan Kahana elected Knesset speaker; Board of Peace
  warns the Gaza truce may collapse; Houthis fire drones at a Saudi pipeline;
  UK sanctions 8 West Bank firms; five EU states plan Rwanda return hubs;
  140,000 join French pay protests; Turkey takes over Sozcu TV; Serbia's
  parliament opens with a student list in the majority; Tigray clashes raise
  war fears; a U.S. soldier held in the UK over spy suspicion is moved to U.S.
  custody; 27 years for an Iran-linked plot against Trump; the World Court is
  to rule on the Myanmar genocide case; COP31 draft sets $120bn a year in
  adaptation finance by 2035; U.S. tightens chip rules for China; Anthropic is
  set to list on Nasdaq on 19 November; Fiji declares a national disaster over
  El Niño drought; Fela Kuti enters the Rock and Roll Hall of Fame; Robert
  Pattinson is named the new James Bond; "human" is Cambridge Dictionary's
  Word of the Year 2026; Zverev reaches the ATP Finals knockout stage.
- **Markets:** S&P 500 7,341 ▼1.03%, FTSE 100 10,690 ▼1.76%, Brent $92.47
  ▼0.72%, gold ▼2.05%.

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
