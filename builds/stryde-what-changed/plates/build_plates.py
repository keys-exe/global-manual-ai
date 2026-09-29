#!/usr/bin/env python3
"""Step-4 plates for stryde-what-changed (§30C, §30G, §30K), assembled from Appendix A by ID (never retyped).
Plates are 16:9 (V7.68.1); everything made against them stays 9:16."""
import re, json, pathlib
MASTER = pathlib.Path(__file__).resolve().parents[3] / "standards/AI_Prompt_Engineer_Global_Standards.md"
T = MASTER.read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    return m.group(1).strip()
NEGS = lambda *ids: ", ".join(S(i) for i in ids)
TAIL = lambda *ids: [S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
                     "AVOID: " + NEGS(*ids, "NEG-M1", "NEG-FILE") + ", no people, no product, no staged objects, no readable text or signage"]
def fill(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:200]; return s
WIDE = "A wide 16:9 landscape photograph."

P = {}
# ---- the podcast set (H-HOST) -------------------------------------------------------------
P["P0-STUDIO"] = dict(loc="L-STUDIO", body=[S("CAM-LOCK"), WIDE +
  " The corner of a converted Victorian warehouse flat in east London used as a small podcast studio, taken from where the camera tripod stands, at seated eye height, about three metres back: "
  "a long wall of exposed London stock brick, yellow-grey and uneven with darker mortar, runs across the back of the frame; on the left a tall black steel-framed factory window with small panes, "
  "its sill deep and painted white; in the middle of the frame, against the brick, a worn cognac-brown leather chesterfield sofa with buttoned back and rolled arms, its seat cushions creased and dipped with use, "
  "a folded mustard wool throw over its right arm; behind the sofa's right end a tall black tripod floor lamp with a big bare globe bulb, switched off; to the right of the sofa a small round dark-wood side table with a black "
  "podcast microphone on a black articulated boom arm clamped to it, the arm reaching in towards the sofa at head height, a mug and a closed notebook beside it; a faded Persian-pattern rug in rust and navy on dark "
  "stained floorboards in front of the sofa; a tall fiddle-leaf fig in a terracotta pot by the window; a low shelf of records and books along the right-hand wall, their spines unreadable. Empty — nobody on the sofa.",
  "Daylight only, from the tall window on the left: a soft broad key falling across the sofa from the left at about sixty degrees to the camera axis, bright on the left arm and cushions, falling off to the right, "
  "the right-hand end of the room a stop darker with soft sensor noise; the window panes blow out to white. Overcast late-morning daylight, neutral to slightly cool. The window faces north-west."] + TAIL("NEG-SCENE"))

# ---- Maureen's house (PROP-M) — Property Sheet fields 1-2 ----------------------------------
PROP_M = {
 "[TYPE AND ERA]": "1930s pebble-dashed semi-detached",
 "[WALL FINISH AND COLOUR]": "smooth painted walls in pale duck-egg blue",
 "[SKIRTING]": "tall ogee-profile skirting painted white satin, scuffed along the bottom stair",
 "[ARCHITRAVE]": "moulded white architraves",
 "[INTERNAL DOOR AND HANDLE]": "1930s-style glazed oak doors with brass lever handles",
 "[CEILING]": "a white ceiling with a pleated fabric lampshade",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "a worn oatmeal wool carpet through the hall and up the stairs, changing to a black-and-white chequerboard vinyl at the kitchen doorway",
 "[RADIATOR]": "a white double-panel radiator under the stairs",
 "[SWITCHES AND SOCKETS]": "white plastic switches and a white telephone socket",
}
P["P1-PROP-M"] = dict(loc="L-M-STAIRS", body=[S("CAM-LOCK"), WIDE + " " + fill(S("PLATE-PROP"), PROP_M) +
  " The staircase rises straight up along the right-hand wall of the hall, open on its left side with plain white-painted spindles and a honey-coloured oak handrail ending in a square newel post at the bottom step, "
  "a half-landing window at the top of the flight; at the far end of the hall a doorway on the left opens into the kitchen, its chequerboard floor just visible. Near the door: a small half-moon hall table with a bowl for keys, "
  "a blue-and-white china vase with dried lavender, a coat stand with a navy raincoat and a straw sunhat, a pair of gardening shoes on a mat. A barometer hangs at the foot of the stairs.",
  "Daylight only: the front door's leaded glass panel behind the camera washes the hall carpet, the half-landing window lights the top of the stairs from above, and the middle of the hall sits a stop darker with soft sensor noise. "
  "The front faces east, so on a morning the hall is bright from the door glass."] + TAIL("NEG-PROP"))

# ---- Desmond's house (PROP-D) ----------------------------------------------------------------
PROP_D = {
 "[TYPE AND ERA]": "late-Edwardian red-brick terraced",
 "[WALL FINISH AND COLOUR]": "painted walls in warm mid-grey",
 "[SKIRTING]": "deep square skirting painted bright white gloss",
 "[ARCHITRAVE]": "plain wide white architraves",
 "[INTERNAL DOOR AND HANDLE]": "white-painted four-panel doors with chrome knob handles",
 "[CEILING]": "a white ceiling with a simple glass pendant",
 "[FLOOR AND WHAT IT CHANGES TO AT THE THRESHOLD]": "light oak laminate through the hall, changing at the foot of the stairs to a charcoal-grey stair carpet with a white stripe at each nosing",
 "[RADIATOR]": "a white column radiator by the door",
 "[SWITCHES AND SOCKETS]": "brushed chrome switches and sockets",
}
P["P2-PROP-D"] = dict(loc="L-D-STAIRS", body=[S("CAM-LOCK"), WIDE + " " + fill(S("PLATE-PROP"), PROP_D) +
  " The staircase rises straight up along the left-hand wall of the hall, open on its right side with square white spindles and a dark-stained handrail; up the stair wall hangs a staggered line of black-framed "
  "photographs of amateur football teams in rows, the players too small to read; at the far end a doorway on the right into the front room. Near the door: a shoe rack with a pair of old boots, a hook with a navy club scarf "
  "with no crest, a small table with post and keys.",
  "Daylight only: the frosted front-door glass behind the camera lights the hall floor, a small window at the top of the stairs lights the upper steps, the middle of the hall a stop darker with soft sensor noise. "
  "The front faces south-west, so by afternoon the hall is warm from the door glass."] + TAIL("NEG-PROP"))

# ---- the pavement (HK3) ------------------------------------------------------------------------
P["P3-STREET"] = dict(loc="L-STREET", body=[S("CAM-LOCK"), WIDE +
  " A residential street in a south-east English town on a weekday, taken at knee height from the edge of the pavement: a long grey paving-slab pavement running away, cracked and patched in places, "
  "low front-garden walls and privet hedges on the right, parked cars along the kerb on the left, a lamppost and a green wheelie bin at a gate, a row of 1930s semis with bay windows going away into the distance. "
  "No house numbers, no readable signs.",
  S("LOC-EXT-OVERCAST")] + TAIL("NEG-SCENE"))

# ---- the kitchen (B10, B22) ----------------------------------------------------------------------
P["P4-KITCHEN"] = dict(loc="L-KITCHEN", body=[S("CAM-LOCK"), WIDE +
  " A lived-in family kitchen in a British 1990s house, taken from the doorway: a square pale-oak table in the foreground with three mismatched chairs, a window over the sink on the far wall, sage-green shaker units "
  "and a speckled grey worktop along it, an open shelf of mugs and jars on the right-hand wall. Named anchors, all fixed: the oak table with a linen runner and a jug of garden flowers; a kettle and a bread bin on the worktop; "
  "a radio on the windowsill; a calendar on the side of a unit with no readable writing.",
  S("LOC-KITCHEN-DAY")] + TAIL("NEG-SCENE"))

# ---- the consulting room (B16) ---------------------------------------------------------------------
P["P5-CONSULT"] = dict(loc="L-CONSULT", body=[S("CAM-LOCK"), WIDE +
  " An orthopaedic consulting room in a British private clinic, taken from just inside the door: a small, practical room. The window on the left-hand wall with a white roller blind half down, a pale wood desk under it "
  "facing into the room with a computer monitor turned away, an examination couch in grey vinyl with a paper roll against the right-hand wall. Named anchors, all fixed: a life-size anatomical knee model on the desk; "
  "a wall-mounted lightbox, switched off; a pair of crutches leaning in the corner; a hand-gel dispenser; a framed botanical print. Grey vinyl floor, off-white walls with scuffs at chair height.",
  "Soft daylight through the half-lowered blind on the left-hand wall as the key, falling across the desk and fading towards the couch, a flat overhead panel light on and doing little. The window side a stop brighter, "
  "mild sensor noise in the far corner. Ambient palette cool neutral."] + TAIL("NEG-SCENE"))

if __name__ == "__main__":
    out = {}
    for k, v in P.items():
        p = "\n\n".join(v["body"]); out[k] = dict(loc=v["loc"], prompt=p)
        pathlib.Path(f"{k}.prompt.txt").write_text(p); print(k, len(p))
    json.dump(out, open("plates.json", "w"), indent=1)
