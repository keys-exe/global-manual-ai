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

FRAMES = [
    dict(beat="SC02-SH01", line=L017, refs=["P-HOUSE", "N"], face=True, body=True, match=None, role="master",
         motion="From this frame: she keeps her right hand on the newel post and calls down the line; she stays on the landing.",
         prompt=" ".join([
             f"For the line \"{L017}\": she stands stranded at the top of her stairs at night, calling down.",
             "SCENE MASTER, Scene 2. A full-length shot from low at the foot of the stairs, three-quarter on, looking up the straight flight to the landing.",
             "Image 1 is this hall: stairs up the left-hand wall, dark banister and square spindles on the open right side, framed photographs up the wall, brass stair rods, oatmeal carpet — copied exactly.",
             f"On the landing stands {HER}, in a heather-green jumper, charcoal A-line skirt and grey slippers.",
             "Her right hand rests on the top newel post, her left hand loose at her side; she is looking down the stairs, mouth open mid-word, about a third of the frame's height.",
             "Two plain shopping bags stand on the carpet at the foot of the bottom step; the telephone table holds only the telephone.",
             "Night: hall pendant and landing lamp, warm 2800K, key from the right; the rest of the house deep blue-grey.",
             PLAIN, LOOK])),
    dict(beat="SC02-SH03", line=L019, refs=["L-STAIRS", "N"], face=True, body=True, match="plate", edit_of="L-STAIRS v4", role="master",
         motion="From this frame: she lowers her left foot to the next step down, then her right foot beside it, both hands sliding down the banister — one step every three seconds, backwards.",
         prompt=" ".join([
             f"For the line \"{L019}\": Keep this photo exactly as it is — Image 1, the stairs from the landing down to the green front door, banister on the left, photographs on the right wall, brass rods; the camera stays high on the landing, recomposed as a tall vertical frame.",
             f"SCENE MASTER, Scene 2, next morning. Add {HER}, in a pale-blue quilted dressing gown, grey nightdress and grey slippers.",
             "She is going down backwards: on the second step, facing up toward the camera, turned to the banister, both hands gripping its rail on frame left, left foot lowered to the next step, right foot on the step above.",
             "Head bowed, looking down at her feet, jaw set; about a third of the frame's height. Every step bare.",
             "Cold grey morning light from the frosted landing window, 6500K, key from the left; the hall below dim.",
             PLAIN, LOOK])),
    dict(beat="SC02-SH07", line=L022, refs=["L-BEDROOM", "N"], face=True, body=True, match="plate", edit_of="L-BEDROOM v1", role="master",
         motion="From this frame: she sits still on the edge of the bed, hands in her lap, eyes on the window; only her breathing moves.",
         prompt=" ".join([
             f"For the line \"{L022}\": Keep this photo exactly as it is — Image 1, the bedroom from the doorway: the bed with the pale green candlewick bedspread on the right, the dark-wood chest of drawers under the window, the walnut wardrobe on the left, the half-open door soft in the near foreground; the camera stays in the doorway, recomposed as a tall vertical frame.",
             f"SCENE MASTER, Scene 2, that afternoon. Add {HER}, in the pale-blue quilted dressing gown and grey slippers.",
             "She sits alone on the near edge of the bed, three-quarter from behind, both feet flat on the carpet, both hands in her lap, her eyes on the window; about a third of the frame's height.",
             "The bed made and bare; the bedside table holds only its lamp, switched off.",
             "Flat grey overcast daylight through the nets, 6500K, from the window ahead.",
             PLAIN, LOOK])),
]

if __name__ == "__main__":
    for f in FRAMES:
        refs = [{"kind": KIND[r], "label": LABEL[r], "ref": f"stryde-half-my-age__{REF_ID[r]}", "job": JOB[r], "role": f"Image {i + 1}"}
                for i, r in enumerate(f["refs"])]
        call = {"beat": f["beat"], "kind": "image", "mode": 4, "prompt": f["prompt"], "script_line": f["line"], "refs": refs,
                "face": f["face"], "body": f["body"], "room": True, "product": False, "match": f.get("match"), "edit_of": f.get("edit_of"),
                "pair": ["gpt_image_2_5", "gpt_image_2_5"], "model": "gpt_image_2_5 · sunburst · high · 2k · 9:16",
                "role": f["role"], "motion_plan": f["motion"], "scene": 2,
                "taste": ["HT02", "HT04", "HT09", "HT17", "HT18", "HT19", "HT22"]}
        (H / f"{f['beat']}.frame.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{f['beat']}.frame.txt").write_text(f["prompt"])
        print(f["beat"], len(f["prompt"]), "chars")
