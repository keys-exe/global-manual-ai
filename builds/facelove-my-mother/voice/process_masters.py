"""§24I part 7 step 4 + the 2026-09-30 amendment: extract each master's audio as generated (stream copy), then cut only the
idle silence outside the speech (0.4 s before the first word, 0.5 s after the last). Inner pauses, pace and room untouched.
Usage: process_masters.py <KEY>=<result_url> ..."""
import sys, json, subprocess, pathlib, urllib.request
import imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe(); H = pathlib.Path(__file__).parent
m = WhisperModel("medium.en", device="cpu", compute_type="int8")
out = {}
for arg in sys.argv[1:]:
    k, url = arg.split("=", 1)
    clip = H / f"{k}_voice_clip.mp4"; urllib.request.urlretrieve(url, clip)
    raw = H / f"{k}_voice_master_raw.m4a"
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(clip), "-vn", "-c:a", "copy", str(raw)], check=True)
    segs, info = m.transcribe(str(raw), word_timestamps=True)
    ws = [w for s in segs for w in s.words]
    a, b = max(0, ws[0].start - 0.4), min(info.duration, ws[-1].end + 0.5)
    mast = H / f"{k}_voice_master.m4a"
    subprocess.run([FF, "-y", "-loglevel", "error", "-ss", f"{a:.3f}", "-to", f"{b:.3f}", "-i", str(raw), "-c:a", "aac", "-b:a", "192k", str(mast)], check=True)
    mp3 = H / f"{k}_voice_master.mp3"
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(mast), "-c:a", "libmp3lame", "-b:a", "192k", str(mp3)], check=True)
    board = H / f"{k}_voice_master.mp4"   # the board refuses .m4a — same audio in an mp4 container
    subprocess.run([FF, "-y", "-loglevel", "error", "-i", str(mast), "-c:a", "copy", str(board)], check=True)
    text = " ".join(w.word.strip() for w in ws)
    out[k] = {"url": url, "clip_s": round(info.duration, 2), "speech_from": round(ws[0].start, 2), "speech_to": round(ws[-1].end, 2),
              "master_s": round(b - a, 2), "heard": text}
    print(k, out[k])
json.dump(out, open(H / "masters.json", "w"), indent=1)
