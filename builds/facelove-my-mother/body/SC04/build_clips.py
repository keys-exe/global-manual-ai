"""Scene 4 — THE DISAPPEARING (D2 a weekday morning months later; D3 a family birthday at the daughter's house). Three Seedance 2.5 calls via
Higgsfield (omni_reference, 720p, 9:16), ingredients only, no frames (§4). Three places / days, so three takes (§24K part 5: a take is one place,
one story day). User go: "CONFIRMED ALL IMAGES. PROCEED" (2026-10-02) — INVITE-CARD, OLD-FOUNDATION-CARD, OUTFIT-N-D2, OUTFIT-N-D3, N-FACE confirmed.
All three are silent (generate_audio false); narration VO-T1-L009 is laid in per take after the render, each phrase on its own shot.
Susan's day clothes differ from her sheet's party outfit, so her face goes in as N-FACE and the outfit card carries the clothes (HT26, HT27)."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).parent; B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "body/SC01/build_clips.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
R = S1.R
SERIES = lambda src: S1.SERIES.replace("the low sun, the string-light bulbs, a candle", src).replace("the yard layered in depth behind", "the room layered in depth behind")
FACE = ("is Susan's face and hair only: her face, age, hair colour and build exactly as shown; her clothes in this take come from the outfit card, "
        "never from anywhere else.")
OUT_D2 = ("is Susan's outfit on these weekday mornings, laid flat: the long grey marl knit cardigan with small grey buttons, the plain white crew-neck T-shirt, "
          "the grey jersey lounge trousers, and the tortoiseshell claw clip holding her hair up at the back — she wears exactly these.")
OUT_D3 = ("is Susan's outfit at the birthday, laid flat: the oatmeal chunky crew-neck knit sweater, the dark indigo straight jeans with a brown belt and the white "
          "leather trainers — she wears exactly these.")
SUSAN_D2 = "the long grey marl cardigan over a white T-shirt and grey lounge trousers, her hair pulled up in a tortoiseshell claw clip"
SUSAN_D3 = "the oatmeal knit sweater, dark jeans and white trainers, her hair loose"
SUSAN_ID_UP = S1.SUSAN_ID.replace(", worn loose", "")
NEG_PARTY = "no dusty-blue blouse, no cream linen trousers, no pearl earrings"
SILENT = "The clip carries no dialogue and no voice at all: nobody speaks; every mouth stays closed."
JOB = {"N-FACE": "67d1090e-3546-45d1-ae77-8a07bb5709fa", "OUT-D2": "148c1f9d-8cd8-4abf-856f-1e9c7c792481", "OUT-D3": "53c21ecc-d16b-4097-8f21-ebda7584b04e",
       "INVITE": "5d032de3-8fa8-4504-a1af-d27ac7c5a178", "OLDF": "5d3408e4-56ba-4147-8435-8b41efaa8cf9", "P-HOUSE": "71bf2c97-0a9a-49bf-9304-f92e1ad36677",
       "L-VANITY": "aeb31e74-e06d-4fdc-9c39-0893e78f59bd", "L-GATHERING": "14a6814f-273b-49b4-ba98-05ec8f338263", "C4": "c7ee4552-d66b-4208-879d-1161fb76fc2b"}
FILE = {"N-FACE": "body/SC04/ingredients/N-FACE.png", "OUT-D2": "body/SC04/ingredients/OUTFIT-N-D2_v1.png", "OUT-D3": "body/SC04/ingredients/OUTFIT-N-D3_v1.png",
        "INVITE": "body/SC04/ingredients/INVITE-CARD_v1.png", "OLDF": "body/SC04/ingredients/OLD-FOUNDATION-CARD_v1.png", "P-HOUSE": "plates/P-HOUSE_v1.png",
        "L-VANITY": "plates/L-VANITY_v1.png", "L-GATHERING": "plates/L-GATHERING_v1.png", "C4": "cast/C4-DAUGHTER_v1.png"}
T = {}

# T1 — the kitchen island, D2 (SH01): hands only
st, en = R["SC04-SH01"]["start_pos"], R["SC04-SH01"]["end_pos"]
T["SC04-T1"] = dict(kind="take", covers=["SC04-SH01"], duration=5, motion="in_place", refs=["N-FACE", "OUT-D2", "INVITE", "P-HOUSE"], start=st, end=en,
  title="Scene 4 · T1 — the invite turned over, the phone on top (SH01, kitchen, D2)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE), ("@image2", OUT_D2),
                 ("@image3", "is the kitchen island top from above: the speckled beige-and-brown granite, the one plain cream invite card with a thin gold border and nothing printed on it, "
                             "the black phone lying face down to its right, the white coffee mug, the three envelopes; every object exactly as shown and counted."),
                 ("@image4", "is this house: its greige walls, white casings and honey oak floor, the same era and upkeep in the kitchen.")]),
    SERIES("the grey window light"), S1.LOOK, S1.INHERIT,
    "THE SCENE SO FAR, a weekday morning months after the party: Susan alone in her own kitchen, cool flat overcast daylight, about 6500K, from the window on the right, "
    "the granite island in front of her. The only person here is Susan, and only her hand and the grey knit cuff of her cardigan sleeve are ever seen.",
    SILENT,
    "One continuous shot, never cut and never restarted, 5s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    "CLOSE-UP at three-quarter from the side of the island, a little above the counter, as if from someone standing beside it: the edge of the granite running across the lower frame, "
    "the invite card face up in the middle, the phone, mug and envelopes laid out exactly as @image3 shows. "
    "[0s-2s]: Susan's right forearm, the grey marl cuff of her cardigan at the wrist, comes in from frame left at counter height, the way a woman standing at the island reaches; "
    "her hand slowly picks up the invite by its edge and turns it over face down; her fingers rest flat on it for a beat. "
    "[2s-5s]: the same hand slides the black phone lying beside it across onto the turned-over card, face down, rests on it a moment, then draws back out of frame left. "
    "Last frame: " + en + ".",
    S1.F2, S1.PHYS,
    "Exactly one invite card and exactly one phone the whole time: nothing appears, doubles or changes shape; the card stays blank on both sides.",
    S1.state("SUSAN", "her hand slow and deliberate, the grey marl cuff at her wrist", "nothing"),
    "FOCUS: the card and her hand sharp; the far edge of the island soft. The blur is optical: soft and round, never smeared.",
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, "no writing, lettering or printing on the card, no second card, no second phone, no phone screen lit, no face in frame, no second hand",
            NEG_PARTY, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)]),
  risks=[{"risk": "lettering appears on the invite", "prevented_by": "@image3 blank card, 'nothing printed', negatives"},
         {"risk": "the hand or sleeve reads as someone else / the party blouse", "prevented_by": "N-FACE + the D2 outfit card, the grey cuff named, NEG_PARTY"},
         {"risk": "objects double or morph", "prevented_by": "counted objects, 'exactly one' clause, PHYS"},
         {"risk": "the arm comes up out of the lens (v1, top-down)", "prevented_by": "three-quarter side angle a little above the counter, forearm in from frame left at counter height"}],
  fix="CREAT NEW VERSION (user, chat, 2026-10-02 — no board note)",
  fix_note="no fault named by the user; seen on v1: the straight top-down view brought her arm up out of the lens with an oversized sleeve, reading as a staged product shot → three-quarter angle from the side of the island a little above the counter, her forearm in from frame left at counter height, slower beats with a held rest after the turn; card, phone, outfit and narration unchanged")

# T2 — the daughter's family room, D3 (SH02)
st, en = R["SC04-SH02"]["start_pos"], R["SC04-SH02"]["end_pos"]
T["SC04-T2"] = dict(kind="take", covers=["SC04-SH02"], duration=4, motion="in_place", refs=["N-FACE", "OUT-D3", "C4", "L-GATHERING"], start=st, end=en,
  title="Scene 4 · T2 — the birthday photo: she takes it, outside it (SH02, the daughter's house, D3)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE), ("@image2", OUT_D3),
                 ("@image3", "is Susan's daughter: face, age, hair and build, wearing exactly the outfit shown on this sheet (a cream ribbed knit cardigan over a white T-shirt and light-wash jeans) — today's outfit."),
                 ("@image4", "is the place: the young couple's family room — the grey fabric sectional under the big window, the low wooden coffee table with the plain white birthday cake, "
                             "the pastel balloons tied to the sofa arm, the bookshelf with plants on the left, the cream rug on the light wood floor; its layout and light side exactly as shown.")]),
    SERIES("the big window behind the sofa"), S1.LOOK, S1.INHERIT,
    "THE SCENE SO FAR, a family birthday on a Sunday afternoon: warm soft daylight, about 5600K, through the big window behind the sofa. On the grey sectional, around the coffee table "
    "and its cake: in the middle, Susan's daughter, a slim woman of twenty-six with long dark-blonde hair and a small mole below her mouth; on her left, her husband, a broad man of about "
    "thirty with short brown hair and a beard, in a navy polo shirt; on her right, their son, a boy of six with a round face and light brown hair, a paper party hat on his head, "
    "in a striped T-shirt. Three people on the sofa, counted, and only these. Susan stands alone on the clear stretch of floor between the coffee table and the camera, her back to us.",
    SILENT,
    "One continuous shot, never cut and never restarted, 4s, in one place with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    f"FULL SHOT from behind Susan at eye level: Susan, in {SUSAN_D3}, seen from behind, the phone in her hand, the family on the sofa beyond her. "
    "[0s-2s]: the daughter smiles and waves her in with one hand, beckoning her into the photo; Susan shakes her head once. "
    "[2s-4s]: Susan raises the phone in both hands, takes the picture of the three of them, and takes one small step back. "
    "Last frame: " + en + ". The family stays on the sofa throughout; nobody gets up.",
    S1.F2, S1.PHYS,
    "LISTENING: the daughter's smile drops a little when Susan shakes her head; nothing on her face arrives before the shake.",
    S1.state("SUSAN", SUSAN_D3 + ", standing apart", "the phone coming up and one step back"),
    "FOCUS: the family on the sofa sharp; Susan's back and shoulder a little soft in the foreground. The blur is optical: soft and round, never smeared.",
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, "no one speaking, no writing on the cake, no Susan's face toward the camera, no Susan joining the photo, no fourth person on the sofa, no phone screen facing the camera",
            NEG_PARTY, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)]),
  risks=[{"risk": "Susan in the party blouse", "prevented_by": "N-FACE + the D3 outfit card, NEG_PARTY"},
         {"risk": "the family members merge or multiply", "prevented_by": "each one-off her/his own clause with place (L55), 'three people, counted'"},
         {"risk": "Susan steps into the photo", "prevented_by": "action words, 'no Susan joining the photo'"}])

# T3 — the vanity, D2 (SH03–SH05)
st, en = R["SC04-SH03"]["start_pos"], R["SC04-SH05"]["end_pos"]
T["SC04-T3"] = dict(kind="multi", covers=["SC04-SH03", "SC04-SH04", "SC04-SH05"], duration=11, motion="in_place", refs=["N-FACE", "OUT-D2", "OLDF", "L-VANITY"], start=st, end=en,
  title="Scene 4 · T3 — the mirror: the old foundation caking (SH03–SH05, vanity, D2)",
  prompt=" ".join([
    S1.manifest([("@image1", FACE), ("@image2", OUT_D2),
                 ("@image3", "is the dressing table top from above: the one plain frosted-glass foundation bottle with a black cap and no label, the used beige teardrop sponge, "
                             "the jars, hairbrush, ceramic dish and wooden jewellery box at the back; every object exactly as shown and counted."),
                 ("@image4", "is the place: the main bedroom — the white dressing table with its large rectangular mirror under the window, the small upholstered stool, "
                             "the sheer white curtains, the end of the bed with the dusty-blue quilt on the left; its layout and light side exactly as shown.")]),
    SERIES("the cool window light through the sheer curtains"), S1.LOOK, S1.INHERIT,
    "THE SCENE SO FAR, a weekday morning months after the party: Susan alone in her bedroom, cool flat morning light, about 6500K, through the sheer curtains over the dressing table from "
    "the right. She sits on the stool facing the big mirror; the foundation bottle and sponge on the table in front of her exactly as @image3 shows. Her face is bare and tired, every line "
    "of it real: the creases beside her mouth, the lines at her eyes.",
    SILENT,
    "One scene covered in 3 shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: " + st + ". "
    "Each shot picks up the movement exactly where the last one left it: the sponge, her hand and her face carry straight across every cut. "
    f"SHOT 1, [0s-4s]: MEDIUM CLOSE-UP of Susan's reflection in the mirror, seen over her shoulder, Susan, {SUSAN_ID_UP}, in {SUSAN_D2}: she presses the sponge with beige foundation "
    "onto her cheek in three slow dabs, watching herself. "
    "SHOT 2, [4s-7s]: EXTREME CLOSE-UP, three-quarter, on the crease beside her mouth: the beige foundation sits grey and dry in the line, cracking and lifting at its edges as her "
    "mouth moves into a small, tired smile. "
    "SHOT 3, [7s-11s]: CLOSE-UP, three-quarter, on Susan herself: the sponge stops halfway to her face; she lowers it slowly to the table and just looks at her reflection, still. "
    "Each cut lands on a completed action. Nobody looks into the lens. Last frame: " + en + ".",
    S1.F2, S1.PHYS,
    "The mirror shows exactly what is in front of it: one Susan, one reflection, the same moves at the same moment, the room behind her reversed.",
    S1.state("SUSAN", "the grey cardigan, hair up in the claw clip, the old foundation on one cheek, tired", "the sponge lowered"),
    "FOCUS: SHOT 1 her reflection's eyes sharp; SHOT 2 the crease and the cracked foundation sharp, the rest of her face falling off soft; SHOT 3 her nearest eye sharp. The blur is optical: soft and round, never smeared.",
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, "no one speaking, no brand, label, logo or writing on the bottle, no second foundation bottle, no smooth flawless skin, no lines erased, "
            "no reflection moving on its own, no second Susan, no tears", NEG_PARTY, S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)]),
  risks=[{"risk": "the reflection breaks (a second Susan, out of sync)", "prevented_by": "mirror clause, 'no reflection moving on its own, no second Susan'"},
         {"risk": "the old foundation looks flattering (the villain must read)", "prevented_by": "SHOT 2 names grey, dry, cracking in the crease; 'no smooth flawless skin, no lines erased'"},
         {"risk": "a brand on the bottle", "prevented_by": "the OLD-FOUNDATION-CARD bottle, no-label negatives (§10)"}])

VO = {"SC04-T1": [(0.0, 4.45, 0.0)], "SC04-T2": [(4.45, 6.0, 0.0)], "SC04-T3": [(6.0, 8.6, 0.0), (8.6, 11.6, 4.0), (11.6, 14.37, 7.0)]}  # (from, to, at) seconds of VO-T1-L009

if __name__ == "__main__":
    for b, s in T.items():
        call = {"beat": b, "build": "facelove-my-mother", "connector": "seedance", "model": "seedance_2_5", "mode": 4, "kind": s["kind"], "prompt": s["prompt"],
                "take": b, "covers": s["covers"], "start_pos": s["start"], "end_pos": s["end"], "duration": s["duration"], "resolution": "720p", "aspect_ratio": "9:16",
                "start_image": None, "ingredients_approved": True, "files": [FILE[r] for r in s["refs"]], "audios": [], "generate_audio": False,
                "dialogue": None, "script_line": None, "pace": "unhurried", "subject_motion": s["motion"], "prefer_multi_shots": "false", "generation": 2 if s.get("fix") else 1, "fault": s.get("fix"), "fix_note": s.get("fix_note"),
                "user_go": ("chat: " + s["fix"]) if s.get("fix") else "chat: \"CONFIRMED ALL IMAGES. PROCEED\" (user, 2026-10-02) — Scene 4's cards confirmed on the board",
                "risks": s["risks"], "scene": 4, "title": s["title"], "taste": ["HT17", "HT18", "HT22", "HT23", "HT25", "HT26", "HT27"],
                "jobs": [JOB[r] for r in s["refs"]], "vo": {"take": "VO-T1-L009", "pieces": VO[b]}}
        (H / f"{b}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
        (H / f"{b}.prompt.txt").write_text(s["prompt"])
        print(b, s["duration"], "s", len(s["prompt"]), "chars")
