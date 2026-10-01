"""Strip the Seedance bed (music / ambience it added despite NEG-SOUND) from a clip's audio: ElevenLabs Voice Isolator
(§24M — the dialogue goes into the mix isolated). Usage: isolate.py CLIP.mp4 [...] → edit/iso/<clip>.iso.mp3"""
import os, subprocess, sys, requests
from pathlib import Path
import imageio_ffmpeg

FF = imageio_ffmpeg.get_ffmpeg_exe()
OUT = Path(__file__).resolve().parent / "iso"
for clip in map(Path, sys.argv[1:]):
    wav = OUT / (clip.stem + ".src.wav")
    out = OUT / (clip.stem + ".iso.mp3")
    if out.exists():
        print("have", out.name); continue
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(clip), "-vn", "-ac", "1", "-ar", "44100", "-af", "apad=pad_dur=1.5", str(wav)], check=True)  # the isolator wants ≥ 4.6 s
    with open(wav, "rb") as f:
        r = requests.post("https://api.elevenlabs.io/v1/audio-isolation", headers={"xi-api-key": os.environ["ELEVENLABS_API_KEY"]},
                          files={"audio": (wav.name, f, "audio/wav")}, timeout=300)
    if r.status_code != 200:
        sys.exit(f"{clip.name}: {r.status_code} {r.text[:300]}")
    raw = OUT / (clip.stem + ".pad.mp3"); raw.write_bytes(r.content); wav.unlink()
    dur = float(__import__("re").search(r"Duration: \d+:\d+:([\d.]+)", subprocess.run([FF, "-hide_banner", "-i", str(clip)], capture_output=True, text=True).stderr).group(1))
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(raw), "-t", f"{dur:.3f}", str(out)], check=True); raw.unlink()
    print("isolated", out.name, len(r.content))
