# SC-01 edit: whole shots cut at their cut cues (§24L — no speed change, no cut inside a take),
# matched colour (§40.1) → one LUT-style cold grade (§40.2) → one grain pass (§40.3), dialogue-only audio
# cleaned per clip, one continuous room tone, no music (SC-01 sound plan), captions lower-centre, one line at a time.
import json, subprocess, sys, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
plan = json.load(open("edit/plan.json"))
parts = []
for i, s in enumerate(plan["shots"]):
    out = f"edit/seg_{i:02d}.mkv"
    af = "anullsrc=r=48000:cl=stereo" if s.get("silent") else None
    cmd = [FF, "-loglevel", "error", "-y", "-ss", str(s["in"]), "-to", str(s["out"]), "-i", f"edit/match/{s['beat']}.mp4"]
    if s.get("silent"):
        cmd += ["-f", "lavfi", "-t", str(s["out"] - s["in"]), "-i", af, "-map", "0:v", "-map", "1:a"]
        afilt = "anull"
    else:
        cmd += ["-map", "0:v", "-map", "0:a"]
        afilt = "afftdn=nr=18:nf=-40,highpass=f=80,loudnorm=I=-20:TP=-3:LRA=7,aresample=48000"
    pi = s.get("punch_in")
    vf = (f"crop=iw/{pi}:ih/{pi}:(iw-iw/{pi})*0.45:(ih-ih/{pi})*0.30," if pi else "") + "scale=720:1280:flags=lanczos,fps=24,setsar=1"
    cmd += ["-vf", vf, "-af", afilt, "-ac", "2",
            "-c:v", "libx264", "-crf", "10", "-preset", "fast", "-c:a", "pcm_s16le", out]
    subprocess.run(cmd, check=True); parts.append(out)
open("edit/concat.txt", "w").write("".join(f"file '{p.split('/')[-1]}'\n" for p in parts))
subprocess.run([FF, "-loglevel", "error", "-y", "-f", "concat", "-safe", "0", "-i", "edit/concat.txt", "-c", "copy", "edit/sc01_cut.mkv"], check=True)
dur = sum(s["out"] - s["in"] for s in plan["shots"])
# room tone: soft air-handling rumble + faint fluorescent hum, steady, under the whole scene
subprocess.run([FF, "-loglevel", "error", "-y", "-f", "lavfi", "-t", str(dur), "-i", "anoisesrc=color=brown:amplitude=0.6:seed=7",
    "-f", "lavfi", "-t", str(dur), "-i", "sine=frequency=120:sample_rate=48000",
    "-filter_complex", "[0]lowpass=f=400,highpass=f=40,volume=0.035[a];[1]volume=0.0025[h];[a][h]amix=inputs=2:normalize=0,aformat=channel_layouts=stereo,aresample=48000[o]",
    "-map", "[o]", "-c:a", "pcm_s16le", "edit/roomtone.wav"], check=True)
# grade (one look for the whole scene: cool fluorescent wound, low saturation) + grain + captions
ass = "edit/captions.ass"
grade = ("colorbalance=rs=-0.03:gs=0.0:bs=0.04:rm=-0.02:bm=0.02,eq=saturation=0.88:contrast=1.04,"
         "noise=alls=5:allf=t,subtitles=" + ass + ":fontsdir=/usr/share/fonts/truetype/liberation")
subprocess.run([FF, "-loglevel", "error", "-y", "-i", "edit/sc01_cut.mkv", "-i", "edit/roomtone.wav",
    "-filter_complex", f"[0:v]{grade},format=yuv420p[v];[0:a][1:a]amix=inputs=2:normalize=0,loudnorm=I=-14:TP=-1:LRA=9[a]",
    "-map", "[v]", "-map", "[a]", "-c:v", "libx264", "-crf", "16", "-preset", "slow", "-profile:v", "high", "-pix_fmt", "yuv420p",
    "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", plan["out"]], check=True)
print(plan["out"], round(dur, 2))
