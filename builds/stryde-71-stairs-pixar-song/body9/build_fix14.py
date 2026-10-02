#!/usr/bin/env python3
"""Fix round 2026-10-02 ~17:00 ("fix those"): the two board Fix notes.
 - M-06a "wrong product and the knee that should be straight in the image is the one with the strap": an edit of the picked v9 A frame —
   the strap redrawn as the product photo (Image 2) at true size on her RIGHT knee, and that right leg (frame left) made the straight,
   weight-bearing one on the upper tread; her bare left leg (frame right) bent, stepping down.
 - T-04a "that is not loreta": an edit of the picked v5 A frame — only the dancer in fuchsia changes, into Loretta from her confirmed
   wedding frame (T-02a v5 A, the day's outfit, HT27) with her face-and-hair crop (HT26, L54).
Picture prompts open "For the line — … —:" (L46). Constants from body4/build_act4.py's header."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
g = {"__file__": str(B4 / "build_act4.py")}
exec(src[src.index("import json"):src.index("J = {}")], g)
ref, L, ID, M, TASTE, TASTE_P, PF = (g[k] for k in ("ref", "L", "ID", "M", "TASTE", "TASTE_P", "PF"))
M06 = ref("M-06a frame v9 A (your pick) — her legs coming down her own staircase (the picture this edit keeps)", "frame", "52597e35-aee3-4e75-96a4-938f708c7114", ID + "M-06a")
FRONT = ref("front.webp — the strap, front (product photo)", "product", M["front"], "products/stryde/stryde_refs/front.webp")
T04 = ref("T-04a frame v5 A (your pick) — the wedding, over her shoulder, the full dance floor (the picture this edit keeps)", "frame", "f169c7e8-5d8d-4741-837d-1e9f4aec74a2", ID + "T-04a")
LOR = ref("T-02a frame v5 A (confirmed) — Loretta at this wedding in her fuchsia dress (the day's outfit, HT27)", "character", "366e9056-44ad-4e5a-b53f-8eb8596098c2", ID + "T-02a")
LORF = ref("C1-LORETTA face-and-hair crop of the confirmed sheet v2 (HT26, no clothes)", "character", M["C1_face"], ID + "C1-LORETTA")
J = {}
J["M-06a"] = ("v6", f'''For the line — {L("M-06a")} —: Keep this photo exactly as it is — her staircase, runner, brass rods, balusters, denim skirt, tan slippers, the light — and change only her legs and the strap. Image 1 is the photo. Image 2 is the strap.
She comes down toward the lens, hands out of frame. Her right leg, at frame left, is straight and locked, its slipper flat on the upper tread, taking her weight; her left leg, at frame right, bends at the knee, its slipper landing on the tread below. On her right knee only, the strap of Image 2 copied exactly — same shape, same parts, same markings, nothing redesigned: a black shell like a wide shallow M, two rounded peaks close together at the middle of its top edge cupping the bottom of the kneecap, a chrome slide at each end, the black band round the back of the knee. Scale true to the set: the strap 12 × 5 cm, a little narrower than her knee, about a quarter of the frame wide.
In frame: two legs, two slippers, exactly one strap on her right knee, five treads; nothing else.
A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun. No lettering, logos or labels but its wordmark.''',
 [M06, FRONT], False, True, True, True, M06, None,
 'user image Fix "wrong product and the knee that should be straight in the image is the one with the strap" → an edit of the picked v9 A: the strap redrawn as the product photo, on her right knee, and that right leg made the straight standing leg')
J["T-04a"] = ("v4", f'''For the line — {L("T-04a")} —: Keep this photo exactly as it is — the seated woman in burgundy, the table, the hall, the lights, the dancing guests — and change only the dancer in fuchsia in the middle of the floor. Image 1 is the photo. Image 2 is that dancer — the woman in fuchsia. Image 3 is her face and silver bob only.
The dancer in fuchsia is the woman of Image 2 and Image 3, copied exactly: her square face, warm brown skin, chin-length silver bob, her full build, about 5.5 heads tall, the same height as the seated woman, in the fuchsia satin dress and white slip-ons of Image 2; she dances in the same spot among the guests, facing the lens, both arms up, eyes on the lights above, a wide closed-mouth smile, four chunky fingers and a thumb on each hand. Scale true to the set: her head level with the guests' heads beside her.
In frame: the seated woman, the table, the guests, exactly one dancer in fuchsia; every other surface as in Image 1.
A final frame from a 3D animated feature film, stylized storybook render, warm evening light. No lettering, logos or labels.''',
 [T04, LOR, LORF], True, True, True, False, T04, None,
 'user image Fix "that is not loreta" → an edit of the picked v5 A: only the dancer in fuchsia changes, into Loretta from her confirmed wedding frame (T-02a) with her face-and-hair crop')
fails = 0
for b, (tag, pr, refs, face, body, room, prod, eo, oneoffs, fn) in J.items():
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": room, "body": body,
         "refs": [{k: r[k] for k in ("label", "kind", "people") if k in r} for r in refs], "match": "frame", "edit_of": eo["job"],
         "taste": TASTE_P if prod else TASTE, "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": prod, "risk_class": None, "first_frame": False, "one_offs": oneoffs,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.{tag}.prompt.txt").write_text(pr); (H / f"{b}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
