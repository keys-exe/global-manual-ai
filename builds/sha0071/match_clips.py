# §40 step 1 — match each clip to the scene master (exposure, white balance, saturation), one adjustment per clip.
import sys, json, subprocess, numpy as np
sys.path.insert(0, "../../.claude/skills/ai-prompt-engineer/scripts")
import light_check as L, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
R = L.load_mean("renders/SC01-F-MASTER.png")
def filt(sat, gain, warm):
    # warmth = r - b mean (0..1 scale); shift red/blue in opposite directions
    return (f"eq=saturation={sat:.3f},colorchannelmixer=rr={gain*(1-warm):.4f}:gg={gain:.4f}:bb={gain*(1+warm):.4f},format=yuv420p")
for beat in sys.argv[1:]:
    src = f"renders/{beat}.mp4"; sat, gain, warm = 1.0, 1.0, 0.0
    for it in range(5):
        out = f"edit/match/{beat}.mp4"
        subprocess.run([FF, "-loglevel", "error", "-y", "-i", src, "-vf", filt(sat, gain, warm), "-c:v", "libx264", "-crf", "12", "-preset", "fast", "-c:a", "copy", out], check=True)
        S = L.load_mean(out)
        ds = (S["sat"] - R["sat"]) / R["sat"]; dl = (S["luma"] - R["luma"]) / R["luma"]; dw = S["warmth"] - R["warmth"]
        print(beat, it, f"sat {ds:+.3f} luma {dl:+.3f} warmth {dw:+.4f}")
        if abs(ds) < 0.1 and abs(dl) < 0.08 and abs(dw) < 0.03: break
        sat /= (1 + ds); gain /= (1 + dl); warm += dw / 2
    json.dump({"sat": sat, "gain": gain, "warm": warm}, open(f"edit/match/{beat}.json", "w"))
