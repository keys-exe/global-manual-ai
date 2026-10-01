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

# ---- v3: the user's Fix notes (board, 2026-10-01) — P-01a "should be looking up the stairs and stepping backwardd", P-01b "this should be the backwards also",
# P-02a "this should be her at the top of the stairs looking down", P-03b "the brace here should be same as the p03a"
P3A = "b327027d83f2ac9342dd7b3f19bed53b"   # P-03a v3 A, confirmed — the brace reference for P-03b
REF_P3A = {"label": "P-03a frame v3 A (confirmed) — the brace", "kind": "frame"}
P3 = {}
P3["P-01a"] = (f'''For the line "{L("P-01a")}": Keep this photo exactly as it is — the hall, the staircase rising to the right, its runner, balusters and oak rail, the photo wall, the light — a tall 9:16 crop on the flight, and add the woman. Image 1 is the hall and staircase. Image 2 is the woman.
Medium shot from the foot of the stairs, the lens low looking up the flight, sharp on her. The same woman as Image 2, seventy-one, on the 8th step, going down backwards: her back to the lens, facing up the stairs, face turned up to the landing, eyes on the top step, both hands gripping the oak rail, her right foot reaching back and down to the step below; {WARD}. Nobody else.
In the frame: the woman from behind, the flight of Image 1 rising above her, its rail, the photo wall, the hall floor at the bottom edge; every other surface bare. Two hands on the rail, two legs.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window above. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P0, REF_N], True, P0)
P3["P-01b"] = (f'''For the line "{L("P-01b")}": Keep this photo exactly as it is — the staircase, its carpet runner, brass rods and white balusters, the oak rail, the light — in close on four steps mid-flight from the side, a tall 9:16 crop, and add her feet. Image 1 is the staircase.
Close-up from the side at step height, feet and four steps filling the frame, sharp on the slippers: she is going down backwards, so both pink terry slippers point up the stairs, toes toward the upper steps; the lower slipper's heel is lowering backwards onto the next step down, the other slipper still flat on the step above; bare brown ankles under the hem of a faded blue floral house dress; one hand gripping the oak rail at the top edge of the frame, her other hand and her head out of frame above.
In frame: two slippers, two legs below the knee, one hand on the rail, four steps of the one flight with their runner and rods; every other surface bare. Each foot whole, heels toward the lower steps.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from above. Slippers and hem plain — no lettering, logos or labels; nobody else.''', [REF_P0], False, P0)
P3["P-02a"] = (f'''For the line "{L("P-02a")}": Keep this photo exactly as it is — the hall, the whole staircase rising to the right, its rail and newel, the photo wall, the light — a tall 9:16 crop on the full flight, and add the woman. Image 1 is the hall and staircase. Image 2 is the woman.
Medium shot from the hall floor, the lens low looking up the whole flight, sharp on her. The same woman as Image 2, seventy-one, sitting on the top step at the head of the stairs, her right hand on the newel post, her left hand in her lap, looking down the flight toward the lens, eyes on the hall floor far below, not going; {WARD}. Nobody else.
In the frame: the woman at the top of the flight of Image 1, every step between her and the lens, the rail, the photo wall; every other surface bare. Two hands placed, two legs.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window above, a catchlight in each eye. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P0, REF_N], True, P0)
P3["P-03b"] = (f'''For the line "{L("P-03b")}": Keep this photo exactly as it is — the kitchen floor, the table and chair legs, the cabinets, the light — in close at floor level, a tall 9:16 crop, and add her feet. Image 1 is the kitchen. Image 2 is the brace, copied exactly — same shape, same wide straps, same round hinges, nothing redesigned.
Close-up at floor level from the side, sharp on the ankle: a seated woman's bare brown shins, the brace of Image 2 slid down her right leg and bunched in a loose ring around her right ankle, its hinges and straps slumped above a pink terry slipper, both slippers flat on the floor, the hem of a faded blue floral house dress at the top edge, a chair leg beside her. Hands and head out of frame above.
In frame: two slippers, two shins, the one brace of Image 2 around the right ankle, the chair and table legs and floor of Image 1; every other surface bare. Each foot whole.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in evening light, the window over the sink dim, the ceiling light on. Brace and slippers plain — no lettering, logos or labels; nobody else.''', [REF_P2, REF_P3A], False, P2)
FIX3 = {"P-01a": "should be looking up the stairs and stepping backwardd", "P-01b": "this should be the backwards also",
        "P-02a": "this should be her at the top of the stairs looking down", "P-03b": "the brace here should be same as the p03a"}
if V >= 3:
    P = P3

# ---- v4 (hourly check 18:20 + user message, 2026-10-01): P-01a "she should be at the top of the middle of the stairs she should never be at the bottom";
# P-03b "p03a and b should be connected so same braces" → a direct edit of the confirmed P-03a frame; P-05 split into three B-rolls ("make this into 3 brolls"):
# P-05a keeps its confirmed frame (clip re-cut), P-05b the heap at the far edge, P-05c her face sat back — new beats, written as v1.
P4 = {}
P4["P-01a"] = (f'''For the line "{L("P-01a")}": Keep this photo exactly as it is — the hall, the staircase rising to the right, its rail, the photo wall, the light — a tall 9:16 crop on the upper half of the flight and the landing, and add the woman. Image 1 is the hall and staircase. Image 2 is the woman.
Medium shot from the hall, the lens low on the top of the flight, sharp on her. The same woman as Image 2, seventy-one, two steps below the landing, going down backwards: her back to the lens, facing up the stairs, face turned up to the landing, eyes on the top step, both hands gripping the oak rail, her right foot reaching back down to the step below; {WARD}. Nobody else.
In the frame: the woman from behind near the top of the flight of Image 1, the landing above her, the steps below her, the rail, the photo wall; every other surface bare. Two hands on the rail, two legs.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P0, REF_N], True, P0)
P4["P-03b"] = (f'''For the line "{L("P-03b")}": Keep this photo exactly as it is — the seated woman, her blue floral house dress, her bare right leg, the lace-covered table, the chair, the kitchen behind — but drop the frame to her ankle and slide the brace down. Image 1 is the picture; nothing in it changes but the brace and the crop.
Close-up at floor level from the same side, sharp on the ankle: the big black hinged knee brace of Image 1, copied exactly — same wide straps, same round hinges, nothing redesigned — now slid all the way down her right leg and bunched in a loose ring around her right ankle just above her pink terry slipper, both slippers flat on the floor; her right hand resting on her knee, her left hand on the table edge, her head and shoulders out of frame above.
In frame: two slippers, two shins, the one brace of Image 1 around the right ankle, the chair and table legs and floor of Image 1; every other surface bare. Each foot whole.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in evening light, the window dim, the ceiling light on. Brace and slippers plain — no lettering, logos or labels; nobody else.''', [REF_P3A], False, P3A)
P4["P-05b"] = (f'''For the line "{L("P-05b")}": Keep this photo exactly as it is — the kitchen, its table with the lace cloth, the chairs, the cabinets, the light — in close at table height on the far edge of the table, a tall 9:16 crop, and lay out the heap. Image 1 is the kitchen.
Close-up from across the table at table height, the far edge of the table filling the lower frame, sharp on the heap: a folded black hinged knee brace, two grey knee sleeves, three plain pill bottles, a white gel tube and a blue ice pack jammed together against the far edge where a push left them; one bottle on its side at the lip, one sleeve hanging over the edge; nobody in the frame, no hands.
In frame: the heap, the table edge and lace of Image 1, the chair back and cabinets behind; every other surface bare, nothing else on the table.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the window over the sink. Bottles and packs plain — no lettering, logos or labels; nobody else.''', [REF_P2], False, P2)
P4["P-05c"] = (f'''For the line "{L("P-05c")}": Keep this photo exactly as it is — the kitchen, its table with the lace cloth, the chair, the cabinets, the light — in close across the table, a tall 9:16 crop, and add the woman. Image 1 is the kitchen. Image 2 is the woman.
Close-up from across the table at her eye level, the heap of braces, sleeves and pill bottles soft in the near foreground at the table's far edge, sharp on her face. The same woman as Image 2, seventy-one, sat back in the chair, shoulders down, eyes on nothing past the lens, mouth closed; {WARD}; both hands slack in her lap, out of frame below the table edge. Nobody else.
In the frame: her face and shoulders, the chair back, the heap soft in front, the cabinets of Image 1 behind; every other surface bare.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the window over the sink, a catchlight in each eye. Clothing and bottles plain — no lettering, logos or labels; no second person.''', [REF_P2, REF_N], True, P2)
FIX4 = {"P-01a": "she should be at the top of the middle of the stairs she should never be at the bottom", "P-03b": "p03a and b should be connected so same braces",
        "P-05b": "make this into 3 brolls (P-05a split)", "P-05c": "make this into 3 brolls (P-05a split)"}
OUTV = {"P-05b": 1, "P-05c": 1}
if V >= 4:
    P = P4

# ---- v5 (user Fix 2026-10-01: "she should be starting from the top to show case the moving backwards"): the plate cropped to the landing and the top of the flight
# (plates/P0-PROP-N_top.png, Higgsfield media 692d9e49) so the model has only the top to put her on.
REF_P0T = {"label": "P0-PROP-N plate (confirmed) — cropped to the landing and the top of the flight", "kind": "location"}
P5 = {}
P5["P-01a"] = (f'''For the line "{L("P-01a")}": Keep this photo exactly as it is — the top of the staircase, the landing, the oak rail, the photo wall, the light — a tall 9:16 crop on the landing and the top steps, and add the woman. Image 1 is the top of the staircase and the landing. Image 2 is the woman.
Medium shot from below, sharp on her. The same woman as Image 2, seventy-one, starting from the top: standing on the top step at the head of the stairs, going down backwards — her back to the lens, face turned up to the landing, eyes on its floor, both hands gripping the oak rail, her right foot reaching back and down to the step below; {WARD}. Nobody else.
In the frame: the woman from behind on the top step of Image 1, the landing above her, a few steps below her, the rail, the photo wall; every other surface bare. Two hands on the rail, two legs.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P0T, REF_N], True, "692d9e49-493e-4792-92c1-4f362f6961d5")
FIX5 = {"P-01a": "she should be starting from the top to show case the moving backwards"}
if V >= 5:
    P = P5

# ---- v6 (same Fix, 2026-10-01): the v5 pair (edit of the cropped plate) still put her at the newel — the crop kept the bottom of the flight in. So the
# frame is now an edit of the confirmed P-02a v6 B (her on the top step, the whole flight from the hall floor): the same woman stood up at the top (FP14).
P02B = "aa7875902a56e13b0b58fc4f961b1371"   # P-02a v6 B, confirmed — job 04e4ff58
REF_P02B = {"label": "P-02a frame v6 B (confirmed) — her at the top of the flight", "kind": "frame"}
P6 = {}
P6["P-01a"] = (f'''For the line "{L("P-01a")}": Keep this photo exactly as it is — the hall floor, the whole flight, the oak rail and newel, the photo wall, the light — and only stand the woman up. Image 1 is the picture; nothing in it moves but her.
Medium shot from the hall floor looking up the whole flight, sharp on her. The woman of Image 1, seventy-one, now standing on the top step where she sat, turned away from the lens to face the landing, going down backwards: her back to us, the back of her grey head, both hands gripping the oak rail, her right foot reaching back and down to the step below; faded blue floral knee-length house dress, grey cardigan, pink terry slippers. Nobody else.
In the frame: the woman from behind at the top of the flight of Image 1, every step between her and the lens, the rail, the newel, the photo wall; every other surface bare. Two hands on the rail, two legs.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the landing window. Clothing and frames plain — no lettering, logos or labels; no second person.''', [REF_P02B], False, P02B)
FIX6 = {"P-01a": "she should be starting from the top to show case the moving backwards (v5 pair kept her at the newel — the crop still held the bottom of the flight; now an edit of the P-02a frame)"}
if V >= 6:
    P = P6

# ---- v7 (user 2026-10-01: "THE WHOLE P03 I NEED NEW ONES THERE / FIX THEM ALL"): a new staging for both — seated on the kitchen chair, from the side at
# knee height. P-03a is an edit of the P2 plate; P-03b is an edit of the new P-03a A frame (FP14), run once P-03a has rendered (P3B_OF = its job id).
P7 = {}
P7["P-03a"] = (f'''For the line "{L("P-03a")}": Keep this photo exactly as it is — the kitchen, its table with the lace cloth, the chairs, the floor, the light — in close at the near chair from the side, a tall 9:16 crop, and add the seated woman from the shoulders down. Image 1 is the kitchen.
Medium close-up from the side at knee height, sharp on the brace: an older Black woman sitting on the kitchen chair at the table, her right leg out a little, a big black hinged knee brace with wide straps slid down below the kneecap, sagging at the top of her shin, her right hand gripping its top strap and hauling it back up, her left hand flat on the chair seat; the hem of a faded blue floral house dress at mid-thigh, pink terry slippers flat on the floor; her head and shoulders out of frame above.
In frame: the seated woman from the shoulders down, two hands placed, the brace, two slippers, the chair and table edge of Image 1; every other surface bare.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in grey morning light from the window over the sink. Brace and dress plain — no lettering, logos or labels; nobody else.''', [REF_P2], False, P2)
P3B_OF = None   # set to the new P-03a A job id when it has rendered
P7["P-03b"] = (f'''For the line "{L("P-03b")}": Keep this photo exactly as it is — the seated woman, her house dress, the chair, the table edge, the kitchen behind — but drop the frame to the floor and slide the brace down. Image 1 is the picture; nothing in it changes but the brace and the crop.
Close-up from the same side at floor level, sharp on the ankle: the big black hinged knee brace of Image 1, copied exactly — same wide straps, same round hinges — now slid all the way down her right leg and bunched in a loose ring around her right ankle just above her pink terry slipper, both slippers flat on the floor, her shins bare; her hands resting on her knees, her head and shoulders out of frame above.
In frame: two slippers, two shins, the one brace of Image 1 around the right ankle, the chair legs and floor of Image 1; every other surface bare. Each foot whole.
A final frame from a 3D animated feature film, stylized storybook render — the render of Image 1 in evening light, the window dim, the ceiling light on. Brace and slippers plain — no lettering, logos or labels; nobody else.''', [{"label": "P-03a frame v7 A (new) — the seat and the brace", "kind": "frame"}], False, "P3A-NEW")
FIX7 = {"P-03a": "THE WHOLE P03 I NEED NEW ONES THERE / FIX THEM ALL", "P-03b": "THE WHOLE P03 I NEED NEW ONES THERE / FIX THEM ALL"}
if V >= 7:
    P = P7
if __name__ == "__main__":
    fails = 0
    for b, (pr, refs, face, eo) in P.items():
        c = {"beat": b, "kind": "image", "mode": 2, "prompt": pr, "script_line": L(b), "face": face, "room": True, "body": b != "P-05b", "refs": refs,
             "match": "frame" if eo in (P3A, P02B, "P3A-NEW") else "plate", "edit_of": eo, "taste": TASTE, "anatomy": False, "pair": PAIR, "alt_reason": None, "fix_note": (FIX7 if V >= 7 else FIX6 if V >= 6 else FIX5 if V >= 5 else FIX4 if V >= 4 else FIX3).get(b) if V >= 3 else None, "product": False}
        OV = (OUTV if V == 4 else {}).get(b, V)
        (H / f"{b}.v{OV}.prompt.txt").write_text(pr); (H / f"{b}.v{OV}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v{OV}.preflight.json")], capture_output=True, text=True)
        print(f"{b} v{OV}: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
        fails += r.returncode != 0
    sys.exit(1 if fails else 0)
