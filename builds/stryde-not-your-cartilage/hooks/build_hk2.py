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
FOLAKE=("THE SAME WOMAN as in the attached character sheet — a Black British woman of Nigerian heritage, sixty-six: a wide face with very high prominent cheekbones "
        "tapering to a narrow pointed chin, narrow deep-set dark eyes, a broad flat nose, a wide mouth with a full lower lip, the small raised keloid bump on the top rim "
        "of her right ear, long thin grey-and-black box braids tied back in a low ponytail, slim and wiry — her real age showing, bare face, no makeup.")
HK2=photo([
 S("FRAME-SCALE").replace("[SCALE]","about three quarters"),
 "A snapshot of an ordinary bad-knee morning. She sits in her high-backed burgundy armchair beside the window, a mug of tea held in her left hand on the chair's "
 "wooden arm; her right hand rests on her right knee, fingers pressed a little into it as she rubs it once, and she looks out of the window, tired, not smiling. "+FOLAKE+
 " She wears a long burnt-orange knitted cardigan over a black long-sleeved jersey top, charcoal jersey trousers and maroon slippers. "
 "No strap, no brace, no support on her knee.",
 S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]","the magnolia woodchip walls, plain white woodwork and the mid-oak laminate")+
 " THE SAME LOUNGE exactly as in the attached location plate — the burgundy armchair with its crocheted cream cushion side-on to the wide east window with net curtains and "
 "gold curtains tied back, the glass-topped coffee table on the cream rug, the brass standard lamp switched off, the rubber plant by the window.",
 angle("HK2-01","her in the armchair"), focus("the nearest eye of Folake"),
 light("the wide window on the lounge's east wall","her","left","bright morning daylight through the nets, the sun not yet round"),
 colour("soft bright morning daylight through net curtains",5600,"magnolia walls, the burgundy armchair, the cream rug","she","burnt orange and black","her maroon slippers","natural, a little flat"),
 S("SKIN-B1")],
 "no knee strap, no knee brace, no sleeve, no support on her leg, no smile, no looking at the camera, no posed portrait, no hair loose over her shoulders, no glasses, no jewellery")
assert "[" not in HK2, HK2[HK2.index("["):][:120]
(H/"HK2-01.image.prompt.txt").write_text(HK2); print(len(HK2))
