#!/usr/bin/env python3
"""§24P — Hollywood drama blocking and coverage for film builds (Modes 4 and 5, V7.96.0).

User, 2026-10-03: "I also want to improve the movie style a lot" — look & light, camera & shots, acting & faces,
edit, pace & sound — "holywood drama movies". The film builds' Fix notes were mostly geography: the wrong side of
the stairs, the wrong floor, people swapping places or starting a take somewhere else, props changing size, shots
"not connected", shots that "feel like an image only", slow-downs in the edit. This checks the act map for what a
drama's script supervisor and first AD hold before anyone rolls.

Usage:
  blocking.py ACT_MAP.json --sets SETS.json [--md blocking.md] [--json]

SETS.json — one set map per location, written at step 5 from the location's plate (§24P part 2):
  {"L-STAIRS": {"view": "from the hall at the foot of the stairs",
                "landmarks": {"banister": "right of frame, the full flight",
                              "photo wall": "left of frame, seven mahogany frames",
                              "front door": "behind the camera, green",
                              "landing": "top of the flight — the first floor"},
                "levels": ["hall (ground floor)", "landing (first floor)"],
                "props": {"strap": "12 x 5 cm, smaller than her palm"},
                "still": ["escalator"]}}            # machines that must not move: kept out of frame (HT22)

Film rows (type SHOT / INSERT, mode 4 or 5) add, on top of their usual fields:
  "marks": {"N": "on the landing, left of the banister"}   every cast member in frame: where they are at frame 1,
                                                            said against a landmark of the location's set map
  "end_marks": {...}                                        last row of a take: where they are on its last frame
  "time_cut": true                                          the take starts later in time (people may have moved)
  "axis": "the line between Her and Barbara across the table"   first row of a scene with 2+ people
  "axis_side": "A" | "B" | "neutral"                        which side of the line the camera is on
  "cross": true                                             a shot that crosses the line on a move, on purpose
  "dir": "L>R" | "R>L" | "toward" | "away" | "none"         screen direction of a travelling subject
  "coverage": "establish" | "master" | "ots" | "single" | "close" | "reaction" | "insert" | "cutaway"
  "turn": true                                              the scene's emotional turn (one row per scene)
  "beat_before": 1.0                                        seconds held before the key line on the turn row
  "motion": "her hand slides the strap up; she straightens"  what moves on screen from the first frame to the last

Checks (any FAIL -> exit 1):
  SETMAP    every film row's location has a set map with at least three landmarks
  MARKS     every cast member of a row has a mark, and each mark names one of the location's landmarks
  CARRY     a take's first marks repeat the previous take's end_marks, word for word, unless time_cut (same scene)
  AXIS      a scene with two or more people names its axis; every row of it keeps one axis_side (neutral and cross
            allowed); a scene never flips side without a cross row
  DIR       a travelling subject keeps its screen direction across consecutive rows of a scene unless cross
  COVER     a scene opening in a new location starts with an establish (or master) row; a scene where 2+ people
            speak has a reaction row; the turn row is a single or close at MCU, CU or ECU and carries beat_before
  RESERVE   every narrated scene (a row with vo) has at least one cutaway, insert or reaction row of 2 s or more —
            the edit covers a gap with it, never by slowing a clip below 0.8x
  STILL     every row names its motion; a locked camera (rig F2) with no motion, or a motion of only standing,
            sitting, looking or holding, is a still picture
  PROPS     every prop a row names from the set map keeps the set map's size words in its action (one size per film)
"""
import argparse, json, re, sys
from pathlib import Path

FILM = {"SHOT", "INSERT"}
# Builds that existed at V7.96.0 keep their film plans (a system update never touches existing builds)
PRE_DRAMA = {"facelove-my-mother", "facelove-paint-wall", "facelove-returning-it", "identity-callout-v2", "intake-1", "sha0071", "six-weeks-ago", "stryde-71-stairs", "stryde-71-stairs-pixar-song", "stryde-cascade", "stryde-failed-alternatives", "stryde-half-my-age", "stryde-her-dad", "stryde-identity", "stryde-lost-moments", "stryde-not-your-cartilage", "stryde-regrets", "stryde-the-impression", "stryde-thirty-years", "stryde-three-regrets", "stryde-too-bad", "stryde-what-changed", "demo-ad"}
STILL_ONLY = re.compile(r"^\s*(?:she|he|they|her|him|\w+)?\s*(?:stands?|sits?|looks?|holds?|waits?|stays?|is|are|remains?)\b[^,.;]*$", re.I)
MOVE = re.compile(r"\b(?:walk|step|climb|turn|reach|lift|lower|slide|press|pull|push|open|close|lean|rise|stand(?:s|ing)? up|sit(?:s|ting)? down|"
                  r"breath|exhal|inhal|nod|shake|swallow|drink|pour|hand(?:s|ing)? (?:it|her|him|over)|wipe|tap|touch|bend|straighten|"
                  r"blink|glance|look(?:s|ing)? (?:down|up|away|back|over|round|across|out)|drift|sway|flick|tighten|loosen|run|carry|drop|pick|set|place|put|move|shift|rock|roll|wave|smile|laugh|cry|tear)",
                  re.I)


def film_rows(rows):
    return [r for r in rows if str(r.get("type", "SHOT")).upper() in FILM and int(r.get("mode") or 4) in (4, 5)]


def scene(r):
    return r.get("scene") or r.get("group")


def people(r):
    c = r.get("cast")
    return [x for x in c if x] if isinstance(c, list) else []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("actmap")
    ap.add_argument("--sets", required=True)
    ap.add_argument("--md")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    parts = Path(a.actmap).resolve().parts
    if "builds" in parts[:-1] and parts[parts.index("builds") + 1] in PRE_DRAMA:
        print("BLOCKING SKIPPED (a build from before V7.96.0 keeps its plan)")
        sys.exit(0)
    data = json.loads(Path(a.actmap).read_text())
    rows = film_rows(data if isinstance(data, list) else data.get("rows", []))
    sets = json.loads(Path(a.sets).read_text())
    out = []

    def fail(kind, beats, detail):
        out.append({"check": kind, "beats": beats, "detail": detail})

    if not rows:
        print("BLOCKING PASS (no film shots)")
        sys.exit(0)

    # SETMAP / MARKS / STILL / PROPS, row by row
    for r in rows:
        b = r.get("beat", "?")
        loc = r.get("location")
        sm = sets.get(loc) if loc else None
        lms = list((sm or {}).get("landmarks") or {})
        if loc and len(lms) < 3:
            fail("SETMAP", [b], f"location {loc} has {len(lms)} landmark(s) on its set map — write at least three, each with its screen side")
        marks = r.get("marks") or {}
        for p in people(r):
            m = marks.get(p)
            if not m:
                fail("MARKS", [b], f"{p} has no mark — where they are at frame 1, against a landmark of {loc}")
            elif lms and not any(l.lower() in m.lower() for l in lms):
                fail("MARKS", [b], f"{p}'s mark {m!r} names none of {loc}'s landmarks ({', '.join(lms)})")
        mo = str(r.get("motion") or "").strip()
        if not mo:
            fail("STILL", [b], "no motion — say what moves on screen from the first frame to the last")
        elif not MOVE.search(mo) or STILL_ONLY.match(mo):
            fail("STILL", [b], f"motion {mo!r} is a still picture — give the subject a continuous physical action (a breath, a hand, a step)")
        for prop, size in ((sm or {}).get("props") or {}).items():
            act = f"{r.get('action', '')} {mo}"
            if re.search(rf"\b{re.escape(prop)}\b", act, re.I):
                key = re.findall(r"\d+(?:\s*[x×]\s*\d+)?\s*cm|smaller than [\w ]+|no (?:longer|bigger) than [\w ]+", size, re.I)
                if key and not any(k.lower() in act.lower() for k in key):
                    fail("PROPS", [b], f"{prop} without its set-map size ({size}) — one size per film")

    # by scene
    by = {}
    for r in rows:
        by.setdefault(scene(r), []).append(r)
    seen_locs = set()
    for sc, rs in by.items():
        beats = [r.get("beat") for r in rs]
        cast = {p for r in rs for p in people(r)}
        # COVER — establish a new place
        loc = rs[0].get("location")
        if loc and loc not in seen_locs and rs[0].get("coverage") not in ("establish", "master"):
            fail("COVER", beats[:1], f"scene {sc} opens in {loc} for the first time without an establish or master shot")
        seen_locs.update(r.get("location") for r in rs if r.get("location"))
        talk = sum(1 for r in rs if r.get("speaking") or r.get("lines"))
        if len(cast) >= 2 and talk >= 2 and not any(r.get("coverage") == "reaction" for r in rs):
            fail("COVER", beats, f"scene {sc}: people talk but no reaction row — the listener's face as the words land")
        turns = [r for r in rs if r.get("turn")]
        if len(rs) >= 3 and not turns:
            fail("COVER", beats, f"scene {sc} has no turn row — mark the emotional turn (turn: true)")
        for t in turns:
            if t.get("coverage") not in ("single", "close") or str(t.get("scale", "")).upper() not in ("MCU", "CU", "ECU"):
                fail("COVER", [t.get("beat")], "the turn is played in a single or close at MCU / CU / ECU")
            if not t.get("beat_before"):
                fail("COVER", [t.get("beat")], "the turn row has no beat_before — the held look before the key line (0.5–1.5 s)")
        # RESERVE — cover narration gaps with pictures, never by slowing
        if any(r.get("vo") for r in rs):
            res = [r for r in rs if r.get("coverage") in ("cutaway", "insert", "reaction") and float(r.get("duration") or r.get("hold_s") or 2) >= 2]
            if not res:
                fail("RESERVE", beats, f"scene {sc} is narrated but has no cutaway, insert or reaction of 2 s+ — plan one so the edit never slows a clip below 0.8x")
        # AXIS
        if len(cast) >= 2:
            if not any(r.get("axis") for r in rs):
                fail("AXIS", beats[:1], f"scene {sc} has two or more people and no axis — name the line between them")
            side = None
            for r in rs:
                s = r.get("axis_side")
                if s in (None, "", "neutral"):
                    continue
                if side and s != side and not r.get("cross"):
                    fail("AXIS", [r.get("beat")], f"the camera jumps the line ({side} → {s}) without a cross row")
                side = s
        # DIR
        last = {}
        for r in rs:
            d = r.get("dir")
            if d not in ("L>R", "R>L"):
                continue
            subj = r.get("subject")
            if subj in last and last[subj] != d and not r.get("cross"):
                fail("DIR", [r.get("beat")], f"{subj} travels {last[subj]} then {d} without a cross — keep the screen direction")
            last[subj] = d
        # CARRY — take to take, marks word for word
        takes, order = {}, []
        for r in rs:
            t = r.get("take") or r.get("beat")
            if t not in takes:
                takes[t] = []
                order.append(t)
            takes[t].append(r)
        for t0, t1 in zip(order, order[1:]):
            end = takes[t0][-1].get("end_marks") or {}
            first = takes[t1][0]
            if first.get("time_cut"):
                continue
            for p, m in (first.get("marks") or {}).items():
                if p in end and end[p].strip().lower() != m.strip().lower():
                    fail("CARRY", [takes[t0][-1].get("beat"), first.get("beat")],
                         f"{p} ends {t0} at {end[p]!r} but starts {t1} at {m!r} — repeat the end mark word for word, or mark time_cut")
            for p in people(first):
                if p not in end and len(takes[t0][-1].get("cast") or []) and p in (takes[t0][-1].get("cast") or []):
                    fail("CARRY", [takes[t0][-1].get("beat")], f"{t0}'s last row has no end_marks for {p}")

    if a.md:
        md = ["### Blocking — set maps and marks", "", "Where everyone stands, shot by shot, against each location's fixed landmarks (§24P part 2).", ""]
        for loc, sm in sets.items():
            md += [f"**{loc}** — {sm.get('view', '')}", "", "| Landmark | Where |", "|---|---|"]
            md += [f"| {k} | {v} |" for k, v in (sm.get("landmarks") or {}).items()]
            if sm.get("props"):
                md += ["", "| Prop | Size |", "|---|---|"] + [f"| {k} | {v} |" for k, v in sm["props"].items()]
            md.append("")
        md += ["| Beat | Take | Coverage | Marks | Motion |", "|---|---|---|---|---|"]
        for r in rows:
            mk = "; ".join(f"{k}: {v}" for k, v in (r.get("marks") or {}).items())
            md.append(f"| {r.get('beat')} | {r.get('take', '')} | {r.get('coverage', '')}{' · turn' if r.get('turn') else ''} | {mk} | {r.get('motion', '')} |")
        Path(a.md).write_text("\n".join(md) + "\n", encoding="utf-8")

    if a.json:
        print(json.dumps({"pass": not out, "rows": len(rows), "fails": out}, indent=1))
    else:
        for f in out:
            print(f"FAIL  {f['check']:7} {', '.join(str(b) for b in f['beats'] if b)}  — {f['detail']}")
        print(f"BLOCKING PASS ({len(rows)} film shots)" if not out else f"BLOCKING FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
