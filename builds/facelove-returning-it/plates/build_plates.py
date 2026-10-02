#!/usr/bin/env python3
"""Step-4 plates for facelove-returning-it (§30C, §30G, 16:9 per V7.68.1), assembled from Appendix A by ID (never retyped).
Mode 1: CAM-LOCK → PLATE-PROP / room + PROP-SHELL → anchors → light in room terms → PHYS-FRAME-C → CAP-A → CAP-FILE → negatives.
Empty plates, no people, no product, one render each (Sunburst 2k)."""
import re, json, pathlib
HERE = pathlib.Path(__file__).parent
T = (HERE.parents[2] / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)
WIDE = "A wide 16:9 reference photograph of the whole space."
TAIL = lambda *ids, people="no people": [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
    "AVOID: " + NEGS(*ids, "NEG-M1", "NEG-FILE") + f", {people}, no makeup stick, no cosmetics product in focus, no staged objects, no readable text, no signage, no logos, no brand names"]
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s

# ---- her house (PROP-H) — Property Sheet fields 1-2 ----------------------------------------
PROP_H = {
 "[TYPE AND ERA]": "2000s single-storey stucco ranch-style",
 "[WALL FINISH AND COLOUR]": "smooth drywall painted a warm off-white with a faint orange-peel texture",
 "[SKIRTING]": "plain white baseboards about a hand high",
 "[ARCHITRAVE]": "plain white flat door casings",
 "[INTERNAL DOOR AND HANDLE]": "white two-panel shaker doors with brushed-nickel lever handles",
 "[CEILING]": "a flat white ceiling with a brushed-nickel flush light",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "large warm-beige porcelain floor tiles in the hall, changing to soft oatmeal carpet at the bedroom door",
 "[RADIATOR]": "a white ceiling air vent",
 "[SWITCHES AND SOCKETS]": "white decora rocker switches and outlets",
}
SHELL_H = {
 "[WALL FINISH AND COLOUR]": PROP_H["[WALL FINISH AND COLOUR]"],
 "[SKIRTING — profile, height, colour]": PROP_H["[SKIRTING]"],
 "[ARCHITRAVE]": PROP_H["[ARCHITRAVE]"],
 "[INTERNAL DOOR — style, colour, handle]": PROP_H["[INTERNAL DOOR AND HANDLE]"],
 "[CEILING]": PROP_H["[CEILING]"],
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "soft oatmeal carpet in the bedroom, changing to warm-beige porcelain tile at the door to the hall",
 "[RADIATOR TYPE]": "white ceiling air vents",
 "[SWITCHES AND SOCKETS]": PROP_H["[SWITCHES AND SOCKETS]"],
}
P = {}
P["P-HOME"] = dict(loc="L-HALL", body=[S("CAM-LOCK"), WIDE + " " +
  fill(S("PLATE-PROP"), PROP_H).replace("ranch-style house,", "ranch-style house in a suburb of San Antonio, Texas.")
  .replace(" taken from just inside the front door looking in: the front door and its glass behind the camera, the foot of the staircase rising away on one side, and an open doorway through into another room.", "")
  .replace("through the front door glass and through the open doorway", "through the frosted glass panel beside the front door") +
  " Taken at standing chest height from the end of the front hall, looking at the front door: a solid wood front door stained a warm walnut with a narrow frosted glass panel beside it, "
  "a slim console table against the left-hand wall with a ceramic bowl for keys and a small trailing plant, a round wall mirror with a thin brass frame above the console, "
  "a woven runner rug down the hall tiles, a white door on the right ajar into a bedroom. Named anchors, all fixed: the walnut front door; the round brass mirror over the console; the key bowl; the frosted side panel.",
  "Daylight only: soft morning daylight through the frosted panel beside the front door as the key, a brighter patch on the tiles in front of the door, the near end of the hall a stop darker with soft sensor noise. "
  "The front of the house faces east, so the morning sun is on the door side."] + TAIL("NEG-PROP"))

P["L-VANITY"] = dict(loc="L-VANITY", body=[S("CAM-LOCK"), WIDE + " " +
  "A single photograph of the main bedroom of the same " + PROP_H["[TYPE AND ERA]"] + " house, taken from the top of a white bedroom vanity desk at seated head height, looking back across the room at the chair she sits in: "
  + fill(S("PROP-SHELL"), SHELL_H) +
  " Named anchors, all fixed: a white upholstered vanity chair with a low curved back in the middle of the frame, close to the camera; behind it the end of a made bed with a cream knit throw and two linen pillows; "
  "a tall window on the left-hand wall with sheer white curtains; a framed abstract print in soft clay and sand colours above the bed with no figures; a cream ceramic table lamp, switched off, on a nightstand on the right; "
  "a fluffy cream rug on the carpet. Along the bottom edge of the frame, the near edge of the white vanity top with a jar of cotton pads and a small tray, out of focus.",
  "Late-afternoon daylight through the sheer curtains of the window on the left-hand wall as the key, about forty-five degrees to the camera, soft and warm, falling across the chair and the bed, the right-hand side of the room a stop darker with soft sensor noise. "
  "The window faces west. Daylight only, the lamp off."] + TAIL("NEG-PROP"))

P["L-COUNTER"] = dict(loc="L-COUNTER", body=[S("CAM-LOCK"), WIDE + " " +
  "A single photograph inside the beauty hall of an ordinary American department store in a mall on a weekday afternoon, taken at head height from the customer side of a makeup counter: "
  "a white glossy counter with a glass display case of plain unlabelled foundation bottles and compacts, a tall stool on the customer side, a lit makeup mirror on a stand on the counter, "
  "a tray of white sponges and a row of brushes in a cup, behind the counter a back wall of shelves with rows of unlabelled bottles in nude and beige shades, plain white panels where any sign would be, "
  "the next counters of the beauty hall soft in the background. Named anchors, all fixed: the glossy white counter with the glass case; the stool; the mirror on its stand; the back wall of nude bottles.",
  "Bright cool-white store downlights from the ceiling as the key, the counter top shining, the lit mirror adding a soft frontal wash on the counter, the far counters a stop darker with mild sensor noise."] + TAIL("NEG-SCENE"))

P["L-CAFE"] = dict(loc="L-CAFE", body=[S("CAM-LOCK"), WIDE + " " +
  "A single photograph inside a small neighbourhood café in San Antonio at midday, taken at seated head height from one chair of a round table by the front window: "
  "a round light-oak table with four bentwood chairs, on it three iced coffees in clear cups, a flat white in a ceramic cup and a plate with a half-eaten pastry; "
  "a big front window on the left with the street and parked cars soft outside; exposed brick on the back wall, a counter with a pastry case and hanging pendant lights in the background, a few potted plants on the windowsill. "
  "Named anchors, all fixed: the round oak table by the window; the three iced coffees and the flat white; the brick back wall; the window on the left.",
  "Bright midday daylight through the big front window on the left as the key, falling across the table, the brick wall behind a stop darker, the pendant lights off, highlights clipping on the cups and the window frame."] + TAIL("NEG-SCENE"))

P["L-FRONT"] = dict(loc="L-FRONT", body=[S("CAM-LOCK"), WIDE + " " +
  "A single photograph of the front of her house, a " + PROP_H["[TYPE AND ERA]"] + " house in a suburb of San Antonio, Texas, on a clear morning, taken at head height from the front path a few steps from the door: "
  "cream stucco walls, a terracotta tile roof edge, a small covered entry with the walnut front door and a narrow frosted glass panel beside it, a terracotta pot with a rosemary bush by the step, "
  "a concrete path from the door down past a low xeriscape bed of gravel and agave to the driveway on the right, where a silver crossover SUV is parked. Named anchors, all fixed: the walnut front door; the rosemary pot by the step; the concrete path; the silver SUV in the drive.",
  S("LOC-EXT-SUN")] + TAIL("NEG-SCENE"))

if __name__ == "__main__":
    out = {}
    for k, v in P.items():
        p = "\n\n".join(v["body"]); out[k] = dict(loc=v["loc"], prompt=p)
        (HERE / f"{k}.prompt.txt").write_text(p); print(k, len(p))
    json.dump(out, open(HERE / "plates.json", "w"), indent=1, ensure_ascii=False)
