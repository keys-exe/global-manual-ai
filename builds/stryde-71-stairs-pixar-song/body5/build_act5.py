#!/usr/bin/env python3
"""Act 5 (PR-01a…PR-06a) A/B image pairs + the M-06a Fix "wrong product and she should be going down the stairs not side ways" (2026-10-02 ~11:45).
Constants come from body4/build_act4.py (its header, up to the beat table). §6A, §24O, preflight.py "kind": "image"."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
hdr = src[src.index("import json"):src.index("J = {}")]
g = {"__file__": str(B4 / "build_act4.py")}
exec(hdr.replace("H = Path(__file__).parent", "H = Path(__file__).parent"), g)
ref, L, ID, FRONT, BACK, WORN, P0, P7, STH, P04A = (g[k] for k in ("ref", "L", "ID", "FRONT", "BACK", "WORN", "P0", "P7", "STH", "P04A"))
SPLIT, PLAIN, HALL, KIT, CLIN, TASTE, TASTE_P, PF = (g[k] for k in ("SPLIT", "PLAIN", "HALL", "KIT", "CLIN", "TASTE", "TASTE_P", "PF"))
N_R07F = ref("R-07a frame v8 A (confirmed) — N's skin and hands (HT27); the day-five clothes are written in words", "frame", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
SHAPE = "the strap of Image 1 copied exactly — a black shell, two pointed peaks round a notch, a chrome slide at each end —"
SHAPE_L = "the strap of Image 1 copied exactly — a black shell with two pointed peaks round a centre notch and its wordmark, a chrome slide at each end, a black band round the back of the knee —"
J = {}
J["M-06a"] = (B4, "v4", f'''For the line "{L("M-06a")}": Staircase of Image 2, tall 9:16. Image 1 is the strap. Image 3 is the woman — her deep brown skin, tan slippers and denim skirt exactly as in Image 3. Image 4 is the style.
Low close shot from the foot of the stairs straight up the flight, she comes down facing the lens, sharp on her right leg: her right slipper stepping down onto the next tread's runner, toes to the lens, her left slipper on the tread above; above, her bare right knee with {SHAPE_L} 12 × 5 cm, a quarter of the frame wide, its front to the lens; hands out of frame. Scale true to the set: each slipper as long as the tread is deep.
In frame: two feet, two shins, one strap, three treads; the rest as Image 2, soft.
{HALL} {SPLIT} {PLAIN}''', [FRONT, P0, N_R07F, STH], False, True, True, True, None,
 'user Fix "wrong product and she should be going down the stairs not side ways" → from the foot of the stairs straight up the flight, she steps down toward the lens; the strap spelled out (shell, two peaks round the notch, chrome slides, band round the back); earlier Fixes in force: "i want a close up shot of the feet", "wrong person" (her own skin and slippers, HT27)')
J["PR-01a"] = (H, "v1", f'''For the line "{L("PR-01a")}": A front porch, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 3 is the style.
Close-up from above at a three-quarter angle, his own view of his knee, he faces the lens's left, sharp on the strap: a man of sixty-odd with grey stubble and warm tan skin, in a faded blue T-shirt and khaki shorts, sits on a wooden porch step; both hands slide {SHAPE} 12 × 5 cm, a third of the frame wide, up his bare right shin to just under the kneecap, his fingers on the band's two ends, four chunky fingers and a thumb on each hand; his left knee bare beside it, a canvas shoe on the step below. Scale true to the set: his knee a third of the frame wide, each porch board a hand wide.
In frame: two knees, two hands, one strap, three porch boards; every other surface plain.
A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun. {SPLIT} {PLAIN}''', [FRONT, WORN, STH], False, True, False, True, None, None)
J["PR-02a"] = (H, "v1", f'''For the line "{L("PR-02a")}": Clinic room of Image 3, tall 9:16. Image 1 is the strap, Image 2 its back. Image 4 is the style.
Medium close-up at eye level from a three-quarter angle, sharp on the strap: an approachable sports doctor, a woman in her forties, warm brown skin, short natural hair, navy polo, seated at her desk facing the lens, a warm closed-mouth smile, eyes on the lens; her right hand holds up {SHAPE} 12 × 5 cm, a quarter of the frame wide, its front to the lens, beside a plastic knee model on the desk; her left hand on the model, four chunky fingers and a thumb on each hand. Scale true to the set: the desk at her waist, the model as tall as her forearm.
In frame: her, the strap, the knee model; the desk otherwise bare, the rest as Image 3, soft.
{CLIN} {SPLIT} {PLAIN}''', [FRONT, BACK, P7, STH], True, True, True, True, None, None)
J["PR-03a"] = (H, "v1", f'''For the line "{L("PR-03a")}": A golf course, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 3 is the style.
Medium-full shot from a low angle, seen from his right side, he faces frame left at the finish of his swing, sharp on him: a Black man of seventy-six, close grey hair, short grey beard, lemon golf polo, khaki shorts, white golf shoes — weight on his left foot, right heel up, the club wrapped over his shoulder, both hands on the grip, four chunky fingers and a thumb on each, a satisfied closed-mouth smile, looking at the far green; on his bare right knee, nearest the lens, {SHAPE} 12 × 5 cm, a fifth of the frame wide, its front to the lens. Scale true to the set: he fills two thirds of the frame height, the flag far behind him, small.
In frame: him, the fairway grass, sky; nobody else.
A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun. {SPLIT} {PLAIN}''', [FRONT, WORN, STH], True, True, False, True, None, None)
J["PR-04a"] = (H, "v1", f'''For the line "{L("PR-04a")}": A running track, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 3 is the style.
Medium-full shot at eye level from a three-quarter front angle, she jogs toward frame left past the lens, sharp on her: a young Black woman of twenty-two, hair in a high puff, white running top, black shorts, white trainers, mid-stride on a red track with white lane lines — her right foot just landing, left foot lifting behind, arms bent at her sides, four chunky fingers and a thumb on each loose hand, a bright closed-mouth smile, looking ahead down the lane; on her bare right knee {SHAPE} 12 × 5 cm, a fifth of the frame wide. Scale true to the set: she fills two thirds of the frame height, her stride as long as a lane is wide.
In frame: her, two lanes, the infield grass soft behind; no other runners.
A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun. {SPLIT} {PLAIN}''', [FRONT, WORN, STH], True, True, False, True, None, None)
J["PR-04a"] = (H, "v2", f'''For the line "{L("PR-04a")}": A running track, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 3 is the style.
Medium-full shot at eye level from a three-quarter front angle, she jogs toward frame left past the lens, sharp on her: a young Black woman of twenty-two, hair in a high puff, white running top, black shorts, white trainers, mid-stride on a red track — her right foot just landing, left foot lifting behind, arms bent at her sides, four chunky fingers and a thumb on each loose hand, a bright closed-mouth smile, looking ahead down the lane; on her bare right knee {SHAPE} 12 × 5 cm, a fifth of the frame wide. Scale true to the set: she fills two thirds of the frame height.
In frame: her, exactly one strap on her right knee, her left leg bare from hip to shoe, two lanes, the infield grass soft behind; no other runners.
A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun. {SPLIT} {PLAIN}''', [FRONT, WORN, STH], True, True, False, True, None, 'kept off twice (L16): v1 A and its re-render each drew two straps on one leg → the frame inventory now counts exactly one strap, on her right knee, and her left leg bare')
J["PR-05a"] = (H, "v1", f'''For the line "{L("PR-05a")}": Her bedroom in the morning, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 3 is the woman — her skin and hands as in Image 3; today a pale-yellow nightgown to the knee. Image 4 is the style.
Close-up from above at a three-quarter angle, her own view of her knee, she faces the lens, sharp on the strap: she sits on her bed's edge, the nightgown's hem above her bare right knee; both hands slide {SHAPE} 12 × 5 cm, a third of the frame wide, the last few centimetres to just under the kneecap, four chunky fingers and a thumb on each hand; her left knee bare beside it; the white quilt's edge, the oak floor below. Scale true to the set: her knee a third of the frame wide.
In frame: two knees, two hands, one strap, the quilt edge; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, WORN, N_R07F, STH], False, True, False, True, None, None)
J["PR-05b"] = (H, "v1", f'''For the line "{L("PR-05b")}": Her bedroom in the morning, tall 9:16. Image 1 is the strap. Image 2 is the woman — her deep brown skin exactly as in Image 2; today she wears navy cotton trousers. Image 3 is the style.
Close-up at knee height from her right side, her right leg in profile with her toes to frame left, sharp on the knee: she sits on the edge of her bed, and her navy trouser leg is falling from above the knee, its hem halfway down over {SHAPE} 12 × 5 cm, a third of the frame wide, the top of the shell still showing just under the kneecap; her hands out of frame; the white quilt's edge behind, the oak floor below. Scale true to the set: her knee a third of the frame wide, the bed edge at her knee.
In frame: one leg, the trouser leg, the strap, the quilt edge; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, N_R07F, STH], False, True, False, True, None, None)
J["PR-06a"] = (H, "v1", f'''For the line "{L("PR-06a")}": Keep this photo exactly as it is — the round wooden kitchen table, the chairs, the floor, the morning light, the view from above — and change only what is on the table: clear it. Image 1 is the photo, the film's own style. Image 2 is the strap.
On the bare table, seen from directly above: one white coffee mug with a thin curl of steam, and beside it the strap of Image 2 copied exactly — a black shell with two pointed peaks round a centre notch and its wordmark, a chrome slide at each end, the black band coiled loosely — 12 × 5 cm, lying flat front up, a quarter of the frame wide. Nothing else on the table, the wood bare all round them.
In frame: the table, one mug, one strap; the rest as Image 1.
{KIT} {SPLIT} {PLAIN}''', [P04A, FRONT], False, False, True, True, P04A, None)
fails = 0
ONLY = sys.argv[1:]
for b, (d, tag, pr, refs, face, body, room, prod, eo, fn) in J.items():
    if ONLY and b not in ONLY: continue
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": ("frame" if eo["kind"] == "frame" else "plate") if eo else None, "edit_of": eo["job"] if eo else None,
         "taste": TASTE_P if prod else TASTE, "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": prod, "risk_class": "stairs" if b == "M-06a" else None, "first_frame": False,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (d / f"{b}.{tag}.prompt.txt").write_text(pr); (d / f"{b}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(d / f"{b}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
