#!/usr/bin/env python3
"""Talking-head re-cut (user 2026-10-01: "some of the vo he didnt finish what he was saying i need you to fix the trimming").
The old trims (trim.py, base.en word edges, 0.3 s tail cap) ended every part while the last word was still sounding (-42…-58 dB in the
last 150 ms), and TH-HK3's cut from the full take was already inside "question". Here:
  1. part boundaries from th/TH-ALL.wav.cuts.json (medium.en, aligned to the script), each moved to the QUIETEST 20 ms point between the
     last word of one part and the first word of the next;
  2. each part starts 0.12 s before its first voiced frame (> -45 dB) and ends 0.20 s after the last frame above -60 dB — the word's
     whole decay is kept; nothing inside a part is cut (pauses stay as he spoke them);
  3. 10 ms fade-in, 60 ms fade-out, video and audio cut together from the HeyGen take (re-encoded, crf 16).
Writes th/TH-<k>.trim2.mp4 and th/recut_v2.json."""
import json, subprocess, numpy as np, imageio_ffmpeg, pathlib
FF = imageio_ffmpeg.get_ffmpeg_exe(); B = pathlib.Path(__file__).parents[1]
SR = 48000; HOP = int(0.01 * SR); WIN = int(0.02 * SR)
a = np.frombuffer(subprocess.run([FF, "-v", "error", "-i", str(B / "th/TH-ALL.wav"), "-f", "s16le", "-ac", "1", "-ar", str(SR), "-"],
                                 capture_output=True).stdout, np.int16).astype(float) / 32768
n = (len(a) - WIN) // HOP
env = np.array([20 * np.log10(np.sqrt(np.mean(a[i * HOP:i * HOP + WIN] ** 2)) + 1e-9) for i in range(n)])
t_of = lambda i: i * HOP / SR + WIN / 2 / SR
fr = lambda t: max(0, min(n - 1, int(round(t * SR / HOP))))
C = json.load(open(B / "th/TH-ALL.wav.cuts.json")); W = C["words"]; spans = C["cuts"]
ORDER = ["HK1", "HK2", "HK3", "A1", "A2", "A3", "A4", "A5"]
# word index ranges per part: words whose start is inside the old span
idx = {k: [i for i, w in enumerate(W) if spans[k][0] <= w[1] < spans[k][1]] for k in ORDER}
bounds = [0.0]
for k1, k2 in zip(ORDER, ORDER[1:]):
    # search from the last word's (early) end to the END of the next part's first word: the real gap is in there somewhere.
    # The cut goes in the middle of the longest quiet run (< -60 dB); with no quiet run, at the quietest frame.
    e, s = W[idx[k1][-1]][2], W[idx[k2][0]][2]
    i0, i1 = fr(e), fr(s)
    q = env[i0:i1 + 1] < -60
    runs, r0 = [], None
    for m, v in enumerate(list(q) + [False]):
        if v and r0 is None: r0 = m
        if not v and r0 is not None: runs.append((m - r0, r0, m)); r0 = None
    j = i0 + ((max(runs)[1] + max(runs)[2]) // 2 if runs else int(np.argmin(env[i0:i1 + 1])))
    bounds.append(round(t_of(j), 3))
bounds.append(len(a) / SR)
rep = {}
for j, k in enumerate(ORDER):
    s0, e0 = bounds[j], bounds[j + 1]
    i0, i1 = fr(s0), fr(e0)
    voiced = np.where(env[i0:i1] > -45)[0]; tail = np.where(env[i0:i1] > -60)[0]
    st = max(s0, t_of(i0 + voiced[0]) - 0.12)
    en = min(e0, t_of(i0 + tail[-1]) + 0.20)
    d = en - st
    out = B / f"th/TH-{k}.trim2.mp4"
    subprocess.run([FF, "-v", "error", "-y", "-ss", f"{st:.3f}", "-i", str(B / "th/TH-ALL.f3fed911.mp4"), "-t", f"{d:.3f}",
                    "-af", f"afade=t=in:d=0.01,afade=t=out:st={d - 0.06:.3f}:d=0.06", "-c:v", "libx264", "-crf", "16", "-preset", "medium",
                    "-c:a", "aac", "-b:a", "256k", "-ar", "48000", str(out)], check=True)
    rep[k] = {"start": round(float(st), 3), "end": round(float(en), 3), "dur": round(float(d), 3), "boundary_in": round(s0, 3), "boundary_out": round(e0, 3),
              "end_level_db_before_fade": round(float(env[fr(en) - 5:fr(en)].max()), 1),
              "first_word": W[idx[k][0]][0], "last_word": W[idx[k][-1]][0], "last_word_end": W[idx[k][-1]][2]}
json.dump(rep, open(B / "th/recut_v2.json", "w"), indent=1)
for k, r in rep.items(): print(k, r)
