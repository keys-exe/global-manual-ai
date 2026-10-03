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
    "anat": {"style": "S1".."S7", "why": "...", "move": "orbit-left" | "orbit-right" | "push-in" | "pull-back"
             | "rise" | "tilt" | "locked",
             "scope": "macro" | "close" | "pair" | "walking" | "load" | "whole",   # what the picture holds (V7.91.0)
             "lead": "the team's look call, in their words",  # that style leads; the range still runs (V7.91.0)
             "only": false},                          # true only when the team ruled out every other style in words
                                                      # anatomy / mechanism rows (type MECH or kind anatomy|mechanism)
    "pair_of": null,                                  # second row of a matched problem -> relief pair
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
  MOVE     (§24N part 2, V7.100.0, Modes 4–5, new builds) every film row names its camera move `rig` (F1–F24, a classic
           pair in `rig2`: crane + tilt, dolly/track + pan, arc + push); per scene never one move three in a row, ≥ 3 moves
           in any five, locked (F2) on at most a third, at least one travelling move in 3+ shots, ≤ 1 crash zoom (≤ 2 a
           film); a walking subject only under F2/F5/F9/F11–F14/F21–F24, a body on the stairs only under F2/F11/F12
  LIGHT    (§30K) missing light; missing or implausible kelvin (1800–10000K); two white balances for one
           source inside one scene or act group; a flat frontal key on a face; a backlit face with no `why` (never while speaking in
           Mode 1); no light state for the act; time going backwards inside a story day
  ANAT     (§12A-1, V7.81.0) the anatomy / mechanism rows as their own sequence: every one has a style (S1-S7) and a
           move; 3-5 rows use >= 2 styles, 6+ use >= 3; no style on over half (4+), never one style three in a row;
           no two in a row with the same style, height, side and scale; any four in a row have >= 3 setups; the low
           three-quarter on at most a third (3+); no move three in a row, none on over half (4+). pair_of exempts.
           SCOPE (V7.91.0, user 2026-10-02 — "closeup on knee or two knees or both feet walking or with stairs"): every
           row names what the picture holds (macro · close · pair · walking · load · whole); 3-4 rows use >= 2 scopes,
           5+ use >= 3; no scope on over half (4+), never three in a row; 4+ rows have a moving scope (walking or load).
           A team's look call (anat.lead) makes its style the lead: it may take more than half and run three in a row,
           but 3-5 rows keep >= 1 beat in another style and 6+ keep >= 2. Only anat.only (the team ruled out every other
           style in so many words) sets the style count aside — scope, angle and move still vary. anat.lock (a build from
           before V7.91.0) keeps its old meaning: the style checks set aside.
  MVCAM    (§3C camera, V7.86.0) music-video rows (rows with `section`): every row names a library `shot` (§24K part 7)
           and a camera `move` (push-in, pull-back, orbit, crane-up, crane-down, track, tilt, drift, locked); locked /
           drift on at most a third; no move three in a row; signature shots at most one in four, never two in a row;
           a section of 4+ rows uses >= 3 shots; every chorus section (name has CHORUS / DROP, or a row's music is MUS-TURN) has a
           hero — WIDE/FULL from low, ground, high or overhead, or a crane / orbit; a repeated lyric is never shot
           from the same setup twice (mirror_of exempts)
Talking heads (TH), POV and CCTV rows are seed- or mount-locked and skipped (§30A rules 6–7, §22E).
"""
import argparse, json, re, sys
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


# Builds whose act maps were written before V7.91.0 keep them: no anatomy scope is required of them (a system update never
# touches existing builds; re-planning their anatomy is their team's call). Recognised by the plan's path or a pre-V7.91 anat.lock.
PRE_SCOPE = {"identity-callout-v2", "intake-1", "sha0071", "six-weeks-ago", "stryde-71-stairs-pixar-song", "stryde-71-stairs",
             "stryde-cascade", "stryde-failed-alternatives", "stryde-half-my-age", "stryde-identity", "stryde-lost-moments",
             "stryde-not-your-cartilage", "stryde-regrets", "stryde-thirty-years", "stryde-three-regrets", "stryde-too-bad",
             "stryde-what-changed", "demo-ad"}


# Builds that existed at V7.100.0 keep their camera plans: no MOVE range is required of them (a system update never touches
# existing builds). Recognised by the act map's path.
PRE_MOVES = {"facelove-my-mother", "facelove-paint-wall", "facelove-returning-it", "identity-callout-v2", "intake-1", "sha0071",
             "six-weeks-ago", "stryde-71-stairs", "stryde-71-stairs-pixar-song", "stryde-cascade", "stryde-failed-alternatives",
             "stryde-half-my-age", "stryde-her-dad", "stryde-identity", "stryde-lost-moments", "stryde-not-your-cartilage",
             "stryde-regrets", "stryde-the-impression", "stryde-thirty-years", "stryde-three-regrets", "stryde-too-bad",
             "stryde-what-changed", "demo-ad"}
FILM_MOVES = {f"F{i}" for i in range(1, 25)}
TRAVELLING = {"F1", "F4", "F5", "F6", "F7", "F8", "F9", "F10", "F13", "F14", "F15", "F16", "F17", "F18", "F20", "F21", "F22", "F24"}
WITH_WALK = {"F2", "F5", "F9", "F11", "F12", "F13", "F14", "F21", "F22", "F23", "F24"}
ON_STAIRS = {"F2", "F11", "F12"}
COMPOUND_OK = [{"F8", "F12"}, {"F16", "F12"}, {"F1", "F11"}, {"F4", "F11"}, {"F9", "F11"}, {"F13", "F11"}, {"F14", "F11"},
               {"F7", "F1"}, {"F15", "F1"}, {"F7", "F18"}, {"F15", "F18"}, {"F2", "F11"}, {"F2", "F12"}]
WALK_ACT = re.compile(r"\b(?:walks?|walking|strides?|striding|crosses|crossing|climbs?|climbing|descends?|descending|runs?|running|steps? (?:toward|into|across|down|up|out))\b", re.I)
STAIRS_W = re.compile(r"\b(?:stairs?|staircase|steps? (?:up|down)|flight)\b", re.I)


def build_of(path):
    parts = path.parts
    return parts[parts.index("builds") + 1] if "builds" in parts[:-1] else None


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

    TRAVEL_RIGS = TRAVELLING | {"R1-W", "R1-FAST"}
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
    sig = lambda r: (bool(SIGNATURE & set(shots(r))) or r.get("rig") == "F10") and not r.get("inspo_ok")   # F10 dolly zoom is a signature move (§24N)
    dz = [r["beat"] for r in film if r.get("rig") == "F10"]
    if len(dz) > 1:
        fail("SHOT", dz, f"{len(dz)} dolly zooms (F10) — at most one per film (§24N)")
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

    # MOVE (V7.100.0, user 2026-10-03 — "camera movements are lacking"): the film move library F1–F24 (§24N part 2), a range of
    # moves per scene like the angles. Builds that existed at V7.100.0 keep their plans (PRE_MOVES, by the act map's path).
    if build_of(Path(a.rows).resolve()) not in PRE_MOVES:
        mv = lambda r: [m for m in (r.get("rig"), r.get("rig2")) if m]
        for r in film:
            ms = mv(r)
            if not ms:
                fail("MOVE", [r.get("beat")], "film row has no camera move (rig F1–F24, §24N part 2)")
                continue
            unk = [m for m in ms if m not in FILM_MOVES]
            if unk:
                fail("MOVE", [r["beat"]], f"unknown move {unk} — F1–F24")
            if len(ms) == 2 and set(ms) not in COMPOUND_OK:
                fail("MOVE", [r["beat"]], f"{'+'.join(ms)} — one move, or a classic pair: crane + tilt, dolly or track + pan, arc + push")
            act = f"{r.get('action', '')} {r.get('staging', '')}"
            walks = r.get("subject_motion") == "travels" or bool(WALK_ACT.search(act))
            stairs = bool(STAIRS_W.search(act)) or r.get("staging") == "stairs"
            if walks and set(ms) - (ON_STAIRS if stairs else WITH_WALK):
                fail("MOVE", [r["beat"]], f"{'+'.join(ms)} on a {'body on the stairs — hold, pan or tilt' if stairs else 'walk — F2, F5, F9, F11–F14, F21–F24 only'} (§27G)")
        for g, rs in fg.items():
            pr = [mv(r)[0] if mv(r) else None for r in rs]
            for i in range(len(pr) - 2):
                if pr[i] and pr[i] == pr[i + 1] == pr[i + 2]:
                    fail("MOVE", [x["beat"] for x in rs[i:i + 3]], f"{pr[i]} three shots in a row")
            for i in range(len(pr) - 4):
                if len({x for x in pr[i:i + 5] if x}) < 3:
                    fail("MOVE", [x["beat"] for x in rs[i:i + 5]], "fewer than 3 different moves in five shots")
            if len(rs) >= 3:
                lk = sum(1 for x in pr if x == "F2")
                if lk * 3 > len(rs):
                    fail("MOVE", [g], f"locked (F2) on {lk}/{len(rs)} shots — at most a third")
                if not any(set(mv(r)) & TRAVELLING for r in rs):
                    fail("MOVE", [g], "no shot where the camera travels — give the scene one push, pull, arc, track, crane or lead")
            cz = sum(1 for r in rs if "F19" in mv(r))
            if cz > 1:
                fail("MOVE", [g], f"{cz} crash zooms in one scene — at most one")
        cz = [r["beat"] for r in film if "F19" in mv(r)]
        if len(cz) > 2:
            fail("MOVE", cz, f"{len(cz)} crash zooms — at most two in a film")

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

    # ANAT (§12A-1, V7.81.0): the anatomy / mechanism beats as their own run — spread among lifestyle
    # shots, one repeated anatomy look passes every act-level check
    STYLES = {f"S{n}" for n in range(1, 8)}
    MOVES = {"orbit-left", "orbit-right", "push-in", "pull-back", "rise", "tilt", "locked"}
    an = [r for r in rows if r.get("type") == "MECH" or r.get("kind") in ("anatomy", "mechanism") or r.get("anat")]
    for r in an:
        A = r.get("anat") or {}
        if A.get("style") not in STYLES:
            fail("ANAT", [r.get("beat")], f"no anatomy style (S1-S7), has {A.get('style')!r}")
        if A.get("move") not in MOVES:
            fail("ANAT", [r.get("beat")], f"no camera move ({' · '.join(sorted(MOVES))}), has {A.get('move')!r}")
    sty = lambda r: (r.get("anat") or {}).get("style")
    mov = lambda r: (r.get("anat") or {}).get("move")
    look = lambda r: (sty(r), r.get("height"), r.get("side"), r.get("scale"))
    counted = [r for r in an if not r.get("pair_of")]          # a matched pair counts once
    n = len(counted)
    used = {sty(r) for r in counted if sty(r)}
    need = 3 if n >= 6 else 2 if n >= 3 else 0   # fewer than three anatomy beats (none included): no range to check (LESSONS L19)
    # the team's one-look call (§12A-1 rule 7, V7.89.3, LESSONS L34): every anatomy row carries anat.lock → the style checks step aside
    # a pre-V7.91 build's lock or the team's explicit "only" (anat.only) sets the style checks aside; scope, angle and move still run
    locked = bool(counted) and all((r.get("anat") or {}).get("lock") or (r.get("anat") or {}).get("only") for r in counted)
    # V7.91.0 (user: "i dont want to be stuck in just one style of anatomy per task"): a look call leads, never the only look
    leads = {(r.get("anat") or {}).get("style") for r in counted if (r.get("anat") or {}).get("lead")}
    lead = next(iter(leads)) if len(leads) == 1 and not locked else None
    if lead and n >= 3:
        others = sum(1 for r in counted if sty(r) != lead)
        want = 2 if n >= 6 else 1
        if others < want:
            fail("ANAT", [r["beat"] for r in counted], f"the team's look ({lead}) leads, but {n} anatomy beats need {want} in another "
                 f"style ({others} now) — a look call is the lead, never the only look unless the team said 'only' (§12A-1 rule 7, V7.91.0)")
        need = 0
    if locked:
        need = 0
        sty = lambda r: None
    # SCOPE (V7.91.0): what the anatomy picture holds — one knee close, both knees, both legs walking, on the stairs
    SCOPES = {"macro", "close", "pair", "walking", "load", "whole"}
    scope = lambda r: (r.get("anat") or {}).get("scope")
    pre = (build_of(Path(a.rows).resolve()) in PRE_SCOPE or any((r.get("anat") or {}).get("lock") for r in counted)) \
        and not any(scope(r) for r in counted)
    for r in ([] if pre else counted):
        if scope(r) not in SCOPES:
            fail("ANAT", [r.get("beat")], f"no scope ({' · '.join(sorted(SCOPES))}) — say what the picture holds, has {scope(r)!r}")
    scopes = {scope(r) for r in counted if scope(r) in SCOPES}
    sneed = 0 if pre else 3 if n >= 5 else 2 if n >= 3 else 0
    if sneed and len(scopes) < sneed:
        fail("ANAT", [r["beat"] for r in counted], f"{n} anatomy beats in {len(scopes)} scope(s) {sorted(scopes)} — use at least {sneed}: "
             "one joint close, both sides, the limbs walking, under load on stairs (§12A-1 V7.91.0)")
    if n >= 4 and not pre:
        for sc in scopes:
            k = sum(1 for r in counted if scope(r) == sc)
            if k * 2 > n:
                fail("ANAT", [sc], f"scope {sc} on {k}/{n} anatomy beats — at most half")
        if not scopes & {"walking", "load"}:
            fail("ANAT", [r["beat"] for r in counted], "no anatomy beat in motion — give one the walking or load scope (both legs walking, on the stairs)")
    for i in range(2, len(counted)):
        q, p, r = counted[i - 2:i + 1]
        if scope(q) in SCOPES and scope(q) == scope(p) == scope(r):
            fail("ANAT", [q["beat"], p["beat"], r["beat"]], f"scope {scope(r)} three in a row")
    if need and len(used) < need:
        fail("ANAT", [r["beat"] for r in counted], f"{n} anatomy beats in {len(used)} style(s) {sorted(used)} — use at least {need} (§12A-1)")
    if n >= 4:
        for st in ([] if locked else used - {lead}):
            k = sum(1 for r in counted if sty(r) == st)
            if k * 2 > n:
                fail("ANAT", [st], f"style {st} on {k}/{n} anatomy beats — at most half")
        for mv in {mov(r) for r in counted if mov(r)}:
            k = sum(1 for r in counted if mov(r) == mv)
            if k * 2 > n:
                fail("ANAT", [mv], f"move {mv} on {k}/{n} anatomy beats — at most half")
    if n >= 3:
        lo = sum(1 for r in counted if r.get("height") == "low" and r.get("side") == "three-quarter")
        if lo * 3 > n:
            fail("ANAT", ["low/three-quarter"], f"the old default angle on {lo}/{n} anatomy beats — at most a third")
    for i in range(1, len(counted)):
        p, r = counted[i - 1], counted[i]
        if look(p) == look(r) and scope(p) == scope(r):
            fail("ANAT", [p["beat"], r["beat"]], f"same style, angle and scale back to back {look(r)}")
        if i >= 2:
            q = counted[i - 2]
            if sty(q) and sty(q) == sty(p) == sty(r) and sty(r) != lead:
                fail("ANAT", [q["beat"], p["beat"], r["beat"]], f"style {sty(r)} three in a row")
            if mov(q) and mov(q) == mov(p) == mov(r):
                fail("ANAT", [q["beat"], p["beat"], r["beat"]], f"move {mov(r)} three in a row")
        if i >= 3:
            w = counted[i - 3:i + 1]
            if len({(x.get("height"), x.get("side"), x.get("scale")) for x in w}) < 3:
                fail("ANAT", [x["beat"] for x in w], "fewer than three angles in four anatomy beats")

    # MVCAM (§3C, V7.86.0 — user: "camera angles in music videos"): the camera moves with the song
    MV_MOVES = {"push-in", "pull-back", "orbit", "crane-up", "crane-down", "track", "tilt", "drift", "locked"}
    mv = [r for r in rows if r.get("section")]
    for r in mv:
        if not shots(r):
            fail("MVCAM", [r.get("beat")], "music-video row with no library shot (§24K part 7) — name it (SH-LOW, SH-OTS, SH-AERIAL…)")
        for sid in shots(r):
            if sid not in LIB:
                fail("MVCAM", [r.get("beat")], f"unknown shot {sid}")
        if r.get("move") not in MV_MOVES:
            fail("MVCAM", [r.get("beat")], f"no camera move ({' · '.join(sorted(MV_MOVES))}), has {r.get('move')!r}")
    if mv:
        still = sum(1 for r in mv if r.get("move") in ("locked", "drift"))
        if still * 3 > len(mv):
            fail("MVCAM", ["video"], f"the camera barely moves: locked / drift on {still}/{len(mv)} shots — at most a third")
        for i in range(2, len(mv)):
            if mv[i].get("move") and mv[i].get("move") == mv[i - 1].get("move") == mv[i - 2].get("move"):
                fail("MVCAM", [mv[i - 2]["beat"], mv[i - 1]["beat"], mv[i]["beat"]], f"move {mv[i]['move']} three in a row")
        sigm = lambda r: bool(SIGNATURE & set(shots(r))) and not r.get("inspo_ok")
        if sum(map(sigm, mv)) * 4 > len(mv):
            fail("MVCAM", ["video"], f"signature shots on {sum(map(sigm, mv))}/{len(mv)} — at most one in four")
        for i in range(1, len(mv)):
            if sigm(mv[i - 1]) and sigm(mv[i]):
                fail("MVCAM", [mv[i - 1]["beat"], mv[i]["beat"]], "two signature shots in a row")
        secs = defaultdict(list)
        for r in mv:
            secs[str(r["section"])].append(r)
        for sec, rs in secs.items():
            kinds_ = {sid for r in rs for sid in shots(r)}
            if len(rs) >= 4 and len(kinds_) < 3:
                fail("MVCAM", [sec], f"{len(kinds_)} shot types in {len(rs)} shots — at least three")
            chorus = re.search(r"chorus|drop", sec, re.I) or any(r.get("music") == "MUS-TURN" for r in rs)
            if chorus and not any((r.get("scale") in ("WIDE", "FULL") and r.get("height") in ("low", "ground", "high", "overhead"))
                                  or r.get("move") in ("crane-up", "crane-down", "orbit") for r in rs):
                fail("MVCAM", [sec], "a chorus with no hero shot — WIDE/FULL from low, ground, high or overhead, or a crane / orbit")
        seen_line = {}
        for r in mv:
            key = re.sub(r"\W+", " ", str(r.get("line", "")).lower()).strip()
            if not key:
                continue
            setup_ = (tuple(shots(r)), r.get("height"), r.get("side"), r.get("scale"))
            if key in seen_line and seen_line[key][0] == setup_ and not r.get("mirror_of"):
                fail("MVCAM", [seen_line[key][1], r["beat"]], "the repeated lyric shot from the same setup — a repeat gets a new angle")
            seen_line.setdefault(key, (setup_, r["beat"]))

    dist = defaultdict(int)
    for r in rows:
        dist[f"{r.get('height')}/{r.get('side')}"] += 1
    if a.json:
        print(json.dumps({"pass": not out, "fails": out, "setups": dist}, indent=1))
    else:
        for f in out:
            print(f"FAIL  {f['check']:8} {', '.join(map(str, f['beats']))}  — {f['detail']}")
        print("setups: " + ", ".join(f"{k} ×{v}" for k, v in sorted(dist.items(), key=lambda x: -x[1])))
        print("ANGLES, SHOTS, MOVES, FOCUS, LIGHT, ANATOMY & MUSIC-VIDEO CAMERA PASS" if not out else f"ANGLES, SHOTS, MOVES, FOCUS, LIGHT, ANATOMY & MUSIC-VIDEO CAMERA FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
