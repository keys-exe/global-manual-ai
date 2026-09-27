#!/usr/bin/env python3
"""§30I — camera angle range: check an act map (or a scene's shot list) for stuck angles.

Usage:
  angles.py ROWS.json [--json]

ROWS.json is a list of shot/beat rows in cut order (talking heads may be included — they are skipped):
  [{"beat": "BF-SC02-SH01", "group": "SC-02",        # scene id (film) or act id (everything else)
    "type": "BR" | "TH" | "SHOT" | "INSERT" | "POV" | "CCTV",
    "subject": "S1",                                  # who or what the shot is on
    "height": "ground" | "low" | "eye" | "high" | "overhead",
    "side": "front" | "three-quarter" | "profile" | "three-quarter-back" | "behind" | "ots",
    "scale": "WIDE" | "FULL" | "MEDIUM" | "MCU" | "CU" | "ECU",
    "fg": "clean" | "through" | "reflection",
    "why": "what the angle says (§30I meaning table)",
    "mirror_of": null}                                # a payoff shot repeating another beat's angle on purpose (§3B)
  ...]

Checks (any FAIL → exit 1):
  JUMP     consecutive shots on the same subject share height, side and scale (§30A rule 2)
  RUN      the same height+side three times in a row
  WINDOW   any five consecutive shots with fewer than three distinct setups (height+side)
  DEFAULT  eye-level frontal over one third of a group's shots
  HEIGHT   a group of four or more shots all at one height
  WHY      a non-eye-level height, a profile/behind/OTS side or a through/reflection foreground with no `why`
Talking heads (TH), POV and CCTV rows are seed- or mount-locked and skipped (§30A rules 6–7, §22E).
"""
import argparse, json, sys
from collections import defaultdict
from pathlib import Path

SKIP = {"TH", "POV", "CCTV"}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("rows")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    rows = [r for r in json.loads(Path(a.rows).read_text()) if r.get("type") not in SKIP]
    out = []

    def fail(kind, beats, detail):
        out.append({"check": kind, "beats": beats, "detail": detail})

    setup = lambda r: (r.get("height"), r.get("side"))
    for i, r in enumerate(rows):
        for k in ("height", "side", "scale"):
            if not r.get(k):
                fail("MISSING", [r.get("beat")], f"no {k}")
        if (r.get("height") not in (None, "eye") or r.get("side") in ("profile", "three-quarter-back", "behind", "ots")
                or r.get("fg") in ("through", "reflection")) and not r.get("why"):
            fail("WHY", [r["beat"]], "angle has no stated reason")
        if i and not r.get("mirror_of"):
            p = rows[i - 1]
            if p.get("subject") == r.get("subject") and setup(p) == setup(r) and p.get("scale") == r.get("scale"):
                fail("JUMP", [p["beat"], r["beat"]], "same subject, angle and scale back to back")
        if i >= 2 and setup(rows[i - 2]) == setup(rows[i - 1]) == setup(r):
            fail("RUN", [rows[i - 2]["beat"], rows[i - 1]["beat"], r["beat"]], f"{setup(r)} three in a row")
        if i >= 4:
            w = rows[i - 4:i + 1]
            if len({setup(x) for x in w}) < 3:
                fail("WINDOW", [x["beat"] for x in w], f"{len({setup(x) for x in w})} setups in five shots")

    groups = defaultdict(list)
    for r in rows:
        groups[r.get("group", "?")].append(r)
    for g, rs in groups.items():
        ef = sum(1 for r in rs if r.get("height") == "eye" and r.get("side") == "front")
        if rs and ef * 3 > len(rs):
            fail("DEFAULT", [g], f"eye-level frontal {ef}/{len(rs)} shots")
        if len(rs) >= 4 and len({r.get("height") for r in rs}) == 1:
            fail("HEIGHT", [g], f"all {len(rs)} shots at {rs[0].get('height')}")

    dist = defaultdict(int)
    for r in rows:
        dist[f"{r.get('height')}/{r.get('side')}"] += 1
    if a.json:
        print(json.dumps({"pass": not out, "fails": out, "setups": dist}, indent=1))
    else:
        for f in out:
            print(f"FAIL  {f['check']:8} {', '.join(map(str, f['beats']))}  — {f['detail']}")
        print("setups: " + ", ".join(f"{k} ×{v}" for k, v in sorted(dist.items(), key=lambda x: -x[1])))
        print("ANGLES PASS" if not out else f"ANGLES FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
