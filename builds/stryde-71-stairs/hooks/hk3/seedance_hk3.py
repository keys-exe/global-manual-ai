"""Hook 3 / HK-C-SD (user 2026-10-02): same concept as Hooks A and B — one continuous Seedance 2.5 clip, the phone propped and still,
the mother's VO laid over it in the edit (she never speaks on camera), only the daughter speaks her one line, her voice = @audio1
(VOICE-C2-HKA v3, confirmed). The user's brief: down the metro station stairs with shopping bags, hurrying to catch the train,
then inside the train the daughter says her line. User kept "down" after the VO's "the whole way up" was flagged (2026-10-02).
One shot: the phone sits inside the carriage looking out through the open doors at the platform stairs, so stairs, platform and
the line in the train are all one continuous moment. "Running" is written as a brisk hurry (§35A/§27G: no 'running' in a prompt;
the speed is made in the edit)."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import seedance_hooks as H
LINE = H.LINE
MAN = ("INGREDIENTS. @image1 is THE MOTHER: face, age, hair and build only, with the wardrobe as written below and never from this sheet. "
  "@image2 is THE DAUGHTER: face, age, hair and build only, with the wardrobe as written below and never from this sheet. "
  "@audio1 is THE DAUGHTER's voice, its timbre, pitch, accent and pace, for the line THE DAUGHTER speaks; it sets who she sounds like, never how she feels in this shot. "
  "@image3 is the place: the underground metro station seen from inside the stopped train — the carriage's open double sliding doors with a steel grab pole in the middle, blue fabric seats at each side, the narrow concrete platform with its yellow edge strip, and directly opposite the doors the wide straight fixed concrete staircase with steel handrails coming down from the concourse between beige tiled walls (no escalator), exactly as shown. "
  "@image4 is an info card: THE MOTHER's outfit in this scene, exactly as shown and captioned; follow it exactly, and its caption never appears in the clip. "
  "@image5 is an info card: THE DAUGHTER's outfit in this scene, exactly as shown and captioned; follow it exactly, and its caption never appears in the clip. "
  "These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")
PROSE = ("A phone propped at chest height inside the stopped metro carriage, a step back from the open doors, looking straight out through them across the platform to the staircase opposite, 24mm, 9:16, the whole flight of stairs framed by the open doorway, the steel grab pole at the right edge of the doorway; "
  "cool-white fluorescent light over the platform and stairs, the carriage lit by its own slightly warmer ceiling strips, faces lit from above and from the left of frame. "
  "Opening mid-descent: the mother, in her teal quilted jacket, cream knit top, charcoal trousers and white trainers, is hurrying down the staircase facing forwards, brisk quick light steps, one step per half-second, "
  "carrying two big shopping bags, one in each hand, her hands never touching the handrail, head up, a small determined smile; she passes two women in their thirties who are walking down the same flight more slowly, one of them holding the rail. "
  "Two steps behind her the daughter, in her olive utility jacket, grey hoodie, black jeans and black trainers, also carrying two big shopping bags, comes down slower, a little out of breath, falling behind. "
  "The mother reaches the bottom, crosses the platform in four quick steps and steps in through the open doors, past the grab pole, and stops inside the carriage at the right of the frame, side-on to the camera, bags still in her hands, breathing easily. "
  "A moment later the daughter steps in through the doors and stops at the left of the frame facing her mother, side-on to the camera, catching her breath. "
  "The daughter never looks at the camera and never stops to perform: her eyes on her mother, she says it to her — in the last three seconds, only these words and nothing else: \"" + LINE + "\" "
  "Her face stays natural — a small, real reaction, brows lifting slightly, no big expression, nothing played to the lens; the moment is caught, not staged. Her voice: " + H.VOICE_C2 + " The doors stay open to the end; the train does not move.")
ROOM = ("Underground station and train carriage, hard tile, concrete and steel, a hollow echo with a long tail; her voice about a metre and a half from the phone inside the carriage, room in the signal, no boom.")
NEG = H.NEG.replace("the mother never touches the handrail, ", "the mother never touches the handrail, no one running, no one falling or slipping on the stairs, ").replace("no escalator, ", "no escalator, no doors closing, no train moving, no readable signs or lettering, ").rstrip(".") + ", " + H.S("NEG-SOUND") + "."
NEG = NEG.replace("no music, no subtitles", "no subtitles")
P = MAN + " " + PROSE + " " + H.S("AUD-A") + " " + ROOM + " " + H.TAIL + NEG
out = pathlib.Path(__file__).parent / "HK-C.seedance.txt"; out.write_text(P); print(len(P))
