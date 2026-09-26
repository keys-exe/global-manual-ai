#!/usr/bin/env python3
"""§30H WINDOW — find the best part of a B-roll clip for its on-screen slot.

Usage:
  best_window.py CLIP.mp4 --len 1.20 [--key 2.10] [--top 3] [--sheet]

A B-roll's on-screen window is never taken from frame 0 by default. This reads the
whole clip's motion (frame difference, smoothed over 0.2s), marks the dead runs
(standing, settling, holding still) and ranks every window of --len seconds:

  - the window with the most action wins;
  - its last 0.2s must still be moving — never at rest at the cut (§27A);
  - --key is the clip time (s) of the frame that shows the line's READ (§30B Part 4),
    judged by the agent from the full-clip sheet. The window must contain it, and
    it should land early: at about a quarter of the window, never later than 0.5s
    into a short one.

The ranking is a motion proxy, not the verdict: the agent confirms the pick on the
window sheet (--sheet, or contact_sheet.py --from/--to) and judges it by §22W.
Prints JSON: motion curve (0.1s bins), dead runs, the ranked candidates, the pick.
"""
import argparse, json, re, subprocess
from pathlib import Path

import imageio_ffmpeg
import numpy as np

FF = imageio_ffmpeg.get_ffmpeg_exe()
FPS = 30
GW, GH = 72, 128          # analysis frame (9:16), grey
SMOOTH_S = 0.2
TAIL_S = 0.2
ABS_DEAD = 0.0008         # mean abs frame difference (0-1): below it only codec noise moves
REL_DEAD = 0.3           # ... dead = below this share of the clip's 90th-percentile motion


def clip_len(path):
    info = subprocess.run([FF, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", info).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def motion(path):
    """Per-frame motion at FPS: mean |frame - previous| in 0-1, smoothed. Index k = time k/FPS."""
    raw = subprocess.run([FF, "-hide_banner", "-loglevel", "error", "-i", str(path), "-vf",
                          f"fps={FPS},scale={GW}:{GH},format=gray", "-f", "rawvideo", "-"],
                         capture_output=True, check=True).stdout
    fr = np.frombuffer(raw, np.uint8).reshape(-1, GH, GW).astype(np.float32) / 255.0
    if len(fr) < 2:
        return np.zeros(len(fr))
    m = np.concatenate([[0.0], np.abs(np.diff(fr, axis=0)).mean(axis=(1, 2))])
    m[0] = m[1]
    k = max(1, int(round(SMOOTH_S * FPS)))
    return np.convolve(m, np.ones(k) / k, mode="same")


def dead_mask(m):
    thr = max(ABS_DEAD, REL_DEAD * float(np.percentile(m, 90))) if len(m) else ABS_DEAD
    return m < thr, thr


def runs(mask):
    out, start = [], None
    for k, d in enumerate(list(mask) + [False]):
        if d and start is None:
            start = k
        elif not d and start is not None:
            if k - start >= int(0.3 * FPS):
                out.append((round(start / FPS, 2), round(k / FPS, 2)))
            start = None
    return out


def pick_window(path, length, key=None, top=3, m=None):
    """Rank every window of `length` s in the clip; return {pick, candidates, ...}."""
    total = clip_len(path)
    m = motion(path) if m is None else m
    dead, thr = dead_mask(m)
    n = int(round(length * FPS))
    tail = max(1, int(round(TAIL_S * FPS)))
    last_in = len(m) - n
    base = {"clip": str(path), "clip_s": round(total, 3), "len_s": round(length, 3),
            "dead_threshold": round(thr, 5), "dead_runs_s": runs(dead)}
    if last_in <= 0:
        return {**base, "pick": {"in": 0.0, "out": round(min(length, total), 3), "why": "window is the whole clip"},
                "candidates": []}
    target = min(0.25 * length, 0.5)
    cands = []
    for s in range(0, last_in + 1):
        w = m[s:s + n]
        c = {"in": round(s / FPS, 3), "out": round((s + n) / FPS, 3),
             "action": round(float(w.mean()), 5),
             "dead_share": round(float(dead[s:s + n].mean()), 3),
             "moving_at_cut": bool(not dead[s + n - tail:s + n].any())}
        score = c["action"] * (1.0 - c["dead_share"])
        if not c["moving_at_cut"]:
            score *= 0.25
        if key is not None:
            pos = key - s / FPS
            if not 0 <= pos <= length:
                continue
            c["key_at_s"] = round(pos, 3)
            score *= 1.0 / (1.0 + 2.0 * abs(pos - target) / max(length, 1e-3))
        c["score"] = round(score, 6)
        cands.append(c)
    if not cands:
        return {**base, "pick": None, "candidates": [],
                "fail": f"no {length:.2f}s window contains the key frame at {key:.2f}s"}
    cands.sort(key=lambda c: -c["score"])
    # keep candidates at least half a window apart so the list shows real alternatives
    shown = []
    for c in cands:
        if all(abs(c["in"] - d["in"]) >= length / 2 for d in shown):
            shown.append(c)
        if len(shown) == top:
            break
    first = next((c for c in cands if c["in"] == 0.0), None)
    return {**base, "pick": shown[0], "candidates": shown,
            "from_frame0": first, "head_cut_s": shown[0]["in"],
            "tail_cut_s": round(max(total - shown[0]["out"], 0.0), 3)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("clip")
    ap.add_argument("--len", type=float, required=True, help="on-screen seconds of source footage")
    ap.add_argument("--key", type=float, help="clip time of the READ frame")
    ap.add_argument("--top", type=int, default=3)
    ap.add_argument("--sheet", action="store_true", help="write a contact sheet of the picked window")
    a = ap.parse_args()
    m = motion(a.clip)
    r = pick_window(a.clip, a.len, a.key, a.top, m)
    r["motion_0p1s"] = [round(float(m[k:k + 3].mean()), 4) for k in range(0, len(m), 3)]
    if a.sheet and r.get("pick"):
        out = Path(a.clip).with_suffix(".window.jpg")
        cs = Path(__file__).with_name("contact_sheet.py")
        res = subprocess.run(["python3", str(cs), a.clip, "--from", str(r["pick"]["in"]),
                              "--to", str(r["pick"]["out"]), "--frames", "6", "--out", str(out)],
                             capture_output=True, text=True)
        r["window_sheet"] = str(out) if res.returncode == 0 else res.stderr[-400:]
    print(json.dumps(r, indent=2))


if __name__ == "__main__":
    main()
