#!/usr/bin/env python3
"""Level a music bed to one steady loudness (user: "ONE investigations style BGM" — one consistent bed, not a swell).
Smooth 3 s RMS envelope → gain toward TARGET dBFS (boost capped at +MAXUP dB, cut at -MAXDOWN), gain smoothed so it never
pumps. Usage: level_bed.py in.mp3 out.wav [--skip 0.2] [--target -24]"""
import argparse, subprocess, numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 44100
ap = argparse.ArgumentParser(); ap.add_argument("src"); ap.add_argument("out")
ap.add_argument("--skip", type=float, default=0.0); ap.add_argument("--target", type=float, default=-24.0)
ap.add_argument("--maxup", type=float, default=14.0); ap.add_argument("--maxdown", type=float, default=8.0)
a = ap.parse_args()
raw = subprocess.run([FF, "-v", "error", "-ss", str(a.skip), "-i", a.src, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
x = np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
m = x.mean(1); hop = SR // 10
e = np.array([np.sqrt((m[i:i + hop] ** 2).mean()) for i in range(0, len(m), hop)])
k = np.ones(30) / 30                                     # 3 s smoothing
env = np.sqrt(np.convolve(e ** 2, k, mode="same")) + 1e-9
g_db = np.clip(a.target - 20 * np.log10(env), -a.maxdown, a.maxup)
g_db = np.convolve(np.pad(g_db, 10, mode="edge"), np.ones(21) / 21, mode="valid")   # 2 s gain smoothing, no pumping
g = 10 ** (np.interp(np.arange(len(m)), np.arange(len(g_db)) * hop, g_db) / 20)
y = np.clip(x * g[:, None], -1, 1)
subprocess.run([FF, "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", a.out], input=y.astype(np.float32).tobytes(), check=True)
print("gain dB min/max:", round(float(g_db.min()), 1), round(float(g_db.max()), 1))
