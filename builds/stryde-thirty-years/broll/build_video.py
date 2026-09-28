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

# ── Second batch (user "generate the confirm images", 2026-09-28 ~18:40): images confirmed after the first 18 ──────────
POV_STILL = ("Phone held at her own eye line in her other hand, out of frame, pointing down. Only a small breath sway, the framing "
             "holding where it is; no second hand ever comes into frame.")
V.update({
 "BR-02": ("CLOSE as in the start frame, his fingertip at the front of her right knee.", HANDHELD,
   "His extended index fingertip presses once into the soft spot just under her kneecap, over about one second, the skin dimpling a "
   "little, holds it there for one second, then eases off a few millimetres, still touching. His other fingers stay curled.", False,
   "no hand gripping the knee, no second finger touching her, no finger sliding onto the kneecap, no face", "in_place",
   [("finger slides onto the kneecap", "the spot under the kneecap named + negative"), ("hand grips the knee", "one fingertip only + negatives"),
    ("fingers fuse with the skin", "HOLD-HC")]),
 "MECH-01": ("MEDIUM as in the start frame, the whole knee from the front.", "The render camera holds still; no move, no zoom.",
   "The glow at the one spot just under the kneecap pulses brighter and fades back once a second, a walking rhythm, eight even "
   "pulses, never spreading beyond that spot; the bones and muscles stay completely still. " + HOLD_ANAT, False,
   NEG_ANAT + ", no glow spreading, no second glow, no knee bending", "in_place",
   [("glow spreads over the knee", "one spot named + no glow spreading"), ("anatomy drifts", "HOLD-ANAT + everything else still"),
    ("camera orbits", "render camera holds still")]),
 "BR-18a": ("CLOSE as in the start frame, him at the bench holding the two straps up to the lens.", HANDHELD,
   "He brings both straps a few centimetres closer to the lens in one small lift over about two seconds, both front faces staying "
   "square to the camera and level with each other the whole time; his face stays calm, eyes on the lens.", True,
   "no third strap, no straps turning, no straps of different sizes, no face changing", "in_place",
   [("the two straps morph into each other or change size", "HOLD_PC + no straps of different sizes"),
    ("a strap turns and shows another face", "faces stay square the whole lift (no angle change, so no end frame needed)"),
    ("his face drifts", "HOLD-HC")]),
 "BR-18b": ("CLOSE as in the start frame, down onto the box on the bench.", PROPPED,
   "His hands lift the lid straight up off the box in one unhurried move over about three seconds and set it down flat on the bench "
   "beside the box, ending exactly as in the end frame; the two straps lying in the insert do not move.", False,
   "no straps moving in the box, no third strap, no lid flipping over, no face, " + P.NEG_PACKAGE, "in_place",
   [("straps in the insert morph or move", "pinned end frame + 'do not move'"), ("lid passes through the box", "one lift, set down beside"),
    ("fingers fuse with the lid", "HOLD-HC")]),
})
PIN_END = {"BR-18b": "broll/renders/BR-18b-END_v1.png"}

# ── Video Fix round 1 (user Fix notes on the videos, 2026-09-28 ~18:40) — §22X: diagnosed, fixed at the source ────────
VFIX = {
 "BR-05a": "he's holding the product → MOTION + RIG: the start frame has his hand on the rolled wrap and the prompt told him to set it "
           "down, and the arm's-length rig invited a 'free hand' in; now the hands let go on frame one and rest empty on the bare wood, "
           "nothing is held or moved, propped rig",
 "BR-05b": "focus the product → CAMERA: the handheld rig's focus hunt and drift carried the camera past the braces and softened them; "
           "now a propped camera, focus locked on the braces at his hand, sharp every frame, the pass shortened",
 "BR-08": "she's putting the product in the drawer → RIG + MOTION: the arm's-length rig's 'free hand enters frame' brought her other "
          "hand into the drawer; now one hand only, on the handle, the phone at her eye line, nothing goes in or comes out",
 "BR-12": "she's walking forward → MOTION: 'readies to step up' read as a step; now both boots stay planted flat on the hall floor, "
          "only her weight settles onto the right leg, no step",
}
V.update({
 "BR-05a": ("As in the start frame: looking down past his shoulder at the bench, his forearms and the row of supports.", PROPPED,
   "On the first frame his hand lets go of the rolled wrap; both hands lift a little off the supports and come to rest flat and empty "
   "on the bare wood beside the row over about two seconds, and stay there. The four supports lie still in their row.", False,
   "no hand holding anything, no support lifted, no support moved, no fifth support, no face", "in_place",
   [("a hand picks a support up again", "hands let go on frame one + no hand holding anything"),
    ("supports merge or change", "HOLD-C + nothing moved"), ("a free hand enters", "propped rig, no arm's-length rig")]),
 "BR-05b": ("MEDIUM as in the start frame, through the hanging braces, the braces at his hand sharp.",
   "Propped, not held. The camera stays exactly where it is; focus locked on the braces at his hand, sharp every frame, no focus "
   "hunt, no drift, no zoom.",
   "His fingertips trail across the three hangers nearest his hand in one unhurried pass over about two seconds, those braces "
   "swinging a little and still swinging after; the braces stay sharp.", False,
   "no braces falling, no hangers merging, no focus change, no blur on the braces, no camera moving along the rail, no face", "in_place",
   [("braces go soft", "locked focus on the braces + no blur"), ("camera travels along the rail", "propped, no drift"),
    ("hand passes through the braces", "fingertips trail across, HOLD-HC")]),
 "BR-08": ("POV as in the start frame: her own view down into the drawer, her one hand on the handle from the bottom edge.", POV_STILL,
   "Her one hand draws the drawer the last few centimetres open by its front in one pull over about two seconds and stays on the "
   "front; the supports inside shift a little with the pull and settle. Nothing goes into the drawer and nothing comes out.", False,
   "no second hand, no hand reaching into the drawer, nothing put in the drawer, nothing taken out, no face, no second person", "in_place",
   [("second hand reaches in", "one hand only, POV_STILL rig without a free hand + negatives"), ("contents morph", "HOLD-C"),
    ("POV becomes third-person", "POV framing")]),
 "BR-12": ("CLOSE as in the start frame, from behind at floor level, her legs at the foot of the stairs.", PROPPED,
   "She stands still at the foot of the stairs; both boots stay planted flat on the floor the whole clip. Her weight settles onto her "
   "right leg over about two seconds, the right calf firming under the band; the band stays flat and level just below the crease of "
   "the knee.", True,
   "no step, no walking, no foot lifting, no shell at the back of the knee, no band sliding down the calf, "
   "no face, no hands", "in_place",
   [("she steps or walks", "boots planted + no step, no walking"), ("band slides down the calf", "product lock"), ("leg warps", "HOLD-C")]),
})

# ── Round 3 (user "fix those" + "generate the confirm images", 2026-09-28 ~18:50) ─────────────────────────────────────
VFIX.update({
 "BR-02": "he's pointing the knee → MOTION: the start frame's fingertip sits beside the knee and 'presses once' read as pointing "
          "at it; now the fingertip moves in to the soft hollow in the centre just under the kneecap and presses into the tendon, "
          "the skin dimpling, and holds",
 "BR-18b": "slowly zoom in → CAMERA: add a slow steady push-in across the whole clip; the pinned end frame is now the confirmed end "
           "frame cropped tighter on the box (BR-18b-END v2, no new generation), so the zoom and the end frame agree",
})
PIN_END["BR-18b"] = "broll/renders/BR-18b-END_v2.png"
V.update({
 "BR-02": ("CLOSE as in the start frame, his fingertip at the front of her right knee.", HANDHELD,
   "His extended index fingertip moves a few centimetres in to the soft hollow in the centre of the knee just under the kneecap, "
   "over about one second, and presses into the tendon there, the skin dimpling under it; he holds the press for two seconds, still "
   "touching. His other fingers stay curled.", False,
   "no finger on the side of the knee, no finger on the kneecap, no pointing from a distance, no hand gripping the knee, "
   "no second finger touching her, no face", "in_place",
   [("fingertip stays beside the knee, pointing", "motion ends pressing in the centre under the kneecap + negatives"),
    ("finger slides onto the kneecap", "'just under the kneecap' + no finger on the kneecap"), ("fingers fuse with the skin", "HOLD-HC")]),
 "BR-18b": ("CLOSE as in the start frame, down onto the box on the bench, ending tighter on the open box.",
   "Propped, not held. One slow, steady push-in towards the box across the whole clip, ending closer on the open box exactly as in "
   "the end frame; no other camera move.",
   "His hands lift the lid straight up off the box in one unhurried move over about three seconds and set it down flat on the bench "
   "beside the box; the two straps lying in the insert do not move.", False,
   "no straps moving in the box, no third strap, no lid flipping over, no fast zoom, no face, " + P.NEG_PACKAGE, "in_place",
   [("straps in the insert morph or move", "pinned end frame + 'do not move'"), ("zoom fights the end frame", "end frame cropped to the zoom's end"),
    ("fingers fuse with the lid", "HOLD-HC")]),
 "BR-13": ("MEDIUM as in the start frame, from the side through the white spindles, her legs on the stairs.", HANDHELD,
   "She completes the one step down she is in: her right foot lands on the step below over about two seconds, the strapped right "
   "knee bending as it takes her weight and; she stays upright, hands out of frame. The camera "
   "stays where it is behind the spindles.", True,
   "no second step, no hand on the rail, no camera following her, no face", "in_place",
   [("feet blend on the stairs", "one step only, already mid-step"), ("strap slides as the knee bends", "product lock + HOLD_PC"),
    ("camera travels", "camera stays behind the spindles")]),
 "BR-14b": ("CLOSE as in the start frame, his two hands and the copy strap at the bench.", PROPPED,
   "His right hand pulls the copy's thin band a little further out over about two seconds, the band stretching long and pale, then "
   "lets it go: the band stays long and slack, hanging limp, never springing back.", False,
   "no band snapping back, no band breaking, no copy gaining a wordmark, no second copy, no face, " + P.NEG_FAKE_HERO, "in_place",
   [("band springs back (the opposite of the line)", "'stays long and slack, never springing back'"), ("copy turns into the real strap", "NEG_FAKE_HERO"),
    ("fingers fuse with the band", "HOLD-HC")]),
 "BR-15a": ("MEDIUM as in the start frame, his chest and apron, the strap held up in his right hand.", HANDHELD,
   "He brings the strap a few centimetres closer to the lens in one small lift over about two seconds, its front face and wordmark "
   "staying square to the camera the whole time, then holds it there.", True,
   "no strap turning, no second strap, no band unfolding, no strap growing, no face changing", "in_place",
   [("strap grows as it nears the lens", "a few centimetres only + no strap growing + HOLD_PC"),
    ("strap turns and shows another face", "face stays square (no angle change, so no end frame needed)"), ("fingers fuse", "HOLD-HC")]),
})

# BR-15c: the confirmed v3 frame already has the strap seated just below the kneecap, so the slide-up is done; the clip is her hands
# pressing it snug and letting go — no angle or place change, so no end frame (act map pin_end → no).
V["BR-15c"] = ("CLOSE as in the start frame, her right knee and shin, her two hands on the strap.", PROPPED,
   "Her two hands press the shell snug against her leg just below the kneecap in one small press over about two seconds, then let "
   "go and move out to her sides; the strap stays exactly where it is, level and centred.", True,
   "no strap sliding, no strap moving up onto the kneecap, no hands pulling the band, no face", "in_place",
   [("strap rides up onto the kneecap", "'stays exactly where it is' + negatives + product lock"), ("fingers fuse with the shell", "HOLD-HC"),
    ("strap reshapes under the press", "HOLD_PC")])

# ── Third tries, approved by the user ("All three", 2026-09-28 ~19:05) — §22X generation 3 ───────────────────────────────
VFIX3 = {
 "BR-05a": "arrage the product → MOTION: v2 had his hands simply leave the supports; the note asks for arranging, so his fingertips "
           "now square the four supports into a neat row on the bench, sliding each a little, never lifting one",
 "BR-05b": "close up the product / slowly zoom in → CAMERA: v2's locked camera kept the wide framing; now one slow steady push-in from "
           "the start frame onto the braces at his hand, ending close on them, focus locked",
}
V.update({
 "BR-05a": ("As in the start frame: looking down past his shoulder at the bench, his forearms and the row of supports.", PROPPED,
   "His two hands arrange the four supports into a neat, straight row on the bench over about four seconds: his fingertips nudge the "
   "rolled wrap into line at the end of the row, then square up the hinged brace beside it, each support sliding a little across the "
   "wood, never lifted off it. The row ends tidy and even.", False,
   "no support lifted off the bench, no support held up, no fifth support, no supports moving by themselves, no face", "in_place",
   [("a hand picks a support up (the v1 note)", "sliding only, never lifted + negatives"), ("supports merge or change", "HOLD-C"),
    ("fingers fuse with the supports", "HOLD-HC")]),
 "BR-05b": ("MEDIUM as in the start frame at first, through the hanging braces, ending CLOSE on the braces at his hand.",
   "Propped, not held. One slow, steady push-in towards the braces at his hand across the whole clip, ending close on them; focus "
   "locked on those braces, sharp every frame; no other camera move.",
   "His fingertips trail across the three hangers nearest his hand in one unhurried pass over about two seconds, those braces "
   "swinging a little and still swinging after.", False,
   "no braces falling, no hangers merging, no blur on the braces, no fast zoom, no camera moving along the rail, no face", "in_place",
   [("braces go soft in the push-in", "focus locked on the braces + no blur"), ("zoom too fast", "slow, steady, whole clip + no fast zoom"),
    ("hand passes through the braces", "HOLD-HC")]),
})

# ── Round 5 (user "fix those" + "generate the confirm images", 2026-09-28 ~19:10) ──────────────────────────────────────
VFIX.update({
 "BR-13": "she is walking down the stair confident → MOTION: v1 finished one step and then stood still; now she keeps walking down "
          "the flight at a brisk, even, confident pace, two steps, still mid-stride at the cut",
 "BR-14b": "he's showing the product → MOTION: v1 turned the copy up to the lens so it read as our strap on display; now his hands "
           "stay low over the bench, the copy's shell kept down and turned away, and only the thin band is stretched out long",
 "BR-18a": "remove the bracelet / fix the holding (image Fixes) → FRAME: the video is remade from the confirmed v4 start image "
           "(nothing on his wrists, BR-15a's grip in both hands); motion as before",
})
V.update({
 "BR-13": ("MEDIUM as in the start frame, side view through the spindles.", HANDHELD,
   "She walks on down the stairs, confident, one step a second, already mid-step, two more steps. "
   + STAIR + " The camera stays behind the spindles.", True,
   "no stopping, no hand on the rail, no camera following her, no face", "travels",
   [("she stops after one step (the v1 fault)", "two steps, still mid-flight at the cut + no stopping"),
    ("feet blend on the stairs", "one step a second, STAIR-EASE"), ("strap slides as the knee bends", "product lock + HOLD_PC")]),
 "BR-14b": ("CLOSE as in the start frame, his two hands and the copy strap low over the bench.", PROPPED,
   "His hands stay low over the bench: his right hand pulls the copy's thin band a little further out over about two seconds, the band "
   "stretching long and pale, then lets it go, the band hanging long and slack; his left hand keeps the copy's shell down, turned away "
   "from the lens.", False,
   "no lifting the copy up, no showing the shell to the camera, no band springing back, no copy gaining a wordmark, no second copy, "
   "no face, " + P.NEG_FAKE_HERO, "in_place",
   [("copy shown to the lens like the product (the v1 fault)", "hands low, shell turned away + negatives"),
    ("band springs back", "'hanging long and slack'"), ("fingers fuse with the band", "HOLD-HC")]),
})

VFIX3["BR-12"] = ("she's walking / front angle → FRAME + MOTION: new front-view start image (v3, confirmed); she stands still at the "
                  "foot of the stairs, boots planted the whole clip, only her weight settling onto the right leg")
V["BR-12"] = ("KNEE HEIGHT from the front as in the start frame, her legs from waist to boots at the foot of the stairs.", PROPPED,
   "She stands still facing the camera, both boots planted flat on the carpet the whole clip. Her weight settles onto her right leg "
   "over about two seconds, the right knee straightening a little under the strap; the strap stays exactly where it is, just below "
   "the kneecap.", True,
   "no step, no walking, no foot lifting, no turning away, no hands on the knee, no face", "in_place",
   [("she walks (the v1/v2 fault)", "boots planted the whole clip + no step, no walking"), ("strap slides", "product lock + HOLD_PC"),
    ("legs warp", "HOLD-C")])


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
                "start_image": img, "start_approved": True, "pinned": beat in PIN_END, "end_image": PIN_END.get(beat),
                "end_approved": beat in PIN_END, "pace": "unhurried", "subject_motion": sm,
                "prefer_multi_shots": "false", "generation": 2 if beat in VFIX else 1,
                "risks": [{"risk": a, "prevented_by": b} for a, b in risks]}
        if beat in VFIX:
            call["fix_note"] = VFIX[beat]
        if beat in VFIX3:
            call.update(generation=3, fix_note=VFIX3[beat], user_go="2026-09-28: third generation approved by the user ('All three')")
        (HERE / f"video/{beat}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (HERE / f"video/{beat}.prompt.txt").write_text(prompt)
        print(beat.ljust(8), str(call["duration"]).rjust(2), "s", str(len(prompt)).rjust(5), "chars", img)
