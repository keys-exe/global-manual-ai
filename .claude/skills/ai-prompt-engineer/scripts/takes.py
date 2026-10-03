#!/usr/bin/env python3
"""§24K part 5 — one take for connected action (V7.88.0); one scene, one take, and the VO sets the length (V7.93.0).

A film scene's connected shots are generated in ONE Seedance call, never as separate clips: a continuous
movement (a walk, a climb, a stand-up) is one continuous take, and coverage of one moment in one place
(a wide, a reverse, a reaction) is one MULTI-SHOT take. Separate clips of one moment come back with people
in different places, the room changed and the movement restarting at every cut (LESSONS L12, L17, L22, L24).

V7.93.0 (user 2026-10-02 — "it doesnt need the clip to be one only if the clips is just one scene… make it 1 clip
only instead of splitting them specially when its a conversation where the position is critical", "the video duration
should depends on the vo"): a scene in one place and one story day is ONE take whenever its running time fits; the row
count never splits it (rows past four shots join the shot before: `joins: true`); a conversation take holds up to
--max-talk-seconds (30, Seedance's longest call) so the people never move between calls; `length` is time only. With a
narration master (--vo / --vo-words) every take's duration is measured from the VO it carries, never a default.

V7.98.0 (user 2026-10-03 — "i dont want clips that is bit by bit, i want it all in one go if that is just one scene cause
the position of them if one clip only it can be consistent… specially the location"; LESSONS L66): every scene — action
or conversation — is ONE take up to 30 s (Seedance's longest call); the 15 s action ceiling is retired. `insert` is no
longer a split reason: a close-up is a shot inside the take. A scene splits only past 30 s (`length`), for a cutaway to
another place (`intercut`), a Kling pinned shot (`pinned`) or the user's ask (`user`). --legacy keeps the pre-V7.98 rules
(15 s action takes, `insert`) for builds that planned under them.

V7.99.0 (user 2026-10-03 — "also dont use little shots in side that scene cause staying in one shot is boring and that is
not the holywood style"; LESSONS L67): the scene stays one clip, but inside it the camera covers it like a feature scene —
every row is its own shot, a new shot every 2–5 s (SHOT_MAX), the size changing (never three in a row at one size; 3+ shots
use 2+ sizes, 5+ shots 3+). `joins` and the four-shot cap are retired for new builds: a take holds as many shots as its
scene needs — no count limit, the full 30 s when needed (V7.99.1: Seedance 2.5 holds 30 s without distortion, user-confirmed). A one-take (one uncut shot) only up to 5 s, or a oner the user asked for (`oner: true`).

Usage:
  takes.py ACT_MAP.json [--suggest] [--write OUT.json] [--md takes.md] [--json] [--max-shots 4] [--max-seconds 30] [--legacy]
           [--max-talk-seconds 30] [--vo MASTER.mp3 [--script LINES.txt] | --vo-words WORDS.json] [--model medium.en]

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
                                     length · pinned · intercut · user  (location, a scene change and
                                     a story-day change split by themselves)
  "pinned": true                     a pinned shot (product turn, exact end frame) — Kling first-and-last frame,
                                     always its own take
  "joins": true                      (V7.93.0) this row continues the shot before it — same camera, no cut (a reaction
                                     or a follow-on step played inside the shot before). Shots = rows without joins.
  "dialogue": "..."                  the words spoken on screen in this row (verbatim) — a take with dialogue from
                                     2+ rows, or a row with "conversation": true, is a CONVERSATION take
  "vo": "..."                        (V7.93.0) the narration phrase played over this row, verbatim from the script
  "hold_s": 2.5                      (V7.93.0) seconds the row needs beyond its VO: silent action, a look, on-screen
                                     dialogue (default: the dialogue's E6 estimate, else 0)

Connected: two rows in a row with the same scene (`scene` or `group`), the same `location` (unknown counts as
the same) and the same `story_day`. Connected rows share a take unless the second names a split reason.

Checks (any FAIL -> exit 1):
  TAKE   every film row names its take
  JOIN   a connected row starts a new take with no split reason — merge it into the take before
  SPLIT  the reason is unknown, or does not hold: `length` only when the two takes' running time together is over
         the ceiling (30 s, V7.98.0) — never for the row count (V7.93.0, L51/L61, L66); `length` needs
         durations; pinned on a row that is not pinned
  TAKE+  a take's rows are consecutive, in one scene, one place and one story day; at most --max-shots SHOTS
         (rows without joins) and, where rows carry `duration`, at most --max-seconds (a conversation take
         --max-talk-seconds); a pinned row is alone
  KIND   a take of 2+ rows names take_kind; a one-take covers one continuous action (<= 3 shots)
  POS    every take has start_pos on its first row and end_pos on its last
  VO     (with --vo / --vo-words) every `vo` phrase is found on the master in order; each take's duration is the
         VO it carries + its rows' hold_s + the master's own pause before the next take, rounded up (Seedance 4–30);
         a row whose stated duration is under its measured VO fails VO_SHORT; a take whose measured time is over its
         ceiling fails VO_LONG and names the sentence end to split at. --write writes the measured durations.

--suggest proposes the takes for an act map that has none (connected runs, one take per run while it fits the
seconds ceiling, rows past --max-shots joined to the shot before — never split for the row count),
prints the calls before and after, and with --write writes the act map with `take` / `take_kind` filled and
start_pos / end_pos left as "?" for the planner to write. The proposal is a starting point: the planner
still checks every take against the action.
"""
import argparse, json, math, sys
from pathlib import Path

FILM_TYPES = {"SHOT", "INSERT"}
REASONS = {
    "length": "the scene's running time is over one take's ceiling (30 s, Seedance's longest call) — never the row count",
    "pinned": "a pinned shot — Kling first-and-last frame (§24K part 1), never a Seedance row",
    "intercut": "the scene cuts away to another place and back (a phone call, a memory)",
    "user": "the user asked for this shot on its own",
}
LEGACY_REASONS = {"insert": "a product or label close-up the take's camera cannot reach crisply (retired V7.98.0: a shot inside the take)"}
AUTO = ("scene", "location", "story day")
# Builds that planned their takes before V7.98.0 / V7.99.0 keep their rules (never re-cut without their team's ask):
# an act map under builds/<one of these>/ runs as --legacy by itself.
PRE_V799 = {"facelove-my-mother", "facelove-paint-wall", "facelove-returning-it", "identity-callout-v2", "intake-1", "sha0071",
            "six-weeks-ago", "stryde-71-stairs-pixar-song", "stryde-71-stairs", "stryde-cascade", "stryde-failed-alternatives",
            "stryde-half-my-age", "stryde-her-dad", "stryde-identity", "stryde-lost-moments", "stryde-not-your-cartilage",
            "stryde-regrets", "stryde-the-impression", "stryde-thirty-years", "stryde-three-regrets", "stryde-too-bad",
            "stryde-what-changed"}


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


WPS = 2.4          # E6: on-screen dialogue at an unhurried pace, words a second
LINE_AIR = 0.6     # E6: a breath before and after a spoken line


def is_talk(rs):
    """A conversation take: dialogue on 2+ rows, or a row marked conversation (V7.93.0)."""
    return sum(1 for r in rs if str(r.get("dialogue") or "").strip()) >= 2 or any(r.get("conversation") for r in rs)


def ceiling(rs, max_seconds, max_talk):
    return max_talk if is_talk(rs) else max_seconds


SHOT_MAX = 5.0     # V7.99.0: no shot inside a take runs past 5 s — feature-drama coverage
SIZES = {"SH-WIDE": "wide", "SH-AERIAL": "wide", "SH-SIL": "wide", "SH-MED": "medium", "SH-OTS": "medium", "SH-34": "medium",
         "SH-PROFILE": "medium", "SH-REAR": "medium", "SH-CU": "close", "SH-HICU": "close", "SH-LOCU": "close",
         "SH-WACU": "close", "SH-MACRO": "extreme close", "SH-MAGNIFY": "extreme close"}


def size_of(r):
    """A row's shot size (wide · medium · close · extreme close) from its `size` or its §24K part 7 `shot`, or None."""
    v = str(r.get("size") or "").lower().strip()
    if v:
        return "extreme close" if "extreme close" in v or v in ("ecu", "insert", "macro") else \
               "close" if "close" in v or v in ("cu", "mcu") else "wide" if "wide" in v or v in ("ws", "full") else "medium"
    return SIZES.get(str(r.get("shot") or "").upper())


def shots(rs):
    """Shots in a take: rows that cut (a row with joins: true plays inside the shot before)."""
    return sum(1 for j, r in enumerate(rs) if j == 0 or not r.get("joins"))


def hold(r):
    if r.get("hold_s") is not None:
        return float(r["hold_s"])
    d = str(r.get("dialogue") or "").split()
    return round(len(d) / WPS + LINE_AIR, 2) if d else 0.0


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


def suggest(rows, max_shots, max_seconds=30, max_talk=30, legacy=False):
    max_shots = max_shots or (4 if legacy else 999)
    takes = []
    for run in runs(rows):
        cap = ceiling(run, max_seconds, max_talk)
        n = 1
        while True:  # the fewest balanced takes that fit the SECONDS ceiling — the row count never splits (V7.93.0)
            size = math.ceil(len(run) / n)
            parts = [run[i:i + size] for i in range(0, len(run), size)]
            if n >= len(run) or all(sum(dur(r) for r in p) <= ceiling(p, max_seconds, max_talk) for p in parts):
                break
            n += 1
        for p in parts:  # rows past max_shots join the shot before: the shortest follow-on rows first
            extra = shots(p) - max_shots
            for r in sorted(p[1:], key=lambda r: (bool(str(r.get("dialogue") or "").strip()), dur(r))):
                if extra <= 0:
                    break
                if not r.get("joins"):
                    r["joins"] = True
                    extra -= 1
        takes += parts
    count = {}
    for t in takes:
        sc = scene(t[0]) or "T"
        count[sc] = count.get(sc, 0) + 1
        tid = f"{sc}-T{count[sc]}"
        subjects = {tuple(sorted(r.get("cast") or [r.get("subject")])) for r in t}
        kind = ("one-take" if shots(t) <= 3 and len(subjects) == 1 and len(next(iter(subjects))) == 1 else "multi") if legacy else "multi"
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


def check(rows, max_shots, max_seconds=30, max_talk=30, legacy=False):
    max_shots = max_shots or (4 if legacy else 999)
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
        if not legacy:  # V7.99.0: the scene covered — a new shot every 2–5 s, the size changing (L67)
            oner = any(r.get("oner") for r in rs)
            jn = [r.get("beat") for r in rs if r.get("joins")]
            if jn:
                fail("COVER", jn, "joins is retired (V7.99.0): every row is its own shot — a cut to a new size or angle, "
                                  "never played inside the shot before")
            if not oner:
                lg = [f"{r.get('beat')} {float(r['duration']):g}s" for r in rs if r.get("duration") and float(r["duration"]) > SHOT_MAX + 1e-6]
                if lg:
                    fail("COVER", [x.split()[0] for x in lg], f"a shot over {SHOT_MAX:g}s ({', '.join(lg)}) — split the row into "
                                                               f"2+ shots at a phrase or on the action, a new size or angle each")
                td = float(rs[0].get("take_duration") or sum(float(r.get("duration") or 0) for r in rs))
                if td and shots(rs) < math.ceil(td / SHOT_MAX - 1e-6):
                    fail("COVER", beats, f"take {t} runs {td:g}s in {shots(rs)} shot(s) — a scene held that long in few shots "
                                         f"reads as boring; cover it in {math.ceil(td / SHOT_MAX - 1e-6)}+ shots")
                sz = [size_of(r) for r in rs]
                for i in range(len(sz) - 2):
                    if sz[i] and sz[i] == sz[i + 1] == sz[i + 2]:
                        fail("COVER", beats[i:i + 3], f"three shots in a row at {sz[i]} — change the size at the cut")
                        break
                need = 1 if len(rs) < 3 else (2 if len(rs) < 5 else 3)
                if all(sz) and len(set(sz)) < need:
                    fail("COVER", beats, f"take {t}: {len(set(sz))} size(s) in {len(rs)} shots — cover it wide, medium and close "
                                         f"(≥ {need})")
        if shots(rs) > max_shots:
            fail("TAKE+", beats, f"take {t} has {shots(rs)} shots (> {max_shots}) — join the follow-on rows to the shot before "
                                 f"(joins: true: a reaction or a next step played inside it); the row count never splits a take")
        secs = float(rs[0].get("take_duration") or sum(float(r.get("duration") or 0) for r in rs))
        cap = ceiling(rs, max_seconds, max_talk)
        if secs > cap:
            fail("TAKE+", beats, f"take {t} runs {secs:g}s (> {cap:g}s{' — a conversation' if is_talk(rs) else ''}) — "
                                 f"split it with split: \"length\" where nobody moves, end_pos -> start_pos")
        if len(rs) > 1 and any(r.get("pinned") for r in rs):
            fail("TAKE+", beats, f"take {t} holds a pinned shot — a pinned shot is its own take on Kling")
        if len(rs) > 1:
            k = rs[0].get("take_kind")
            if k not in ("one-take", "multi"):
                fail("KIND", beats[:1], f"take {t}: take_kind must be one-take or multi")
            elif k == "one-take" and not legacy and not any(r.get("oner") for r in rs):
                fail("KIND", beats, f"take {t}: a one-take holds the scene in one uncut shot — only up to {SHOT_MAX:g}s or a oner "
                                    "the user asked for (oner: true); cover it as multi, a new shot every 2–5 s (V7.99.0)")
            elif k == "one-take" and shots(rs) > 3:
                fail("KIND", beats, f"take {t}: a one-take of {shots(rs)} shots — one continuous action covers at most 3; use multi")
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
            elif sp == "insert" and not legacy:
                fail("SPLIT", [b.get("beat")], "split \"insert\" is retired (V7.98.0, L66): a close-up is a shot inside the scene's "
                                               "take, its info card one of the take's ingredients — merge it")
            elif sp not in REASONS and not (legacy and sp in LEGACY_REASONS):
                fail("SPLIT", [b.get("beat")], f"split {sp!r} is not a reason — one of {' · '.join(REASONS)}")
            elif sp == "length":
                both = takes[a["take"]] + takes[b["take"]]
                secs = sum(float(takes[x][0].get("take_duration") or sum(float(r.get("duration") or 0) for r in takes[x]))
                           for x in (a["take"], b["take"]))
                cap = ceiling(both, max_seconds, max_talk)
                if not all(r.get("duration") for r in both):
                    fail("SPLIT", [a.get("beat"), b.get("beat")],
                         f"split \"length\" with no durations on takes {a['take']} / {b['take']} — length is time, never the row count "
                         f"(V7.93.0): give the rows their durations (--vo measures them) or merge the takes")
                elif secs <= cap:
                    fail("SPLIT", [a.get("beat"), b.get("beat")],
                         f"split \"length\" but takes {a['take']} and {b['take']} together run {secs:g}s (<= {cap:g}s"
                         f"{', a conversation' if is_talk(both) else ''}) — one scene in one place is one take: merge them "
                         f"(rows past {max_shots} shots join the shot before)")
        if sp == "pinned" and not b.get("pinned"):
            fail("SPLIT", [b.get("beat")], "split \"pinned\" on a row that is not pinned — set pinned: true or merge it")
    return out, takes


def _norm(t):
    import re
    return re.sub(r"[^a-z0-9']", "", t.lower())


def vo_words(a):
    """Word timings of the narration master: [(start, end, word)] — from --vo-words JSON or Whisper on --vo."""
    if a.vo_words:
        return [tuple(w) if isinstance(w, (list, tuple)) else (w["start"], w["end"], w["word"])
                for w in json.loads(Path(a.vo_words).read_text())]
    sys.path.insert(0, str(Path(__file__).parent))
    from trim import words  # noqa: E402
    ws = words(a.vo, a.model)
    if a.script:
        from assemble import align  # noqa: E402  (the script's words, timed on the transcript — V7.79.0)
        ws = align(Path(a.script).read_text(encoding="utf-8").split(), ws)
    return ws


def measure(rows, ws, max_seconds, max_talk, lead=0.25, tail=0.5):
    """V7.93.0: each take's duration from the VO it carries. Rows carry `vo` (verbatim). The VO is never cut or
    sped (§24L): a take runs from its first VO word (minus the lead) to the next take's first VO word, plus its
    rows' hold_s (silent action, on-screen dialogue — the narration waits for them). Returns fails and timings."""
    toks = [_norm(w[2]) for w in ws]
    fails, at = [], 0
    for r in rows:
        if not str(r.get("vo") or "").strip():
            continue
        tgt = [_norm(t) for t in r["vo"].split() if _norm(t)]
        hit = next((i for i in range(at, len(toks) - len(tgt) + 1) if toks[i:i + len(tgt)] == tgt), None)
        if hit is None:
            fails.append({"check": "VO", "beats": [r.get("beat")], "detail": f"vo {r['vo']!r} not found on the master after the "
                          "previous row — copy it verbatim from the script, in order"})
            continue
        r["_vo"] = (ws[hit][0], ws[hit + len(tgt) - 1][1], hit, hit + len(tgt) - 1)
        at = hit + len(tgt)
    order = []
    for r in rows:
        if r.get("take") and (not order or order[-1][0] != r["take"]):
            order.append((r["take"], []))
        if r.get("take"):
            order[-1][1].append(r)
    starts = [min((r["_vo"][0] for r in rs if "_vo" in r), default=None) for _, rs in order]
    timing = []
    for k, (t, rs) in enumerate(order):
        s0 = starts[k]
        nxt = next((x for x in starts[k + 1:] if x is not None), None)
        if s0 is None:
            vo_s = 0.0
        else:
            end = (nxt - lead) if nxt is not None else max(r["_vo"][1] for r in rs if "_vo" in r) + tail
            vo_s = max(end - (s0 - lead), 0.0)
        need = vo_s + sum(hold(r) for r in rs)
        call = max(4, math.ceil(need - 1e-6))
        cap = ceiling(rs, max_seconds, max_talk)
        for r in rs:  # each row on screen for its own VO (+ its hold), the take's last row to the next take's cut
            if "_vo" in r:
                m = r["_vo"][1] - r["_vo"][0] + hold(r)
                if r.get("duration") and float(r["duration"]) + 1e-6 < m:
                    fails.append({"check": "VO_SHORT", "beats": [r.get("beat")], "detail": f"duration {r['duration']}s but its VO "
                                  f"runs {m:.2f}s on the master — the picture would leave mid-line; set it from the VO (--write)"})
        if need > cap:
            # the last sentence end inside the ceiling: where the take splits (split: "length", end_pos -> start_pos)
            limit, cut = (s0 or 0) - lead + cap - sum(hold(r) for r in rs), None
            for i, w in enumerate(ws):
                if s0 is not None and s0 <= w[1] <= limit and w[2].rstrip().endswith((".", "!", "?")):
                    cut = w
            fails.append({"check": "VO_LONG", "beats": [r.get("beat") for r in rs], "detail": f"take {t} needs {need:.1f}s for its "
                          f"VO and holds (> {cap:g}s) — split it with split: \"length\" at the sentence end"
                          + (f" after {cut[2]!r} ({cut[1]:.2f}s)" if cut else " (no sentence end inside — split the row)")
                          + ", end_pos -> start_pos"})
        timing.append({"take": t, "vo_s": round(vo_s, 2), "hold_s": round(sum(hold(r) for r in rs), 2),
                       "duration": call, "conversation": is_talk(rs)})
        rs[0]["take_duration"] = call
        for r in rs:
            if "_vo" in r:
                r["duration"] = round(r["_vo"][1] - r["_vo"][0] + hold(r), 2)
            elif r.get("hold_s") is not None or r.get("dialogue"):
                r["duration"] = round(hold(r), 2)
    for r in rows:
        r.pop("_vo", None)
    return fails, timing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--suggest", action="store_true")
    ap.add_argument("--write")
    ap.add_argument("--md")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--max-shots", type=int, default=None, help="--legacy only (4): new builds have no cap — a shot every 2–5 s (V7.99.0)")
    ap.add_argument("--max-seconds", type=float, default=None, help="a take's ceiling: 30 s (V7.98.0, every scene); --legacy 15")
    ap.add_argument("--legacy", action="store_true", help="a build planned before V7.98.0: 15 s action takes, split \"insert\" accepted")
    ap.add_argument("--max-talk-seconds", type=float, default=30, help="a conversation take's ceiling (V7.93.0): Seedance's longest call")
    ap.add_argument("--vo", help="the narration master — each take's duration is measured from the VO it carries (V7.93.0)")
    ap.add_argument("--vo-words", help="word timings JSON instead of --vo: [[start, end, word], ...]")
    ap.add_argument("--script", help="with --vo: the verbatim script lines (script_lines.py), aligned onto the transcript")
    ap.add_argument("--model", default="medium.en")
    a = ap.parse_args()
    parts = Path(a.plan).resolve().parts
    if "builds" in parts[:-1] and parts[parts.index("builds") + 1] in PRE_V799:
        a.legacy = True
    if a.max_seconds is None:
        a.max_seconds = 15.0 if a.legacy else 30.0
    data = json.loads(Path(a.plan).read_text())
    rows_all = data if isinstance(data, list) else data.get("rows", [])
    rows = film_rows(rows_all)
    if not rows:
        print("TAKES PASS (no film shots)")
        sys.exit(0)
    vo_fails, timing = [], []
    if a.vo or a.vo_words:  # measure first, so --suggest groups on the VO's real seconds
        ws = vo_words(a)
        for r in rows:
            r.setdefault("take", r.get("beat"))  # provisional: one row per take, to time each row
        provisional = not any(r.get("take") != r.get("beat") for r in rows)
        vo_fails, timing = measure(rows, ws, a.max_seconds, a.max_talk_seconds)
        if provisional and a.suggest:
            for r in rows:
                r.pop("take", None); r.pop("take_duration", None)
    if a.suggest:
        takes = suggest(rows, a.max_shots, a.max_seconds, a.max_talk_seconds, a.legacy)
        print(f"{len(rows)} rows -> {len(takes)} takes (Seedance calls)")
        for t in takes:
            print(f"  {t[0]['take']:10} {t[0].get('take_kind', 'single'):8} {', '.join(r.get('beat') + ('+' if r.get('joins') else '') for r in t)}"
                  f"{'  [split: ' + t[0]['split'] + ']' if t[0].get('split') else ''}")
        if a.vo or a.vo_words:
            vo_fails, timing = measure(rows, ws, a.max_seconds, a.max_talk_seconds)
    if timing:
        total = sum(x["duration"] for x in timing)
        print(f"VO-timed takes (V7.93.0): film runs {total}s in {len(timing)} takes")
        for x in timing:
            print(f"  {x['take']:10} {x['duration']:>3}s  (VO {x['vo_s']}s + holds {x['hold_s']}s){'  conversation' if x['conversation'] else ''}")
    if a.write:
        Path(a.write).write_text(json.dumps(data, indent=1, ensure_ascii=False))
    out, takes = check(rows, a.max_shots, a.max_seconds, a.max_talk_seconds, a.legacy)
    out = vo_fails + out
    if a.md:
        md = ["### Takes", "", "One scene in one place is one take — one Seedance call up to 30 s (§24K part 5, V7.98.0), "
              "covered inside it in a new shot every 2–5 s (V7.99.0). "
              f"{len(rows)} rows in {len(takes)} takes.", "",
              "| Take | Kind | Rows | Length | Starts | Ends | Split |", "|---|---|---|---|---|---|---|"]
        for t, rs in takes.items():
            ln = rs[0].get("take_duration") or (sum(float(r.get("duration") or 0) for r in rs) or "")
            md.append(f"| {t} | {rs[0].get('take_kind', 'single')}{' · conversation' if is_talk(rs) else ''} | "
                      f"{', '.join(r.get('beat', '') + ('+' if r.get('joins') else '') for r in rs)} | {ln}{'s' if ln else ''} | "
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
