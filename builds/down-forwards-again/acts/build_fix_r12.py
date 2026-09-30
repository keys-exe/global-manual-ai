#!/usr/bin/env python3
"""Step 7 · image Fix round 12 (hourly Fix check, 2026-09-30 11:41 UTC; board Fix notes on the round-11 images). One render each, to the board To check.
  BR-10c v3  "i want a new one here" → a new composition: close on the knee from a low three-quarter front angle, the load drawn as bright red pulses
             travelling down the thigh and landing on the tendon as the foot meets the step (v2 was the whole leg in profile).
  BR-16a2 v2 "wrong product" and BR-16b v3 "wrong product" → both rendered big padded open-kneecap braces. Now: the strap is described by what the
             knee shows (the kneecap fully bare above it, a thin band, a small curved shell below the kneecap only), the worn reference attached FIRST,
             brace/sleeve/open-patella negatives, and the camera closer so the strap is large enough to read (BR-16b: four walkers, not eight).
  BR-20c v2  "fix this cause its distorted" → v1 drew two crossed legs; now ONE leg only, the other entirely out of frame, no crossing.
Bases: the round-11 prompts (acts/<beat>.image.r11.prompt.txt), exact replacements asserted."""
import json, pathlib
here = pathlib.Path(__file__).parent
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
r11 = lambda b: (here / f"{b}.image.r11.prompt.txt").read_text()
R = dict(FRONT="c942d91d-718d-4723-b190-ad85186ac8d9", TQ="4a56cffe-69bc-4f77-ac90-38258b124e65", WORN="793ca329-e4b3-49fd-943c-5e97bae5366d")
LOOK = ("WHAT THE STRAP LOOKS LIKE ON A KNEE — exactly as in the FIRST attached photograph of it worn: the whole kneecap stays BARE and fully visible, "
        "nothing covers it or rings it; just below the kneecap sits one small curved matte-black shell about three centimetres tall, as wide as the front of the knee, "
        "and from its two ends a thin flat black band only two fingers wide runs round the back of the leg. That is all of it — no padding, no "
        "sleeve, no hole for the kneecap, no straps above the knee, no hinges. From a few metres away it reads as a thin black line under the kneecap. ")
NEG_BRACE = ("no knee brace, no knee sleeve, no knee support, no open-patella brace, no ring round the kneecap, no hole around the kneecap, no padding, "
             "no neoprene, no straps above the knee, no hinges, no wraps, no strap covering the kneecap, no thick strap, ")
OUT = {}
t = r11("BR-16a2")
t = rep(t, [("the two surgeons and the knee in one frame.", "close enough that the patient's knee and the surgeon's hands fill the lower half of the frame, the two surgeons above."),
            ("The product exactly as in the attached reference image", LOOK + "The shell's front face is exactly as in the second attached reference image"),
            ("AVOID: ", "AVOID: " + NEG_BRACE)])
OUT["BR-16a2"] = dict(v=2, refs=[R["WORN"], R["FRONT"]], prompt=t)
t = r11("BR-16b")
t = rep(t, [("a few metres ahead of the group", "a couple of metres ahead of the group"),
            ("A walking group of eight older people", "A walking group of four older people"),
            ("The front walkers are a few metres from the lens, the rest behind them; faces and knees both read.",
             "The front two are about two metres from the lens, the other two just behind them; faces and knees both read clearly, the knees large in frame."),
            ("On the knees of four of them — the two nearest and two further back — the same knee strap.", "On the LEFT knee of the two nearest walkers, the same knee strap."),
            ("The product exactly as in the attached reference image", LOOK + "The shell's front face is exactly as in the second attached reference image"),
            ("The other four wear nothing on their knees.", "The other two wear nothing on their knees."),
            ("no crowd of more than eight,", "no more than four people,"), ("AVOID: ", "AVOID: " + NEG_BRACE)])
OUT["BR-16b"] = dict(v=3, refs=[R["WORN"], R["FRONT"]], prompt=t)
t = r11("BR-20c")
t = rep(t, [("A stylised anatomical model of a single left knee in true lateral profile,",
             "A stylised anatomical model of ONE single left leg only — the other leg entirely out of frame, nothing crossing it — the knee in true lateral profile,"),
            ("no second limb,", "no second limb, no second leg, no crossed legs, no legs overlapping, no extra thigh, no extra shin, no double knee, no bent or broken bones,")])
OUT["BR-20c"] = dict(v=2, refs=[R["FRONT"], R["TQ"]], prompt=t)
t = r11("BR-10c")
t = rep(t, [("A stylised anatomical model of a whole left leg seen from a low three-quarter front angle, from the hip down to the foot, the foot just landing flat on a simple dark floor a step down from a simple dark step behind it, the knee bending to take the weight, the leg dominating the frame",
             "A stylised anatomical model of ONE left leg seen close from a low three-quarter front angle, framed from mid-thigh down to the foot, the foot just landing flat on the edge of a simple dark step, the knee bending a little to take the weight, the knee large in the middle of the frame, the other leg entirely out of frame"),
            ("a stream of warm red light runs down through the thigh like a current, from the hip to the knee, and pours into one point",
             "three bright red pulses of light travel down through the thigh one after another like a current, from the top of the frame to the knee, and pour into one point"),
            ("no second limb,", "no second limb, no second leg, no crossed legs,")])
OUT["BR-10c"] = dict(v=3, refs=[], prompt=t)
for b, o in OUT.items():
    assert "[" not in o["prompt"], b
    (here / f"{b}.image.r12.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(f"{b:8s} v{o['v']} {len(o['prompt']):5d}")
json.dump(OUT, open(here / "fix_r12.json", "w"), indent=1)
json.dump([{"index": 1300 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r12_batch.json", "w"), ensure_ascii=False)
