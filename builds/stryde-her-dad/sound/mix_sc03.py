"""§24M SC03 re-score mix (2026-10-03 Fix). Per take: room tone under everything, each sound on its frame (times read off
the clip frame by frame), MUS-SC03 v1 as a quiet bed under the sounds (its own 0-5 / 5-13 / 13-22 s sections), -16 LUFS.
Picture stream-copied from the take's current version — never re-encoded, never trimmed (§24L).
usage: mix_sc03.py <dir with T1_v2.mp4 T2_v2.mp4 T3_v2.mp4 MUS_v1.mp4> <out dir>"""
import subprocess, sys, numpy as np
from pathlib import Path
SR = 48000
H = Path(__file__).parent / "sc03"
src, out = Path(sys.argv[1]), Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)

def load(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).copy()
def rms_db(x):
    return 20 * np.log10(np.sqrt(np.mean(x[np.abs(x) > 1e-4] ** 2)) + 1e-9)
def at(x, db):                     # set a stem to a target RMS (its loud part)
    return x * 10 ** ((db - rms_db(x)) / 20)
def fade(x, i=0.02, o=0.15):
    n = len(x); a, b = int(i * SR), int(o * SR)
    if a: x[:a] *= np.linspace(0, 1, a)
    if b and b < n: x[-b:] *= np.linspace(1, 0, b)
    return x
def rate(x, r):                    # small speed change so repeated steps don't sound identical
    idx = np.arange(0, len(x) - 1, r); return np.interp(idx, np.arange(len(x)), x).astype(np.float32)
def loop(x, n):
    return np.tile(x, n // len(x) + 1)[:n]

S = {k: load(H / f"{k}_v1.mp3") for k in ["TONE-BEDROOM", "SFX-SLEEVES-RUMMAGE", "SFX-DRAWER-SHUT", "SFX-EXHALE-TONY", "TONE-HALL",
     "SFX-STAIR-STEP", "SFX-HANDRAIL-GRIP", "SFX-BREATH-STRAIN", "TONE-CAR-INT", "SFX-BAGS-BOOT", "SFX-BOOT-SLAM"]}
MUS = load(src / "MUS_v1.mp4")

# (sound, start s, level dB RMS, rate)  — levels: tone -42, bed -34, sounds -18 to -28
TAKES = {
 "T1": {"tone": "TONE-BEDROOM", "mus": (0.0, 5.04), "hits": [
     ("SFX-SLEEVES-RUMMAGE", 0.00, -26, 1.0),
     ("SFX-DRAWER-SHUT",     3.01, -19, 1.0),   # the thud (0.74 s into the sound) lands at 3.75 s, the drawer stopping
     ("SFX-EXHALE-TONY",     3.95, -27, 1.0)]},
 "T2": {"tone": "TONE-HALL", "mus": (5.0, 13.04), "hits": [
     ("SFX-BREATH-STRAIN",   0.00, -30, 1.0),
     ("SFX-HANDRAIL-GRIP",   0.05, -27, 1.0),   # crouched, both hands on the rail
     ("SFX-HANDRAIL-GRIP",   3.40, -28, 0.97),  # from below: the hand sliding down the rail
     ] + [("SFX-STAIR-STEP", t, g, r) for t, g, r in [(0.80, -24, 1.0), (1.90, -25, 0.97), (2.80, -24, 1.03),
           (3.85, -22, 1.0), (4.35, -23, 0.96), (5.00, -22, 1.02), (5.80, -23, 0.98), (6.50, -22, 1.0), (7.30, -23, 1.03)]]},
 "T3": {"tone": "TONE-CAR-INT", "mus": (13.0, 22.04), "hits": [
     ("SFX-BAGS-BOOT",       0.00, -27, 1.0),
     ("SFX-BOOT-SLAM",       6.35, -19, 1.0)]},
}
for take, p in TAKES.items():
    clip = src / f"{take}_v2.mp4"
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(clip)], capture_output=True, text=True).stdout)
    n = int(dur * SR); mix = np.zeros(n, np.float32)
    mix += fade(at(loop(S[p["tone"]], n), -42), 0.3, 0.3)
    a, b = p["mus"]; m = MUS[int(a * SR):int(a * SR) + n]; m = np.pad(m, (0, n - len(m)))
    mix += fade(at(m, -34), 0.05, 0.4)
    for k, t, g, r in p["hits"]:
        x = fade(at(rate(S[k], r) if r != 1.0 else S[k].copy(), g)); i = int(t * SR); x = x[:max(0, n - i)]
        if len(x) > int(0.3 * SR): x = fade(x, 0.0, 0.25)
        mix[i:i + len(x)] += x
    wav = out / f"SC03-{take}.mix.wav"
    # measured gain to -16 LUFS integrated under a -1.5 dB peak limiter, re-measured until within 0.3 LU
    # (one-pass loudnorm undershoots on 5-9 s clips; the limiter takes back loudness on the hits)
    def lufs(x):
        e = subprocess.run(["ffmpeg", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", "ebur128", "-f", "null", "-"],
                           input=x.tobytes(), capture_output=True).stderr.decode()
        return float(e.split("Integrated loudness:")[1].split("I:")[1].split("LUFS")[0])
    def limit(x, g):
        return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af",
            f"volume={g:.2f}dB,alimiter=limit=0.84:attack=2:release=60:level=disabled", "-f", "f32le", "-"],
            input=x.tobytes(), capture_output=True, check=True).stdout, np.float32)
    g = -16 - lufs(mix)
    for _ in range(6):
        y = limit(mix, g); d = -16 - lufs(y)
        if abs(d) < 0.3: break
        g += d
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-ac", "2", str(wav)],
                   input=y.tobytes(), check=True)
    mp4 = out / f"SC03-{take}_v3.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(clip), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(mp4)], check=True)
    print(take, f"{dur:.2f}s ->", mp4.name)
