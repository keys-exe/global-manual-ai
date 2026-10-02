#!/usr/bin/env python3
"""Line 15 split (user 2026-10-02: "Pain pills. Cortisone shots. we need brolls for these 2"): P-04b keeps "Physical therapy.",
two new beats — P-04c "Pain pills." (her kitchen, N-D1c, from the confirmed P-04a frame) and P-04d "Cortisone shots." (the clinic, N-D1b,
from the confirmed P-04b frame). §6A short form, Mode 2, A/B pair on nano_banana_pro; picture prompts open "For the line — … —:" (L46).
Constants from body4/build_act4.py's header."""
import json, subprocess, sys, re
from pathlib import Path
H = Path(__file__).parent; B4 = H.parent / "body4"
src = (B4 / "build_act4.py").read_text()
g = {"__file__": str(B4 / "build_act4.py")}
exec(src[src.index("import json"):src.index("J = {}")], g)
ref, L, ID, P04A, TASTE, PF = (g[k] for k in ("ref", "L", "ID", "P04A", "TASTE", "PF"))
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
def LN(b): return re.sub(r'["“”]', "", rows[b]["line"])
P04B = ref("P-04b frame v3 A (confirmed) — the exam room, her on the treatment table in the floral house dress", "frame", "d6e85763-5356-4351-8f90-f4fc5eec9aa8", ID + "P-04b")
J = {}
J["P-04c"] = (f'''For the line — {LN("P-04c")} —: Close-up at table height from the side, sharp on her palm. Image 1 is her kitchen table and her hands from the scene before — the same wooden table, the same brown hands and grey cardigan cuffs, the same light; copy them exactly.
Her hands come in from frame right, facing frame left: her left hand held open, palm up, low over the table; her right hand tips a plain amber pill bottle, cap off, and two small white pills drop from its mouth toward her palm, one already in it; a plain glass of water stands beside on the table; four chunky fingers and a thumb on each hand. Scale true to the set: the bottle a little taller than her palm is wide, each pill the size of a fingernail; her two hands fill half the frame width.
In frame: two hands, the cardigan cuffs, one bottle, two pills, one glass, the table top; her head out of frame above; every other surface bare.
A final frame from a 3D animated feature film, stylized storybook render, grey morning light from the window over the sink. Bottle and glass plain — no lettering, logos or labels.''',
 [P04A], False, True, True,
 "From this frame: two white pills tip out of the bottle into her palm — one tip, about a second; camera RV sway — the virtual camera breathes in place, never travels")
J["P-04d"] = (f'''For the line — {LN("P-04d")} —: Close-up from low at the side of the treatment table, sharp on her knee. Image 1 is the exam room and her from the scene before — the same treatment table and paper sheet, her faded blue floral house dress, the same light through the half-open blind; copy them exactly.
Her bare right knee bent up on the table in profile, her shin and foot pointing frame right, the dress hem above it; a doctor seen only as two hands in pale blue gloves and white coat cuffs, coming in from frame left: one steadies the side of her knee, the other holds a small plain syringe, its thin needle just touching the skin at the side of the knee, thumb on the plunger; her own right hand grips the paper sheet at the table edge, four chunky fingers and a thumb. Scale true to the set: the syringe as long as a finger; the knee half the frame wide.
In frame: one knee and shin, her right hand, two gloved hands, one syringe, the table edge and sheet; her head out of frame; nobody else.
A final frame from a 3D animated feature film, stylized storybook render, afternoon light through the blind. No lettering, logos or labels; no blood.''',
 [P04B], False, True, True,
 "From this frame: the doctor's thumb presses the plunger — one slow press, about a second; camera RV sway — the virtual camera breathes in place, never travels")
fails = 0
for b, (pr, refs, face, body, room, mp) in J.items():
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": LN(b), "face": face, "room": room, "body": body,
         "refs": [{k: r[k] for k in ("label", "kind", "people") if k in r} for r in refs], "match": None, "edit_of": None,
         "taste": TASTE, "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": None, "product": False, "risk_class": None, "first_frame": False, "one_offs": None, "motion_plan": mp,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.v1.prompt.txt").write_text(pr); (H / f"{b}.v1.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v1.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
