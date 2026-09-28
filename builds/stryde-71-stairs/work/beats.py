#!/usr/bin/env python3
"""stryde-71-stairs — beat T2I prompts (step 6/7), assembled from Appendix A and the Product Sheet by ID.

Order per §30E Part 3 / §30I–§30K: CAM-LOCK → ANGLE-LINE → FOCUS-LINE → PROP-REF/PROP-SHELL → SUBJ-REF → the beat's frame
(caught mid-action, §27G rule 4) → wardrobe → skin → LIGHT-SHOT → BROLL-REAL → PHYS-FRAME-C → CAP-A → CAP-FILE →
AVOID (NEG-SUBJ, NEG-PROP, NEG-LIGHT, NEG-M1, NEG-FILE, beat negatives).
Usage: beats.py HK-01a HK-02a …   → work/prompts/<beat>.t2i.txt + work/prompts/<beat>.refs.json
"""
import re, json, sys, pathlib
HERE = pathlib.Path(__file__).parent
ROOT = HERE.parents[2]
T = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
def S(i):
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n+```\n(.*?)\n```" % re.escape(i), T, re.S)
    if not m: raise KeyError(i)
    return m.group(1).strip()
ROWS = {r["beat"]: r for r in json.load(open(HERE / "actmap_rows.json"))}

HEIGHT = {"ground": "the lens a few centimetres off the floor, looking along it and slightly up",
          "low": "the lens at hip height, looking up at the subject", "eye": "the lens at the subject's eye height, level",
          "high": "the lens above head height, looking down at the subject", "overhead": "the lens directly above, looking straight down"}
SIDE_W = {"front": "the front", "three-quarter": "a three-quarter angle", "profile": "the side, in profile",
          "three-quarter-back": "a three-quarter angle from behind", "behind": "directly behind", "ots": "over the near shoulder"}

# Confirmed plates and sheets (Higgsfield job ids = reference media)
JOB = {"N": "5d4f7598-14d9-4e53-8173-bb48b516e54a", "C1": "cf777e26-5d0f-4fae-9063-116f20e27ffd", "C2": "61ff6760-6aba-4054-aaf5-31b7a67c6cd9",
       "P0": "237b6320-5f42-434a-826b-ce58c49024d2", "P5": "2b888662-9dc3-4a44-a0c4-4a909cef79e5", "P1": "2cc80516-284f-4355-92df-61e009c28d4d", "P2": "2d997177-d22f-4743-b215-7fafbd6e06be",
       "P8": "8b47c878-021a-4f21-b887-9ca63b1b1379"}
PROP_N_CARRIED = ("warm greige walls, plain white baseboards, white six-panel doors with round brass knobs, honey-coloured oak floors, "
                  "the worn beige stair runner, white balusters under a dark-stained oak handrail with a square dark newel, and the stair wall "
                  "hung with black-and-white and sepia family portraits in dark wooden frames")
PROP_N_SHELL = {
 "[WALL FINISH AND COLOUR]": "painted drywall in a warm greige, scuffed at hip height along the stairs",
 "[SKIRTING — profile, height, colour]": "plain white baseboards about ten centimetres high",
 "[ARCHITRAVE]": "simple colonial-profile white door casings",
 "[INTERNAL DOOR — style, colour, handle]": "white six-panel doors with round brass knobs",
 "[CEILING]": "a white ceiling with a brass-and-frosted-glass flush light",
 "[FLOOR, AND WHAT IT CHANGES TO AT THE THRESHOLD]": "honey-coloured oak floorboards, changing to worn beige carpet on the stairs and the upstairs landing",
 "[RADIATOR TYPE]": "floor air-vent grilles",
 "[SWITCHES AND SOCKETS]": "ivory plastic rocker switches and outlets",
}
SUBJ = {
 "N": dict(name="her", markers="short grey natural hair in tight curls, fuller on top, a wide face with heavy-lidded dark brown eyes, a small cluster of dark raised spots high on her left cheek, medium height and full through the hips",
           skin="a Black American woman of seventy-one, deep brown skin, deep laugh folds, fine creases at the eyes"),
 "C2": dict(name="the daughter", markers="long dark box braids pulled back in a low ponytail, a round face with full cheeks and straight thick brows, a small crescent scar on her chin, sturdy build",
            skin="a Black American woman in her mid-forties, medium-deep brown skin, fine lines at the eye corners"),
}
WARD = {
 "N-D4": "an emerald-green church dress falling to mid-calf, so her knees are covered, and low black pumps",
 "C2": "a heather-grey crewneck sweatshirt, mid-blue jeans and white trainers",
}

def fillp(s, d):
    for k, v in d.items(): s = s.replace(k, v)
    assert "[" not in s, s[:160]; return s

def angle_line(r, subject):
    a = r["angle"]
    fg = {"clean": "", "through": ", looking past the white balusters, soft in the near foreground", "reflection": ", seen in reflection"}[a["fg"]]
    return (S("ANGLE-LINE").replace("[HEIGHT CLAUSE from §30I]", HEIGHT[a["height"]]).replace("[SIDE]", SIDE_W[a["side"]])
            .replace("[SUBJECT]", subject).replace("[, looking past FOREGROUND, soft in the near foreground | , seen in REFLECTION]", fg))

def focus_line(r, name):
    f = r["focus"]
    plane = {"eyes": "the nearest eye of " + name, "hands": "the hands and what they hold", "product": "the product and its wordmark",
             "foreground": "the foreground", "background": "the background", "deep": "everything"}[f["plane"]]
    depth = ("everything from near to far stays sharp" if f["dof"] == "deep" else "the room behind falls to a soft, recognisable shape")
    return (S("FOCUS-LINE").replace("[PLANE — the nearest eye of NAME / the hands and what they hold / the product and its wordmark / the foreground / everything]", plane)
            .replace("[DEPTH — the room behind falls to a soft, recognisable shape | everything from near to far stays sharp]", depth))

def light_line(r, subject, quality):
    side = {"L": "left", "R": "right", "back": "back", "front": "front"}[r["light"]["key_side"]]
    return (S("LIGHT-SHOT").replace("[SOURCE from the light plan — the window on the room's WALL, or the named practical]", "the " + r["light"]["source"])
            .replace("[SUBJECT]", subject).replace("[SCREEN SIDE]", side).replace("[TIME-OF-DAY QUALITY and the act's light state]", quality)
            .replace("[SIDE]", side))

def tail(extra):
    return [S("BROLL-REAL"), S("PHYS-FRAME-C"), S("CAP-A"), S("CAP-FILE"),
            "AVOID: " + ", ".join([S("NEG-SUBJ"), S("NEG-PROP"), S("NEG-LIGHT"), S("NEG-M1"), S("NEG-FILE"), extra])]

BEATS = {}

def hk_01a():
    r = ROWS["HK-01a"]; n, d = SUBJ["N"], SUBJ["C2"]
    body = [S("CAM-LOCK"),
     angle_line(r, "the two women climbing the stairs"), focus_line(r, "the mother"),
     S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_N_CARRIED) + " " + fillp(S("PROP-SHELL"), PROP_N_SHELL),
     "THE HALL AND STAIRS of the attached property reference, seen from the hall floor at the foot of the straight open flight, looking up the stairs from a little behind and to the open side: "
     "the photo wall on the right running up with the flight, the white balusters and dark oak handrail on the left, the landing window bright at the top.",
     "TWO PEOPLE, each exactly as in their attached reference sheet. THE MOTHER, higher up the stairs: " + n["markers"] + ". THE DAUGHTER, two steps below and behind her: " + d["markers"] + ". Unchanged in face, age and build.",
     "Caught mid-climb, seen from behind and below at a three-quarter angle: the mother is ahead, about two-thirds of the way up the flight, taking the stairs briskly — her right foot planted on the step above and her weight already moving up onto it, "
     "her left heel just lifting off the step below, her right hand only brushing the handrail, head up, turned a little so her cheek and the side of her smile show. "
     "Directly behind her on the same flight, two steps lower, the daughter is working to keep up: both feet on the carpet runner of the stairs, inside the handrail, right at her mother's back and following in her line, "
     "one hand gripping the rail, leaning into the climb, looking up after her mother, a little out of breath — the daughter is already on the stairs, not on the hall floor and not beside the banister. "
     "Both women are on the carpeted treads, one behind the other. Waist-up to full length as the stairs allow; both women whole in the frame.",
     "THE MOTHER is wearing " + WARD["N-D4"] + ". THE DAUGHTER is wearing " + WARD["C2"] + ".",
     "Real unretouched skin: the mother " + n["skin"] + "; the daughter " + d["skin"] + ".",
     light_line(r, "the two women and the stairs", "Sunday afternoon sun through the front door's sidelights behind the camera, warm and clear — the after state, never moody"),
     *tail("no face turned fully to camera, no product visible, no knee strap visible, no walking stick, no stairlift, no third person, no different staircase from the property reference, no enclosed stairwell, no turn in the stairs, no one standing on the hall floor, no one outside the banister, no daughter beside or ahead of her mother")]
    refs = [("N sheet", JOB["N"]), ("C2 sheet", JOB["C2"]), ("P0-PROP-N plate", JOB["P0"])]
    return dict(model="nano_banana_2", refs=refs, body=body)
BEATS["HK-01a"] = hk_01a

def hk_02a():
    r = ROWS["HK-02a"]; d = SUBJ["C2"]
    body = [S("CAM-LOCK"),
     angle_line(r, "the daughter on the stairs"), focus_line(r, "the daughter"),
     S("PROP-REF").replace("[THE CARRIED FINISHES, NAMED IN ONE CLAUSE]", PROP_N_CARRIED),
     "THE TOP OF THE STAIRS exactly as in the attached landing photo: seen from the upstairs landing looking straight down the straight open flight — the photo wall on the left running down with the flight, "
     "the white balusters and dark oak handrail on the right, the hall's oak floor and the front door with its glass sidelights at the bottom.",
     S("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", d["markers"]),
     "Caught arriving: the daughter is three steps from the top, coming up toward the camera — her right foot on the next step and her weight moving up onto it, her right hand on the handrail, "
     "her face lifted toward the lens with a surprised, delighted, slightly out-of-breath look, mouth just opening as if to speak. Chest-up to waist-up, the flight dropping away behind her.",
     "She is wearing " + WARD["C2"] + ".",
     "Real unretouched skin: " + d["skin"] + ", visible pores, a light sheen on the forehead from the climb.",
     light_line(r, "her face and the stairs", "Sunday afternoon sun through the front door's sidelights at the bottom of the flight and soft daylight from the landing window behind the camera — the after state, warm and clear"),
     *tail("no second person in frame, no product visible, no knee strap, no enclosed stairwell, no turn in the stairs, no different staircase from the landing photo, no different photographs on the wall")]
    refs = [("C2 sheet", JOB["C2"]), ("P1-LANDING plate v3", JOB["P1"]), ("P0-PROP-N plate", JOB["P0"])]
    return dict(model="nano_banana_2", refs=refs, body=body)
BEATS["HK-02a"] = hk_02a

MALL_PLATE = ("THE MALL STAIRCASE exactly as in the attached location photo: the wide straight open staircase of pale terrazzo steps with brushed-steel handrails and glass balustrade panels "
              "rising to the upper-level walkway, the up escalator running right beside it, shopfronts on both levels with plain coloured panels and no readable lettering, the atrium skylight above")
MALL_Q = "soft Sunday-afternoon daylight from the atrium skylight, warm and clear — the after state, never moody"

def hk_01b():
    r = ROWS["HK-01b"]; n = SUBJ["N"]
    body = [S("CAM-LOCK"),
     angle_line(r, "the woman climbing the mall staircase"), focus_line(r, "her"),
     MALL_PLATE + " — seen from the ground-floor concourse at the foot of the stairs, a little to the escalator side.",
     S("SUBJ-REF").replace("[two or three named markers: hair, build, one distinctive feature]", n["markers"]),
     "Caught mid-climb on a Sunday afternoon after church: she is halfway up the mall staircase, taking the stairs briskly — her right foot planted on the step above, her weight already moving up onto it, her left heel lifting off the step below, "
     "her right hand free above the steel handrail, not touching it, a small shopping bag in her left hand, head up, a small proud smile. Right beside the stairs, on the up escalator, two younger women in their thirties are standing still, riding it, "
     "one holding the escalator's rubber handrail and looking at her phone — the woman on the stairs is drawing level with them and about to pass them. All three whole in the frame.",
     "She is wearing " + WARD["N-D4"] + ". The two younger women (one-off extras, thirties) wear casual weekend clothes — jeans, a denim jacket, a cream knit top — and trainers.",
     "Real unretouched skin: " + n["skin"] + ".",
     light_line(r, "the three women and the staircase", MALL_Q),
     *tail("no fourth person close to camera, no crowd, no product visible, no knee strap visible, no walking stick, no running, no one coming down the stairs, no different mall from the location photo, no readable sign, no text, no logos, no church hat")]
    refs = [("N sheet", JOB["N"]), ("P8-MALL plate", JOB["P8"])]
    return dict(model="nano_banana_2", refs=refs, body=body)
BEATS["HK-01b"] = hk_01b

def hk_02b():
    r = ROWS["HK-02b"]; n, d = SUBJ["N"], SUBJ["C2"]
    body = [S("CAM-LOCK"),
     angle_line(r, "the mother and daughter on the mall staircase"), focus_line(r, "the mother"),
     MALL_PLATE + " — seen side-on from the ground-floor concourse at the height of the middle of the flight, the staircase running diagonally across the frame, the glass balustrade clean in front of them.",
     "TWO PEOPLE, each exactly as in their attached reference sheet. THE MOTHER, ahead and higher: " + n["markers"] + ". THE DAUGHTER, one step directly behind and below her on the same stairs: " + d["markers"] + ". Unchanged in face, age and build.",
     "Caught mid-climb, in profile: the mother is climbing briskly, her front foot planted on the next step and her weight moving onto it, one hand only brushing the steel handrail, a small shopping bag in the other, face in profile, a small smile. "
     "Directly behind her, one step lower, the daughter follows with two big shopping bags, one hand reaching for the handrail, her body leaning into the climb, her face turned up toward her mother, eyebrows raised in surprise, a little out of breath. "
     "Waist-up to knees, both women whole in the frame, one behind the other.",
     "THE MOTHER is wearing " + WARD["N-D4"] + ". THE DAUGHTER is wearing " + WARD["C2"] + ".",
     "Real unretouched skin: the mother " + n["skin"] + "; the daughter " + d["skin"] + ".",
     light_line(r, "the two women and the staircase", MALL_Q),
     *tail("no third person close to camera, no crowd, no product visible, no knee strap visible, no walking stick, no daughter beside or ahead of her mother, no different mall from the location photo, no readable sign, no text, no logos, no home staircase")]
    refs = [("N sheet", JOB["N"]), ("C2 sheet", JOB["C2"]), ("P8-MALL plate", JOB["P8"])]
    return dict(model="nano_banana_2", refs=refs, body=body)
BEATS["HK-02b"] = hk_02b

if __name__ == "__main__":
    out = HERE / "prompts"; out.mkdir(exist_ok=True)
    for b in sys.argv[1:] or BEATS:
        dd = BEATS[b](); p = "\n\n".join(dd["body"])
        (out / f"{b}.t2i.txt").write_text(p)
        (out / f"{b}.refs.json").write_text(json.dumps(dict(model=dd["model"], refs=dd["refs"]), indent=1))
        print(b, dd["model"], len(p), "chars", [x[0] for x in dd["refs"]])
