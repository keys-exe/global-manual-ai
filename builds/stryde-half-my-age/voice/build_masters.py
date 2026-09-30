"""§24I part 7 — neutral voice masters (Seedance 2.5 on Kie, 10s, 720p, 9:16), one per sheeted speaking character."""
import json, re, pathlib
H = pathlib.Path(__file__).parent
T = (H.resolve().parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
AUD = S("AUD-FILM") + " The microphone and all equipment stay outside the picture."
NEGS = S("NEG-SOUND")
NEUTRAL = "Level, even and unhurried; conversational volume; no emotion coloured into the words; a person reading a sentence aloud to themselves."
LINES = json.load(open(H.parent / "work/lines.json"))["lines"]
LN = {r["n"]: r["text"] for r in LINES}
CH = {
 "N": ("Her", "a woman of seventy-one", 35, "the living room of her own house, a plain magnolia wall", "VOICE-HER",
       "An English woman of seventy-one from the north of England, Lancashire, a light, dry, slightly reedy voice with a little gravel at the bottom of her range. Plain northern vowels, flat \"a\", unhurried and understated — she says the big things quietly and lets a line land without pushing it. A dry humour just under the surface. Statements fall at the end; never sing-song, never theatrical."),
 "C1": ("Barbara", "a woman of seventy-four", 49, "a plain warm magnolia wall", "VOICE-BARBARA",
       "An English woman of seventy-four from the Midlands, a bright, certain, slightly husky voice with Midlands warmth in the vowels. Quick and practical, amused underneath — she has seen it work and isn't arguing. Clear consonants, ends of sentences land firmly."),
 "C2": ("the daughter", "a woman of forty-six", 1, "a plain pale grey wall", "VOICE-DAUGHTER",
       "An English woman of forty-six from the north of England, a quick, warm mid-range voice with the same flat northern vowels as her mother, a little brisker and higher. Concern tucked under teasing; words tumble slightly faster than her mother's."),
 "C3": ("the husband", "a man of seventy-four", 58, "a plain pale blue wall", "VOICE-HUSBAND",
       "An English man of seventy-four from the north of England, a gruff, soft, low voice with a slight roughness, few words, plain northern vowels. He says kind things a little too quickly and lets them drop."),
 "C4": ("the sister", "a woman of sixty-eight", 27, "a plain cream wall", "VOICE-SISTER",
       "An English woman of sixty-eight from the north of England, a soft, careful, slightly breathy mid-range voice, northern vowels, a gentle rise of hesitation, used to suggesting the easier plan."),
 "C5": ("Friend 1", "a woman of sixty-nine", 62, "a plain warm white wall", "VOICE-FRIEND1",
       "An Irish woman of sixty-nine who has lived in England for forty years, a crisp, dry, lightly Irish voice, quick and direct with a teasing edge; clear consonants, a lilt that rises then drops."),
 "C6": ("Friend 2", "a woman of seventy-two", 64, "a plain light grey-green wall", "VOICE-FRIEND2",
       "A Black British woman of seventy-two from London with a light Jamaican lilt, a warm, round, unhurried low voice, curious and kind, vowels open and warm."),
}
out = {}
for k, (name, who, n, wall, vid, voice) in CH.items():
    line = LN[n]
    p = (f"INGREDIENTS. @image1 is {name}: face, age, hair and build only. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to. "
         f"A plain medium close-up of {name}, {who}, standing against {wall}, soft daylight from the left, the camera on a locked tripod, nothing else in frame. "
         f"{name[0].upper() + name[1:]} looks just off the lens at someone beside the camera and says, clearly and completely: \"{line}\" "
         f"Delivery: {voice} {NEUTRAL} {AUD} Dialogue only: {NEGS}. One speaker only. "
         "NEGATIVES: no other people, no second voice, no microphone in frame, no looking into the lens, no text, no captions, " + NEGS + ".")
    call = {"beat": f"VOICE-{k}", "connector": "seedance", "mode": 4, "kind": "voice_master", "prompt": p, "duration": max(4, min(10, round(len(line.split()) / 2.5 + 1.5))),
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "start_approved": True, "ingredients_approved": True, "files": [f"voice/{k}_face.jpg"], "audios": [],
            "generate_audio": True, "dialogue": line, "script_line": line, "pace": "unhurried", "subject_motion": "still", "prefer_multi_shots": "false",
            "generation": 1, "user_go": None, "fix_note": None, "rack": None,
            "risks": [{"risk": "emotional colour in the master", "prevented_by": "the neutral delivery clause after VOICE-[CHAR]"},
                      {"risk": "music or effects under the voice", "prevented_by": "NEG-SOUND twice, dialogue only"},
                      {"risk": "microphone or a second person in frame", "prevented_by": "equipment outside the picture, one speaker, negatives"}]}
    (H / f"VOICE-{k}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / f"VOICE-{k}.prompt.txt").write_text(p); out[k] = (len(p), line)
print(json.dumps(out, indent=1, ensure_ascii=False))
