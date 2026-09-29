import sys,json
from faster_whisper import WhisperModel
m=WhisperModel("small",device="cpu",compute_type="int8",cpu_threads=4)
for h in sys.argv[1:]:
    segs,_=m.transcribe(f"{h}.16k.wav",word_timestamps=True,vad_filter=False)
    out=[{"s":round(s.start,2),"e":round(s.end,2),"t":s.text.strip(),"w":[[round(w.start,2),round(w.end,2),w.word] for w in s.words]} for s in segs]
    json.dump(out,open(f"{h}.tx.json","w"),indent=0)
    print(h,len(out),flush=True)
