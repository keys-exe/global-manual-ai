#!/usr/bin/env python3
"""New B-rolls on doctor-only lines (user 2026-10-01: "there is a band of tendon about as wide as your thumb — THIS LINE AND ALSO CHECK THE OTHER
SCRIPT LINES IF IT CAN BE ADDED A BROLL"). Build lock (§18A step 2): nano_banana_pro, one render each (this build predates the A/B pair; CLAUDE.md:
existing boards get the pair only on their team's ask). Short §6A prompts — the BR-10c lesson: short targeted edits land, long prompts drift."""
import json, pathlib
here = pathlib.Path(__file__).parent
REF = {"BR-04 v9": "7527b4ef-2b3e-43c6-b59f-5e39cb223893", "BR-11b": "fa5442a9-ed51-4c45-9e00-b0da971e9e0e",
       "P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P1-P-FRONTROOM v2": "d0eeaf2a-abad-4a79-a9da-624c5eef41a1",
       "front.webp": "c942d91d-718d-4723-b190-ad85186ac8d9"}
B = {}
B["BR-03b"] = dict(line="there is a band of tendon about as wide as your thumb.", act="Act 1",
  refs=[("BR-04 v9", "frame")], match="frame", edit_of="BR-04 v9", product=False, face=False, room=True,
  taste=["HT06"], motion="From this frame: her thumb settles flat across the band under the kneecap and rests there; the knee stays still.",
  prompt=("For the line \"there is a band of tendon about as wide as your thumb.\": keep this photo (Image 1) exactly as it is, and show her own thumb laid flat across that band, just below her kneecap, exactly as wide as it. Keep the framing, her bent left knee head-on, her rust jersey sleeve and gold wedding band, the camel corduroy skirt, the mustard armchair, the rug, the room and the light. "
  "Change only her right hand: her thumb now lies flat and crosswise on the front of the knee, in the soft band directly below the bottom edge of the kneecap, the thumbnail facing the lens, "
  "the thumb's width covering that band from its top edge to its bottom edge. Her other four fingers curl loosely round the outer side of the knee. "
  "The kneecap sits just above the thumb, fully visible. Her hand stays the same hand as in the photo: pale, slightly freckled, sixty-nine years old. "
  "The knee and thumb fill about a third of the frame, in sharp focus.\n\n"
  "Avoid: no fingertip pressing, no thumb on the kneecap, no second hand on the knee, no text."))
B["BR-18"] = dict(line="because it is the cheapest thing on the list and the only one aimed at the band.", act="Act 4",
  refs=[("BR-11b", "frame"), ("front.webp", "product")], match="frame", edit_of="BR-11b", product=True, face=False, room=True,
  taste=["FP01", "FP02", "FP11", "FP12", "HT06"], motion="From this frame: the camera eases in a little towards the small strap at the end of the row; nothing on the table moves.",
  prompt=("For the line \"because it is the cheapest thing on the list and the only one aimed at the band.\": keep this photo (Image 1) exactly as it is, and show everything she tried in a row on her kitchen table, the small strap at the end of it. Keep the kitchen table, the room, the light and the camera angle. On the table, in one neat row from left to right: "
  "a grey knit knee sleeve, the hinged knee brace already in the photo, a white tube of gel, and last, the Stryde strap from Image 2, copied exactly: same rigid moulded shell, black knit band, slides and wordmark, nothing redesigned. "
  "True sizes: the strap's shell is 12 by 5 cm, smaller than the gel tube and far smaller than the brace; the strap lies flat with the shell facing up, about a quarter of the frame wide. "
  "The four things fill the width of the frame, all in sharp focus; every other surface bare.\n\n"
  "Avoid: no hands, no text, no price tags, no second strap."))
B["BR-21"] = dict(line="You cannot strengthen your way out of a load problem.", act="Act 5",
  refs=[("P-PATIENT", "character"), ("P1-P-FRONTROOM v2", "location")], match=None, edit_of=None, product=False, face=True, room=True,
  taste=["HT06"], motion="From this frame: she lifts her left leg straight against the band once and lowers it slowly; she stays seated.",
  prompt=("Line: \"You cannot strengthen your way out of a load problem.\" The picture shows her doing her strengthening exercise, trying hard, and it not being the answer.\n\n"
  "A photo on an ordinary phone, held at seated eye height, three-quarter front. The woman is exactly the woman in Image 1: same face, age, hair and build. "
  "She wears a rust-coloured long-sleeve jersey top, a knee-length camel corduroy skirt with bare legs, and bare feet. "
  "She sits upright in the mustard armchair of the front room in Image 2, which stays exactly as it is. A green exercise band is looped round both ankles. "
  "She holds her left leg out straight against the band, a hand's height off the rug, her right foot flat on the floor, both hands gripping the chair arms. "
  "She is looking down at her left knee, her jaw set with effort, determined, not sad. She fills about half the frame, whole body in frame from hair to bare feet. "
  "Grey morning daylight from the window on the left.\n\n"
  "Avoid: no strap on either knee, no weights, no second person, no text."))
calls = []
for i, (beat, o) in enumerate(B.items()):
    assert len(o["prompt"]) <= 1200, (beat, len(o["prompt"]))
    (here / f"{beat}.image.prompt.txt").write_text(o["prompt"])
    pf = {"beat": beat, "kind": "image", "mode": 1, "prompt": o["prompt"], "script_line": o["line"], "face": o["face"], "room": o["room"],
          "product": o["product"], "body": beat != "BR-18", "refs": [{"label": l, "kind": k} for l, k in o["refs"]], "match": o["match"],
          "edit_of": REF[o["edit_of"]] if o["edit_of"] else None, "taste": o["taste"], "anatomy": False,
          "pair": ["nano_banana_pro", "nano_banana_pro"],
          "alt_reason": "build step-2 lock (§18A): this build's images run on nano_banana_pro, one render — no Sunburst switch on a running build (CLAUDE.md, V7.72 new builds only)"}
    json.dump(pf, open(here / f"{beat}.preflight.json", "w"), ensure_ascii=False, indent=1)
    calls.append({"beat": beat, "params": {"model": "nano_banana_pro", "aspect_ratio": "9:16", "resolution": "2k", "count": 1, "use_unlim": False,
                  "medias": [{"role": "image_references", "value": REF[l]} for l, _ in o["refs"]], "prompt": o["prompt"]}})
    print(beat, len(o["prompt"]))
json.dump({k: {kk: v for kk, v in o.items() if kk != "prompt"} for k, o in B.items()}, open(here / "beats.json", "w"), ensure_ascii=False, indent=1)
json.dump(calls, open(here / "calls.json", "w"), ensure_ascii=False, indent=1)
