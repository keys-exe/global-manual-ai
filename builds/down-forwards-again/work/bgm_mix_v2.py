#!/usr/bin/env python3
"""Music v2 beds (work/music_v2.py; user 2026-10-01 "investigation … change when the product shows, not sad"). One bed per hook variant:
  the hook's investigation cue → (crossfade 0.6 s) BODY_A, the investigation groove, from where the hook cue starts to fade (HK1 and HK3's cues
  fade ~2 s before their hook ends, so the groove carries on with no dip) → BODY_B, the bright major-key lift, starting exactly on the turn word
  "This does." (the product's first appearance, PR-12), steady to the end → 1.5 s fade after the last word.
Levels: the investigation at −21 dBFS RMS, the lift a step up at −17 (music sits ~18 dB under the voice in finish.py, ducked while he speaks).
Writes edit/music/v2/BGM-HK<n>.wav (+ .mp3) and MUS-BODY.wav (the body bed alone, for the board)."""
import json, subprocess, pathlib
import numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 48000
B = pathlib.Path(__file__).parents[1]; D = B / "edit/music/v2"
HOOK = {"HK1": 12.2, "HK2": 8.64, "HK3": 7.64}; BODY = 148.27; TURN = 67.07
def load(p):
    raw = subprocess.run([FF, "-v", "error", "-i", str(p), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def save(a, name):
    p = D / f"{name}.wav"
    subprocess.run([FF, "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", str(p)], input=a.astype(np.float32).tobytes(), check=True)
    subprocess.run([FF, "-y", "-v", "error", "-i", str(p), "-c:a", "libmp3lame", "-b:a", "320k", str(D / f"{name}.mp3")], check=True)
rms = lambda x: 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9)
def level_to(a, target):
    w = SR // 2; v = [rms(a[k:k + w]) for k in range(0, len(a) - w, w)]; v = [x for x in v if x > -40]
    return a * 10 ** ((target - float(np.median(v))) / 20)
def fade_point(a):
    """the time the cue's own fade-out begins: the last half-second still within 8 dB of the cue's median level."""
    w = SR // 2; v = [rms(a[k:k + w]) for k in range(0, len(a) - w, w)]; med = float(np.median([x for x in v if x > -40]))
    last = max(i for i, x in enumerate(v) if x > med - 8); return (last + 1) * 0.5
def env(n, fin=0.0, fout=0.0):
    e = np.ones(n); i, o = int(fin * SR), int(fout * SR)
    if i: e[:i] = np.linspace(0, 1, i)
    if o: e[-o:] = np.linspace(1, 0, o)
    return e[:, None]
A = level_to(load(D / "BODY_A.mp3"), -21.0); Bm = level_to(load(D / "BODY_B.mp3"), -17.0)
XF = 0.6
body = np.zeros((int((BODY + 1.5) * SR), 2), np.float32)
a = A[:int((TURN + 0.3) * SR)]; body[:len(a)] += a * env(len(a), fout=0.3)          # the investigation groove (missing in the first MUS-BODY card)
b = Bm[:len(body) - int(TURN * SR)]; b = b * env(len(b), fin=0.05); body[int(TURN * SR):int(TURN * SR) + len(b)] += b
save(body * env(len(body), fout=1.5), "MUS-BODY")
for h, L in HOOK.items():
    hc = level_to(load(D / f"{h}.mp3"), -21.0); F = min(L, fade_point(hc) - 0.3)
    n = int((L + BODY + 1.5) * SR); bed = np.zeros((n, 2), np.float32)
    a0 = hc[:int((F + XF) * SR)]; bed[:len(a0)] += a0 * env(len(a0), fout=XF)
    a_end = L + TURN + 0.3                                   # the investigation runs up to the turn word
    need = a_end - F; assert fade_point(A) - 0.3 >= need, (h, need, fade_point(A))   # BODY_A is composed long enough (TURN + 12 s)
    seg = A[:int(need * SR)]; seg = seg * env(len(seg), fin=XF, fout=0.3); bed[int(F * SR):int(F * SR) + len(seg)] += seg
    tb = int((L + TURN) * SR); bb = Bm[:n - tb] * env(n - tb, fin=0.05); bed[tb:tb + len(bb)] += bb
    bed = bed * env(n, fout=1.5); save(bed, f"BGM-{h}")
    print(h, "hook cue until", round(F, 2), "s; investigation", round(F, 2), "→", round(a_end, 2), "; lift from", round(L + TURN, 2))
