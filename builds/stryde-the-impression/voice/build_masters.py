"""§24I part 7 — neutral voice masters for stryde-the-impression (Seedance 2.5 on Kie, 720p, 9:16), one per speaking character.
Built at the length the last drama settled on (stryde-half-my-age, user 2026-09-30: short masters don't hold a voice): 3–4 plain script
sentences read one after another, ~8–10 s of speech (Kie caps a call's reference audio at 30 s in total, and SC01 takes carry three speakers), duration fitted to the words (master_fit). Face crop of the confirmed sheet only."""
import json, re, pathlib, sys
H = pathlib.Path(__file__).parent
sys.path.insert(0, str(H.resolve().parents[2] / ".claude/skills/ai-prompt-engineer/scripts"))
from preflight import master_fit, words
T = (H.resolve().parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
AUD, NEGS = S("AUD-FILM"), S("NEG-SOUND")
NEUTRAL = "Level, even and unhurried; conversational volume; no emotion coloured into the words; a person reading a sentence aloud to themselves."
LN = {r["id"]: r["text"] for r in json.load(open(H.parent / "work/lines.json"))["lines"]}
CH = {  # id: (name, who, pronoun, wall, lines, VOICE-[CHAR])
 "N": ("Hazel", "a woman of sixty-seven", "She", "a plain pale duck-egg blue wall", ["L023", "L035"],
       "An English woman of sixty-seven from West Yorkshire, Halifax: a warm, plain, mid-low voice with a little huskiness, flat northern vowels and a short \"u\", unhurried. She says the hard things quietly and evenly and lets a line sit; dry rather than sad, never self-pitying. Statements fall at the end; questions only lift a little. Never theatrical, never sing-song."),
 "C1": ("Roy", "a man of seventy", "He", "a plain warm magnolia wall", ["L040", "L092"],
       "An English man of seventy from West Yorkshire: a soft, slightly gruff mid-low voice, plain northern vowels, practical and kind; he says kind things a little too quickly and fills a silence with a plan. Statements fall at the end."),
 "C2": ("Emma", "a woman of thirty-nine", "She", "a plain pale grey wall", ["L008", "L032", "L030"],
       "An English woman of thirty-nine, Yorkshire softened by years in Leeds: a quick, bright mid-range voice with her mother's northern vowels, a little faster and higher, brightness covering worry."),
 "C3": ("Dan", "a man of forty-one", "He", "a plain pale sage-green wall", ["L006", "L092", "L040"],
       "A British Indian man of forty-one, born and raised in Leeds: an easy, warm, mid-low Leeds voice, unhurried, careful and honest when he has to be; plain Yorkshire vowels."),
 "C4": ("Oscar", "a boy of four", "He", "a plain pale yellow wall", ["L007", "L110", "L112"],
       "A boy of four from West Yorkshire: a small, clear child's voice, matter-of-fact, the words a little slow and careful the way a four-year-old says them, Yorkshire vowels."),
 "C5": ("Wendy", "a woman of seventy-four", "She", "a plain cream wall", ["L052", "L062", "L050"],
       "A Black British woman of seventy-four from Leeds with a light Barbadian lilt from home: a full, warm, certain voice, amused, a laugh just under the words; Leeds vowels with a Bajan rise and fall."),
 "X1": ("the assistant", "a young woman of twenty-five", "She", "a plain clinical white wall", ["L022", "L024", "L028"],
       "A British Bangladeshi woman of twenty-five from Bradford: a bright, polite, light shop voice, quick and helpful, Bradford vowels."),
 "X2": ("the mum", "a woman of thirty-two", "She", "a plain warm white wall", ["L038", "L078", "L080", "L082"],
       "An English woman of thirty-two from West Yorkshire: a friendly, direct, mid-range voice, a little breathless from the hill, plain Yorkshire vowels."),
 "X3": ("the lollipop lady", "a woman of sixty-three", "She", "a plain pale blue wall", ["L046", "L048"],
       "An English woman of sixty-three, broad West Yorkshire: a chatty, warm, slightly raspy voice, conspiratorial, broad flat vowels."),
}
out = {}
for k, (name, who, pr, wall, ids, voice) in CH.items():
    line = " ".join(LN[i] for i in ids)
    d = master_fit(line)
    nm = name[0].upper() + name[1:]
    p = (f"INGREDIENTS. @image1 is {name}: face, age, hair and build only. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to. "
         f"A plain medium close-up of {name}, {who}, standing against {wall}, soft daylight from the left, the camera on a locked tripod, nothing else in frame. "
         f"{nm} looks just off the lens at someone beside the camera and, starting straight away, says these sentences one after another, clearly and completely, with only an ordinary breath between them: \"{line}\" {pr} keeps speaking from the first second to the last; no long silences. "
         f"Delivery: {voice} {NEUTRAL} {AUD} Dialogue only: {NEGS}. One speaker only. "
         "NEGATIVES: no other people, no second voice, no looking into the lens, no text, no captions, no long pauses, no silent beats, " + NEGS + ".")
    call = {"beat": f"VOICE-{k}", "connector": "seedance", "mode": 4, "kind": "voice_master", "prompt": p, "duration": d,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "start_approved": True, "ingredients_approved": True,
            "files": [f"voice/{k}_face.jpg"], "audios": [], "generate_audio": True, "dialogue": line, "script_line": line, "pace": "unhurried",
            "subject_motion": "still", "prefer_multi_shots": "false", "generation": 1, "fix_note": None, "user_go": None, "rack": None,
            "risks": [{"risk": "long silences (a short master that doesn't hold a voice)", "prevented_by": "3–4 sentences, duration fitted to the words, 'keeps speaking from the first second to the last'"},
                      {"risk": "emotional colour in the master", "prevented_by": "the neutral delivery clause after VOICE-[CHAR]"},
                      {"risk": "music or a second voice", "prevented_by": "NEG-SOUND twice, one speaker only"}]}
    (H / f"VOICE-{k}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / f"VOICE-{k}.prompt.txt").write_text(p); out[k] = (d, words(line), len(p))
print(json.dumps(out))
