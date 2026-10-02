#!/usr/bin/env python3
"""Fix round 2026-10-02 ~13:00 ("fix those and generate the next act") + Act 7 first pairs.
 - PR-05b "should show productive broll not showing the product" → an image edit of her own staircase frame (R-07a v8 A): she comes down
   with a full laundry basket in the day-five navy trousers; the strap is hidden — nobody can tell it is there (HT01 productive after-state).
 - PR-06a "should be the normal and not the long strap" → the strap lies as front.webp shows it: a short stub of band past each slide (FP22 amended, L48).
 - Act 7: C-01a, C-02a, C-02b, C-03b (Pixar S3, the team's normal anatomy), C-04a, C-05a.
Picture prompts open "For the line — … —:" (V7.90.7, L46). Constants from body4/build_act4.py's header."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
g = {"__file__": str(B4 / "build_act4.py")}
exec(src[src.index("import json"):src.index("J = {}")], g)
ref, L, ID, FRONT, P7, STH, P04A, M = (g[k] for k in ("ref", "L", "ID", "FRONT", "P7", "STH", "P04A", "M"))
SPLIT, PLAIN, KIT, CLIN, TASTE, TASTE_P, PF = (g[k] for k in ("SPLIT", "PLAIN", "KIT", "CLIN", "TASTE", "TASTE_P", "PF"))
ANAT_PIX = src.split('ANAT_PIX = "')[1].split('"\n')[0]
R07F = ref("R-07a frame v8 A (confirmed) — her own staircase from the hall, she coming down (the picture this edit keeps)", "frame", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
PR05A = ref("PR-05a frame v2 B (confirmed) — N on her bed edge in the day-five pale-yellow nightgown (HT27)", "frame", "24dcdbbf-db60-4e98-a9cf-3833f2afb90c", ID + "PR-05a")
P5 = ref("P5-CHURCH plate (confirmed) — the church and its steps", "location", "020f7d83-d6e2-4744-9595-bef39ecf8f9f", ID + "P5-CHURCH")
NF = ref("N-NARR face-and-hair crop of the confirmed sheet v2 (HT26, no clothes)", "character", M["N_face"], ID + "N-NARR")
M05B = ref("M-05b frame v5 (confirmed) — the Pixar knee model with the strap seated (the anatomy style, L36)", "style", "c97a3ad0-ad6c-455a-959d-3e6594eb62cb", ID + "M-05b")
def SH(n): return (f"the strap of Image {n} copied exactly — a black shell with two matching pointed peaks close together at the middle of its top edge, "
                   "a notch between them, sloping down to a chrome slide at each end —")
SUN = "A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun."
HALL = g["HALL"]
J = {}
J["PR-05b"] = ("v3", f'''For the line — {L("PR-05b")} —: Keep this photo exactly as it is — her own staircase, the runner, the brass rods, the newel post, the photo wall, the front door, the light, and where she stands on the flight — and change only her clothes and her hands. Image 1 is the photo.
Today she wears a pale-yellow cotton top and navy cotton trousers that fall smooth and straight over both knees to her tan slippers, nothing showing under them. She comes down facing the lens, mid-step, both hands holding a full laundry basket of folded towels at her waist, hands off the rail, four chunky fingers and a thumb on each, a calm closed-mouth smile, looking ahead down the stairs. Scale true to the set: the basket as wide as her hips.
In frame: her, the basket, the staircase and hall of Image 1; nothing else.
{HALL} {PLAIN}''', [R07F], True, True, True, False, R07F,
 'user Fix "should show productive broll not showing the product" → she carries a laundry basket down her own stairs in the day-five navy trousers; the strap hidden under them')
J["PR-06a"] = ("v3", f'''For the line — {L("PR-06a")} —: Keep this photo exactly as it is — the round wooden kitchen table, the chairs, the floor, the morning light, the view from above — and change only what is on the table: clear it. Image 1 is the photo. Image 2 is the strap.
On the bare table, seen from directly above: one white coffee mug with a thin curl of steam, and beside it {SH(2)} the normal strap exactly as Image 2 shows it, only a short stub of black band past each slide, not stretched long — 12 × 5 cm, lying flat front up, a quarter of the frame wide.
In frame: the table, one mug, exactly one strap; the rest as Image 1.
{KIT} {SPLIT} {PLAIN}''', [P04A, FRONT], False, False, True, True, P04A,
 'user Fix "should be the normal and not the long strap" → the strap lies exactly as the front photo shows it, a short stub of band past each slide; earlier Fix in force: "wrong product"')
J["C-01a"] = ("v1", f'''For the line — {L("C-01a")} —: Her bedroom in the morning, tall 9:16. Image 1 is the strap. Image 2 is the woman — her skin and pale-yellow nightgown as in Image 2. Image 3 is the style.
Close-up at eye level from a three-quarter angle, sharp on the strap: she sits facing the lens on her bed's edge, the hem above her bare right knee; on that knee {SH(1)} 12 × 5 cm, a third of the frame wide, its notch cupping the bottom of the kneecap; her right hand flat on her thigh above it, thumb by the shell, her left hand on the quilt, four chunky fingers and a thumb on each; her left knee bare. Scale true to the set: her knee a third of the frame wide.
In frame: two knees, two hands, exactly one strap on her right knee, the quilt edge; every other surface plain.
{KIT} {SPLIT} {PLAIN}''', [FRONT, PR05A, STH], False, True, False, True, None, None)
J["C-02a"] = ("v1", f'''For the line — {L("C-02a")} —: Keep this photo exactly as it is — the red-brick church, its white columns, the wide steps with the black centre rail, the hedges, the sidewalk, the afternoon sun — a tall 9:16 crop at the foot of the steps, and add three women. Image 1 is the church. Image 2 is the style.
Medium close-up at eye level from the sidewalk, sharp on them: three Black women in their seventies in Sunday dresses and wide hats — lilac, coral, cream — stand side by side at the foot of the steps facing the lens; the middle one nudges the woman on her left with her elbow and nods up toward the steps, all three looking up the steps with knowing closed-mouth smiles, each holding a small handbag in her near hand, the other hand loose, four chunky fingers and a thumb on each. Scale true to the set: the bottom step at their ankles.
In frame: three women, the steps, the hedges; nobody else.
{SUN} {PLAIN}''', [P5, STH], True, True, True, False, P5, None)
J["C-02b"] = ("v1", f'''For the line — {L("C-02b")} —: Keep this photo exactly as it is — the red-brick church, its white columns, the wide steps with the black centre rail, the hedges, the afternoon sun — a tall 9:16 crop of the steps, and add four women. Image 1 is the church. Image 2 is the woman — her face and silver twist-out only. Image 3 is the style.
Medium shot from a low angle at the foot of the steps, three-quarter, sharp on her: the woman of Image 2 comes down the steps facing the lens, mid-step on the third step from the bottom, hands free at her sides away from the rail, in an emerald-green church dress to mid-calf, black pumps, a wide green hat, a proud closed-mouth smile, looking ahead; at the foot of the steps to one side three women in lilac, coral and cream Sunday dresses and hats watch her, hands clasped at their waists, four chunky fingers and a thumb on each hand. Scale true to the set: each step a shin high.
In frame: four women, the steps, the doors behind; nobody else.
{SUN} {PLAIN}''', [P5, NF, STH], True, True, True, False, P5, None)
J["C-03b"] = ("v1", f'''For the line — {L("C-03b")} —: {ANAT_PIX} Image 1 is the strap. Image 2 is the style.
Front-on close-up, sharp on the strap: {SH(1)} 12 × 5 cm, a third of the frame wide, seated on the model's patellar tendon, its notch cupping the kneecap's bottom, wordmark to the lens; under the pad a calm soft blue glow along the tendon ribbon.
In frame: the knee model, exactly one strap; the rest plain grey. {SPLIT} {PLAIN}''', [FRONT, M05B], False, False, False, True, None, None)
J["C-04a"] = ("v1", f'''For the line — {L("C-04a")} —: Keep this photo exactly as it is — the exam room, the table, the light — a tall 9:16 crop of the table, and add two people. Image 1 is the room. Image 2 is the strap. Image 3 is the style.
Medium shot over his right shoulder, sharp on the strap: a man of fifty in a grey tee and khaki shorts sits on the table's edge, his bare right knee forward; a friendly surgeon in navy scrubs, grey bun, crouches facing the lens, pressing {SH(2)} 12 × 5 cm, a fifth of the frame wide, under his kneecap, both thumbs on it, four chunky fingers and a thumb on each hand, eyes on the knee, mouth closed; his hands on the table edge. Scale true to the set: the table at her chest.
In frame: two people, exactly one strap on his right knee, the table; surfaces plain.
{CLIN} {PLAIN}''', [P7, FRONT, STH], True, True, True, True, P7, None)
J["C-05a"] = ("v1", f'''For the line — {L("C-05a")} —: Keep this photo exactly as it is — the round wooden kitchen table, the floor, the morning light, the view from above — and change only what is on the table: clear it. Image 1 is the photo. Image 2 shows the shape these cheap copies imitate.
Close-up from above at a three-quarter angle, sharp on the copies, her hands reaching in facing away from the lens: her two hands stretch one cheap copy between them by its band, four chunky fingers and a thumb on each, the band sagging thin and frayed, the soft shell bending in the middle; a second copy lies flat beside them. Each copy: a thin shiny grey plastic shell with soft rounded peaks, a crack and scuffs, cheap plastic buckles instead of chrome, no wordmark, a quarter of the frame wide. Scale true to the set: each copy as long as her hand.
In frame: two hands, two copies, the bare table; no boxes, no packaging, no screens.
{KIT} {PLAIN}''', [P04A, FRONT], False, True, True, False, P04A, None)
fails = 0; ONLY = sys.argv[1:]
for b, (tag, pr, refs, face, body, room, prod, eo, fn) in J.items():
    if ONLY and b not in ONLY: continue
    anat = b == "C-03b"
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{"label": r["label"], "kind": r["kind"]} for r in refs], "match": ("frame" if eo and eo["kind"] == "frame" else "plate") if eo else None, "edit_of": eo["job"] if eo else None,
         "taste": TASTE_P if prod else TASTE, "anatomy": anat, "anat_style": "S3" if anat else None, "pixar_anatomy": anat, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": prod, "risk_class": None, "first_frame": False,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.{tag}.prompt.txt").write_text(pr); (H / f"{b}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
