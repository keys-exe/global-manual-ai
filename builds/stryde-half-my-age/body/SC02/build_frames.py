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

# Round 2 (user Fix, chat: "I want new ones in scene two, more emotional camera angles, the best Netflix-style cinematic"):
# each master rebuilt around one emotional idea — SH01 trapped behind the spindles, SH03 the strain in profile against the
# cold window, SH07 a sliver of her through the door gap, small in the negative space. Low-key motivated light, deeper shadow.
GO = "I WANT NEW ONES IN SCENE TWO MORE EMOTIONAL CAMERA ANGLES I WANT THE BEST NETFLIX STYLE CINEMATIVE"
FRAMES = [
    dict(beat="SC02-SH01", line=L017, refs=["P-HOUSE", "N"], face=True, body=True, match=None, role="master", gen=2,
         motion="From this frame: she keeps her right hand on the newel post and calls down the line; she stays on the landing.",
         prompt=" ".join([
             f"For the line \"{L017}\": she is stranded at the top of her own stairs at night, calling down.",
             "SCENE MASTER, Scene 2. A low, wide shot from the dark hall floor, looking up the whole flight through the banister's square spindles: the dark spindles soft in the near foreground like bars, the flight rising between them.",
             "Image 1 is this hall and staircase — copied exactly.",
             f"At the top, small in the frame, stands {HER}, in a heather-green jumper and charcoal skirt, in the one pool of warm light from the landing lamp.",
             "Her right hand grips the newel post, her left hand at her chest; she is looking down the stairs, mouth open mid-word, the face lit, tired.",
             "Two plain shopping bags at the foot of the bottom step, near frame; every step bare.",
             "Low-key night: one warm 2800K lamp on the landing, the hall below in deep blue-grey shadow, high contrast.",
             PLAIN, LOOK])),
    dict(beat="SC02-SH03", line=L019, refs=["L-STAIRS", "N"], face=True, body=True, match=None, role="master", gen=2,
         motion="From this frame: she lowers her left foot to the next step down, then her right foot beside it, both hands sliding down the banister — one step every three seconds, backwards.",
         prompt=" ".join([
             f"For the line \"{L019}\": she goes down her stairs backwards, one step at a time.",
             "SCENE MASTER, Scene 2, next morning. A medium-wide shot level with her, side-on in profile from beside the flight, through the banister spindles, long lens, shallow focus on her face.",
             "Image 1 is this staircase — the oatmeal carpet, brass stair rods, dark banister — copied exactly.",
             f"Mid-flight is {HER}, in a pale-blue quilted dressing gown and grey slippers, facing up the stairs, going down backwards.",
             "Both hands grip the banister rail, knuckles pale; her left foot reaches down for the next step, her right still on the step above; eyes down on the step, jaw set, a breath held.",
             "Every step bare.",
             "Cold grey morning: the frosted landing window behind her rims her hair and shoulders, her face half in shadow; 6500K, soft, low-key.",
             PLAIN, LOOK])),
    dict(beat="SC02-SH07", line=L022, refs=["L-BEDROOM", "N"], face=True, body=True, match=None, role="master", gen=2,
         motion="From this frame: she sits still on the edge of the bed, hands in her lap, eyes on the window; only her breathing moves.",
         prompt=" ".join([
             f"For the line \"{L022}\": she stays upstairs, alone, instead of going down.",
             "SCENE MASTER, Scene 2, that afternoon. Seen from the dark landing through the gap of the half-open bedroom door: the door and frame dark and soft at both sides of the frame, a tall bright sliver of room between them.",
             "Image 1 is this bedroom — the pale green candlewick bedspread, the dark-wood chest of drawers under the window — copied exactly.",
             f"In the sliver, small, sits {HER}, in the pale-blue dressing gown, on the far edge of the bed, three-quarter from behind.",
             "Both hands rest in her lap, both feet flat on the carpet; her eyes on the window and the grey garden beyond the nets.",
             "The bed made and bare; the bedside table holds only its lamp, switched off.",
             "Flat grey afternoon light from the window ahead silhouettes her softly; the landing around the door in shadow.",
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
                "taste": ["HT02", "HT04", "HT09", "HT18", "HT19", "HT22"], "generation": f.get("gen", 1), "fix_note": GO if f.get("gen", 1) > 1 else None}
        (H / f"{f['beat']}.frame.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{f['beat']}.frame.txt").write_text(f["prompt"])
        print(f["beat"], len(f["prompt"]), "chars")
