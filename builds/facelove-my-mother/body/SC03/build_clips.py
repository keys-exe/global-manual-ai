"""Scene 3 — THE DOOR (day D1, the hosts' dark back hall, straight after the walk-out). One Seedance 2.5 one-take via Higgsfield
(omni_reference, 720p, 9:16), ingredients only, no frames (§4, §24K part 5). User go: "CONFIRMED ALL VIDEO. PROCEED" (2026-10-02).
SH01 (F2, a little above) and SH02 (F1 push-in) are one place, one moment and 15 s together, so they are one take (L51) on one rig: a single
slow F1 push from a medium a little above her to a close-up as her eyes open. Silent clip: L008 is narration (VO-T1-L008), laid over in the edit;
generate_audio false (§24M). Shared look strings come from body/SC01/build_clips.py."""
import importlib.util, json
from pathlib import Path
H = Path(__file__).parent; B = H.parents[1]
_s = importlib.util.spec_from_file_location("sc01", B / "body/SC01/build_clips.py"); S1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(S1)
R = S1.R
START = R["SC03-SH01"]["start_pos"]
END = R["SC03-SH02"]["end_pos"]
PORCH = ("is the place: the dim back hall just inside the hosts' house, looking at the closed white back door from inside — its upper half one glass pane with the party's "
         "warm bulb glow soft beyond it and the deck railing just outside, a coat hook rail with two jackets and a small bench with garden shoes on the left wall, greige walls, "
         "an oak floor in deep shadow, a light switch beside the door; its layout and light side exactly as shown.")
YARD_GLOW = "is the yard outside that door: the warm bulb swags over the long table, seen only as the soft out-of-focus glow through the door's glass."
GEO3 = ("THE SCENE SO FAR, seconds after she walked out of the party: Susan has come in through the back door and shut it behind her. The hall is dark; the only light is "
        "the party's warm bulb glow, about 4300K, coming through the glass pane behind her head, rimming her hair and one cheek, the near side of her face in soft shadow. "
        "Behind the glass the party goes on, soft and far away. She is alone.")
PROMPT = " ".join([
    S1.manifest([("@image1", S1.SHEET("Susan", S1.SUSAN_D1)), ("@image2", PORCH), ("@image3", YARD_GLOW)]),
    S1.SERIES, S1.LOOK, S1.INHERIT, GEO3,
    "The clip carries no dialogue and no voice at all: nobody speaks; every mouth stays closed.",
    "One continuous shot, never cut and never restarted, 15s, in one place with the same light, look and wardrobe throughout. Frame 1: " + START + ". "
    f"Susan, {S1.SUSAN_ID}, in {S1.SUSAN_D1}, stands with her back against the shut door, small in the frame at first, the party glow through the glass behind her head. "
    "[0s-7s]: from a MEDIUM a little above her eye line, she stands against the door with her eyes closed and lets out one slow breath; her shoulders drop. "
    "[7s-15s]: as the camera arrives at a CLOSE-UP, three-quarter, she opens her eyes and looks at nothing across the dark hall; her jaw sets. "
    "Last frame: " + END + ". "
    "The movement is continuous from the first frame to the last: she stays against the door the whole time, never steps away, and the hall stays the same hall.",
    S1.F1(60), S1.PHYS,
    S1.state("SUSAN", "the dusty-blue blouse, composed, her face very still after the toast and the whisper", "her eyes closing and opening"),
    "FOCUS: Susan's nearest eye sharp throughout; the bulb glow through the glass soft and round behind her. The blur is optical: soft and round, never smeared.",
    S1.negs(S1.NEG_EQUIP, S1.NEG_MORPH, "no one speaking, no Susan crying, no tears, no hall light switched on, no other person in the hall, no Susan stepping away from the door",
            S1.NEG_FILM, S1.NEG_SCENECUT, S1.NEG_DRAMA, S1.NEG_SOUND)])

FILES = ["cast/N-SUSAN_v1.png", "plates/L-PORCH-IN_v1.png", "plates/L-YARD_v1.png"]
JOBS = [S1.JOBS["N"], "7eb05ec3-8c3d-4a90-ad42-7a7cc60ca4e2", S1.JOBS["L-YARD"]]

if __name__ == "__main__":
    call = {"beat": "SC03-T1", "build": "facelove-my-mother", "connector": "seedance", "model": "seedance_2_5", "mode": 4, "kind": "take", "prompt": PROMPT,
            "take": "SC03-T1", "covers": ["SC03-SH01", "SC03-SH02"], "start_pos": START, "end_pos": END, "duration": 15,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "ingredients_approved": True, "files": FILES, "audios": [],
            "generate_audio": False, "dialogue": None, "script_line": None, "pace": "unhurried", "subject_motion": "still", "prefer_multi_shots": "false",
            "generation": 1, "user_go": "chat: \"CONFIRMED ALL VIDEO. PROCEED\" (user, 2026-10-02) — SC01-T1..T4 confirmed on the board",
            "risks": [{"risk": "she speaks or mouths the narration", "prevented_by": "silent clip (generate_audio false), 'nobody speaks', 'no one speaking'"},
                      {"risk": "the hall gets lit or changes", "prevented_by": "the porch plate as Image2, the only light the glow through the glass, 'no hall light switched on'"},
                      {"risk": "the push drifts or she steps away", "prevented_by": "F1 level 60 cm, subject still against the door, 'no Susan stepping away from the door'"}],
            "scene": 3, "title": "Scene 3 · T1 — the door: alone in the dark hall (SH01–SH02, under VO L008)",
            "taste": ["HT17", "HT18", "HT22", "HT23", "HT25"], "jobs": JOBS}
    (H / "SC03-T1.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / "SC03-T1.prompt.txt").write_text(PROMPT)
    print("SC03-T1", len(PROMPT), "chars")
