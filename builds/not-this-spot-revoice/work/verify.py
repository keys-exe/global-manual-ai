import sys,json,difflib
sys.argv=[sys.argv[0],sys.argv[1],"plan"]; X=sys.argv[1]
exec(open("revoice.py").read().split("if STEP ==")[0])
from faster_whisper import WhisperModel
m=WhisperModel("medium.en",compute_type="int8")
W=[(w.start,w.end,w.word) for s in m.transcribe(f"mix{X}.wav",word_timestamps=True)[0] for w in s.words]
json.dump(W,open(f"newwords{X}.json","w"))
st=[t for u in units() for t in toks(u)]; nt=[t for w in W for t in toks(w[2])]
sm=difflib.SequenceMatcher(None,st,nt,autojunk=False)
print(X,"script words",len(st),"heard",len(nt),"match %.3f"%sm.ratio())
for op,a,b,c,d in sm.get_opcodes():
    if op!="equal": print(" ",op,st[a:b],"->",nt[c:d])
# timing drift: per unit, new start vs original start
P=json.load(open(f"plan{X}.json")); ns=fill(align(P["units"],W))
d=[abs(ns[u][0]-P["span"][u][0]) for u in range(len(P["units"]))]
import numpy as np; print("unit start drift: median %.2fs  max %.2fs  >0.25s: %d"%(np.median(d),max(d),sum(x>0.25 for x in d)))
