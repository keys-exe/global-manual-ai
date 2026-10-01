"""Act 6 start images (Manual, 2026-09-28). Same structure as act5/make_act5_images.py."""
import json, sys, re
sys.path.insert(0, '../../../products/stryde'); import stryde_product_sheet as s
F = lambda x: s.fill(x, 'right')
HEAD="Shot on an iPhone 17 Pro Max, handheld, the main 48MP Fusion camera at 24mm equivalent and f/1.78, left on its default 24 megapixel output, Smart HDR 5 and Deep Fusion on, Photographic Style on Standard, everything left on automatic — exposure, white balance and focus all chosen by the phone rather than by a person. An ordinary photo taken on an ordinary phone."
FILE="THIS IS A FILE, NOT A PICTURE. Nobody framed it, nobody lit it, nobody chose the moment and nobody looked at it afterwards. It is an unremarkable photograph off a phone. Sharpness is uneven across the frame: one plane is in focus and everything in front of and behind it falls away, because the lens has one fixed aperture and nobody chose where to put the focus. Edges are soft rather than crisp, with faint compression mush in the shadows and detail thinning toward the corners. Nothing has been sharpened, cleaned up, separated from its background or arranged, and no part of the frame has been given more attention than any other part."
AV="no posing for camera, no glancing at the lens, no staged or completed action, no centred composition, no stock footage look, no AI face, no extra fingers, no fused fingers, no deformed limbs, no warped background, no over-saturated colors, no moody dark grade, no light from nowhere, no lens flare"
def P(scene, angle, focus, light, avoid, text_ok=False):
    tail = ", no other text, no other logos" if text_ok else ", no readable text, no logos"
    return "\n\n".join([HEAD, scene, "THE CAMERA ANGLE: "+angle+" This exact angle, not a straight-on eye-level view.", "FOCUS: "+focus+" The blur is optical: soft and round, never smeared.", light, FILE, "AVOID: "+avoid+", "+AV+tail])+"\n"
def drop(neg, *bad):  # remove clauses that contradict a two-strap beat
    parts=[p.strip() for p in neg.split(",")]
    return ", ".join(p for p in parts if not any(b in p for b in bad))

NHANDS="THE SAME WOMAN'S HANDS as in the attached reference sheet — fifty-seven, long fingers, a little knuckly, short plain nails, no rings —"
KEN="THE SAME MAN as in the attached reference sheet — a thin long hollow face, a broken nose, sparse white hair combed back, seventy-two, small, wiry and straight-backed —"
JOAN="THE SAME WOMAN as in the attached reference sheet — seventy-nine, small and slight, a small round soft face, a thick white pixie crop, a thin scar through one eyebrow, a friendly, natural face —"
KD2="A bottle-green short-sleeved polo shirt, khaki chino shorts just above the knee, navy socks, brown brogues, his flat cap in one hand."
JD2="A navy white-polka-dot cotton dress just above the knee, a coral cotton cardigan, bare legs, white canvas pumps, a straw handbag on her arm."
WORK_L="THE LIGHT: the sash window on the room's east wall lights the desk from the left of the frame, soft ordinary morning daylight, warm on the paper and the red brick, so each hand has a lit side toward the left and a softer shadow side. The shadows fall away from that source, one way only."
STOP_L="THE LIGHT: broken-cloud afternoon sun, brighter and warmer than before, from the left of the frame, bounce off the pale pavement, so he has a lit side toward the left. The shadows fall away from that source, one way only."
STEPS_L="THE LIGHT: low warm afternoon sun from the west raking across the sandstone steps from the left of the frame, warm on her face and the stone, long soft shadows falling to the right, one way only."
TABLE_L="THE LIGHT: soft daylight from a kitchen window to the left of the frame, ordinary and even, a little warm. The shadows fall away from the window, one way only."
PROD=s.REF_PROD
W=PROD+" "+F(s.PLACE_LOCK_C)+" "+s.SIZE_WORN+" "+s.FIT_SNUG
B={}
B["BR-057"]=P(NHANDS+" IN THE SAME WORKROOM as the attached room photograph, at the long worktop desk among the post trays and loose letters. Both hands are partway through unfolding one printed letter flat on the desk, the sheet half open, its top fold lifting as her fingers smooth it down. The rust-orange needlecord cuffs of her open overshirt show at the wrists. The printing is too small and soft to read.",
 "the lens directly above, looking straight down at the desk, seen from the front of her, close: her two hands and the half-open letter fill the frame, other letters around it.",
 "her hands and the letter are in sharp focus; the letters at the edges fall a little soft.", WORK_L,
 "no faces, no melted hands, no smooth young hands, no manicured nails, no floating paper, no styled or cleared surfaces, no product")
B["BR-058"]=P(NHANDS+" IN THE SAME WORKROOM as the attached room photograph, at the cork pinboard crowded with pinned cards and notes. One forefinger rests lightly just under one handwritten line on a small cream card pinned among the others, the fingertip still, touching the card. The handwriting is soft blue ink, too small and blurred to read. The rust-orange needlecord cuff of her overshirt shows at the wrist.",
 "the lens at eye height, three-quarter to the pinboard, very close: her fingertip and the card fill the frame, the neighbouring cards falling away.",
 "her fingertip and the line of ink under it are sharp; everything else on the board falls soft quickly.", WORK_L,
 "no readable words, no faces, no melted hands, no smooth young hands, no manicured nails, no product")
B["PR-061a"]=P("On an ordinary wooden kitchen table, the open Stryde box. "+s.PACKAGE_LOCK+" The lid leans against the back of the base. One hand, a woman's, rests on the edge of the lid at the back, about to settle it. "+PROD.replace("The product exactly as in the attached reference image","Each strap exactly as in the attached product photos")+" two identical straps. "+s.SIZE_OBJECT,
 "the lens directly above the open box, looking down, seen from the front: the box, both straps in their wells and the hand on the lid fill the frame, a strip of wooden table around it.",
 "both straps and their wordmarks are in sharp focus.", TABLE_L,
 s.NEG_PACKAGE+", no face", text_ok=True)
B["BR-061b"]=P(KEN+" AT THE SAME BUS STOP as the attached street photograph: the high granite kerb, the glass shelter with its red perch bench, the lamp post with the hanging basket of red geraniums. He is halfway through standing up briskly from the red perch bench: his weight already forward over his feet, both hands pushing off his thighs just above the knees, bottom just lifting off the bench, a small pleased set to his mouth. ONE STRAP ON EACH KNEE — two identical straps. On his right knee: "+W+" On his left knee an identical second strap sits exactly the same way, on the tendon below the kneecap. His hands stay on his thighs above the straps, never on them. "+s.LEG_SKIN+" "+KD2,
 "the lens low, at knee height in front of the shelter, seen from three-quarter of him, full: his whole figure from head to shoes, the bench and shelter behind.",
 "everything from near to far stays sharp — him, both straps, the shelter.", STOP_L,
 drop(F(s.NEG_PLACE),"left knee","both knees","second unit")+", no hands on the straps, no shorts over the straps, no looking at the lens", text_ok=True)
B["PR-062"]=P(KEN.replace("THE SAME MAN","THE SAME MAN'S HANDS AND FOREARMS")+" AT THE SAME BUS STOP as the attached street photograph, the pavement and kerb soft behind. His open right palm, held out in front of him at chest height, holds two identical straps stacked loosely one on the other, the top one's front facing the lens with its wordmark readable, the band of each a soft relaxed loop. "+PROD.replace("The product exactly as in the attached reference image","Each strap exactly as in the attached product photos")+" "+s.SIZE_HELD+" "+s.WORDMARK_LOCK+" The green polo sleeve and a bare forearm show.",
 "the lens at eye height, level, square to his palm from the front, close: his open hand and the two straps fill the middle of the frame, the street soft behind.",
 "the two straps in his palm are in sharp focus; the street behind falls soft.", STOP_L,
 "no face, no fingers closing over the straps, no third strap, no single strap, no strap worn, no stretched band, no twisted shell, no shell seen edge-on", text_ok=True)
B["BR-064"]=P("On an ordinary wooden kitchen chair by a kitchen table, one bare lower leg of an older person in cropped trousers, seen from the side. "+s.FAKE_BASE+" This copy: "+dict(s.FAKE_ARCHETYPES)["wide webbing"]+". It has slipped: the copy has slid down the shin to just above the ankle-bone half-way, its stretched band slack and gaping away from the skin, the shell tilted and loose, leaving the knee above it completely bare. "+s.LEG_SKIN,
 "the lens low, at shin height, in profile to the leg, close: the knee, the shin and the sagging copy fill the frame, the chair leg and kitchen floor behind.",
 "the copy on the shin is sharp; the kitchen behind falls soft.", TABLE_L,
 s.NEG_FAKE_HERO+", no stryde wordmark, no chrome, no strap on the knee, no face")
B["BR-065"]=P(JOAN+" AT THE SAME HOUSE as the attached street photograph: the seven worn sandstone steps up to the dark-red front door, the black iron railing on the left side of the steps only, the terracotta pot of lavender on the top step. She is coming DOWN the steps forwards, towards the lens, halfway through one easy step: her left hand light on the black iron railing, her right foot lowered onto the next step down with the knee bending over it, her left foot on the step above, upright and relaxed, smiling, eyes on the steps ahead. "+W+" "+s.LEG_SKIN+" "+JD2,
 "the lens low at the foot of the steps, a little above the pavement, looking up the flight at her from the front. Her whole figure on the steps, the railing and the red door behind her.",
 "everything from near to far stays sharp — the steps, the railing, her, the strap.", STEPS_L,
 F(s.NEG_BENT)+", no gripping the rail hard, no leaning back, no stiff leg, no both feet on one step, no dress over the strap, no looking at the lens", text_ok=True)
REFS={"N":"4bb1467d-f843-4329-affe-b50470add366","R2":"4fe46b58-adec-4baf-bbf8-61f70a909fca","R3":"5684782d-e205-428b-a5f1-00a73d31f126",
      "P2":"698faa52-95f7-43c6-97f9-a275cd523628","P3":"81a48aac-63e3-4ed3-9535-28152afddeda","P5":"f947f98d-3e33-4f28-ad55-71758c81b9b1",
      "front":"7106f755-c1f5-4d61-b948-4462ed654dfe","back":"b461416e-189b-470b-9fc9-cb77da229ead","worn_front":"f5263ed7-0667-4ebd-977e-9bfd835d5036",
      "box_open":"a9409405-2d78-4802-bdf0-01c7266b18a1"}
PLAN={"BR-057":("nano_banana_2",["N","P2"]),"BR-058":("nano_banana_2",["N","P2"]),
      "PR-061a":("gpt_image_2_5",["box_open","front","back"]),"BR-061b":("nano_banana_pro",["R2","P3","front","back","worn_front"]),
      "PR-062":("nano_banana_pro",["front","back","R2","P3"]),"BR-064":("nano_banana_pro",[]),
      "BR-065":("nano_banana_pro",["R3","P5","front","back","worn_front"])}
refs={}
for b,t in B.items():
    open(b+".txt","w").write(t)
    refs[b]=[PLAN[b][0],[{"value":REFS[r],"role":"image_references"} for r in PLAN[b][1]]]
    print(b,len(t),PLAN[b])
json.dump(refs,open("refs.json","w"))
