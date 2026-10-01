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

if __name__ == "__main__" and not any(a in sys.argv for a in ("--v2","--v3","--v4","--v5")):
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

# ---- v2 (user 2026-10-01 "generate new ones"; end frames waived) — the faults read off v1: HK-01b a white top edge at the daughter's hip;
# HK-02a bare treads + a hall mat (A) / a tiled hall floor (B), off the plate; HK-03a A put the mother on the hall floor at the foot of the stairs.
V2 = {}
V2["HK-01b"] = f'''For the line "{L2}": at step height from the side, an older woman's feet take the stairs at a stride — one low black pump planted on the 6th of 14 steps, the other foot lifting to the 7th, the hem of an emerald-green dress swinging at mid-calf — and a few steps below, white trainers under black denim shorts reaching for the 4th step. Image 1 is the staircase.
Close-up, profile, at the height of the 6th step, feet and five steps filling the frame, sharp on the pumps; the frame's top edge cuts the green dress at the knee and the olive sweatshirt hem at the hip. The same beige runner, brass stair rods, white balusters and dark oak handrail as Image 1, photo frames soft behind. Both women's hands and faces out of frame.
In the frame: two low black pumps, two white trainers, four legs, five steps of the one staircase; every other surface bare. Each foot whole, one foot per step.
A final frame from a 3D animated feature film — stylized storybook render, every surface with a material, afternoon sun through the door sidelights from the left.
Shoes, clothing and walls plain — no lettering, logos or labels.'''
V2["HK-02a"] = f'''For the line "{L3}": her daughter near the top of the flight, a hand on the rail, looking up after her, a little out of breath. Image 1 is the daughter. Image 2 is the hall and staircase.
Medium close-up from the top of the flight, front-on, sharp on her eyes. The same woman as Image 1 on the 12th of 14 steps, mid-step, weight on her right foot, the left lifting to the 13th, right hand gripping the oak handrail, left hand on her thigh, lips parted, face up, both eyes up into the lens; {C2_WARD}. She fills over half the frame. Below her the staircase of Image 2 copied exactly — beige runner, a brass rod on every step, white balusters, the photo wall — and far down the bare oak floorboards of Image 2.
In the frame: one woman, the one staircase, the photo wall, the oak floor; every other surface bare. Two hands, two legs.
A final frame from a 3D animated feature film — stylized storybook render, a catchlight in each eye, afternoon sun from below, front left.
Clothing, shoes and walls plain — no lettering, logos or labels; no second person.'''
V2["HK-03a"] = f'''For the line "{L4}": Keep this photo exactly as it is — hall, staircase, camera, light — as a tall 9:16 crop on the top steps and the landing, with two women there. Image 1 is the hall and staircase. Image 2 is the mother. Image 3 is her daughter.
The landing is a storey above the hall, at the head of the 14-step flight. The same woman as Image 2 standing on the landing floor itself, above the top step, body facing along it, head turned back over her left shoulder to her daughter, a small knowing smile, mouth closed, eyes on her daughter, hands free at her sides; {N_WARD}. The same woman as Image 3 one step below on the 14th and top step, right hand on the handrail, left hand on her chest, face up to her mother, both eyes on her, mouth open mid-word; {C2_WARD}. The two fill over half the frame.
In the frame: the two women, the top of the one staircase of Image 1, the landing wall; every other surface bare. Two legs each.
The render and light of Image 1, the women on model.
Clothing, shoes and walls plain — no lettering, logos or labels; no third person.'''
if __name__ == "__main__" and "--v2" in sys.argv and "--v5" not in sys.argv:
    fails = 0
    for b, pr in V2.items():
        c = dict(CALLS[b]); c["prompt"] = pr; c["fix_note"] = "see V2 comment"
        (H / f"{b}.v2.prompt.txt").write_text(pr); (H / f"{b}.v2.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v2.preflight.json")], capture_output=True, text=True)
        print(f"{b} v2: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
        fails += r.returncode != 0
    sys.exit(1 if fails else 0)

# ---- v3 (user 2026-10-01 "FIX THOSE": HK-01b "WRONG CHARACTER", HK-02a "INCORRECT PLACEMENTS OF PICTURE FRAMES FIX THE LOCATION", HK-03a "WRONG LOCATION").
# HT17: all three are now image edits of the CONFIRMED HK-01a frame A (the user's pick: the right staircase, the right two women) — Image 1 = that frame.
# HT23 (V7.78.1): one SCENE SO FAR line on every hook shot.
HK01A_A = "dd00641302644603f67a37537f1e5afe"   # HK-01a v1 A, confirmed (Higgsfield job c5ffa422…)
SCENE = "Scene so far: one straight 14-step flight, hall to landing, photo wall on its right, balusters and oak rail on its left; the mother climbs ahead hands free, the daughter behind, right hand on the rail; nobody holds anything."
V3 = {}
V3["HK-01b"] = f'''For the line "{L2}": Keep the two women of this picture exactly — skin, build, the emerald-green dress, black pumps, black denim shorts, white trainers — and the same staircase, reframed as a close-up of their feet. Image 1 is the confirmed frame of this moment.
Close-up, profile, at the height of the 6th step, feet and five steps filling the frame, sharp on the pumps: one black pump planted on the 6th of 14 steps, the other foot lifting to the 7th, the green hem at mid-calf; a few steps below, the white trainers reaching for the 4th step. The top edge cuts the dress at the knee and the olive sweatshirt hem at the hip. Both women's hands and faces out of frame. {SCENE}
In frame: two black pumps, two white trainers, four legs, five steps of the one staircase, beige runner, brass rods; every other surface bare. Each foot whole, one foot per step.
The render and light of Image 1. Shoes, clothing and walls plain — no lettering, logos or labels.'''
V3["HK-02a"] = f'''For the line "{L3}": Keep this picture exactly as it is — the staircase, the photo wall with every frame where it is, the handrail, the light — and move the two women up it: the daughter near the top, a hand on the rail, looking up after her mother. Image 1 is the confirmed frame of this moment.
Tall crop on the upper half of the flight: the mother stepping onto the landing at the top edge, back to us; the daughter on the 12th of 14 steps, side-on, right hand gripping the oak handrail, left hand on her thigh, lips parted on a breath, face in profile turned up the stairs, eyes on her mother; she fills over half the frame, the photo wall of Image 1 beside her. {SCENE}
In the frame: two women, the one staircase, the photo wall; every other surface bare. Two hands, two legs each.
The render and light of Image 1. Clothing, shoes and walls plain — no lettering, logos or labels; no third person.'''
V3["HK-03a"] = f'''For the line "{L4}": Keep this picture exactly as it is — the staircase, the photo wall, the handrail, the landing, the light — and move the two women to the top. Image 1 is the confirmed frame of this moment.
Tall crop on the top of the flight and the landing of Image 1: the mother standing on the landing floor above the top step, body facing along the landing, head turned back over her left shoulder, a small knowing smile, mouth closed, eyes on her daughter, hands free at her sides; the daughter one step below on the 14th and top step, right hand on the handrail, left hand on her chest, face up to her mother, both eyes on her, mouth open mid-word. The two fill over half the frame. {SCENE}
In the frame: two women, the top of the one staircase, the landing's balusters and rail, the photo wall; every other surface bare. Two legs each.
The render and light of Image 1. Clothing, shoes and walls plain — no lettering, logos or labels; no third person.'''
if __name__ == "__main__" and "--v3" in sys.argv and "--v5" not in sys.argv:
    fails = 0
    for b, pr in V3.items():
        c = dict(CALLS[b]); c["prompt"] = pr; c["refs"] = [{"label": "HK-01a v1 A (confirmed frame)", "kind": "frame"}]; c["match"] = "frame"; c["edit_of"] = HK01A_A
        c["taste"] = TASTE + ["HT23"]; c["fix_note"] = {"HK-01b": "WRONG CHARACTER", "HK-02a": "INCORRECT PLACEMENTS OF PICTURE FRAMES FIX THE LOCATION", "HK-03a": "WRONG LOCATION"}[b]
        (H / f"{b}.v3.prompt.txt").write_text(pr); (H / f"{b}.v3.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v3.preflight.json")], capture_output=True, text=True)
        print(f"{b} v3: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
        fails += r.returncode != 0
    sys.exit(1 if fails else 0)

# ---- v4 (user 2026-10-01 "USE THE CINEMATIC CAMERA ANGLES CAUSE THIS HOOK IS TOO WEAK"; HK-01b Fix note "THEY ARE SO BIG"): the hook re-angled per
# §30I with the §24K part 7 shot names on the user's call — SH-LOW FULL through the newel · SH-GROUND through the balusters · SH-HIGH from the landing ·
# SH-OTS over the daughter's shoulder. New viewpoints, so not edits: the confirmed HK-01a frame A is Image 1 for the scene (same staircase, women, clothes).
SC4 = "Scene so far: one 14-step flight, hall to landing, photo wall on its right, balusters and oak rail on its left; the mother climbs ahead hands free, the daughter behind, right hand on the rail."
V4 = {}
FR1 = {"label": "HK-01a v1 A (confirmed frame)", "kind": "frame"}
V4["HK-01a"] = (f'''For the line "{L1}": a seventy-one-year-old woman towers mid-flight on her staircase, climbing briskly hands free, her daughter two steps behind reaching for the rail. Image 1 is this scene's confirmed frame — same staircase, women and clothes. Image 2 is the older woman. Image 3 is her daughter.
Full shot from the foot of the stairs, the lens at hip height by the newel looking steeply up the flight, deep focus, balusters and photo wall converging to the landing light. The same woman as Image 2 on the 6th of 14 steps, weight on her right foot, left foot lifting to the 7th, hands free at her sides, chin up, eyes on the landing; {N_WARD}. The same woman as Image 3 on the 4th step, right hand reaching the oak handrail, left hand loose, eyes on her mother's back; {C2_WARD}. Both at true scale to the flight.
In the frame: the two women, the one staircase of Image 1, the newel; every other surface bare. Two legs each, one foot per step.
The render and light of Image 1. Clothing, shoes and walls plain — no lettering, logos or labels; no third person.''', [FR1, REF_N, REF_C2], True)
V4["HK-01b"] = (f'''For the line "{L2}": at tread level through the white balusters, an older woman's black pump strikes the 7th of 14 steps mid-stride, her green hem swinging, and a few steps below a white trainer lands on the 5th. Image 1 is this scene's confirmed frame — same staircase, shoes and hems.
Close-up, the lens resting on the 4th step at the open side of the flight, looking along the treads past two balusters soft and pale in the near foreground, sharp on the black pump, the lower steps soft: the pump, a deep brown ankle and the emerald hem at the left, the white trainer and a bare brown shin under black denim shorts at the right, the beige runner and brass rods between. Both women's hands and faces out of frame; the feet at true scale to the steps, each step at shin height.
In frame: two black pumps, two white trainers, four legs below the knee, four steps of the one staircase, two balusters; every other surface bare. Each foot whole, one foot per step.
The render and light of Image 1. Shoes, clothing and walls plain — no lettering, logos or labels.''', [FR1], False)
V4["HK-02a"] = (f'''For the line "{L3}": her daughter on the 12th step below, a hand on the rail, looking up at the lens, out of breath. Image 1 is this scene's confirmed frame. Image 2 is the daughter. Image 3 is the hall and staircase.
Medium shot from the landing, the lens above head height looking steeply down the flight, sharp on her eyes. The same woman as Image 2 on the 12th of 14 steps, weight on her right foot, the left lifting to the 13th, right hand gripping the oak handrail, left hand on her thigh, lips parted, face up, both eyes up into the lens; {C2_WARD}. Past her the flight of Image 3 falls away: the photo wall at the left of frame, balusters and handrail at the right, beige runner and brass rods, the bare oak floor and the front door far below.
In the frame: one woman, the one staircase, the photo wall, the hall floor, the front door; every other surface bare. Two hands, two legs.
The render of Image 1, sun from the sidelights below, a catchlight in each eye. Clothing, shoes and walls plain — no lettering, logos or labels; no second person.''', [FR1, REF_C2, REF_P0], True)
V4["HK-03a"] = (f'''For the line "{L4}": over the daughter's shoulder on the top step, her mother on the landing turned back with a small knowing smile. Image 1 is this scene's confirmed frame. Image 2 is the mother. Image 3 is her daughter.
Medium close-up over the daughter's right shoulder from the top step, her olive shoulder and afro puff soft in the near right foreground, the lens at her eye height, sharp on her mother's eyes. The same woman as Image 2 on the landing two paces beyond, body turned along it, head turned back over her left shoulder, a small knowing smile, mouth closed, eyes on her daughter, both hands free at her sides; {N_WARD}. Behind her the landing's balusters, oak rail and the window flaring bright, rimming her silver hair. The same woman as Image 3 in the foreground, only her shoulder and hair.
In the frame: the two women, the landing floor, the balusters and rail, the window; every other surface bare.
The render of Image 1, the window the key light, a catchlight in each eye. Clothing and walls plain — no lettering, logos or labels; no third person.''', [FR1, REF_N, REF_C2], True)
if __name__ == "__main__" and "--v4" in sys.argv and "--v5" not in sys.argv:
    fails = 0
    for b, (pr, refs, face) in V4.items():
        c = dict(CALLS[b]); c.update({"prompt": pr, "refs": refs, "face": face, "match": None, "edit_of": None, "taste": TASTE + ["HT05", "HT23"],
                                      "fix_note": "user: cinematic camera angles — the hook is too weak" + (' / "THEY ARE SO BIG"' if b == "HK-01b" else "")})
        (H / f"{b}.v4.prompt.txt").write_text(pr); (H / f"{b}.v4.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
        r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v4.preflight.json")], capture_output=True, text=True)
        print(f"{b} v4: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
        fails += r.returncode != 0
    sys.exit(1 if fails else 0)

# ---- HK-03a v5 (user Fix on the OTS pair: "wrong location"): the landing has no plate (P1 dropped), so the OTS stays but the picture is an image edit
# of the user's confirmed HK-03a v6 (both women at the top of the flight, seen from the hall — the right location), the viewpoint moved up the flight.
V5 = {}
V5["HK-03a"] = f'''For the line "{L4}": Keep this picture exactly as it is — the top of the staircase, the landing behind it, the photo wall, the handrail, the two women and their clothes, the light — and move the viewpoint up to the 9th step, close behind the daughter. Image 1 is the confirmed frame of this beat.
Medium close-up over the daughter's right shoulder: she stands on the 14th and top step with her back three-quarter to us, her olive shoulder and afro puff soft in the near right foreground, right hand on the handrail; her mother on the landing two paces beyond, body turned along it, head turned back over her left shoulder, a small knowing smile, mouth closed, eyes on her daughter, both hands free at her sides; the mother sharp, the landing wall and balusters of Image 1 behind her exactly as they are.
In the frame: the two women, the top steps, the landing's balusters and rail, the landing wall of Image 1; every other surface bare. Two legs each.
The render and light of Image 1, a catchlight in each eye. Clothing and walls plain — no lettering, logos or labels; no third person; no window.'''
if __name__ == "__main__" and "--v5" in sys.argv:
    b = "HK-03a"; pr = V5[b]
    c = dict(CALLS[b]); c.update({"prompt": pr, "refs": [{"label": "HK-03a v6 B (confirmed frame)", "kind": "frame"}], "face": True, "match": "frame",
                                  "edit_of": "4122ca3c0e3d17a8c4ef2d90f9d03d49 (Old copy of v6; Higgsfield job 4e7f3ff7…)", "taste": TASTE + ["HT05", "HT23"], "fix_note": "wrong location"})
    (H / f"{b}.v5.prompt.txt").write_text(pr); (H / f"{b}.v5.preflight.json").write_text(json.dumps(c, indent=1, ensure_ascii=False))
    r = subprocess.run([sys.executable, str(PF), str(H / f"{b}.v5.preflight.json")], capture_output=True, text=True)
    print(f"{b} v5: {len(pr)} chars — {'PASS' if r.returncode == 0 else 'FAIL'}"); [print("   ", l) for l in r.stdout.splitlines() if "FAIL" in l]
    sys.exit(r.returncode)
