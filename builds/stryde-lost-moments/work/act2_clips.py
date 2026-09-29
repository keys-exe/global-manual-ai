#!/usr/bin/env python3
"""stryde-lost-moments — Act 2 (Gloria) clip calls, §35 JSON, §27G natural motion (one action at a named pace,
camera propped, stairs from the side, walking 3 steps across a locked frame, rigid product, no multi-shot).
Start frames are the confirmed Kie renders (work/act2jobs/<beat>.json). A-08 reuses A-HKb — no call.
Usage: act2_clips.py → work/clips/<beat>.v1.{call,kling}.json
"""
import json, pathlib
HERE = pathlib.Path(__file__).parent
L = json.load(open(HERE / "broll_lengths.json"))

CAM = {"movement": "Propped, not held, not tripod. Small settle at entry, then near-stillness with a slow unresolved drift. Slightly off-level and never corrected.",
       "framing": "PROPPED as in the start frame."}
LIGHT = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
HOLD = (" Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, "
        "merges, splits, grows or becomes something else.")
RIGID = " The strap keeps its exact shape, size, position and wordmark in every frame and moves only with the knee it sits on; its rigid shell never bends."
NEG = ("no morphing, no warping, no melting, no merging, no splitting, no duplicate objects, no background bending, no texture swimming, "
       "no camera travelling with the subject, no slow motion, no music, no speech, no cut, no second shot, no extra fingers, no fused fingers")
PNEG = ", no strap sliding, no strap changing shape, no strap on the left knee, no second strap, no misspelled wordmark"
NOSTRAP = ", no knee strap appearing, no brace, no walking stick"

B = {
 "A-01": ("Medium close-up of Gloria, a Black British woman of seventy-three with short silver twists, at the top of her stairs, hand on the mahogany rail, looking down the flight. Exactly as in the start frame.",
          "Already on the first frame she is looking down the flight: she draws one slow breath in before the first step, her chest rising and her grip tightening on the rail, about a second, then holds, eyes fixed on the drop below. She does not step. Mass and momentum: the breath lifts her shoulders, the hand follows.",
          False, ", no stepping down, no smile, no speaking" + NOSTRAP,
          [("she steps or falls", "one breath only, 'she does not step'"), ("face drifts", "HOLD clause, no speaking"), ("hand fuses with the rail", "grip only tightens")]),
 "A-02": ("Extreme close-up of an older woman's feet in burgundy slippers on a deep-red stair runner, turned sideways. Exactly as in the start frame.",
          "Already moving on the first frame: her lower foot slides sideways and down onto the next step, slow and careful, about a second and a half, and settles flat; the other foot stays on the step above taking her weight. One step only. Mass and momentum: the weight shifts first, the foot arrives last.",
          False, ", no feet facing forwards, no second step, no face" + NOSTRAP,
          [("feet turn forwards", "'sideways', 'no feet facing forwards'"), ("extra feet or steps", "one step only, HOLD clause"), ("slipper morphs", "HOLD clause")]),
 "A-03": ("Close-up of an older Black woman's hand gripping a dark mahogany handrail, lilac cardigan cuff at the edge. Exactly as in the start frame.",
          "Already gripping on the first frame: her knuckles whiten as her weight comes down onto the rail, one slow squeeze, about a second, the tendons on the back of the hand standing out, then holds. The rail and the hand stay where they are.",
          False, ", no hand letting go, no second hand, no rail moving" + NOSTRAP,
          [("fingers fuse with the rail", "one squeeze only, hand negatives"), ("rail bends", "HOLD clause"), ("hand slides away", "'then holds'")]),
 "A-04": ("Medium close-up of Gloria on her landing in a coral blouse, eyes easing closed. Exactly as in the start frame.",
          "Already easing on the first frame: her shoulders drop as she breathes out slowly, about two seconds, the tension leaving her face, the corners of her mouth lifting into the start of a small smile, then she holds it. She stays where she is.",
          False, ", no walking, no speaking, no big grin" + NOSTRAP,
          [("face drifts", "HOLD clause, one breath out"), ("she walks off", "'she stays where she is'"), ("exaggerated smile", "'the start of a small smile'")]),
 "A-05": ("From the side and waist-down: an older woman in a navy linen skirt coming down a carpeted staircase facing forwards, a black knee strap on her right knee. Exactly as in the start frame.",
          "Already moving on the first frame: she takes one step down facing forwards, her foot landing flat on the next tread, the knee bending easily under her, about a second, one hand resting lightly on the rail, then her weight settles. One step only. Mass and momentum: the weight transfers first, the trailing foot follows." + RIGID,
          True, ", no gripping the rail, no sideways, no backwards, no face" + PNEG,
          [("strap slides or morphs", "RIGID clause, product negatives"), ("she turns sideways", "'facing forwards', negatives"), ("camera follows her down", "propped camera, 'no camera travelling'")]),
 "A-06": ("From the side: an older woman in a coral blouse and navy linen skirt coming down the last stairs facing forwards, a black knee strap on her right knee. Exactly as in the start frame.",
          "Already moving on the first frame: she steps down one more step, easy and confident, about a second, her knee bending freely, her hand light on the rail, then her weight settles. One step only. Mass and momentum: the weight transfers first, the trailing foot follows." + RIGID,
          True, ", no gripping, no sideways, no backwards" + PNEG,
          [("strap slides or morphs", "RIGID clause, product negatives"), ("she turns sideways", "'facing forwards', negatives"), ("face drifts", "HOLD clause")]),
 "A-07": ("Medium shot from behind: Gloria in a coral blouse and navy linen skirt walking away down her tiled hall toward a bright kitchen doorway. Exactly as in the start frame.",
          "Already walking on the first frame: three easy steps away from the lens down the hall, one step per second, arms swinging loosely, shoulders straight; the camera stays where it is and she gets a little smaller. Mass and momentum: the hips lead, the arms swing after.",
          False, ", no turning round, no stick, no hand on the wall, no running" + NOSTRAP,
          [("camera follows her", "propped camera, 'the camera stays where it is'"), ("she turns round", "negatives"), ("legs tangle", "three steps at a named pace")]),
 "A-09": ("Medium shot from the hall: Gloria in a lilac cardigan and floral skirt at the foot of her stairs, hand on the newel post, a black strap on her right knee. Exactly as in the start frame.",
          "Already on the first frame: she lifts her eyes up the flight, chin rising, one slow look up, about a second, then holds, calm and ready. She does not climb." + RIGID,
          True, ", no climbing, no speaking" + PNEG,
          [("she starts climbing", "'she does not climb'"), ("strap morphs", "RIGID clause"), ("face drifts", "HOLD clause")]),
 "A-10": ("Medium close-up of Gloria in a coral blouse on her landing, one hand on the rail, looking down the stairs. Exactly as in the start frame.",
          "Already on the first frame: a small private smile starts and grows, about a second, her eyes on the stairs below, then she holds it. She stays where she is.",
          False, ", no walking, no speaking, no big grin, no looking at the camera" + NOSTRAP,
          [("face drifts", "HOLD clause"), ("big grin", "'a small private smile'"), ("she walks off", "'she stays where she is'")]),
}

if __name__ == "__main__":
    out = HERE / "clips"
    for b, (subj, mot, strap, neg, risks) in B.items():
        s = open(HERE / "act2jobs" / f"{b}.json").read(); job = json.loads(s[s.index("{", 5):])
        p = dict(shot=b.lower().replace("-", "_"), subject=subj, camera=CAM, motion=mot + HOLD, lighting=LIGHT, style="As in the start frame.",
                 negatives=NEG + neg)
        pj = json.dumps(p, ensure_ascii=False)
        c = dict(beat=b, connector="kling", mode=1, kind="broll", prompt=pj, duration=max(3, L[b]["call_s"]), resolution="1080p",
                 aspect_ratio="9:16", start_image=job["urls"][0], start_approved=True,
                 approved_by="user: 'I'VE CONFIRM PROCEED' (2026-09-29) on the Act 2 images", pinned=False, end_image=None,
                 end_approved=False, subject_motion="walking" if b == "A-07" else "in_place", prefer_multi_shots="false", generation=1,
                 risks=[dict(risk=r, prevented_by=v) for r, v in risks])
        json.dump(c, open(out / f"{b}.v1.call.json", "w"), indent=1)
        (out / f"{b}.v1.kling.json").write_text(pj)
        print(b, c["duration"], len(pj))
