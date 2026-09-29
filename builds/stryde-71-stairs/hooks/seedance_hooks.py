"""Seedance 2.5 hooks (user 2026-09-29): one continuous clip per hook; the VO plays over it in the edit and the daughter says
"Mama, when did that happen?" on camera. @audio1 = her mother's voice (VO T2, locked); Hook B also gets @audio2 = the daughter's line
cut from the Hook A clip (the first Seedance generation), so her voice matches across both hooks."""
import re, json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
LINE = "Mama, when did that happen?"
VOICE_C2 = ("A Black American woman in her mid-forties from the Atlanta suburbs, a warm alto with a light Georgia accent: soft 'r', drawn vowels, 'Mama' said MAH-muh. "
            "Real, unperformed surprise, a little out of breath from the stairs, the question rising at the end, half a laugh of disbelief in the breath before it, never shouted.")
MAN = lambda aud2: ("INGREDIENTS. @image1 is the opening composition: the clip opens on exactly this framing, light and camera position, and nothing in it is re-composed. "
    "@image2 is THE MOTHER: face, age, hair and build only, with the wardrobe taken from @image1 and never from this sheet. "
    "@image3 is THE DAUGHTER: face, age, hair and build only, with the wardrobe taken from @image1 and never from this sheet. "
    "@image4 is the place, exactly as shown. "
    "@audio1 is THE MOTHER's voice, its timbre, pitch, accent and pace — she does not speak in this clip; it sets who she sounds like for any breath or sound she makes. "
    + ("@audio2 is THE DAUGHTER's voice, its timbre, pitch, accent and pace, for the line THE DAUGHTER speaks; it sets who she sounds like, never how she feels in this shot. " if aud2 else "")
    + "These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to.")
TAIL = ("The phone is propped and still apart from the tiniest drift; it never moves, pans or follows anyone. One continuous shot, no cut. "
        "Mass and momentum in all movement: weight transfers first, hands arrive last, clothes and braids lag and settle; nothing melts, merges or changes shape; both women keep their faces, builds and clothes from the first frame to the last. ")
NEG = ("Negative: " + S("NEG-DEFAULT-VOICE") + ", the mother never speaks, no second line, no narration, no music, no subtitles, no text on screen, no cut to another shot, "
       "no camera travelling with anyone, no running, no one falling or stumbling, no knee strap visible, no third person close to camera, no morphing, no warping, no face swap.")
HOOKS = {
 "A": dict(dur=11, room="Small hallway and carpeted stairs, the photo wall and runner deadening it, short dull tail; her voice about a metre and a half below the phone, a little room in the signal, no boom.",
   prose=("Opening mid-climb exactly as in @image1: the mother, in her royal-blue skirt suit, comes up the last four steps toward the camera quickly and lightly, one step per half-second, her hand only brushing the rail, "
          "head up, a small proud smile, and walks past the camera on its right and out of frame at the top. "
          "Three steps behind her the daughter, in her burgundy sweater, keeps climbing, slower, gripping the rail and a little out of breath; she stops two steps from the top, one hand on the rail, "
          "looks up past the lens to where her mother went, and — in the last three seconds — says, surprised and out of breath: \"" + LINE + "\" Her voice: " + VOICE_C2)),
 "B": dict(dur=11, room="Big open mall atrium, hard terrazzo and glass, a long bright tail and a soft wash of distant shoppers; her voice about two metres from the phone, room in the signal, no boom.",
   prose=("Opening mid-descent exactly as in @image1: the daughter, in her denim jacket, comes down the mall stairs carefully with two big shopping bags, one hand on the rail. "
          "Behind her the mother, in her mustard cardigan, comes down briskly and quickly, facing forwards, one small bag in her hand, head up — she overtakes her daughter on the open side, "
          "passes her with a small proud smile, reaches the bottom and walks past the camera on its left and out of frame. "
          "The daughter stops on the second step from the bottom, bags hanging from her hands, turns her head to look after her mother, and — in the last three seconds — says, surprised and a little out of breath: \"" + LINE + "\" Her voice: " + VOICE_C2)),
}
def build(k, aud2=False):
    h = HOOKS[k]
    p = MAN(aud2) + " " + h["prose"] + " " + S("AUD-A") + " " + h["room"] + " " + TAIL + NEG
    pathlib.Path(__file__).parent.joinpath(f"sd/HK-{k}.seedance.txt").write_text(p)
    print(k, len(p), h["dur"], "s")
    return p
if __name__ == "__main__":
    build("A"); build("B", aud2=True)
