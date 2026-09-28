#!/usr/bin/env python3
"""Six Weeks Ago — replace the BGM on a finished hook variant (§24M, mix rules of mix_scene.py).

Usage:
  mix_film.py HK1|HK2|HK3 [--no-mux]

Builds one continuous timeline for the variant:
  dialogue  = the variant's own isolated hook (ElevenLabs Voice Isolator) up to its seam
              + the shared body dialogue, isolated from HK1, from HK1's seam on (identical body in all variants)
  music     = the hook's cue from 0, then one cue per body scene starting on its scene cut
              (lead-in silence trimmed so the cue sounds on the cut; outgoing cue faded 0.8s after the cut),
              every cue levelled to one loudness (+ its "scene_gain_db"), then section gain automation
              from each section's "mix_gain_db" (ramps 0.5s),
              music at -18 dB under dialogue (loudness), ducked a further 8 dB while anyone speaks
  ambience  = one looping room tone per location and the film's SFX list on their frames (sound_plan.json,
              files in fx/ made by fx.py), when the plan exists
Then normalises to -14 LUFS / -1 dBTP and muxes onto the untouched picture (video stream copied).
"""
import json, subprocess, sys
from pathlib import Path

import imageio_ffmpeg
import numpy as np

FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 44100
HERE = Path(__file__).parent
WORK = HERE.parent / "work"
INTAKE = HERE.parent / "intake"
OUT = HERE.parent / "out"

HK1_SEAM = 17.5333                                  # first frame of the shared body in HK1
SEAM = {"HK1": 17.5333, "HK2": 15.4667, "HK3": 14.9}  # the same frame in each variant
BODY = ["SC01-KITCHEN-SARAH", "SC02-NIGHT-FRANK", "SC03-WEDDING", "SC04-BARBARA-KITCHEN", "SC05-STAIRS-BARBARA",
        "SC06-DOCTOR", "SC07-HALLWAY-FRANK", "SC08-STAIRS-SARAH", "SC09-THE-DANCE", "SC10-CALL-JOAN"]
MUSIC_UNDER_DB, DUCK_DB = -18.0, 8.0
CUE_REF_DB = -20.0                                   # each cue's audible level before section gains
ROOM_UNDER_DB, SFX_UNDER_DB = -30.0, -10.0           # §24M: room tone ~30 dB under dialogue, effects near natural


def load(path, ch):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ac", str(ch), "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32).reshape(-1, ch).copy()


def duration(path):
    import re
    info = subprocess.run([FF, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", info).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def rms_db(x):
    return 20 * np.log10(max(float(np.sqrt(np.mean(x ** 2))), 1e-9))


def active_level(x, win=0.4):
    """Loudness of the audible parts only (windows within 25 dB of the loudest)."""
    w = int(win * SR)
    e = np.array([rms_db(x[k:k + w]) for k in range(0, len(x) - w, w)])
    return float(np.mean(e[e > e.max() - 25]))


def lead_in(y, thresh_db=-50):
    w = int(0.01 * SR)
    for k in range(0, len(y) - w, w):
        if rms_db(y[k:k + w]) > thresh_db:
            return max(0, k - int(0.05 * SR))
    return 0


def ramp_env(n, points):
    """points: [(t, gain_db)] → linear gain per sample, linear interpolation in dB."""
    t = np.arange(n) / SR
    ts, gs = zip(*points)
    return (10 ** (np.interp(t, ts, gs) / 20)).astype(np.float32)


def cue_track(name, dest_len, at):
    cue = json.loads((HERE / f"{name}.cue.json").read_text())
    y = load(HERE / f"{name}.v1.mp3", 2)
    y = y[lead_in(y.mean(1)):]
    y *= 10 ** ((CUE_REF_DB + cue.get("scene_gain_db", 0.0) - active_level(y.mean(1))) / 20)  # every cue at one level
    # section gain automation
    pts = [(0.0, 0.0)]
    for s in cue["sections"]:
        g = s.get("mix_gain_db", 0.0)
        pts += [(s["start"], pts[-1][1]), (s["start"] + 0.5, g)]
    env = ramp_env(len(y), pts)
    y = y * env[:, None]
    out = np.zeros((dest_len, 2), np.float32)
    a = int(round(at * SR))
    n = min(len(y), dest_len - a)
    out[a:a + n] = y[:n]
    return out, cue


def ambience(hk, N, shift, d_lvl):
    """Room tone per location and SFX on their frames, from sound_plan.json (§24M).

    Room tone: the hook's location from 0 to the seam, then each body scene's location from its cut —
    looped (0.5s crossfade at the loop point), changed only at a cut (0.3s crossfade), a location
    reused across scenes is the same file. Level: ROOM_UNDER_DB under the dialogue.
    SFX: body events are in HK1 time (moved by the variant's shift); hook events carry "in": "HK<n>"
    and play only in that variant, in its own time. Level: SFX_UNDER_DB under the dialogue + gain_db.
    """
    plan = json.loads((HERE / "sound_plan.json").read_text())
    out = np.zeros((N, 2), np.float32)

    segs = [(0.0, plan["hook_tone"][hk])]
    for name in BODY:
        cue = json.loads((HERE / f"{name}.cue.json").read_text())
        segs.append((cue["timeline_at_HK1_s"] - shift, plan["scene_tone"][name]))
    cache = {}
    for i, (a, loc) in enumerate(segs):
        b = segs[i + 1][0] if i + 1 < len(segs) else N / SR
        if loc is None:
            continue
        if loc not in cache:
            y = load(HERE / "fx" / f"{loc}.mp3", 2)
            y *= 10 ** ((d_lvl + ROOM_UNDER_DB + plan["tones"][loc].get("gain_db", 0.0) - active_level(y.mean(1))) / 20)
            cache[loc] = y
        y = cache[loc]
        xf = int(0.5 * SR)
        need = int((b - a + 0.6) * SR)
        loop = y.copy()
        while len(loop) < need:                      # loop with a 0.5s crossfade at each join
            f = np.linspace(0, 1, xf, dtype=np.float32)[:, None]
            loop = np.concatenate([loop[:-xf], loop[-xf:] * (1 - f) + y[:xf] * f, y[xf:]])
        s0, s1 = int(a * SR), min(N, int((b + 0.3) * SR))
        seg = loop[:s1 - s0].copy()
        ramp = int(0.3 * SR)
        if i > 0:
            seg[:ramp] *= np.linspace(0, 1, ramp, dtype=np.float32)[:, None]
        if s1 < N:
            seg[-ramp:] *= np.linspace(1, 0, ramp, dtype=np.float32)[:, None]
        out[s0:s1] += seg

    fx = {}
    for ev in plan["events"]:
        if "in" in ev and ev["in"] != hk:
            continue
        at = ev["at"] if "in" in ev else ev["at"] - shift
        if at < 0 or ("in" not in ev and at < SEAM[hk] - 0.05):
            continue
        if ev["id"] not in fx:
            y = load(HERE / "fx" / f"{ev['id']}.mp3", 2)
            fx[ev["id"]] = y * 10 ** ((d_lvl + SFX_UNDER_DB - active_level(y.mean(1))) / 20)
        y = fx[ev["id"]] * 10 ** (ev.get("gain_db", 0.0) / 20)
        a = int(at * SR)
        n = min(len(y), N - a)
        out[a:a + n] += y[:n]
    return out


def main():
    hk = sys.argv[1]
    mux = "--no-mux" not in sys.argv
    video = INTAKE / f"{hk}.mp4"
    total = duration(video)
    N = int(round(total * SR))
    seam = SEAM[hk]
    shift = HK1_SEAM - seam                          # HK1 time = variant time + shift (body)

    # dialogue
    body = load(WORK / "HK1.full.iso.mp3", 1)[:, 0]
    hook = body if hk == "HK1" else load(WORK / f"{hk}.hook.iso.mp3", 1)[:, 0]
    dia = np.zeros(N, np.float32)
    s = int(round(seam * SR))
    dia[:s] = hook[:s]
    b0 = int(round(HK1_SEAM * SR))
    seg = body[b0:b0 + (N - s)]
    dia[s:s + len(seg)] = seg
    x = int(0.01 * SR)                               # 10 ms crossfade at the seam
    if hk != "HK1":
        fade = np.linspace(0, 1, 2 * x, dtype=np.float32)
        dia[s - x:s + x] = hook[s - x:s + x] * (1 - fade) + body[b0 - x:b0 + x] * fade

    # music: one cue per scene, each starting on its cut
    starts = [(f"HOOK{hk[-1]}", 0.0)]
    for name in BODY:
        cue = json.loads((HERE / f"{name}.cue.json").read_text())
        starts.append((name, cue["timeline_at_HK1_s"] - shift))
    mus = np.zeros((N, 2), np.float32)
    for i, (name, at) in enumerate(starts):
        tr, _ = cue_track(name, N, at)
        if i + 1 < len(starts):                      # the outgoing cue gives way 0.8s after the next cut
            nxt = starts[i + 1][1]
            fo = ramp_env(N, [(0, 0), (nxt, 0), (nxt + 0.8, -60)])
            fo[int((nxt + 0.8) * SR):] = 0
            tr *= fo[:, None]
        if i > 0:                                    # 30 ms fade-in on the cut
            a = int(at * SR)
            tr[a:a + int(0.03 * SR)] *= np.linspace(0, 1, int(0.03 * SR), dtype=np.float32)[:, None]
        mus += tr

    d_lvl = active_level(dia)
    amb = ambience(hk, N, shift, d_lvl) if (HERE / "sound_plan.json").exists() else np.zeros((N, 2), np.float32)

    # levels: music -18 dB under the dialogue, ducked 8 dB under speech
    m_lvl = active_level(mus.mean(1))
    mus *= 10 ** ((d_lvl + MUSIC_UNDER_DB - m_lvl) / 20)
    w = int(0.02 * SR)
    frames = np.array([rms_db(dia[k:k + w]) for k in range(0, N, w)])
    speech = (frames > d_lvl - 20).astype(float)
    # hold 300 ms after speech, attack 60 ms, release 400 ms
    hold = int(0.3 / 0.02)
    held = np.array([speech[max(0, k - hold):k + 1].max() for k in range(len(speech))])
    g = np.zeros_like(held)
    for k in range(len(held)):
        prev = g[k - 1] if k else 0.0
        coef = 0.02 / 0.06 if held[k] > prev else 0.02 / 0.4
        g[k] = prev + (held[k] - prev) * min(1.0, coef)
    duck = 10 ** (-DUCK_DB * np.repeat(g, w)[:N] / 20)
    mus *= duck[:, None].astype(np.float32)

    mix = mus + amb + dia[:, None]
    OUT.mkdir(exist_ok=True)
    raw = OUT / f"{hk}.mix.raw.wav"
    import wave
    pcm = (np.clip(mix, -1, 1) * 32767).astype(np.int16)
    with wave.open(str(raw), "wb") as f:
        f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR); f.writeframes(pcm.tobytes())
    # two-pass loudnorm to -14 LUFS, -1 dBTP
    m = subprocess.run([FF, "-hide_banner", "-i", str(raw), "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    j = json.loads(m[m.rindex("{"):m.rindex("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    wav = OUT / f"{hk}.mix.wav"
    subprocess.run([FF, "-v", "error", "-y", "-i", str(raw), "-af", af, "-ar", str(SR), str(wav)], check=True)
    raw.unlink()
    res = {"variant": hk, "picture_s": round(total, 3), "mix_s": round(duration(wav), 3),
           "dialogue_level_db": round(d_lvl, 1), "music_gain_db": round(d_lvl + MUSIC_UNDER_DB - m_lvl, 1),
           "cues": [[n, round(a, 3)] for n, a in starts]}
    if mux:
        mp4 = OUT / f"Six Weeks Ago {hk} - new music + room tone + sfx.mp4"
        subprocess.run([FF, "-v", "error", "-y", "-i", str(video), "-i", str(wav), "-map", "0:v:0", "-map", "1:a:0",
                        "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart",
                        str(mp4)], check=True)
        res["video"] = str(mp4)
        res["video_s"] = round(duration(mp4), 3)
    print(json.dumps(res, indent=2))


if __name__ == "__main__":
    main()
