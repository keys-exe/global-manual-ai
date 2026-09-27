import json, re
from faster_whisper import WhisperModel
m = WhisperModel("small.en", compute_type="int8")
plan = json.load(open("edit/plan.json")); lines = {x["beat"]: x.get("line") for x in json.load(open("act_map.json"))}
def ts(t): h=int(t//3600); t-=h*3600; mm=int(t//60); t-=mm*60; return f"{h}:{mm:02d}:{t:05.2f}"
events=[]; t0=0.0
for s in plan["shots"]:
    line = lines.get(s["beat"])
    if line and not s.get("silent"):
        segs,_ = m.transcribe(f"renders/{s['beat']}.mp4", word_timestamps=True)
        ws=[w for sg in segs for w in sg.words if s["in"]-0.05 <= w.start < s["out"]]
        words=line.split()
        # chunk the verbatim script words at punctuation, ≤5 words
        chunks=[]; cur=[]
        for w in words:
            cur.append(w)
            if re.search(r"[.,?!]$", w) or len(cur)>=5: chunks.append(cur); cur=[]
        if cur: chunks.append(cur)
        for i in range(1,len(chunks)):
            if len(chunks[i])==1 and len(chunks[i-1])>=4 and not re.search(r"[.,?!]$", chunks[i-1][-1]):
                chunks[i]=chunks[i-1][-2:]+chunks[i]; chunks[i-1]=chunks[i-1][:-2]
        n=len(words); k=0
        for c in chunks:
            a=k; b=k+len(c)-1; k+=len(c)
            ia=min(int(a*len(ws)/n), len(ws)-1); ib=min(int(b*len(ws)/n), len(ws)-1)
            st=t0+max(0,ws[ia].start-s["in"]); en=t0+min(s["out"]-s["in"], ws[ib].end-s["in"]+0.25)
            events.append((st,en," ".join(c)))
    t0 += s["out"]-s["in"]
for i in range(len(events)-1):
    if events[i][1] > events[i+1][0]: events[i]=(events[i][0],events[i+1][0]-0.02,events[i][2])
hdr="""[Script Info]
ScriptType: v4.00+
PlayResX: 720
PlayResY: 1280

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Cap,Liberation Sans,30,&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,0,0,2,60,60,300,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
open("edit/captions.ass","w").write(hdr+"".join(f"Dialogue: 0,{ts(a)},{ts(b)},Cap,,0,0,0,,{t}\n" for a,b,t in events))
for e in events: print(f"{e[0]:6.2f}-{e[1]:6.2f}  {e[2]}")
