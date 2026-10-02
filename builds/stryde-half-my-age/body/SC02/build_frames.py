"""Scene 2 (Rock bottom) — start frames for the Wan 3.0 body (§18A: the body is a declared adopting build, §24H frames).
Round 1: the three SCENE MASTER frames (B1 night on the stairs, B2 morning on the stairs, B2 afternoon in the bedroom),
each an A/B pair of Sunburst renders (§5, preflight). Coverage frames (SH02, SH04, SH05, SH06) and the SH03 end frame
(stairs = pinned, §35A rule 10) are built against the confirmed masters in round 2.
House Taste applied: HT02 (the struggle for real: backwards, both hands on the rail), HT04 (the move in progress, from the top),
HT09/HT17 (the plate matched by editing it), HT18 (plain, unbranded), HT19 (a counted frame), HT22 (the stairs' geography)."""
import json
from pathlib import Path

H = Path(__file__).parent
JOB = {"N": "30fd2bc8-17e3-4e27-b2cf-8225e00b088c", "C3": "98c11aee-5f7f-4244-a68e-d649856acf2d",
       "P-HOUSE": "cc27b514-c130-4cc5-abec-f01c18368e62", "L-STAIRS": "73351f73-d511-45c9-839f-4aec7c451868",
       "L-BEDROOM": "1af15221-e405-4725-9b43-e006f801af2e"}
LABEL = {"N": "Her — cast sheet (face, hair, build)", "C3": "The husband — cast sheet",
         "P-HOUSE": "Her house — hall and stairs from the front door", "L-STAIRS": "Her stairs from the landing (v4)",
         "L-BEDROOM": "Her bedroom from the doorway"}
KIND = {"N": "character", "C3": "character", "P-HOUSE": "location", "L-STAIRS": "location", "L-BEDROOM": "location"}
REF_ID = {"N": "N-HER", "C3": "C3-HUSBAND", "P-HOUSE": "P-HOUSE", "L-STAIRS": "L-STAIRS", "L-BEDROOM": "L-BEDROOM"}
HER = "the woman from Image 2 — face, steel-grey bob with its heavy fringe and small slight build copied exactly"
LOOK = "A still from a British prestige drama, ARRI Alexa, natural colour, real texture."
PLAIN = "Clothing and bags plain and unbranded."

L017 = "Just leave it by the stairs, love. I’ll get it later."
L019 = "Six weeks ago, I was going down my stairs backwards. One step at a time."
L022 = "If I’m being honest, some days I wasn’t going down them at all. I’d just stay upstairs."

# Round 2 (user Fix: "more emotional camera angles… the best Netflix style cinematic") — spindles as bars, profile through the
# spindles, a sliver through the door gap: all three still wide, her small in frame.
# Round 3 (user Fix: "I want new ones, all of them are not good"): the emotion is in her face, so every key frame goes close —
# long lens, shallow focus, her face and hands large in frame, one hard motivated light, the house falling away soft behind.
GO = "i want new ones the all of theme are not good (scene 2)"
GO4 = "use gpt image 2 and not sunburst re do all the scene 2"
FRAMES = [
    # Fresh start (user 2026-10-01: "redo the shot 1 of scene 2, fresh start, cause everything you gave me is not correct"):
    # built only from the plan — act map SC02-SH01 ("from the hall looking up at her on the landing — she is stranded up there",
    # FULL, night: hall pendant + landing lamp), wardrobe B1 = her cast-sheet outfit (green jumper, charcoal skirt, black shoes —
    # never slippers), and the confirmed hall plate edited in place (HT17), the camera left exactly where the plate's is.
    dict(beat="SC02-SH01", line=L017, refs=["P-HOUSE", "N"], face=True, body=True, match="plate", edit_of="P-HOUSE v1", role="key", gen=7,
         fix="re do the shot1 of the scene 2 fresh start cause everything you gave me is not correct",
         motion="From this frame: she stays on the landing, right hand on the newel post, and calls the line down to the hall; on 'later' she looks away from the stairs; she does not step down.",
         prompt=" ".join([
             f"For the line \"{L017}\": Keep this photo exactly as it is — Image 1, the hall seen from the front door: the staircase rising straight ahead along the left-hand wall with its framed photographs, the dark banister on its right, the landing and its lamp at the top, the telephone table with only the telephone, the barometer, the doorways on the right. The camera stays exactly where it is; recompose it as a tall vertical frame centred on the staircase.",
             "Change only three things.",
             "It is night: the hall's glass pendant and the landing lamp are lit, warm 2800K; the door glass is dark.",
             "Add the woman from Image 2, exactly as on her sheet — face, steel-grey bob with its heavy fringe, small build, and the same clothes: the green crew-neck jumper, charcoal skirt and black low-heeled shoes. She stands on the landing at the very top of the stairs, small in the frame, facing down the flight toward the camera, her right hand on the top newel post, her left hand at her side; she is looking down the stairs, calling, tired.",
             "Two plain shopping bags stand on the hall carpet at the foot of the bottom step.",
             PLAIN])),
    dict(beat="SC02-SH03", line=L019, refs=["L-STAIRS", "N"], face=True, body=True, match=None, role="key", gen=3,
         motion="From this frame: she lowers her weight down one step backwards, both hands sliding a little down the banister, and breathes out through her mouth; one step in the clip.",
         prompt=" ".join([
             f"For the line \"{L019}\": each step down her own stairs costs her.",
             "A close-up from the landing above and to her side, 85mm lens, shallow focus on her face and hands.",
             f"{HER}, in a pale-blue quilted dressing gown, is going down backwards: she faces up the stairs, two steps below the camera.",
             "Both hands grip the dark banister rail beside her face, knuckles pale; her head is bowed, eyes down on the step at her feet, brow tight, lips pressed, a held breath.",
             "Image 1 is this staircase: below her, out of focus, the oatmeal stair carpet and brass rods drop away toward the hall.",
             "Cold grey morning light from the frosted landing window, 6500K, from frame left, lights her face and hands; the far side in soft shadow.",
             PLAIN, LOOK])),
    dict(beat="SC02-SH07", line=L022, refs=["L-BEDROOM", "N"], face=True, body=True, match=None, role="key", gen=3,
         motion="From this frame: she sits still, eyes on the window; she blinks once and her thumb moves over her other hand; nothing else moves.",
         prompt=" ".join([
             f"For the line \"{L022}\": some days she gives up and stays upstairs.",
             "A close profile shot at her eye level, 85mm lens, very shallow focus on her eye; her face fills the left half of the frame, the right half open toward the window.",
             f"{HER}, in a pale-blue quilted dressing gown, sits on the edge of her bed.",
             "Her hands rest in her lap, one thumb over the other hand; her eyes on the window and the grey garden, wet but no tears, mouth still.",
             "Image 1 is this bedroom: behind her, far out of focus, the net curtains and the dark-wood chest of drawers.",
             "Flat grey afternoon daylight through the nets, 6500K, falls on the front of her face; the back of her head in shadow.",
             PLAIN, LOOK])),
]

if __name__ == "__main__":
    for f in FRAMES:
        refs = [{"kind": KIND[r], "label": LABEL[r], "ref": f"stryde-half-my-age__{REF_ID[r]}", "job": JOB[r], "role": f"Image {i + 1}"}
                for i, r in enumerate(f["refs"])]
        call = {"beat": f["beat"], "kind": "image", "mode": 4, "prompt": f["prompt"], "script_line": f["line"], "refs": refs,
                "face": f["face"], "body": f["body"], "room": True, "product": False, "match": f.get("match"), "edit_of": f.get("edit_of"),
                "pair": ["gpt_image_2", "gpt_image_2"], "model": "gpt-image-2 image-to-image · 9:16 (Kie AI)",
                "model_override": "user 2026-10-01: \"use gpt image 2 and not sunburst, re do all the scene 2\" — overrides the §18A Sunburst routing for this build's body frames",
                "role": f["role"], "motion_plan": f["motion"], "scene": 2,
                "taste": ["HT02", "HT04", "HT09", "HT18", "HT19", "HT22"], "generation": f.get("gen", 1), "fix_note": f.get("fix") or (GO if f.get("gen", 1) > 1 else None)}
        (H / f"{f['beat']}.frame.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{f['beat']}.frame.txt").write_text(f["prompt"])
        print(f["beat"], len(f["prompt"]), "chars")
