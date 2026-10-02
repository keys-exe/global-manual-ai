#!/usr/bin/env python3
"""M-06a Fix 2026-10-02 ~17:10: "the product is distorted i need a new one thats why i said it should be straid leg".
Diagnosis: the last two pairs were edits of a small, angled crop of her staircase — the shell wrapped round the lower thigh, its middle
dipping where the two peaks should rise, seen at an angle. FP07 (the strapped knee straight so the shell reads), FP11 (big in frame),
FP03 (below the kneecap) and FP22 (peaks together at the middle) were in the prompt but the edit couldn't hold them.
Fix at the source: a fresh picture, not an edit — front-on close of both straight legs, the shell flat to the lens and a third of the
frame wide, the product photo as Image 1, her day (R-07a frame: staircase, denim skirt, tan slippers) as Image 2; run on true
nano-banana-pro through Kie (Higgsfield logs nano_banana_2 under the Pro name — §5, F10)."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
g = {"__file__": str(B4 / "build_act4.py")}
exec(src[src.index("import json"):src.index("J = {}")], g)
ref, L, ID, M, TASTE_P, PF = (g[k] for k in ("ref", "L", "ID", "M", "TASTE_P", "PF"))
FRONT = ref("front.webp — the strap, front (product photo)", "product", M["front"], "products/stryde/stryde_refs/front.webp")
R07 = ref("R-07a frame v4 (confirmed) — her own staircase, her denim skirt and tan slippers on this day", "frame", "11b8a6bb-8c4a-4739-86ce-0c779f413c53", ID + "R-07a")
pr = f'''For the line — {L("M-06a")} —: Close-up from the front at knee height, sharp on the strap. Image 1 is the strap. Image 2 is her staircase, her denim skirt and tan slippers on this day.
She stands on her own staircase of Image 2, facing the lens, both legs straight, knees locked, feet flat side by side on one tread, hands out of frame above. On her right knee, at frame left, the strap of Image 1 copied exactly — same shape, same parts, same markings, nothing redesigned: a rigid black shell flat to the lens, its top edge rising into two rounded peaks together at the middle with a small notch between them, the notch seated against the bottom of her kneecap, a chrome slide at each end, the black band round the back of the knee. Scale true to the set: the shell 12 × 5 cm, a third of the frame wide, a little narrower than her knee.
In frame: two straight legs from the skirt hem to the slippers, exactly one strap on her right knee, the runner and two brass rods; nothing else.
A final frame from a 3D animated feature film, stylized storybook render, warm afternoon sun. No lettering, logos or labels but its wordmark.'''
MP = "From this frame: her left slipper steps down onto the next tread toward the lens, the strapped right leg straight and steady — one step, about a second; camera RV sway — the virtual camera breathes in place, never travels"
refs = [FRONT, R07]
c = {"beat": "M-06a", "kind": "image", "mode": 2, "prompt": pr, "script_line": L("M-06a"), "face": False, "room": True, "body": True,
     "refs": [{k: r[k] for k in ("label", "kind")} for r in refs], "match": None, "edit_of": None,
     "taste": TASTE_P + ["FP07", "FP18", "FP22"], "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"],
     "alt_reason": None, "route": "Kie AI nano-banana-pro (true Pro; Higgsfield logs nano_banana_2 under the Pro name)",
     "fix_note": 'user image Fix "the product is distorted i need a new one thats why i said it should be straid leg" → a fresh front-on close of both straight legs, the shell flat to the lens a third of the frame wide, product photo first, on true nano-banana-pro (Kie)',
     "product": True, "risk_class": None, "first_frame": False, "one_offs": None, "motion_plan": MP,
     "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
(H / "M-06a.v7.prompt.txt").write_text(pr); (H / "M-06a.v7.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
r = subprocess.run([sys.executable, str(PF), str(H / "M-06a.v7.preflight.json")], capture_output=True, text=True)
print(f"M-06a: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
sys.exit(r.returncode)
