import json,sys
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8")
segs,info=m.transcribe(sys.argv[1],word_timestamps=False,vad_filter=False)
out=[{"s":round(s.start,2),"e":round(s.end,2),"t":s.text.strip()} for s in segs]
json.dump(out,open(sys.argv[2],"w"),indent=1)
