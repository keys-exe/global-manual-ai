#!/usr/bin/env python3
"""§22U step 9 — fit a tagged Eleven v3 script inside the 5,000-character limit.

Usage:
  tts_budget.py SCRIPT.txt [--limit 5000] [--out FITTED.txt]

Counts the full request string (tags, spaces and newlines included) and applies
the budget ladder in order until it fits:
  1. full tagging
  2. strip Rhythm + Vocal Effects (reactions) tags, then Dialogue tags
     (act-opening tags — the first tag of each paragraph — are kept)
  3. strip every tag
  4. split untagged text at paragraph ends into requests <= limit
Also flags any tag not in the library or in a banned category.
BREATH TAGS (V7.60.8): any breath, sigh, gasp, pant or inhale/exhale tag is a
FAIL (exit 2) — breaths are never asked for; E11 cuts the ones the model adds.

VERBATIM LOCK (--script-lines LINES.txt, from script_lines.py): with every tag
removed, the fitted text must be the script's spoken lines word for word — no
word added, removed or changed, nothing re-ordered. Any difference is a FAIL
(exit 2) and the text is never sent to ElevenLabs.
Prints a JSON report; writes the fitted text (parts joined by a line of '=====').
"""
import argparse, json, re
from pathlib import Path

LIB = Path(__file__).parent.parent / "references" / "eleven_v3_tags.json"
BANNED = {"Sound Effects", "Effects", "Environment", "Genre", "Accents", "Humor"}
TAG = re.compile(r"\[[^\[\]]+\]")
BREATH = re.compile(r"breath|sigh|inhal|exhal|gasp|pant|huff", re.I)


def library():
    data = json.loads(LIB.read_text(encoding="utf-8"))
    return {t["tag"].lower().replace("‑", "-"): t["category"] for t in data["tags"]}


def tidy(text):
    text = re.sub(r"[ \t]{2,}", " ", text)
    return re.sub(r" +([,.!?;:])", r"\1", text).strip()


def strip(text, lib, cats):
    out = []
    for para in text.split("\n\n"):
        tags = TAG.findall(para)
        first = tags[0] if tags else None
        def keep(m):
            t = m.group(0)
            if t == first and m.start() == para.find(first):
                return t
            return "" if lib.get(t.lower()) in cats else t
        out.append(tidy(TAG.sub(keep, para)) if cats != "ALL" else tidy(TAG.sub("", para)))
    return "\n\n".join(out)


def split(text, limit):
    parts, cur = [], ""
    for para in text.split("\n\n"):
        cand = f"{cur}\n\n{para}" if cur else para
        if len(cand) <= limit:
            cur = cand
        else:
            if cur:
                parts.append(cur)
            cur = para  # a single paragraph over the limit is reported, never cut
    if cur:
        parts.append(cur)
    return parts


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("script")
    ap.add_argument("--limit", type=int, default=5000)
    ap.add_argument("--out")
    ap.add_argument("--script-lines", help="spoken lines from script_lines.py; enables the verbatim lock")
    a = ap.parse_args()

    lib = library()
    text = Path(a.script).read_text(encoding="utf-8").strip()
    used = TAG.findall(text)
    unknown = sorted({t for t in used if t.lower() not in lib})
    banned = sorted({t for t in used if lib.get(t.lower()) in BANNED})
    breath = sorted({t for t in used if BREATH.search(t)})

    rungs = [
        ("1 full tagging", text),
        ("2a strip rhythm + reactions", strip(text, lib, {"Rhythm", "Vocal Effects"})),
        ("2b strip dialogue moves too", strip(text, lib, {"Rhythm", "Vocal Effects", "Dialogue"})),
        ("3 no tags", strip(text, lib, "ALL")),
    ]
    report = {"limit": a.limit, "tags_used": len(used), "unknown_tags": unknown,
              "banned_category_tags": banned,
              "breath_tags": breath,
              "ladder": [{"rung": r, "chars": len(t)} for r, t in rungs]}
    for rung, t in rungs:
        if len(t) <= a.limit:
            report.update(rung_used=rung, parts=1, chars=len(t))
            fitted = [t]
            break
    else:
        fitted = split(rungs[-1][1], a.limit)
        report.update(rung_used="4 split untagged", parts=len(fitted),
                      part_chars=[len(p) for p in fitted],
                      oversize_paragraph=any(len(p) > a.limit for p in fitted))
    out = Path(a.out) if a.out else Path(a.script).with_suffix(".fitted.txt")
    out.write_text("\n=====\n".join(fitted), encoding="utf-8")
    report["out"] = str(out)
    if a.script_lines:
        want = Path(a.script_lines).read_text(encoding="utf-8").split()
        got = tidy(TAG.sub("", " ".join(fitted))).split()
        report["verbatim"] = "PASS" if got == want else "FAIL"
        if got != want:
            import difflib
            report["verbatim_diff"] = [d for d in difflib.ndiff(want, got) if d[:1] in "+-"][:40]
    print(json.dumps(report, indent=2))
    if report.get("verbatim") == "FAIL" or breath:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
