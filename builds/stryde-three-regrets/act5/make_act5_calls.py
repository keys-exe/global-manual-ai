"""Act 5 clip calls (§35 JSON on Kie kling-3.0-omni). The first Act 5 clip batch (8 beats) was built in the
previous session and its call files were lost with its container; this file rebuilds BR-043 (the one clip
that never landed) in the same shape as act4/make_act4_calls.py."""
import json, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/../act4")
D = os.path.dirname(os.path.abspath(__file__)) + "/"
R1C = "Already drifting on frame one. Low breath sway throughout, vertical with slight roll. Brief focus hunt at entry. One late partial reframe. Camera lags the subject, never anticipates. Still drifting at the cut."
HOLD_C = "Everything in frame keeps the exact form, proportion and count it has in the start frame, first frame to last — nothing melts, merges, splits, grows or becomes something else. One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning."
HOLD_HC = "Same person, face and wardrobe every frame; five separate fingers on each hand, never fusing or passing through anything; limbs keep their length and bend only as real joints bend."
PHYS = "Mass and momentum in all movement: heavy starts and settles slow, nothing at uniform speed, nothing stops instantly — motions decelerate into a settle or small overshoot; actions travel through the body, weight transferring first, hands arriving last; hair, fabric and straps lag and keep moving after the body stops; objects drag with friction, never glide."
CAP = "Capture characteristics exactly as in the start frame — same tone-mapping, same noise, same colour temperature. No grading change across the clip."
NEGW = "no morphing, no warping, no melting, no shape shifting, no merging, no splitting, no parts detaching, no proportions changing, no duplicate objects, no background bending, no texture swimming, no smearing, no flickering geometry, no flickering light, no exposure pumping"
N = "no glancing at the lens, no talking, no slow motion, no music"

B = [dict(
    beat="BR-043", shot="act5_front_path",
    subject="THE SAME WOMAN as in the start frame, copper bob, white blouse, sage-green linen trousers to the ankle; unchanged in every respect.",
    framing="FULL as in the start frame: low, waist height in front of her on the path near the gate, looking up the path at her, from the front. FOCUS: deep; the path, her and the house stay sharp.",
    motion="CONTINUING: she is already mid-stride on her front path, right foot planted, left foot swinging through. COMPLETING: three easy steps towards the lens, about three seconds — each foot lands heel first and takes her weight, both knees bending freely, arms loose. UNRESOLVED: she slows near the gate, in frame head to shoes.",
    style="Unremarkable phone clip, warm midday sun on the front of the house, no grade.",
    negs="no strap, no knee support, no product, no limping, no running, no walking past the camera, no camera moving with her, " + N,
    risks=[{"risk": "the camera tracks with her and the walk turns to a glide", "prevented_by": "R1C sway only; no camera moving with her; feet land heel first and take her weight"},
           {"risk": "she walks out of frame or past the lens", "prevented_by": "three steps, slows near the gate, still in frame from head to shoes; no walking past the camera"},
           {"risk": "a strap reappears on the knee", "prevented_by": "start frame has none; no strap, no knee support, no product"}],
    sm="travels")]

C = sys.argv[1] if len(sys.argv) > 1 else "/tmp/cards/"
for b in B:
    card = json.load(open(C + f"stryde-three-regrets__{b['beat']}.json"))
    prompt = json.dumps({"shot": b["shot"], "subject": b["subject"], "camera": {"movement": R1C, "framing": b["framing"]},
                         "motion": b["motion"] + " " + HOLD_C + " " + HOLD_HC + " " + PHYS, "lighting": CAP,
                         "style": b["style"], "negatives": NEGW + ", " + b["negs"]}, ensure_ascii=False, separators=(",", ":"))
    call = {"beat": b["beat"], "connector": "kling", "mode": 1, "kind": "broll", "prompt": prompt,
            "duration": card["duration"], "resolution": "1080p", "aspect_ratio": "9:16",
            "start_image": card["imageUrl"], "start_approved": card["imageStatus"] == "confirmed",
            "pinned": False, "subject_motion": b["sm"], "prefer_multi_shots": "false", "generation": 1, "risks": b["risks"]}
    json.dump(call, open(D + f"{b['beat']}.call.json", "w"), ensure_ascii=False, indent=1)
    open(D + f"{b['beat']}.kie_prompt.txt", "w").write(prompt)
    print(b["beat"], card["duration"], len(prompt))
