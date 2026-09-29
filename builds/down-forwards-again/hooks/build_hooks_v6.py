#!/usr/bin/env python3
"""Step 6 hook frame HK1-02c v4 — the user's board Fix note, 2026-09-29 ~12:45 UTC: "she should never put that strap on that drawer".
Keeps the earlier brief (the strap sharp, the braces behind): the STRYDE strap lies apart on the kitchen table, sharp in the foreground;
behind it, soft, she tips the whole drawer of old braces into a black bin bag — no more braces going in the drawer. The strap never touches the drawer.
Helpers and shared strings come from build_hooks.py (v1)."""
import re, json, pathlib, importlib.util
here = pathlib.Path(__file__).parent
src = (here / "build_hooks.py").read_text()
exec(compile(src[:src.index("\nB = {}")].replace("__file__", repr(str(here / "build_hooks.py"))), "build_hooks.py", "exec"))
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
P_D1 = ("She wears a cream fine-knit roll-neck under an oatmeal cable-knit cardigan buttoned once, a knee-length plum wool skirt with bare legs, "
        "and reading glasses on a cord round her neck.")
B = {}
B["HK1-02c"] = dict(model="nano_banana_pro", refs=["front.webp", "product_tq_left.jpg", "P2-P-KITCHEN v2", "P-PATIENT"], prompt="\n\n".join([S("CAM-LOCK"),
  angle("low", "the front", "the strap on the table, with her behind it"),
  focus("the product and its wordmark", "the room behind falls to a soft, recognisable shape"),
  PROPREF + " The kitchen of the attached kitchen photograph: the pine farmhouse table in the foreground, the old pine Welsh dresser behind it.",
  "A snapshot from a phone resting low on the edge of the pine table, not looking at the screen. In the near foreground, lying flat on the bare pine tabletop on its own, "
  "nothing else near it, sharp and filling the lower middle of the frame, front face up and square to the lens: her knee strap. " + ps.REF_PROD +
  " the band laid in a loose closed loop behind the shell. "
  "Behind it, soft and out of focus beyond the table: the woman of sixty-nine from the attached reference sheet — " + P_D1.replace("She wears ", "wearing ").rstrip(".") +
  " — stands at the dresser holding a black bin bag open under the dresser's top drawer, which she has pulled right out and tipped up, "
  "caught in the moment the whole heap of old knee supports — black sleeves, beige wraps, a grey hinged brace with metal side bars — slides out of the drawer into the bin bag, "
  "a sleeve and a wrap in mid-air between drawer and bag. Her face is soft, turned to the bag, calm and done with it, mouth shut.",
  light("The window over the sink on the room's west wall", "the table and the strap", "right", "flat overcast daylight", "the right", face=False),
  S("CAP-FILE"),
  "AVOID: " + ", ".join([pick("NEG-M1", "no AI face", "no plastic skin", "no extra fingers", "no fused fingers", "no melted hands", "no CGI look", "no fake commercial gloss", "no moody dark grade"),
                         pick("NEG-LIGHT", "no glowing skin", "no shadows falling in two directions", "no lens flare"),
                         "no strap in the drawer, no strap in the bin bag, no strap in her hands, no strap on her knee, no second strap, no braces on the table, "
                         "no sharp background, no packaging, no strap tipped on its side with the wordmark vertical",
                         NOTEXT.replace("anywhere", "anywhere except the stryde wordmark on the strap")])]))
REF = {"P-PATIENT": "02333782-0c9a-4696-b3f1-fcc7480fe8db", "P2-P-KITCHEN v2": "abc2c220-b0f0-43d2-b583-d22b5696225b",
       "front.webp": "c942d91d-718d-4723-b190-ad85186ac8d9", "product_tq_left.jpg": "4a56cffe-69bc-4f77-ac90-38258b124e65"}
out = {}
for k, b in B.items():
    txt = b["prompt"]; assert "[" not in txt, (k, txt[txt.index("["):txt.index("[")+80])
    out[k] = dict(model=b["model"], refs=b["refs"], ref_jobs=[REF[r] for r in b["refs"]], chars=len(txt), prompt=txt)
    (here / f"{k}.image.v6.prompt.txt").write_text(txt); print(f"{k:8s} {len(txt):5d}  {b['model']:15s} refs: {', '.join(b['refs'])}")
json.dump(out, open(here / "hooks_v6.json", "w"), indent=1)
