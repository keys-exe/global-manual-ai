#!/usr/bin/env python3
"""§22U step 8 — pull the spoken lines out of a script file, verbatim.

Usage:
  script_lines.py SCRIPT(.docx|.txt|.md|.pdf) [--out LINES.txt]

Keeps every spoken line exactly as written (no word added, removed or changed).
Drops only what is never spoken:
  - the title (first non-empty line)
  - section headings: short lines with no sentence punctuation (Hooks, Body, CTA,
    Hook 1, Offer ...)
  - reference / link lines (Reference:, Ref:, Link:, Source:, any line with a URL)
  - visual and editor notes: whole lines in [brackets] or (parentheses), or lines
    starting VISUAL / B-ROLL / BROLL / SHOT / SCENE / ON SCREEN / TEXT / SFX /
    MUSIC / NOTE / EDITOR / CAPTION / SUPER
Prints JSON: the kept lines, and every dropped line with the reason, so nothing
leaves the script silently.
"""
import argparse, json, re, sys
from pathlib import Path

NOTE_PREFIX = re.compile(r"^\s*(visual|visuals|b-?roll|shot|scene|on[- ]screen|text|sfx|music|note|notes|"
                         r"editor|caption|super|overlay)\b\s*[:\-–]", re.I)
REF_PREFIX = re.compile(r"^\s*(reference|ref|link|source|inspo)\s*[:\-–]", re.I)
URL = re.compile(r"https?://|www\.", re.I)


def read(path):
    p = Path(path)
    ext = p.suffix.lower()
    if ext == ".docx":
        import docx
        return [para.text for para in docx.Document(str(p)).paragraphs]
    if ext == ".pdf":
        from pypdf import PdfReader
        return "\n".join((pg.extract_text() or "") for pg in PdfReader(str(p)).pages).splitlines()
    return p.read_text(encoding="utf-8").splitlines()


def classify(line):
    s = line.strip()
    if REF_PREFIX.match(s) or URL.search(s):
        return "reference/link"
    if NOTE_PREFIX.match(s):
        return "visual/editor note"
    if (s.startswith("[") and s.endswith("]")) or (s.startswith("(") and s.endswith(")")):
        return "bracketed direction"
    if len(s.split()) <= 4 and not re.search(r"[.!?,;:\"'…]", s):
        return "section heading"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--out")
    a = ap.parse_args()
    raw = read(a.script)
    kept, dropped, title_done = [], [], False
    for n, line in enumerate(raw, 1):
        if not line.strip():
            continue
        if not title_done:
            title_done = True
            dropped.append({"line": n, "text": line.strip(), "reason": "title"})
            continue
        why = classify(line)
        if why:
            dropped.append({"line": n, "text": line.strip(), "reason": why})
        else:
            kept.append(line.strip())
    text = "\n".join(kept)
    out = Path(a.out) if a.out else Path(a.script).with_suffix(".lines.txt")
    out.write_text(text + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "spoken_lines": len(kept), "words": len(text.split()),
                      "chars": len(text), "dropped": dropped, "lines": kept}, indent=2))


if __name__ == "__main__":
    main()
