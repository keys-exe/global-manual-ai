#!/usr/bin/env python3
"""§22U step 8 — pull the spoken lines out of a script file, verbatim.

Usage:
  script_lines.py SCRIPT(.docx|.txt|.md|.pdf) [--out LINES.txt] [--visual VISUAL.md]

Keeps every spoken line exactly as written (no word added, removed or changed).
Drops only what is never spoken:
  - the title (first non-empty line)
  - section headings: short lines with no sentence punctuation (Hooks, Body, CTA,
    Hook 1, Offer ...)
  - reference / link lines (Reference:, Ref:, Link:, Source:, any line with a URL)
  - visual and editor notes: whole lines in [brackets] or (parentheses), or lines
    starting VISUAL / B-ROLL / BROLL / SHOT / SCENE / ON SCREEN / TEXT / SFX /
    MUSIC / NOTE / EDITOR / CAPTION / SUPER
  - inline [bracketed] notes inside a spoken line (square brackets are never
    spoken): cut out of the line, the rest of the line kept word for word
  - speaker labels at the start of a spoken line (VO:, V.O.:, NARRATOR:, SARAH:,
    DR. LEE: ...): cut off, the rest of the line kept word for word
.docx tables are read in document order (V7.61.1). A table whose header row names a
voice column (VO, Voiceover, Voice, Audio, Script, Dialogue, Narration, Copy) and a
visual column (Visual, B-roll, Shot, Scene, Video, On screen, Direction, Notes) is a
two-column script: each row's visual cell becomes a VISUAL note anchored to that
row's spoken line. Any other table is read cell by cell, row by row.
Prints JSON: the kept lines, and every dropped line with the reason, so nothing
leaves the script silently.

§27F: every visual/editor note, bracketed direction and inline note is also a
binding visual instruction. They are listed under "visual_notes" (VN01, VN02...),
each anchored to the spoken line it applies to: the next spoken line, or the
previous one when the note closes a section. --visual writes them as the starting
rows of the Visual Instruction Ledger.
"""
import argparse, json, re, sys
from pathlib import Path

NOTE_PREFIX = re.compile(r"^\s*(visual|visuals|b-?roll|shot|scene|on[- ]screen|text|sfx|music|note|notes|"
                         r"editor|caption|super|overlay)\b\s*[:\-–]", re.I)
REF_PREFIX = re.compile(r"^\s*(reference|ref|link|source|inspo)\s*[:\-–]", re.I)
URL = re.compile(r"https?://|www\.", re.I)
SPEAKER = re.compile(r"^\s*((?:V\.?O\.?|VOICE[- ]?OVER|NARRATOR|NARRATION|ANNCR|ANNOUNCER|"
                     r"[A-Z][A-Z.'\-]*(?: [A-Z][A-Z.'\-]*){0,2})(?:\s*\([^)]*\))?)\s*:\s+(?=\S)")
VOICE_COL = re.compile(r"^\s*(vo|v\.o\.?|voice[- ]?over|voice|audio|script|dialogue|narration|copy|spoken)\b", re.I)
VISUAL_COL = re.compile(r"^\s*(visuals?|b-?roll|shots?|scenes?|video|on[- ]screen|directions?|notes?|images?)\b", re.I)
INLINE = re.compile(r"\s*\[[^\]]*\]\s*")
VISUAL = {"visual/editor note", "bracketed direction"}


def docx_lines(path):
    """Every paragraph and table of a .docx, in document order (tables were skipped before V7.61.1)."""
    import docx
    from docx.table import Table
    from docx.text.paragraph import Paragraph
    d = docx.Document(str(path))
    out = []
    for el in d.element.body.iterchildren():
        tag = el.tag.rsplit("}", 1)[-1]
        if tag == "p":
            out.append(Paragraph(el, d).text)
        elif tag == "tbl":
            out += table_lines(Table(el, d))
    return out


def cell_lines(cell):
    return [t.strip() for t in cell.text.splitlines() if t.strip()]


def table_lines(t):
    rows = [[c for c in r.cells] for r in t.rows]
    if not rows:
        return []
    head = [c.text.strip() for c in rows[0]]
    vo = next((i for i, h in enumerate(head) if VOICE_COL.match(h)), None)
    vis = next((i for i, h in enumerate(head) if VISUAL_COL.match(h) and i != vo), None)
    out = []
    if vo is not None and vis is not None:  # two-column script: visual cell anchors to its row
        for r in rows[1:]:
            out += [f"VISUAL: {x}" for x in cell_lines(r[vis])] if vis < len(r) else []
            out += cell_lines(r[vo]) if vo < len(r) else []
        return out
    for r in rows:
        seen, row = set(), []
        for c in r:
            if id(c._tc) in seen:  # merged cells repeat
                continue
            seen.add(id(c._tc))
            row += cell_lines(c)
        # a note in a row belongs to that row's spoken line: notes first, then the line
        out += [x for x in row if classify(x)] + [x for x in row if not classify(x)]
    return out


def read(path):
    p = Path(path)
    ext = p.suffix.lower()
    if ext == ".docx":
        return docx_lines(p)
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
    ap.add_argument("--visual")
    a = ap.parse_args()
    raw = read(a.script)
    kept, dropped, notes, title_done = [], [], [], False
    pending = []  # notes waiting for the next spoken line
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
            if why in VISUAL:
                pending.append({"line": n, "text": line.strip(), "kind": why})
            elif why == "section heading" and pending and kept:
                for p in pending:  # a note that closes a section belongs to its last line
                    notes.append({**p, "applies_to": len(kept), "spoken": kept[-1]})
                pending = []
            continue
        s = line.strip()
        inline = [m.strip() for m in re.findall(r"\[[^\]]*\]", s)]
        if inline:
            s = INLINE.sub(" ", s).strip()
            dropped.append({"line": n, "text": " ".join(inline), "reason": "inline note"})
            if not s:
                pending += [{"line": n, "text": t, "kind": "bracketed direction"} for t in inline]
                continue
        m = SPEAKER.match(s)
        if m and m.group(1).upper() not in {"VISUAL", "NOTE", "TEXT"}:
            dropped.append({"line": n, "text": m.group(1), "reason": "speaker label"})
            s = s[m.end():].strip()
        kept.append(s)
        for p in pending:
            notes.append({**p, "applies_to": len(kept), "spoken": s})
        pending = []
        notes += [{"line": n, "text": t, "kind": "inline note", "applies_to": len(kept), "spoken": s}
                  for t in inline]
    for p in pending:
        notes.append({**p, "applies_to": len(kept) or None, "spoken": kept[-1] if kept else None})
    notes.sort(key=lambda x: x["line"])
    for i, v in enumerate(notes, 1):
        v["id"] = f"VN{i:02d}"
    text = "\n".join(kept)
    out = Path(a.out) if a.out else Path(a.script).with_suffix(".lines.txt")
    out.write_text(text + "\n", encoding="utf-8")
    if a.visual:
        md = ["| ID | Source | Instruction | Applies to (spoken line) | Carried by | Beat ID | Status |",
              "|---|---|---|---|---|---|---|"]
        md += [f"| {v['id']} | script L{v['line']} | {v['text']} | {v['applies_to']}: {v['spoken']} | | | open |"
               for v in notes]
        Path(a.visual).write_text("\n".join(md) + "\n", encoding="utf-8")
    print(json.dumps({"out": str(out), "spoken_lines": len(kept), "words": len(text.split()),
                      "chars": len(text), "dropped": dropped, "visual_notes": notes,
                      "lines": kept}, indent=2))


if __name__ == "__main__":
    main()
