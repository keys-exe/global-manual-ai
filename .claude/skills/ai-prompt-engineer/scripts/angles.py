#!/usr/bin/env python3
"""§30I / §30J / §30K — camera angle range, focus and light: check an act map (or a scene's shot list).

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
    "mirror_of": null,                                # a payoff shot repeating another beat's angle on purpose (§3B)
    "mode": 1,                                        # §18A mode of this row
    "shot": "SH-OTS" | ["SH-CU", "SH-OTS"],           # Modes 4–5: §24K part 7 library ID(s)
    "speaking": false,                                # carries a lip-synced line
    "product_beat": false,
    "focus": {"plane": "eyes" | "hands" | "product" | "foreground" | "background" | "deep",
              "dof": "deep" | "medium" | "shallow",
              "rack": null | {"from": "...", "to": "...", "cue": "the word or moment", "kind": "pull" | "tap"},
              "moving_subject": false},               # the subject travels toward or away from the lens
    "story_day": 2,
    "face": true,                                     # a face is a subject of the shot
    "light": {"source": "kitchen window, east wall", "key_side": "L" | "R" | "back" | "front",
              "time": "morning" | "midday" | "afternoon" | "evening" | "night",
              "arc": "the act's light state", "why": "reason for a backlit or 90° key",
              "kelvin": 5600}}                         # the key's colour temperature = the scene's white balance
  ...]

Checks (any FAIL → exit 1):
  JUMP     consecutive shots on the same subject share height, side and scale (§30A rule 2)
  RUN      the same height+side three times in a row
  WINDOW   any five consecutive shots with fewer than three distinct setups (height+side)
  DEFAULT  eye-level frontal over one third of a group's shots
  HEIGHT   a group of four or more shots all at one height
  WHY      a non-eye-level height, a profile/behind/OTS side or a through/reflection foreground with no `why`
  FOCUS    (§30J) missing focus plane or depth; shallow on WIDE/FULL; a product beat not focused on the product;
           a rack with no cue, on a travelling or moving shot, or a clean pull in Mode 1 (phones tap to focus);
           shallow on a subject travelling in depth; more than two thirds of a group shallow (the blurred-everything look)
  SHOT     (§24K part 7, Modes 4–5) a film row with no library `shot`, an unknown ID, setup fields that disagree
           with the shot, more than one signature shot per scene / two in a row / over one in five across the film,
           a scene of 5+ shots with fewer than 3 library shots, a wide-angle or fisheye close-up on a face, a
           lip-synced line on a rear/silhouette/aerial/overhead-fisheye shot, a distorting shot on a product beat,
           a Dutch/prism/magnifier/macro shot on a travelling rig (`inspo_ok: true` exempts a shot the inspo uses)
  LIGHT    (§30K) missing light; missing or implausible kelvin (1800–10000K); two white balances for one
           source inside one scene or act group; a flat frontal key on a face; a backlit face with no `why` (never while speaking in
           Mode 1); no light state for the act; time going backwards inside a story day
Talking heads (TH), POV and CCTV rows are seed- or mount-locked and skipped (§30A rules 6–7, §22E).
"""
import argparse, json, sys
from collections import defaultdict
from pathlib import Path

SKIP = {"TH", "POV", "CCTV"}

# §24K part 7 — the 34-shot film library: ID -> required setup fields (a set = any of these values)
LIB = {
    "SH-WIDE": {"scale": {"WIDE"}}, "SH-MED": {"scale": {"MEDIUM"}}, "SH-CU": {"scale": {"CU"}},
    "SH-MACRO": {"scale": {"ECU"}},
    "SH-OVFISH": {"height": {"overhead"}, "scale": {"WIDE"}}, "SH-PROFILE": {"side": {"profile"}},
    "SH-34": {"side": {"three-quarter"}}, "SH-REAR": {"side": {"behind", "three-quarter-back"}},
    "SH-OTS": {"side": {"ots"}}, "SH-POV": {}, "SH-PRISM": {"fg": {"through"}},
    "SH-EYE": {"height": {"eye"}}, "SH-LOW": {"height": {"low"}}, "SH-HIGH": {"height": {"high"}},
    "SH-DUTCH": {}, "SH-OVER": {"height": {"overhead"}},
    "SH-AERIAL": {"height": {"overhead", "high"}, "scale": {"WIDE"}}, "SH-GROUND": {"height": {"ground"}},
    "SH-WORM": {"height": {"ground"}, "scale": {"FULL", "WIDE"}}, "SH-HOLE": {"height": {"ground", "low"}, "fg": {"through"}},
    "SH-HOOP": {}, "SH-WACU": {"scale": {"CU", "ECU"}}, "SH-FISH": {"scale": {"WIDE", "FULL"}},
    "SH-FISHCU": {"scale": {"CU", "ECU"}}, "SH-HICU": {"height": {"high"}, "scale": {"CU"}},
    "SH-LOCU": {"height": {"low"}, "scale": {"CU"}}, "SH-SELFIE": {"height": {"eye", "high"}, "side": {"front"}},
    "SH-SIL": {}, "SH-OCCL": {"fg": {"through"}}, "SH-FGFOC": {"fg": {"through"}},
    "SH-BGFOC": {"fg": {"through"}}, "SH-FLARE": {}, "SH-MAGNIFY": {"fg": {"through"}}, "SH-INSIDE": {"fg": {"through"}},
}
SIGNATURE = {"SH-OVFISH", "SH-PRISM", "SH-DUTCH", "SH-AERIAL", "SH-WORM", "SH-HOLE", "SH-HOOP", "SH-WACU",
             "SH-FISH", "SH-FISHCU", "SH-SELFIE", "SH-FLARE", "SH-MAGNIFY", "SH-INSIDE"}
NO_FACE = {"SH-WACU", "SH-FISHCU"}
NO_LINE = {"SH-REAR", "SH-SIL", "SH-AERIAL", "SH-OVFISH"}
NO_PRODUCT = {"SH-OVFISH", "SH-FISH", "SH-FISHCU", "SH-WACU", "SH-PRISM", "SH-DUTCH", "SH-AERIAL", "SH-SIL", "SH-MAGNIFY"}
LOCKED = {"SH-DUTCH", "SH-PRISM", "SH-MAGNIFY", "SH-MACRO"}


def shots(r):
    s = r.get("shot")
    return [s] if isinstance(s, str) else list(s or [])


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

    TRAVEL_RIGS = {"F1", "F4", "F5", "R1-W", "R1-FAST"}
    for r in rows:
        f = r.get("focus")
        if not f:
            fail("FOCUS", [r.get("beat")], "no focus")
            continue
        if not f.get("plane") or not f.get("dof"):
            fail("FOCUS", [r["beat"]], "focus plane or depth missing")
        if f.get("dof") == "shallow" and r.get("scale") in ("WIDE", "FULL"):
            fail("FOCUS", [r["beat"]], f"shallow depth on a {r.get('scale')}")
        if r.get("product_beat") and f.get("plane") != "product":
            fail("FOCUS", [r["beat"]], "product beat not focused on the product")
        if f.get("dof") == "shallow" and f.get("moving_subject"):
            fail("FOCUS", [r["beat"]], "shallow focus on a subject travelling in depth")
        rk = f.get("rack")
        if rk:
            if not rk.get("cue"):
                fail("FOCUS", [r["beat"]], "rack focus with no cue")
            if r.get("rig") in TRAVEL_RIGS or f.get("moving_subject"):
                fail("FOCUS", [r["beat"]], "rack focus on a travelling camera or moving subject")
            if int(r.get("mode", 1)) == 1 and rk.get("kind") != "tap":
                fail("FOCUS", [r["beat"]], "Mode 1 focus changes are a phone tap-to-focus, never a clean pull")

    film = [r for r in rows if int(r.get("mode", 1)) in (4, 5)]
    for r in film:
        ids = shots(r)
        if not ids:
            fail("SHOT", [r.get("beat")], "film row has no library shot (§24K part 7)")
            continue
        if len(ids) > 2:
            fail("SHOT", [r["beat"]], "more than two library shots on one row")
        for sid in ids:
            if sid not in LIB:
                fail("SHOT", [r["beat"]], f"unknown shot {sid}")
                continue
            for k, allowed in LIB[sid].items():
                if r.get(k) not in allowed:
                    fail("SHOT", [r["beat"]], f"{sid} needs {k} in {sorted(allowed)}, row has {r.get(k)}")
            if sid in NO_FACE and r.get("face"):
                fail("SHOT", [r["beat"]], f"{sid} on a face")
            if sid in NO_LINE and r.get("speaking"):
                fail("SHOT", [r["beat"]], f"lip-synced line on {sid}")
            if sid in NO_PRODUCT and r.get("product_beat"):
                fail("SHOT", [r["beat"]], f"{sid} distorts or hides the product on a product beat")
            if sid in LOCKED and r.get("rig") in TRAVEL_RIGS:
                fail("SHOT", [r["beat"]], f"{sid} on a travelling rig {r.get('rig')}")
            if sid in SIGNATURE and not r.get("why"):
                fail("SHOT", [r["beat"]], f"signature shot {sid} with no why")
    sig = lambda r: bool(SIGNATURE & set(shots(r))) and not r.get("inspo_ok")
    for i in range(1, len(film)):
        if sig(film[i - 1]) and sig(film[i]):
            fail("SHOT", [film[i - 1]["beat"], film[i]["beat"]], "two signature shots in a row")
    if film and sum(map(sig, film)) * 5 > len(film):
        fail("SHOT", ["film"], f"signature shots on {sum(map(sig, film))}/{len(film)} shots — over one in five")
    fg = defaultdict(list)
    for r in film:
        fg[r.get("group", "?")].append(r)
    for g, rs in fg.items():
        n = sum(map(sig, rs))
        if n > 1:
            fail("SHOT", [g], f"{n} signature shots in one scene")
        d = sum(1 for r in rs if shots(r) and "SH-DUTCH" in shots(r))
        if d > 1:
            fail("SHOT", [g], f"{d} Dutch angles in one scene")
        kinds = {sid for r in rs for sid in shots(r)}
        if len(rs) >= 5 and len(kinds) < 3:
            fail("SHOT", [g], f"{len(kinds)} library shots in {len(rs)} shots")

    ORDER = ["morning", "midday", "afternoon", "evening", "night"]
    last_time = {}
    for r in rows:
        L = r.get("light")
        if not L:
            fail("LIGHT", [r.get("beat")], "no light")
            continue
        for k in ("source", "key_side", "time", "arc", "kelvin"):
            if not L.get(k):
                fail("LIGHT", [r["beat"]], f"light {k} missing")
        k = L.get("kelvin")
        if k and not (isinstance(k, (int, float)) and 1800 <= k <= 10000):
            fail("LIGHT", [r["beat"]], f"kelvin {k} outside 1800–10000K")
        if r.get("face") and L.get("key_side") == "front":
            fail("LIGHT", [r["beat"]], "flat frontal key on a face")
        if r.get("face") and L.get("key_side") == "back":
            if not L.get("why"):
                fail("LIGHT", [r["beat"]], "backlit face with no reason")
            if int(r.get("mode", 1)) == 1 and r.get("type") in ("TH", "SHOT") and r.get("speaking"):
                fail("LIGHT", [r["beat"]], "backlit speaking face in Mode 1")
        day, t = r.get("story_day"), L.get("time")
        if day is not None and t in ORDER:
            if day in last_time and ORDER.index(t) < ORDER.index(last_time[day][0]):
                fail("LIGHT", [last_time[day][1], r["beat"]], f"time goes back on story day {day}: {last_time[day][0]} → {t}")
            if day not in last_time or ORDER.index(t) >= ORDER.index(last_time[day][0]):
                last_time[day] = (t, r["beat"])

    wb = {}
    for r in rows:
        L = r.get("light") or {}
        if L.get("kelvin") and L.get("source"):
            key = (r.get("group"), L["source"], L.get("time"))
            if key in wb and wb[key][0] != L["kelvin"]:
                fail("LIGHT", [wb[key][1], r["beat"]], f"white balance {wb[key][0]}K → {L['kelvin']}K for one source in one scene")
            wb.setdefault(key, (L["kelvin"], r["beat"]))

    groups = defaultdict(list)
    for r in rows:
        groups[r.get("group", "?")].append(r)
    for g, rs in groups.items():
        ef = sum(1 for r in rs if r.get("height") == "eye" and r.get("side") == "front")
        if rs and ef * 3 > len(rs):
            fail("DEFAULT", [g], f"eye-level frontal {ef}/{len(rs)} shots")
        sh = sum(1 for r in rs if (r.get("focus") or {}).get("dof") == "shallow")
        if len(rs) >= 3 and sh * 3 > len(rs) * 2:
            fail("FOCUS", [g], f"shallow on {sh}/{len(rs)} shots — the blurred-everything look")
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
        print("ANGLES, SHOTS, FOCUS & LIGHT PASS" if not out else f"ANGLES, SHOTS, FOCUS & LIGHT FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
