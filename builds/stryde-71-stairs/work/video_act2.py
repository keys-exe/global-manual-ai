#!/usr/bin/env python3
"""stryde-71-stairs — Act 2 videos + the P-01b Fix (generation 2). Same §35 shape as video_act1.py."""
import json, sys
sys.path.insert(0, __file__.rsplit('/', 1)[0])
import video_act1 as V
S = "/tmp/claude-0/-home-user-global-manual-ai/8f10ea69-fe4e-5541-9214-2e22280bbf9c/scratchpad"
CUR2 = json.load(open(S + "/act2_cur.json"))
LOCKED = ("Camera fixed in place on a small tripod-like hold, only the faintest breath of movement, the frame never pans, tilts, follows or travels. "
          "Still at the cut.")
PARTY_NEG = ", no flash, no posing, no looking at the camera, no faces changing, no people merging, no extra limbs"
B2 = {
 "T-01a": dict(framing="MEDIUM as in the start frame, at the reception table under the string lights.", cam=V.SWAY,
   motion="The bride, mid-laugh, tips her head back a little further and then forward again in one laugh over about a second and a half, her hand staying on the arm of the woman beside her; "
          "the guests around the table shift slightly and smile. Everyone keeps their own different face.",
   extra=PARTY_NEG + ", no two faces alike changing into one", pace="unhurried", smot="in_place",
   risks=[("faces blend into one","'Everyone keeps their own different face' + no faces changing"),("hands merge with arms","finger clause"),("table items morph","HOLD count clause")]),
 "T-01b": dict(framing="MEDIUM as in the start frame, Loretta at the edge of the dance floor.", cam=V.SWAY,
   motion="Loretta claps on the beat twice, her hands meeting in front of her chest about once a second, grinning at the dancers off-frame, her weight rocking a little from foot to foot. The guests behind her move softly out of focus.",
   extra=PARTY_NEG + ", no dancing steps, no dress changing colour", pace="unhurried", smot="in_place",
   risks=[("hands fuse on the clap","finger clause, two claps only"),("dress colour shifts","HOLD + no dress changing colour"),("background guests warp","no people merging")]),
 "T-02a": dict(framing="WIDE as in the start frame, the line dance seen past the backs of two gold chairs.", cam=LOCKED,
   motion="The whole line of dancers, Loretta in the middle in her royal-blue dress and white sneakers, takes ONE side-step to the right together in time, about one step per second, their arms loose, then settles on the beat.",
   extra=PARTY_NEG + ", no spinning, no jumping, no running, no crowd crossing the camera", pace="brisk", smot="in_place",
   risks=[("dancers' legs blend in the step","one side-step only, camera locked (§27G dancing: short burst, camera still)"),("Loretta's dress changes","HOLD"),("faces become identical","no faces changing")]),
 "T-02b": dict(framing="CLOSE as in the start frame, low over the parquet dance floor, the row of dancing feet.", cam=LOCKED,
   motion="The row of feet steps back together once in time — every foot lifting and landing one step back in about a second, Loretta's white slip-on sneakers among them — then taps once on the beat.",
   extra=PARTY_NEG + ", no feet merging, no extra feet, no shoes changing", pace="brisk", smot="in_place",
   risks=[("feet multiply or merge","HOLD count clause + no extra feet"),("shoes change style","no shoes changing"),("floor pattern swims","no texture swimming")]),
 "T-03a": dict(framing="The anatomical knee as in the start frame, side view.", cam="Camera completely still. The frame does not move.",
   motion="The tight red spot on the patellar tendon just below the kneecap pulses once — brightening over about a second and easing back — while the worn joint surfaces behind it stay pale and rough. Nothing else moves.",
   extra=", no glow spreading over the kneecap, no bones moving, no leg bending, no anatomy changing shape, no text, no labels", pace="unhurried", smot="still",
   risks=[("glow drifts onto the kneecap","'just below the kneecap' + no glow over the kneecap"),("anatomy morphs","HOLD + no anatomy changing shape"),("leg moves","camera still, nothing else moves")]),
}

def build(beat, cfg, start, gen=1, fix=None, dur=None):
    p = {"shot": beat.lower().replace("-", "_"), "subject": V.SUBJ, "camera": {"movement": cfg["cam"], "framing": cfg["framing"]},
         "motion": cfg["motion"] + " " + V.HOLD + (" " + V.PERSON if cfg["smot"] != "still" else ""),
         "lighting": V.LIGHT, "style": V.STYLE, "negatives": V.NEG + cfg["extra"]}
    prompt = json.dumps(p, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": beat, "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt, "duration": dur or V.LEN[beat],
            "resolution": "1080p", "aspect_ratio": "9:16", "start_image": "broll/images/" + start, "start_approved": True,
            "pinned": False, "pace": cfg["pace"], "subject_motion": cfg["smot"], "prefer_multi_shots": "false", "generation": gen,
            "risks": [{"risk": r, "prevented_by": v} for r, v in cfg["risks"]]}
    if fix: call["fix_note"] = fix
    (V.B / f"broll/video/{beat}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (V.B / f"broll/video/{beat}.prompt.txt").write_text(prompt)
    return len(prompt)

P01B = dict(framing="CLOSE as in the start frame, from the side through the white balusters at knee height, her feet on the step.", cam=LOCKED,
   motion="ONLY ONE STEP IN THE WHOLE CLIP. Both slippers start together on the same step. Her right foot lowers behind her onto the step just below, then her left foot joins it on that SAME step, "
          "the two feet side by side again after about two seconds — then both feet stay still together on that one step to the end of the clip, her hand resting on the rail. She does not take another step.",
   extra=", no second step, no walking, no alternating feet, no feet on different steps at the end, no walking forwards, no stumbling", pace="unhurried", smot="in_place",
   risks=[("she walks down several steps","'ONLY ONE STEP IN THE WHOLE CLIP' + no second step / no alternating feet"),
          ("camera follows her down","camera fixed in place, never travels"),("feet end on different steps","'feet stay still together on that one step to the end'")])

if __name__ == "__main__":
    for bt, cfg in B2.items(): print(bt, V.LEN[bt], "s", build(bt, cfg, CUR2[bt][0]), "chars")
    print("P-01b", build("P-01b", P01B, V.CUR["P-01b"][0], gen=2,
          fix="v1 walked down several steps alternating feet while the camera followed (motion fault, user: 'it should be same step on the stair both feet') → one step-to only, both feet end together and hold, camera fixed, walking/alternating feet banned"), "chars")
