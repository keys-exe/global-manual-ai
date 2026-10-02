"""Shared strings and the take assembler for stryde-the-impression's Seedance takes (§24K part 5, §24N, V7.68.0 — ingredients, never frames).
Every string is Appendix A by ID where one exists; fills are the build's own (act map, wardrobe map, Look Sheet)."""
import json, re, pathlib, sys
H = pathlib.Path(__file__).parent; B = H.parent
T = (B.parents[1] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
S = lambda i: re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S).group(1).strip()
sys.path.insert(0, str(B.parents[1] / ".claude/skills/ai-prompt-engineer/scripts"))
from preflight import master_fit, words  # noqa
ROWS = {r["beat"]: r for r in json.load(open(B / "step5/act_map.json"))["rows"]}
LN = {r["id"]: r["text"] for r in json.load(open(B / "work/lines.json"))["lines"]}

SERIES = S("SERIES-LOOK")
LOOK = (B / "cast/LOOK.txt").read_text().strip().replace("shot like a prestige streaming series", "shot like a prestige drama series")
INHERIT = S("INHERIT-FILM").replace("The look exactly as in the start frame:", "The look exactly as set out here, from the first frame to the last:")
PHYS = S("PHYS-FRAME-C")
AUD = S("AUD-FILM")
NEG_FILM, NEG_DRAMA, NEG_SOUND = S("NEG-FILM"), S("NEG-DRAMA"), S("NEG-SOUND")
NEG_SCENECUT = ("no light direction changing within the scene, no colour changing between shots, no graded look, no wardrobe changing within the scene, no prop moving between shots unless shown moving, "
                "no character changing position between shots, no camera crossing the action line, no eyeline pointing the wrong way, no time of day changing within the scene, no different room, "
                "no extra people, no missing people, no tears, redness or sweat appearing or vanishing between shots, no hair or clothing state resetting between shots, no prop jumping to the other hand")
NEG_EQUIP = "no microphone in frame, no boom pole, no film equipment, no crew in frame"
NEG_MORPH = "no morphing, no warping, no melting, no merging, no splitting, no duplicate people, no background bending, no texture swimming, no flickering geometry"
F2 = ("Camera on a tripod, framed and locked for each shot, with no drift, no sway and no reframe. The only camera life is one small operator pan or tilt of a few degrees to keep the subject in frame as they shift. "
      "It arrives a beat late and corrects only part of the way. The people and the room carry all the other movement.")
F1 = lambda cm: (f"On the last shot the camera is on a dolly, already moving: a slow, steady push toward the face covering about {cm} centimetres, perfectly level, with no bounce and no sway; "
                 "the subject stays in place and never walks while the camera moves.")
ONLY_SPEAKER = "Only the person whose line it is speaks; everyone else keeps their mouth closed and listens."

SHEET = lambda name, out: f"is {name}: face, age, hair and build only, wearing {out}."
VOICE = lambda name: f"is {name}'s voice, its timbre, pitch, accent and pace, for every line {name} speaks; it sets who they sound like, never how they feel in this shot."
PLACE = lambda desc: f"is the place: {desc}, its walls, windows, furniture and light side exactly as shown."

def manifest(items):
    return ("INGREDIENTS. " + " ".join(f"{t} {c}" for t, c in items) +
            " These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")

def state(name, what, change="nothing"):
    return S("STATE-CARRY").replace("[NAME]", name).replace("[STATE: eyes, face, hair, wardrobe state, what each hand holds, where they are]", what).replace(
        "[WHAT HAS VISIBLY CHANGED, and its cause, or nothing]", change)

def delivery(voice, moment, to, between, playing, entry, turn, change, exitst, stress, now, under, tell):
    return (f"{voice} IN THIS MOMENT: {moment}. Speaking to {to}, {between}. PLAYING: {playing} {to}. Opens {entry}; turns on the exact word '{turn}', where {change}; "
            f"exits {exitst}. Stress on '{stress}'. VOICE NOW: {now}, continuing from how they sounded on the previous line, and matching the face in this shot. "
            f"UNDER THE LINE: {under}, which leaks only through {tell}. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens.")

def listen(name, speaker, what):
    return (f"{name} is listening, not waiting to speak. As {speaker} talks, {name} takes it in: {what}. The reaction arrives a beat after the words that cause it, never before them. "
            f"Mouth closed, face alive and never frozen, eyes on {speaker}.")

def business(name, when, what, pace):
    return f"While {when}, {name} keeps doing one thing with their hands: {what}, at {pace}. It is ordinary and unhurried, and the hands never stop to gesture."

def negs(*extra):
    return "NEGATIVES: " + ", ".join(x for x in extra if x) + "."

def multi(n, start, move, shots, rhythm, end):
    head = f"One scene covered in {n} shots within a single take, all on the same side of the action line, with the same light, look and wardrobe throughout. Frame 1: {start}. "
    mv = ("MOVE: The action carries straight across every cut: each shot picks up the movement exactly where the last one left it — the same step, the same hand, the same direction — and everyone is where the last shot left them. "
          if move else "STILL: Everyone stays in place, seated or standing; the only movement in each shot is its business and the performance. ")
    body = " ".join(f"SHOT {i+1}, [{a}s-{b}s]: {t}" for i, (a, b, t) in enumerate(shots))
    return (head + mv + body + f" The lines land on each other in the rhythm this scene needs: {rhythm}. Each cut lands on a completed line, action or reaction. "
            f"The eyelines match across every reverse. Nobody looks into the lens. Last frame: {end}.")

def call(beat, scene, covers, dur, title, files, audios, prompt, start, end, dialogue, risks, motion, taste, go, fix=None, gen=1, ingredients=()):
    return {"beat": beat, "build": "stryde-the-impression", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4,
            "kind": "multi" if len(covers) > 1 else ("take" if motion != "still" else "multi"), "take": beat, "covers": covers,
            "start_pos": start, "end_pos": end, "duration": dur, "resolution": "720p", "aspect_ratio": "9:16", "start_image": None,
            "ingredients_approved": True, "files": files, "audios": audios, "generate_audio": bool(dialogue), "dialogue": dialogue or None,
            "script_line": dialogue or None, "pace": "unhurried", "subject_motion": motion, "prefer_multi_shots": "false", "generation": gen,
            "user_go": go, "fix_note": fix, "rack": None, "risks": risks, "scene": scene, "title": title, "taste": taste, "prompt": prompt,
            "ingredients": list(ingredients)}
