"""Hook 3 (user 2026-10-02): same concept as Hooks A and B — Seedance 2.5, the phone propped and still, the mother's VO laid over
it in the edit (she never speaks on camera), only the daughter speaks her one line, her voice = @audio1 (VOICE-C2-HKA v3).
User: "Cause the last sunday is a different scene" -> two shots, cut together in the edit:
  HK-C1-SD (5 s, silent) under "I'm 71, and I take the stairs faster than women half my age." (VO 0.00-3.94 s):
      the mother hurries down the metro stairs with her shopping bags, past two women in their thirties, and into the waiting train.
  HK-C2-SD (7 s, dialogue) under "Last Sunday, my daughter walked behind me the whole way up and said," + the daughter's line:
      inside the moving train, the daughter, out of breath, says "Mama, when did that happen?".
Both shots look the same way (the carriage's door wall, P9), so no reverse plate is needed (HT22/L24); one SCENE SO FAR block (HT23).
"Running" is written as a brisk hurry (§35A/§27G); the speed is made in the edit."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[1]))
import seedance_hooks as H
LINE = H.LINE
HERE = pathlib.Path(__file__).parent
PLACE = ("@image3 is the place: the underground metro station seen from inside the train — the carriage's double sliding doors with a steel grab pole in the middle, blue fabric seats at each side, the narrow concrete platform with its yellow edge strip, and directly opposite the doors the wide straight fixed concrete staircase with steel handrails coming down from the concourse between beige tiled walls (no escalator), exactly as shown. ")
def MAN(aud, n0):
    return ("INGREDIENTS. @image1 is THE MOTHER: face, age, hair and build only, with the wardrobe as written below and never from this sheet. "
      "@image2 is THE DAUGHTER: face, age, hair and build only, with the wardrobe as written below and never from this sheet. "
      + ("@audio1 is THE DAUGHTER's voice, its timbre, pitch, accent and pace, for the line THE DAUGHTER speaks; it sets who she sounds like, never how she feels in this shot. " if aud else "")
      + PLACE
      + "@image4 is an info card: THE MOTHER's outfit in this scene, exactly as shown and captioned; follow it exactly, and its caption never appears in the clip. "
      "@image5 is an info card: THE DAUGHTER's outfit in this scene, exactly as shown and captioned; follow it exactly, and its caption never appears in the clip. "
      "These references set who, where and what things ARE; the prose below sets the shot and what HAPPENS, and nothing in them is a shot to cut to.")
SCENE = ("SCENE SO FAR: a Sunday afternoon; the mother, in her teal quilted jacket, cream knit top, charcoal trousers and white trainers, carries two big shopping bags, one in each hand; "
  "the daughter, in her olive utility jacket, grey hoodie, black jeans and black trainers, carries two big shopping bags too; the daughter is a little taller than her mother. ")
LIGHT = ("cool-white fluorescent light over the platform and stairs, the carriage lit by its own slightly warmer ceiling strips, faces lit from above and from the left of frame. ")
C1 = ("A phone propped at chest height inside the stopped metro carriage, a step back from the open doors, looking straight out through them across the platform to the staircase opposite, 24mm, 9:16, the whole flight of stairs framed by the open doorway, the steel grab pole at the right edge of the doorway; " + LIGHT +
  "Opening mid-descent: the mother is halfway down the staircase, hurrying, facing forwards, brisk quick light steps, one step per half-second, a bag in each hand, her hands never touching the handrail, head up, a small determined smile; "
  "she passes two women in their thirties who are walking down the same flight more slowly, one of them holding the rail. Three steps behind her the daughter comes down too, slower, a little out of breath. "
  "The mother reaches the bottom, crosses the platform in four quick steps and steps in through the open doors, passing the camera on its right and out of frame. "
  "Nobody speaks; every mouth stays closed. The doors stay open to the end; the train does not move.")
C2 = ("A phone propped at chest height inside the metro carriage, looking across the carriage at its closed double doors and the steel grab pole in front of them, 24mm, 9:16, both women in frame from the knees up; "
  "the train is moving through the tunnel: dark tunnel walls and passing lights slide by in the door windows, the carriage sways gently, the carriage lit by its own slightly warmer ceiling strips, faces lit from above and from the left of frame. "
  "Opening a moment after they boarded: the mother stands at the right of the frame beside the pole, side-on to the camera, her two shopping bags at her feet, one hand resting on the pole, breathing easily, a small proud smile, looking ahead. "
  "The daughter stands at the left of the frame facing her mother, side-on to the camera, her two bags at her feet, still catching her breath, one hand on her chest. "
  "The mother never speaks. The daughter never looks at the camera and never stops to perform: her eyes on her mother, she says it to her — in the last three seconds, only these words and nothing else: \"" + LINE + "\" "
  "Her face stays natural — a small, real reaction, brows lifting slightly, no big expression, nothing played to the lens; the moment is caught, not staged. Her voice: " + H.VOICE_C2)
ROOM = "Inside a metro carriage in a tunnel, a steady low rumble, hard steel and plastic, a short tail; her voice about a metre and a half from the phone, room in the signal, no boom."
TAIL = H.TAIL.replace("both women keep", "both women keep")
NEG1 = H.NEG.replace("the mother never speaks, the daughter says only her one line, ", "nobody speaks, no one's lips move, ").replace("the mother never touches the handrail, ", "the mother never touches the handrail, no one running, no one falling or slipping on the stairs, ").replace("no escalator, ", "no escalator, no doors closing, no train moving, no readable signs or lettering, ").replace("no music, no subtitles", "no subtitles").rstrip(".") + ", " + H.S("NEG-SOUND") + "."
NEG2 = H.NEG.replace("the mother never touches the handrail, no empty-handed mother, ", "no empty-handed mother, ").replace("no escalator, ", "no doors opening, no station platform, no stairs, no readable signs or lettering, ").replace("no camera travelling with anyone, no running, no one falling or stumbling, ", "no camera travelling with anyone, no one falling or stumbling, ").replace("no music, no subtitles", "no subtitles").rstrip(".") + ", " + H.S("NEG-SOUND") + "."
P1 = MAN(False, 3) + " " + SCENE + C1 + " " + TAIL + NEG1
P2 = MAN(True, 3) + " " + SCENE + C2 + " " + H.S("AUD-A") + " " + ROOM + " " + TAIL + NEG2
(HERE / "HK-C1.seedance.txt").write_text(P1); (HERE / "HK-C2.seedance.txt").write_text(P2)
old = HERE / "HK-C.seedance.txt"
if old.exists(): old.unlink()
print(len(P1), len(P2))
