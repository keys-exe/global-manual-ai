#!/usr/bin/env python3
"""Act 1 (the problem, N-D1) — §6A short beat prompts, Mode 2, A/B pair on nano_banana_pro; every shot an image edit of its confirmed plate (HT17).
Writes body/<BEAT>.v<n>.prompt.txt + .preflight.json and runs preflight.py."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent; B = "stryde-71-stairs-pixar-song"
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
rows = {r["beat"]: r for r in json.load(open(H.parent / "work/actmap_rows.json"))}
PAIR = ["nano_banana_pro", "nano_banana_pro"]
TASTE = ["HT02", "HT03", "HT04", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22"]
P0 = "973904c55f316a52570c8bff44ef7a07"; P2 = "cc6ec5031226aadf6d5a46725855adea"; P7 = "857c003a828c12e98bc42df4406cce57"
REF_P0 = {"label": "P0-PROP-N plate (confirmed)", "kind": "location"}; REF_P2 = {"label": "P2-KITCHEN plate v2 (confirmed)", "kind": "location"}
REF_P7 = {"label": "P7-CLINIC plate (confirmed)", "kind": "location"}; REF_N = {"label": "N-NARR sheet v2", "kind": "character"}
WARD = "faded blue floral knee-length house dress, grey cardigan, pink terry slippers"
V = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 1
P = {}
def L(b): return rows[b]["line"]
P["P-01a"] = (f'''For the line "{L("P-01a")}": Keep this photo exactly as it is — the hall, the staircase, its runner and oak rail, the photo wall, the light — but seen from the top landing looking down the flight, a tall 9:16 crop, and add the woman. Image 1 is the hall and staircase. Image 2 is the woman.
Medium shot from the landing, the lens high looking down the steps, sharp on her. The same woman as Image 2, seventy-one, on the 4th step from the top, going down backwards — facing up the stairs toward the lens, both hands gripping the oak handrail, her right foot feeling for the step below, head down, eyes on the step under her; {WARD}. Nobody else.
In the frame: the woman, the flight of Image 1, its rail and balusters, the photo wall, the hall floor far below; every other surface bare. Two hands on the rail, two legs, one foot per step.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window behind the lens. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P0, REF_N], True, P0)
P["P-01b"] = (f'''For the line "{L("P-01b")}": Keep this photo exactly as it is — the staircase, its carpet runner, brass rods and balusters, the light — in close on four steps mid-flight, a tall 9:16 crop, and add her feet. Image 1 is the staircase.
Close-up from the side at step height, feet and four steps filling the frame, sharp on the slippers: a pink terry slipper lowering onto the next step down, the other slipper still on the step above about to join it, bare brown ankles under the hem of a faded blue floral house dress, one hand gripping the oak rail at the top edge of the frame, her other hand and her head out of frame above.
In frame: two slippers, two legs below the knee, one hand on the rail, four steps of the one flight with their runner and rods; every other surface bare. Each foot whole.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from above. Slippers and hem plain — no lettering, logos or labels; nobody else.''', [REF_P0], False, P0)
P["P-02a"] = (f'''For the line "{L("P-02a")}": Keep this photo exactly as it is — the staircase, the landing, the oak newel and balusters, the photo wall, the light — seen from the landing through the balusters, a tall 9:16 crop, and add the woman. Image 1 is the hall and staircase. Image 2 is the woman.
Medium shot at eye level from the landing, the top balusters soft in the near foreground, sharp on her. The same woman as Image 2, seventy-one, sitting on the top step, her right hand on the newel post, her left hand in her lap, looking down the flight, eyes on the hall floor below, not going; {WARD}. Nobody else.
In the frame: the woman, the top of the flight of Image 1, the newel and balusters, the photo wall, the hall below; every other surface bare. Two hands placed, two legs.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window at her side, a catchlight in each eye. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P0, REF_N], True, P0)
P["P-03a"] = (f'''For the line "{L("P-03a")}": Keep this photo exactly as it is — the kitchen, its table and chairs, the cabinets, the light — in close at the table, a tall 9:16 crop, and add a seated woman's knee. Image 1 is the kitchen.
Close-up from above and to the side, her own view of her knee, sharp on the brace: a seated older Black woman's bare right knee forward, a big black hinged knee brace with wide straps slid down below the kneecap, sagging in folds at the top of her shin, her right hand gripping its top strap and hauling it back up, her left hand on the table edge; the hem of a faded blue floral house dress at mid-thigh, a pink terry slipper on the floor, her head and shoulders out of frame above.
In frame: the bare knee, the sagging brace, two hands placed, the table edge and one chair of Image 1; every other surface bare.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the window over the sink. Brace and dress plain — no lettering, logos or labels; nobody else.''', [REF_P2], False, P2)
P["P-03b"] = (f'''For the line "{L("P-03b")}": Keep this photo exactly as it is — the kitchen floor, the table and chair legs, the cabinets, the light — in close at floor level, a tall 9:16 crop, and add her feet. Image 1 is the kitchen.
Close-up at floor level from the side, sharp on the ankle: a seated woman's bare brown shins, the big black hinged knee brace bunched in a loose ring around her right ankle just above a pink terry slipper, both slippers flat on the floor, the hem of a faded blue floral house dress at the top edge, a chair leg beside her. Hands and face out of frame.
In frame: two slippers, two shins, the brace around the right ankle, the chair and table legs and floor of Image 1; every other surface bare. Each foot whole.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in evening light, the window over the sink dim, the ceiling light on. Brace and slippers plain — no lettering, logos or labels; nobody else.''', [REF_P2], False, P2)
P["P-04a"] = (f'''For the line "{L("P-04a")}": Keep this photo exactly as it is — the kitchen table top, the light — straight down from above, a tall 9:16 crop, and lay out the things. Image 1 is the kitchen.
Overhead close-up of the wooden table of Image 1, sharp across it: a woman's two brown hands spread over the heap, the right pushing a tall pill bottle, the left on a folded black hinged knee brace; around them three plain pill bottles, a white gel tube, two grey knee sleeves, a blue ice pack, a roll of beige tape; the cuffs of a grey cardigan at the frame edge, her head and shoulders out of frame above.
In frame: two hands placed, the brace, two sleeves, three bottles, the tube, the ice pack, the tape, the table top; every other surface bare, nothing else on the table.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the window over the sink. Bottles and packs plain — no lettering, logos or labels; nobody else.''', [REF_P2], False, P2)
P["P-04b"] = (f'''For the line "{L("P-04b")}": Keep this photo exactly as it is — the exam room, its treatment table, the window with the half-open blind, the light — a tall 9:16 crop on the table, and add two people. Image 1 is the exam room. Image 2 is the woman.
Medium shot from above and to the side, sharp on her. The same woman as Image 2, seventy-one, lying on her back on the treatment table, head on the paper-covered pillow, eyes on the ceiling, hands folded on her stomach; faded blue floral house dress, the hem above the knee, pink terry slippers off on the floor. A physical therapist in a plain navy polo, seen only from the shoulders down, stands at the table's side, both hands on her bare right leg, bending the knee up. Nobody else.
In frame: the woman, the therapist's torso and two hands placed, the table and window of Image 1; every other surface bare. Two legs on her.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in afternoon light through the blind, a catchlight in each eye. Clothing and walls plain — no lettering, logos or labels; no third person.''', [REF_P7, REF_N], True, P7)
P["P-05a"] = (f'''For the line "{L("P-05a")}": Keep this photo exactly as it is — the kitchen, its table and chairs, the cabinets, the light — from across the table at its edge, a tall 9:16 crop, and add the woman. Image 1 is the kitchen. Image 2 is the woman.
Medium shot from low across the table, the table edge in the near foreground, sharp on her face. The same woman as Image 2, seventy-one, seated at the table, the heap of braces, sleeves and pill bottles pushed to the far side with the back of her right hand, her left hand slack in her lap, sitting back in the chair, eyes on nothing past the lens; {WARD}. Nobody else.
In frame: the woman, the heap on the table, the table and chair of Image 1, the cabinets behind; every other surface bare. Two hands placed, two legs under the table.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the window over the sink, a catchlight in each eye. Clothing and bottles plain — no lettering, logos or labels; no second person.''', [REF_P2, REF_N], True, P2)
if __name__ == "__main__":
    fails = 0
    for b, (pr, refs, face, eo) in P.items():
        c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": True, "product": False, "body": True, "refs": refs,
             "match": "plate", "edit_of": eo, "taste": TASTE, "anatomy": False, "pair": PAIR, "alt_reason": None, "fix_note": None}
        (H / f"{b}.v{V}.prompt.txt").write_text(pr); (H / f"{b}.v{V}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{V}.preflight.json")], capture_output=True, text=True)
        print(f"{b} v{V}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
        fails += r.returncode != 0
    sys.exit(1 if fails else 0)
