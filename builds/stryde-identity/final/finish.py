#!/usr/bin/env python3
"""Final finish for the three STRYDE ads: the rough cut from assemble.py (PASS) + the post overlays the build sheet
names (§17: numbers are post overlays, never generated; EG04 offer card). Master audio copied untouched.
Overlays: 17x on MECH-01 · 34% on BR-09 · 200,000+ on BR-21 · offer card (EG04) from BR-22 to the end.
EG04 in the reference also has a URL box — no URL is on file for STRYDE, so it is left out (flagged)."""
import json, subprocess
from pathlib import Path
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
B = Path(__file__).resolve().parent
W, H = 1080, 1920


def t(x):
    h = int(x // 3600); m = int(x % 3600 // 60); s = x % 60
    return f"{h}:{m:02d}:{s:05.2f}"


HEAD = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Big,FreeSans,190,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,9,0,5,40,40,0,1
Style: Sub,FreeSans,70,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,6,0,5,40,40,0,1
Style: Offer,FreeSans,76,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,-1,0,0,100,100,0,0,1,7,0,5,40,40,0,1
Style: Urg,FreeSans,54,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,1,0,1,5,0,5,40,40,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""


def ev(style, a, b, x, y, text):
    return f"Dialogue: 0,{t(a)},{t(b)},{style},,0,0,0,,{{\\pos({x},{y})\\fad(120,120)}}{text}\n"


for hk in ["HK1", "HK2", "HK3"]:
    run = json.loads((B / f"edit/run_{hk}.json").read_text())
    edl = {e["beat"]: e for e in run["edl"]}
    total = run["master_s"]
    s = HEAD
    e = edl["MECH-01"]; s += ev("Big", e["start"] + 0.3, e["end"], W // 2, int(H * 0.30), "17×")
    s += ev("Sub", e["start"] + 0.3, e["end"], W // 2, int(H * 0.30) + 140, "YOUR BODYWEIGHT")
    e = edl["BR-09"]; s += ev("Big", e["start"] + 0.2, e["end"], W // 2, int(H * 0.30), "34%")
    s += ev("Sub", e["start"] + 0.2, e["end"], W // 2, int(H * 0.30) + 140, "LESS STRAIN")
    e = edl["BR-21"]; s += ev("Big", e["start"] + 0.2, e["end"], W // 2, int(H * 0.30), "200,000+")
    s += ev("Sub", e["start"] + 0.2, e["end"], W // 2, int(H * 0.30) + 140, "PEOPLE WEAR ONE")
    a = edl["BR-22"]["start"]
    s += ev("Offer", a, total, W // 2, int(H * 0.68), "• Buy 1 Get 1 Free")
    s += ev("Urg", a, total, W // 2, int(H * 0.68) + 100, "60-DAY MONEY-BACK GUARANTEE")
    ass = B / f"edit/overlays_{hk}.ass"; ass.write_text(s)
    out = B / f"STRYDE_Identity_{hk}_final.mp4"
    subprocess.run([FF, "-y", "-hide_banner", "-loglevel", "error", "-i", str(B / f"edit/rough_{hk}.mp4"),
                    "-vf", f"subtitles='{ass}':fontsdir=/usr/share/fonts/truetype/freefont",
                    "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "24",
                    "-c:a", "copy", "-movflags", "+faststart", str(out)], check=True)
    print(hk, out.name, f"{total:.2f}s")
