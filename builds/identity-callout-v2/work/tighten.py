# Shorten true silences (silencedetect -40 dB, > maxgap) to maxgap, centred. Voiced audio is never touched.
import json, sys, re, subprocess, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe()
src, out, maxgap = sys.argv[1], sys.argv[2], float(sys.argv[3])
log = subprocess.run([FF, "-i", src, "-af", f"silencedetect=noise=-40dB:d={maxgap}", "-f", "null", "-"], capture_output=True, text=True).stderr
st = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", log)]; en = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", log)]
dur = float(re.search(r"Duration: (\d+):(\d+):([\d.]+)", log).group(3)) + 60 * int(re.search(r"Duration: (\d+):(\d+)", log).group(2))
keep, cuts, t0 = [], [], 0.0
for s, e in zip(st, en):
    if s < 0.05 or e > dur - 0.05: continue
    a, b = s + maxgap / 2, e - maxgap / 2
    keep.append((t0, a)); cuts.append((round(a, 3), round(b, 3))); t0 = b
keep.append((t0, None))
f = "".join(f"[0:a]atrim=start={a}" + (f":end={b}" if b else "") + f",asetpts=PTS-STARTPTS[a{i}];" for i, (a, b) in enumerate(keep)) + "".join(f"[a{i}]" for i in range(len(keep))) + f"concat=n={len(keep)}:v=0:a=1[o]"
subprocess.run([FF, "-y", "-loglevel", "error", "-i", src, "-filter_complex", f, "-map", "[o]", "-c:a", "libmp3lame", "-q:a", "2", out], check=True)
print(json.dumps({"src": src, "out": out, "rule": f"silences >{maxgap}s at -40dB shortened to {maxgap}s", "cuts": cuts, "n_cuts": len(cuts), "removed_s": round(sum(b - a for a, b in cuts), 2)}))
