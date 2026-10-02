#!/usr/bin/env python3
"""§24K part 5 — one take for connected action (V7.88.0).

A film scene's connected shots are generated in ONE Seedance call, never as separate clips: a continuous
movement (a walk, a climb, a stand-up) is one continuous take, and coverage of one moment in one place
(a wide, a reverse, a reaction) is one MULTI-SHOT take. Separate clips of one moment come back with people
in different places, the room changed and the movement restarting at every cut (LESSONS L12, L17, L22, L24).

Usage:
  takes.py ACT_MAP.json [--suggest] [--write OUT.json] [--md takes.md] [--json] [--max-shots 4] [--max-seconds 15]

ACT_MAP.json: the step-5 act map — a list of rows, or {"rows": [...]}. Film rows (type SHOT / INSERT, Modes 4
and 5) carry, on top of their usual fields:
  "take": "SC07-T1"                  every row: the take it is generated in (one Seedance call)
  "take_kind": "one-take" | "multi"  first row of a take of 2+ rows: one continuous shot (TAKE-FILM), or
                                     coverage cut inside one generation (MULTI-FILM)
  "start_pos": "..."                 first row of a take: where everyone is at frame 1, which way they face,
                                     what is in their hands
  "end_pos": "..."                   last row of a take: where everyone is on the last frame — the next take
                                     in the same place starts from it
  "split": "<reason>"                first row of a take that follows a connected row (same scene, same place,
                                     same story day): why it is not in the previous take — one of
                                     length · pinned · insert · intercut · user  (location, a scene change and
                                     a story-day change split by themselves)
  "pinned": true                     a pinned shot (product turn, exact end frame) — Kling first-and-last frame,
                                     always its own take

Connected: two rows in a row with the same scene (`scene` or `group`), the same `location` (unknown counts as
the same) and the same `story_day`. Connected rows share a take unless the second names a split reason.

Checks (any FAIL -> exit 1):
  TAKE   every film row names its take
  JOIN   a connected row starts a new take with no split reason — merge it into the take before
  SPLIT  the reason is unknown, or does not hold (length when the takes together fit; pinned on a row that
         is not pinned)
  TAKE+  a take's rows are consecutive, in one scene, one place and one story day; at most --max-shots rows
         and, where rows carry `duration`, at most --max-seconds; a pinned row is alone
  KIND   a take of 2+ rows names take_kind; a one-take covers one continuous action (<= 3 rows)
  POS    every take has start_pos on its first row and end_pos on its last

--suggest proposes the takes for an act map that has none (connected runs, cut at --max-shots, balanced),
prints the calls before and after, and with --write writes the act map with `take` / `take_kind` filled and
start_pos / end_pos left as "?" for the planner to write. The proposal is a starting point: the planner
still checks every take against the action.
"""
import argparse, json, math, sys
from pathlib import Path

FILM_TYPES = {"SHOT", "INSERT"}
REASONS = {
    "length": "the connected run is longer than one take holds (--max-shots rows)",
    "pinned": "a pinned shot — Kling first-and-last frame (§24K part 1)",
    "insert": "a product or label close-up the take's camera cannot reach crisply — its own info card",
    "intercut": "the scene cuts away to another place and back (a phone call, a memory)",
    "user": "the user asked for this shot on its own",
}
AUTO = ("scene", "location", "story day")


def scene(r):
    return r.get("scene") or r.get("group")


def connected(a, b):
    """Why b is not connected to a (an automatic split), or None when they are one moment in one place."""
    if scene(a) != scene(b):
        return "scene"
    la, lb = a.get("location"), b.get("location")
    if la and lb and la != lb:
        return "location"
    if a.get("story_day") != b.get("story_day"):
        return "story day"
    return None


def film_rows(rows):
    return [r for r in rows if str(r.get("type", "SHOT")).upper() in FILM_TYPES and int(r.get("mode") or 4) in (4, 5)]


def runs(rows):
    """Connected runs: consecutive rows with no automatic split between them; a pinned row is its own run."""
    out = []
    for r in rows:
        if out and not r.get("pinned") and not out[-1][-1].get("pinned") and connected(out[-1][-1], r) is None:
            out[-1].append(r)
        else:
            out.append([r])
    return out


def dur(r):
    return float(r.get("duration") or 0)


def suggest(rows, max_shots, max_seconds=15):
    takes = []
    for run in runs(rows):
        n = math.ceil(len(run) / max_shots)
        while True:  # the fewest balanced takes that each fit the shot and second limits
            size = math.ceil(len(run) / n)
            parts = [run[i:i + size] for i in range(0, len(run), size)]
            if n >= len(run) or all(sum(dur(r) for r in p) <= max_seconds for p in parts):
                break
            n += 1
        takes += parts
    count = {}
    for t in takes:
        sc = scene(t[0]) or "T"
        count[sc] = count.get(sc, 0) + 1
        tid = f"{sc}-T{count[sc]}"
        subjects = {tuple(sorted(r.get("cast") or [r.get("subject")])) for r in t}
        kind = "one-take" if len(t) <= 3 and len(subjects) == 1 and len(next(iter(subjects))) == 1 else "multi"
        for j, r in enumerate(t):
            r["take"] = tid
            if j == 0:
                if len(t) > 1:
                    r["take_kind"] = kind
                r.setdefault("start_pos", "?")
                if takes.index(t) and connected(takes[takes.index(t) - 1][-1], r) is None and not r.get("pinned") \
                        and not takes[takes.index(t) - 1][-1].get("pinned"):
                    r.setdefault("split", "length")
            if j == len(t) - 1:
                r.setdefault("end_pos", "?")
    return takes


def check(rows, max_shots, max_seconds=15):
    out = []

    def fail(kind, beats, detail):
        out.append({"check": kind, "beats": beats, "detail": detail})

    for r in rows:
        if not r.get("take"):
            fail("TAKE", [r.get("beat")], "no take — name the take this shot is generated in (one Seedance call)")
    rows_t = [r for r in rows if r.get("take")]
    order = {}
    for i, r in enumerate(rows_t):
        order.setdefault(r["take"], []).append(i)
    takes = {t: [rows_t[i] for i in ix] for t, ix in order.items()}

    for t, ix in order.items():
        rs = takes[t]
        beats = [r.get("beat") for r in rs]
        if ix != list(range(ix[0], ix[0] + len(ix))):
            fail("TAKE+", beats, f"take {t} is not consecutive — a take is one stretch of the scene")
        for a, b in zip(rs, rs[1:]):
            why = connected(a, b)
            if why:
                fail("TAKE+", [a.get("beat"), b.get("beat")], f"take {t} crosses a {why} change — a take is one moment in one place")
        if len(rs) > max_shots:
            fail("TAKE+", beats, f"take {t} has {len(rs)} shots (> {max_shots}) — split it with split: \"length\"")
        secs = sum(float(r.get("duration") or 0) for r in rs)
        if secs > max_seconds:
            fail("TAKE+", beats, f"take {t} runs {secs:g}s (> {max_seconds:g}s) — split it with split: \"length\"")
        if len(rs) > 1 and any(r.get("pinned") for r in rs):
            fail("TAKE+", beats, f"take {t} holds a pinned shot — a pinned shot is its own take on Kling")
        if len(rs) > 1:
            k = rs[0].get("take_kind")
            if k not in ("one-take", "multi"):
                fail("KIND", beats[:1], f"take {t}: take_kind must be one-take or multi")
            elif k == "one-take" and len(rs) > 3:
                fail("KIND", beats, f"take {t}: a one-take of {len(rs)} shots — one continuous action covers at most 3 rows; use multi")
        if not str(rs[0].get("start_pos") or "").strip("? "):
            fail("POS", beats[:1], f"take {t}: no start_pos — where everyone is at frame 1, facing, hands")
        if not str(rs[-1].get("end_pos") or "").strip("? "):
            fail("POS", beats[-1:], f"take {t}: no end_pos — where everyone is on the last frame")

    for a, b in zip(rows_t, rows_t[1:]):
        if a["take"] == b["take"]:
            continue
        why = connected(a, b)
        sp = b.get("split")
        if why is None and not a.get("pinned") and not b.get("pinned"):
            if not sp:
                fail("JOIN", [a.get("beat"), b.get("beat")],
                     f"{b.get('beat')} carries straight on from {a.get('beat')} (same scene, place and day) but starts a new take — "
                     f"put it in take {a['take']}, or name the split reason ({' · '.join(REASONS)})")
            elif sp not in REASONS:
                fail("SPLIT", [b.get("beat")], f"split {sp!r} is not a reason — one of {' · '.join(REASONS)}")
            elif sp == "length" and len(takes[a["take"]]) + len(takes[b["take"]]) <= max_shots:
                fail("SPLIT", [a.get("beat"), b.get("beat")],
                     f"split \"length\" but takes {a['take']} and {b['take']} fit in one ({len(takes[a['take']]) + len(takes[b['take']])} shots)")
        if sp == "pinned" and not b.get("pinned"):
            fail("SPLIT", [b.get("beat")], "split \"pinned\" on a row that is not pinned — set pinned: true or merge it")
    return out, takes


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--suggest", action="store_true")
    ap.add_argument("--write")
    ap.add_argument("--md")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max-shots", type=int, default=4)
    ap.add_argument("--max-seconds", type=float, default=15)
    a = ap.parse_args()
    data = json.loads(Path(a.plan).read_text())
    rows_all = data if isinstance(data, list) else data.get("rows", [])
    rows = film_rows(rows_all)
    if not rows:
        print("TAKES PASS (no film shots)")
        sys.exit(0)
    if a.suggest:
        takes = suggest(rows, a.max_shots, a.max_seconds)
        print(f"{len(rows)} shots -> {len(takes)} takes (Seedance calls)")
        for t in takes:
            print(f"  {t[0]['take']:10} {t[0].get('take_kind', 'single'):8} {', '.join(r.get('beat') for r in t)}"
                  f"{'  [split: ' + t[0]['split'] + ']' if t[0].get('split') else ''}")
        if a.write:
            Path(a.write).write_text(json.dumps(data, indent=1, ensure_ascii=False))
    out, takes = check(rows, a.max_shots, a.max_seconds)
    if a.md:
        md = ["### Takes", "", "Connected shots are generated in one take — one Seedance call (§24K part 5). "
              f"{len(rows)} shots in {len(takes)} takes.", "",
              "| Take | Kind | Shots | Starts | Ends | Split |", "|---|---|---|---|---|---|"]
        for t, rs in takes.items():
            md.append(f"| {t} | {rs[0].get('take_kind', 'single')} | {', '.join(r.get('beat', '') for r in rs)} | "
                      f"{rs[0].get('start_pos', '')} | {rs[-1].get('end_pos', '')} | {rs[0].get('split', '')} |")
        Path(a.md).write_text("\n".join(md) + "\n", encoding="utf-8")
    if a.json:
        print(json.dumps({"pass": not out, "shots": len(rows), "takes": len(takes), "fails": out}, indent=1))
    else:
        for f in out:
            print(f"FAIL  {f['check']:5} {', '.join(str(b) for b in f['beats'])}  — {f['detail']}")
        print(f"TAKES PASS ({len(rows)} shots in {len(takes)} takes)" if not out else f"TAKES FAIL ({len(out)})")
    sys.exit(1 if out else 0)


if __name__ == "__main__":
    main()
