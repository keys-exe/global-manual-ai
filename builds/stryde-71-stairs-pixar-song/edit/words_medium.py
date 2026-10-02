#!/usr/bin/env python3
"""Sung word timings for the cut (§30H V7.80.0): faster-whisper medium.en, word timestamps, on the whole song."""
import json, sys
from pathlib import Path
from faster_whisper import WhisperModel
B = Path(__file__).parent.parent
m = WhisperModel("medium.en", device="cpu", compute_type="int8")
segs, _ = m.transcribe(str(B / "intake/song.mp3"), word_timestamps=True, vad_filter=False, beam_size=5,
                       condition_on_previous_text=False)
out = [{"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 3)} for s in segs for w in s.words]
(B / "edit/words_medium.json").write_text(json.dumps(out))
print(len(out))
