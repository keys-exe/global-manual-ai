#!/usr/bin/env python3
"""Step 6 hook frames v2 — the user's Fix 2026-09-29: "I WANT A HOOK THAT WILL SELL I DONT WANT THIS NORMAL LOOKING HOOKS".
Same spoken lines (verbatim, §22U); new pictures built as pattern interrupts (§31, §30B run grammar: escalation, the strange image the line names):
  HK1-01a  home-camera footage (§22E CCTV-FULL, CCTV-CORNER): she comes down her stairs BACKWARDS, both hands on the banister (P-D1, the before)
  HK1-02a  the drawer too full to shut — braces spill out onto the tiles as she shoves one more in (caught mid-spill)
  HK2-02a  the doctor tears the blank top sheet off his prescription pad and crumples it in his fist
  HK3-01a  his desk buried under knee X-rays and scan envelopes; he drops one more on the heap
Helpers and shared strings come from build_hooks.py (v1), read up to its beat table."""
import re, json, pathlib
here = pathlib.Path(__file__).parent
src = (here / "build_hooks.py").read_text()
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(here / "build_hooks.py"))), "build_hooks.py", "exec"))

def dedupe(*lists):
    seen, out = set(), []
    for c in (c.strip() for l in lists for c in l.split(",")):
        if c not in seen: seen.add(c); out.append(c)
    return ", ".join(out)
P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "burgundy fleece-lined slippers, and reading glasses on a cord round her neck.")
B = {}
# HK1-01a — CCTV-FULL, hall corner mount; P-D1; backwards descent, both hands on the rail, one step caught mid-lowering; product absent (six weeks ago)
B["HK1-01a"] = dict(model="nano_banana_2", refs=["P0-PROP-P v2", "P-PATIENT"], body=[
  S("CCTV-CORNER"), S("MOUNT-GEOM"), S("CCTV-FRAME"),
  PROPREF + " The hall and the wide straight staircase of the attached property photograph, seen from a home security camera fixed high in the corner of the hall by the front door: "
  "the stairs rise away along the left-hand wall, the dark turned banister on the open right side, the patterned runner with brass rods on every tread, the telephone table at the foot.",
  "A white British woman of sixty-nine, short, petite and slightly stooped, chestnut-dyed chin-length hair with silver roots, as in the attached reference sheet — small in the frame, off to one side. "
  + P_D1 + " She is halfway down her own stairs COMING DOWN BACKWARDS, facing the steps and the wall, her back to the hall, both hands clamped on the banister rail one above the other, "
  "her body leaning in towards the rail, caught in the middle of one careful step: her weight on her left foot on the upper tread, her right foot reaching down behind her, feeling for the tread below. "
  "The top of her head and her shoulders are the clearest parts of her; her face is turned down to her feet and away from the camera.",
  S("MOUNT-PERSON") + " Here she is backing down towards the camera, so it sees her from above and BEHIND: the back of her head, her shoulders and her back, her hands on the rail ahead of her.",
  "The room's own light: a grey morning, the stained-glass panel in the front door below the camera throwing a pale wash down the runner and the lower stairs, the landing window at the top a flat blown-out white, the far end of the hall muddy and dark.",
  S("CAP-CCTV"),
  "AVOID: " + ", ".join([dedupe(S("NEG-CCTV"), S("NEG-MOUNT")), pick("NEG-M1", "no extra fingers", "no fused fingers", "no melted hands", "no deformed limbs", "no CGI look"),
                         "no walking forwards, no facing the camera, no face towards the lens, no one hand free, no stick, no second person, no product, no strap, no brace on the knee, no fall, no lying on the stairs", NOTEXT])])

# HK1-02a — P-D1 hand, high · front · CU; the spill (run grammar: escalation); product absent
B["HK1-02a"] = dict(model="nano_banana_2", refs=["P2-P-KITCHEN v2", "P-PATIENT"], body=[S("CAM-LOCK"),
  angle("high", "the front", "the open dresser drawer and her hand"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph: the old pine Welsh dresser beside the pine table, its top drawer pulled open, the red-and-black quarry tiles below.",
  "A snapshot from a phone held above the drawer by someone standing beside the dresser, looking down, not looking at the screen. "
  "The drawer is stuffed so far past full that it cannot shut: a mountain of old knee supports — black stretchy sleeves, beige wraps with loose velcro tabs, grey neoprene sleeves, a hinged brace with metal side bars, white tubular bandages, "
  "all worn, blank and plain, no brand, no writing — heaped above the sides and bulging over the front edge. "
  "Her right hand — the hand of a woman of sixty-nine, thin skin, soft lines across the knuckles, a plain gold wedding band, the cuff of an oatmeal cable-knit cardigan over a cream roll-neck at the wrist — "
  "is jammed flat on top of the heap, shoving one more grey hinged knee brace down into it, and the pile is giving way: "
  "caught in the moment it spills, two sleeves and a beige wrap already tumbling out over the drawer's front edge in mid-air, falling towards the quarry tiles below, one more slipping after them. "
  "The drawer, the heap, the whole hand and the falling supports are all in frame with room below for them to fall into.",
  light("The window over the sink on the room's west wall", "the drawer and her hand", "right", "flat overcast daylight, the grey, cooler light of the problem days", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no strap product, no small padded strap, no knee strap with a silicone pad, no new or packaged supports, no hand cut off at the frame edge, "
                         "no more than one hand, no drawer closed, no tidy folded pile, no motion blur smearing the hand", NOTEXT])])

# HK2-02a — D hands, high · three-quarter · CU; tears the blank top sheet off the pad and crumples it; hands; key L 6500K
B["HK2-02a"] = dict(model="nano_banana_2", refs=["P3-D-CONSULT", "D-VOICE-IMG v2"], body=[S("CAM-LOCK"),
  angle("high", "a three-quarter angle", "his hands over the desk"),
  focus("the hands and what they hold", "the room behind falls to a soft, recognisable shape"),
  "IN THE SAME ROOM as the attached consulting-room photograph: the light-wood desk, the closed laptop to one side, the white plastic knee model, the pale grey wall soft behind.",
  "A snapshot from a phone held at his shoulder by someone standing beside his chair on his side of the desk, looking down, not looking at the screen. "
  "The doctor's two hands — a stocky man's hands of fifty-four, fair freckled skin with reddish hairs on the backs, short clean nails, a plain steel watch on the left wrist, "
  "the white cuffs of his doctor's coat over pale blue shirt cuffs — hold a small white prescription pad just above the desk: his left hand pins the pad, "
  "his right hand has torn the top sheet halfway off, the blank sheet — nothing written or printed on it — creased and ripping away along the gummed edge, caught in the middle of the tear. "
  "A cheap blue biro lies on the desk beside the pad. Both hands, the pad and the tearing sheet sit well inside the frame.",
  light("The consulting-room window on the room's north wall", "the desk and his hands", "left", "steady overcast daylight", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no writing on the sheet, no printed form, no drug names, no pharmacy logo, no pills, no pen in the hand, no hand cut off at the frame edge, "
                         "no bare forearm, no coat missing, no angry gesture", NOTEXT])])

# HK3-01a — D hand, overhead · the desk; the heap of scans, one more dropped on top (escalation: "every week")
B["HK3-01a"] = dict(model="nano_banana_2", refs=["P3-D-CONSULT", "D-VOICE-IMG v2"], body=[S("CAM-LOCK"),
  "THE CAMERA ANGLE: the lens directly above the desk, looking straight down at it, seen from over the doctor's side of the desk. This exact angle, not a straight-on eye-level view.",
  focus("the heap of scans and the falling film", "everything from near to far stays sharp"),
  "IN THE SAME ROOM as the attached consulting-room photograph, looking straight down onto its light-wood desk.",
  "A snapshot from a phone held straight out over the desk by someone standing beside it, not looking at the screen. "
  "The whole desktop is buried under a heap of knee scans: dozens of grey-and-black X-ray films of knees, the pale bones and the thin dark joint gaps showing through them, "
  "fanned and overlapping, some half out of plain brown hospital scan envelopes, the heap spilling over the desk edges; the corner of the closed laptop and the white plastic knee model just visible under it. "
  "From the top of the frame the doctor's right hand — a stocky freckled hand, a plain steel watch, the white cuff of his doctor's coat over a pale blue shirt cuff — "
  "has just let go of one more knee X-ray film, caught in mid-air a hand's width above the heap, tilted as it drops, its shadow on the films below.",
  light("The consulting-room window on the room's north wall", "the desk", "left", "steady overcast daylight, the films catching it as dull grey sheen", "the left", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([*NEG_BASE(), "no face, no lightbox, no glowing screen, no X-rays of hands, chests or skulls, no writing, names or labels on films or envelopes, "
                         "no hand cut off at the wrist, no coat missing, no tidy stack", NOTEXT])])

REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P0-PROP-P v2": "176c5c39-ac17-46c4-9e9b-2c06735dc0c8",
       "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b", "P3-D-CONSULT": "757817ea-6840-487c-879c-1b0310e137b2",
       "D-DOC v2": "71b20c5a-f8ef-48d8-8645-f5685a4a92b6", "D-VOICE-IMG v2": "b17f293d-306f-406c-b145-029402a1c074"}
out = {}
for k, b in B.items():
    txt = "\n\n".join(b["body"]); assert "[" not in txt, k
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.v2.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  refs: {', '.join(b['refs'])}")
json.dump(out, open(here / "hooks_v2.json", "w"), indent=1)
json.dump([{"index": i, "params": {"model": v["model"], "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in v["ref_jobs"]], "prompt": v["prompt"]}} for i, v in enumerate(out.values())],
          open(here / "batch_v2.json", "w"), indent=1)
