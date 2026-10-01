#!/usr/bin/env python3
"""Step 7 · image Fix round 16 (the user, 2026-10-01: "fix those and generate the next ones"; board Fix notes). One render each, to the board To check.
  BR-16a v6 "remove those silver dots on the body" → v5 had motion-capture markers taped on his leg and shorts. An edit of v5 (attached first):
            everything kept, the markers removed from his body and clothes (the ones on stands stay in the room).
  BR-23 v4  "the product is wrong" → v3 drew a chunky block sitting ON the kneecap. An edit of v3 (attached first): the strap redrawn as it really is
            on a knee — kneecap bare, a small curved shell just below it, a thin band (round-12 LOOK line), the worn reference attached second,
            brace/sleeve negatives. Everything else in v3 kept.
Bases: acts/BR-16a.image.r13.prompt.txt, acts/BR-23.image.r14.prompt.txt (exact replacements asserted)."""
import json, pathlib
here = pathlib.Path(__file__).parent
def rep(t, pairs):
    for o, n in pairs:
        assert t.count(o) == 1, o[:80]; t = t.replace(o, n)
    return t
R = dict(FRONT="c942d91d-718d-4723-b190-ad85186ac8d9", WORN="793ca329-e4b3-49fd-943c-5e97bae5366d")
src = (here / "build_fix_r12.py").read_text()
ns = {}; exec(src[src.index("LOOK = ("):src.index("OUT = {}")], ns); LOOK, NEG_BRACE = ns["LOOK"], ns["NEG_BRACE"]
OUT = {}
t = (here / "BR-16a.image.r13.prompt.txt").read_text()
t = rep(t, [("EDIT THE FIRST ATTACHED PHOTOGRAPH: keep the same gait lab, the same volunteer, his clothes, the strap on his left knee, the light and the camera "
             "height exactly as they are, and change only the equipment and his action.",
             "EDIT THE FIRST ATTACHED PHOTOGRAPH: keep everything exactly as it is — the gait lab, the treadmill, the volunteer, his pose, his clothes, the strap "
             "on his left knee, the monitor, the light and the camera height — and change only one thing: remove every reflective marker from his body and "
             "clothes. His skin, shorts and t-shirt are plain, with nothing taped or stuck on them."),
            (", small round reflective markers taped on his leg —", " — nothing taped or stuck on his body —"),
            ("AVOID: ", "AVOID: no reflective markers on his body, no silver dots, no grey dots, no sensors on his legs, no stickers, no tape on his skin, no markers on his shorts, ")])
OUT["BR-16a"] = dict(v=6, refs=["4a486ee5-3179-434d-9424-bbe98fdbacb7", R["WORN"], R["FRONT"]], prompt=t)
t = (here / "BR-23.image.r14.prompt.txt").read_text()
P = t.split("\n\n")
P.insert(3, "EDIT THE FIRST ATTACHED PHOTOGRAPH: keep everything exactly as it is — the stairs, the hall, the window, the woman, her pose, her dress, "
            "cardigan and sandals, the light and the camera — and change only the strap on her LEFT knee, redrawn as it really looks on a knee. "
            + LOOK.replace("exactly as in the FIRST attached photograph of it worn", "exactly as in the SECOND attached photograph, of it worn"))
assert "SECOND attached photograph" in P[3]
t = "\n\n".join(P)
t = rep(t, [("AVOID: ", "AVOID: " + NEG_BRACE + "no strap on the kneecap, no block on the knee, "),
            ("The product exactly as in the attached reference image", "The shell's front face is exactly as in the third attached reference image")])
t = t.replace("THE SAME WOMAN, in the same clothes, as in the first attached photograph and the attached reference sheet",
              "THE SAME WOMAN, in the same clothes, as in the first attached photograph", 1)
OUT["BR-23"] = dict(v=4, refs=["a9d04c6e-8793-4802-98d5-5df883a56d71", R["WORN"], R["FRONT"]], prompt=t)
for b, o in OUT.items():
    assert "[" not in o["prompt"], b
    (here / f"{b}.image.r16.prompt.txt").write_text(o["prompt"]); o["model"] = "nano_banana_pro"; print(f"{b:8s} v{o['v']} {len(o['prompt']):5d}")
json.dump(OUT, open(here / "fix_r16.json", "w"), indent=1)
json.dump([{"index": 1600 + i, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
            "medias": [{"role": "image_references", "value": j} for j in o["refs"]], "prompt": o["prompt"]}} for i, o in enumerate(OUT.values())],
          open(here / "fix_r16_batch.json", "w"), ensure_ascii=False)
