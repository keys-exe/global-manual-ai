#!/usr/bin/env python3
"""§24M — mix one film scene's sound: dialogue, one continuous room tone, one music cue, placed SFX.

Usage:
  mix_scene.py SCENE.json [--out SC-03.mix.mp4]

SCENE.json:
  {"scene": "SC-03",
   "picture": "SC-03.cut.mp4",            # the scene's picture-locked cut (whole shots, §24L)
   "dialogue": "SC-03.dialogue.wav",      # the scene's dialogue, isolated (Voice Isolator), aligned to the cut
   "room_tone": "LOC-KITCHEN.tone.mp3",   # the location's looping room tone (§24M) — looped under the whole scene
   "music": "SC-03.music.mp3",            # the scene's one cue, generated at the scene's length (or null)
   "music_in": 0.0,                        # where the cue starts in the scene (s)
   "sfx": [{"id": "SFX-CUP-DOWN", "file": "sfx/SFX-CUP-DOWN.mp3", "at": 3.42, "gain_db": -6}],
   "levels": {"room_tone_db": -30, "music_db": -18, "duck_db": 8}}

Renders the scene with:
  - dialogue at 0 dB;
  - the room tone looped under the full scene at room_tone_db — never restarting at a cut;
  - the music at music_db, ducked by about duck_db whenever dialogue plays (sidechain), faded in/out 0.5s;
  - every SFX at its time and gain;
  - the whole mix normalised to -14 LUFS integrated (phone / social delivery), true peak -1 dB.
Then verifies: duration equals the picture, and prints the integrated loudness.
Picture is copied untouched. Exit 0 = PASS, 2 = FAIL.
"""
import argparse, json, re, subprocess, sys
from pathlib import Path

import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()


def duration(path):
    info = subprocess.run([FF, "-hide_banner", "-i", str(path)], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", info).groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("scene")
    ap.add_argument("--out")
    a = ap.parse_args()
    root = Path(a.scene).parent
    sc = json.loads(Path(a.scene).read_text())
    R = lambda p: str((root / p) if not Path(p).is_absolute() else p)
    lv = {"room_tone_db": -30, "music_db": -18, "duck_db": 8, **sc.get("levels", {})}
    pic = R(sc["picture"])
    T = duration(pic)
    out = a.out or str(root / f"{sc['scene']}.mix.mp4")

    inputs = ["-i", pic, "-i", R(sc["dialogue"]), "-stream_loop", "-1", "-i", R(sc["room_tone"])]
    n = 3
    filt = [f"[1:a]aresample=48000,apad,atrim=0:{T},asplit=2[dlg][key]",
            f"[2:a]aresample=48000,atrim=0:{T},volume={lv['room_tone_db']}dB[tone]"]
    mix = ["[dlg]", "[tone]"]
    if sc.get("music"):
        inputs += ["-i", R(sc["music"])]
        mi = sc.get("music_in", 0.0)
        ms = int(mi * 1000)
        mlen = max(0.0, T - mi)
        filt.append(f"[{n}:a]aresample=48000,atrim=0:{mlen},afade=t=in:d=0.5,afade=t=out:st={max(0, mlen - 0.5)}:d=0.5,"
                    f"volume={lv['music_db']}dB,adelay={ms}|{ms},apad,atrim=0:{T}[mus]")
        # duck the music under the dialogue
        ratio = max(2, int(lv["duck_db"]))
        filt.append(f"[mus][key]sidechaincompress=threshold=0.02:ratio={ratio}:attack=20:release=400[musd]")
        mix.append("[musd]")
        n += 1
    else:
        filt.append("[key]anullsink")
    for i, fx in enumerate(sc.get("sfx", [])):
        inputs += ["-i", R(fx["file"])]
        d = int(fx["at"] * 1000)
        filt.append(f"[{n}:a]aresample=48000,volume={fx.get('gain_db', 0)}dB,adelay={d}|{d},apad,atrim=0:{T}[fx{i}]")
        mix.append(f"[fx{i}]")
        n += 1
    filt.append(f"{''.join(mix)}amix=inputs={len(mix)}:normalize=0,loudnorm=I=-14:TP=-1:LRA=11,atrim=0:{T}[aout]")
    cmd = [FF, "-v", "error", "-y", *inputs, "-filter_complex", ";".join(filt),
           "-map", "0:v", "-map", "[aout]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", out]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode:
        print(json.dumps({"status": "FAIL", "error": r.stderr[-800:]}, indent=2)); sys.exit(2)

    got = duration(out)
    m = subprocess.run([FF, "-hide_banner", "-i", out, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True).stderr
    li = re.findall(r"I:\s+(-?[\d.]+) LUFS", m)
    res = {"status": "PASS" if abs(got - T) < 0.1 else "FAIL", "scene": sc["scene"], "out": out,
           "picture_s": round(T, 3), "mix_s": round(got, 3), "integrated_lufs": float(li[-1]) if li else None}
    print(json.dumps(res, indent=2))
    sys.exit(0 if res["status"] == "PASS" else 2)


if __name__ == "__main__":
    main()
