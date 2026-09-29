"""§22U step 12 — align the script's words to the VO master's word timestamps and cut one audio segment per TH beat."""
import json,re,difflib,subprocess,imageio_ffmpeg,sys
FF=imageio_ffmpeg.get_ffmpeg_exe()
take=sys.argv[1] if len(sys.argv)>1 else "T1"
segs=json.load(open(f"cut/VO_{take}.words.json"))
W=[(s,e,w) for sg in segs for (s,e,w) in sg["w"]]
norm=lambda t:re.sub(r"[^a-z0-9]","",t.lower())
hw=[norm(w) for _,_,w in W]
rows=json.load(open("../work/actmap_rows.json"))
# script word index per row (dedupe consecutive repeated lines — cutaways over a TH share its words)
sw=[];rowspan={};prev=None
for r in rows:
    if not r["line"]: continue
    if r["line"]==prev: rowspan[r["beat"]]=rowspan[last]; continue
    toks=[norm(t) for t in r["line"].split() if norm(t)]
    rowspan[r["beat"]]=(len(sw),len(sw)+len(toks)); sw+=toks; prev=r["line"]; last=r["beat"]
m=difflib.SequenceMatcher(None,sw,hw,autojunk=False)
s2h={}
for a,b,n in m.get_matching_blocks():
    for k in range(n): s2h[a+k]=b+k
def t_of(i,side):
    j=i
    while j not in s2h: j+= (1 if side=="s" else -1)
    return W[s2h[j]][0] if side=="s" else W[s2h[j]][1]
out={}
for r in rows:
    a,b=rowspan[r["beat"]]
    st,en=t_of(a,"s"),t_of(b-1,"e")
    out[r["beat"]]={"type":r["type"],"start":round(st,3),"end":round(en,3),"line":r["line"]}
# TH segments: cut between words (midpoint of the gaps around the segment)
ends=[e for _,e,_ in W]; starts=[s for s,_,_ in W]
import bisect
for k,v in out.items():
    if v["type"]!="TH": continue
    i=bisect.bisect_left(starts,v["start"]-1e-3); j=bisect.bisect_right(ends,v["end"]+1e-3)-1
    a=(ends[i-1]+starts[i])/2 if i>0 else 0.0
    b=(ends[j]+starts[j+1])/2 if j+1<len(starts) else ends[j]+0.2
    v.update(cut_in=round(a,3),cut_out=round(b,3))
    subprocess.run([FF,"-v","error","-y","-i",f"cut/VO_{take}.mp3","-ss",str(a),"-to",str(b),"-c:a","libmp3lame","-b:a","192k",f"th/{k}.mp3"],check=True)
json.dump(out,open(f"cut/VO_{take}.beats.json","w"),indent=1)
print("matched",len(s2h),"/",len(sw))
for k,v in out.items():
    if v["type"]=="TH": print(k,v["cut_in"],v["cut_out"],round(v["cut_out"]-v["cut_in"],2),v["line"][:60])
