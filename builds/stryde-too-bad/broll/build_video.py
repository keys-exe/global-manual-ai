#!/usr/bin/env python3
"""Step 7 B-roll clips for stryde-too-bad — §35 Kling JSON per confirmed start image (§27G, §37 ≤ 2,500 chars).

Route: Kling 3.0 on Kie (`kie.py kling`, pro, 9:16, multi_shots false, sound off) — the Kling connector holds 3 credits (§5).
Durations are the E6 call lengths from `assemble.py --lengths` on both videos (edit/lengths_V1.json, edit/lengths_V2.json):
a beat cut into both videos takes the longer call. Pattern from stryde-thirty-years/broll/build_video.py.
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


LEN = {}
for v in ("V1", "V2"):
    for r in json.loads((BUILD / f"edit/lengths_{v}.json").read_text())["lengths"]:
        LEN[r["beat"]] = max(LEN.get(r["beat"], 0), r["call_s"])
LEN["MECH-S2"] = LEN["MECH-S1"]   # the split's bottom band plays under MECH-S1 for the same time

HANDHELD = S("RIG-R1C")
RENDER = "The render camera holds still; no move, no zoom."
PRODUCT = "The strap keeps its exact shape, size and wordmark in every frame and moves only with the body or hand it is on; " + P.HOLD_PC
NEG_PROD = ("no bending, no curling, no folding, no melting, no flipping of the product, no shell rotating on the leg, "
            "no strap sliding, no second strap")
NEG_BASE = S("NEG-WARP-C")
NEG_MOT = "no held pose, no looping motion, no reversed motion, no slow motion, no two separate actions in one clip"
NEG_TAIL = "no music, no voice, no text, no captions"
WALK = "One step a second, relaxed, torso upright; still mid-stride at the cut. The camera sways where it is, never following."
HOLD_ANAT = ("Bones keep their shape, length and spacing, joints never separate or pass through each other, muscle keeps its volume "
             "and the layer order holds.")
NEG_ANAT = "no bones bending, no joint separating, no rubbery deformation, no structures inflating, no anatomy sliding through the outer contour"
NEG_GLOW = "no glow spreading onto the shin, no second glow, no flicker"

# beat: (framing, rig, motion, product?, extra negatives, subject_motion, risks)
V = {
 "B1-01a": ("MCU as in the start frame, eye level three-quarter across the desk: his hands, the strap and the knee model.", HANDHELD,
   "His hands bring the strap the last few centimetres in over about two seconds, already moving on the first frame, and seat the "
   "shell just below the model's kneecap, ending as in the end frame, with one small press. The model never moves. The camera sways "
   "where it is.", True,
   "no model moving, no band fastened, no white coat", "in_place",
   [("the shell reshapes as it meets the model", "pinned end frame + HOLD_PC + product negatives"),
    ("fingers fuse with the shell or the model", "HOLD-HC, fingers stated on the ends and the pad behind"),
    ("the model knee moves or bends", "'the knee model never moves' + negative")]),
 "MECH-S1": ("MCU as in the start frame, the knee from the front with the strap on it.", RENDER,
   "The strap's shell and band glow a cool electric blue along their edges, the glow rising slowly and evenly over about two "
   "seconds and holding; the whole knee beneath stays calm, washed in faint clear blue. " + HOLD_ANAT, True,
   NEG_ANAT + ", no red glow, " + NEG_GLOW, "still",
   [("anatomy deforms", "HOLD-ANAT + NEG_ANAT"), ("the strap moves on the tendon", "product lock"), ("camera orbits", "render camera holds still")]),
 "MECH-S2": ("MCU as in the start frame, the knee in the big brace, three-quarter.", RENDER,
   "The hot red-orange glow in the joint under the brace pulses slowly once, brightening and settling over about two seconds; "
   "the brace and the anatomy stay completely still. " + HOLD_ANAT, False,
   NEG_ANAT + ", no brace moving, no strap, " + NEG_GLOW, "still",
   [("glow spreads over the leg", "one pulse in the joint + no glow spreading"), ("brace warps", "brace stays still"),
    ("camera orbits", "render camera holds still")]),
 "B1-03a": ("MEDIUM as in the start frame, ground level three-quarter: his legs on the step and the kitchen floor.", HANDHELD,
   "He completes the one step down he is in: his right foot lands flat on the floor tiles over about one second, already moving on "
   "the first frame, and his right knee bends a little as it takes his whole weight, then straightens as he stands on both feet. "
   "His hands stay free at his sides. The camera sways where it is.", False,
   "no second step, no hand on the wall, no hand on the door frame, no stumble, no strap, no camera following him", "in_place",
   [("feet blend or slide on the step (§27G)", "one step only, start frame mid-step"),
    ("knee bends the wrong way", "HOLD-HC + limbs negative in NEG-WARP-C"), ("camera travels", "sways where it is")]),
 "MECH-02": ("MCU as in the start frame, low three-quarter on the knee.", RENDER,
   "Heel strike: a pulse of load runs down the thigh over about one second and lands on the one tight red point on the tendon just "
   "below the kneecap, which flares hot and settles; the heat stays on that one point. " + HOLD_ANAT, False,
   NEG_ANAT + ", no strap, no brace, " + NEG_GLOW, "still",
   [("the red spreads down the shin", "one tight point named + no glow spreading"), ("the knee bends", "anatomy holds, render still"),
    ("camera moves", "render camera holds still")]),
 "MECH-03": ("MCU as in the start frame, the knee from the front in the translucent brace.", RENDER,
   "The translucent brace squeezes in evenly all round the knee over about two seconds and holds; the one tight red point on the "
   "tendon below the kneecap stays exactly as bright, untouched. " + HOLD_ANAT, False,
   NEG_ANAT + ", no red point fading, no strap, " + NEG_GLOW, "still",
   [("the red point cools (the opposite of the line)", "'stays exactly as bright, untouched'"),
    ("the brace passes through the anatomy", "squeezes evenly + NEG_ANAT"), ("camera moves", "render camera holds still")]),
 "MECH-04": ("MCU as in the start frame, the knee in profile with the strap on it.", RENDER,
   "The strap glows a cool blue and the red point under the kneecap cools slowly to the same calm blue over about two seconds, as the "
   "load is taken off the spot; everything else stays still. " + HOLD_ANAT, True,
   NEG_ANAT + ", no red returning, " + NEG_GLOW, "still",
   [("the red spreads instead of cooling", "'cools slowly to calm blue' + negatives"), ("the strap moves", "product lock"),
    ("anatomy deforms", "HOLD-ANAT")]),
 "B1-05b": ("MEDIUM as in the start frame, low three-quarter: her by the sofa, the strap on her right knee.", HANDHELD,
   "She stands up from the sofa in one smooth, easy rise over about two seconds, already rising on the first frame, hands on her "
   "knees then free, and comes fully upright with a small surprised breath out. The camera sways where it is.", True,
   "no sitting back down, no hands on the sofa arm, no wobble, no wincing", "in_place",
   [("hands grab the sofa to push up", "hands on knees then free + negatives"), ("the strap slides as the knee straightens", "product lock + HOLD_PC"),
    ("knees bend wrongly on the rise", "one rise over 2s, HOLD-HC")]),
 "B1-07a": ("CU as in the start frame, high three-quarter: his hands on his right knee at the kitchen table.", HANDHELD,
   "Both his hands slowly rub the sides of his right knee through his grey trousers, one slow rub down and back over about three "
   "seconds, his head bowed a little; his body stays seated and still. The camera sways where it is.", False,
   "no standing up, no trousers rolling up, no strap, no fingers passing through the fabric", "in_place",
   [("fingers merge with the trousers", "HOLD-HC + negative"), ("he stands (second action)", "stays seated + negatives"),
    ("knee reshapes under the hands", "HOLD-C")]),
 "MECH-05": ("CU as in the start frame, the knee three-quarter, muscle over bone.", RENDER,
   "A dull red glow in the narrowed joint space and along the torn meniscus edge pulses slowly, brightening and easing twice over "
   "about four seconds; the muscles, bones and worn surfaces stay completely still. " + HOLD_ANAT, False,
   NEG_ANAT + ", no strap, no brace, no glow on the tendon, " + NEG_GLOW, "still",
   [("glow drifts onto the tendon", "one site named + no glow on the tendon"), ("anatomy drifts over 6s", "HOLD-ANAT, everything else still"),
    ("camera orbits", "render camera holds still")]),
 "B1-08": ("FULL as in the start frame, low and in front: her on the park path, the bandstand behind.", HANDHELD,
   "She walks along the path towards the camera, already mid-stride on the first frame, three steps. " + WALK, True,
   "no camera following her, no running, no limping", "travels",
   [("feet slide or legs cross (§27G walk at camera)", "three steps at one a second, start frame mid-stride"),
    ("camera travels with her", "sways where it is, never following"), ("strap slides on the moving knee", "product lock + HOLD_PC")]),
 "B1-09a": ("CU as in the start frame, low three-quarter: his right leg on the lawn, the trouser leg rolled above the knee.", HANDHELD,
   "His rolled trouser leg unrolls and drops over about one second, already moving on the first frame, and falls flat over the "
   "strap to his boot, hiding it. His leg stays still. The camera sways where it is.", True,
   "no hand on the trousers, no bulge under the trousers", "still",
   [("the strap shows through or bulges under the cloth", "falls flat + no bulge negative"),
    ("the cloth morphs or passes through the leg", "HOLD-C"), ("the strap slides as the cloth falls", "product lock")]),
 "B1-09b": ("FULL as in the start frame, eye level in profile: him on the lawn with the green watering can.", HANDHELD,
   "He walks across the frame down the lawn towards the vegetable bed carrying the watering can, already mid-stride on the first "
   "frame, three steps, the can swinging a little. " + WALK, False,
   "no water pouring, no strap showing, no trousers rolled, no camera following him", "travels",
   [("legs blend mid-stride (§27G walk)", "three steps at one a second, start frame mid-stride"),
    ("the can changes shape", "HOLD-C"), ("camera pans with him", "sways where it is, never following")]),
 "B1-10": ("MEDIUM as in the start frame, ground level three-quarter: him in the shop aisle with the cardboard box.", HANDHELD,
   "He walks along the aisle carrying the cardboard box in both hands, already mid-stride on the first frame, three steps, the strap "
   "on his right knee. " + WALK, True,
   "no box dropping, no shelves moving", "travels",
   [("legs blend mid-stride", "three steps at one a second, start frame mid-stride"), ("the strap slides on the moving knee", "product lock + HOLD_PC"),
    ("the box morphs or passes through his hands", "HOLD-HC + negatives")]),
 "B1-11": ("FULL as in the start frame, from behind: her on the clifftop path, the sea on the left.", HANDHELD,
   "She walks away along the path, already mid-stride on the first frame, three steps, growing a little smaller as she goes. " + WALK, True,
   "no turning round, no face, no running, no camera following her", "travels",
   [("legs blend walking away", "three steps at one a second, start frame mid-stride"), ("she turns to camera", "no turning round, no face"),
    ("the strap slides", "product lock + HOLD_PC")]),
 "B1-12a": ("CU as in the start frame, overhead: the open box on the coffee table, the lid beside it.", HANDHELD,
   "Her hand lifts away from the lid she has just laid flat beside the box, over about two seconds, and leaves the frame; the open "
   "box and the two straps lying in its insert do not move.", False,
   "no straps moving in the box, no third strap, no lid flipping over, no face, " + P.NEG_PACKAGE, "in_place",
   [("straps in the insert morph or move", "'do not move' + HOLD-C"), ("fingers fuse with the lid", "HOLD-HC"),
    ("the lid flips", "negative")]),
 "B1-13a": ("MEDIUM as in the start frame, high and in front at the top of the stairs: her on the landing.", HANDHELD,
   "She stands on the landing looking down the flight and takes one easy breath, her shoulders lifting and settling over about two "
   "seconds; her feet stay planted. Both knees are bare. The camera sways where it is.", False,
   "no step, no walking, no hand on the banister, no strap, no knee strap, no brace, no worried face", "still",
   [("she steps down (second action)", "feet planted + no step"), ("her face drifts", "HOLD-HC"),
    ("a strap appears on her knee", "no strap stated + negatives")]),
 "B1-13b": ("FULL as in the start frame, low at the foot of the stairs: her coming down the flight.", HANDHELD,
   "She comes down the stairs forwards towards the camera, already mid-step on the first frame, two steps, one foot per step, a "
   "relaxed even rhythm, torso upright, eyes ahead, hands free and never reaching for the rail; still mid-flight at the cut. Both "
   "knees are bare. The camera stays where it is and sways, never following.", False,
   "no hand on the rail, no strap, no knee strap, no brace, no camera following her, no stumble", "travels",
   [("feet blend or slide on the stairs (§27G hard motion)", "two steps, one foot per step, start frame mid-step"),
    ("camera travels with her", "sways where it is, never following"), ("a strap appears on her knee", "no strap stated + negatives")]),
}
PIN_END = {"B1-01a": "broll/v2/B1-01a-END_v1.png"}   # act map pin_end: product placed (§27G rule 5); END v1 confirmed by the user
CDN = "https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/"


def build(beat):
    framing, rig, motion, prod, extra, sm, risks = V[beat]
    j = {"shot": beat.lower().replace("-", "_"),
         "subject": S("INHERIT-SUBJ") + (" " + PRODUCT if prod else ""),
         "camera": {"movement": rig, "framing": framing},
         "motion": motion + " " + S("HOLD-C") + ("" if beat.startswith("MECH-") else " " + S("HOLD-HC")),
         "lighting": S("INHERIT-CAP"),
         "style": S("INHERIT-ENV"),
         "negatives": ", ".join([NEG_BASE, extra] + ([NEG_PROD] if prod else []) + [NEG_MOT, NEG_TAIL])}
    return json.dumps(j, ensure_ascii=False, separators=(",", ":"))


if __name__ == "__main__":
    (HERE / "video").mkdir(exist_ok=True)
    imgs = json.loads((HERE / "video/_confirmed.json").read_text())   # beat -> the confirmed start image (path or URL)
    for beat in sys.argv[1:]:
        prompt = build(beat)
        framing, rig, motion, prod, extra, sm, risks = V[beat]
        call = {"beat": beat, "connector": "kling", "route": "Kling 3.0 on Kie (kie.py kling), Kling connector out of credits",
                "mode": 1, "kind": "broll", "prompt": prompt, "duration": LEN[beat], "resolution": "1080p", "aspect_ratio": "9:16",
                "start_image": imgs[beat], "start_approved": True, "pinned": beat in PIN_END, "end_image": PIN_END.get(beat),
                "end_approved": beat in PIN_END, "pace": "unhurried", "subject_motion": sm,
                "prefer_multi_shots": "false", "generation": 1,
                "risks": [{"risk": a, "prevented_by": b} for a, b in risks]}
        (HERE / f"video/{beat}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (HERE / f"video/{beat}.prompt.txt").write_text(prompt)
        print(beat.ljust(8), str(call["duration"]).rjust(2), "s", str(len(prompt)).rjust(5), "chars")
