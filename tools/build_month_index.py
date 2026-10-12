#!/usr/bin/env python3
"""Build a month index (cover + Table of Contents) for a month folder.

The per-section files under ``<month>/<n>-<Section>/notes.md`` are the single
source of truth for content.  This script keeps the combined monthly file
content-free (an index only) by:

  1. Adding a portable HTML anchor (``<a id="sec-...">``) before every heading in
     each section file, plus a "Back to Monthly Index" link at the top and bottom.
  2. Rewriting the combined monthly file so that it keeps its cover/preamble and
     rebuilds its Table of Contents, with every entry linking into the matching
     section file and anchor.

Usage:
    python3 tools/build_month_index.py July-2026

The operation is idempotent: re-running it does not duplicate anchors or links.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ANCHOR_RE = re.compile(r'^<a id="sec-[a-z0-9-]+"></a>$')
HEADING_RE = re.compile(r"^(#{1,6}) (.+?)\s*$")
NUMBER_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s")
BACKLINK_TEXT = "Back to Monthly Index"
MAX_TOC_LEVEL = 3
TOC_MARKER = '<a id="toc"></a>'

DEFAULT_COVER = (
    "# CURRENT AFFAIRS\n\n"
    "> **About this compilation.** This document is an independently prepared\n"
    "> study aid. The full content lives in the per-section files listed below.\n"
)


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def anchor_id(heading_text: str) -> str:
    match = NUMBER_RE.match(heading_text)
    if match:
        return "sec-" + match.group(1).replace(".", "-")
    return "sec-" + slugify(heading_text)


def section_folders(month_dir: Path) -> list[Path]:
    folders = []
    for path in month_dir.iterdir():
        if (
            path.is_dir()
            and re.match(r"^\d+-", path.name)
            and (path / "notes.md").is_file()
        ):
            folders.append((int(path.name.split("-", 1)[0]), path))
    folders.sort(key=lambda item: item[0])
    return [path for _, path in folders]


def combined_file(month_dir: Path) -> Path:
    candidates = [
        path
        for path in sorted(month_dir.glob("*.md"))
        if path.name.lower() != "readme.md"
    ]
    if not candidates:
        raise SystemExit(f"no combined .md file found in {month_dir}")
    return candidates[0]


def process_section(notes_path: Path, combined_name: str) -> tuple[str, list]:
    backlink = f"[↑ {BACKLINK_TEXT}](../{combined_name}#toc)"
    raw = notes_path.read_text(encoding="utf-8").split("\n")

    out: list[str] = []
    toc: list[tuple[int, str, str]] = []
    top_done = False

    for line in raw:
        if ANCHOR_RE.match(line):
            continue
        if BACKLINK_TEXT in line:
            # Remove the back-link together with the blank line we inserted
            # before it, so re-runs stay stable.
            if out and out[-1] == "":
                out.pop()
            continue
        match = HEADING_RE.match(line)
        if match:
            level = len(match.group(1))
            text = match.group(2).strip()
            anchor = anchor_id(text)
            out.append(f'<a id="{anchor}"></a>')
            out.append(f"{match.group(1)} {text}")
            if level <= MAX_TOC_LEVEL:
                toc.append((level, text, anchor))
            if level == 1 and not top_done:
                out.append("")
                out.append(backlink)
                top_done = True
        else:
            out.append(line)

    while out and out[-1] == "":
        out.pop()
    out.append("")
    out.append(backlink)

    return "\n".join(out) + "\n", toc


def build_index(month_dir: Path, combined_path: Path, toc: list[tuple[str, int, str, str]]) -> None:
    text = combined_path.read_text(encoding="utf-8")
    index = text.find(TOC_MARKER)
    cover = text[:index] if index != -1 else DEFAULT_COVER
    if cover and not cover.endswith("\n"):
        cover += "\n"

    lines = [TOC_MARKER, "## Table of Contents", ""]
    for folder, level, title, anchor in toc:
        indent = "  " * (level - 1)
        lines.append(f"{indent}- [{title}]({folder}/notes.md#{anchor})")
    lines.append("")

    combined_path.write_text(cover + "\n".join(lines), encoding="utf-8")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print(__doc__)
        return 2

    month_dir = Path(argv[1]).resolve()
    if not month_dir.is_dir():
        raise SystemExit(f"not a directory: {month_dir}")

    combined_path = combined_file(month_dir)
    folders = section_folders(month_dir)
    if not folders:
        raise SystemExit(f"no section folders found in {month_dir}")

    toc: list[tuple[str, int, str, str]] = []
    for folder in folders:
        notes_path = folder / "notes.md"
        new_text, entries = process_section(notes_path, combined_path.name)
        notes_path.write_text(new_text, encoding="utf-8")
        toc.extend((folder.name, level, title, anchor) for level, title, anchor in entries)
        print(f"section: {notes_path.relative_to(month_dir)} ({len(entries)} headings)")

    build_index(month_dir, combined_path, toc)
    print(f"index:   {combined_path.relative_to(month_dir)} ({len(toc)} TOC entries)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
