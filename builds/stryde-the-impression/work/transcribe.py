import json,sys
from faster_whisper import WhisperModel
m=WhisperModel("small.en",device="cpu",compute_type="int8")
segs,_=m.transcribe(sys.argv[1],vad_filter=False)
out=[{"s":round(s.start,2),"e":round(s.end,2),"t":s.text.strip()} for s in segs]
json.dump(out,open(sys.argv[2],"w"),indent=0)
print(sum(len(o["t"].split()) for o in out),"words")
