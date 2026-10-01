"""Hook edits for the user's check (user 2026-10-01: "give me the hook edit first, I'll check them").
Each hook: its five confirmed Seedance shots, whole (§24L, no trimming), in order; the clip dialogue at 0 dB; the locked
narration (VO-T1 v2) laid on SH05 (L004 for Hooks A/B/C — the same line as L008/L013 — and L016 for Hook E); the film LUT
(LUT-HALFMYAGE.cube); loudness -14 LUFS. No music yet: MUS-HK is composed after the Music Register Map (§40A) — the next pass."""
import re, subprocess, sys
from pathlib import Path
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
B = Path(__file__).resolve().parent.parent
OUT = B / "edit" / "hooks"
LUT = B / "edit" / "LUT-HALFMYAGE.cube"
CONFIRMED = {  # the version the user confirmed on the board
    "HKA": [1, 1, 1, 1, 1], "HKB": [1, 1, 2, 1, 3], "HKC": [3, 3, 2, 1, 3], "HKE": [3, 3, 3, 2, 3]}
VO = {"HKA": "L004_v2.m4a", "HKB": "L004_v2.m4a", "HKC": "L004_v2.m4a", "HKE": "L016_v2.m4a"}
VO_IN = 0.3  # the narration enters 0.3 s into SH05


def info(p):
    s = subprocess.run([FF, "-hide_banner", "-i", str(p)], capture_output=True, text=True).stderr
    h, m, sec = re.search(r"Duration: (\d+):(\d+):([\d.]+)", s).groups()
    return int(h) * 3600 + int(m) * 60 + float(sec), "Audio:" in s


def build(hook):
    shots = [B / "hooks" / hook / f"{hook}-SH0{i + 1}_v{v}.mp4" for i, v in enumerate(CONFIRMED[hook])]
    args, parts, t, sh05_at = [], [], 0.0, 0.0
    for i, s in enumerate(shots):
        d, has_a = info(s)
        args += ["-i", str(s)]
        if i == 4:
            sh05_at = t
        parts.append((i, d, has_a))
        t += d
    n = len(shots)
    args += ["-i", str(B / "edit" / "vo" / VO[hook])]
    fc = []
    for i, d, has_a in parts:
        fc.append(f"[{i}:v]scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:(ow-iw)/2:(oh-ih)/2,fps=24,setsar=1,format=yuv420p[v{i}]")
        if has_a:
            fc.append(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo,apad,atrim=0:{d:.3f}[a{i}]")
        else:
            fc.append(f"anullsrc=r=48000:cl=stereo,atrim=0:{d:.3f}[a{i}]")
    fc.append("".join(f"[v{i}][a{i}]" for i in range(n)) + f"concat=n={n}:v=1:a=1[vc][ac]")
    fc.append(f"[vc]lut3d=file='{LUT}'[vg]")
    ms = int((sh05_at + VO_IN) * 1000)
    fc.append(f"[{n}:a]aresample=48000,aformat=channel_layouts=stereo,adelay={ms}|{ms}[vo]")
    fc.append("[ac][vo]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1:LRA=11[am]")
    out = OUT / f"{hook}_edit_v1.mp4"
    cmd = [FF, "-y", "-hide_banner", "-loglevel", "error", *args, "-filter_complex", ";".join(fc), "-map", "[vg]", "-map", "[am]",
           "-c:v", "libx264", "-crf", "17", "-preset", "medium", "-c:a", "aac", "-b:a", "192k", "-ar", "48000", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    d, _ = info(out)
    print(hook, f"{t:.2f}s of shots ->", out.name, f"{d:.2f}s", "VO at", f"{sh05_at + VO_IN:.2f}s")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for h in (sys.argv[1:] or CONFIRMED):
        build(h)
