#!/usr/bin/env python3
"""Fix round 2026-10-02 ~12:30 ("fix those and generate the next act"):
 - M-06a "wrong locastion" → an image edit of her own staircase: a crop of the confirmed R-07a v8 A frame round her legs (Image 1), the strap corrected from front.webp.
 - PR-03a "fwrong product", PR-06a "wrong product" → the shape line now carries the product sheet's placement of the peaks: two matching pointed peaks close together
   at the middle of the top edge, one kneecap wide, the shell sloping down to a slide at each end (the short line let the peaks drift to the ends as horns).
 - PR-05b "product placemetn is too low" → the notch cups the bottom of the kneecap, on the tendon, never lower on the shin (product sheet §placement 3).
 - Act 6 (L-01a…L-03a), the store-walk day N-D6, first pairs: street and store shots are edits of their plates (HT17), N by her face-and-hair crop (HT26).
Constants from body4/build_act4.py's header. §6A, §24O, preflight.py "kind": "image"."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
g = {"__file__": str(B4 / "build_act4.py")}
exec(src[src.index("import json"):src.index("J = {}")], g)
ref, L, ID, FRONT, WORN, P0, STH, P04A, M = (g[k] for k in ("ref", "L", "ID", "FRONT", "WORN", "P0", "STH", "P04A", "M"))
SPLIT, PLAIN, HALL, KIT, TASTE, TASTE_P, PF = (g[k] for k in ("SPLIT", "PLAIN", "HALL", "KIT", "TASTE", "TASTE_P", "PF"))
N_R07F = ref("R-07a frame v8 A (confirmed) — N's skin and hands (HT27); the day's clothes are written in words", "frame", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
CROP = ref("R-07a frame v8 A (confirmed), cropped round her legs on her own staircase — the picture this edit keeps", "frame", "6279fb3c-1576-438f-ad78-54c777179d89", ID + "R-07a")
P6 = ref("P6-STREET plate (confirmed) — her tree-lined street", "location", "0de1960b-34b2-44bd-b2f5-cc6e1f98cd60", ID + "P6-STREET")
P4 = ref("P4-STORE plate (confirmed) — the store and its checkout", "location", "057a1f56-033c-4b52-80c2-a2e2c122ce13", ID + "P4-STORE")
NF = ref("N-NARR face-and-hair crop of the confirmed sheet v2 (HT26, no clothes)", "character", M["N_face"], ID + "N-NARR")
NFB = ref("N-NARR face-and-hair crop of the confirmed sheet v2 — her hair from behind (HT26, HT27)", "frame", M["N_face"], ID + "N-NARR")
def SH(n): return (f"the strap of Image {n} copied exactly — a black shell with two matching pointed peaks close together at the middle of its top edge, "
                   "a notch between them, sloping down to a chrome slide at each end —")
SUN = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun."
STORE = "A final frame from a 3D animated feature film, stylized storybook render, soft overhead store light."
LIV = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon window light."
D6 = "a coral windbreaker over a white T-shirt, light-blue straight jeans, white walking sneakers"
J = {}
J["M-06a"] = ("v5", f'''For the line — {L("M-06a")} —: Keep this picture exactly as it is — her own staircase: the beige runner, the brass stair rods, the white balusters at frame left, her denim skirt, brown legs and closed tan slippers — redrawn sharp. Image 1 is the picture. Image 2 is the strap.
She steps down toward the lens: right slipper landing on the next tread, left slipper on the tread above, hands out of frame. Correct only the strap on her right knee at frame left: {SH(2)} 12 × 5 cm, a quarter of the frame wide, its notch cupping the bottom of the kneecap, the band round the back of the knee. Scale true to the set: each slipper as long as a tread is deep.
In frame: two legs, two slippers, exactly one strap on her right knee, five treads of the runner; nothing else.
{HALL} {SPLIT} {PLAIN}''', [CROP, FRONT], False, True, True, True, CROP,
 'user Fix "wrong locastion" → an image edit of her own staircase (a crop of the confirmed R-07a v8 A frame); earlier Fixes in force: "i want a close up shot of the feet", "wrong person", "wrong product and she should be going down the stairs not side ways"')
J["PR-03a"] = ("v2", f'''For the line — {L("PR-03a")} —: A golf course, tall 9:16. Image 1 is the strap, Image 2 it worn. Image 3 is the style.
Medium-full shot from low at his right front, facing frame left at his swing's finish, sharp on the strap: a Black man of seventy-six, grey hair and beard, lemon polo, khaki shorts, golf shoes — the club over his shoulder in both hands, four chunky fingers and a thumb on each, a closed-mouth smile, looking at the far green; on his bare right knee, nearest the lens, {SH(1)} 12 × 5 cm, a fifth of the frame wide, its notch cupping the bottom of the kneecap. Scale true to the set: he fills two thirds of the frame height.
In frame: him, exactly one strap on his right knee, his left knee bare, fairway, sky; nobody else.
{SUN} {SPLIT} {PLAIN}''', [FRONT, WORN, STH], True, True, False, True, None,
 'user Fix "fwrong product" → the peaks were drawn as horns at the shell\'s two ends; the shape line now puts two matching peaks close together at the middle, one kneecap wide, sloping down to a slide at each end')
J["PR-05b"] = ("v2", f'''For the line — {L("PR-05b")} —: Her bedroom in the morning, tall 9:16. Image 1 is the strap. Image 2 is the woman — her deep brown skin exactly as in Image 2. Image 3 is the style.
Close-up at knee height from her right side, her right leg in profile with her toes to frame left, sharp on the knee: she sits on her bed's edge, her navy cotton trouser leg falling from above the knee, its hem halfway down over {SH(1)} 12 × 5 cm, a third of the frame wide, its notch cupping the bottom of the kneecap, on the tendon, never lower on the shin; her hands out of frame; the quilt edge behind. Scale true to the set: her knee a third of the frame wide.
In frame: one leg, the trouser leg, exactly one strap, the quilt edge; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, N_R07F, STH], False, True, False, True, None,
 'user Fix "product placemetn is too low" → the notch cups the bottom of the kneecap, on the tendon, never lower on the shin')
J["PR-06a"] = ("v2", f'''For the line — {L("PR-06a")} —: Keep this photo exactly as it is — the round wooden kitchen table, the chairs, the floor, the morning light, the view from above — and change only what is on the table: clear it. Image 1 is the photo. Image 2 is the strap.
On the bare table, seen from directly above: one white coffee mug with a thin curl of steam, and beside it {SH(2)} with its wordmark, the black band laid out straight to each side exactly as Image 2 shows it, never coiled or looped — 12 × 5 cm, lying flat front up, a quarter of the frame wide.
In frame: the table, one mug, exactly one strap; the rest as Image 1.
{KIT} {SPLIT} {PLAIN}''', [P04A, FRONT], False, False, True, True, P04A,
 'user Fix "wrong product" → the band was drawn coiled and the peaks at the ends; now the strap lies flat as front.webp shows it, the band straight out to each side, the peaks together at the middle')
J["L-01a"] = ("v1", f'''For the line — {L("L-01a")} —: Keep this photo exactly as it is — the tree-lined street, the sidewalk, the mailboxes, the red-brick house, the afternoon sun — a tall 9:16 crop looking down the sidewalk, and add her walking away. Image 1 is the street. Image 2 is the woman — her silver twist-out only. Image 3 is the style.
Medium shot from behind at eye level, sharp on her: her back to the lens, facing down the sidewalk, she walks away down its middle, mid-stride, her left foot forward, in {D6}, a canvas tote on her right shoulder, her right hand on its strap, her left arm swinging, four chunky fingers and a thumb on each hand. Scale true to the set: her head level with the top of the mailbox post's box.
In frame: her, the sidewalk, two trees, the street; nobody else; every other surface as in Image 1.
{SUN} {PLAIN}''', [P6, NFB, STH], False, True, True, False, P6, None)
J["L-01b"] = ("v1", f'''For the line — {L("L-01b")} —: Keep this photo exactly as it is — the tree-lined street, the sidewalk, the mailboxes, the afternoon sun — a tall 9:16 crop along the sidewalk, and add four women. Image 1 is the street. Image 2 is the woman — her face and silver twist-out only. Image 3 is the style.
Medium shot from a low angle at her front three-quarter, she walks facing frame right, sharp on her: the woman of Image 2 in {D6}, a canvas tote on her right shoulder, her right hand on its strap, her left arm swinging, a small closed-mouth smile, looking ahead; she draws level with three women in their thirties strolling slowly side by side on her left, each holding a coffee cup in one hand, the other loose, each hand four chunky fingers and a thumb, chatting. Scale true to the set: all four the same height, the mailbox at their waists.
In frame: four women, the sidewalk, two trees; nobody else.
{SUN} {PLAIN}''', [P6, NF, STH], True, True, True, False, P6, None)
J["L-02a"] = ("v1", f'''For the line — {L("L-02a")} —: Keep this photo exactly as it is — the store, the checkout counter, the overhead light — a tall 9:16 crop of the lane, and add her. Image 1 is the store. Image 2 is the woman — her face and silver twist-out only. Image 3 is the style.
Medium shot at eye level from her front three-quarter, sharp on her eyes: facing frame left toward the counter, she stands square in the checkout line, both feet planted side by side, in {D6}, a full red basket in her right hand, her left hand loose at her side, four chunky fingers and a thumb on each, a small closed-mouth smile, looking ahead at the counter; two shoppers ahead, backs to the lens, each lifting groceries onto the belt with both hands. Scale true to the set: the counter at her waist.
In frame: three people, one basket, the counter with its belt and card reader; every other surface bare, packaging plain.
{STORE} {PLAIN}''', [P4, NF, STH], True, True, True, False, P4, None)
J["L-02b"] = ("v1", f'''For the line — {L("L-02b")} —: Keep this photo exactly as it is — the red-brick house, its white porch with two rocking chairs, the front path, the lawn, the afternoon sun — a tall 9:16 crop of the path to the porch, and add her walking up it. Image 1 is the street. Image 2 is the woman — her silver twist-out only. Image 3 is the style.
Medium shot from a low angle behind her, three-quarter, sharp on her: her back to the lens, facing the porch, she walks up the front path toward the porch steps, mid-stride, her right foot forward, in {D6}, a paper grocery bag in each hand at her sides, arms straight, four chunky fingers and a thumb round each bag's top. Scale true to the set: her head level with the porch rail.
In frame: her, two bags, the path, the porch; nobody else; every other surface as in Image 1.
{SUN} {PLAIN}''', [P6, NFB, STH], False, True, True, False, P6, None)
J["L-03a"] = ("v1", f'''For the line — {L("L-03a")} —: Her living room, tall 9:16 — the greige walls, white six-panel door and oak floor of Image 1. Image 2 is the woman — her face and silver twist-out only. Image 3 is the style.
Medium shot at eye level from a three-quarter angle, sharp on his eyes: her husband, a Black man of about eighty, bald, white moustache, brown cardigan, sits in a brown recliner at frame left facing frame right, lowering a newspaper with blank pages onto his lap with both hands, looking up at her with a raised eyebrow, mouth closed; at frame right in the open doorway she stands in {D6}, a paper grocery bag in each hand at her sides, four chunky fingers and a thumb on each hand, looking at him with a small knowing closed-mouth smile. Scale true to the set: the door handle at her hip.
In frame: two people, one recliner, two bags, the doorway; every other surface plain.
{LIV} {PLAIN}''', [P0, NF, STH], True, True, True, False, None, None)
fails = 0; ONLY = sys.argv[1:]
for b, (tag, pr, refs, face, body, room, prod, eo, fn) in J.items():
    if ONLY and b not in ONLY: continue
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": ("frame" if eo and eo["kind"] == "frame" else "plate") if eo else None, "edit_of": eo["job"] if eo else None,
         "taste": TASTE_P if prod else TASTE, "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": prod, "risk_class": "stairs" if b == "M-06a" else None, "first_frame": False,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.{tag}.prompt.txt").write_text(pr); (H / f"{b}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
