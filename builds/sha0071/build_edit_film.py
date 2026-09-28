# SC-01 film finish on the raw cut (user, 2026-09-27: "color grading and fades ... look like a movie not a grave"):
# the raw shots (build_edit_raw.py) → one warm, gentle film grade → captions → fade out to black → the score mixed under the clips' own dialogue (mix_scene.py). No trims or speed changes (§24L).
import json, subprocess, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
plan = json.load(open("edit/plan.json"))
T = sum(s["out"] - s["in"] for s in plan["shots"])
FADE_OUT = 1.5
# Warm and alive, not cold: soft S-curve with a little lift in the blacks and roll-off in the whites,
# mids/skin nudged warm, shadows a touch cool, saturation almost natural, soft lens vignette. No grain and no fade in (user, 2026-09-27); captions white, no outline or shadow.
GRADE = ("curves=master='0/0.035 0.25/0.22 0.5/0.5 0.75/0.79 1/0.97',"
         "colorbalance=rs=-0.02:bs=0.03:rm=0.025:gm=0.005:bm=-0.02:rh=0.015:bh=-0.01,"
         "eq=saturation=0.96,vignette=PI/5")
vf = (f"{GRADE},subtitles=edit/captions.ass:fontsdir=/usr/share/fonts/truetype/liberation,"
      f"fade=t=out:st={T - FADE_OUT:.3f}:d={FADE_OUT},format=yuv420p")
subprocess.run([FF, "-loglevel", "error", "-y", "-i", "edit/raw_cut.mkv", "-vf", vf,
    "-af", f"afade=t=out:st={T - FADE_OUT:.3f}:d={FADE_OUT}",
    "-c:v", "libx264", "-crf", "12", "-preset", "slow", "-c:a", "pcm_s16le", "edit/film_picture.mkv"], check=True)
subprocess.run([FF, "-loglevel", "error", "-y", "-i", "edit/film_picture.mkv", "-vn", "-ac", "2", "-ar", "48000",
    "sound/SC01.dialogue.film.wav"], check=True)
mix = json.load(open("sound/SC01.mix.json"))
mix.update({"picture": "../edit/film_picture.mkv", "dialogue": "SC01.dialogue.film.wav"})
json.dump(mix, open("sound/SC01.mix.film.json", "w"), indent=1)
subprocess.run(["python3", "../../.claude/skills/ai-prompt-engineer/scripts/mix_scene.py", "sound/SC01.mix.film.json",
    "--out", "edit/film_mix.mkv"], check=True)
out = "edit/SHA0071_SC01_HK1_film.mp4"
subprocess.run([FF, "-loglevel", "error", "-y", "-i", "edit/film_mix.mkv", "-c:v", "libx264", "-b:v", "4300k",
    "-maxrate", "5M", "-bufsize", "10M", "-preset", "slow", "-pix_fmt", "yuv420p",
    "-af", f"afade=t=out:st={T - FADE_OUT:.3f}:d={FADE_OUT}", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print(out, round(T, 2))
