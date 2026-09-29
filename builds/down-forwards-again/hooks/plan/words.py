#!/usr/bin/env python3
"""Word timings (faster-whisper medium.en) and a 30 ms loudness trace for the hook talking heads — for placing cuts by hand."""
import sys, json, subprocess
import numpy as np, imageio_ffmpeg
from faster_whisper import WhisperModel
FF = imageio_ffmpeg.get_ffmpeg_exe()
m = WhisperModel("medium.en", compute_type="int8")
out = {}
for h in sys.argv[1:]:
    f = f"th/TH-{h}.trim.mp4"
    s, _ = m.transcribe(f, word_timestamps=True)
    words = [(w.word.strip(), round(w.start, 2), round(w.end, 2)) for x in s for w in x.words]
    raw = subprocess.run([FF, "-v", "error", "-i", f, "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(float) / 32768
    db = [round(float(20 * np.log10(np.sqrt((a[i:i + 480] ** 2).mean()) + 1e-9)), 1) for i in range(0, len(a) - 480, 480)]
    out[h] = {"words": words, "db30ms": db}
    print(h, words)
json.dump(out, open("hooks/plan/words.json", "w"))
