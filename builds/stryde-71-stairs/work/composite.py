"""Join a list or montage line's B-rolls into one clip, each picture cut on its own word (cut 7).
usage: composite.py OUT.mp4 clip:dur[:in] ... — each piece from its in-point (default 0.4s skip),
slowed to no slower than 0.8x when its footage is short, 1080x1920 at 24 fps, no audio."""
import subprocess, sys, json
import imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()

def length(p):
    r = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr
    h, m, s = r.split("Duration: ")[1].split(",")[0].split(":")
    return int(h) * 3600 + int(m) * 60 + float(s)

out, pieces = sys.argv[1], sys.argv[2:]
args, chains, report = [], [], []
for i, spec in enumerate(pieces):
    clip, dur, *rest = spec.split(":")
    dur, inp = float(dur), float(rest[0]) if rest else 0.4
    have = length(clip) - inp
    if have < dur:                      # give back the skipped opening first, then slow (>= 0.8x)
        inp = max(0.0, length(clip) - dur); have = length(clip) - inp
    speed = min(1.0, have / dur)
    if speed < 0.8:
        sys.exit(f"{clip}: needs {dur:.2f}s, has {have:.2f}s even at 0.8x")
    args += ["-ss", f"{inp:.3f}", "-i", clip]
    chains.append(f"[{i}:v]setpts=(PTS-STARTPTS)/{speed:.4f},fps=24,scale=1080:1920:force_original_aspect_ratio=increase,"
                  f"crop=1080:1920,setsar=1,trim=duration={dur:.4f},setpts=PTS-STARTPTS[v{i}]")
    report.append({"clip": clip.split("/")[-1], "dur": dur, "in": round(inp, 3), "speed": round(speed, 3)})
graph = ";".join(chains) + ";" + "".join(f"[v{i}]" for i in range(len(pieces))) + f"concat=n={len(pieces)}:v=1:a=0[o]"
subprocess.run([FF, "-y", "-v", "error", *args, "-filter_complex", graph, "-map", "[o]", "-an",
                "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", out], check=True)
print(json.dumps({"out": out, "len": round(length(out), 3), "pieces": report}))
