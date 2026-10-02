"""§24I part 7 neutral film voice masters for facelove-my-mother (Seedance 2.5 on Higgsfield, omni_reference, 720p, 9:16).
Recurring speakers get ~12–15 s of continuous speech (3–4 plain script sentences, their own neutral lines first, then neutral
narration sentences); one-line speakers a shorter master (2026-09-30 amendment). Duration = master_fit (no paid dead space)."""
import json, re, pathlib, sys
H = pathlib.Path(__file__).parent
ROOT = H.resolve().parents[2]
sys.path.insert(0, str(ROOT / ".claude/skills/ai-prompt-engineer/scripts"))
from preflight import master_fit, words
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
AUD, NEGS = S("AUD-FILM"), S("NEG-SOUND")
NEUTRAL = "Level, even and unhurried; conversational volume; no emotion coloured into the words; a person reading a sentence aloud to themselves."
VOICE = {  # §22D strings (BUILD_SHEET §3)
 "N": "An American woman of forty-nine from the suburban Midwest, a low, warm, slightly smoky voice, plain General American vowels, unhurried. She says the worst things quietly and flatly, almost to herself, and lets a line sit; a dry, tired humour under it. Statements fall at the end; never breathy, never theatrical.",
 "C1": "An American man of fifty-two, a warm, easy baritone with a little gravel, relaxed General American vowels, sociable and sure of himself; when he talks quietly the warmth drops out and it goes flat. Statements fall at the end; never shouting, never theatrical.",
 "C2": "An American woman of forty-nine, East Coast Italian-American, a warm, low, slightly husky voice, quick and friendly, the vowels a little open. Statements fall at the end; never shrill, never theatrical.",
 "C3": "An American woman of forty-nine, a bright, easy, honest voice with a smile in it, clear General American vowels, unhurried and certain without selling anything. Statements fall at the end; never salesy, never theatrical.",
 "C5": "An American woman of fifty-one, a low, quick, warm voice, plain General American, a little hushed, speaking close to a friend.",
 "C6": "An American woman of fifty, a soft, gentle, light voice, careful and kind-sounding, plain General American, never sharp.",
}
WHO = {"N": ("Susan", "a woman of forty-nine", "she", "a plain pale grey wall"), "C1": ("Greg", "a man of fifty-two", "he", "a plain pale blue-grey wall"),
       "C2": ("Paula", "a woman of forty-nine", "she", "a plain warm cream wall"), "C3": ("Beth", "a woman of forty-nine", "she", "a plain soft sage wall"),
       "C5": ("Friend A", "a woman of fifty-one", "she", "a plain light beige wall"), "C6": ("Friend B", "a woman of fifty", "she", "a plain pale blue wall")}
# verbatim script sentences (work/lines.json) — neutral ones, never the crisis line (§24I part 7 step 2)
LINES = {
 "N":  "Saturday. The same yard I'd been hiding from for months. I almost turned the car around. So I made it true. I stopped going. Muted the group chat. Skipped the birthdays.",
 "C1": "Thirty years. Thirty. Paula's the same age as you. Exact same. Right now, buy two and they'll add their Dream Skin Primer free, with free shipping and a thirty day guarantee.",
 "C2": "Susan. Look at you. Saturday. The same yard I'd been hiding from for months.",
 "C3": "There's a thing Saturday. Whole group. You're coming. This was made for us. Goes on white, don't panic. No needles. No downtime. Thirty seconds.",
 "C5": "Muted the group chat. Skipped the birthdays.",
 "C6": "Saturday. The same yard I'd been hiding from for months.",
}
out = {}
for k, line in LINES.items():
    name, who, pr, wall = WHO[k]
    d = master_fit(line)
    p = (f"INGREDIENTS. @image1 is {name}: face, age and hair only. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to. "
         f"A plain medium close-up of {name}, {who}, standing against {wall}, soft daylight from the left, the camera on a locked tripod, nothing else in frame. "
         f"{name} looks just off the lens at someone beside the camera and, starting straight away, says these sentences one after another, clearly and completely, with only an ordinary breath between them: \"{line}\" "
         f"{pr.capitalize()} keeps speaking from the first second to the last; no long silences. "
         f"Delivery: {VOICE[k]} {NEUTRAL} {AUD} Dialogue only: {NEGS}. One speaker only. "
         f"NEGATIVES: no other people, no second voice, no looking into the lens, no text, no captions, no long pauses, no silent beats, {NEGS}.")
    call = {"beat": f"VOICE-{k}", "build": "facelove-my-mother", "connector": "seedance", "mode": 4, "kind": "voice_master", "prompt": p, "duration": d,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "start_approved": True, "ingredients_approved": True,
            "files": [f"voice/{k}_face.jpg"], "audios": [], "generate_audio": True, "dialogue": line, "script_line": line, "pace": "unhurried",
            "subject_motion": "still", "prefer_multi_shots": "false", "generation": 1, "user_go": None, "rack": None,
            "risks": [{"risk": "long silences — paid dead space", "prevented_by": "duration fitted to the words (master_fit), 'keeps speaking from the first second to the last', no-long-pauses negatives"},
                      {"risk": "emotional colour in the master", "prevented_by": "neutral, informational script sentences only; the neutral delivery clause after VOICE-[CHAR]"},
                      {"risk": "music or a second voice", "prevented_by": "NEG-SOUND twice, one speaker only, no other people"}]}
    (H / f"VOICE-{k}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / f"VOICE-{k}.prompt.txt").write_text(p); out[k] = (d, words(line), len(p))
print(out)
