#!/usr/bin/env python3
"""Fix round 2026-10-02 ~15:00 (hourly check): C-02a "make a new one the face looks the same" → three different women, each in her own
clause (§24O rule 10, V7.91.3, L55); C-02b "use the c02a as rerefence for all of them" → the new C-02a frame attached as the ladies to copy.
Run `python3 build_fix13.py C-02a` first; C-02b needs C02A_JOB (the new C-02a A render) set below."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
src = (H / "build_act8.py").read_text()
g = {"__file__": str(H / "build_act8.py")}
exec(src[src.index("import json"):src.index("\nJ = {}\n")], g)
ref, L, ID, P5, NF, PIXP, SUN, PLAIN, TASTE, PF = (g[k] for k in ("ref", "L", "ID", "P5", "NF", "PIXP", "SUN", "PLAIN", "TASTE", "PF"))
C02A_JOB = sys.argv[2] if len(sys.argv) > 2 else None
LEFT = "on the left a short, plump lady with deep brown skin, round glasses and short white curls, in lilac"
MID = "in the middle a tall, slim lady with light brown skin, high cheekbones, freckles and a grey bun, in coral"
RIGHT = "on the right a broad lady with very dark skin, full cheeks and silver braids, in cream"
J = {}
J["C-02a"] = ("v3", f'''For the line — {L("C-02a")} —: Keep this photo exactly as it is, a tall 9:16 crop at the foot of the steps; add three women. Image 1 is the church. Image 2 is the style — its runner's render and proportions.
Medium close-up at eye level, sharp on them: three different Black church ladies of seventy, about 5.5 heads tall, big round heads, side by side at the foot of the steps facing the lens — {LEFT}; {MID}, nudging the left one and nodding up the steps; {RIGHT} — matching wide hats, knowing closed-mouth smiles, eyes up the steps, a handbag in each near hand, four chunky fingers and a thumb on each. Scale true to the set: the bottom step at their ankles.
In frame: three women, the steps, the hedges; nobody else.
{SUN} {PLAIN}''', [P5, PIXP], P5, ["three church ladies"],
 'user image Fix "make a new one the face looks the same" → three different women, each with her own face, skin, hair and build (§24O rule 10, L55); earlier Fix in force: "not a pixar"')
if C02A_JOB:
    LAD = ref("C-02a frame v5 A (new) — the three church ladies to copy: faces, hair, dresses, hats", "style", C02A_JOB, ID + "C-02a"); LAD["people"] = True
    J["C-02b"] = ("v4", f'''For the line — {L("C-02b")} —: Keep this photo exactly as it is, a tall 9:16 crop of the steps; add four women. Image 1 is the church. Image 2 is the woman — face and silver twist-out only. Image 3 is the three church ladies and the style — copy each lady exactly: face, skin, hair, dress and hat.
Medium shot from low at the foot of the steps, three-quarter, sharp on her: the woman of Image 2, about 5.5 heads tall, comes down facing the lens, mid-step on the third step from the bottom, hands free off the rail, in an emerald church dress, black pumps, a wide green hat, a proud closed-mouth smile, looking ahead; to one side at the foot the three ladies of Image 3 watch her side by side — the lady in lilac nearest, then coral, then cream — hands clasped, four chunky fingers and a thumb on each hand. Scale true to the set: each step a shin high.
In frame: exactly four women, the steps; nobody else.
{SUN} No captions or subtitles; no lettering, logos or labels anywhere.''', [P5, NF, LAD], P5, ["three church ladies (copied from C-02a)"],
     'user image Fix "use the c02a as rerefence for all of them" → the new C-02a frame attached as the ladies to copy (§24O rule 10, L55); earlier Fixes in force: "not a pixar", no captions')
fails = 0; ONLY = sys.argv[1:2]
for b, (tag, pr, refs, eo, oneoffs, fn) in J.items():
    if ONLY and b not in ONLY: continue
    c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": True, "room": True, "body": True,
         "refs": [{k: r[k] for k in ("label", "kind", "people") if k in r} for r in refs], "match": "plate", "edit_of": eo["job"],
         "taste": TASTE, "anatomy": False, "anat_style": None, "pair": ["nano_banana_pro", "nano_banana_pro"], "alt_reason": None,
         "fix_note": fn, "product": False, "risk_class": None, "first_frame": False, "one_offs": oneoffs,
         "medias": [r["job"] for r in refs], "board_refs": [{"label": r["label"], "kind": r["kind"], "ref": r["ref"], "role": f"Image {i + 1}"} for i, r in enumerate(refs)]}
    (H / f"{b}.{tag}.prompt.txt").write_text(pr); (H / f"{b}.{tag}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.{tag}.preflight.json")], capture_output=True, text=True)
    print(f"{b}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    fails += r.returncode != 0
sys.exit(1 if fails else 0)
