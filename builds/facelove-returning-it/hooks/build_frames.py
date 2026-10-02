#!/usr/bin/env python3
"""Step 6 — the three hooks' cold-open frames (§6A, A/B pair: two gpt_image_2_5 Sunburst renders each).
HK1-01 her bare face + the closed stick held up (refs: CLOSED, N-VOICE-IMG-B) · HK2-01 her hands taping the FACELOVE mailer shut (PACKAGING, N-VOICE-IMG-B)
· HK3-01 the makeup counter, an edit of the L-COUNTER plate (L-COUNTER, C1 sheet, N-BEFORE sheet)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
F = {
 "HK1-01": dict(line="I am so mad, and this is exactly why you read the reviews before you buy another foundation.",
  refs=[("FACELOVE stick, closed (CLOSED.jpg)", "product", "6258295b-8f69-4d47-950f-1c980dc2af8b"), ("N-VOICE-IMG-B (confirmed)", "character", "99d3f3a6-e596-4487-9370-82bdbb4ce912")],
  face=True, room=True, product=True, body=True, match=None, edit_of=None,
  motion="From this frame: she taps the closed stick twice against her palm, brows drawn, then holds it still beside her cheek — two taps, about 2 s; phone propped, no camera move.",
  prompt=("For the line — I am so mad, and this is exactly why you read the reviews before you buy another foundation. —: she holds the closed FACELOVE stick up beside her face, cross. "
   "Chest-up at her vanity, phone propped at eye level. "
   "Image 1 is the product, copied exactly — same shape, same parts, same violet finish, one wordmark, nothing redesigned; held upright in her right hand beside her right cheek, the size of a thick marker pen, a little longer than her hand is wide, about a quarter of the frame tall. "
   "Image 2 is her: the same woman, bare face with the redness and brown patches, the same cream robe, the same bedroom behind her. "
   "Exactly one stick, capped; her right hand holds it, her left hand rests on the vanity edge; both eyes on the lens, brows drawn together, mouth closed. "
   "A real phone photo, soft late-afternoon window light from the left. "
   "No lettering but the stick's own wordmark, no other products, no makeup, no smile, no phone in frame.")),
 "HK2-01": dict(line="Okay, I need to vent. I finally found a foundation that actually matches my redness, and I am sending it back. Here is why.",
  refs=[("FACELOVE bubble mailer (PACKAGING.jpg)", "product", "10c828e4-ae8f-42ab-8b07-596e23f8a323"), ("N-VOICE-IMG-B (confirmed)", "character", "99d3f3a6-e596-4487-9370-82bdbb4ce912")],
  face=True, room=True, product=True, body=True, match=None, edit_of=None,
  motion="From this frame: her hands pull the tape strip across the mailer flap and press it flat, then she looks up at the lens — one pull, about 2 s; phone propped, no camera move.",
  prompt=("For the line — Okay, I need to vent. I finally found a foundation that actually matches my redness, and I am sending it back. Here is why. —: she tapes the FACELOVE mailer shut to send it back. "
   "Seen from the propped phone on her vanity, slightly above, her hands and face both in frame. "
   "Image 1 is the product mailer, copied exactly — the same white bubble mailer with the same violet wordmark, nothing redesigned; the size of a hardback book, lying flat on the white vanity, about a third of the frame wide. "
   "Image 2 is her: the same woman, bare face with the redness and brown patches, the same cream robe, the same bedroom behind her. "
   "Exactly one mailer; her left hand holds its flap down, her right hand pulls a strip of clear tape across it; her eyes lifted to the lens, mouth closed, fed up. "
   "A real phone photo, soft late-afternoon window light from the left. "
   "No lettering but the mailer's own wordmark, bare vanity top, no other products, no makeup, no phone in frame.")),
 "HK3-01": dict(line="Every makeup counter told me nothing would ever match my redness. So why am I returning the one stick that finally did?",
  refs=[("L-COUNTER plate (confirmed)", "location", "0a1ed1e5-3ba1-40cb-b0e9-82858a419537"), ("C1-COUNTER sheet (confirmed)", "character", "399b12ef-dd88-49c2-aaee-db48e4223da8"), ("N-BEFORE v2 sheet (confirmed)", "character", "8861a293-49b2-4f55-b76d-2a2f9a20911b")],
  face=True, room=True, product=False, body=True, match="plate", edit_of="L-COUNTER v1 (Higgsfield job 0a1ed1e5)",
  motion="From this frame: the saleswoman lowers the bottle from her jaw and slowly shakes her head once — about 2 s; phone held still at counter height.",
  prompt=("Keep this photo exactly as it is — Image 1, the makeup counter: the same glossy white counter, glass case, mirror and back wall of nude bottles. "
   "Add, for the line — Every makeup counter told me nothing would ever match my redness. So why am I returning the one stick that finally did? —: the counter woman judging her skin. "
   "Over the saleswoman's right shoulder, from behind the counter, at counter height. "
   "Image 2 is the saleswoman: the same face, sleek black low bun and black tunic; her shoulder and the back of her head fill the left third of the frame. "
   "Image 3 is the customer: the same woman, bare face with blotchy redness on both cheeks, seated on the stool facing us, in a camel coat over a cream sweater. "
   "Exactly two people; the saleswoman holds one unlabelled beige foundation bottle beside the customer's right jaw, where three short beige swatch stripes sit on the red skin, matching nothing; the customer's hands rest in her lap; her eyes on the saleswoman, mouth closed. "
   "No readable text, no logos, no other customers.")),
}
for k, f in F.items():
    call = {"beat": k, "kind": "image", "mode": 1, "prompt": f["prompt"], "script_line": f["line"], "face": f["face"], "room": f["room"], "product": f["product"],
            "body": f["body"], "refs": [{"label": l, "kind": kd} for l, kd, _ in f["refs"]], "match": f["match"], "edit_of": f["edit_of"],
            "taste": ["HT18", "HT19", "HT20", "HT21"] + (["HT17"] if f["match"] else []), "anatomy": False, "pair": ["gpt_image_2_5", "gpt_image_2_5"],
            "motion_plan": f["motion"], "media": [m for _, _, m in f["refs"]]}
    json.dump(call, open(HERE / f"{k}.image.call.json", "w"), indent=1, ensure_ascii=False)
    print(k, len(f["prompt"]))
