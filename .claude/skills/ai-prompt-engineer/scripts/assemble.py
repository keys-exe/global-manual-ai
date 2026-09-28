#!/usr/bin/env python3
"""§30H — place B-roll on its lines, close every hole, render and verify a rough cut.

Usage:
  assemble.py PLAN.json [--out ROUGH.mp4] [--min-th 1.5] [--lead 0.1] [--skip 0.4] [--fps 24] [--dry-run]
  assemble.py PLAN.json --lengths      # before any B-roll call: the length each clip needs (E6)

PLAN.json:
{
  "audio": "voice/Knee_master.mp3",          # the master — wall-to-wall, never cut
  "script": "work/script.lines.txt",          # the verbatim spoken lines (script_lines.py):
                                              # phrases are found in the SCRIPT, timed by
                                              # aligning the transcript to it (so "seventeen"
                                              # still matches when the transcript says "17")
  "base":  "th/talking_heads.mp4" | null,     # talking-head track aligned to the master;
                                              # null = voice-only build: every frame must be B-roll
  "broll": [ {"beat": "BR-01", "clip": "renders/BR-01.mp4",
              "phrase": "seventeen times your bodyweight",
              "key": "bodyweight",            # optional: the word the picture shows —
                                              # the cut lands on it instead of the phrase's first word
              "peak": 2.1,                    # optional: second in the clip where its action
                                              # peaks — the in-point puts it on the key word
              "in": 0.0,                      # optional: explicit in-point (overrides skip/peak)
              "out": 2.4,                     # optional: the clip's clean part ends here (the
                                              # user's "use only up to here"); nothing after it is used
              "max": 6,                       # optional (--lengths): longest call for this row;
                                              # default 6s — human motion distorts in longer clips
              "layout": {"type": "full"}}, ... ],     # optional, default full (§42 Part 3A)
  "punch_in": [ {"phrase": "and that's when", "scale": 1.15}, ... ],   # optional
  "th_focus_y": 0.4                            # optional: face height in the TH frame (0-1)
}

Layouts (the inspo's edit grammar, EDIT-[BUILD], §42 Part 3A / §30H):
  {"type": "full"}                              B-roll fills the frame (default)
  {"type": "split", "broll_pos": "top"|"bottom", "ratio": 0.5}
                                                B-roll in one band (ratio of the height,
                                                0.3-0.7), talking head in the other,
                                                cropped around th_focus_y
  {"type": "pip", "over": "th"|"broll", "corner": "tl"|"tr"|"bl"|"br",
   "scale": 0.35, "border": 0}                  over "th": B-roll box over the talking
                                                head; over "broll": talking-head box over
                                                the B-roll. scale = box width / frame width
                                                (0.2-0.5), border in px (white)
  split and pip need a talking-head track (base); in a voice-only build they FAIL.
Punch-ins: the talking head cuts in to `scale` (1.05-1.5) on the phrase's first word
and holds until the next B-roll or the next punch-in (scale 1.0 = punch back out).
A punch-in landing under a B-roll is reported and ignored.

Rules (§30H):
  1. PLACE   each B-roll cuts in --lead (3 frames) before its anchor word: the
             phrase's `key` word when given, else its first word (word timestamps
             of the master; never before 0 or inside the previous clip's first
             2.0s). It plays from its in-point, not frame 0: `in` if given, else
             `peak` minus the lead-to-key time, else --skip (0.4s — the start
             image's static opening). It runs until the next B-roll starts, the
             phrase's line ends, or the clip runs out — whichever is first.
  2. JOIN    two B-rolls that meet are joined frame-exact: no gap, no overlap.
  3. FLICKER a talking-head window shorter than --min-th between two B-rolls is a
             flicker. Closed by, in order: giving back the skipped opening (a
             skip/peak in-point moves toward 0); extending the earlier clip with its
             own footage; slowing it down to no slower than 0.8x (never in a Mode 4/5
             plan — §24L, no speed change); else FAIL NEED_LONGER
             (regenerate that clip at a longer duration).
  4. HOLE    in a voice-only build (base null) every uncovered moment is a hole and
             is closed the same way; an unclosable hole is a FAIL.
  5. HOLD    every B-roll holds ~3.0s (HOLD) when the next B-roll allows it, holding over the next
             words — never leaving a face window under --min-th (it holds to the next cut
             when its footage reaches, else stops --min-th short of it); under 2.0s (MIN_FLASH) is a FLASH FAIL (merge the rows) (V7.65.0).
  6. LAYOUT  full screen is the default: split/pip on at most 1 B-roll in 5, never two in a row.
Then renders (1080x1920 at --fps, default 24 = Kling's native rate, so no frame
is repeated; the master as the only audio) and verifies the
render: duration equals the master, no black frames, every cut where the EDL says.
Prints JSON (EDL, fixes, failures, verification). Exit 0 = PASS, 2 = FAIL.

--lengths (E6): run on the plan before the B-roll is generated (clips may be absent).
For each B-roll: its cut, how long it will be on screen (to the next cut; in a
talking-head build to its line end unless the gap to the next cut is a flicker),
and the call duration = on-screen + skip + 0.5s handle, rounded up, Kling 3-15s.
Over the row's `max` (default 6s, §27G: one action per clip) -> SPLIT: two clips,
at a word boundary. Sized this way, no clip needs
slowing down to close a flicker or hole.

Setup: pip install -q imageio-ffmpeg faster-whisper
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

sys.path.insert(0, str(Path(__file__).parent))
from trim import words, duration  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 24                     # set from --fps; Kling renders 24 fps
MIN_SLOW = 0.8
FILM = False                 # plan "mode" 4/5: no speed change ever (§24L)
MIN_FLASH = 2.0                # §30H rule 5 (V7.65.0): every B-roll holds >= 2.0s on screen (was 0.8s)
HOLD = 3.0                     # §30H rule 5 (V7.65.0): a B-roll holds about 3s when the next one allows it
MAX_SPLIT_SHARE = 0.2          # §30H layouts (V7.65.0): full is the default; split/pip at most 1 in 5, never two in a row
HANDLE = 0.5                 # E6: seconds of spare footage on every call
KLING_MIN, KLING_MAX = 3, 15
W, H = 1080, 1920
CORNER_MARGIN = 48


def even(x):
    return int(round(x / 2.0)) * 2


def check_layout(b, has_base):
    """Normalise a B-roll's layout; return (layout, error)."""
    lay = dict(b.get("layout") or {"type": "full"})
    t = lay.get("type", "full")
    if t == "full":
        return {"type": "full"}, None
    if not has_base:
        return lay, f"layout {t} needs a talking-head track; this build is voice-only"
    if t == "split":
        lay.setdefault("broll_pos", "top"); lay.setdefault("ratio", 0.5)
        if lay["broll_pos"] not in ("top", "bottom") or not 0.3 <= lay["ratio"] <= 0.7:
            return lay, "split needs broll_pos top|bottom and ratio 0.3-0.7"
        return lay, None
    if t == "pip":
        lay.setdefault("over", "th"); lay.setdefault("corner", "tr")
        lay.setdefault("scale", 0.35); lay.setdefault("border", 0)
        if lay["over"] not in ("th", "broll") or lay["corner"] not in ("tl", "tr", "bl", "br") \
                or not 0.2 <= lay["scale"] <= 0.5:
            return lay, "pip needs over th|broll, corner tl|tr|bl|br and scale 0.2-0.5"
        return lay, None
    return lay, f"unknown layout type {t!r}"


def norm(t):
    return re.sub(r"[^a-z0-9']", "", t.lower())


def find_phrase(ws, phrase, after=0):
    target = [norm(t) for t in phrase.split() if norm(t)]
    toks = [norm(w[2]) for w in ws]
    for i in range(after, len(toks) - len(target) + 1):
        if toks[i:i + len(target)] == target:
            return i, i + len(target) - 1
    return None


def align(script_words, ws):
    """Give every script word a (start, end) from the transcript. Matched words take
    their transcript time; unmatched runs are spread evenly across the gap."""
    import difflib
    a = [norm(w) for w in script_words]
    b = [norm(w[2]) for w in ws]
    times = [None] * len(a)
    for blk in difflib.SequenceMatcher(None, a, b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            times[blk.a + k] = (ws[blk.b + k][0], ws[blk.b + k][1])
    total_end = ws[-1][1] if ws else 0.0
    i = 0
    while i < len(times):
        if times[i] is None:
            j = i
            while j < len(times) and times[j] is None:
                j += 1
            t0 = times[i - 1][1] if i > 0 else (ws[0][0] if ws else 0.0)
            t1 = times[j][0] if j < len(times) else total_end
            step = max(t1 - t0, 0.0) / (j - i)
            for k in range(i, j):
                times[k] = (t0 + step * (k - i), t0 + step * (k - i + 1))
            i = j
        else:
            i += 1
    return [(times[k][0], times[k][1], script_words[k]) for k in range(len(a))]


def line_end(ws, j):
    """End time of the sentence containing word j."""
    k = j
    while k < len(ws) - 1 and not re.search(r"[.!?]$", ws[k][2]):
        k += 1
    return ws[k][1]


def join_media(root, spec, kind):
    """One path, or a list of paths joined in order (hook + body)."""
    if not isinstance(spec, list):
        return root / spec
    if len(spec) == 1:
        return root / spec[0]
    tmp = root / "_joined"
    tmp.mkdir(exist_ok=True)
    out = tmp / ("_".join(Path(x).stem for x in spec) + (".wav" if kind == "audio" else ".mp4"))
    ins = sum([["-i", str(root / x)] for x in spec], [])
    n = len(spec)
    if kind == "audio":
        graph = "".join(f"[{k}:a]aresample=48000,aformat=channel_layouts=mono[a{k}];" for k in range(n)) + \
                "".join(f"[a{k}]" for k in range(n)) + f"concat=n={n}:v=0:a=1[o]"
        extra = ["-c:a", "pcm_s16le"]
    else:
        graph = "".join(f"[{k}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps={FPS},setsar=1[v{k}];"
                        for k in range(n)) + "".join(f"[v{k}]" for k in range(n)) + f"concat=n={n}:v=1:a=0[o]"
        extra = ["-c:v", "libx264", "-crf", "16"]
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *ins, "-filter_complex", graph,
                    "-map", "[o]", *extra, str(out)], check=True)
    return out


def snap(t):
    return round(round(t * FPS) / FPS, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--out")
    ap.add_argument("--min-th", type=float, default=1.5)
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--lead", type=float, default=0.1, help="cut this many seconds before the anchor word (3 frames)")
    ap.add_argument("--skip", type=float, default=0.4, help="default in-point: skip the clip's static opening")
    ap.add_argument("--lengths", action="store_true", help="print each B-roll's required call duration (E6) and exit")
    ap.add_argument("--fps", type=int, default=24, help="timeline frame rate; 24 = Kling's native rate (no repeated frames)")
    ap.add_argument("--max-clip", type=float, default=6.0, help="--lengths: longest call per clip unless the row sets max (§27G)")
    a = ap.parse_args()
    global FPS
    FPS = a.fps

    root = Path(a.plan).parent
    plan = json.loads(Path(a.plan).read_text())
    # A hook variant is [hook, body]: lists are joined in order into one continuous
    # master, one script and one talking-head track, so §30H holds across the seam.
    global FILM
    FILM = int(plan.get("mode", 1)) in (4, 5)   # §24L: film clips never change speed
    audio = join_media(root, plan["audio"], "audio")
    base = join_media(root, plan["base"], "video") if plan.get("base") else None
    total = duration(audio)
    # Word timings are taken PER PART (hook alone, body alone) and offset by the
    # parts before it, so the body is timed identically in every hook variant.
    parts = plan["audio"] if isinstance(plan["audio"], list) else [plan["audio"]]
    scripts = plan.get("script")
    scripts = (scripts if isinstance(scripts, list) else [scripts]) if scripts else [None] * len(parts)
    ws, offset = [], 0.0
    for part, sc in zip(parts, scripts):
        pw = words(root / part, a.model)
        if sc:
            pw = align((root / sc).read_text(encoding="utf-8").split(), pw)
        ws += [(s0 + offset, e0 + offset, w) for s0, e0, w in pw]
        offset += snap(duration(root / part))  # each part starts on a whole frame
    fails, fixes, edl = [], [], []

    # 1. PLACE — a lead before the anchor word (the key word, else the phrase's first
    # word); play from the in-point, not the start image's static opening
    cursor = 0
    for b in plan["broll"]:
        hit = find_phrase(ws, b["phrase"], cursor)
        if not hit:
            fails.append({"beat": b["beat"], "fail": "PHRASE_NOT_FOUND", "phrase": b["phrase"]})
            continue
        i, j = hit
        cursor = i + 1
        anchor = i
        if b.get("key"):
            k = find_phrase(ws, b["key"], i)
            if not k or k[1] > j:
                fails.append({"beat": b["beat"], "fail": "KEY_NOT_IN_PHRASE", "key": b["key"], "phrase": b["phrase"]})
            else:
                anchor = k[0]
        word_t = ws[anchor][0]
        lay, lerr = check_layout(b, base is not None)
        if lerr:
            fails.append({"beat": b["beat"], "fail": "LAYOUT_INVALID", "detail": lerr})
        clip = root / b["clip"] if b.get("clip") else None
        if clip is None and not a.lengths:
            fails.append({"beat": b["beat"], "fail": "NO_CLIP", "detail": "no clip yet — run --lengths to size the call"})
            continue
        edl.append({"beat": b["beat"], "clip": str(clip) if clip else None, "phrase": b["phrase"],
                    "key": ws[anchor][2], "layout": lay, "word_t": word_t,
                    "start": snap(max(0.0, word_t - a.lead)), "line_end": snap(line_end(ws, j)),
                    "in_spec": b.get("in"), "peak": b.get("peak"), "max": b.get("max", a.max_clip),
                    "clip_len": (min(duration(clip), float(b["out"])) if b.get("out") else duration(clip)) if clip else None,
                    "speed": 1.0})
    edl.sort(key=lambda e: e["start"])
    for n, e in enumerate(edl):
        # the lead never cuts into the previous clip's first MIN_FLASH seconds
        if n and e["start"] < edl[n - 1]["start"] + MIN_FLASH:
            e["start"] = snap(max(e["word_t"], edl[n - 1]["start"] + MIN_FLASH))
        lead = e["word_t"] - e["start"]
        if e["in_spec"] is not None:
            e["in"], e["flex"] = float(e["in_spec"]), False
        elif e["peak"] is not None:
            e["in"], e["flex"] = max(0.0, float(e["peak"]) - lead), True
        else:
            e["in"], e["flex"] = a.skip, True
        e["skip"] = e["in"]

    if a.lengths:
        out = []
        for n, e in enumerate(edl):
            nxt = edl[n + 1]["start"] if n + 1 < len(edl) else total
            end = nxt
            if base is not None and n + 1 < len(edl) and nxt - max(e["line_end"], e["start"]) >= a.min_th:
                end = max(e["line_end"], e["start"])   # a deliberate return to face
            if base is not None and n + 1 == len(edl):
                end = max(e["line_end"], e["start"])
            on = max(end - e["start"], min(HOLD, nxt - e["start"]))   # the hold (rule 5)
            if base is not None and n + 1 < len(edl) and 1e-3 < nxt - e["start"] - on < a.min_th:
                on = nxt - e["start"]   # a hold never leaves a face window under --min-th
            need = on + e["skip"] + HANDLE
            call = max(KLING_MIN, int(-(-need // 1)))
            row = {"beat": e["beat"], "cut_s": e["start"], "anchor": e["key"], "on_screen_s": round(on, 2),
                   "skip_s": round(e["skip"], 2), "call_s": call}
            cap = min(KLING_MAX, e["max"])
            if call > cap:
                row["call_s"] = int(cap)
                row["flag"] = f"SPLIT — needs {need:.1f}s, over {cap:g}s; split the phrase into two clips at a word boundary"
            out.append(row)
        print(json.dumps({"master_s": round(total, 3), "lead_s": a.lead, "skip_s": a.skip,
                          "lengths": out, "failures": fails}, indent=2))
        sys.exit(2 if fails else 0)

    def give_back(e, need):
        """Move a skip/peak in-point toward 0 until the clip has `need` seconds; return what it has."""
        avail = e["clip_len"] - e["in"]
        if avail < need and e["flex"] and e["in"] > 0:
            take = min(e["in"], need - avail)
            e["in"] = round(e["in"] - take, 3)
            fixes.append({"beat": e["beat"], "fix": f"gave back {take:.2f}s of the skipped opening (in-point {e['in']:.2f}s)"})
        return e["clip_len"] - e["in"]

    for n, e in enumerate(edl):
        nxt = edl[n + 1]["start"] if n + 1 < len(edl) else total
        want = min(nxt, max(e["line_end"], e["start"]))
        avail = give_back(e, want - e["start"])
        e["end"] = snap(min(want, e["start"] + avail))
        if e["end"] <= e["start"]:
            e["end"] = snap(min(nxt, e["start"] + avail))

    # 2-4. JOIN / FLICKER / HOLE
    def close(e, target, why):
        need = target - e["start"]
        avail = give_back(e, need)
        if avail >= need - 1e-3:
            e["end"] = snap(target); fixes.append({"beat": e["beat"], "fix": f"{why}: extended with own footage to {target:.2f}s"}); return True
        speed = avail / need
        if speed >= MIN_SLOW and not FILM:
            e["end"] = snap(target); e["speed"] = round(speed, 3)
            fixes.append({"beat": e["beat"], "fix": f"{why}: slowed to {speed:.2f}x to reach {target:.2f}s"}); return True
        fails.append({"beat": e["beat"], "fail": "NEED_LONGER",
                      "detail": f"{why}: needs {need:.2f}s of footage, has {avail:.2f}s — regenerate longer"})
        return False

    # 5. HOLD — a B-roll whose line is shorter than MIN_FLASH holds over the next words
    # (up to the next B-roll) so it can be read (V7.65.0)
    for n, e in enumerate(edl):
        nxt = edl[n + 1]["start"] if n + 1 < len(edl) else total
        if e["end"] - e["start"] < HOLD - 1e-3:
            target = snap(min(nxt, e["start"] + HOLD))
            if base is not None and n + 1 < len(edl) and 1e-3 < nxt - target < a.min_th:
                # never hold into a face window and leave a flicker: hold to the next cut when the
                # footage reaches it, else stop so the face keeps at least --min-th
                target = nxt if give_back(e, nxt - e["start"]) >= nxt - e["start"] - 1e-3 else snap(nxt - a.min_th)
            if target > e["end"] + 1e-3:
                # the hold uses the clip's own footage only — never slowed to reach it
                avail = give_back(e, target - e["start"])
                reach = snap(min(target, e["start"] + avail))
                if reach > e["end"] + 1e-3:
                    e["end"] = reach
                    fixes.append({"beat": e["beat"], "fix": f"HOLD: held to {reach - e['start']:.2f}s on screen"})
                if e["end"] - e["start"] < MIN_FLASH - 1e-3:   # still unreadable: slow (>= 0.8x) or FAIL
                    close(e, snap(min(nxt, e["start"] + MIN_FLASH)), "HOLD")

    for n, e in enumerate(edl):
        nxt = edl[n + 1]["start"] if n + 1 < len(edl) else None
        gap_to = nxt if nxt is not None else total
        gap = gap_to - e["end"]
        if gap <= 1e-3:
            e["end"] = snap(gap_to) if nxt is not None else e["end"]
            continue
        if base is None:
            close(e, gap_to, "HOLE")
        elif nxt is not None and gap < a.min_th:
            close(e, gap_to, f"FLICKER {gap:.2f}s")
    if base is None and edl and edl[0]["start"] > 1e-3:
        fails.append({"beat": edl[0]["beat"], "fail": "HOLE_AT_START",
                      "detail": f"0.00–{edl[0]['start']:.2f}s uncovered — place a B-roll on the opening line"})
    for e in edl:
        if e["end"] - e["start"] < MIN_FLASH - 1e-3:
            fails.append({"beat": e["beat"], "fail": "FLASH", "detail": f"on screen {e['end']-e['start']:.2f}s < {MIN_FLASH}s — merge the row with its neighbour or give it a longer line"})
    # layout mix: full screen is the default; split/pip sparingly (V7.65.0, user 2026-09-28)
    if base is not None and edl:
        boxed = [e for e in edl if e["layout"]["type"] != "full"]
        if len(boxed) > MAX_SPLIT_SHARE * len(edl) + 1e-9:
            fails.append({"fail": "LAYOUT_MIX", "detail": f"{len(boxed)} of {len(edl)} B-rolls are split/pip — at most {int(MAX_SPLIT_SHARE * 100)}%"})
        for p0, p1 in zip(edl, edl[1:]):
            if p0["layout"]["type"] != "full" and p1["layout"]["type"] != "full":
                fails.append({"fail": "LAYOUT_MIX", "detail": f"{p0['beat']} and {p1['beat']} are both split/pip — never two in a row"})

    # timeline segments
    raw, t = [], 0.0
    for e in edl:
        if e["start"] - t > 1e-3:
            raw.append({"kind": "TH" if base else "HOLE", "start": t, "end": e["start"]})
        raw.append({"kind": "BR", "beat": e["beat"], "layout": e["layout"]["type"], "start": e["start"], "end": e["end"]})
        t = e["end"]
    if total - t > 1e-3:
        raw.append({"kind": "TH" if base else "HOLE", "start": t, "end": total})
    for s in raw:
        if s["kind"] == "TH" and s["end"] - s["start"] < a.min_th and 0 < s["start"] and s["end"] < total:
            fails.append({"fail": "FLICKER_REMAINS", "detail": f"TH {s['start']:.2f}–{s['end']:.2f}s"})
        if s["kind"] == "HOLE":
            fails.append({"fail": "HOLE_REMAINS", "detail": f"{s['start']:.2f}–{s['end']:.2f}s"})

    # punch-ins: split talking-head runs at each punch; the zoom holds until the next
    # B-roll or the next punch-in
    punches, pc = [], 0
    for p in plan.get("punch_in", []):
        hit = find_phrase(ws, p["phrase"], pc)
        sc = float(p.get("scale", 1.15))
        if not hit:
            fails.append({"fail": "PUNCH_PHRASE_NOT_FOUND", "phrase": p["phrase"]}); continue
        if not (sc == 1.0 or 1.05 <= sc <= 1.5):
            fails.append({"fail": "PUNCH_SCALE", "phrase": p["phrase"], "detail": "scale 1.0 or 1.05-1.5"}); continue
        pc = hit[0] + 1
        punches.append((snap(ws[hit[0]][0]), sc, p["phrase"]))
    warnings = []
    if punches and base is None:
        fails.append({"fail": "PUNCH_NEEDS_TH", "detail": "punch-ins need a talking-head track"})
    segs = []
    for s in raw:
        if s["kind"] != "TH":
            segs.append(s); continue
        cuts_at = [(pt, sc) for pt, sc, _ in punches if s["start"] - 1e-3 <= pt < s["end"] - 1e-3]
        t0, zoom = s["start"], 1.0
        for pt, sc in cuts_at:
            if pt - t0 > 1e-3:
                segs.append({"kind": "TH", "start": t0, "end": pt, "zoom": zoom})
            t0, zoom = max(pt, t0), sc
        segs.append({"kind": "TH", "start": t0, "end": s["end"], "zoom": zoom})
    for pt, sc, ph in punches:
        if any(s["kind"] == "BR" and s["start"] + 1e-3 < pt < s["end"] - 1e-3 for s in raw):
            warnings.append({"punch": ph, "warning": f"lands under a B-roll at {pt:.2f}s — ignored"})

    report = {"master_s": round(total, 3), "min_th_s": a.min_th, "edl": edl,
              "timeline": [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in s.items()} for s in segs],
              "fixes": fixes, "warnings": warnings, "failures": fails}
    if fails or a.dry_run:
        report["status"] = "FAIL" if fails else "PLANNED"
        print(json.dumps(report, indent=2)); sys.exit(2 if fails else 0)

    # render: concat of segments, master audio only
    out = Path(a.out) if a.out else root / "rough_cut.mp4"
    focus = float(plan.get("th_focus_y", 0.4))
    V = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps={FPS},setsar=1"
    END = ",setsar=1,format=yuv420p"
    inputs, parts = [], []

    def add(path):
        """Register an input file; return its ffmpeg input index."""
        inputs.extend(["-i", str(path)])
        return len(inputs) // 2 - 1

    def th_chain(idx, s0, s1):
        return f"[{idx}:v]trim={s0}:{s1},setpts=PTS-STARTPTS,{V}"

    def br_chain(e, dur, w, h):
        src_len = dur * e["speed"]
        fit = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={FPS},setsar=1"
        return (f"[{add(e['clip'])}:v]trim={e['in']}:{e['in'] + src_len},setpts=(PTS-STARTPTS)/{e['speed']},"
                f"{fit},trim=0:{dur},setpts=PTS-STARTPTS")

    for n, s in enumerate(segs):
        dur = s["end"] - s["start"]
        if s["kind"] == "TH":
            z = s.get("zoom", 1.0)
            zoom = "" if z == 1.0 else (f",scale=trunc(iw*{z}/2)*2:trunc(ih*{z}/2)*2,"
                                        f"crop={W}:{H}:(in_w-{W})/2:(in_h-{H})*{focus}")  # the face point holds still
            parts.append(f"{th_chain(add(base), s['start'], s['end'])}{zoom}{END}[s{n}]")
            continue
        e = next(x for x in edl if x["beat"] == s["beat"])
        lay = e["layout"]
        if lay["type"] == "full":
            parts.append(f"{br_chain(e, dur, W, H)}{END}[s{n}]")
        elif lay["type"] == "split":
            hb = even(H * lay["ratio"]); ht = H - hb
            y = even(min(max(H * focus - ht / 2, 0), H - ht))
            parts.append(f"{br_chain(e, dur, W, hb)}[b{n}]")
            parts.append(f"{th_chain(add(base), s['start'], s['end'])},crop={W}:{ht}:0:{y}[t{n}]")
            order = f"[b{n}][t{n}]" if lay["broll_pos"] == "top" else f"[t{n}][b{n}]"
            parts.append(f"{order}vstack=inputs=2{END}[s{n}]")
        else:  # pip
            bw = even(W * lay["scale"]); bh = even(bw * 16 / 9); bd = int(lay.get("border", 0))
            fw, fh = bw + 2 * bd, bh + 2 * bd
            x = CORNER_MARGIN if lay["corner"] in ("tl", "bl") else W - fw - CORNER_MARGIN
            y = CORNER_MARGIN * 3 if lay["corner"] in ("tl", "tr") else H - fh - CORNER_MARGIN * 6
            box = f",pad={fw}:{fh}:{bd}:{bd}:white" if bd else ""
            if lay["over"] == "th":
                parts.append(f"{th_chain(add(base), s['start'], s['end'])}[g{n}]")
                parts.append(f"{br_chain(e, dur, bw, bh)}{box}[f{n}]")
            else:
                parts.append(f"{br_chain(e, dur, W, H)}[g{n}]")
                th_box = f"scale={bw}:{bh}:force_original_aspect_ratio=increase,crop={bw}:{bh}"
                parts.append(f"{th_chain(add(base), s['start'], s['end'])},{th_box}{box}[f{n}]")
            parts.append(f"[g{n}][f{n}]overlay={x}:{y}:shortest=1{END}[s{n}]")
    aidx = add(audio)
    graph = ";".join(parts) + ";" + "".join(f"[s{n}]" for n in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=0[v]"
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph,
                    "-map", "[v]", "-map", f"{aidx}:a", "-c:v", "libx264", "-crf", "18",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", str(out)], check=True)

    # verify
    err = subprocess.run([FF, "-hide_banner", "-i", str(out), "-vf", "blackdetect=d=0.03:pic_th=0.98",
                          "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
    black = re.findall(r"black_start:([\d.]+) black_end:([\d.]+)", err)
    got = duration(out)
    report["render"] = {"file": str(out), "duration_s": round(got, 3),
                        "duration_matches_master": abs(got - total) <= 2 / FPS,
                        "black_frames": [(float(x), float(y)) for x, y in black]}
    ok = report["render"]["duration_matches_master"] and not black
    report["status"] = "PASS" if ok else "FAIL"
    print(json.dumps(report, indent=2)); sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
