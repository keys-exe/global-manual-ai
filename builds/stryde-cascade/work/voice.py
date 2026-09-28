"""§22U steps 1-2 for N (stryde-cascade): talking-head frame + Kling voice-source takes."""
import json, pathlib
from lib import s
P = pathlib.Path(__file__).resolve().parents[1] / "prompts"
VOICE_N_FULL = ("A man of sixty-one from Nottingham, a low gravelly chest voice, slow and deliberate with a short stop before the word that matters. "
 "Pitch low for his age, placed in the chest with a little nasal colour on the vowels; texture dry and gravelly, a rasp on held vowels from years of sawdust and building sites; "
 "tempo slow, about 150 words a minute, steady then a short stop before the key word; melody flat, every statement falling at the end; "
 "articulation: East Midlands vowels, short flat 'a', 'you' softened to 'yuh', final t's caught in the throat, h's kept; "
 "habit: a short dry breath out through the nose before a number, a small throat-clear before a hard line. "
 "Age wear: a slight crack on held vowels, breath running short at the end of a long sentence. "
 "Stress register: quieter and slower on the hard line, never louder, eyes steady.")
# Compressed once for the Kling ceiling (§37) and locked in this form.
VOICE_N = ("A man of sixty-one from Nottingham, a low gravelly chest voice, slow and deliberate with a short stop before the word that matters. "
 "East Midlands vowels, short flat 'a', final t's caught in the throat; statements land flat and fall at the end; a dry breath out through the nose before a number. "
 "Stress: quieter and slower on the hard line, never louder.")
AGE = "the deep creases from nose to mouth, deep crow's feet, three horizontal forehead creases and weathered ruddy cheeks"
STEP1 = "\n\n".join([
 s("CAM-LOCK"),
 s("FRAME-SCALE").replace("[SCALE]", "about three quarters") + " " + s("FRAME-PROPPED"),
 "THE SAME MAN exactly as in the attached reference sheet — close-cropped grey hair receding at the temples, grey two-day stubble, deep-set grey-blue eyes, a nose bent slightly at the bridge, a short pale scar through the outer end of his left eyebrow, stocky and broad-shouldered — unchanged in face, age and build. "
 "THE SAME WORKSHOP exactly as in the attached scene reference image — the pegboard of hand tools, the scarred workbench, the offcut handrail lengths standing in the corner, the tray of brass handrail brackets — seen from about a metre and a half in front of him at chest height. The phone taking this picture is never in the picture: nothing stands between him and the lens. "
 "He sits on the wooden stool in front of the workbench, forearms resting on his thighs, hands loosely together, turned square to the phone, eyes on the lens, mouth closed, about to speak. "
 "He wears the faded navy half-zip work fleece over the grey crew-neck T-shirt from the reference sheet.",
 s("SKIN-B1"),
 s("SKIN-B3").replace("[FOREHEAD-LINES]", "three deep horizontal creases").replace("[AGE-FEATURES]", AGE),
 s("SKIN-B4"), s("EYES-A"),
 s("HAIR-A").replace("[HAIR-SPEC]", "close-cropped grey hair, darker at the sides, receding at the temples, grey two-day stubble"),
 s("NECK-A"), s("TEETH-A"),
 "THE LIGHT: the small side window to camera-left at about forty-five degrees, low afternoon daylight across his face and the bench, the terminator running down his right cheek, the right side of the garage a stop under into warm brown shadow, the window edge blowing to white.",
 s("CAP-A"), s("CAP-FILE"),
 "AVOID: " + ", ".join([s("NEG-FRAME"), s("NEG-SKIN"), s("NEG-TEX"), s("NEG-FINISH"), s("NEG-M1"), "no phone in frame, no second phone, no phone stand, no tripod, no selfie stick, no ring light, no microphone, no logos, no text"]),
])
TAKES = [
 ("G1", "A bad knee is not a knee problem. It is a weight problem.", "problem", "weight", "telling it straight"),
 ("G2", "I fit stair rails for a living. I have been in about four hundred houses.", "houses", "four hundred", "a plain fact"),
 ("G3", "Here is the sequence, and it is almost always the same.", "same", "always", "quietly certain"),
]
def take(tid, line, closure, stress, intent):
    mouth = s("MOUTH-C").replace("[CLOSURE-WORD]", closure).replace("[MOUTH-CORNER]", "right")
    for cut in (" Small conversational amplitude matched to the voice, teeth mostly hidden.", " Cheeks and throat move with speech.", " Mouth fully closed between sentences."):
        mouth = mouth.replace(cut, "")
    d = {"shot": f"Voice take {tid}.", "dialogue": line,
     "delivery": VOICE_N + f" To one person, {intent}; stress on '{stress}'. " + s("AUD-A") + " Garage workshop, phone a metre away.",
     "subject": "As in the start frame.",
     "camera": {"movement": s("RIG-R3C"), "framing": "PROPPED as in the start frame, hands in the lower frame."},
     "motion": s("BREATH-A") + f" Right hand lifts on '{stress}', settles; eyes on lens. " + mouth + " " + s("HOLD-C"),
     "lighting": s("INHERIT-CAP"), "style": "As in the start frame.",
     "negatives": ", ".join([s("NEG-WARP-C"), s("NEG-CAM-TH"), "no music, no second voice"])}
    return json.dumps(d, ensure_ascii=False, separators=(",", ":"))
if __name__ == "__main__":
    (P / "N_TH_frame.prompt.txt").write_text(STEP1); print("step1", len(STEP1))
    out = {}
    for t in TAKES:
        j = take(*t); out[t[0]] = j; (P / f"N_{t[0]}.kling.json").write_text(j); print(t[0], len(j), len(t[1].split()))
    json.dump({"VOICE_N": VOICE_N, "VOICE_N_FULL": VOICE_N_FULL, "takes": out}, open(P / "voice.json", "w"), indent=1, ensure_ascii=False)
