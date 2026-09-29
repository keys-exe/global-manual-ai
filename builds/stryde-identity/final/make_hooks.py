#!/usr/bin/env python3
"""Final hooks (EG01 split 50/50, VO line as caption on the split — VN01–VN03).
Top/bottom = the clips the user confirmed on the board; audio = the locked VO master, 0 → 'Because'."""
import json, subprocess, sys
from pathlib import Path
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
B = Path(__file__).resolve().parent.parent
VO = Path(sys.argv[1])            # folder holding the VO master files <asset>.mp4
MDIR = "master2" if "--master2" in sys.argv else "master"   # master2 = the slower VO cut (user, 2026-09-28)
AUDIO = lambda hk: B / f"vo/master2/Identity-Narrator_master2_{hk}.mp3" if MDIR == "master2" else VO / f"{MASTERS[hk]}.mp4"
CLEAN = "--clean" in sys.argv     # no caption: finish.py burns the hook caption (ad style, 2026-09-28)
MASTERS = {"HK1": "b8db26a0d46e7635e8ef63afc04dff92", "HK2": "fa5e2defd2333a6e04b2c49559892b72", "HK3": "f67ee06f7b67c8bd10a8f5aa5a666ebb"}
CLIPS = {  # board picks; tops = sd5 (2026-09-29 redo, one hand, real inside)
    "HK1": ("HK1-T_video_sd5.mp4", "HK1-B_video_v2.mp4"),
    "HK2": ("HK2-T_video_sd5.mp4", "HK2-B_video_sd2.mp4"),
    "HK3": ("HK3-T_video_sd5.mp4", "HK3-B_video_sd1.mp4"),
}
SKIP = 0.4   # §30H: the start image's static opening
W, H = 1080, 1920

def ass(text, dur, path):
    t = f"0:00:{dur:05.2f}"
    path.write_text(f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,FreeSans,62,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,1,6,0,5,70,70,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
Dialogue: 0,0:00:00.00,{t},Cap,,0,0,0,,{{\\pos({W//2},{H//2})}}{text}
""")

for hk, (top, bot) in CLIPS.items():
    words = json.loads((B / f"vo/{MDIR}/{hk}.words.json").read_text())
    dur = next(w["s"] for w in words if w["w"].startswith("Because")) - 0.02
    line = (B / f"vo/{hk}.lines.txt").read_text().strip().strip('"')
    a = B / f"final/{hk}.ass"; ass(line, dur, a)
    out = B / f"final/{hk}_{'hook_clean' if CLEAN else 'final_hook'}.mp4"
    half = f"scale={W}:-2,crop={W}:{H//2}:(iw-{W})/2:(ih-{H//2})/2,setsar=1,fps=24"
    fc = (f"[0:v]trim=start={SKIP},setpts=PTS-STARTPTS,{half}[t];"
          f"[1:v]trim=start={SKIP},setpts=PTS-STARTPTS,{half}[b];"
          + ("[t][b]vstack=inputs=2[v]" if CLEAN else f"[t][b]vstack=inputs=2,subtitles='{a}':fontsdir=/usr/share/fonts/truetype/freefont[v]"))
    cmd = [FF, "-y", "-hide_banner", "-loglevel", "error",
           "-i", str(B / "hooks" / top), "-i", str(B / "hooks" / bot), "-i", str(AUDIO(hk)),
           "-filter_complex", fc, "-map", "[v]", *([] if CLEAN else ["-map", "2:a"]), "-t", f"{dur:.2f}",
           "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-r", "24",
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    print(hk, f"{dur:.2f}s", out.name, top, bot)
