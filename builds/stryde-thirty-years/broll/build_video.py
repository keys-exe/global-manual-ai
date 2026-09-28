#!/usr/bin/env python3
"""Step 7 B-roll videos for stryde-thirty-years — §35 Kling JSON per confirmed start image (§27G, §37 ≤ 2,500 chars).

Route: Kling 3.0 on Kie (`kie.py kling`, pro, 9:16, multi_shots false) — the Kling connector ran out of credits at HK1
and the build switched to Kie with no switch back (§5). Durations are the E6 call lengths (work/broll/lengths_HK1.json).
Writes broll/video/<BEAT>.call.json (for preflight.py) and <BEAT>.prompt.txt (the minified JSON sent to Kling).
Usage: build_video.py BEAT [BEAT ...]
"""
import json, re, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent
BUILD = HERE.parent
ROOT = BUILD.parents[1]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
sys.path.insert(0, str(ROOT / "products/stryde"))
import stryde_product_sheet as P  # noqa: E402


def S(i):
    return re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()


LEN = {r["beat"]: r for r in json.loads((BUILD / "work/broll/lengths_HK1.json").read_text())["lengths"]}
ROWS = {r["beat"]: r for r in json.loads((BUILD / "work/actmap.json").read_text())}

PROPPED = S("RIG-R3C")
HANDHELD = S("RIG-R1C")
PRODUCT = ("The strap keeps its exact shape, size and wordmark in every frame and moves only with the body it sits on; " + P.HOLD_PC)
NEG_PROD = ("no bending, no curling, no folding, no melting, no flipping of the product, no shell rotating on the leg, "
            "no strap sliding, no second strap")
NEG_BASE = S("NEG-WARP-C")
NEG_HUMAN = "no face changing, no extra fingers, no fused fingers, no hands passing through objects, no limbs bending the wrong way"
NEG_MOT = "no held pose, no looping motion, no reversed motion, no slow motion, no two separate actions in one clip"
NEG_TAIL = "no music, no voice, no text, no captions"
STAIR = ("One foot per step, alternating, a brisk even rhythm, torso upright, eyes ahead, hands free and never reaching for the rail; "
         "still mid-flight at the cut.")
HOLD_ANAT = ("Bones keep their shape, length and spacing, joints never separate or pass through each other, muscle keeps its volume "
             "and the layer order holds.")
NEG_ANAT = "no bones bending, no joint separating, no rubbery deformation, no structures inflating, no anatomy sliding through the outer contour"
NEG_PROT = "no emission below the product line, no load reaching the tendon, no product moving, no glow flickering"

# beat: (framing, rig, motion, product?, extra negatives, subject_motion, risks)
V = {
 "BR-03a": ("WIDE as in the start frame, low at the foot of the stairs.", HANDHELD,
   "She comes down the stairs forwards towards the camera, one step a second, already mid-step on the first frame, three steps. "
   + STAIR + " The camera never moves with her.", True,
   "no hand on the rail, no camera following her", "travels",
   [("feet blend or slide on the stairs (§27G hard motion)", "three steps at one a second, STAIR-EASE staging, start frame mid-step"),
    ("camera travels with her, adding a second motion", "handheld sway in place, 'never moves with her', no camera following negative"),
    ("the strap slides or reshapes as the knee bends", "product lock + HOLD_PC + product negatives")]),
 "BR-03b": ("MEDIUM as in the start frame, the whole of her in frame beside the armchair.", HANDHELD,
   "She stands up from the armchair in one smooth rise over about two seconds, already rising on the first frame, weight forward "
   "over her feet, hands free and never touching the chair arms; she comes fully upright and her weight shifts onto one foot as if "
   "to walk. The camera sways where it is.", True,
   "no hands on the chair arms, no sitting back down, no wobble", "in_place",
   [("hands grab the chair arms", "hands free stated + negative"), ("knees or hips bend wrongly while rising", "one rise over 2s, HOLD-HC"),
    ("the strap slides as the knee straightens", "product lock + HOLD_PC")]),
 "BR-03c": ("WIDE as in the start frame, three-quarter behind her in the lane, the dog ahead of her.", HANDHELD,
   "She walks away down the lane at one step a second with the terrier trotting ahead on the loose red lead, already mid-stride on "
   "the first frame; she grows a little smaller as she goes. The camera stays where it is and sways, never following.", True,
   "no dog off the lead, no second dog, no camera following her", "travels",
   [("legs blend while walking away", "one step a second, walking away (safe staging)"), ("dog morphs or duplicates", "dog stated once + no second dog"),
    ("camera follows her", "camera stays and sways")]),
 "BR-05a": ("POV as in the start frame: his own view down at the bench, his forearms coming in from the bottom edge.", S("RIG-R2B"),
   "His right hand sets the rolled wrap down at the end of the row in one slow move over about two seconds, lets go of it and draws "
   "back a little, the four supports now in a row. The other hand rests on the wood.", False,
   "no supports moving by themselves, no fifth support, no face", "in_place",
   [("supports merge or change", "HOLD-C + one placement only"), ("fingers fuse around the wrap", "HOLD-HC + finger negatives"),
    ("POV turns into a third-person view", "POV framing + no face")]),
 "BR-05b": ("MEDIUM as in the start frame, through the hanging braces, his hand the subject.", HANDHELD,
   "His hand runs along the hangers in one unhurried pass over about three seconds, fingers trailing across them, each brace swinging a "
   "little as his fingers pass and still swinging after.", False,
   "no braces falling, no hangers merging, no face", "in_place",
   [("braces warp or merge on the rail", "HOLD-C + NEG-WARP-C"), ("hand passes through the braces", "fingers trail across them, never through"),
    ("camera travels along the rail", "camera sways in place")]),
 "BR-07a": ("CLOSE as in the start frame, looking down at her knee in the armchair.", HANDHELD,
   "She tugs the beige sleeve up over her right knee in one tug over about two seconds, both hands pulling it up until it sits over the "
   "kneecap, then her hands loosen on it.", False,
   "no strap, no sleeve tearing, no sleeve changing colour", "in_place",
   [("sleeve and fingers merge", "HOLD-HC + finger negatives"), ("sleeve changes shape or colour", "HOLD-C"), ("face distorts", "HOLD-HC")]),
 "BR-07b": ("CLOSE as in the start frame, his hands and the brace on the bench.", PROPPED,
   "His hands push the top of the hinged brace sideways in one firm push over about two seconds; the steel side bars do not give, "
   "the brace stays straight, and his hands ease off.", False,
   "no brace bending, no brace breaking, no face", "in_place",
   [("brace bends (the opposite of the line)", "'bars do not give, stays straight' + no bending"), ("fingers fuse to the brace", "HOLD-HC"),
    ("camera moves", "propped rig")]),
 "BR-08": ("POV as in the start frame: her own view down into the drawer, her hand on the handle from the bottom edge.", S("RIG-R2B"),
   "She draws the drawer the last few centimetres open in one pull over about two seconds; the tangle of supports inside shifts a "
   "little with the pull and settles.", False,
   "no supports moving by themselves, no face, no second person", "in_place",
   [("contents morph or multiply", "HOLD-C"), ("hand passes into the drawer front", "HOLD-HC"), ("POV becomes third-person", "POV framing")]),
 "BR-10a": ("CLOSE as in the start frame, looking down at her strapped knee on the stool.", PROPPED,
   "His fingertip traces slowly along the line where her kneecap's lower edge sits in the notch, one trace over about two seconds, "
   "then lifts a little off the skin.", True,
   "no finger on the wordmark, no hand pulling the band", "in_place",
   [("finger pushes the strap out of place", "fingertip traces lightly + product lock"), ("strap reshapes", "HOLD_PC"), ("extra fingers", "HOLD-HC")]),
 "BR-10b": ("CLOSE as in the start frame, her straight right leg from the side.", HANDHELD,
   "She shifts her weight onto the strapped right leg once, over about two seconds; the calf firms, the band presses in a little and the "
   "strap stays exactly where it is.", True, "no hands, no face", "in_place",
   [("strap slides with the weight shift", "product lock"), ("leg proportions drift", "HOLD-C"), ("camera travels", "camera sways in place")]),
 "BR-12": ("CLOSE as in the start frame, the back of her right knee on the bottom stair.", PROPPED,
   "Her weight shifts onto her right leg over about two seconds as she readies to step up; the calf firms under the band and the band "
   "stays flat and level just below the crease of the knee.", True,
   "no shell at the back of the knee, no band sliding down the calf, no face, no hands", "in_place",
   [("band slides down the calf", "product lock + no band sliding"), ("shell appears at the rear", "no shell at the back"),
    ("leg warps", "HOLD-C")]),
 "BR-14a": ("CLOSE as in the start frame, looking down at the bench.", PROPPED,
   "His hand tips the bag a little further and the last cheap copy slides out onto the heap in one slide over about two seconds, "
   "the heap settling; the real strap beside it does not move.", False,
   "no copy gaining a wordmark, no copies multiplying, no face, " + P.NEG_FAKE_HERO, "in_place",
   [("copies multiply or merge", "HOLD-C"), ("the real strap moves or reshapes", "'does not move' + HOLD_PC in negatives"),
    ("hand fuses with the bag", "HOLD-HC")]),
 "BR-15b": ("MEDIUM over her shoulder as in the start frame, him across the bench.", HANDHELD,
   "The hand-over completes in one move over about two seconds: her fingers close on the strap and she takes it from his hand, his "
   "hand letting go and drawing back; his face stays calm, eyes on the strap.", True,
   "no strap dropping, no second strap, no face changing", "in_place",
   [("strap passes through a hand", "HOLD-HC + one hand-over"), ("his face drifts from the reference", "HOLD-HC, face never reshapes"),
    ("strap reshapes in the hand-over", "HOLD_PC")]),
 "BR-16": ("WIDE as in the start frame, from the landing, the flight below her.", HANDHELD,
   "She carries on down the stairs away from the camera, one step a second, already mid-step, two more steps. "
   + STAIR + " The camera stays on the landing.", True,
   "no hand on the rail, no camera following her", "travels",
   [("feet blend on the stairs", "one step a second, STAIR-EASE, walking away (safe)"), ("camera follows", "camera stays on the landing"),
    ("band slides", "product lock")]),
 "MECH-02": ("CLOSE as in the start frame, the front of the knee joint.", "The render camera holds still; no move, no zoom.",
   "The knee flexes a few degrees and back in one slow cycle over about two seconds; the smooth cartilage surfaces glide over each "
   "other and the menisci ride with them. " + HOLD_ANAT, False,
   "no glow, no tendon, " + NEG_ANAT, "in_place",
   [("bones pass through each other", "HOLD-ANAT + NEG-WARP-A"), ("a glow appears", "no glow"), ("camera orbits", "render camera holds still")]),
 "MECH-06": ("CLOSE as in the start frame, low in front of her knee.", HANDHELD,
   "Her fingertips press and rub the spot just under her kneecap in small slow circles, one slow rub over about two seconds, and keep "
   "pressing; the beige sleeve on the chair arm does not move.", False,
   "no strap, no sleeve moving, no fingers on the kneecap", "in_place",
   [("fingers fuse with the skin", "HOLD-HC"), ("rub drifts onto the kneecap", "the spot just under the kneecap named"), ("camera travels", "sway in place")]),
 "MECH-11": ("CLOSE as in the start frame, the front of the knee with the strap on it.", "The render camera holds still; no move, no zoom.",
   "The pad presses on the one spot under the kneecap and the tight glow there eases, cooling from near-white towards a soft calm amber "
   "over about two seconds, the rest of the knee calm. " + HOLD_ANAT, True,
   NEG_ANAT + ", no glow spreading", "in_place",
   [("glow spreads instead of easing", "'eases, cooling' + no glow spreading"), ("anatomy deforms", "HOLD-ANAT"), ("strap moves", "product lock")]),
 "MECH-12": ("CLOSE as in the start frame, the knee in profile.", "The render camera holds still; no move, no zoom.",
   "The foot lands on the step below and the body's weight comes down the thigh in one arrival over about two seconds; the pad lights "
   "a soft cool white and carries the load outward to the shell's ends, the tendon beneath it staying calm. " + HOLD_ANAT, True,
   NEG_ANAT + ", " + NEG_PROT, "in_place",
   [("load reaches the tendon", "NEG-PROT"), ("anatomy warps under load", "HOLD-ANAT + NEG-WARP-A"), ("strap moves", "product lock")]),
}


def build(beat):
    framing, rig, motion, prod, extra, sm, risks = V[beat]
    r = ROWS[beat]
    j = {"shot": beat.lower().replace("-", "_"),
         "subject": S("INHERIT-SUBJ") + (" " + PRODUCT if prod else ""),
         "camera": {"movement": rig, "framing": framing},
         "motion": motion + " " + S("HOLD-C") + (" " + S("HOLD-HC") if not beat.startswith("MECH-") or beat == "MECH-06" else ""),
         "lighting": S("INHERIT-CAP"),
         "style": S("INHERIT-ENV"),
         "negatives": ", ".join([NEG_BASE, extra] + ([NEG_PROD] if prod else []) + [NEG_MOT, NEG_TAIL])}
    prompt = json.dumps(j, ensure_ascii=False, separators=(",", ":"))
    n = len(re.findall(r"renders/%s_v(\d+)\.png" % re.escape(beat), "\n".join(str(p) for p in (HERE / "renders").glob(beat + "_v*.png"))))
    return j, prompt


if __name__ == "__main__":
    (HERE / "video").mkdir(exist_ok=True)
    for beat in sys.argv[1:]:
        j, prompt = build(beat)
        framing, rig, motion, prod, extra, sm, risks = V[beat]
        img = json.loads((HERE / "video/_confirmed.json").read_text())[beat]
        call = {"beat": beat, "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt,
                "duration": LEN[beat]["call_s"], "resolution": "1080p", "aspect_ratio": "9:16",
                "start_image": img, "start_approved": True, "pinned": False, "pace": "unhurried", "subject_motion": sm,
                "prefer_multi_shots": "false", "generation": 1,
                "risks": [{"risk": a, "prevented_by": b} for a, b in risks]}
        (HERE / f"video/{beat}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (HERE / f"video/{beat}.prompt.txt").write_text(prompt)
        print(beat.ljust(8), str(call["duration"]).rjust(2), "s", str(len(prompt)).rjust(5), "chars", img)
