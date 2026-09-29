from strings import *
GRID = open('/tmp/claude-0/grid.txt').read().strip()
def sheet(sex, face, hair, body, face_note, ward, side="left", wall="pale grey", floor="grey carpet tile"):
    return (f"A character reference sheet: FIVE PHOTOGRAPHS OF THE SAME ONE {sex}, tiled edge to edge on a single tall 9:16 canvas with thin seams between them, all taken within the same minute in the same spare room by somebody standing where the door is. "
     + GRID + " " +
     f"TOP ROW, three equal panels: full length head to toe, standing square at the same distance in all three so the head is the same size in each — left panel facing the camera, middle panel in true left profile, right panel in true right profile. "
     f"BOTTOM ROW, two panels: left, the back of the head and shoulders from the waist up; right, a tight face close-up from the hairline to the collarbones, facing the camera, eyes level on the lens — the same face as the front panel, closer. "
     f"Every panel is this person and only this person, exactly the person in the attached reference photograph, and nothing changes between panels except the angle of the body. {face} {hair} {body} {face_note} "
     f"Mouth closed, no expression held for the camera. {ward}, identical in every panel; exposed skin plain, nothing on the skin in one panel that is not in all the others. "
     f"THE LIGHT is one window, to the {side}, in every panel: daylight from that side at about forty-five degrees, bright on the near side of the face and body and falling off across the far cheek to open shadow lifted by bounce off the wall — the same side, the same fall-off, in all five panels, so the profiles are lit one from the front and one from behind exactly as they would be. "
     f"The window out of frame, its edge blowing a patch of the wall to flat white in the {side}-hand panels, the room a little under-exposed away from it. Plain {wall} wall, white skirting, {floor}, nothing else in frame.")
NEG_SHEET = ("no different people, no face changing between panels, no age changing between panels, no younger face in the close-up, no hair colour or length changing between panels, no clothing changing between panels, "
 "no head size changing across the top row, no window changing sides between panels, no sweat, no wet skin, no tattoos, no birthmarks, no skin patches, no marks in one panel only, no smile, no glasses, "
 "no eyes looking away in the front or close-up panels, no labels, no text, no captions, no arrows, no drawn turnaround, no illustration, no mannequin, no 3D render, no CGI, no studio backdrop, no gradient backdrop, "
 "no studio lighting, no even frontal light, no flat shadowless face, no more than five panels, no fewer than five panels, no overlapping panels, no gaps between panels")
NEG_GRID = ("no head size changing between full-length panels, no figure at a different scale in any full-length panel, no feet cut off, no head cut off, no hair cut off, no figure off centre in its panel, no figure leaning, "
 "no three-quarter view in a profile panel, no profile panel showing both eyes, no back view showing the face, no close-up cropped above the collarbones or below the top of the head, no unequal panels in a row, "
 "no overlapping panels, no gaps between panels, no more than five panels, no fewer than five panels")
NEG_DEF = ("no generically pleasant symmetrical face, no default silver swept-back hair, no catalogue-model bone structure, no stock retiree archetype, no soft agreeable features throughout, not a face that could advertise anything")
paula = sheet("WOMAN",
 "Paula, a Black American woman of fifty-eight with deep brown, melanin-rich skin, the woman in the attached reference photograph. An oval face with broad high cheekbones whose fullness has dropped, a jawline softening into the start of jowls at its corners, deep nasolabial folds and marionette lines running down from the mouth corners, hollows under the eyes with dark circles and fine crepey lines, two horizontal creases across the forehead and a short vertical line between the brows. Almond eyes under heavy, slightly hooded upper lids, dark brown irises; a broad nose with a rounded tip; full lips, the upper lip darker, the corners turning slightly down. Her left upper eyelid sits a little heavier than her right.",
 "Black hair heavily streaked with grey at the hairline and temples, pulled back into a low loose bun at the nape with soft flyaway wisps at the temples — the same grey, the same bun height in every panel.",
 "Medium build, soft through the middle, average height, shoulders a little rounded.",
 "Skin slightly grey and flat in tone, uneven, with a thin everyday foundation that has settled into the lines around the eyes and mouth, exactly as in the reference; the same in every panel.",
 "A charcoal grey textured wool-blend blazer worn open over a plain black scoop-neck knit top, charcoal tailored trousers, black low-heeled leather pumps, small silver hoop earrings")
robin = sheet("WOMAN",
 "Robin, a white American woman of forty-eight with fair skin, the woman in the attached reference photograph. A heart-shaped face with defined cheekbones, a narrow straight nose, warm brown eyes under arched dark brows, medium-full lips, light freckling across the nose and upper cheeks, fine crow's feet at the eye corners and faint lines from nose to mouth, the skin just softening under the jaw. Her smile lines sit deeper on the right side.",
 "Shoulder-length layered brown hair with caramel highlights, worn loose with a slight side parting, the ends flicking outward — the same tone and length in every panel.",
 "Slim build, average height, upright easy posture.",
 "Light everyday makeup exactly as in the reference; the same in every panel.",
 "A navy tailored single-button blazer over an ivory draped silk V-neck blouse, navy tailored trousers, black leather pumps, small gold hoop earrings and a fine gold chain with a small round disc pendant")
tail = lambda: " " + LOOK + " " + CAP + " NEGATIVES: " + NEG_SHEET + ", " + NEG_GRID + ", " + NEG_DEF + ", " + NEG_FILM
for n, body in (("PAULA", paula), ("ROBIN", robin)):
    p = CAM(50, "T4", "a locked tripod at standing eye height") + " " + body + tail()
    open(f"beats/SHEET-{n}.t2i.txt", "w").write(p)
    print(n, len(p))
