#!/usr/bin/env python3
"""Fix round 2026-10-02 ~14:00 ("fix those and generate the next act") + Act 8 first pairs.
 - C-02a / C-02b "not a pixar" (user image Fix on both): the church ladies had no sheet and the only style frame showed hands on a table,
   so they came back with realistic proportions. Now their build is given in heads from the §24A elder ladder and the style frame is the
   PR-04a jogger — a confirmed full-body Pixar character, not Loretta (§24O rule 10, V7.90.9, L50).
 - Act 8: C-06a, C-07a, C-08a, C-08b, C-09a, C-09c. Wardrobe by story day (STEP4_5 map): C-06a/C-07a/C-09a N-D5 sheet outfit (mustard top,
   denim skirt), C-08a N-D0 (plum knit top, long grey skirt, pink slippers), C-08b N-D3 (R-07a frame), C-09c N-D7 (sheet outfit; the sister, navy).
Picture prompts open "For the line — … —:" (V7.90.7, L46). Constants from body4/build_act4.py's header."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
g = {"__file__": str(B4 / "build_act4.py")}
exec(src[src.index("import json"):src.index("J = {}")], g)
ref, L, ID, FRONT, P0, P04A, M = (g[k] for k in ("ref", "L", "ID", "FRONT", "P0", "P04A", "M"))
SPLIT, PLAIN, KIT, HALL, TASTE, TASTE_P, PF = (g[k] for k in ("SPLIT", "PLAIN", "KIT", "HALL", "TASTE", "TASTE_P", "PF"))
R07F = ref("R-07a frame v8 A (confirmed) — her own staircase from the hall, she coming down in her day-three clothes, the strap on her right knee", "frame", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
P5 = ref("P5-CHURCH plate (confirmed) — the church and its steps", "location", "020f7d83-d6e2-4744-9595-bef39ecf8f9f", ID + "P5-CHURCH")
NF = ref("N-NARR face-and-hair crop of the confirmed sheet v2 (HT26, no clothes)", "character", M["N_face"], ID + "N-NARR")
NS = ref("N-NARR sheet v2 (confirmed) — the sheet outfit, worn today (N-D5: mustard top, denim skirt)", "character", "32b8bfc2-4538-4c28-b485-3fd28fc5d489", ID + "N-NARR")
PIXP = ref("PR-04a frame v2 B (confirmed) — a full-body Pixar character, the build's body proportions (§24O rule 10)", "style", "027d407e-ad54-4f9a-9594-32cb4c047765", ID + "PR-04a")
PIXP["people"] = True
PKG = ref("package_open.jpg — the box, open, two straps in the tray (product photo)", "product", "33cf39f6-2945-410f-8ccf-d11e91538148", "products/stryde/stryde_refs/package_open.jpg")
LAND = ref("HK-03a frame v7 A (old version) — the view down her staircase from the landing, her mustard shoulder in the foreground (the picture this edit keeps)", "frame", "90555894-9918-4cd2-8548-df38ec0d7490", ID + "HK-03a")
def SH(n): return f"the strap of Image {n} copied exactly — a black shell, two matching peaks close together at the middle of its top edge, a chrome slide at each end —"
SUN = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun."
LIV = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon light from the front window."
GREY = "A final frame from a 3D animated feature film, stylized storybook render, cool grey morning light from the landing window above."
BODY = "about 5.5 heads tall, big round heads, soft round bodies, big eyes"
LADIES = f"three Black church ladies of seventy, each {BODY}, in Sunday dresses and wide hats — lilac, coral, cream —"
J = {}
J["C-02a"] = ("v2", f'''For the line — {L("C-02a")} —: Keep this photo exactly as it is — the red-brick church, its white columns, the wide steps with the black centre rail, the hedges, the sidewalk, the afternoon sun — a tall 9:16 crop at the foot of the steps, and add three women. Image 1 is the church. Image 2 is the style — the same render and character proportions as its runner.
Medium close-up at eye level from the sidewalk, sharp on them: {LADIES} stand side by side at the foot of the steps facing the lens; the middle one nudges the lady on her left and nods up the steps, all three eyes up the steps with knowing closed-mouth smiles, a small handbag in each near hand, four chunky fingers and a thumb on each. Scale true to the set: the bottom step at their ankles.
In frame: three women, the steps, the hedges; nobody else.
{SUN} {PLAIN}''', [P5, PIXP], True, True, True, False, P5, ["three church ladies"],
 'user image Fix "not a pixar" → the ladies drawn to the Pixar elder ladder (about 5.5 heads, big round heads, soft rounded bodies) with a full-body Pixar character as the style frame (§24O rule 10)')
J["C-02b"] = ("v3", f'''For the line — {L("C-02b")} —: Keep this photo exactly as it is — the church, its columns, steps, rail, hedges and sun — a tall 9:16 crop of the steps; add four women. Image 1 is the church. Image 2 is the woman — face and silver twist-out only. Image 3 is the style — its runner's render and proportions.
Medium shot from low at the foot of the steps, three-quarter, sharp on her: the woman of Image 2, about 5.5 heads tall, comes down facing the lens, mid-step on the third step from the bottom, hands free off the rail, in an emerald church dress, black pumps, a wide green hat, a proud closed-mouth smile, looking ahead; to one side at the foot {LADIES} watch her, hands clasped, four chunky fingers and a thumb on each hand. Scale true to the set: each step a shin high.
In frame: exactly four women, the steps; nobody else.
{SUN} {PLAIN}''', [P5, NF, PIXP], True, True, True, False, P5, ["three church ladies"],
 'user image Fix "not a pixar" → every woman drawn to the Pixar elder ladder (about 5.5 heads) with a full-body Pixar character as the style frame (§24O rule 10); earlier faults kept out: no titles (L16), exactly four women')
J["C-06a"] = ("v1", f'''For the line — {L("C-06a")} —: Her living room in the afternoon, tall 9:16, the greige walls and white doors of Image 3's house. Image 1 is the strap. Image 2 is the woman, in the outfit of Image 2. Image 3 is her house. Image 4 is the style.
Medium close-up at eye level, front-on, sharp on the straps: she sits on a soft sage sofa facing the lens and holds up two straps, one in each hand at shoulder height, fronts to the lens — each {SH(1)} 12 × 5 cm, a fifth of the frame wide, a short stub of band past each slide — eyes on the left one, a closed-mouth grin, four chunky fingers and a thumb on each hand. Scale true to the set: the sofa back level with her shoulders.
In frame: her, the sofa, exactly two straps, one in each hand; every other surface bare.
{LIV} {SPLIT} {PLAIN}''', [FRONT, NS, P0, PIXP], True, True, True, True, None, None, None)
J["C-07a"] = ("v1", f'''For the line — {L("C-07a")} —: Keep this photo exactly as it is — the round wooden table, the light, the view from above — and clear the table. Image 1 is the photo. Image 2 is the box. Image 3 is the strap.
From directly above, sharp on the box: on the bare table the open black box of Image 2 copied exactly, two straps side by side in its tray, fronts up, each {SH(3)} 12 × 5 cm — the box a third of the frame wide; her right hand reaches in from the bottom edge, its back to the lens, a mustard sleeve at the wrist, setting the black lid down flat beside the box, four chunky fingers and a thumb. Scale true to the set: the box as long as her forearm.
In frame: the table, one open box, exactly two straps, the lid, one hand; nothing else.
{KIT} {SPLIT} {PLAIN}''', [P04A, PKG, FRONT], False, True, True, True, P04A, None, None)
J["C-08a"] = ("v1", f'''For the line — {L("C-08a")} —: Keep this photo exactly as it is — her own staircase, the runner, the brass rods, the dark oak rail, the newel post, the photo wall, the front door — and change only her and the light. Image 1 is the photo.
The old way, years before: she wears a plum knit top, a long grey skirt to her shins and pink terry slippers. She stands side-on on the 6th step from the bottom, in profile facing the rail, both hands gripping the dark oak rail, four chunky fingers and a thumb on each, one slipper reaching down feeling for the step below, her face tight and careful, mouth closed, eyes on her foot. Scale true to the set: each step riser up to her shin.
In frame: her, the staircase and hall of Image 1; no strap anywhere, nobody else.
{GREY} {PLAIN}''', [R07F], True, True, True, False, R07F, None, None)
J["C-08b"] = ("v1", f'''For the line — {L("C-08b")} —: Keep this photo exactly as it is — her staircase, runner, rods, rail, newel, photo wall, door, light, her rose-pink blouse and denim skirt — and change only where she is. Image 1 is the photo. Image 2 is the strap.
Now on the 3rd step from the bottom, nearer the lens, she comes down facing the lens mid-step, right slipper reaching for the next tread, hands free off the rail, four chunky fingers and a thumb on each, a proud closed-mouth smile, looking ahead down the flight, her body half the frame tall; on her bare right knee {SH(2)} 12 × 5 cm, its notch cupping the kneecap's bottom. Scale true to the set: each step riser up to her shin.
In frame: her, exactly one strap on her right knee, the staircase and hall of Image 1; nobody else.
{HALL} {SPLIT} {PLAIN}''', [R07F, FRONT], True, True, True, True, R07F, None, None)
J["C-09a"] = ("v1", f'''For the line — {L("C-09a")} —: Keep this photo exactly as it is — the round wooden kitchen table, the morning light — and change only what is on the table: clear it. Image 1 is the photo. Image 2 is the box.
Close-up from high at a three-quarter angle, sharp on the bow: on the bare table the black box of Image 2 copied exactly, closed, its lid on with the wordmark up, half the frame wide, tied round with a wide red satin ribbon; her two hands, mustard sleeves at the wrists, reach in from the bottom edge facing away from the lens, their backs to the lens, and pull the bow tight on its top, four chunky fingers and a thumb on each. Scale true to the set: the box as long as her forearm.
In frame: the table, one closed box, the ribbon, two hands; nothing else.
{KIT} {PLAIN}''', [P04A, PKG], False, True, True, False, P04A, None, None)
J["C-09c"] = ("v1", f'''For the line — {L("C-09c")} —: Keep this photo exactly as it is — the view down her staircase from the landing, the runner, rods, balusters, photo wall, door, light, and the silver hair and mustard shoulder in the near foreground — and replace only the young woman on the stairs with her sister. Image 1 is the photo. Image 2 is the style — its runner's render and proportions. Image 3 is the gift box.
Her sister, a Black woman of 68, about 5.5 heads tall, a big round head, a soft round body, big eyes, short grey curls, in a navy Sunday dress to mid-calf and navy pumps, climbs toward the lens on the 5th step from the top, mid-step, the closed black box of Image 3 tied with a red ribbon under her left arm, her right hand swinging free off the rail, four chunky fingers and a thumb, a happy closed-mouth smile, eyes up at her sister. Scale true to the set: her head level with the 3rd picture frame.
In frame: two women, one boxed gift, the staircase; nobody else.
{HALL} {PLAIN}''', [LAND, PIXP, PKG], True, True, True, False, LAND, ["the sister"], None)
# L16 re-renders (one each): C-02b v3 B printed the line as a caption; C-06a v1 B drew another woman (the jogger style frame's face)
STH = g["STH"]
c02 = J["C-02b"][1].replace("Keep this photo exactly as it is — the church, its columns, steps, rail, hedges and sun — a tall 9:16 crop of the steps; add four women.",
                            "Keep this photo exactly as it is, a tall 9:16 crop of the steps; add four women.").replace(
    "No lettering, logos or labels but its wordmark.", "No captions or subtitles; no lettering, logos or labels anywhere.")
J["C-02b@r"] = ("v3r", c02, J["C-02b"][2], *J["C-02b"][3:9], J["C-02b"][9] + "; the v3 B render printed the line as a caption — kept off (L16), re-rendered once with no captions")
c06 = J["C-06a"][1].replace("Image 2 is the woman, in the outfit of Image 2.", "Image 2 is the woman — her face, twist-out, skin and outfit exact.").replace("one in each hand at shoulder height, fronts to the lens", "one in each hand, fronts to the lens").replace("Scale true to the set: the sofa back level with her shoulders.", "Scale true to the set: the sofa back at her shoulders.")
J["C-06a@r"] = ("v1r", c06, [FRONT, NS, P0, STH], *J["C-06a"][3:9], "the v1 B render drew another woman — kept off (L16), re-rendered once with the hands-only style frame so no other face is attached")
fails = 0; ONLY = sys.argv[1:]
for b, (tag, pr, refs, face, body, room, prod, eo, oneoffs, fn) in J.items():
    if ONLY and b not in ONLY: continue
    bb = b.split("@")[0]
    c = {"beat": bb, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(bb), "face": face, "room": room, "body": body,
         "refs": [{k: r[k] for k in ("label", "kind", "people") if k in r} for r in refs], "match": ("frame" if eo and eo["kind"] == "frame" else "plate") if eo else None, "edit_of": eo["job"] if eo else None,
         "taste": TASTE_P if prod else TASTE, "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": prod, "risk_class": None, "first_frame": False, "one_offs": oneoffs,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{bb}.{tag}.prompt.txt").write_text(pr); (H / f"{bb}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{bb}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
