"""§24M SC03 re-score mix (2026-10-03 Fix). Per take: room tone under everything, each sound on its frame (times read off
the clip frame by frame), MUS-SC03 v1 as a quiet bed under the sounds (its own 0-5 / 5-13 / 13-22 s sections), -16 LUFS.
Picture stream-copied from the take's current version — never re-encoded, never trimmed (§24L).
usage: mix_sc03.py <dir with T1_v2.mp4 T2_v2.mp4 T3_v2.mp4 MUS_v1.mp4> <out dir> [--round 2]
Round 2 (2026-10-03, board Fixes): T1 "remove the last sound" → the exhale out, the rest kept; T2 "remove all the sound make it like his natural
foot sound" → footsteps only (three natural carpet-step sounds, varied), no tone, rail, breath or music, at a natural -22 LUFS."""
import subprocess, sys, numpy as np
from pathlib import Path
SR = 48000
H = Path(__file__).parent / "sc03"
src, out = Path(sys.argv[1]), Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
RND = sys.argv[sys.argv.index("--round") + 1] if "--round" in sys.argv else "1"
ROUND2 = RND in ("2", "3", "4")

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
def stretch(x, r):                 # slower without a pitch change (ffmpeg atempo), r < 1 = longer
    return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-af", f"atempo={r}",
                         "-f", "f32le", "-"], input=x.tobytes(), capture_output=True, check=True).stdout, np.float32).copy()
def loop(x, n):
    return np.tile(x, n // len(x) + 1)[:n]

S = {k: load(H / f"{k}_v1.mp3") for k in ["TONE-BEDROOM", "SFX-SLEEVES-RUMMAGE", "SFX-DRAWER-SHUT", "SFX-EXHALE-TONY", "TONE-HALL",
     "SFX-STAIR-STEP", "SFX-STEP-NAT-A", "SFX-STEP-NAT-B", "SFX-STEP-NAT-C", "SFX-STRAIN-TONY", "SFX-SHUFFLE-STAIR", "TONE-CAR-QUIET", "SFX-SEAT-SETTLE", "SFX-SIGH-NOSE-TONY", "SFX-BREATH-IN-DEEP", "SFX-BREATH-OUT-LONG", "SFX-BREATH-SOFT", "SFX-HANDRAIL-GRIP", "SFX-BREATH-STRAIN", "TONE-CAR-INT", "SFX-BAGS-BOOT", "SFX-BOOT-SLAM"]}
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
if ROUND2:
    TAKES = {
     "T1": {"tone": "TONE-BEDROOM", "mus": (0.0, 5.04), "lufs": -16, "ver": 4, "hits": [h for h in TAKES["T1"]["hits"] if h[0] != "SFX-EXHALE-TONY"]},
     "T2": {"tone": None, "mus": None, "lufs": -22, "ver": 4, "hits": [  # (B's thud is 0.15 s into its file)
         (k, t - (0.15 if k.endswith("B") else 0.0), g, r) for k, t, g, r in [
         ("SFX-STEP-NAT-A", 0.80, -25, 1.0), ("SFX-STEP-NAT-C", 1.90, -26, 1.0), ("SFX-STEP-NAT-B", 2.80, -25, 1.0),
         ("SFX-STEP-NAT-A", 3.85, -23, 0.97), ("SFX-STEP-NAT-C", 4.35, -24, 1.02), ("SFX-STEP-NAT-B", 5.00, -23, 0.98),
         ("SFX-STEP-NAT-A", 5.80, -24, 1.03), ("SFX-STEP-NAT-C", 6.50, -23, 0.97), ("SFX-STEP-NAT-B", 7.30, -24, 1.0)]]},
    }
if RND == "3":
    # Round 3 (2026-10-03, board Fixes): every sound timed off the picture by measurement, not by eye at 2 fps.
    # T1 "add a sound based on his face and make sure it match": his face strains from 3.1 s (brow knotted, eyes squeezed), hardest
    #   3.4-3.6 s, lips closed -> a closed-mouth grunt of effort through the nose over the strain, ending before the drawer's thud at 3.75 s.
    # T2 "the sound did not match and make it match of his foot": boot landings from frame-difference motion in the boot area
    #   (shot 1 stabilised against the stairs): 0.29, 1.42 s; a weight shift without a lift at 2.05 s; cut at 3.54 s; 4.52, 5.52 (the back foot),
    #   6.76 s; nothing moves after 7.0 s.
    # T3 "add a sound" (v4 picture, alone in the car): a quiet cabin, a seat creak on his settle at 0.85 s, one slow breath out through the
    #   nose as his eyes drop at 3.25 s (back up by 4.75 s).
    TAKES = {
     "T1": {"tone": "TONE-BEDROOM", "mus": (0.0, 5.04), "lufs": -16, "ver": 5, "hits": TAKES["T1"]["hits"] + [("SFX-STRAIN-TONY", 3.12, -24, 0.9)]},
     "T2": {"tone": None, "mus": None, "lufs": -22, "ver": 5, "hits": [
         (k, t - (0.15 if k.endswith("B") else 0.05 if k == "SFX-SHUFFLE-STAIR" else 0.0), g, r) for k, t, g, r in [
         ("SFX-STEP-NAT-A", 0.29, -24, 1.0), ("SFX-STEP-NAT-C", 1.42, -24, 1.0), ("SFX-SHUFFLE-STAIR", 2.05, -30, 1.0),
         ("SFX-STEP-NAT-A", 4.52, -23, 1.03), ("SFX-STEP-NAT-C", 5.52, -27, 1.03), ("SFX-STEP-NAT-A", 6.76, -23, 0.97)]]},
     "T3": {"clip": "T3_v4.mp4", "tone": "TONE-CAR-QUIET", "tone_db": -38, "mus": None, "lufs": -24, "ver": 5, "hits": [
         ("SFX-SEAT-SETTLE", 0.85, -32, 1.0), ("SFX-SIGH-NOSE-TONY", 3.25, -28, 1.0)]},
    }
if RND == "4":
    # Round 4 (2026-10-03, board Fix on T3): "change the sound make it like his deep breath and make sure it match the sound".
    # His breathing read off the picture: the chest band tracked frame to frame (sub-pixel), the head subtracted, the push-in's
    # drift detrended — chest rises 0.25-1.65 s (deep breath in), falls slowly 1.8-5.0 s (long breath out, through his eyes dropping),
    # a small shallow breath 5.0-7.0 s, rises again 7.2-8.8 s (deep breath in). Each breath stretched (atempo, pitch kept) to its window.
    # The sigh and seat creak of v5 out; the quiet cabin kept very low under the breaths.
    TAKES = {"T3": {"clip": "T3_v4.mp4", "tone": "TONE-CAR-QUIET", "tone_db": -46, "mus": None, "lufs": -26, "ver": 6, "hits": [
        ("SFX-BREATH-IN-DEEP", 0.28, -26, ("st", 0.85)), ("SFX-BREATH-OUT-LONG", 1.80, -28, ("st", 0.80)),
        ("SFX-BREATH-SOFT", 5.10, -33, ("st", 0.80)), ("SFX-BREATH-IN-DEEP", 7.25, -25, ("st", 0.70))]}}
for take, p in TAKES.items():
    clip = src / p.get("clip", f"{take}_v2.mp4")
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(clip)], capture_output=True, text=True).stdout)
    n = int(dur * SR); mix = np.zeros(n, np.float32)
    if p.get("tone"): mix += fade(at(loop(S[p["tone"]], n), p.get("tone_db", -42)), 0.3, 0.3)
    if p.get("mus"):
        a, b = p["mus"]; m = MUS[int(a * SR):int(a * SR) + n]; m = np.pad(m, (0, n - len(m)))
        mix += fade(at(m, -34), 0.05, 0.4)
    for k, t, g, r in p["hits"]:
        src_x = stretch(S[k], r[1]) if isinstance(r, tuple) else (rate(S[k], r) if r != 1.0 else S[k].copy())
        x = fade(at(src_x, g)); i = max(0, int(t * SR)); x = x[:max(0, n - i)]
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
    T = p.get("lufs", -16); g = T - lufs(mix)
    for _ in range(6):
        y = limit(mix, g); d = T - lufs(y)
        if abs(d) < 0.3: break
        g += d
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-ac", "2", str(wav)],
                   input=y.tobytes(), check=True)
    mp4 = out / f"SC03-{take}_v{p.get('ver', 3)}.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(clip), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(mp4)], check=True)
    print(take, f"{dur:.2f}s ->", mp4.name)
