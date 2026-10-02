from faster_whisper import WhisperModel
import json
m = WhisperModel("base.en", compute_type="int8")
segs, info = m.transcribe("intake/inspo.mp4", word_timestamps=False)
out = [dict(s=round(s.start,2), e=round(s.end,2), t=s.text.strip()) for s in segs]
json.dump(out, open("work/inspo_transcript.json","w"), indent=1)
w = sum(len(o["t"].split()) for o in out)
print("words", w, "dur", info.duration, "wpm", round(w/info.duration*60,1))
