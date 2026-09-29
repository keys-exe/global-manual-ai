import sys, json, re
sys.path.insert(0,'.'); sys.path.insert(0,'../build'); sys.path.insert(0,'/home/user/global-manual-ai/products/stryde')
from strings import S
import stryde_product_sheet as P
from scenes_b2 import SC
import voice, locs, extras
from scenes import WARD
from data import LOOK_STRING

FOCAL={"WIDE":24,"FULL":35,"MEDIUM":35,"MCU":35,"TWO-SHOT":35,"CU":50,"ECU":85,"INSERT":85}
SCALE={"WIDE":"no more than half","FULL":"about two thirds","MEDIUM":"about three quarters, with a band of room above",
 "MCU":"head and chest, with the room readable to one side","CU":"the face at about half the frame width","TWO-SHOT":"two people at medium close-up, the near shoulder soft at the edge",
 "ECU":"detail only, never a whole face","INSERT":"detail only, never a whole face"}
SCALE_NAME={"WIDE":"wide establishing shot","FULL":"full shot, head to toe","MEDIUM":"medium shot, waist up","MCU":"medium close-up, chest up","CU":"close-up, head and shoulders","TWO-SHOT":"two-shot","ECU":"extreme close-up","INSERT":"insert"}
RIGWORD={"F1":"a dolly","F2":"a locked tripod","F3":"an operator's shoulder","F4":"a slider","F5":"a stabiliser"}
AGE={"MARGARET":"fine forehead lines, soft jowls, a small healed red scar across the bridge of the nose, pink cheeks, crepey skin at the neck",
 "BARBARA":"deep crow's feet, deeply lined weathered skin, a raised brown mole on the left side of the neck, sun-freckled cheeks",
 "FRANK":"heavy jowls, a ruddy bulbous nose, brown age spots at the temple, bristling white eyebrows",
 "SARAH":"fine lines at the eyes and forehead, a small raised blemish at the top of the forehead, grey threads at the parting",
 "EMILY":"light freckles across the nose and cheeks, a small crescent scar under the right eye",
 "DOCTOR":"a deep vertical crease between the brows, stubble greying at the chin, lines at the eyes"}
IDENT={"MARGARET":"Margaret, seventy-one: silver-white chin-length bob with a side part, hazel eyes, broad round face, heavy-set with rounded shoulders",
 "BARBARA":"Barbara, seventy-four: short spiky white crop, pale blue eyes, broad square weathered face, stocky and heavy",
 "FRANK":"Frank, seventy-six: swept-back white hair long at the collar, bristling white brows, grey-blue eyes, heavy jowled face, a soft belly, slight stoop",
 "SARAH":"Sarah, about fifty: dark brown jaw-length bob with grey threads at the parting, brown eyes, long narrow face, lean",
 "EMILY":"Emily, about thirty: long straight mid-brown hair with a centre part, hazel-green eyes, freckled, slim",
 "DOCTOR":"the doctor, late forties: dark curly hair greying at the temples, brown eyes, stubble, lean long face"}
LOCN={l['id']:l for l in locs.LOCS}
AUD={a[0]:a[2] for a in extras.AUDIO}
PLATE={"L-KIT":"PLATE-KITCHEN","L-HALL":"PLATE-HALL (property plate)","L-STAIR":"PLATE-LANDING","L-LIV":"PLATE-LIVING","L-GP":"PLATE-GP"}
SIG={"signature glasses":"reading glasses on a bead chain","signature beads":"a purple glass-bead necklace","signature hoops":"small gold hoop earrings"}
def garment(x):
    x=x.replace(" (sheet)","").replace(" (signature)","")
    for k,v in SIG.items(): x=x.replace(k,v)
    p=[t.strip() for t in x.split(",")]
    if len(p)>=2 and not any(s in p[0] for s in ("glasses","necklace","earrings","lanyard","pearl")):
        g=p[1]+" "+p[0]
        return g+(", "+", ".join(p[2:]) if len(p)>2 else "")
    return x
def ward(day,who):
    for w in WARD:
        if w[0]==day and w[1].upper()==who:
            parts=[garment(x) for x in w[2:8] if x and x!='—' and not x.startswith('(')]
            return "Wearing "+"; ".join(parts)+"; the palette "+w[8].replace("/"," and ")+"."
    return ""
PROPSHELL=S["PROP-SHELL"]
shell=dict(locs.PROPERTY)["2 · Shell"]
PROP_REF=S["PROP-REF"].replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]","cream walls, white ogee skirting, sapele doors with brass lever handles, artex swirl ceilings, the sage-green floral carpet")
PROP_SHELL=("Shared through the whole house and identical in every room: cream emulsion walls, white ogee skirting about fifteen centimetres high, plain white architrave, sapele-veneer flush internal doors with brass lever handles, artex swirl ceilings, sage-green carpet with a small cream-and-rose floral motif changing to beige vinyl tile at the kitchen threshold, white steel panel radiators, white plastic switches and sockets. "
 "One age of building, one decade of decoration, one standard of upkeep throughout — no room newer, cleaner or better kept than the rest.")
VIEW={"L-KIT":"the back lawn, the rotary washing line and the close-board fence with neighbouring roofs beyond",
      "L-LIV":"the quiet residential street softened through the net curtains"}

def cam(scale,rig): return S["CAM-FILM"].replace("[CAMERA]","a large-format digital cinema camera").replace("[LENS FAMILY]","spherical prime lenses").replace("[FOCAL]",str(FOCAL[scale])).replace("[STOP]","T2.0").replace("[RIG]",RIGWORD[rig])
def filmframe(scale): return S["FILM-FRAME"].replace("[SHOT SCALE]",SCALE_NAME[scale]).replace("[SCALE]",SCALE[scale])
def light(sc,side): return S["LIGHT-FILM"].replace("[MOTIVATION]",sc["light"].upper()).replace("[SIDE]",side.upper()).replace("[KEY QUALITY]","soft and broad").replace("[RATIO]","2:1" if sc["day"] in ("D4","D5","D6","D7") else "3:1")
CAPF=S["CAP-FILM"].replace("[HIGHLIGHT BEHAVIOUR]","rolling off softly, with a faint halation where a window or practical sits in frame")
def product_clause(kind, side):
    if not kind: return ""
    if kind in ("reveal-B","reveal-M","worn-M","worn-B"):
        lock=P.fill(P.PLACE_BENT if kind.startswith("reveal") else P.PLACE_LOCK_C, side=side)
        return P.fill(P.REF_PROD, side=side)+" "+lock+" "+S["IFACE-C"]
    if kind in ("worn-M-small",):
        return "The strap is on her "+side+" leg under the kneecap, small in frame, black shell with its chrome slides, exactly as in the attached product reference."
    if kind=="palm":
        return P.fill(P.REF_PROD, side="right")+" One single closed strap, whole and correctly formed, held flat in the palm, the band closed and looped, never being threaded or fastened."
    if kind=="lap":
        return "Two straps, each exactly as in the attached product reference image — "+P.fill(P.REF_PROD,side="right").split("—",1)[1].strip().rstrip("—").strip()+" — rest side by side in her lap, closed and whole. This is the two-for-one offer and the only beat with two units."
    return ""
def product_negs(kind, side):
    if not kind: return []
    base=["no second unit","no silicone pad visible","no inner face of the shell visible"]
    if kind in ("reveal-B","reveal-M","worn-M","worn-B"):
        return [P.fill(P.NEG_PLACE,side=side), P.fill(P.NEG_BENT,side=side)]+base
    if kind=="lap": return ["no third unit, no unit worn on the leg in this shot"]
    return base
SIDEOF={"reveal-B":"left","worn-B":"left","reveal-M":"right","worn-M":"right","worn-M-small":"right","palm":"right","lap":"right"}

def attach_frame(sc, f):
    a=[]
    if not f.get("key"): a.append(f"{sc['_master']} (scene master)")
    for w in f["who"]: a.append(f"SHEET-{w}")
    if sc["loc"] in PLATE: a.append(PLATE[sc["loc"]])
    if sc["house"] and sc["loc"]!="L-HALL": a.append("PLATE-HALL (property plate)")
    k=f.get("product")
    if k:
        a.append("PROD-CANONICAL")
        if k in("reveal-B","reveal-M"): a.append("PLACE-BENT")
        if k in("worn-M","worn-B"): a.append("PLACE-FRONT")
    a.append("LOOK-1 (one approved frame from your Scenes 1–3)")
    return a

def t2i(sc, f):
    parts=[cam(f["scale"],f["rig"])]
    if f.get("key"):
        parts.append(S["SCENE-MASTER"].replace("[ID]",sc["_id"]).replace("[LOCATION]","The "+LOCN[sc["loc"]]["name"].lower()).replace("[TIME OF DAY]",sc["time"]).replace("[LIGHT STATE]",sc["light"]).replace("[BLOCKING, in room terms]",sc["blocking"]).replace("[AXIS]",sc["axis"]).replace("[SIDE]",sc["side"]).replace("[PROP STATES]",sc["props"]))
    else:
        who=" and ".join(n.title() if n!="DOCTOR" else "the doctor" for n in f["who"])
        k=S["SCENE-KEY"].replace("[SHOT SCALE]",SCALE_NAME[f["scale"]]).replace("[WHO]",who).replace("[CAMERA POSITION, in action-line terms]",f"the {sc['side']} side of the line, framed on {who}")
        k=k.replace("[WHO IS OFF FRAME and where they are, so this character's eyeline points toward them]", (f"{f['off'][0].upper()+f['off'][1:]} is off frame, and the eyeline points toward them." if f.get("off") else "Nobody else is in frame."))
        parts.append(k)
    parts.append(filmframe(f["scale"]))
    subj=[f["desc"][0].upper()+f["desc"][1:]+"."]
    for w in f["who"]:
        subj.append(IDENT[w]+". "+ward(sc["day"],w))
    parts.append(" ".join(subj))
    kind=f.get("product")
    if kind: parts.append(product_clause(kind, SIDEOF[kind]))
    parts.append(S["BODY-WHOLE"])
    faces=[w for w in f["who"] if w in f.get("emo",{})]
    for w in faces:
        nm=w.title() if w!="DOCTOR" else "the doctor"
        parts.append(S["EMO-SEED"].replace("[NAME]",nm).replace("[the emotional state from the scene's emotion map, written as physical detail: the set of the jaw, where the eyes rest, the tension in the brow and mouth, the breath]",f["emo"][w]))
    if f["scale"] in ("MCU","CU","ECU","TWO-SHOT") and faces:
        parts.append(S["SKIN-A"].replace("[AGE-FEATURES]","; ".join(AGE[w] for w in faces)))
    if sc["house"]:
        parts.append(PROP_REF); parts.append(PROP_SHELL)
    parts.append("Named anchors: "+LOCN[sc["loc"]]["anchors"]+".")
    if sc["loc"]=="L-KIT": parts.append("The kitchen floor is beige vinyl tile with a worn patch, exactly as in the kitchen plate; the sage carpet stops at the hall threshold and never enters the kitchen.")
    if sc["loc"] in VIEW and f["scale"] in ("WIDE","FULL","MCU"):
        parts.append(S["VIEW-OUT"].replace("[WHAT THE PROPERTY'S EXTERIOR SHOWS FROM THIS ROOM'S SIDE, NAMED]",VIEW[sc["loc"]]))
    parts.append(light(sc, "the window side" if sc["loc"] in ("L-KIT","L-LIV","L-GP") else "the landing-window side" if sc["loc"]=="L-STAIR" else "the front-door side"))
    parts.append(LOOK_STRING)
    parts.append(S["PHYS-FRAME-C"])
    parts.append(CAPF)
    negs=[S["NEG-FILM"],S["NEG-SCENECUT"],S["NEG-BODY"],"no film camera, no tripod, no dolly, no microphone, no boom pole, no lights on stands, no film crew or equipment anywhere in frame, no character-sheet panels, no split screen, no text"]
    if sc["loc"]=="L-KIT": negs.append("no carpet in the kitchen, no rug on the kitchen floor")
    if faces: negs+= [S["NEG-SKIN"]]
    if sc["house"]: negs.append(S["NEG-PROP"])
    if not f.get("key"): negs.append(S["NEG-SCENE"])
    negs+=product_negs(kind, SIDEOF.get(kind,"right"))
    if sc["_id"] in ("SC07","SC08","SC09","SC10","SC11") and f["scale"] in ("FULL","WIDE"): negs.append(S["NEG-SUPPORT"])
    parts.append("Avoid: "+", ".join(negs)+".")
    return "\n\n".join(p for p in parts if p)

def manifest(sc, c, frame, pack):
    s=["INGREDIENTS. @image1 is the opening composition: the clip opens on exactly this framing, light and camera position, and nothing in it is re-composed."]
    i=2; imgs=["@image1: "+frame["id"]]
    others=[f for f in sc["frames"] if f["id"]!=frame["id"]][:3]
    if others:
        h=f"@image{i}–@image{i+len(others)-1}" if len(others)>1 else f"@image{i}"
        s.append(f"{h} are this scene: "+", ".join(o['id'] for o in others)+", and they set the room, the light side, the blocking and every prop's position.")
        for o in others: imgs.append(f"@image{i}: {o['id']}"); i+=1
    people=sorted({w for sh in c["shots"] for w in ([sh[2]] if sh[2] else [])}|set(frame["who"])|set(pack.get("extra",[])))
    for w in people:
        if w not in sc["cast"]: continue
        s.append(f"@image{i} is {w.title() if w!='DOCTOR' else 'the doctor'}: face, age, hair and build only, with the wardrobe taken from the scene frames and never from this sheet.")
        imgs.append(f"@image{i}: SHEET-{w}"); i+=1
    if pack.get("product"):
        s.append(f"@image{i} is the product, one object seen from the front, the side and behind, exactly as shown: "+P.fill(P.REF_PROD,side="right").rstrip(" —")+".")
        imgs.append(f"@image{i}: PROD-CANONICAL"); i+=1
    if sc["loc"] in PLATE:
        s.append(f"@image{i} is the room and the house.")
        imgs.append(f"@image{i}: {PLATE[sc['loc']]}"); i+=1
    s.append(f"@image{i} carries the film's look."); imgs.append(f"@image{i}: LOOK-1"); i+=1
    auds=[]; a=1
    for w in [x for x in people if any(sh[2]==x and sh[3] for sh in c["shots"])]:
        nm=w.title() if w!='DOCTOR' else 'the doctor'
        s.append(f"@audio{a} is {nm}'s voice, its timbre, pitch, accent and pace, for every line {nm} speaks; it sets who they sound like, never how they feel in this shot.")
        auds.append(f"@audio{a}: VOICE-{w}"); a+=1
    s.append("These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to.")
    return " ".join(s), imgs, auds

def clip(sc, c):
    frame=next(f for f in sc["frames"] if f["id"]==c["frame"])
    prod=any(f.get("product") for f in [frame]) or any("strap" in (sh[4] or "") or "trouser" in (sh[4] or "") for sh in c["shots"])
    man,imgs,auds=manifest(sc,c,frame,{"product":prod})
    t=0; shots=[]
    spoken=[sh for sh in c["shots"]]
    # allot time: spoken shots by words, silent shots share the rest
    w=[len(sh[3].split()) if sh[3] else 0 for sh in spoken]
    need=[max(2.0, x/2.1+0.8) if x else 0 for x in w]
    silent=[i for i,x in enumerate(w) if not x]
    rest=max(0,c["dur"]-sum(need))
    for i in silent: need[i]=max(2.0, rest/len(silent)) if silent else 0
    scale_f=c["dur"]/sum(need)
    for i,sh in enumerate(spoken):
        d=need[i]*scale_f; a,b=round(t),round(t+d) if i<len(spoken)-1 else c["dur"]; t+=d
        who=sh[2]; nm=(who.title() if who and who!='DOCTOR' else 'the doctor') if who else None
        rig={"F1":"slow dolly push","F2":"locked tripod","F3":"shoulder","F4":"slider","F5":"stabiliser follow"}[sh[1]]
        if sh[3] and sh[0]=="INSERT":
            body=f"{sh[4][0].upper()+sh[4][1:]}; {nm} is heard off screen saying: \"{sh[3]}\""
        elif sh[3]:
            body=f"{nm} says: \"{sh[3]}\" Played {sh[4]}."
        elif sh[4].startswith("LISTEN:"):
            body=S["LISTEN-LINE"].replace("[NAME]",nm).replace("[SPEAKER]","the other speaker").replace("[what lands, on which words, and the one named physical response]",sh[4][7:].strip())
        elif sh[4].startswith("PHONE LISTEN:"):
            body=sh[4][13:].strip()+". Silence on the soundtrack: no voice is generated for the other end of the call."
        else:
            body=sh[4][0].upper()+sh[4][1:]+"."
        shots.append(f"SHOT {i+1}, [{a}s-{b}s]: {SCALE_NAME[sh[0]]}, {rig}, {body}")
    if len(spoken)>1:
        mf=S["MULTI-FILM"]
        head=mf.split("SHOT 1")[0].replace("[N]",str(len(spoken)))
        tail="The lines land on each other in the rhythm this scene needs: "+("a beat held on the listener before each reply, never overlapping." )+" Each cut lands on a completed line, action or reaction. The eyelines match across every reverse. Nobody looks into the lens."
        prose=head+" ".join(shots)+" "+tail
    else:
        prose="One continuous shot with no cuts. "+shots[0].split(": ",1)[1]
    parts=[man, prose]
    for w in [x for x in sc["cast"] if any(sh[2]==x and sh[3] for sh in c["shots"])]:
        parts.append(f"{w.title() if w!='DOCTOR' else 'The doctor'}'s voice: "+voice.VOICE[w])
    parts.append(S["HOLD-C"].replace(" One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning.",""))
    parts.append(S["HOLD-HC"])
    if prod: parts.append(P.HOLD_PC)
    parts.append(S["PHYS-MOTION-C"])
    for r in sorted({sh[1] for sh in c["shots"]}):
        parts.append(S["RIG-"+r].replace("[DISTANCE]","30"))
    parts.append(S["INHERIT-FILM"])
    parts.append(S["AUD-FILM"]+" "+AUD[sc["loc"]])
    negs=[S["NEG-WARP-C"],S["NEG-SCENECUT"],S["NEG-DRAMA"],S["NEG-AUD"],"no microphone in frame, no boom pole, no boom microphone or furry windshield visible anywhere in the frame, no film crew or equipment in frame, no generated music, no subtitles, no text on screen, no letterbox bars, no slow motion, no speed ramp, no actor looking into the lens"]
    if prod: negs+=["no second unit"+("" if sc["_id"]!="SC11" else " beyond the two in her lap"),"no strap sliding, no strap rotating, no strap changing shape","no silicone pad visible"]
    if sc["_id"] in ("SC07","SC08","SC09","SC10","SC11"): negs.append(S["NEG-SUPPORT"])
    parts.append("Avoid: "+", ".join(negs)+".")
    return "\n\n".join(parts), imgs, auds

OUT=[]
for sid,sc in SC.items():
    sc["_id"]=sid; sc["_master"]=next(f["id"] for f in sc["frames"] if f.get("key"))
    frames=[dict(id=f["id"],kind="frame",scale=f["scale"],model="nano_banana_pro",meta="Higgsfield · nano_banana_pro · 9:16 · 2k · references as image_references",attach=attach_frame(sc,f),prompt=t2i(sc,f),desc=f["desc"]) for f in sc["frames"]]
    clips=[]
    for c in sc["clips"]:
        p,imgs,auds=clip(sc,c)
        lines=[f'{(sh[2] or "").title()}: "{sh[3]}"' for sh in c["shots"] if sh[3]]
        clips.append(dict(id=c["id"],kind="clip",meta=f"kie.ai · Seedance 2.5 · reference_image_urls + reference_audio_urls · 720p · 9:16 · {c['dur']} s",images=imgs,audios=auds,prompt=p,lines=lines,shots=len(c["shots"]),opening=c["frame"]))
    OUT.append(dict(id=sid,title=sc["title"],day=sc["day"],loc=LOCN[sc["loc"]]["name"],frames=frames,clips=clips))
json.dump(OUT,open("b2.json","w"),indent=1,ensure_ascii=False)
import statistics
fl=[len(f["prompt"]) for s in OUT for f in s["frames"]]; cl=[len(c["prompt"]) for s in OUT for c in s["clips"]]
print(len(fl),"frames",min(fl),max(fl),int(statistics.mean(fl)),"|",len(cl),"clips",min(cl),max(cl),int(statistics.mean(cl)))
print(max(len(c["images"])+len(c["audios"]) for s in OUT for c in s["clips"]),"max files")
