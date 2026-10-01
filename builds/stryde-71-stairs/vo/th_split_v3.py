"""V7.66.0 — beat times on the house-cut take (whole take, one pass) and the TH cut points for the one-go Avatar V video.
TH segments are cut mid-gap between the neighbouring words; repeated script lines (hook versions) are aligned once."""
import json,re,difflib,sys,bisect
from faster_whisper import WhisperModel
src=sys.argv[1]; out=sys.argv[2]
m=WhisperModel("base.en",device="cpu",compute_type="int8")
segs,_=m.transcribe(src,word_timestamps=True,vad_filter=False)
W=[(float(w.start),float(w.end),w.word.strip()) for s in segs for w in (s.words or [])]
NUM={"eleven":"11"}
norm=lambda t:(lambda x:NUM.get(x,x))(re.sub(r"[^a-z0-9]","",t.lower()))
hw=[norm(w) for _,_,w in W]
rows=json.load(open("../work/actmap_rows.json"))
sw=[];span={};seen={}
for r in rows:
    if not r["line"]: continue
    if r["line"] in seen: span[r["beat"]]=span[seen[r["line"]]]; continue
    toks=[norm(t) for t in r["line"].split() if norm(t)]
    span[r["beat"]]=(len(sw),len(sw)+len(toks)); sw+=toks; seen[r["line"]]=r["beat"]
sm=difflib.SequenceMatcher(None,sw,hw,autojunk=False)
s2h={a+k:b+k for a,b,n in sm.get_matching_blocks() for k in range(n)}
def h(i,d):
    while i not in s2h: i+=d
    return s2h[i]
res={}
for r in rows:
    a,b=span[r["beat"]]; i,j=h(a,1),h(b-1,-1)
    d=dict(type=r["type"],start=round(W[i][0],3),end=round(W[j][1],3),line=r["line"])
    if r["type"]=="TH":
        d["cut_in"]=round((W[i-1][1]+W[i][0])/2,3) if i>0 else 0.0
        d["cut_out"]=round((W[j][1]+W[j+1][0])/2,3) if j+1<len(W) else round(W[j][1]+0.3,3)
        d["heard"]=" ".join(w for _,_,w in W[i:j+1])
    res[r["beat"]]=d
json.dump(res,open(out,"w"),indent=1)
print("matched",len(s2h),"/",len(sw))
for k,v in res.items():
    if v["type"]=="TH": print(k,v["cut_in"],v["cut_out"],"|",v["heard"])
