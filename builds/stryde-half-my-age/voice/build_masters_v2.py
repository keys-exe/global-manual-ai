"""§24I voice masters v2 for the main four (user 2026-09-30: "I don't think we can make consistent voices with this short seconds voices").
All speech, ~12–15s: 3–4 plain script sentences read one after another; duration fitted to the words (master_fit, no dead space)."""
import json, pathlib, sys
H = pathlib.Path(__file__).parent
sys.path.insert(0, str(H.resolve().parents[2] / ".claude/skills/ai-prompt-engineer/scripts"))
from preflight import master_fit, words
import build_masters as B   # reuses CH (voice strings), AUD, NEGS, NEUTRAL, LN
LN = B.LN
PICK = {  # own neutral lines first, then neutral narration sentences to fill (a voice reference: the words carry who, not the story)
 "N":  [35, 54],
 "C1": [49, 38, 36],
 "C2": [1, 5, 60],
 "C3": [58, 25, 18, 20, 32, 33],
}
out = {}
for k, ns in PICK.items():
    name, who, _, wall, vid, voice = B.CH[k]
    line = " ".join(LN[n] for n in ns)
    d = master_fit(line)
    p = (f"INGREDIENTS. @image1 is {name}: face, age, hair and build only. These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to. "
         f"A plain medium close-up of {name}, {who}, standing against {wall}, soft daylight from the left, the camera on a locked tripod, nothing else in frame. "
         f"{name[0].upper() + name[1:]} looks just off the lens at someone beside the camera and, starting straight away, says these sentences one after another, clearly and completely, with only an ordinary breath between them: \"{line}\" She keeps speaking from the first second to the last; no long silences." .replace("She keeps", "He keeps" if k == "C3" else "She keeps")
         + f" Delivery: {voice} {B.NEUTRAL} {B.AUD} Dialogue only: {B.NEGS}. One speaker only. "
         "NEGATIVES: no other people, no second voice, no microphone in frame, no looking into the lens, no text, no captions, no long pauses, no silent beats, " + B.NEGS + ".")
    call = {"beat": f"VOICE-{k}", "connector": "seedance", "mode": 4, "kind": "voice_master", "prompt": p, "duration": d,
            "resolution": "720p", "aspect_ratio": "9:16", "start_image": None, "start_approved": True, "ingredients_approved": True,
            "files": [f"voice/{k}_face.jpg"], "audios": [], "generate_audio": True, "dialogue": line, "script_line": line, "pace": "unhurried",
            "subject_motion": "still", "prefer_multi_shots": "false", "generation": 2,
            "fix_note": "masters too short to hold a voice (2–8s of speech after the idle cut; user) → 3–5 script sentences read back to back, ~12–15s, duration fitted to the words",
            "user_go": None, "rack": None,
            "risks": [{"risk": "long silences again", "prevented_by": "duration fitted to the words, 'keeps speaking from the first second to the last', no-long-pauses negatives"},
                      {"risk": "emotional colour in the master", "prevented_by": "the neutral delivery clause after VOICE-[CHAR]"},
                      {"risk": "music or a second voice", "prevented_by": "NEG-SOUND twice, one speaker only"}]}
    (H / f"VOICE-{k}.v2.call.json").write_text(json.dumps(call, indent=1, ensure_ascii=False))
    (H / f"VOICE-{k}.v2.prompt.txt").write_text(p); out[k] = (d, words(line), line)
print(json.dumps(out, indent=1, ensure_ascii=False))
