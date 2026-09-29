#!/usr/bin/env python3
"""Hook rough cuts with every cut placed by hand (user notes 2026-09-29, build-local — the shared assemble.py is not used or changed here):
  HK1: the stairs shot runs until 'backwards' has fully rung out (the loudness trace, not the transcript word end); the last shot cuts on 'And'.
  HK2: the strap cuts in earlier than 'It'.   HK3: open on the B-roll, not the doctor.
Timeline JSON: {"th": "th/TH-HKn.trim.mp4", "out": "...mp4", "segments": [{"kind": "TH"|"BR", "start": s, "end": s, "clip": path, "in": s}]}
Video: each segment cut from its source (TH at the same timeline time; BR from its in-point), scaled/cropped to 1080x1920 at 24 fps,
concatenated frame-exact; audio = the TH track untouched. Verifies duration = the TH audio and no black frames."""
import sys, json, subprocess, re, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
def dur(p):
    e = subprocess.run([FF, "-i", p], capture_output=True, text=True).stderr
    h, m, s = re.search(r"Duration: (\d+):(\d+):([\d.]+)", e).groups(); return int(h) * 3600 + int(m) * 60 + float(s)
t = json.load(open(sys.argv[1]))
th = t["th"]; total = dur(th); segs = t["segments"]
assert abs(segs[0]["start"]) < 1e-6 and abs(segs[-1]["end"] - total) < 0.05, "segments must cover 0..end"
for a, b in zip(segs, segs[1:]): assert abs(a["end"] - b["start"]) < 1e-6, "gap/overlap"
inputs, parts = [], []
for i, s in enumerate(segs):
    d = s["end"] - s["start"]
    if s["kind"] == "TH":
        src, ss = th, s["start"]
    else:
        src, ss = s["clip"], s.get("in", 0.4)
    sp = s.get("speed", 1.0); assert 0.8 <= sp <= 1.0, "never slower than 0.8x (§30H), never faster"
    if s["kind"] == "BR":
        assert ss + d * sp <= dur(src) + 1e-3, f"{s['clip']}: needs {ss + d * sp:.2f}s, has {dur(src):.2f}s"
    inputs += ["-ss", f"{ss:.3f}", "-t", f"{d * sp + 0.05:.3f}", "-i", src]
    parts.append(f"[{i}:v]setpts=(PTS-STARTPTS)/{sp},scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=24,setsar=1,trim=duration={d:.3f},setpts=PTS-STARTPTS[v{i}];")
n = len(segs)
graph = "".join(parts) + "".join(f"[v{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=0[v]"
cmd = [FF, "-v", "error", "-y", *inputs, "-i", th, "-filter_complex", graph, "-map", "[v]", "-map", f"{n}:a",
       "-c:v", "libx264", "-crf", "16", "-preset", "medium", "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-shortest", t["out"]]
subprocess.run(cmd, check=True)
e = subprocess.run([FF, "-i", t["out"], "-vf", "blackdetect=d=0.1:pix_th=0.05", "-an", "-f", "null", "-"], capture_output=True, text=True).stderr
black = re.findall(r"black_start:([\d.]+)", e)
print(json.dumps({"out": t["out"], "duration_s": round(dur(t["out"]), 2), "master_s": round(total, 2),
                  "duration_matches_master": abs(dur(t["out"]) - total) < 0.1, "black_frames": black,
                  "segments": [(s["kind"], s.get("beat", "TH"), round(s["start"], 2), round(s["end"], 2)) for s in segs]}, indent=1))
