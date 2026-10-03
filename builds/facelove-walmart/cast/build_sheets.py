#!/usr/bin/env python3
"""§19 Mode 5 avatar-sheet prompts for facelove-walmart, assembled from Appendix A by ID (never retyped).
Mode 5 sheet (§19 "Mode 5 sheets"): CAM-ANIM (portrait focal, deep focus) + SHEET-GRID + AVATAR-SHEET (sameness, wardrobe,
one-window light, room) + PIX-SHAPE + PIX-EYES + LOOK-WALMART + CAP-ANIM; negatives NEG-SHEET (its two anti-render clauses
dropped — the sheet IS a render) + NEG-GRID + NEG-PIX + NEG-DEFAULT-FACE.
Adaptation (as stryde-71-stairs-pixar-song): AVATAR-SHEET / SHEET-GRID say "photograph" and "phone" — read as render / camera,
because §24O rule 1 keeps photograph words out of a stylised prompt. No cast pictures were supplied: every face is new (§19A).
Michelle's after sheet keeps every line of the before sheet (TERRAIN_LOCK, product sheet) — only colour evens out."""
import re, json, pathlib
HERE = pathlib.Path(__file__).parent
MASTER = HERE.resolve().parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()

def unphoto(s):
    return (s.replace("FIVE PHOTOGRAPHS", "FIVE RENDERS").replace("photographs", "renders").replace("photograph", "render")
             .replace("all taken within the same minute", "all rendered within the same minute")
             .replace("by somebody standing where the door is", "from a virtual camera standing where the door is")
             .replace("facing the phone", "facing the camera").replace("the phone", "the camera"))

# Animated Film Look Sheet fields 1, 4, 6 (BUILD_SHEET.md §1b) — pasted verbatim on every Mode 5 frame
LOOK = (S("LOOK-ANIM-PATTERN")
  .replace("[GENRE AND REFERENCE, one plain sentence]",
           "A warm, grown-up American animated family drama made like a theatrical 3D feature — a bright big-box store aisle, a lamplit family living room, a bedroom vanity and a sunlit patio, told with tenderness and quiet wit")
  .replace("[DESIGN: the shape language and proportions of the characters]",
           "Appealing stylised adults about five and a half to six heads tall, each built on one clear shape, large expressive eyes, soft rounded features and simple readable hands")
  .replace("[MATERIALS: how stylized skin, hair, fabric and surfaces are]",
           "Soft subsurface skin with no pores, sculpted groomed hair that catches the light in strands, fabric with real weave and weight, and surfaces with a light painterly softness")
  .replace("[PALETTE: the dominant colours of the sets and wardrobe]",
           "Bright clean whites, cool blues and warm wood in the store; amber lamplight, dusty mauve and faded grey in the house of the Before; soft lilac, cream, camel and warm gold in the After"))

CAM = (S("CAM-ANIM").replace("[VIRTUAL PACKAGE]", "a large-format sensor with spherical primes").replace("[FOCAL]", "50")
       .replace("[DEPTH OF FIELD]", "deep focus, everything sharp from the floor to the wall"))
CAP = S("CAP-ANIM") + " The skin is stylised animation skin: smooth subsurface warmth, no pores, no photographic texture."

CAST = {
 "N-MICHELLE": dict(sex="WOMAN", side="left", wall="pale warm grey", floor="worn honey oak floorboards", heads="five and a half heads tall, a little stooped",
   shape="TRIANGULAR is her dominant shape: a heart-shaped face wide at the temples narrowing to a small pointed chin, a long slender neck, narrow sloping shoulders over a slim A-line body — the silhouette a tall narrow triangle. The one contrasting shape is a single soft round curl of hair resting on her right cheekbone",
   face="A heart-shaped face with high cheekbones, large dark-brown almond eyes under thin gently arched brows, a slim straight nose with a slightly rounded tip, and a small mouth with a full lower lip. Her charm marker: ONE small dark beauty mark high on her LEFT cheekbone, below the outer corner of the left eye — on the left side only, the right cheek plain. Her left eyebrow sits a touch higher than the right",
   hair="Chin-length dark ash-brown hair heavily threaded with grey, flat and limp, tucked behind the left ear with no shape at the crown — the same tone and the same length in every panel",
   body="A Latina American woman, light olive-tan skin, sixty-three years old. Medium height, slim and narrow, shoulders rounded forward",
   ward="A shapeless faded dusty-mauve knit cardigan buttoned over a washed-out grey T-shirt, loose charcoal pull-on trousers and flat grey felt slippers",
   age="deep lines across the forehead, a deep crease between the brows, deep folds from the nose to the mouth corners, crow's feet, a slackening jaw and soft neck, and grey-violet shadows under the eyes; the skin dull and a little greyish, the face hollow under the cheekbones and tired — all stylised, drawn as shape and soft shading, never as pores"),
 "N-MICHELLE-AFTER": dict(sex="WOMAN", side="left", wall="pale warm grey", floor="worn honey oak floorboards", heads="five and a half heads tall, standing tall", after=True,
   shape="TRIANGULAR is her dominant shape: the same heart-shaped face narrowing to a small pointed chin, the same long slender neck, narrow shoulders now held back over a slim A-line body — the silhouette a tall narrow triangle. The one contrasting shape is the single soft round curl of hair resting on her right cheekbone",
   face="The same heart-shaped face with high cheekbones, large dark-brown almond eyes under thin gently arched brows, a slim straight nose with a slightly rounded tip and a small mouth with a full lower lip, now relaxed and composed. Her charm marker: ONE small dark beauty mark high on her LEFT cheekbone, below the outer corner of the left eye — on the left side only. Her left eyebrow sits a touch higher than the right",
   hair="The same chin-length dark ash-brown hair threaded with grey, now washed and blown out with soft volume at the crown, swept back from the face and tucked behind the left ear in a sleek polished shape — the same tone and the same length in every panel",
   body="A Latina American woman, light olive-tan skin, sixty-three years old. Medium height, slim, standing tall with her shoulders back and her chin level",
   ward="A soft cream fine-knit sweater with a boat neck, high-waisted camel wide-leg trousers and tan leather loafers",
   age="the same lines still there and still visible — across the forehead, between the brows, the folds from the nose to the mouth and the crow's feet — but the skin tone now even and warm, the redness and the grey-violet shadows under the eyes gone, the skin the same skin, not a mask — all stylised, drawn as shape and soft shading, never as pores"),
 "C1-PETER": dict(sex="MAN", side="right", wall="pale blue-grey", floor="dark stained floorboards", heads="six heads tall",
   shape="SQUARE is his dominant shape: a big boxy head with a broad flat-topped skull and a square jaw, wide square shoulders, a thick rectangular torso and square hands — the silhouette a stack of blocks. The one contrasting shape is a single round tuft of grey hair left at the front of his receding hairline",
   face="A broad square face with a heavy square jaw, small pale-blue eyes set close under thick straight grey brows, a wide fleshy nose and a wide thin-lipped mouth. His charm marker: a deep cleft in the middle of his chin. His right ear sits a touch higher than the left",
   hair="Short grey hair receding high at both temples, cropped close at the sides, one round grey tuft left at the front — the same in every panel",
   body="A white American man, ruddy fair skin, sixty-five years old. Tall, barrel-chested, a heavy middle and broad shoulders",
   ward="A navy quarter-zip pullover over a white collared shirt, pressed tan chinos and brown leather boat shoes",
   age="deep lines across the forehead, heavy bags under the eyes, deep folds from the nose to the mouth, jowls and a soft double chin — all stylised, drawn as shape, never as pores"),
 "C2-YOUNGER": dict(sex="WOMAN", side="right", wall="soft white", floor="pale grey floorboards", heads="six heads tall",
   shape="TRIANGULAR, POINT DOWN, is her dominant shape: broad straight athletic shoulders tapering to narrow hips and long tapering legs, a face wide at the cheekbones narrowing to a sharp pointed chin — the silhouette an inverted triangle. The one contrasting shape is a single round high bun on the top of her head",
   face="A face wide at the cheekbones narrowing to a sharp pointed chin, wide-set green cat-shaped eyes under sharp angled brows, a short upturned nose and a wide mouth with thin lips. Her charm marker: a small scatter of freckles across her RIGHT cheek only — the left cheek plain. Her right eye sits a touch narrower than the left",
   hair="Long straight honey-blonde hair with darker roots, pulled up into one round high bun on the crown, smooth at the sides — the same size and height in every panel",
   body="A white American woman, fair skin, forty-one years old. Tall and athletic, broad straight shoulders, narrow hips, long legs",
   ward="A fitted camel cropped blazer over a white ribbed tank top, black flared leggings and white chunky platform trainers",
   age="smooth skin with faint lines at the outer eyes and a faint crease between the brows — all stylised, drawn as shape, never as pores"),
 "C3-ROSA": dict(sex="WOMAN", side="left", wall="warm terracotta-beige", floor="warm red-brown floor tiles", heads="five and a half heads tall, solid and planted",
   shape="ROUND is her dominant shape: a round head, round full cheeks, a round soft bosom and hips and rounded hands — the silhouette a stack of soft circles. The one contrasting shape is her straight blunt fringe, a single hard horizontal line across her forehead",
   face="A round face with full rosy cheeks, warm dark-brown round eyes with lifted outer corners under thick dark arched brows, a broad rounded nose and a wide generous mouth with full lips. Her charm marker: ONE bold streak of silver-white hair running back from the LEFT temple — on the left side only. Her right eyebrow sits a touch higher than the left",
   hair="Thick shoulder-length black hair with a few grey threads, a straight blunt fringe across the forehead and soft waves below, one bold silver-white streak from the left temple — the same tone and the same length in every panel",
   body="A Latina American woman, warm medium-tan skin, sixty-seven years old — the older sister. A little shorter than average, soft and full-figured, round shoulders, planted firmly on both feet",
   ward="A deep marigold-orange wrap blouse, a long full ink-blue skirt to mid-calf and flat tan leather sandals",
   age="laugh lines fanning from the outer eyes, soft folds from the nose to the mouth, a soft jawline, and an even warm skin tone with a healthy flush on the cheeks — all stylised, drawn as shape, never as pores"),
}

def build(k, c):
    opening = (f"A character reference sheet from a finished 3D animated feature film: FIVE RENDERS OF THE SAME ONE {c['sex']}, "
               "tiled edge to edge on a single tall 9:16 canvas with thin seams between them. NO WRITING ANYWHERE ON THE CANVAS: no panel titles, no captions, no labels, no text of any kind.")
    sheet = S("AVATAR-SHEET")
    _, rest = sheet.split(". ", 1)                       # the opening sentence is replaced by the render opening above
    body = unphoto(rest)
    for a, b in [("[FACE — architecture in three or four plain sentences, the one marker, the asymmetries]", c["face"]),
                 ("[HAIR — colour, roots, how worn, the same tone and the same height in every panel]", c["hair"]),
                 ("[BODY — build, height impression]", c["body"] + ", drawn " + c["heads"] + " (§24A proportion)"),
                 ("[WARDROBE — BASE, LOWER, FOOT]", c["ward"]),
                 ("[SIDE]", c["side"]), ("[WALL COLOUR]", c["wall"]), ("[FLOOR]", c["floor"])]:
        body = body.replace(a, b)
    ns = S("NEG-SHEET").replace(", no 3D render, no CGI", "")
    if c.get("after"):   # the after look IS the product on her face: an even finish, terrain unchanged (cover, not erase)
        body = body.replace("Bare face, no makeup, in every panel including the close-up.",
            "In every panel including the close-up she wears a light, natural foundation that evens her skin tone and covers the shadows under her eyes, and nothing else but a little mascara; every line and crease of her face is still there, the skin still reads as skin.")
        ns = ns.replace("no makeup, ", "no heavy makeup, no lipstick colour, no contour, ")
    assert "[" not in body, k
    pix = ("SHAPE LANGUAGE. " + c["shape"] + ". " + S("PIX-SHAPE") + " "
           "The face is stylised the way a great animated feature stylises an adult — larger emotive eyes, a softened sculpted structure, appealing exaggeration — "
           "and the age is carried in shape: " + c["age"] + ".")
    eyes = "EYES. " + S("PIX-EYES")
    extra = "no live-action photograph, no photoreal human, no panel titles, no words on the canvas, no matching marks on both sides of the face"
    if c.get("after"):
        extra += ", no lines erased, no smoothed or airbrushed skin, no younger face than the before sheet"
    neg = ", ".join([ns, S("NEG-GRID"), S("NEG-PIX"), S("NEG-DEFAULT-FACE"), extra])
    return "\n\n".join([CAM, opening, "THE SHEET. " + unphoto(S("SHEET-GRID")), body, pix, eyes, LOOK, "RENDER. " + CAP, "AVOID: " + neg + "."])

if __name__ == "__main__":
    out = {}
    for k, c in CAST.items():
        p = build(k, c); out[k] = p
        (HERE / f"{k}.prompt.txt").write_text(p)
        print(k, len(p))
    json.dump(out, open(HERE / "prompts.json", "w"), indent=1, ensure_ascii=False)
    (HERE / "LOOK.txt").write_text(LOOK)
