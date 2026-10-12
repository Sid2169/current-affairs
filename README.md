# UPSC Prelims — Current Affairs Notes

A structured repository of current-affairs notes for the UPSC Civil Services
Preliminary Examination, organised month-wise in the section-by-section style of
monthly current-affairs magazines.

## Repository Structure

```
.
├── README.md                # this index
├── .gitignore
├── tools/
│   └── build_month_index.py # regenerates a month's index from its section files
├── July-2026/               # one folder per month
│   ├── CURRENT_AFFAIRS_JULY_2026.md   # monthly index (cover + Table of Contents)
│   ├── 1-Polity-and-Governance/notes.md
│   ├── 2-International-Relations/notes.md
│   ├── 3-Economy/notes.md
│   ├── 4-Security/notes.md
│   ├── 5-Environment/notes.md
│   ├── 6-Social-Issues/notes.md
│   ├── 7-Science-and-Technology/notes.md
│   ├── 8-Culture/notes.md
│   ├── 9-Schemes-in-News/notes.md
│   └── 10-Places-in-News/notes.md
└── August-2026/             # (add future months here)
```

- Each **month** gets its own folder (e.g. `July-2026/`).
- Every month folder contains a **monthly index** file (cover + Table of Contents)
  plus the ten **per-section** notes folders.
- Content lives **only** in the per-section files. The monthly index links to them
  and stores no duplicated text, so there is a single source of truth per section.

## Monthly Index

| Month | Monthly Index |
|-------|---------------|
| July 2026 | [CURRENT_AFFAIRS_JULY_2026.md](July-2026/CURRENT_AFFAIRS_JULY_2026.md) |

## Section Structure

Every monthly edition uses the same ten standard sections:

| # | Section | Folder |
|---|---------|--------|
| 01 | Polity & Governance | `1-Polity-and-Governance/notes.md` |
| 02 | International Relations | `2-International-Relations/notes.md` |
| 03 | Economy | `3-Economy/notes.md` |
| 04 | Security | `4-Security/notes.md` |
| 05 | Environment | `5-Environment/notes.md` |
| 06 | Social Issues | `6-Social-Issues/notes.md` |
| 07 | Science & Technology | `7-Science-and-Technology/notes.md` |
| 08 | Culture | `8-Culture/notes.md` |
| 09 | Schemes in News | `9-Schemes-in-News/notes.md` |
| 10 | Places in News | `10-Places-in-News/notes.md` |

Each **section file** follows the standard monthly-magazine format:

- Numbered sections, each opening with long-form **"Why in News?"** items.
- Background explainers, comparison tables, **Challenges / Way Forward / Conclusion**.
- A **News in Shorts** subsection of concise, factual items.

Each **monthly index** (`CURRENT_AFFAIRS_<MONTH>_<YEAR>.md`) is a thin navigation
file: a cover note plus a **clickable Table of Contents** whose every entry (three
levels deep) links into the relevant section file and heading anchor. Each section
file also carries a **↑ Back to Monthly Index** link at its top and bottom. These
links work in rendered Markdown (GitHub, GitLab, VS Code preview, etc.).

## Section Index — July 2026

Direct links into the section files (also reachable via the
[monthly index](July-2026/CURRENT_AFFAIRS_JULY_2026.md)):

| # | Section | Jump to section | Section notes |
|---|---------|-----------------|---------------|
| 01 | Polity & Governance | [1. Polity & Governance](July-2026/1-Polity-and-Governance/notes.md#sec-1) | [notes](July-2026/1-Polity-and-Governance/notes.md) |
| 02 | International Relations | [2. International Relations](July-2026/2-International-Relations/notes.md#sec-2) | [notes](July-2026/2-International-Relations/notes.md) |
| 03 | Economy | [3. Economy](July-2026/3-Economy/notes.md#sec-3) | [notes](July-2026/3-Economy/notes.md) |
| 04 | Security | [4. Security](July-2026/4-Security/notes.md#sec-4) | [notes](July-2026/4-Security/notes.md) |
| 05 | Environment | [5. Environment](July-2026/5-Environment/notes.md#sec-5) | [notes](July-2026/5-Environment/notes.md) |
| 06 | Social Issues | [6. Social Issues](July-2026/6-Social-Issues/notes.md#sec-6) | [notes](July-2026/6-Social-Issues/notes.md) |
| 07 | Science & Technology | [7. Science & Technology](July-2026/7-Science-and-Technology/notes.md#sec-7) | [notes](July-2026/7-Science-and-Technology/notes.md) |
| 08 | Culture | [8. Culture](July-2026/8-Culture/notes.md#sec-8) | [notes](July-2026/8-Culture/notes.md) |
| 09 | Schemes in News | [9. Schemes in News](July-2026/9-Schemes-in-News/notes.md#sec-9) | [notes](July-2026/9-Schemes-in-News/notes.md) |
| 10 | Places in News | [10. Places in News](July-2026/10-Places-in-News/notes.md#sec-10) | [notes](July-2026/10-Places-in-News/notes.md) |

## How to use

- Start at a month's **index** file, then use its **clickable Table of Contents**
  to jump straight to any item; each section file's **↑ Back to Monthly Index**
  links return you to the index.
- Or open an individual section folder to revise one topic at a time.
- To add a future month, create the folder and its section files, then run
  `python3 tools/build_month_index.py <month-folder>` to (re)generate its index.

## Visuals & image credits

- Diagrams are authored in **Mermaid** directly in the section files (flowcharts,
  timelines, mind-maps) or as self-authored **SVG** assets under
  `July-2026/assets/`; these are original and carry no third-party rights.
- External images are included only when they are **public domain**, with the
  source and licence given in the caption. Currently: a public-domain 1880s
  photograph of the Dhamek Stupa, Sarnath (Wikimedia Commons) and a NASA MODIS
  satellite image of the Strait of Hormuz (public domain, NASA).

## Reference

- `6_CURRENT_AFFAIRS_JUNE_2026.pdf` (kept locally at the repository root, not
  committed) — a sample monthly magazine kept only as a **format reference**.
  All rights belong to its original publisher.

## Disclaimer

This repository is an independent study aid. It is not affiliated with, endorsed
by, or a reproduction of any coaching institute's material. Content is compiled
from publicly reported developments and should be cross-verified against official
sources (PIB, ministry websites, The Hindu, Indian Express) before use.
