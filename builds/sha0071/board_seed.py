import json, time, os
now=int(time.time()*1000)
A={"SHEET-PAULA":"109a6a94b7277e1ad0f220f119a4a0a8","SHEET-ROBIN":"fa7f917409de1f8b6da857a91afbae64","LOC":"cce85ff521634cd483e91fbdd8fa3fc5",
"MASTER":"f034c12dd0e58ad5c8ecfe19b7b440bc","PAULA-OTS":"f637a13f27f4280c5f4def7105f508b7","ROBIN-OTS":"8d91e2bbd12063e9f2667442aa692191",
"INS-v1":"da4aa41ecb2a88603175a439a8488f11","INS-v2":"46063a4cee36ad35ae9e5ea4b645463b","RLOW-v1":"7db5c79fbdeb2bbf129dea727883321b","RLOW":"769e4e51cded4c597a89a2e632ccf1e1",
"PMCU-v1":"2f928b01de91912fefb3db884146a62e","PMCU":"77babd2d0c332eb253fc21309eed462b","VP":"6ef252b470ffd6698406dd0f83320670","VR":"882638876a006ddce1bef41b3acbe1a0"}
H="Higgsfield"
def img(asset, prompt, model, vers=None, status="confirmed", fault=None, credits=2):
    d={"imageAsset":asset,"imageType":"image/png","imagePrompt":prompt,"imageModel":model,"imageConnector":H,"imageCredits":credits,"imageRes":"1536×2752","imageAt":now,"imageStatus":status}
    if vers: d["imageVersions"]=vers; d["imageRegens"]=len(vers)-1
    if fault: d["imageFault"]=fault
    return d
B="beats/"
rd=lambda f: open(B+f).read() if os.path.exists(B+f) else ""
out={}
out[("builds","sha0071")]={"name":"SHA0071 · Energy — Scene 1 (first ~30s)","product":"KST Collagen Peptide Serum (koreanskintherapy.com)","mode":"Mode 4 · Realistic Film","format":"Film VSL · Scene 1 hook excerpt","run":"Automatic","aspect":"9:16","kind":"film","talkingHeads":False,
 "voices":[{"id":"PAULA","name":"Paula (58)","needed":True,"status":"locked","voice":"Seedance neutral master · low alto 144 Hz"},{"id":"ROBIN","name":"Robin (48)","needed":True,"status":"locked","voice":"Seedance neutral master · mid 180 Hz"}],
 "balances":{"Higgsfield":4795,"Kling (unused this run)":4864,"Kie (unused this run)":21523},"balancesAt":"2026-09-27 08:40 UTC","updatedAt":now}
def gen(beat, **k):
    d={"build":"sha0071","beat":beat,"updatedAt":now}; d.update(k); out[("generations","sha0071__"+beat)]=d
gen("SHEET-PAULA",stage="cast",act="Cast",title="Paula — character sheet (from supplied talent photo)",status="use",**img(A["SHEET-PAULA"],rd("SHEET-PAULA.t2i.txt"),"gpt_image_2_5 sunburst · high · 2k",credits=6))
gen("SHEET-ROBIN",stage="cast",act="Cast",title="Robin — character sheet (from supplied talent photo)",status="use",**img(A["SHEET-ROBIN"],rd("SHEET-ROBIN.t2i.txt"),"gpt_image_2_5 sunburst · high · 2k",credits=6))
gen("LOC-CORRIDOR",stage="locations",act="Locations",title="Upper-floor corridor outside the glass meeting room",status="use",**img(A["LOC"],rd("LOC-CORRIDOR.t2i.txt"),"gpt_image_2_5 sunburst · high · 2k",credits=6))
for c,a,l in (("PAULA",A["VP"],"I was at my desk by seven every morning in this building for twenty six years."),("ROBIN",A["VR"],"The operations role. Six weeks Thursday. Same building. They want you to start on the sixth.")):
    gen("VOICE-"+c,stage="voice",act="Voice",kind="audio",title=f"{c.title()} — neutral voice master (§24I, untouched)",line=l,status="use",videoAsset=a,videoType="video/mp4",prompt=rd(f"VOICE-{c}.seedance.txt"),model="seedance_2_5 · omni_reference · 720p",videoConnector=H,credits=70,duration=10,videoAt=now)
act=json.load(open("act_map.json")); lines={x["beat"]:x for x in act}
FR={"F-MASTER":(A["MASTER"],"SC01-F-MASTER.t2i.txt",None),"F-PAULA-OTS":(A["PAULA-OTS"],"SC01-F-PAULA-OTS.t2i.txt",None),"F-ROBIN-OTS":(A["ROBIN-OTS"],"SC01-F-ROBIN-OTS.t2i.txt",None),
 "F-ROBIN-LOW":(A["RLOW"],"SC01-F-ROBIN-LOW.v2.t2i.txt",[{"v":1,"asset":A["RLOW-v1"],"type":"image/png","model":"nano_banana_2","connector":H,"credits":2,"at":now,"note":""},{"v":2,"asset":A["RLOW"],"type":"image/png","model":"nano_banana_2","connector":H,"credits":2,"at":now,"note":"Q2: returned the master composition, not a low MCU → Robin frame first, 'new camera position'"}]),
 "F-PAULA-MCU":(A["PMCU"],"SC01-F-PAULA-MCU.v2.t2i.txt",[{"v":1,"asset":A["PMCU-v1"],"type":"image/png","model":"nano_banana_2","connector":H,"credits":2,"at":now,"note":""},{"v":2,"asset":A["PMCU"],"type":"image/png","model":"nano_banana_2","connector":H,"credits":2,"at":now,"note":"Q4: lift behind her flipped the geography → approved reverse attached, lift behind camera"}]),
 "F-INS-BADGE":(A["INS-v2"],"SC01-F-INS-BADGE.v2.t2i.txt",[{"v":1,"asset":A["INS-v1"],"type":"image/png","model":"nano_banana_2","connector":H,"credits":2,"at":now,"note":""},{"v":2,"asset":A["INS-v2"],"type":"image/png","model":"nano_banana_2","connector":H,"credits":2,"at":now,"note":"Q4: read as seated → restated standing"}]),
 "F-PAULA-CU":(None,"SC01-F-PAULA-CU.t2i.txt",None)}
clips=json.load(open("clips.json"))
for b,x in lines.items():
    f=x["frame"]; a,pf,vers=FR[f]
    d=dict(stage="hooks",act="Hook 1",title=f"{x['scale']} · {x['height']}/{x['side']} · {x.get('speaker') or 'insert'}",line=x.get("line") or "",duration=x["duration"],model="seedance_2_5 · omni_reference · 720p",videoConnector=H)
    if b in clips: d["prompt"]=clips[b]["prompt"]
    if a:
        st="confirmed"; fault=None
        if f=="F-INS-BADGE": st="regenerate"; fault="Q4: still reads as seated (a lap) → lift the folder to chest height, no legs in frame"
        d.update(img(a,rd(pf),"nano_banana_2 (sent as nano_banana_pro)",vers=vers,status=st,fault=fault))
        d["status"]="regenerate" if st=="regenerate" else ("ready" if b in clips else "planned")
    else:
        d.update({"imagePrompt":rd(pf),"imageModel":"nano_banana_pro","imageStatus":"generating","status":"generating"})
    gen(b,**d)
docs_abs={"title":"Absorption Sheet","step":1,"order":1,"build":"sha0071","source":"Drive intake + 2 inspo films","updatedAt":now,"confirmed":True,
 "summary":[{"label":"Length","value":"This run: the first ~30s of the script — Scene 1, up to Paula's \"Energy.\" (about 33s)"},{"label":"Pace","value":"Unhurried. Shots hold 3–9 seconds; the quiet lines get their own shot"},{"label":"Voice","value":"No narrator here — two women talking; each has her own fixed voice"},{"label":"On screen","value":"A real-looking short film: an office corridor, Paula (58) and Robin the recruiter"},{"label":"Opening","value":"Starts on dialogue at 0:00 — no music, no title card"},{"label":"Ending","value":"Paula repeats one word, \"Energy.\", on her tightest close-up"},{"label":"We do better","value":"Every shot built from one master frame: same light, same colours, same props"},{"label":"We leave out","value":"The product — it doesn't appear until later scenes"}],
 "sections":[{"title":"Inspo — what it does","md":"| Instrument | Reading |\n|---|---|\n| Primary inspo | 408s, 9:16 720×1280, 46 shots, mean shot 8.9s |\n| Secondary inspo | 504s, 9:16, 101 shots, mean shot 5.0s |\n| Edit grammar | full-frame only; OTS two-shots and MCU singles; small white lower-centre captions, one line |\n| Light | motivated window / practical key, a shadow side on every face, cool interiors |"},
 {"title":"Scope of this run","md":"User: *MAKE THE FIRST 30 SECONDS OF THE SCRIPT ONLY.* The nearest clean line to 30s is Paula's **\"Energy.\"** (Scene 1, line 8). Estimated at ~33s. Lines 9–10 and scenes 2–12 are not built."},
 {"title":"Film Look Sheet","md":"| Field | Value |\n|---|---|\n| Genre | Restrained American workplace drama about dignity and age |\n| Camera | ARRI Alexa 35, Super 35, Cooke S4/i · 25mm wide, 40mm MCU, 50mm CU, 65mm insert · T2–T4 · 24fps, 180° |\n| Light | Overcast daylight through the meeting-room glass (key), hard cool fluorescent top light; 3:1 |\n| Palette | Cool greys, off-white, glass and aluminium; charcoal (Paula), navy/ivory (Robin); warm accents only the buff folder and the red VISITOR band |\n| Grade (edit only) | Cold, fluorescent for the wound — cool shadows, low saturation |\n| Texture | Soft roll-off, no halation, Cooke edge softness; fine grain in the edit |\n| Motion | F2 locked; one F1 push on Paula for the verdict |\n| Performance | Restrained, still; Paula never plays triumph |\n| Sound | Dialogue only in clips; corridor room tone; no music intro, a low cello under the verdict, silence on \"Energy.\" |"}]}
out[("docs","absorption")]=docs_abs
rows="| Beat | Act | Type | Subject | Framing | Phrase |\n|---|---|---|---|---|---|\n"+"\n".join(f"| {x['beat']} | Hook 1 | {x['type']} · {x.get('playing') or 'insert'} | {x['subject']} | {x['scale']} · {x['height']}/{x['side']} · {x['rig']} | {x.get('line') or '(badge insert)'} |" for x in act)
out[("docs","actmap")]={"title":"Act map — SC-01","step":5,"order":2,"build":"sha0071","source":"act_map.json","updatedAt":now,"sections":[{"title":"Shot list","md":rows}]}
w=[]
for (c,i),d in out.items():
    fn=f"board/{c}__{i}.json"; json.dump(d,open(fn,"w")); w.append({"op":"set","collection":c,"doc_id":i,"file_path":os.path.abspath(fn)})
json.dump(w,open("board/writes.json","w"),indent=0); print(len(w))
