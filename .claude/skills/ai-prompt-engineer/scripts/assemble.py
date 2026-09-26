#!/usr/bin/env python3
"""§30H — place B-roll on its lines, close every hole, render and verify a rough cut.

Usage:
  assemble.py PLAN.json [--out ROUGH.mp4] [--min-th 1.5] [--dry-run]

PLAN.json:
{
  "audio": "voice/Knee_master.mp3",          # the master — wall-to-wall, never cut
  "script": "work/script.lines.txt",          # the verbatim spoken lines (script_lines.py):
                                              # phrases are found in the SCRIPT, timed by
                                              # aligning the transcript to it (so "seventeen"
                                              # still matches when the transcript says "17")
  "words": "work/master.words.json",         # optional: word timestamps [[start, end, word], ...]
                                              # (one file per part for a hook variant); else
                                              # the master is transcribed here
  "base":  "th/talking_heads.mp4" | null,     # talking-head track aligned to the master;
                                              # null = voice-only build: every frame must be B-roll
  "broll": [ {"beat": "BR-01", "clip": "renders/BR-01.mp4",
              "phrase": "seventeen times your bodyweight",
              "in": "auto",                   # default: the best window (best_window.py);
                                              # a number = a hand-picked clip time (s)
              "key": 2.1,                     # optional: clip time of the READ frame —
                                              # must be on screen, early in the window
              "read": "one small spot below the kneecap takes the load",
              "read_kind": "state",           # state | event | contrast (§30B Part 4)
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
  1. PLACE   each B-roll starts on the first word of its phrase (word timestamps of
             the master) and runs until the next B-roll starts, the phrase's line
             ends, or the clip runs out — whichever is first.
  2. JOIN    two B-rolls that meet are joined frame-exact: no gap, no overlap.
  3. FLICKER a talking-head window shorter than --min-th between two B-rolls is a
             flicker. Closed by, in order: extending the earlier clip with its own
             footage; slowing it down to no slower than 0.8x; else FAIL NEED_LONGER
             (regenerate that clip at a longer duration).
  4. HOLE    in a voice-only build (base null) every uncovered moment is a hole and
             is closed the same way; an unclosable hole is a FAIL.
  5. WINDOW  each B-roll shows its best part, never frame 0 by default: with "in"
             "auto" (the default) the on-screen window is picked from the whole
             clip by best_window.py — most action, still moving at the cut, the
             READ frame ("key") inside it and early. The dead part (standing
             before the step, settling after it) is what gets cut. A key frame
             that is not on screen is a FAIL (KEY_OFF_SCREEN).
  6. FLASH   a B-roll on screen for less than its read floor is a FAIL: state 0.8s,
             event 1.2s, contrast 1.8s (read_kind; 0.8s when not given).
Then renders (1080x1920, 30fps, the master as the only audio) and verifies the
render: duration equals the master, no black frames, every cut where the EDL says.
Prints JSON (EDL, fixes, failures, verification). Exit 0 = PASS, 2 = FAIL.

Setup: pip install -q imageio-ffmpeg faster-whisper
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

sys.path.insert(0, str(Path(__file__).parent))
from trim import words, duration  # noqa: E402
from best_window import pick_window  # noqa: E402

FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 30
MIN_SLOW = 0.8
MIN_FLASH = 0.8
MIN_READ = {"state": 0.8, "event": 1.2, "contrast": 1.8}   # §30H FLASH floors by read kind
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
        graph = "".join(f"[{k}:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1[v{k}];"
                        for k in range(n)) + "".join(f"[v{k}]" for k in range(n)) + f"concat=n={n}:v=1:a=0[o]"
        extra = ["-c:v", "libx264", "-crf", "16"]
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *ins, "-filter_complex", graph,
                    "-map", "[o]", *extra, str(out)], check=True)
    return out


def timed_words(root, plan, model):
    """Script-aligned word timestamps for the whole master. Taken PER PART (hook alone,
    body alone) and offset by the parts before it, so the body is timed identically
    in every hook variant. "words" (one JSON per part) skips transcription."""
    parts = plan["audio"] if isinstance(plan["audio"], list) else [plan["audio"]]
    scripts = plan.get("script")
    scripts = (scripts if isinstance(scripts, list) else [scripts]) if scripts else [None] * len(parts)
    given = plan.get("words")
    given = (given if isinstance(given, list) else [given]) if given else [None] * len(parts)
    ws, offset = [], 0.0
    for part, sc, wf in zip(parts, scripts, given):
        pw = [tuple(x) for x in json.loads((root / wf).read_text())] if wf else words(root / part, model)
        if sc:
            pw = align((root / sc).read_text(encoding="utf-8").split(), pw)
        ws += [(s0 + offset, e0 + offset, w) for s0, e0, w in pw]
        offset += snap(duration(root / part))  # each part starts on a whole frame
    return ws


def snap(t):
    return round(round(t * FPS) / FPS, 4)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan")
    ap.add_argument("--out")
    ap.add_argument("--min-th", type=float, default=1.5)
    ap.add_argument("--model", default="base.en")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    root = Path(a.plan).parent
    plan = json.loads(Path(a.plan).read_text())
    # A hook variant is [hook, body]: lists are joined in order into one continuous
    # master, one script and one talking-head track, so §30H holds across the seam.
    audio = join_media(root, plan["audio"], "audio")
    base = join_media(root, plan["base"], "video") if plan.get("base") else None
    total = duration(audio)
    ws = timed_words(root, plan, a.model)
    fails, fixes, edl, warnings = [], [], [], []

    # 1. PLACE
    cursor = 0
    for b in plan["broll"]:
        hit = find_phrase(ws, b["phrase"], cursor)
        if not hit:
            fails.append({"beat": b["beat"], "fail": "PHRASE_NOT_FOUND", "phrase": b["phrase"]})
            continue
        i, j = hit
        cursor = i + 1
        clip = root / b["clip"]
        lay, lerr = check_layout(b, base is not None)
        if lerr:
            fails.append({"beat": b["beat"], "fail": "LAYOUT_INVALID", "detail": lerr})
        spec = b.get("in", "auto")
        kind = b.get("read_kind")
        if kind is not None and kind not in MIN_READ:
            fails.append({"beat": b["beat"], "fail": "READ_KIND_INVALID", "detail": f"{kind!r}: state|event|contrast"})
        if kind is None:
            warnings.append({"beat": b["beat"], "warning": "no read_kind — FLASH floor 0.8s used"})
        clen = duration(clip)
        if spec != "auto" and not 0 <= float(spec) < clen:
            fails.append({"beat": b["beat"], "fail": "IN_OUTSIDE_CLIP", "detail": f"in {spec}s, clip {clen:.2f}s"})
            spec = 0.0
        edl.append({"beat": b["beat"], "clip": str(clip), "phrase": b["phrase"], "layout": lay,
                    "read": b.get("read"), "read_kind": kind, "key": b.get("key"),
                    "start": snap(ws[i][0]), "line_end": snap(line_end(ws, j)),
                    "in": 0.0 if spec == "auto" else float(spec), "in_source": "auto" if spec == "auto" else "set",
                    "clip_len": clen, "speed": 1.0})
    edl.sort(key=lambda e: e["start"])
    for n, e in enumerate(edl):
        nxt = edl[n + 1]["start"] if n + 1 < len(edl) else total
        avail = e["clip_len"] - e["in"]
        e["end"] = snap(min(nxt, max(e["line_end"], e["start"]), e["start"] + avail))
        if e["end"] <= e["start"]:
            e["end"] = snap(min(nxt, e["start"] + avail))

    # 2-4. JOIN / FLICKER / HOLE
    def close(e, target, why):
        need = target - e["start"]
        avail = e["clip_len"] - e["in"]
        if avail >= need - 1e-3:
            e["end"] = snap(target); fixes.append({"beat": e["beat"], "fix": f"{why}: extended with own footage to {target:.2f}s"}); return True
        speed = avail / need
        if speed >= MIN_SLOW:
            e["end"] = snap(target); e["speed"] = round(speed, 3)
            fixes.append({"beat": e["beat"], "fix": f"{why}: slowed to {speed:.2f}x to reach {target:.2f}s"}); return True
        fails.append({"beat": e["beat"], "fail": "NEED_LONGER",
                      "detail": f"{why}: needs {need:.2f}s of footage, has {avail:.2f}s — regenerate longer"})
        return False

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

    # 5. WINDOW — the best part of each clip, never frame 0 by default
    for e in edl:
        src = (e["end"] - e["start"]) * e["speed"]
        if e["in_source"] == "auto":
            if e["clip_len"] - src > 1.0 / FPS:
                r = pick_window(e["clip"], src, e["key"])
                if r.get("pick") is None:
                    fails.append({"beat": e["beat"], "fail": "KEY_OFF_SCREEN", "detail": r.get("fail")})
                else:
                    e["in"] = r["pick"]["in"]
                    e["window_pick"] = {k: r["pick"][k] for k in ("action", "dead_share", "moving_at_cut", "key_at_s")
                                        if k in r["pick"]}
                    if r.get("from_frame0"):
                        e["window_pick"]["frame0_action"] = r["from_frame0"]["action"]
                    e["dead_runs_s"] = r["dead_runs_s"]
                    if not r["pick"]["moving_at_cut"]:
                        warnings.append({"beat": e["beat"], "warning": "best window is at rest at the cut (§27A) — "
                                         "check the window sheet; §22W Q4"})
                    if r["pick"]["dead_share"] > 0.3:
                        warnings.append({"beat": e["beat"], "warning": f"best window is {r['pick']['dead_share']:.0%} "
                                         "dead footage — the clip has less action than its slot; §22W Q7"})
            else:
                e["window_pick"] = {"note": "on-screen time uses the whole clip"}
        e["in"] = round(min(e["in"], max(0.0, e["clip_len"] - src)), 3)
        e["out"] = round(e["in"] + src, 3)
        e["head_cut_s"], e["tail_cut_s"] = e["in"], round(max(e["clip_len"] - e["out"], 0.0), 3)
        if e["key"] is not None and not e["in"] - 1e-3 <= e["key"] <= e["out"] + 1e-3:
            if not any(f.get("beat") == e["beat"] and f["fail"] == "KEY_OFF_SCREEN" for f in fails):
                fails.append({"beat": e["beat"], "fail": "KEY_OFF_SCREEN",
                              "detail": f"key frame {e['key']:.2f}s is outside the on-screen window {e['in']:.2f}–{e['out']:.2f}s"})

    # 6. FLASH — the read floor by read kind
    for e in edl:
        floor = MIN_READ.get(e["read_kind"], MIN_FLASH)
        if e["end"] - e["start"] < floor - 1e-3:
            fails.append({"beat": e["beat"], "fail": "FLASH",
                          "detail": f"on screen {e['end']-e['start']:.2f}s < {floor}s ({e['read_kind'] or 'no read_kind'})"})

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
    V = f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},fps=30,setsar=1"
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
        fit = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps=30,setsar=1"
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
