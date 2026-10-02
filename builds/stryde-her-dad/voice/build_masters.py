"""§24I part 7 — neutral voice masters for stryde-her-dad (Seedance 2.5 on Kie, 720p, 9:16), one per sheeted speaking character.
3–5 plain script sentences read back to back (~12–15 s, half-my-age lesson: shorter masters can't hold a voice); duration fitted to the words."""
import json, re, pathlib, sys
H = pathlib.Path(__file__).parent
sys.path.insert(0, str(H.resolve().parents[2] / ".claude/skills/ai-prompt-engineer/scripts"))
from preflight import master_fit
T = (H.resolve().parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
AUD, NEGS = S("AUD-FILM"), S("NEG-SOUND")
NEUTRAL = "Level, even and unhurried; conversational volume; no emotion coloured into the words; a person reading a sentence aloud to themselves."
LN = {r["id"]: r["line"] for r in json.load(open(H.parent / "work/lines.json"))}
CH = {  # id: (name, who, pronoun, wall, voice string, neutral lines)
 "C1": ("Tony", "a man of sixty-four", "He", "a plain pale grey wall",
        "An Englishman of sixty-four from the south-east of England, Kent, a builder all his life: a low, rough, chesty voice with gravel in it, plain working vowels, dropped t's, unhurried. He says little and says it flat; when he is hurt he goes quieter, not louder. Never theatrical, never sing-song; statements fall at the end.",
        ["L023", "L045", "L036", "L055"]),
 "C2": ("Sue", "a woman of fifty-two", "She", "a plain warm grey wall",
        "An Englishwoman of fifty-two from the south-east of England, Kent: a quick, clear, warm mid-range voice, light estuary vowels, crisp consonants; her anger is fear held down — clipped when frightened, soft when she lets go. Natural, never theatrical.",
        ["L054", "L044", "L007", "L004", "L046"]),
 "C3": ("Gary", "a man of seventy", "He", "a plain pale stone wall",
        "An Englishman of seventy from Essex: a dry, amused, certain voice, a little hoarse, a builder's directness, broad Essex vowels; he enjoys being right and isn't arguing. Unhurried, never theatrical.",
        ["L024", "L030", "L032"]),
 "C4": ("the lad", "a young man of nineteen", "He", "a plain light grey-green wall",
        "A young Londoner of nineteen from south London: a quick, light, friendly voice, London vowels, kind and easy, a little breathless when he has been running. Natural and unforced.",
        ["L002", "L003", "L056"]),
 "C5": ("the GP", "a woman of forty-eight", "She", "a plain pale blue-grey wall",
        "An Englishwoman of forty-eight, a family doctor of British Indian heritage from the Midlands: a calm, measured, warm and brisk voice, clear consonants, light Midlands vowels — a ten-minute appointment, kind but moving on.",
        ["L018", "L022"]),
}
out = {}
for k, (name, who, pr, wall, voice, ids) in CH.items():
    line = " ".join(LN[i] for i in ids)
    d = master_fit(line)
    cap = name[0].upper() + name[1:]
    p = (f"INGREDIENTS. @image1 is {name}: face, age, hair and build only. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to. "
         f"A plain medium close-up of {name}, {who}, standing against {wall}, soft daylight from the left, the camera on a locked tripod, nothing else in frame. "
         f"{cap} looks just off the lens at someone beside the camera and, starting straight away, says these sentences one after another, clearly and completely, with only an ordinary breath between them: \"{line}\" "
         f"{pr} keeps speaking from the first second to the last; no long silences. "
         f"Delivery: {voice} {NEUTRAL} {AUD} Dialogue only: {NEGS}. One speaker only. "
         "NEGATIVES: no other people, no second voice, no looking into the lens, no text, no captions, no long pauses, no silent beats, " + NEGS + ".")
    call = {"beat": f"VOICE-{k}", "connector": "seedance", "mode": 4, "kind": "voice_master", "prompt": p, "duration": d,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "start_approved": True, "ingredients_approved": True,
            "files": [f"voice/{k}_face.jpg"], "audios": [], "generate_audio": True, "dialogue": line, "script_line": line, "pace": "unhurried",
            "subject_motion": "still", "prefer_multi_shots": "false", "generation": 1, "user_go": None, "fix_note": None, "rack": None,
            "risks": [{"risk": "emotional colour in the master", "prevented_by": "the neutral delivery clause after VOICE-[CHAR]"},
                      {"risk": "music or a second voice", "prevented_by": "NEG-SOUND twice, one speaker only"},
                      {"risk": "silences that leave too little voice", "prevented_by": "duration fitted to the words, 'keeps speaking from the first second to the last'"}]}
    (H / f"VOICE-{k}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / f"VOICE-{k}.prompt.txt").write_text(p); out[k] = (len(p), d, len(line.split()))
print(json.dumps(out))
