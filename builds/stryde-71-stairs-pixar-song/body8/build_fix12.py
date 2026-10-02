#!/usr/bin/env python3
"""Fix round 2026-10-02 ~14:40 ("fix those and generate the clips") — the board's image Fix notes:
 - C-07a "dont cover the box stryde logo" → an edit of the picked v1 A frame: only her hand moves off the lid, the wordmark clear.
 - C-08a "wrong avatar" → the same edit of R-07a v8 A, now with her face-and-hair crop attached (§24O rule 7, V7.91.2, L54).
 - PR-06a "the strap is too big" → an edit of the picked v5 frame: only the strap's size changes, true size against the mug (§6A rule 2, L53).
Constants from build_act8.py's header."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
src = (H / "build_act8.py").read_text()
g = {"__file__": str(H / "build_act8.py")}
exec(src[src.index("import json"):src.index("\nJ = {}\n")], g)
ref, L, ID, FRONT, PKG, NF, R07F, SH = (g[k] for k in ("ref", "L", "ID", "FRONT", "PKG", "NF", "R07F", "SH"))
SPLIT, PLAIN, KIT, TASTE, TASTE_P, PF, GREY = (g[k] for k in ("SPLIT", "PLAIN", "KIT", "TASTE", "TASTE_P", "PF", "GREY"))
C07 = ref("C-07a frame v1 A (your pick) — the open box from above, her hand on the lid (the picture this edit keeps)", "frame", "accecf96-a496-4405-aacc-46f3726357f5", ID + "C-07a")
P06 = ref("PR-06a frame v5 (your pick) — the mug and strap on the table from above (the picture this edit keeps)", "frame", "bff302b8-80ad-40ab-815d-4ce947fe34f4", ID + "PR-06a")
J = {}
J["C-07a"] = ("v2", f'''For the line — {L("C-07a")} —: Keep this photo exactly as it is — the round wooden table, the open black box with its two straps, the light, the view from above — and change only her hand and the lid. Image 1 is the photo. Image 2 is the box.
The box and both straps stay copied exactly as in Image 1 and Image 2 — same shape, same parts, same markings, nothing redesigned. The black lid lies flat beside the box with its wordmark face up and fully in view, nothing over it; her right hand, a mustard sleeve at the wrist, has just let go of the lid's near bottom corner, its back to the lens, four chunky fingers and a thumb, clear of the wordmark. Scale true to the set: the lid as long as her forearm, each strap 12 × 5 cm in its tray, the box a third of the frame wide.
In frame: the table, one open box, exactly two straps in it, the lid, one hand; nothing else.
{KIT} {PLAIN}''', [C07, PKG], False, True, True, True, C07, None,
 'user image Fix "dont cover the box stryde logo" → an edit of the picked v1 A frame: her hand off the lid, the wordmark clear')
J["C-08a"] = ("v2", f'''For the line — {L("C-08a")} —: Keep this photo exactly as it is — her own staircase, the runner, the brass rods, the dark oak rail, the newel post, the photo wall, the front door — and change only her clothes, her pose and the light. Image 1 is the photo. Image 2 is her face and silver twist-out.
She is the woman of Image 1 and Image 2 — the same round face, dark brown skin and silver twist-out, about 5.5 heads tall. The old way, years before: she wears a plum knit top, a long grey skirt and pink terry slippers, standing side-on on the 6th step from the bottom, in profile facing the rail, both hands gripping the dark oak rail, four chunky fingers and a thumb on each, one slipper reaching down for the step below, her face tight and careful, mouth closed, eyes on her foot. Scale true to the set: each step riser up to her shin.
In frame: her, the staircase and hall of Image 1; no strap anywhere, nobody else.
{GREY} {PLAIN}''', [R07F, NF], True, True, True, False, R07F, None,
 'user image Fix "wrong avatar" → the same edit with her face-and-hair crop attached and her face named (§24O rule 7, L54)')
J["PR-06a"] = ("v4", f'''For the line — {L("PR-06a")} —: Keep this photo exactly as it is — the round wooden table, the white mug and its steam, the morning light, the view from above — and change only the strap's size: make it smaller, its true size. Image 1 is the photo. Image 2 is the strap.
Beside the mug lies {SH(2)} the normal strap as Image 2 shows it, a short stub of band past each slide, lying flat front up: 12 × 5 cm, its whole length only a little longer than the mug is tall and its height half the mug's, about a fifth of the frame wide.
In frame: the table, one mug, exactly one strap; the rest as Image 1.
{KIT} {SPLIT} {PLAIN}''', [P06, FRONT], False, False, True, True, P06, None,
 'user image Fix "the strap is too big" → an edit of the picked v5 frame: the strap at true size against the mug (§6A rule 2, L53); earlier Fixes in force: "wrong product", "should be the normal and not the long strap"')
fails = 0; ONLY = sys.argv[1:]
for b, (tag, pr, refs, face, body, room, prod, eo, oneoffs, fn) in J.items():
    if ONLY and b not in ONLY: continue
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
