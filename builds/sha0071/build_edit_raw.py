# SC-01 raw cut: same shots and cut points as build_edit.py, but straight from the renders —
# no colour match, no grade, no grain, and the clips' own dialogue untouched (no denoise, no levelling,
# no room tone). Only the SH08 punch-in and the captions are kept.
import json, subprocess, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
plan = json.load(open("edit/plan.json"))
parts = []
for i, s in enumerate(plan["shots"]):
    out = f"edit/raw_seg_{i:02d}.mkv"
    cmd = [FF, "-loglevel", "error", "-y", "-ss", str(s["in"]), "-to", str(s["out"]), "-i", f"renders/{s['beat']}.mp4"]
    if s.get("silent"):
        cmd += ["-f", "lavfi", "-t", str(s["out"] - s["in"]), "-i", "anullsrc=r=48000:cl=stereo", "-map", "0:v", "-map", "1:a"]
    else:
        cmd += ["-map", "0:v", "-map", "0:a"]
    pi = s.get("punch_in")
    vf = (f"crop=iw/{pi}:ih/{pi}:(iw-iw/{pi})*0.45:(ih-ih/{pi})*0.30," if pi else "") + "scale=720:1280:flags=lanczos,fps=24,setsar=1"
    cmd += ["-vf", vf, "-af", "aresample=48000", "-ac", "2", "-c:v", "libx264", "-crf", "10", "-preset", "fast", "-c:a", "pcm_s16le", out]
    subprocess.run(cmd, check=True); parts.append(out)
open("edit/raw_concat.txt", "w").write("".join(f"file '{p.split('/')[-1]}'\n" for p in parts))
subprocess.run([FF, "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", "edit/raw_concat.txt", "-c", "copy", "edit/raw_cut.mkv"], check=True)
out = "edit/SHA0071_SC01_HK1_raw.mp4"
subprocess.run([FF, "-loglevel", "error", "-y", "-i", "edit/raw_cut.mkv",
    "-vf", "subtitles=edit/captions.ass:fontsdir=/usr/share/fonts/truetype/liberation,format=yuv420p",
    "-c:v", "libx264", "-b:v", "4300k", "-maxrate", "5M", "-bufsize", "10M", "-preset", "slow", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print(out)
