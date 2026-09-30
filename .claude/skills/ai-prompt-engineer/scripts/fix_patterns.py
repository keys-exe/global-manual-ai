#!/usr/bin/env python3
"""§34A — harvest every Fix note from Generation Board dumps, so the patterns can be learned.

Usage:
  fix_patterns.py DIR [DIR ...] [--md OUT.md] [--json OUT.json]

Each DIR is an ArtifactData `list` dump of a board's `generations` collection
(out_dir=<DIR>, files at <DIR>/generations/<doc_id>.json). Current and Old boards
both count: Old boards hold the replaced versions and the notes that replaced them.

A Fix note is any of: `imageFault` / `fault` on a card, or the `note` on an
`imageVersions` / `videoVersions` entry after v1 (the note that produced it).
Agent verdict notes (`Q<n>: …`) are the agent's own §22V/§22W reads, not the
user's, and are listed apart. Notes are de-duplicated per build + beat + step.

Output: one row per note (build, beat, stage, step, v, model, note) and counts by
a rough keyword class, as a starting point for the reading in §34A — the classes
are a triage aid, never the lesson itself.
"""
import argparse, glob, json, re, sys
from collections import Counter
from pathlib import Path

CLASSES = [  # first match wins; a triage aid only
    ("text/logo", r"letter|logo|text|label|swoosh|brand|writing|readable"),           # §6A Part 2 rule 5 / HT18
    ("clutter", r"belonging|remove the|clutter|phone|pen mug|props?\b|on the table|nothing on"),   # rule 4 / HT19
    ("plate-match", r"location plate|use the plate|same (?:stair|room|hall)|match the plate"),    # rule 3 / HT17
    ("gaze", r"face (?:in|to|the) camera|look(?:ing)? at the camera|eyes on|turned away"),        # rule 6 / HT20
    ("product", r"product|strap|brace|stryde|shell|wordmark|box|pack|fake|copy"),
    ("placement", r"below|above|knee ?cap|tendon|spot|placement|side of|wrong spot"),
    ("size", r"\bbig\b|small|size|huge|tiny"),
    ("anatomy", r"leg|finger|hand|arm|limb|third|extra|foot|feet|face|distort"),
    ("stairs/place", r"stair|step|rail|banister|wall|room|location|counter|church"),
    ("story/plan", r"productive|struggl|happy|fast|slow|carry|running|should be|instead|new one|other activ|concept|reaction"),
    ("motion/feel", r"zoom|frozen|stiff|physics|moving|walk|motion|staged|natural"),
    ("camera", r"angle|close|wide|frame|top of|from the|pov|view"),
]
AGENT = re.compile(r"^\s*Q\d+\s*:")
LOG = re.compile(r"^(?:task|job|kie|preflight|@\w+|gen(?:eration)? ?\d|first render|refs? |same prompt|from confirmed frame|trimmed |cut \d|verify |redo at |\d+(?:\.\d+)?–\d)", re.I)


def clean(n):
    """Drop the agent's bookkeeping segments (task ids, preflight, refs) from a version note."""
    parts = [x.strip() for x in re.split(r"\s+·\s+", n or "")]
    keep = [x for x in parts if x and not LOG.match(x) and not re.fullmatch(r"[0-9a-f-]{8,}", x)]
    return " · ".join(keep).strip()


def klass(n):
    t = n.lower()
    for name, rx in CLASSES:
        if re.search(rx, t):
            return name
    return "other"


def notes_of(g):
    out = []
    for step, fault, vers, model in (("image", "imageFault", "imageVersions", "imageModel"), ("video", "fault", "videoVersions", "model")):
        seen = set()
        for x in g.get(vers) or []:
            n = clean(x.get("note"))
            if n and int(x.get("v") or 1) > 1 and n not in seen:
                seen.add(n); out.append((step, x.get("v"), x.get("model") or g.get(model) or "", n))
        f = clean(g.get(fault))
        if f and f not in seen:
            out.append((step, "open", g.get(model) or "", f))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--md"); ap.add_argument("--json")
    ap.add_argument("--all-stages", action="store_true", help="include voice, VO, talking heads and edit (mostly process logs)")
    a = ap.parse_args()
    rows, seen = [], set()
    for d in a.dirs:
        for f in sorted(glob.glob(str(Path(d) / "**" / "*.json"), recursive=True)):
            try:
                g = json.load(open(f)); g = g.get("data", g)
            except Exception:
                continue
            if not isinstance(g, dict) or not g.get("beat"):
                continue
            if not a.all_stages and g.get("stage") in ("voice", "vo", "talking", "edit"):
                continue
            build = g.get("build") or Path(d).name
            for step, v, model, n in notes_of(g):
                key = (build, g["beat"], step, n)
                if key in seen:
                    continue
                seen.add(key)
                rows.append({"build": build, "beat": g["beat"], "stage": g.get("stage", ""), "step": step, "v": v,
                             "model": model, "who": "agent" if AGENT.match(n) else "user", "class": klass(n), "note": n})
    user = [r for r in rows if r["who"] == "user"]
    cnt = Counter((r["step"], r["class"]) for r in user)
    lines = [f"# Fix notes — {len(user)} from the user, {len(rows) - len(user)} agent verdicts", "",
             "| step | class | notes |", "|---|---|---|"]
    lines += [f"| {s} | {c} | {n} |" for (s, c), n in sorted(cnt.items(), key=lambda x: -x[1])]
    lines += ["", "| build | beat | stage | step | v | model | class | note |", "|---|---|---|---|---|---|---|---|"]
    for r in sorted(user, key=lambda r: (r["build"], r["beat"], r["step"])):
        lines.append("| {build} | {beat} | {stage} | {step} | {v} | {model} | {class} | {n} |".format(**r, n=r["note"].replace("|", "/").replace("\n", " ")))
    md = "\n".join(lines) + "\n"
    if a.md:
        Path(a.md).write_text(md)
    if a.json:
        Path(a.json).write_text(json.dumps(rows, indent=1, ensure_ascii=False))
    if not a.md:
        sys.stdout.write(md)
    else:
        print(f"{len(user)} user notes, {len(rows) - len(user)} agent verdicts → {a.md}")


if __name__ == "__main__":
    main()
