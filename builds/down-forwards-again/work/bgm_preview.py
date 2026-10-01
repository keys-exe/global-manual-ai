#!/usr/bin/env python3
"""A listening preview of one variant (§40A, the user's check): the doctor's locked VO (TH-<hook>.trim + TH-A1…A5.trim audio, as the edit lays them)
with BGM-<hook> under it — music ~18 dB under the voice, ducked further while he speaks (sidechain, §24M levels). Not the edit; the edit sets
its own levels in CapCut. usage: bgm_preview.py HK1 → edit/music/PREVIEW-HK1.mp3"""
import subprocess, sys, pathlib
import numpy as np, imageio_ffmpeg
FF = imageio_ffmpeg.get_ffmpeg_exe(); B = pathlib.Path(__file__).parents[1]; h = sys.argv[1]
parts = [B / f"th/TH-{p}.trim.mp4" for p in [h, "A1", "A2", "A3", "A4", "A5"]]
def rms(p):
    raw = subprocess.run([FF, "-v", "error", "-i", str(p), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float) / 32768; w = 8000
    v = [np.sqrt((a[i:i + w] ** 2).mean()) for i in range(0, len(a) - w, w)]; v = [x for x in v if x > 0.01]
    return 20 * np.log10(np.median(v))
vo = B / f"edit/music/_vo_{h}.wav"
fc = "".join(f"[{i}:a]aresample=48000,aformat=channel_layouts=stereo[a{i}];" for i in range(len(parts))) + "".join(f"[a{i}]" for i in range(len(parts))) + f"concat=n={len(parts)}:v=0:a=1[v]"
subprocess.run([FF, "-y", "-v", "error", *sum([["-i", str(p)] for p in parts], []), "-filter_complex", fc, "-map", "[v]", str(vo)], check=True)
bgm = B / f"edit/music/BGM-{h}.wav"
g = rms(vo) - 18 - rms(bgm)
fc = (f"[1:a]volume={g:.1f}dB[m];[0:a]asplit[v1][v2];[m][v1]sidechaincompress=threshold=0.03:ratio=3:attack=30:release=400:makeup=1[md];"
      f"[v2][md]amix=inputs=2:normalize=0:duration=first[o]")
out = B / f"edit/music/PREVIEW-{h}.mp3"
subprocess.run([FF, "-y", "-v", "error", "-i", str(vo), "-i", str(bgm), "-filter_complex", fc, "-map", "[o]", "-c:a", "libmp3lame", "-b:a", "256k", str(out)], check=True)
vo.unlink(); print(out, f"music gain {g:.1f} dB")
