"""Trim only the silence before the first word and after the last one — nothing inside the speech is touched.
usage: ends_only.py IN OUT [--floor -50] [--pad 0.08]
Start: 0.08 s before the first 10 ms frame above FLOOR dB. End: 0.25 s after the last frame above FLOOR,
then a 60 ms fade. Prints JSON: in/out durations, cut at head/tail."""
import argparse, json, subprocess
import numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 44100
ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--floor", type=float, default=-50); ap.add_argument("--pad", type=float, default=0.08)
a = ap.parse_args()
x = np.frombuffer(subprocess.run([FF, "-v", "error", "-i", a.src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32)
hop = SR // 100
db = np.array([20 * np.log10(max(np.sqrt(np.mean(x[i:i + hop] ** 2)), 1e-9)) for i in range(0, len(x) - hop, hop)])
on = np.where(db > a.floor)[0]
t0 = max(0.0, on[0] / 100 - a.pad); t1 = min(len(x) / SR, (on[-1] + 1) / 100 + 0.25)
subprocess.run([FF, "-v", "error", "-y", "-i", a.src, "-ss", f"{t0:.3f}", "-to", f"{t1:.3f}",
                "-af", f"afade=t=out:st={max(t1 - t0 - 0.06, 0):.3f}:d=0.06", "-ac", "1", "-ar", str(SR), a.out], check=True)
print(json.dumps({"in_s": round(len(x) / SR, 3), "out_s": round(t1 - t0, 3), "head_cut_s": round(t0, 3),
                  "tail_cut_s": round(len(x) / SR - t1, 3)}))
