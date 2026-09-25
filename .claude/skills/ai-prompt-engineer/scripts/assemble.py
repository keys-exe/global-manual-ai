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
  "base":  "th/talking_heads.mp4" | null,     # talking-head track aligned to the master;
                                              # null = voice-only build: every frame must be B-roll
  "broll": [ {"beat": "BR-01", "clip": "renders/BR-01.mp4",
              "phrase": "seventeen times your bodyweight", "in": 0.0}, ... ]
}

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
  5. FLASH   a B-roll on screen for under 0.8s is a FAIL (too short to read).
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

FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 30
MIN_SLOW = 0.8
MIN_FLASH = 0.8


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
        edl.append({"beat": b["beat"], "clip": str(clip), "phrase": b["phrase"],
                    "start": snap(ws[i][0]), "line_end": snap(line_end(ws, j)),
                    "in": b.get("in", 0.0), "clip_len": duration(clip), "speed": 1.0})
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
    for e in edl:
        if e["end"] - e["start"] < MIN_FLASH:
            fails.append({"beat": e["beat"], "fail": "FLASH", "detail": f"on screen {e['end']-e['start']:.2f}s < {MIN_FLASH}s"})

    # timeline segments
    segs, t = [], 0.0
    for e in edl:
        if e["start"] - t > 1e-3:
            segs.append({"kind": "TH" if base else "HOLE", "start": t, "end": e["start"]})
        segs.append({"kind": "BR", "beat": e["beat"], "start": e["start"], "end": e["end"]})
        t = e["end"]
    if total - t > 1e-3:
        segs.append({"kind": "TH" if base else "HOLE", "start": t, "end": total})
    for s in segs:
        if s["kind"] == "TH" and s["end"] - s["start"] < a.min_th and 0 < s["start"] and s["end"] < total:
            fails.append({"fail": "FLICKER_REMAINS", "detail": f"TH {s['start']:.2f}–{s['end']:.2f}s"})
        if s["kind"] == "HOLE":
            fails.append({"fail": "HOLE_REMAINS", "detail": f"{s['start']:.2f}–{s['end']:.2f}s"})

    report = {"master_s": round(total, 3), "min_th_s": a.min_th, "edl": edl,
              "timeline": [{k: (round(v, 3) if isinstance(v, float) else v) for k, v in s.items()} for s in segs],
              "fixes": fixes, "failures": fails}
    if fails or a.dry_run:
        report["status"] = "FAIL" if fails else "PLANNED"
        print(json.dumps(report, indent=2)); sys.exit(2 if fails else 0)

    # render: concat of segments, master audio only
    out = Path(a.out) if a.out else root / "rough_cut.mp4"
    inputs, parts = [], []
    V = "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30,setsar=1"
    for n, s in enumerate(segs):
        if s["kind"] == "TH":
            inputs += ["-i", str(base)]
            parts.append(f"[{n}:v]trim={s['start']}:{s['end']},setpts=PTS-STARTPTS,{V}[s{n}]")
        else:
            e = next(x for x in edl if x["beat"] == s["beat"])
            src_len = (s["end"] - s["start"]) * e["speed"]
            inputs += ["-i", e["clip"]]
            parts.append(f"[{n}:v]trim={e['in']}:{e['in'] + src_len},setpts=(PTS-STARTPTS)/{e['speed']},{V},"
                         f"trim=0:{s['end'] - s['start']}[s{n}]")
    inputs += ["-i", str(audio)]
    graph = ";".join(parts) + ";" + "".join(f"[s{n}]" for n in range(len(segs))) + f"concat=n={len(segs)}:v=1:a=0[v]"
    subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-y", *inputs, "-filter_complex", graph,
                    "-map", "[v]", "-map", f"{len(segs)}:a", "-c:v", "libx264", "-crf", "18",
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
