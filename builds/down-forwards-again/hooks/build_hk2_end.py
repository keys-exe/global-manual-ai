#!/usr/bin/env python3
"""HK2-02a END frame (§27G rule 5, pin_end, §22V Q6): the confirmed v3 start frame, the strap now seated on the patellar tendon
(Product Sheet PLACE_LOCK, left knee), both hands lifting away. Same camera, room, light and wardrobe."""
import json, pathlib, importlib.util
here = pathlib.Path(__file__).parent; ROOT = here.parents[2]
spec = importlib.util.spec_from_file_location("ps", ROOT / "products/stryde/stryde_product_sheet.py"); ps = importlib.util.module_from_spec(spec)
try: spec.loader.exec_module(ps)
except AssertionError: pass
p = json.load(open(here / "hooks_v3.json"))["HK2-02a"]["prompt"]
a = p.index("The strap is already fully formed and closed"); b = p.index("Her face at the top of the frame")
end = ("THE SAME MOMENT THREE SECONDS LATER, the same camera, same framing and same light as the attached start frame: the strap has been slid up her shin and is now SEATED. "
       + ps.fill(ps.PLACE_LOCK, "left") + " Both hands are just lifting away from the shell's two sides, fingertips a centimetre off it, the job done. ")
p = p[:a] + end + p[b:]
p = p.replace("no strap already under the kneecap, no strap seated yet,", "no strap still at mid-shin, no strap on the kneecap, no hands gripping the strap,")
p = p.replace("She is putting her knee strap on.", "She has just put her knee strap on.")
(here / "HK2-02a.end.prompt.txt").write_text(p)
json.dump({"HK2-02a-END": {"model": "nano_banana_pro", "refs": ["HK2-02a v3 (start frame)", "front.webp", "W-L-FRONT", "P-PATIENT"],
  "ref_jobs": ["dd2add6c-2681-4176-8877-4d9cbd5eb04c", "c942d91d-718d-4723-b190-ad85186ac8d9", "793ca329-e4b3-49fd-943c-5e97bae5366d", "02333782-0c9a-4696-b3f1-fcc7480fe8db"],
  "chars": len(p), "prompt": p}}, open(here / "hk2_end.json", "w"), indent=1)
print(len(p))
