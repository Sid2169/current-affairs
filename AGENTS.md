# AGENTS.md — How to build a month of current-affairs notes

This repository holds original, month-wise Current Affairs notes for the UPSC
Civil Services Preliminary Examination, in the section-by-section style of monthly
magazines. Read this file before adding or editing any month.

- Remote: `https://github.com/Sid2169/current-affairs` (public), branch `main`.
- Content is an **independently compiled study aid**, not a reproduction of any
  coaching institute's material.

## Hard rules

- **Never copy** text from a coaching institute's magazine or any copyright work.
  Compile factual items from public sources and write in your own words.
- Keep the disclaimer (in `README.md`) and the "About this compilation" blockquote
  (in each monthly index) intact.
- Give every item a `*Source: ...*` line and cross-verify figures.
- **Images: public domain only**, with source and licence in the caption. Diagrams
  should be self-authored (Mermaid or SVG). No copyrighted photographs.
- Do **not** commit `6_CURRENT_AFFAIRS_JUNE_2026.pdf` (it is gitignored).
- Only commit or push when the user explicitly asks.

## Directory layout

A month is a folder named `<Month>-<Year>` with a capitalised English month and a
4-digit year (e.g. `July-2026`, `August-2026`). Inside it:

```
<Month>-<Year>/
├── CURRENT_AFFAIRS_<MONTH_UPPER>_<YEAR>.md   # monthly INDEX only (cover + TOC)
├── 1-Polity-and-Governance/notes.md          # CONTENT (single source of truth)
├── 2-International-Relations/notes.md
├── 3-Economy/notes.md
├── 4-Security/notes.md
├── 5-Environment/notes.md
├── 6-Social-Issues/notes.md
├── 7-Science-and-Technology/notes.md
├── 8-Culture/notes.md
├── 9-Schemes-in-News/notes.md
├── 10-Places-in-News/notes.md
└── assets/                                   # optional: SVG + public-domain images
```

The ten section names and folder names are fixed and in this exact numbering.
Content lives **only** in the `notes.md` files; the monthly index duplicates none.

## Section file format (`<N>-<Section>/notes.md`)

- H1: `# <N>. <SECTION TITLE IN CAPITALS>` (e.g. `# 3. ECONOMY`).
- **Long-form item**: H2 `## <N>.<k>. <TITLE>` containing subsections such as
  `**Why in News?**`, `**About ...**`, comparison tables, `**Challenges**`,
  `**Way Forward**`, `**Conclusion**`, then a `*Source: ...*` line.
- **News in Shorts**: H2 `## <N>.<k>. NEWS IN SHORTS`, then one H3 per item
  `### <N>.<k>.<m>. <TITLE>` ending with `*Source: ...*`.
- Separate major items with a `---` line.
- **Places in News is special**: H2 `## India` and `## World`, with H3 items
  numbered `### 10.<m>. <PLACE>`.
- Do **not** hand-write anchors (`<a id="...">`) or back-links — the build script
  inserts them.

## Monthly index format (`CURRENT_AFFAIRS_<MONTH_UPPER>_<YEAR>.md`)

Cover only, then the Table of Contents — no section content:

```
# CURRENT AFFAIRS — <MONTH YEAR>

### A Monthly Compilation for the UPSC Civil Services Preliminary Examination

> **About this compilation.** ... (disclaimer blockquote)

**Coverage:** <Month Year> · **Sections:** 10

---

<a id="toc"></a>
## Table of Contents

- [1. POLITY AND GOVERNANCE](1-Polity-and-Governance/notes.md#sec-1)
  - [1.1. ...](1-Polity-and-Governance/notes.md#sec-1-1)
    - [1.1.1. ...](1-Polity-and-Governance/notes.md#sec-1-1-1)
...
```

The script generates the `<a id="toc">` marker and the whole TOC. Do not edit the
TOC by hand — edit the section files and re-run the script.

## Build step (required)

After creating or editing any `notes.md`, run:

```bash
python3 tools/build_month_index.py <Month-Year>
```

The script (idempotent):

1. Discovers section folders matching `^\d+-` that contain `notes.md`, in numeric
   order.
2. Inserts `<a id="sec-..."></a>` before every heading and a
   `[↑ Back to Monthly Index](../<INDEX_FILE>#toc)` link at the top and bottom of
   each section file.
3. Rebuilds the monthly index TOC so every entry (3 levels deep) links to the
   matching `<folder>/notes.md#anchor`.
4. Bootstraps the index (default cover + TOC) if the file does not exist yet.

Anchor scheme: `sec-N`, `sec-N-k`, `sec-N-k-m`; unnumbered H2 → `sec-<slug>`
(e.g. `sec-india`, `sec-world`). Run it twice to confirm the second run changes
nothing.

## Visuals (selective)

- Prefer **Mermaid** inline in the section file: `flowchart` for processes,
  `timeline` for dated sequences, `mindmap` for groupings.
- Use a self-authored **SVG** (in `assets/`) when Mermaid cannot express it.
- Use **public-domain** images (`assets/` + `<img>`/`![]` embed) only when they add
  real value, with a caption crediting the source and licence.
- Typically about one visual per section; skip a section if no visual helps.

## README maintenance

- Add the new month to the **Monthly Index** table.
- Add a **Section Index — <Month> <Year>** table linking each section to its
  `notes.md` (anchor `#sec-N`).

## New-month checklist

1. Create the folder `<Month>-<Year>/`.
2. Create the ten section folders, each with `notes.md`, and write the content in
   the standard format.
3. (Optional) add `assets/` visuals.
4. Run `python3 tools/build_month_index.py <Month-Year>`.
5. Adjust the index cover if needed and re-run the script.
6. Update `README.md` (Monthly Index + Section Index).
7. Verify every link resolves; then commit and push **only if asked**.

## Verification

- `python3 tools/build_month_index.py <Month-Year>` a second time → no changes.
- Every index TOC link's file and `#anchor` exists; no duplicate `<a id>` per file;
  every `![...](../assets/...)` path exists.
