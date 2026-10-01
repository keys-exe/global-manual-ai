#!/usr/bin/env python3
"""§40A music beds for down-forwards-again — mix fixes, not regenerations (the composer does not follow per-section loudness reliably).
  body bed  = BODY_A (the patient → the failed fixes; it fades on the turn word "This does.") + BODY_B laid from OFFSET s into it at the turn
              (B out under "Two for one", crossfaded 2 s into BODY_C, the close — B decays to silence ~15 s before the VO ends),
              so B's quiet first seconds sit under A's fade and the new key arrives just after "This does." (§40A: silence on the turn word,
              then the new key). Each section levelled to its energy (low −24, mid −21, high −18 dBFS RMS, 0.6 s ramps); the price
              ("Two for one" → "Nothing to lose") held back 4 dB; B's own fade (from ~73 s of B) held up to the end; a 1.5 s fade after the last word.
  hook beds = HK<n>.mp3 levelled the same way (low → mid), faded over the hand-over.
Writes edit/music/MUS-BODY.wav, MUS-HK<n>.wav and BGM-HK<n>.wav (the variant's whole bed: the hook's cue, then the body from the hook's
last word, the hook's fade running over the body's quiet first second) — 48 kHz stereo — and an mp3 (320k) of each for the board."""
import json, subprocess, pathlib
import numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); SR = 48000
B = pathlib.Path(__file__).parents[1]; D = B / "edit/music"
TARGET = {"low": -26.0, "mid": -22.0, "high": -17.0}
OFFSET = 4.0
def load(p):
    raw = subprocess.run([FF, "-v", "error", "-i", str(p), "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, 2).copy()
def save(a, name):
    p = D / f"{name}.wav"
    subprocess.run([FF, "-y", "-v", "error", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s16le", str(p)], input=a.astype(np.float32).tobytes(), check=True)
    subprocess.run([FF, "-y", "-v", "error", "-i", str(p), "-c:a", "libmp3lame", "-b:a", "320k", str(D / f"{name}.mp3")], check=True)
rms = lambda x: 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-9)
def level(a, secs):
    """gain curve: each section to its target RMS (measured on its audible windows), 0.6 s linear ramps between."""
    n = len(a); g = np.zeros(n)
    for s in secs:
        i, j = int(s["start"] * SR), min(n, int(s["end"] * SR))
        if j <= i or s["energy"] == "silent": continue
        w = a[i:j]; win = [rms(w[k:k + SR // 4]) for k in range(0, len(w) - SR // 4, SR // 4)]
        aud = [x for x in win if x > -45] or win
        g[i:j] = np.clip(TARGET[s["energy"]] - float(np.median(aud)), -12, 12) + s.get("extra", 0)
    k = int(0.6 * SR); g = np.convolve(g, np.ones(k) / k, mode="same")
    return a * (10 ** (g / 20))[:, None]
def fade(a, t0, d):
    i = int(t0 * SR); m = np.ones(len(a)); L = int(d * SR)
    m[i:i + L] = np.linspace(1, 0, min(L, len(a) - i)); m[i + L:] = 0; return a * m[:, None]
def hold_up(a, t0, t1, ref):
    """undo the composer's own fade: from t0 the level is held at the RMS of the 5 s before t0 (capped +24 dB)."""
    w = SR // 4; i0, i1 = int(t0 * SR), min(len(a), int(t1 * SR)); r = rms(a[i0 - 5 * SR:i0]) if ref is None else ref
    out = a.copy()
    for k in range(i0, i1, w):
        out[k:k + w] *= 10 ** (min(24.0, max(0.0, r - rms(a[k:k + w]))) / 20)
    return out
cue = lambda k: json.load(open(D / f"{k}.cue.json"))
# body
A, Bm, C = load(D / "BODY_A.mp3"), load(D / "BODY_B.mp3"), load(D / "BODY_C.mp3")
bc = cue("BODY"); BODY = max(x["end"] for x in bc["sections"] if x["name"] != "Tail")
TURN = [x for x in bc["sections"] if x["name"] == "This does"][0]["start"]
OFFER = [x for x in bc["sections"] if x["name"] == "The offer"][0]["start"]
L = int((BODY + 1.5) * SR); bed = np.zeros((L, 2), np.float32)
a = A[:int((TURN + 2.0) * SR)]; bed[:len(a)] += a
st = int((TURN - OFFSET) * SR); b = fade(Bm, OFFER + 1.0 - (TURN - OFFSET), 1.5)[:max(0, L - st)]; bed[st:st + len(b)] += b    # B out under the price
X = 1.0; c0 = int((OFFER - X) * SR); cc = hold_up(C, 14.0, len(C) / SR, None)
ramp = np.ones(len(cc)); ramp[:int(2 * X * SR)] = np.linspace(0, 1, int(2 * X * SR)); cc = (cc * ramp[:, None])[:L - c0]; bed[c0:c0 + len(cc)] += cc
secs = [dict(x) for x in bc["sections"] if x["name"] != "Tail"]
for x in secs:
    if x["name"] == "This does": x["start"] = round(TURN + 2.0, 2)            # the release is levelled from its arrival, not over the join
    if x["name"] == "The offer": x["extra"] = -6.0
bed = fade(level(bed, secs), BODY, 1.5); save(bed, "MUS-BODY")
print("MUS-BODY", round(len(bed) / SR, 2), "s;", " ".join(f"{x['name']}:{rms(bed[int(x['start']*SR):int(x['end']*SR)]):.1f}" for x in secs))
for h in ["HK1", "HK2", "HK3"]:
    c = cue(h); a = load(D / f"{h}.mp3"); end = [x for x in c["sections"] if x["name"] == "Hand-over"][0]["start"]
    k0 = next(k for k in range(0, len(a), SR // 20) if rms(a[k:k + SR // 20]) > -45)          # the composer's silent lead-in (HK1: ~0.6 s) cut
    a = a[k0:]
    for x in c["sections"]:
        if x["energy"] == "low": x["extra"] = -4.0          # the pulse makes the median read ~3 dB under the section's mean (BGM-HK2/HK3 ENERGY)
    a = fade(level(a, c["sections"]), end, 1.5)[:int((end + 1.5) * SR)]; save(a, f"MUS-{h}")
    v = np.zeros((int(end * SR) + len(bed), 2), np.float32); v[:len(a)] += a; v[int(end * SR):] += bed; save(v, f"BGM-{h}")   # the variant's bed: hook, then the body from the hook's end
    print(f"MUS-{h}", round(len(a) / SR, 2), "s;", " ".join(f"{x['name']}:{rms(a[int(x['start']*SR):int(min(x['end'],end)*SR)]):.1f}" for x in c["sections"] if x["name"] != "Hand-over"))
