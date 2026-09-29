"""Seedance 2.5 hooks (user 2026-09-29): one continuous clip per hook; the mother's voice is only the VO,
laid over the clip in the edit (never an ingredient, she never speaks on camera). Only the daughter talks: "Mama, when did that happen?".
Hook A has no voice ingredient (her voice is written); Hook B gets @audio1 = the daughter's line cut from the generated Hook A clip,
so her voice matches across both hooks (user 2026-09-29)."""
import re, json, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[3]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
LINE = "Mama, when did that happen?"
VOICE_C2 = ("A Black American woman in her mid-forties from the Atlanta suburbs, a warm alto with a light Georgia accent: soft 'r', drawn vowels, 'Mama' said MAH-muh. "
            "Candid, not performed: said to her mother, not to anyone watching, a little under her breath and a little out of breath from the stairs, real surprise in the rising question and nothing added to it; no laugh, no giggle, no smile in the voice, never shouted, never projected.")
# V7.68.0: ingredients are information, never frames — sheets, voice clips, the plate(s), info cards; the prose writes the shot.
def MAN(k, aud2):
    # aud2: Hook B only — the daughter's line cut from the Hook A clip
    place = ("@image3 is the place: her house's upstairs landing and straight open staircase, the photo wall of black-and-white and sepia family portraits, white balusters under a dark oak handrail, the worn beige runner and the front door with glass sidelights at the bottom, exactly as shown; @image4 is the same house's hall and the foot of those stairs, its finishes exactly as shown. "
             if k == "A" else
             "@image3 is the place: the two-level suburban mall's wide open terrazzo staircase with brushed-steel handrails and glass balustrade panels standing on its own (no escalator), the shopfronts and the atrium skylight, exactly as shown. ")
    n = 5 if k == "A" else 4
    return ("INGREDIENTS. @image1 is THE MOTHER: face, age, hair and build only, with the wardrobe as written below and never from this sheet. "
      "@image2 is THE DAUGHTER: face, age, hair and build only, with the wardrobe as written below and never from this sheet. "
      + ("@audio1 is THE DAUGHTER's voice, its timbre, pitch, accent and pace, for the line THE DAUGHTER speaks; it sets who she sounds like, never how she feels in this shot. " if aud2 else "")
      + place
      + f"@image{n} is an info card: THE MOTHER's outfit in this scene, exactly as shown and captioned; follow it exactly, and its caption never appears in the clip. "
      + f"@image{n+1} is an info card: THE DAUGHTER's outfit in this scene, exactly as shown and captioned; follow it exactly, and its caption never appears in the clip. "
      "These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")
TAIL = ("The phone is propped and still apart from the tiniest drift; it never moves, pans or follows anyone. One continuous shot, no cut. "
        "Mass and momentum in all movement: weight transfers first, hands arrive last, clothes and braids lag and settle; nothing melts, merges or changes shape; both women keep their faces, builds and clothes from the first frame to the last. ")
NEG = ("Negative: " + S("NEG-DEFAULT-VOICE").replace(" no American vowel colouring,", "") + ", the mother never speaks, the daughter says only her one line, no laugh, no giggle, no smile from the daughter, the daughter never looks at the camera, no posed or staged reaction, no exaggerated expression, no overacting, the mother never touches the handrail, no empty-handed mother, no second line, no narration, no music, no subtitles, no text on screen, no cut to another shot, no escalator, "
       "no camera travelling with anyone, no running, no one falling or stumbling, no knee strap visible, no third person close to camera, no morphing, no warping, no face swap.")
HOOKS = {
 "A": dict(dur=11, room="Small hallway and carpeted stairs, the photo wall and runner deadening it, short dull tail; her voice about a metre and a half below the phone, a little room in the signal, no boom.",
   prose=("A phone propped on the upstairs landing at head height, looking straight down the flight, 24mm, 9:16, the whole flight in frame, the front door bright at the bottom; "
          "the light comes from the front-door sidelights below and the landing window behind the camera, warm clear Sunday afternoon, faces lit from the left of frame. "
          "Opening mid-climb: the mother, in her royal-blue skirt suit (cream blouse, navy pumps), comes up the last four steps toward the camera quickly and lightly, one step per half-second, "
          "both arms swinging freely at her sides, her hands never touching the handrail or the wall, head up, a small proud smile, and walks past the camera on its right and out of frame at the top. "
          "Two steps behind her, in frame from the first second, the daughter, in her burgundy sweater, dark jeans and white trainers, climbs too, slower, one hand on the rail, a little out of breath, falling behind. "
          "She never looks at the camera and never stops to perform: still climbing, her eyes on her mother as her mother pulls away above her, she says it to her — in the last three seconds, only these words and nothing else: \"" + LINE + "\" "
          "Her face stays natural — a small, real reaction, brows lifting slightly, no big expression, nothing played to the lens; the moment is caught, not staged. Her voice: " + VOICE_C2)),
 "B": dict(dur=11, room="Big open mall atrium, hard terrazzo and glass, a long bright tail and a soft wash of distant shoppers; her voice about two metres below the phone, room in the signal, no boom.",
   prose=("A phone propped at head height on the upper walkway at the top of the mall stairs, looking straight down the flight, 24mm, 9:16, the whole flight in frame and the busy ground-floor concourse below; "
          "soft daylight from the atrium skylight above, warm and clear, faces lit from the left of frame, pale terrazzo bouncing light up. "
          "Opening mid-climb: the daughter, in her light denim jacket, black top and black leggings, is halfway up the mall stairs, climbing carefully with two big shopping bags, one hand on the rail, a little out of breath. "
          "Right behind her the mother, in her mustard cardigan, cream blouse and navy wide-leg trousers, comes up the stairs briskly, facing forwards, carrying two big shopping bags just like her daughter's, one in each hand, her hands never touching the handrail, head up — "
          "she overtakes her daughter on the open side, passes her with a small proud smile, climbs the last steps toward the camera and walks past it on its right and out of frame at the top. "
          "The daughter never looks at the camera and never stops to perform: still climbing, slower, her eyes on her mother as her mother pulls away above her, she says it to her — in the last three seconds, only these words and nothing else: \"" + LINE + "\" "
          "Her face stays natural — a small, real reaction, brows lifting slightly, no big expression, nothing played to the lens; the moment is caught, not staged. Her voice: " + VOICE_C2)),
}
def build(k, aud2=False):
    h = HOOKS[k]
    p = MAN(k, aud2) + " " + h["prose"] + " " + S("AUD-A") + " " + h["room"] + " " + TAIL + NEG
    pathlib.Path(__file__).parent.joinpath(f"sd/HK-{k}.seedance.txt").write_text(p)
    print(k, len(p), h["dur"], "s")
    return p
if __name__ == "__main__":
    build("A"); build("B", aud2=True)
