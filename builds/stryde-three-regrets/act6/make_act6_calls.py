"""Act 6 clip calls (§35 JSON on Kie kling-3.0-omni), same shape as act5/make_act5_calls.py."""
import json, sys, os
sys.path.insert(0, "/home/user/global-manual-ai/products/stryde"); import stryde_product_sheet as ps
D = os.path.dirname(os.path.abspath(__file__)) + "/"
R1C = "Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Brief focus hunt at entry. One late partial reframe. Camera lags the subject, never anticipates. Still drifting at the cut."
LOCK = "Locked off on a steady surface, only a faint breath of sway. The camera never pans or travels. Still at the cut."
HOLD_C = "Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning."
HOLD_HC = "Same person, face and wardrobe every frame; five separate fingers on each hand, never fusing or passing through anything; limbs keep their length and bend only as real joints bend."
PHYS = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
CAP = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
NEGW = "no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, no texture swimming, no smearing, no flickering geometry, no flickering light, no exposure pumping"
HPC = " " + ps.HOLD_PC
B = [
 dict(beat="BR-057", shot="act6_unfold", cam=R1C, subject="THE SAME HANDS AND LETTER as in the start frame; unchanged in every respect.",
  framing="CU as in the start frame: directly above the desk. FOCUS: her hands and the letter are sharp.",
  motion="CONTINUING: her hands are already unfolding the printed letter on the desk. COMPLETING: one unfold, about two seconds — the top fold opens down flat and her fingers smooth it once across the page. UNRESOLVED: her hands rest on the open letter.",
  style="Unremarkable phone clip, soft warm morning window light on the desk, no grade.",
  negs="no readable text, no words forming, no paper tearing, no second letter moving, no face, no talking, no music",
  risks=[{"risk":"text appears readable or morphs","prevented_by":"no readable text, no words forming"},{"risk":"fingers fuse with the paper","prevented_by":"HOLD-HC"},{"risk":"other letters slide about","prevented_by":"no second letter moving; HOLD-C"}], sm="in_place"),
 dict(beat="BR-058", shot="act6_finger_line", cam=R1C, subject="THE SAME HAND AND CARD as in the start frame; unchanged in every respect.",
  framing="ECU as in the start frame: eye height, three-quarter to the pinboard. FOCUS: her fingertip and the line of ink are sharp.",
  motion="CONTINUING: her forefinger rests under one handwritten line on the card. COMPLETING: one slow small trace, about two seconds — the fingertip moves a finger's width along under the line and stops. UNRESOLVED: her finger rests there, still.",
  style="Unremarkable phone clip, soft warm morning window light, no grade.",
  negs="no readable words, no words forming, no card falling, no pins moving, no face, no talking, no music",
  risks=[{"risk":"the handwriting turns readable or changes","prevented_by":"no readable words, no words forming"},{"risk":"the card falls off the board","prevented_by":"no card falling, no pins moving"},{"risk":"the finger fuses into the card","prevented_by":"HOLD-HC"}], sm="in_place"),
 dict(beat="PR-061a", shot="act6_box_open", cam=R1C, subject="THE SAME OPEN BOX, TWO STRAPS AND HAND as in the start frame; unchanged in every respect.",
  framing="CU as in the start frame: directly above the open box. FOCUS: both straps and their wordmarks are sharp.",
  motion="CONTINUING: her hand rests on the edge of the open lid. COMPLETING: one small settle, about two seconds — her fingers ease the lid a touch further back so it rests open, then lift away. UNRESOLVED: the box stays open, both straps still in their wells." + HPC,
  style="Unremarkable phone clip, soft kitchen window daylight, no grade.",
  negs="no lid closing, no straps moving, no third strap, no strap leaving its well, no offer text, no face, no music",
  risks=[{"risk":"the lid closes over the straps","prevented_by":"the lid eased back to rest open; no lid closing"},{"risk":"a strap morphs or a third appears","prevented_by":"HOLD-PC; no third strap"},{"risk":"the wordmarks smear","prevented_by":"HOLD-PC; no straps moving"}], sm="in_place", hc=False),
 dict(beat="BR-061b", shot="act6_stand_both", cam=R1C, subject="THE SAME MAN as in the start frame, green polo, khaki shorts, a strap on each knee; unchanged in every respect.",
  framing="FULL as in the start frame: low, knee height, three-quarter, the shelter behind. FOCUS: deep.",
  motion="CONTINUING: he is already rising off the red perch bench, hands pushing on his thighs. COMPLETING: one brisk stand, about two seconds — he pushes up and straightens to his full height, both knees extending easily, hands leaving his thighs. UNRESOLVED: he stands upright, a small pleased look, both straps in place." + HPC,
  style="Unremarkable phone clip, warm broken-cloud afternoon sun, no grade.",
  negs="no hands on the straps, no strap sliding, no walking away, no sitting back down, no stumbling, no talking, no glancing at the lens, no music",
  risks=[{"risk":"a strap slides as the knees straighten","prevented_by":"HOLD-PC; no strap sliding"},{"risk":"he walks off or sits back","prevented_by":"one stand only; no walking away, no sitting back down"},{"risk":"hands grab the straps","prevented_by":"no hands on the straps"}], sm="in_place", hc=False),
 dict(beat="PR-062", shot="act6_two_on_palm", cam=LOCK, subject="THE SAME HAND AND TWO STRAPS as in the start frame; unchanged in every respect.",
  framing="CU as in the start frame: eye height, square to his palm. FOCUS: both straps are sharp.",
  motion="CONTINUING: he holds the two straps level on his open palm. COMPLETING: one small lift of the hand, about two seconds — the palm rises a little and settles, both straps staying level, fronts to the lens, never turning. UNRESOLVED: he holds them still." + HPC,
  style="Unremarkable phone clip, warm broken-cloud afternoon sun, no grade.",
  negs="no turning the straps, no strap sliding off, no fingers over the straps, no third strap, no one strap only, no face, no music",
  risks=[{"risk":"the straps turn and are redrawn","prevented_by":"level, never turning; HOLD-PC"},{"risk":"one strap slides off","prevented_by":"small lift and settle; no strap sliding off"},{"risk":"a third strap appears or one vanishes","prevented_by":"no third strap, no one strap only"}], sm="in_place", hc=False),
 dict(beat="BR-064", shot="act6_copy_sags", cam=R1C, subject="THE SAME LEG AND CHEAP COPY STRAP as in the start frame; unchanged in every respect.",
  framing="CU as in the start frame: low, shin height, profile. FOCUS: the copy on the shin is sharp.",
  motion="CONTINUING: the stretched copy strap hangs loose below the knee. COMPLETING: one slow sag, about two seconds — the slack band slips a little further down the shin, the shell tilting as it goes, then catches and stops. UNRESOLVED: it hangs loose on the shin, the knee bare above it.",
  style="Unremarkable phone clip, soft kitchen window daylight, no grade.",
  negs="no wordmark, no chrome, no strap falling off the leg, no leg moving, no hands, no face, no music",
  risks=[{"risk":"the copy gains a wordmark or chrome","prevented_by":"no wordmark, no chrome"},{"risk":"it drops off the leg entirely","prevented_by":"slips a little then catches; no strap falling off"},{"risk":"the leg moves and blurs","prevented_by":"no leg moving"}], sm="in_place", hc=False),
 dict(beat="BR-065", shot="act6_steps_down", cam=LOCK, subject="THE SAME WOMAN as in the start frame, polka-dot dress, coral cardigan, strap on her right knee; unchanged in every respect.",
  framing="FULL as in the start frame: low at the foot of the steps, looking up at her. FOCUS: deep.",
  motion="CONTINUING: she is already stepping down, right foot lowering onto the next step, left hand light on the railing. COMPLETING: two easy steps down towards the lens, about three seconds — each foot lands and takes her weight, the knee bending freely over it, her smile holding. UNRESOLVED: she keeps coming down, still on the steps, in frame." + HPC,
  style="Unremarkable phone clip, low warm afternoon sun raking across the steps, no grade.",
  negs="no gripping the rail hard, no stumbling, no stiff leg, no strap sliding, no dress over the strap, no walking past the camera, no talking, no music",
  risks=[{"risk":"she stumbles or the steps warp","prevented_by":"two easy steps, feet landing and taking the weight; NEG warp"},{"risk":"the strap slides as the knee bends","prevented_by":"HOLD-PC; no strap sliding"},{"risk":"the camera travels with her","prevented_by":"locked-off camera"}], sm="travels", hc=False),
]
C = sys.argv[1]
for b in B:
    card = json.load(open(C + f"stryde-three-regrets__{b['beat']}.json"))
    prompt = json.dumps({"shot": b["shot"], "subject": b["subject"], "camera": {"movement": b["cam"], "framing": b["framing"]},
                         "motion": b["motion"] + " " + HOLD_C + (" " + HOLD_HC if b.get("hc", True) else "") + " " + PHYS, "lighting": CAP,
                         "style": b["style"], "negatives": NEGW + ", " + b["negs"]}, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": b["beat"], "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt,
            "duration": card["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": card["imageUrl"], "start_approved": card["imageStatus"] == "confirmed",
            "pinned": False, "subject_motion": b["sm"], "prefer_multi_shots": "false", "generation": 1, "risks": b["risks"]}
    json.dump(call, open(D + f"{b['beat']}.call.json", "w"), ensure_ascii=False, indent=1)
    open(D + f"{b['beat']}.kie_prompt.txt", "w").write(prompt)
    print(b["beat"], card["duration"], len(prompt))
