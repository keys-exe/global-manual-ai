#!/usr/bin/env python3
"""§24I part 7 neutral film voice masters for facelove-walmart — Mode 5 (AUD-ANIM: studio voice performance for animation),
Seedance 2.5 on Higgsfield (omni_reference, 720p, 9:16), one face-only crop of the confirmed sheet as the only ingredient.
Recurring speakers get ~12–15 s of continuous speech (their own neutral script sentences, then neutral narration sentences);
the one-scene speaker (the woman, 41) a shorter master. Duration = master_fit (no paid dead space)."""
import json, re, pathlib, sys
H = pathlib.Path(__file__).parent
ROOT = H.resolve().parents[2]
sys.path.insert(0, str(ROOT / ".claude/skills/ai-prompt-engineer/scripts"))
from preflight import master_fit, words
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
AUD, NEGS = S("AUD-ANIM"), S("NEG-SOUND")
NEUTRAL = "Level, even and unhurried; conversational volume; no emotion coloured into the words; a person reading a sentence aloud to themselves."
VOICE = {  # §22D (BUILD_SHEET §3)
 "N": "An American woman of sixty-three, Latina, raised in the American Southwest — a warm, low, slightly husky voice with plain General American vowels and the faintest Spanish softness on her r's, unhurried and composed. Statements fall at the end; never breathy, never theatrical.",
 "C1": "An American man of sixty-five, a confident baritone with a salesman's ease, relaxed General American vowels, a little gravel. Statements fall at the end; never shouting, never theatrical.",
 "C2": "An American woman of forty-one, a bright, clipped, quick voice, crisp General American vowels, a little guarded. Statements fall at the end; never shrill, never theatrical.",
 "C3": "A Latina American woman of sixty-seven, a warm, husky voice with a laugh close under it and a light Spanish lilt on the vowels, unhurried and certain. Statements fall at the end; never salesy, never theatrical.",
}
WHO = {"N": ("Michelle", "a woman of sixty-three", "she", "a plain pale warm grey wall"), "C1": ("Peter", "a man of sixty-five", "he", "a plain pale blue-grey wall"),
       "C2": ("The woman", "a woman of forty-one", "she", "a plain soft white wall"), "C3": ("Rosa", "a woman of sixty-seven", "she", "a plain warm terracotta-beige wall")}
LINES = {  # verbatim script sentences (work/lines.json) — neutral ones, never the crisis line (§24I part 7 step 2)
 "N":  "I ordered my own before Rosa even left. Two weeks later, Peter texted me. First time in four years. It is called FACELOVE, and I have linked it below.",
 "C1": "I am sorry, Michelle. After thirty one years. Right now you get two Foundation Sticks for almost the price of one.",
 "C2": "Wait. That is your ex-wife? I am sorry, I just have to ask.",
 "C3": "Michelle, open the door. I brought wine and I am not leaving. This is the one that changed it for me. It has jojoba, shea, vitamin E.",
}
FACE = json.load(open(H / "face_media.json"))
out = {}
for k, line in LINES.items():
    name, who, pr, wall = WHO[k]
    d = master_fit(line)
    p = (f"INGREDIENTS. @image1 is {name}: face, age and hair only. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to. "
         f"A single frame from a finished 3D animated feature film: a plain medium close-up of {name}, {who}, standing against {wall}, soft daylight from the left, the camera locked, nothing else in frame. "
         f"{name} looks just off the lens at someone beside the camera and, starting straight away, says these sentences one after another, clearly and completely, with only an ordinary breath between them: \"{line}\" "
         f"{pr.capitalize()} keeps speaking from the first second to the last; no long silences; the mouth moves with every word. "
         f"Delivery: {VOICE[k]} {NEUTRAL} {AUD} Dialogue only: {NEGS}. One speaker only. "
         f"NEGATIVES: no other people, no second voice, no looking into the lens, no text, no captions, no long pauses, no silent beats, {NEGS}.")
    call = {"beat": f"VOICE-{k}", "build": "facelove-walmart", "connector": "seedance", "model": "seedance_2_5", "mode": 5, "kind": "voice_master", "prompt": p, "duration": d,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "start_approved": True, "ingredients_approved": True,
            "files": [f"voice/{k}_face.jpg"], "media": [FACE[k]], "audios": [], "generate_audio": True, "dialogue": line, "script_line": line, "pace": "unhurried",
            "subject_motion": "still", "prefer_multi_shots": "false", "generation": 1, "user_go": None, "rack": None,
            "risks": [{"risk": "long silences — paid dead space", "prevented_by": "duration fitted to the words (master_fit), 'keeps speaking from the first second to the last', no-long-pauses negatives"},
                      {"risk": "emotional colour in the master", "prevented_by": "neutral, informational script sentences only; the neutral delivery clause after VOICE-[CHAR]"},
                      {"risk": "music or a second voice", "prevented_by": "NEG-SOUND twice, one speaker only, no other people"}]}
    (H / f"VOICE-{k}.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / f"VOICE-{k}.prompt.txt").write_text(p); out[k] = (d, words(line), len(p))
print(out)
