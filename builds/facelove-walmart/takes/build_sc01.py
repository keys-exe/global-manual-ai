#!/usr/bin/env python3
"""SC01-T1 — Hook 1, the carts hit. One Seedance 2.5 take (§24K part 5), SD-PROMPT (V7.97.0), sound on (V7.101.0).
Rows SC01-SH01…SH07 of step5/act_rows.json, 27 s, eight shots."""
import json, pathlib
H = pathlib.Path(__file__).parent
L2 = "Michelle? Is that you? My God, what happened, did you get work done? You look so much more beautiful."
rows = {r["beat"]: r for r in json.load(open(H.parent / "step5/act_rows.json")) if r["group"] == "SC01"}
s1, s7 = rows["SC01-SH01"], rows["SC01-SH07"]
marks = {"N": "Michelle mid-aisle by the paper shelves pushing her cart toward the walkway", "C1": "Peter and the woman unseen beyond the end-cap on the walkway", "C2": "Peter and the woman unseen beyond the end-cap on the walkway"}  # the row marks, as written in start_pos
P = f"""REFERENCES
@image1 — Michelle, 63: face, hair and build only.
@image2 — Peter, 65: face, hair and build only.
@image3 — the woman, 41, with Peter: face, hair and build only. Clothes are written in LOOK.
@image4 — the store aisle: copy it — paper shelves left, detergent shelves right, the blue end-cap at the far right corner, the walkway across the far end.
@image5 — the same aisle from the walkway: the end-cap on the left.
@audio1 — Michelle's voice.
@audio2 — Peter's voice.

SHOT: A warm animated family drama with a comic sting: in a bright store aisle Michelle's cart hits her ex-husband's, he can barely place her, she answers in four words and glides away; one take of eight shots, 9:16, 27 s.

TIMELINE
[0–3s] Shot 1 · wide, leading her, backing away in front, 28mm: Frame 1: {s1['start_pos']}. Brisk: {s1['motion']}.
[3–5s] Shot 2 · insert, low on the floor, crash zoom: {rows['SC01-SH02']['motion']}.
[5–9s] Shot 3 · medium two-shot, slow tilt up from his hands to his face: Peter looks up annoyed, then his face changes; {rows['SC01-SH03']['motion']}.
[9–14s] Shot 4 · close-up, low, slow push-in: Peter stares, his mouth falling open between questions. Peter says: "{L2}"
[14–17s] Shot 5 · medium shot past the woman's arm, slow pan: Peter leans over his cart toward Michelle, waiting; the woman beside him goes still.
[17–20s] Shot 6 · close-up, locked: Michelle holds his look for a beat, calm, cool, unbothered; one corner of her mouth lifts. Michelle says: "It is just me."
[20–24s] Shot 7 · full shot, the camera follows from behind: {rows['SC01-SH06']['motion']} along the walkway, unhurried, never looking back.
[24–27s] Shot 8 · medium, high, the camera pulls back: Peter stands frozen staring after her; the woman's head turns slowly from her to him. Last frame: {s7['end_pos']}.

LOOK: A theatrical 3D animated feature, stylised adults with large expressive eyes; bright whites and cool blues, ungraded; light from the overhead panels, a shadow side on every face. Michelle: cream boat-neck knit sweater, camel wide-leg trousers, tan loafers. Peter: navy quarter-zip, white collar, tan chinos. The woman: camel cropped blazer, white tank, black flared leggings, white trainers.

SOUND: Dialogue in natural American English — Peter's voice from @audio2 on shot 4, Michelle's from @audio1 on shot 6; on every other shot nobody speaks. No music. The actions' own sounds: cart wheels rattling on the floor, the metal clang of the hit, her loafers as she leaves; the store's soft hum under it.

KEEP: same faces, hair and clothes in every frame; just these three people in the aisle; full-size store carts, plain and unbranded; five fingers on each hand; real weight in the hit and the walk; eyes off the lens; text, logos and captions nowhere"""
call = {"beat": "SC01-T1", "take": "SC01-T1", "build": "facelove-walmart", "connector": "seedance", "model": "seedance_2_5", "mode": 5, "kind": "multi",
        "prompt": P, "duration": 27, "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": True,
        "files": ["cast/N-MICHELLE-AFTER", "cast/C1-PETER", "cast/C2-YOUNGER", "plates/L-AISLE", "plates/L-AISLE-REV"],
        "media": ["7ee60be8-ae88-458d-8d13-d5ebfc2ff6a7", "cd1173f1-ffef-4258-90f0-4c5143ea351b", "260a0f37-7ab1-4b16-b87a-ccc9c4bba621",
                  "61b35cd5-43a2-4e4d-a243-be5ace889248", "12d24c80-9b60-4ead-a892-c373e9c984fd"],
        "audios": ["voice/N_voice_master.mp3", "voice/C1_voice_master.mp3"], "audio_media": ["18b2c0a4-b1d2-40f0-8321-dbd8fba7c8f1", "57c4e338-a41d-4931-a5ac-9ecbd7e26975"],
        "generate_audio": True, "dialogue": L2, "script_line": L2, "dialogue_2": "It is just me.",
        "covers": list(rows), "start_pos": s1["start_pos"], "end_pos": s7["end_pos"], "marks": marks, "motion": s1["motion"],
        "subject_motion": "travels", "pace": s1["pace"], "prefer_multi_shots": "false", "generation": 1, "user_go": None, "rack": None,
        "risks": [{"risk": "a real store brand or logo on the shelves or carts", "prevented_by": "plates are unbranded; KEEP: plain unbranded carts, text and logos nowhere"},
                  {"risk": "voices swapped or a third voice", "prevented_by": "SOUND names whose voice from which audio ref, on which shot; nobody speaks elsewhere"},
                  {"risk": "the aisle flips sides between the forward and reverse shots", "prevented_by": "@image4/@image5 sides written out; marks against the end-cap"}],
        "taste": ["no real brand or logo in frame (F-flags)", "faces from sheets, clothes in words"]}
(H / "SC01-T1.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
print(len(P))
