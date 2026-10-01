"""TH audio v2 (user 2026-09-28: "the th is too quick the trim") — cut each TH segment from the UNTIGHTENED take
(full/<take>.mp3, natural TTS pauses) instead of the house cut, with room before the first word and after the last:
real room tone from the neighbouring gaps first, then digital silence to reach LEAD / TAIL. Any repeated script line
(hook versions, cutaways) is aligned once."""
import json,re,difflib,subprocess,imageio_ffmpeg,sys
FF=imageio_ffmpeg.get_ffmpeg_exe()
take=sys.argv[1] if len(sys.argv)>1 else "T1"
LEAD,TAIL,GUARD=0.35,0.6,0.06
W=[(float(s),float(e),w) for s,e,w in json.load(open(f"full/{take}.words.json"))]
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
m=difflib.SequenceMatcher(None,sw,hw,autojunk=False)
s2h={a+k:b+k for a,b,n in m.get_matching_blocks() for k in range(n)}
def h(i,d):
    while i not in s2h: i+=d
    return s2h[i]
out={}
for r in rows:
    if r["type"]!="TH": continue
    a,b=span[r["beat"]]; i,j=h(a,1),h(b-1,-1)
    st,en=W[i][0],W[j][1]
    prev_end=W[i-1][1] if i>0 else 0.0
    next_st=W[j+1][0] if j+1<len(W) else en+TAIL
    cin=max(st-LEAD,prev_end+GUARD,0.0); cout=min(en+TAIL,next_st-GUARD)
    pad_in=round(LEAD-(st-cin),3); pad_out=round(TAIL-(cout-en),3)
    k=r["beat"]
    af=f"adelay={int(max(pad_in,0)*1000)}:all=1,apad=pad_dur={max(pad_out,0)}"
    subprocess.run([FF,"-v","error","-y","-i",f"full/{take}.mp3","-ss",f"{cin:.3f}","-to",f"{cout:.3f}","-af",af,
                    "-c:a","libmp3lame","-b:a","192k",f"th/v2/{k}.mp3"],check=True)
    n=len(r["line"].split())
    out[k]=dict(line=r["line"],first_word=st,last_word=en,cut_in=round(cin,3),cut_out=round(cout,3),pad_in=max(pad_in,0),pad_out=max(pad_out,0),
                speech_s=round(en-st,2),wpm=round(n/(en-st)*60),heard=" ".join(w for _,_,w in W[i:j+1]))
json.dump(out,open("th/v2/split.json","w"),indent=1)
print("matched",len(s2h),"/",len(sw))
for k,v in out.items(): print(k,v["speech_s"],v["wpm"],"wpm","pad",v["pad_in"],v["pad_out"],"|",v["heard"])
