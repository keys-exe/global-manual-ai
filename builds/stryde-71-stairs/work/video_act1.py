#!/usr/bin/env python3
"""stryde-71-stairs — Act 1 B-roll videos (§35 Kling JSON, §27G natural motion, §22X preflight, E6 lengths).
Writes broll/video/<beat>.call.json + <beat>.prompt.txt. Durations from work/lengths_T2.json."""
import json, pathlib
B = pathlib.Path(__file__).resolve().parents[1]
LEN = {l["beat"]: l["call_s"] for l in json.load(open(B / "work/lengths_T2.json"))["lengths"]}
CUR = json.load(open("/tmp/claude-0/-home-user-global-manual-ai/8f10ea69-fe4e-5541-9214-2e22280bbf9c/scratchpad/act1_cur.json"))

SUBJ = "Exactly as in the start frame, unchanged in every respect."
SWAY = ("Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Brief focus hunt at entry. "
        "One late partial reframe. Camera lags the subject, never anticipates. Still drifting at the cut. The camera never travels.")
HOLD = ("Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. "
        "One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning.")
PERSON = ("Same person every frame: same face, bone structure, age, skin, hair and wardrobe. Five separate fingers on each hand throughout, never fusing and never passing through anything. "
          "Limbs stay attached, keep their length, and bend only the way real joints bend.")
LIGHT = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
STYLE = "Location, surface, dressing and light exactly as in the start frame. Nothing added, nothing removed."
NEG = ("no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, "
       "no background bending, no texture swimming, no smearing, no flickering geometry, no held pose, no looping motion, no reversed motion, no slow motion, "
       "no two separate actions in one clip, no camera travelling, no cut, no music, no voice, no text, no captions")

BEATS = {
 "P-01a": dict(framing="MEDIUM as in the start frame, from the hall below and to the side of the stairs, looking up at her on the flight.",
   motion="Going down her stairs backwards, facing up the flight, she lowers her right foot behind her onto the step below in one slow, careful step over about two seconds, "
          "her hand gripping the handrail and her weight shifting onto that foot as it lands, her body sinking one step lower; then she pauses there, still holding the rail.",
   extra=", no walking forwards, no turning around, no stumbling, no fall, no second step",
   pace="unhurried", smot="in_place",
   risks=[("legs and steps blend on the stairs","side view, one step only, camera never travels (§27G stairs staging)"),
          ("she turns to face down the stairs","'facing up the flight' + negatives no turning around / no walking forwards"),
          ("hand fuses with the handrail","PERSON finger clause + HOLD")]),
 "P-01b": dict(framing="CLOSE as in the start frame, from the side through the white balusters at knee height, her feet on the step.",
   motion="Both slippers stand together on the same step; her right foot lifts and lowers behind her onto the step below in one slow step over about two seconds, "
          "then her left foot follows and joins it on that same lower step, the two feet ending side by side again. One step down, backwards, slow and careful.",
   extra=", no feet on different steps at the end, no walking forwards, no stumbling, no second step",
   pace="unhurried", smot="in_place",
   risks=[("feet blend or merge on the tread","close side view, one step only, HOLD + finger/limb clause"),
          ("she walks forwards down","'lowers behind her… backwards' + negatives"),
          ("balusters bend around the legs","HOLD + no background bending")]),
 "P-02a": dict(framing="MEDIUM as in the start frame, from behind her on the landing, the flight dropping away below.",
   motion="Standing at the head of the stairs, she looks down the flight for a moment, then lets go of the newel post and turns her head and shoulders slowly away from the stairs, "
          "about a quarter turn over two seconds, her weight settling back onto the landing. She does not step down.",
   extra=", no stepping down, no walking down the stairs, no full turn to face the camera",
   pace="unhurried", smot="in_place",
   risks=[("she steps onto the stairs","'She does not step down' + no stepping down"),
          ("turn warps her body","a quarter turn of head and shoulders only, HOLD"),
          ("hand fuses with the newel post","PERSON finger clause")]),
 "P-03a": dict(framing="CLOSE as in the start frame, looking down at her lap and knee.",
   motion="Both hands grip the top edge of the sagging black knee brace and haul it up toward her knee in one tug over about two seconds, the fabric bunching, "
          "then the brace slips back down a little as her grip loosens.",
   extra=", no brace changing shape, no brace changing colour, no velcro tearing off, no strap",
   pace="unhurried", smot="in_place",
   risks=[("brace and fingers merge","HOLD + finger clause"),("brace changes shape or colour","HOLD + negatives"),("hands pass through the brace","PERSON clause")]),
 "P-03b": dict(framing="CLOSE as in the start frame, low near the tile floor, her foot and the brace around her ankle.",
   motion="She shifts her right foot a little on the tile, the slipper turning a few degrees and settling, the black knee brace bunched around her ankle sliding a centimetre with it.",
   extra=", no brace changing shape, no brace moving up the leg, no strap",
   pace="unhurried", smot="in_place",
   risks=[("brace melts into the slipper","HOLD + no brace changing shape"),("foot deforms","PERSON limb clause"),("too much motion","one small shift only")]),
 "P-04a": dict(framing="MEDIUM as in the start frame, in the physical therapy room.",
   motion="The therapist's hands, one under her calf and one on the front of her knee, ease her bent right knee a little further in one slow press over about two seconds, "
          "her face tightening slightly at the stretch, then he holds it there.",
   extra=", no therapist face appearing, no strap, no fast bending",
   pace="unhurried", smot="in_place",
   risks=[("hands merge with her leg","PERSON finger clause + HOLD"),("knee bends the wrong way","'bend only the way real joints bend'"),("face distorts","same person clause")]),
 "P-04b": dict(framing="CLOSE as in the start frame, looking down at the kitchen table and her hands.",
   motion="Her right hand tips the orange pill bottle a little further over her cupped left palm and two small white tablets drop out and land in her palm in about a second, then the bottle tips back up.",
   extra=", no pills spilling everywhere, no bottle changing shape, no readable label",
   pace="unhurried", smot="in_place",
   risks=[("tablets multiply or melt","HOLD count clause"),("bottle and fingers merge","finger clause"),("labels become text","no readable label")]),
 "P-04c": dict(framing="CLOSE as in the start frame, on her bare knee and the doctor's gloved hands.",
   motion="The doctor's gloved hands hold still against the side of her knee while his thumb presses the syringe plunger down slowly by a few millimetres over about two seconds; her own hand rests on her skirt.",
   extra=", no needle bending, no blood, no needle moving through the skin, no syringe changing shape",
   pace="unhurried", smot="in_place",
   risks=[("syringe bends or melts","HOLD + no syringe changing shape"),("gloves fuse with skin","finger clause"),("graphic injection","no blood, plunger only")]),
 "P-04d": dict(framing="MEDIUM-CLOSE as in the start frame, on the corner of the kitchen table and her hand.",
   motion="Her hand lets go of the grey elastic sleeve and it drops a short way onto the heap of braces and sleeves, landing and slumping onto the pile in about a second, then settles still.",
   extra=", no items changing shape, no pile rearranging, no strap",
   pace="unhurried", smot="in_place",
   risks=[("sleeve floats or bounces unnaturally","gravity: drops, lands, settles"),("pile items morph","HOLD count clause"),("hand distorts","finger clause")]),
 "P-05a": dict(framing="WIDE as in the start frame, from the next room through the open kitchen doorway.",
   motion="Sitting alone at the table, she lets out one long breath over about two seconds, her shoulders dropping and her head lowering a little, then she stays still, looking at nothing.",
   extra=", no standing up, no crying, no smiling, no looking at the camera",
   pace="unhurried", smot="in_place",
   risks=[("face warps at distance","same person clause + minimal motion"),("she stands up","no standing up"),("doorway frame bends","no background bending")]),
}

def build(beat):
    b = BEATS[beat]; f, asset, url = CUR[beat]
    p = {"shot": beat.lower().replace("-", "_"), "subject": SUBJ,
         "camera": {"movement": SWAY, "framing": b["framing"]},
         "motion": b["motion"] + " " + HOLD + " " + PERSON,
         "lighting": LIGHT, "style": STYLE, "negatives": NEG + b["extra"]}
    prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": beat, "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": LEN[beat],
            "resolution": "1080p", "aspect_ratio": "9:16", "start_image": f"broll/images/{f}", "start_approved": True,
            "pinned": False, "pace": b["pace"], "subject_motion": b["smot"], "prefer_multi_shots": "false", "generation": 1,
            "risks": [{"risk": r, "prevented_by": v} for r, v in b["risks"]]}
    (B / f"broll/video/{beat}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (B / f"broll/video/{beat}.prompt.txt").write_text(prompt)
    return len(prompt)

if __name__ == "__main__":
    for bt in BEATS: print(bt, LEN[bt], "s", build(bt), "chars")
