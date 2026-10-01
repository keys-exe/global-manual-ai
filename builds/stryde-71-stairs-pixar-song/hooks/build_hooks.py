#!/usr/bin/env python3
"""Step 6 — hook start frames (§6A short form, Mode 2) and the pinned end frames (§27G rules 5 & 10, stairs class).
Writes hooks/<BEAT>.prompt.txt + hooks/<BEAT>.preflight.json and runs preflight.py on each."""
import json, subprocess, sys
from pathlib import Path
H = Path(__file__).parent
PF = H / "../../../.claude/skills/ai-prompt-engineer/scripts/preflight.py"
P0 = "973904c55f316a52570c8bff44ef7a07"   # P0-PROP-N Current asset (confirmed)
PAIR = ["nano_banana_pro", "nano_banana_pro"]
TASTE = ["HT03", "HT04", "HT05", "HT08", "HT09", "HT12", "HT17", "HT18", "HT19", "HT22"]
REG = "A final frame from a 3D animated feature film — stylized storybook render, every surface with a material, a single catchlight in each eye, soft warm bounce in the shadows"
N_WARD = "emerald-green church dress to mid-calf, low black pumps"
C2_WARD = "olive-green crewneck sweatshirt, black denim shorts, white trainers"
REF_P0 = {"label": "P0-PROP-N plate", "kind": "location"}
REF_N = {"label": "N-NARR sheet v2", "kind": "character"}
REF_C2 = {"label": "C2-DAUGHTER sheet v2", "kind": "character"}

CALLS = {}
def add(beat, line, prompt, refs, *, face, room=True, product=False, body=True, match=None, edit_of=None):
    CALLS[beat] = {"beat": beat, "kind": "image", "mode": 2, "prompt": prompt, "script_line": line,
                   "face": face, "room": room, "product": product, "body": body, "refs": refs,
                   "match": match, "edit_of": edit_of, "taste": TASTE, "anatomy": False, "pair": PAIR, "alt_reason": None}

L1 = "I'm seventy-one, and I take the stairs"
L2 = "faster than women half my age."
L3 = "Last Sunday, my daughter walked behind me the whole way up and said,"
L4 = "Mama, when did that happen?"

add("HK-01a", L1, f'''For the line "{L1}": Keep this photo exactly as it is — hall, staircase, camera, light — as a tall 9:16 crop centred on the flight, and add two women climbing it. Image 1 is the hall and staircase. Image 2 is the older woman. Image 3 is her daughter.
The same woman as Image 2, seventy-one, on the 6th of 14 steps mid-step: weight on her right foot, left foot lifting to the 7th, both hands free at her sides, face in part profile, eyes up the stairs, mouth closed; {N_WARD}. The same woman as Image 3 on the 4th step, inside the rail behind her, right hand on the oak handrail, left hand loose at her side, eyes on her mother's back; {C2_WARD}. The two fill more than half the frame's height.
In the frame: the two women, the one staircase of Image 1 with its runner, brass rods, balusters and photo wall, the hall floor below; every other surface bare. Two legs each, one foot per step.
The render and light of Image 1, the women on model, a catchlight in each eye.
Clothing, shoes, walls and frames plain — no lettering, logos or labels; no third person.''',
    [REF_P0, REF_N, REF_C2], face=True, match="plate", edit_of=P0)

add("HK-01b", L2, f'''For the line "{L2}": at step height from the side, an older woman's feet take the stairs at a stride — one low black pump planted on the 6th of 14 steps, the other foot lifting to the 7th, the hem of an emerald-green dress swinging at mid-calf — and a few steps below, white trainers under black denim shorts reaching for the 4th step. Image 1 is the staircase.
Close-up, profile, at the height of the 6th step, feet and five steps filling the frame, sharp on the pumps. The same beige runner, brass stair rods, white balusters and dark oak handrail as Image 1, photo frames soft behind. Both women's hands and faces out of frame — the picture is feet, legs below the knee and steps. Deep brown skin at the ankles.
In the frame: two low black pumps, two white trainers, four legs, five steps of the one staircase; every other surface bare. Each foot whole, one foot per step.
{REG}, afternoon sun through the door sidelights from the left.
Shoes, clothing and walls plain — no lettering, logos or labels.''',
    [REF_P0], face=False)

add("HK-02a", L3, f'''For the line "{L3}": her daughter near the top of the flight, a hand on the rail, looking up after her, a little out of breath. Image 1 is the daughter. Image 2 is the hall and staircase.
Medium close-up from the top of the flight looking down, front-on, sharp on her eyes. The same woman as Image 1 on the 12th of 14 steps, mid-step, weight on her right foot, the left lifting to the 13th, right hand gripping the dark oak handrail, left hand on her thigh, chest rising, lips parted, face up, both eyes up into the lens; {C2_WARD}. She fills more than half the frame's height. Below her the staircase of Image 2, its photo wall and the hall floor far down.
In the frame: one woman, the one staircase, the photo wall; every other surface bare. Two hands, two legs.
{REG}, afternoon sun from below lighting her front left.
Clothing, shoes, walls and frames plain — no lettering, logos or labels; no second person.''',
    [REF_C2, REF_P0], face=True)

add("HK-03a", L4, f'''For the line "{L4}": Keep this photo exactly as it is — hall, staircase, camera, light — as a tall 9:16 crop on the top four steps and the landing, with two women there. Image 1 is the hall and staircase. Image 2 is the mother. Image 3 is her daughter.
The same woman as Image 2 on the landing at the head of the flight, body facing along it, head turned back over her left shoulder to her daughter, a small knowing smile, mouth closed, eyes on her daughter, both hands free at her sides; {N_WARD}. The same woman as Image 3 on the 14th and top step, right hand on the handrail, left hand on her chest, face turned up to her mother, both eyes on her, mouth open mid-word; {C2_WARD}. The two fill over half the frame's height.
In the frame: the two women, the top of the one staircase of Image 1 with its runner, balusters and handrail, the landing wall; every other surface bare. Two legs each.
The render and light of Image 1, the women on model, a catchlight in each eye.
Clothing, shoes and walls plain — no lettering, logos or labels; no third person.''',
    [REF_P0, REF_N, REF_C2], face=True, match="plate", edit_of=P0)

# ---- pinned end frames (§27G rules 5 & 10: stairs class) — each an edit of its start frame (A of A, B of B)
END = {}
END["HK-01a-END"] = (L1, f'''For the line "{L1}": Keep this picture exactly as it is — the staircase, the camera, the light, the two women and their clothes — and move them two steps higher. Image 1 is the start frame.
The older woman now on the 8th of 14 steps, mid-step, weight on her left foot, right foot lifting to the 9th, both hands free at her sides, the side of her face showing, eyes up the stairs, mouth closed. Her daughter now on the 6th step, inside the rail behind her, right hand on the oak handrail, left hand loose at her side, eyes on her mother's back.
In the frame: the two women, the one staircase of Image 1, the hall floor below; every other surface bare. Two legs each, one foot per step. Everything else exactly as Image 1.
Clothing, shoes, walls and frames plain — no lettering, logos or labels; no third person.''', True)
END["HK-01b-END"] = (L2, f'''For the line "{L2}": Keep this picture exactly as it is — the staircase, the camera, the light, the shoes and the hems — and move the feet two steps higher. Image 1 is the start frame.
The low black pump now planted on the 8th of 14 steps, the other foot lifting to the 9th, the emerald hem swinging at mid-calf; the white trainers now reaching for the 6th step. Both women's hands and faces out of frame — the picture is feet, legs below the knee and steps.
In the frame: two low black pumps, two white trainers, four legs, five steps of the one staircase; every other surface bare. Each foot whole, one foot per step. Everything else exactly as Image 1.
Shoes, clothing and walls plain — no lettering, logos or labels.''', False)
END["HK-02a-END"] = (L3, f'''For the line "{L3}": Keep this picture exactly as it is — the staircase, the camera, the light, the woman and her clothes — and move her one step higher. Image 1 is the start frame.
The daughter now on the 13th of 14 steps, one below the top, both feet planted, right hand still gripping the dark oak handrail, left hand on her thigh, chest rising, lips parted on a breath, face fully turned up, both eyes up into the lens.
In the frame: one woman, the one staircase, the photo wall; every other surface bare. Two hands, two legs. Everything else exactly as Image 1.
Clothing, shoes, walls and frames plain — no lettering, logos or labels; no second person.''', True)
for b, (ln, pr, face) in END.items():
    add(b, ln, pr, [{"label": "the start frame (A of A, B of B)", "kind": "frame"}], face=face, match="frame", edit_of="<start frame>")

if __name__ == "__main__":
    fails = 0
    for b, c in CALLS.items():
        (H / f"{b}.prompt.txt").write_text(c["prompt"])
        (H / f"{b}.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.preflight.json")], capture_output=True, text=True)
        bad = [l for l in r.stdout.splitlines() if "FAIL" in l]
        print(f"{b}: {len(c['prompt'])} chars — {'PASS' if r.returncode == 0 else 'FAIL'}")
        for l in bad: print("   ", l)
        fails += r.returncode != 0
    sys.exit(1 if fails else 0)
