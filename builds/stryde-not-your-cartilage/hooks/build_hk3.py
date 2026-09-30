import re,sys,json,pathlib
H=pathlib.Path('/home/user/global-manual-ai/builds/stryde-not-your-cartilage/hooks'); B=H.parent; ROOT=B.parents[1]
T=(ROOT/"standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m=re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```"%re.escape(i),T,re.S); return m.group(1).strip()
ROWS={r["beat"]:r for r in json.loads((B/"work/actmap.json").read_text())["rows"]}
HEIGHT={"overhead":"an overhead camera looking straight down","high":"a high camera looking down","eye":"an eye-level camera","low":"a low camera close to the floor looking up","ground":"a camera at ground level"}
SIDE={"front":"the front","three-quarter":"three-quarter","profile":"the side, in profile","ots":"over the shoulder"}
def angle(b,subj,fg=""):
    r=ROWS[b]; return S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]",HEIGHT[r["height"]]).replace("[SIDE]",SIDE[r["side"]]).replace("[SUBJECT]",subj).replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]",fg)
def focus(plane,deep=False):
    return S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]",plane).replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]","everything from near to far stays sharp" if deep else "the room behind falls to a soft, recognisable shape")
def light(src,subj,side,q,face=True):
    s=S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]",src).replace("[SUBJECT]",subj).replace("[SCREEN SIDE]",side).replace("[TIME-OF-DAY QUALITY and the act's light state]",q)
    s=s.replace("toward [SIDE]",f"toward the {side}")
    if not face: s=s.replace(f"so the face has a lit side toward the {side} and a softer shadow side, with a small catchlight in the eyes",f"so it has a lit side toward the {side} and a softer shadow side")
    return s
def colour(lc,k,sc,who,wc,ac,sat):
    return S("COLOUR-KEY").replace(", exactly as in the attached master frame","").replace("[LIGHT COLOUR]",lc).replace("[KELVIN]",str(k)).replace("[SET COLOURS]",sc).replace("[WHO]",who).replace("[WARDROBE COLOURS]",wc).replace("[ACCENT]","the accent is "+ac).replace("[SATURATION AND CONTRAST IN CAMERA]",sat)
NEG_BASE=("no readable text, no logos, no AI face, no plastic skin, no waxy skin, no extra fingers, no fused fingers, no polished render, no advertising image, "
          "no studio lighting, no vignette, no glowing skin, no light from nowhere, no shadows falling in two directions, no lens flare")
def photo(parts,avoid): return "\n\n".join([S("CAM-LOCK")]+[p for p in parts if p]+[S("CAP-FILE"),"AVOID: "+avoid+", "+NEG_BASE])
HK3=photo([
 "A snapshot in a hospital consultant's room. A knee X-ray film is clipped to the wall light box, lit from behind: a plain greyscale X-ray of one knee seen from the front, "
 "the femur above and the tibia below, the gap between them visibly narrowed on the inner side where the cartilage has worn thin, the kneecap a faint oval over the joint. "
 "The film carries no writing, no letters, no numbers, no markers and no labels of any kind. A consultant's right forefinger touches the film and traces the narrowed gap; "
 "her hand is a white woman's hand of about fifty, short unpainted nails, a plain watch on the wrist, the cuff of a navy dress at the wrist. "
 "Her navy shoulder and the back of her short dark hair are soft and out of focus in the near foreground at the left of the frame; her face is not seen.",
 "THE SAME ROOM exactly as in the attached location plate — the wall-mounted X-ray light box on the far wall, the pale grey-blue walls, the window with its vertical blind "
 "on the left-hand wall — seen close, the light box filling most of the frame.",
 angle("HK3-01","the consultant, towards the lit X-ray",", looking past her navy shoulder, soft in the near foreground"), focus("her fingertip on the X-ray"),
 light("the window on the consulting room's left-hand wall","the light box and her hand","left","overcast morning daylight, the light box glowing an even cool white",face=False),
 colour("overcast morning daylight",6500,"pale grey-blue walls, the cool white light box, the grey X-ray","she","navy","the bright white of the lit film","cool, true to life")],
 "no text on the X-ray, no letters, no numbers, no markers, no labels, no arrows, no ruler, no annotations, no screen, no computer monitor in focus, no face, no white coat, "
 "no stethoscope, no knee strap, no brace, no wrong finger count, no malformed hands")
assert "[" not in HK3, HK3[HK3.index("["):][:120]
(H/"HK3-01.image.prompt.txt").write_text(HK3); print(len(HK3))
