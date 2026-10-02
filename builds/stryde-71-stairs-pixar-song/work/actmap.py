#!/usr/bin/env python3
"""stryde-71-stairs-pixar-song — step 5 act map (E4) on the song's clock. One source of truth.
Writes: work/actmap_rows.json (cut order, E4 fields + §27G/§30I/§30J/§30K, song t_in/t_out, E6 call length),
        work/angles.json (for angles.py), work/actmap.md (tables), work/plan.json (assemble.py plan).
Mode 2 (3D Pixar): no talking heads (§3A variant A — the song is the voice; N is seen, never addresses the lens),
render rigs only (RV / R4), every image nano_banana_pro (A/B pair), PIX-SPLIT on product beats.
Durations (E6, V7.60.6): the beat's time on screen = its cut (6 frames before its first lyric word's onset) to the next
beat's cut, + 0.4 s skipped opening + 0.5 s handle, rounded up, Kling 3–15 s, human motion capped at `max` (6)."""
import json, math, pathlib
HERE = pathlib.Path(__file__).parent
LYR = {r["n"]: r for r in json.load(open(HERE / "lyrics.timed.json"))}
LYR[37]["start"], LYR[37]["end"] = 84.46, 86.28       # "Stryde." — not heard by the transcript (F4); the gap after line 36 carries it
VOCAL_END, LEAD, SKIP, HANDLE = 222.68, 0.25, 0.4, 0.5
GRID = json.load(open(HERE.parent / "music/MUS-BODY.grid.json")); BEATS = GRID["beats"]; BAR = GRID["beat_s"] * 4
SECTIONS = [(sec["name"], sec["start"], sec["end"]) for sec in json.load(open(HERE.parent / "music/MUS-BODY.cue.json"))["sections"]]
def snap(t):
    b = [x for x in BEATS if x <= t + 1e-6]
    return round(b[-1], 2) if b else 0.0

ROWS = []
def R(beat, act, lines, key, fn, subj, loc, day, framing, action, pace, staging, prod, vis,
      h, side, fg, scale, why, plane, dof, src, kelvin, time, arc, face, music, ledger="", layout="full", eg="",
      pin="no", camera="RV sway — the virtual camera breathes in place, never travels", mx=6, mirror=None, moving=False, ks=None, tin=0.0,
      sub=None, t0=None):
    pin_waived = None
    if staging.startswith("stairs"):
        # §27G rule 10 would pin every stairs clip; the user waived it: "we dont need end frame" (2026-10-01) — recorded as pin_waived
        pin = "no"; pin_waived = "user 2026-10-01: \"we dont need end frame\""
    a, b = lines
    line = sub or " ".join(LYR[i]["line"] for i in range(a, b + 1))   # sub: one phrase of a line that has its own picture (user 2026-10-02)
    if vis in ("VISIBLE", "REVEAL", "REVEAL→CONCEALED") or prod.startswith(("worn (anatomical)", "held", "box", "seated")):
        plane = "product"
    ks = ks or {"front": "L", "three-quarter": "R", "profile": "L", "behind": "L", "three-quarter-back": "R", "ots": "R"}[side]
    ROWS.append(dict(beat=beat, act=act, type="BR", lines=[a, b], line=line, key=key, function=fn, subject=subj, location=loc,
        story_day=day, framing=framing, action=action, pace=pace, camera=camera, staging=staging, pin_end=pin, pin_waived=pin_waived, max=mx,
        product=prod, visibility=vis, model="NBP", layout=layout, eg=eg, ledger=ledger, music=music,
        angle=dict(height=h, side=side, fg=fg, scale=scale, why=why), mirror_of=mirror,
        focus=dict(plane=plane, dof=dof, rack=None, moving_subject=moving),
        light=dict(source=src, key_side=ks, time=time, arc=arc, kelvin=kelvin), face=face, speaking=False, tin=tin, t0=t0))

E, TQ, PR, FR, BH, OT, TQB = "eye", "three-quarter", "profile", "front", "behind", "ots", "three-quarter-back"
STAIR_AM = ("landing window at the top of the stairs, south wall", 6500)
STAIR_PM = ("front-door sidelights, west wall", 5600)
KIT = ("window over the sink, south wall", 5600)
REC = ("warm string lights and chandeliers", 3200)
STORE = ("overhead panel lights", 4000)
SUN = ("open sky, afternoon sun", 5600)
CLIN = ("exam-room window, blind half open, west wall", 5600)
BED = ("bedroom window, east wall", 5600)
LIV = ("living-room window, front wall", 5600)
PORCH = ("open sky, afternoon sun on the porch", 5600)
ANAT = ("anatomical register (§12A), neutral studio light", 5600)
R4 = "R4 — slow single-axis push on a stabilised virtual rig"

# ---------------- Hook (0.0–15.5 s) — Last Sunday, N-D4
A = "Hook 1"
# Hook re-angled on the user's ask (2026-10-01, "USE THE CINEMATIC CAMERA ANGLES CAUSE THIS HOOK IS TOO WEAK"): §30I setups named with the
# §24K part 7 shot library (Modes 4–5 library, applied here on the user's explicit call); §27G staging unchanged. HT05: the hook must sell.
# HOOK v3 concept on the user's call (2026-10-01, "i want new ones cause these hooks look the same as the others i want more powerful hooks"):
# one monumental public staircase out in the world — the long outdoor steps of a downtown arena plaza (new plate P8-PLAZA, L-PLAZA), the younger
# crowd on the steps around her (HT05: stakes in the picture, out in the world). The same Sunday (N-D4): church dress + hat; the daughter in her sheet outfit.
R("HK-01a", A, (1, 2), "stairs", "hook — the result, one B-roll for both lines (user 2026-10-01: her walking faster up the stairs, the women half her age walking behind her, left behind; HT05 out in the world) · SH-LOW at FULL from the plaza", "N + two women half her age", "L-PLAZA", "N-D4",
  "FULL from the plaza at the foot of the great outdoor flight, the lens at hip height looking up the steps: N in her church dress and hat mid-flight on the 15th of 30 steps, climbing away from the lens with her back to it, facing the doors, hands free, head up, the edge of a smile past the hat brim; three and four steps behind her two women of thirty-five in weekend clothes walking up slowly, one with a hand on the steel rail, both looking up at her back, left behind — the arena's glass doors at the top",
  "three quick steps up, N pulling away; the two women behind her climb slowly and fall further back", "one step per second for N, half that for the women", "stairs: side-on/behind, full body, camera still at the foot", "worn (under the dress)", "HIDDEN",
  "low", TQB, "clean", "FULL", "low = resolve, the monumental flight rising above her; the women half her age falling behind her are the stakes", "deep", "deep", "open sky, afternoon sun", 5600, "afternoon", "after: Sunday sun", True, "MUS-OPEN", ledger="VN04", mx=10)
R("HK-02a", A, (3, 4), "daughter", "hook — the witness (last Sunday: the daughter walking behind her up the church steps, edit of P5, HT17) · SH-LOW at FULL from the sidewalk", "N + C2", "L-CHURCH", "N-D4",
  "FULL from the sidewalk at the foot of the church steps, the lens at hip height looking up the flight: N on the 6th of 8 steps climbing briskly hands free, her daughter two steps behind her on the 4th, right hand on the black iron handrail, eyes on her mother's back; the white church doors at the top",
  "two steps up, the daughter following two steps behind", "one step per second", "stairs: side-on/behind, full body, camera still at the foot", "worn (under the dress)", "HIDDEN",
  "low", TQB, "clean", "FULL", "low = resolve, the church rising above her; the daughter walking behind her is the witness of the line", "deep", "deep", "open sky, afternoon sun", 5600, "afternoon", "after: Sunday sun", True, "MUS-OPEN")
R("HK-03a", A, (5, 5), "Mama", "hook — the line (a new angle on the user's call: from inside the open church doorway, the two on the doorstep, close up on the user's Fix) · CU through the doors", "N + C2", "L-CHURCH", "N-D4",
  "CU at eye level from inside the church's open front doorway, both heads filling the frame: N nearest the lens in three-quarter profile turned back to her daughter, a small smile; the daughter a step beyond, face up to her mother, mouth open mid-word; the door edge and the sunlit sidewalk soft",
  "the daughter's head tilts as she asks, N's smile widens", "a beat, about a second", "none", "worn (under the dress)", "HIDDEN",
  "eye", TQ, "through", "CU", "through the doorway in close = the line lands between the two faces; she has arrived, the daughter is still on the step (HT24)", "eyes", "shallow", "open sky, afternoon sun", 5600, "afternoon", "after: Sunday sun", True, "MUS-OPEN")
R("P-01a", A, (6, 6), "backwards", "problem (HT02; user Fix 2026-10-01: looking up the stairs, stepping backward — so the lens goes to the foot of the flight, edit of P0)", "N", "L-N-STAIRS", "N-D1",
  "MEDIUM from the hall, the lens low on the top of the flight and the landing: N starting from the top — standing on the top step at the head of the stairs (user Fix 2026-10-01: starting from the top to show the moving backwards; never at the bottom), her back to the lens, face turned up to the landing, both hands gripping the oak rail, her first foot reaching back and down to the step below",
  "one careful step down backwards, her back to the lens", "one step, about two seconds", "stairs: camera at the foot, subject above with her back to it, slow single step", "absent", "—",
  "low", BH, "clean", "MEDIUM", "low from the hall, her back to us = going down the wrong way, small against the flight rising above her", "deep", "deep", *STAIR_AM, "morning", "problem: grey", False, "MUS-EXPOSE", ledger="VN04")
R("P-01b", A, (7, 7), "step", "problem", "N feet", "L-N-STAIRS", "N-D1",
  "CU from the side at step height on her legs going down backwards (user 2026-10-01: 'a close shot of the legs here going down backwards'): her body facing up the stairs, the left slipper on the step above, the right reaching back and down heel first onto the step below, one hand on the rail at the top edge",
  "the right heel settles on the step below, the left foot joins it", "about two seconds", "stairs: legs only, side, going down backwards", "absent", "—",
  "ground", PR, "clean", "CU", "ground from the side = the heel-first step down reads as backwards, which the view from below never did", "foreground", "medium", *STAIR_AM, "morning", "problem: grey", False, "MUS-EXPOSE")
R("P-02a", A, (8, 10), "down", "problem (edit of P0: the top of the flight, HT17)", "N", "L-N-STAIRS (landing)", "N-D1",
  "MEDIUM from mid-flight looking up at the top step (an edit of the confirmed P-02a v6 frame — her own staircase; user Fix 2026-10-01: 'wrong location' after the over-the-shoulder try): N sitting on the top step in her house dress, one hand on the newel, looking down the flight toward the lens, the top steps and the photo wall around her",
  "she looks down the stairs and looks away", "one turn of the head, about two seconds", "none", "absent", "—",
  "low", FR, "clean", "MEDIUM", "low from mid-flight = closer on her at the top, the steps between us; her own hall, not a new one", "eyes", "deep", *STAIR_AM, "morning", "problem: grey", True, "MUS-EXPOSE")
R("P-03a", A, (11, 12), "brace", "failed fix", "N", "L-N-KITCHEN", "N-D1",
  "MEDIUM-CU from the side at knee height, N seated on the kitchen chair at the table, her right leg out a little: a short black hinged knee brace — a hand's length above and below the knee — sagging below the kneecap, her right hand hauling its top strap up, her left hand on the chair seat; head and shoulders out of frame (user 2026-10-01: the whole P-03 new; the brace a bit more short)",
  "the brace drifts down her shin, then her hand pulls it back up over the knee", "one slide down, one pull up, about four seconds", "hands: large in frame, one movement, seated", "absent (generic brace, §10)", "—",
  "low", PR, "clean", "CU", "low at knee height from the side = the brace is the subject; seated, so P-03b can be the same seat (FP14); user Fix 2026-10-01 on the clip: it should feel like drifting down, then: falling while drifting down; then: drifts down, then pull it up again", "hands", "medium", *KIT, "morning", "problem: grey", False, "MUS-EXPOSE")
R("P-03b", A, (13, 13), "ankle", "failed fix", "N feet", "L-N-KITCHEN", "N-D1",
  "CU from the same side, the frame dropped to floor level: the same seat and chair as P-03a, the same brace now bunched around her right ankle above her slipper, both slippers on the floor; hands and head out of frame (edit of the P-03a frame, FP14)",
  "she shifts her foot once", "one small shift, about a second", "feet only, seated", "absent", "—",
  "ground", PR, "clean", "CU", "ground = where it ended up; the same side as P-03a so the two connect", "foreground", "medium", *KIT, "evening", "problem: grey", False, "MUS-EXPOSE")
R("P-04a", A, (14, 14), "everything", "failed fix (HT10)", "N hands", "L-N-KITCHEN", "N-D1c",
  "overhead on the kitchen table: her two hands spread the whole arsenal across the wood — pill bottles, a gel tube, two sleeves, a hinged brace, an ice pack",
  "both hands push the pile apart", "one push, about two seconds", "hands: large in frame", "absent (generic, §10)", "—",
  "overhead", FR, "clean", "MEDIUM", "overhead = the whole routine laid out", "hands", "deep", *KIT, "morning", "problem: grey", False, "MUS-EXPOSE", ledger="VN06")
R("P-04b", A, (15, 15), "therapy", "failed fix", "N + one-off PT", "L-CLINIC", "N-D1b",
  "MEDIUM: N lying on a PT treatment table, a therapist's hands bending her right knee",
  "the therapist bends the knee a little further", "one slow bend, about two seconds", "hands: one movement, subject lying still", "absent", "—",
  "high", TQ, "clean", "MEDIUM", "high = done to her, passive", "hands", "medium", *CLIN, "afternoon", "problem: clinical", False, "MUS-EXPOSE",
  sub="Physical therapy.")
# Line 15 split into three pictures on the user's ask (2026-10-02: "Pain pills. Cortisone shots. we need brolls for these 2") — one per phrase,
# each cut on its own first sung word (medium.en: "Pain" 36.96 s, "Cortisone" 38.14 s); short by the song's own speed, the user's call
R("P-04c", A, (15, 15), "pills", "failed fix — the pills (user 2026-10-02: a B-roll each for 'Pain pills.' and 'Cortisone shots.')", "N hands", "L-N-KITCHEN", "N-D1c",
  "CU at table height from the side: two white pills tip out of a plain amber bottle into her open palm, a glass of water beside on the kitchen table",
  "two pills tip into her palm", "one tip, about a second", "hands: large in frame", "absent (generic, §10)", "—",
  "eye", PR, "clean", "CU", "eye at table height = the daily dose up close", "hands", "medium", *KIT, "morning", "problem: grey", False, "MUS-EXPOSE",
  mx=3, sub="Pain pills.", t0=36.96)
R("P-04d", A, (15, 15), "Cortisone", "failed fix — the shot (user 2026-10-02)", "N knee + one-off doctor (hands)", "L-CLINIC", "N-D1b",
  "CU on her bare right knee as she lies on the treatment table: a doctor's gloved hand holds a syringe, its needle at the side of the knee, the other gloved hand steadying the knee; her own hand grips the paper sheet at the table edge",
  "the doctor's thumb presses the plunger", "one slow press, about a second", "hands: one movement, subject lying still", "absent", "—",
  "low", PR, "clean", "CU", "low = the needle looming over the knee, the fear of it", "hands", "medium", *CLIN, "afternoon", "problem: clinical", False, "MUS-EXPOSE",
  mx=3, sub="Cortisone shots.", t0=38.14)
# P-05 split into three B-rolls on the user's Fix (board, 2026-10-01: "make this into 3 brolls") — one line each; the push, the heap, her face
R("P-05a", A, (16, 16), "Every", "low — the push (user 2026-10-01: three B-rolls, one per line)", "N", "L-N-KITCHEN", "N-D1c",
  "MEDIUM across the table: N pushes the heap of braces, sleeves and bottles away from her with the back of her hand",
  "one push away across the table", "one push, about two seconds", "hands: one movement, seated", "absent", "—",
  "low", TQ, "clean", "MEDIUM", "low = the table edge, her giving up made big", "eyes", "deep", *KIT, "morning", "problem: grey", True, "MUS-EXPOSE", mx=3)
R("P-05b", A, (17, 17), "worked", "low — the heap, pushed to the far edge (user 2026-10-01: three B-rolls)", "N hands", "L-N-KITCHEN", "N-D1c",
  "CU on a kitchen drawer pulled open under the counter, stuffed with knee sleeves, a hinged brace and pill bottles, N's hand on its front pushing it shut (an insert, a different kind of B-roll — user Fix 2026-10-01: 'wrong person, a different type of broll')",
  "her hand pushes the drawer shut", "one push, about a second", "hands: one movement, insert", "absent (generic, §10)", "—",
  "eye", FR, "clean", "CU", "eye on the drawer = where it all ended up, shut away", "product", "medium", *KIT, "morning", "problem: grey", False, "MUS-EXPOSE", mx=3)
R("P-05c", A, (18, 18), "life", "low — her face, sat back (user 2026-10-01: three B-rolls)", "N", "L-N-KITCHEN", "N-D1c",
  "MEDIUM at the kitchen window: N in profile at the sink, both hands on its edge, looking out of the window at the street, the light on her face (a different kind of B-roll with her cast sheet — user Fix 2026-10-01: 'wrong person, a different type of broll')",
  "she looks out, then her eyes drop to the sink", "one look down, about two seconds", "face: one movement, standing still", "absent", "—",
  "eye", PR, "clean", "MEDIUM", "profile at the window = the life outside she is not in", "eyes", "medium", *KIT, "morning", "problem: grey", True, "MUS-EXPOSE", mx=3)

# ---------------- Act 2 — the turn (44.0–64.4 s), the wedding, N-D2
A = "Act 2"
R("T-01a", A, (19, 19), "married", "turn", "N + one-off bride", "L-RECEPTION", "N-D2",
  "MEDIUM: the bride in white hugging N (burgundy dress) at the edge of the dance floor, string lights overhead, both smiling with eyes closed (user 2026-10-01: new images, new wardrobe)",
  "the two of them sway once in the hug", "one slow sway, about two seconds", "none", "absent", "—",
  "eye", TQ, "clean", "MEDIUM", "eye level, close on the hug = her grandbaby, her day", "eyes", "deep", *REC, "evening", "turn: warm party light", True, "MUS-TURN", ledger="VN05")
R("T-01b", A, (20, 21), "Loretta", "turn", "C1", "L-RECEPTION", "N-D2",
  "MCU: Loretta on the dance floor in her fuchsia satin dress, both hands up waving to the beat, a big closed-mouth grin",
  "her raised hands wave once on the beat", "one wave, about a second", "hands: one movement", "absent", "—",
  "low", TQ, "clean", "MCU", "low = she's the one with the strength", "eyes", "deep", *REC, "evening", "turn: warm party light", True, "MUS-TURN", ledger="VN05")
R("T-02a", A, (22, 22), "floor", "turn", "C1 + one-off guests", "L-RECEPTION", "N-D2",
  "WIDE from a little above: Loretta in fuchsia leads the line dance at the front, nearest the lens, her face clear, the guests stepping behind her (user Fix 2026-10-02: this should be loreta)",
  "one side step with the line", "one step per beat, about a second", "dancing: wide, side step, camera still", "worn (under her dress, hidden)", "HIDDEN",
  "high", FR, "clean", "WIDE", "high over the floor = the whole line moving as one, her in the middle of it", "deep", "deep", *REC, "evening", "turn: warm party light", False, "MUS-TURN", ledger="VN05")
R("T-02b", A, (23, 23), "Slide", "turn", "C1 feet + line", "L-RECEPTION", "N-D2",
  "CU at floor level from the side: the line's feet in profile on the parquet, Loretta's white slip-ons under a fuchsia hem, stepping together",
  "one step forward in unison", "one step, about a second", "feet only, one step", "absent", "—",
  "ground", PR, "clean", "CU", "ground from the side = the step reads as a step", "foreground", "medium", *REC, "evening", "turn: warm party light", False, "MUS-TURN", ledger="VN05")
R("T-03a", A, (24, 24), "bone", "mechanism — the worn joint", "—", "—", "—",
  "ANAT-A: S2 X-ray of both knees front-on, the worn joint surfaces touching, glowing red where bone meets bone",
  "the red pulses once", "one pulse, about a second", "none", "absent", "—",
  "eye", FR, "clean", "CU", "front-on shows both knees and the gap gone on each side of the joint", "deep", "deep", *ANAT, "—", "mechanism", False, "MUS-TURN", eg="EG04", camera=R4, mx=15)
R("T-04a", A, (25, 25), "mine", "turn — her doubt", "N + C1 (far)", "L-RECEPTION", "N-D2",
  "MEDIUM over her shoulder: N seated alone at a reception table in her burgundy dress, Loretta in fuchsia dancing in focus beyond, N's hand resting on her own right knee",
  "she looks from the dance floor down to her knee", "one look down, about two seconds", "none", "absent", "—",
  "eye", OT, "through", "MEDIUM", "over her shoulder = we see what she sees, the dance she sits out", "eyes", "deep", *REC, "evening", "turn: warm party light", True, "MUS-TURN")
R("T-04b", A, (26, 26), "fixing", "turn — her doubt", "N hand", "L-RECEPTION", "N-D2",
  "CU under the table edge, front-on: N's hand rubbing her right knee through the burgundy dress, the parquet and dancing feet soft beyond",
  "her hand rubs the knee once", "one slow rub, about two seconds", "hands: one movement", "absent", "—",
  "low", FR, "clean", "CU", "low = under the table, the thing she hides", "hands", "medium", *REC, "evening", "turn: warm party light", False, "MUS-TURN")

# ---------------- Act 3 — the reveal + payoff (65.0–106.6 s), Loretta's visit, N-D3
A = "Act 3"
R("R-01a", A, (27, 27), "stay", "reveal", "C1", "L-N-STAIRS", "N-D3a",
  "MEDIUM from inside the hall: Loretta stepping in through the open front door with a small overnight bag, the photo wall and the newel beside her",
  "one step over the threshold", "one step, about a second", "walking toward camera: waist-up, 1 step", "absent", "—",
  "eye", FR, "clean", "MEDIUM", "", "eyes", "deep", *STAIR_PM, "afternoon", "turn: daylight in the door", True, "MUS-TURN")
R("R-02a", A, (28, 29), "watched", "reveal — the routine", "N + C1", "L-N-KITCHEN", "N-D3",
  "MEDIUM across the kitchen table: Loretta seated with a coffee watching N, who is laying out her morning routine on the table between them",
  "N sets the gel tube down beside the bottles", "one set-down, about a second", "hands: one movement, seated", "absent", "—",
  "eye", OT, "clean", "MEDIUM", "over Loretta's shoulder = we watch with her", "hands", "deep", *KIT, "morning", "routine", True, "MUS-TURN", ledger="VN06")
R("R-02b", A, (30, 31), "gel", "reveal — the routine", "N hands", "L-N-KITCHEN", "N-D3",
  "overhead: her hands squeeze gel from a plain tube onto her fingers beside two tablets, a glass of water, the folded brace and a blue ice pack",
  "one squeeze", "about a second", "hands: large in frame", "absent", "—",
  "overhead", FR, "clean", "CU", "overhead = routine", "hands", "deep", *KIT, "morning", "routine", False, "MUS-TURN", ledger="VN06")
R("R-03a", A, (32, 33), "said", "reveal", "C1", "L-N-KITCHEN", "N-D3",
  "MCU across the table: Loretta leans in with a half smile, one hand already reaching down toward her own knee",
  "she leans in and reaches down", "one lean, about two seconds", "none", "absent", "—",
  "low", TQ, "clean", "MCU", "low = she has the answer", "eyes", "deep", *KIT, "morning", "turn", True, "MUS-TURN")
R("R-03b", A, (34, 35), "leg", "reveal (§9D)", "C1", "L-N-KITCHEN", "N-D3",
  "CLOSE from low at knee height: Loretta, chair turned out from the table, rolls her right khaki pant leg up above the knee — the strap on her knee a third of the frame wide, her knowing face above (FP11: the strap big in frame)",
  "one pull up past the knee", "one pull, about two seconds", "hands: one movement, seated", "worn", "REVEAL",
  "low", FR, "clean", "MCU", "low at the knee = the reveal is the strap, FP11", "hands", "medium", *KIT, "morning", "turn", True, "MUS-TURN")
R("R-04a", A, (36, 37), "strap", "product first appearance (PIX-SPLIT, FP01, FP03, FP11)", "C1 knee", "L-N-KITCHEN", "N-D3",
  "ECU her right knee, front-on, the strap at least a quarter of the frame wide: the little black strap seated just under the kneecap, her fingertip tapping the shell once",
  "one tap on the strap", "one tap, about a second", "hands: large in frame", "worn", "VISIBLE",
  "low", FR, "clean", "ECU", "low = the answer, resolve", "product", "medium", *KIT, "morning", "turn", False, "MUS-TURN", camera=R4)
R("R-05a", A, (38, 39), "handed", "held product (FP02, FP06)", "N hands", "L-N-KITCHEN", "N-D3",
  "CU: the strap resting across N's open palm, small against her hand, her thumb beside the shell, her face doubtful above",
  "she turns her hand a little to look at it", "one small tilt, about a second", "hands: product rigid", "held", "VISIBLE",
  "high", FR, "clean", "CU", "high = her own view of it in her hand", "product", "medium", *KIT, "morning", "turn", True, "MUS-TURN")
R("R-06a", A, (40, 41), "Loretta", "reveal — the doubt", "N + C1", "L-N-KITCHEN", "N-D3",
  "MEDIUM two-shot across the table: N holds the strap up on her open palm between them, its front to the lens, a quarter of the frame wide, one eyebrow up, Loretta across from her unbothered (FP06, FP11)",
  "N lifts the strap and tilts her head", "one lift, about two seconds", "hands: product rigid", "held", "VISIBLE",
  "eye", PR, "clean", "MEDIUM", "profile = the two of them face to face, the strap between", "product", "deep", *KIT, "morning", "turn", True, "MUS-TURN")
R("R-06b", A, (42, 43), "put", "SEAT (FP10)", "N", "L-N-KITCHEN", "N-D3",
  "CU seated: both hands slide the strap up her right shin to seat it under the kneecap — one move up to the tendon",
  "slides up the last few centimetres and stops at contact", "one slide, about a second", "hands: start mid-movement, end on contact", "seated", "VISIBLE",
  "high", TQ, "clean", "CU", "high = her own view of her knee", "product", "medium", *KIT, "morning", "turn", False, "MUS-TURN")
R("R-07a", A, (44, 49), "rail", "payoff (HT03, HT04) — one take for both lines (user 2026-10-02: R-07c \"should be part of the r07a so it should be one take only\"; \"wrong stairs\" → an edit of the P0-PROP-N plate)", "N", "L-N-STAIRS", "N-D3",
  "FULL from the hall floor at the plate's own viewpoint, a tall crop on her staircase (carpet runner, brass rods, white balusters, oak rail, square newel, photo wall): N on the ninth step up coming down in three-quarter toward the lens, hands free off the rail, the strap on her bare right knee at true size",
  "comes down the flight, one step a second, facing forwards, hands off the rail", "one step per second", "stairs: three-quarter, full body, camera still at the foot", "worn", "VISIBLE",
  "eye", TQ, "clean", "FULL", "three-quarter from the hall = the whole descent, her own stairs, done on her own", "deep", "deep", *STAIR_PM, "afternoon", "after: sun through the sidelights", True, "MUS-TURN", mx=10)

# ---------------- Act 4 — Pure Mechanism (106.6–134.2 s)
A = "Act 4"
R("M-01a", A, (50, 51), "comfortable", "mechanism — comparative (F1)", "N", "L-CLINIC", "N-D1b",
  "MEDIUM: N lying back on the PT table with a heat pad on her knee, eyes closed",
  "she settles her head back", "one settle, about a second", "none", "absent", "—",
  "overhead", FR, "clean", "MEDIUM", "overhead = passive, managed", "eyes", "deep", *CLIN, "afternoon", "problem: clinical", True, "MUS-EDU", ledger="F1")
R("M-02a", A, (52, 53), "fixes", "mechanism — comparison card (EG03, F1/F5)", "—", "—", "—",
  "CARD: two knees side by side in the anatomical register — left, a full sleeve over the whole knee, pressure spread everywhere; right, the strap seated under the kneecap on one spot",
  "a slow soft glow settles on the right knee's spot", "about two seconds", "none", "worn (anatomical)", "—",
  "eye", FR, "clean", "MEDIUM", "", "deep", "deep", *ANAT, "—", "mechanism", False, "MUS-EDU", layout="card", eg="EG03 · labels in the edit", ledger="F5", camera=R4, mx=15)
R("M-03a", A, (54, 55), "spot", "mechanism — the spot (HT11)", "—", "—", "—",
  "ANAT-A: the knee front-on, a red point on the patellar tendon just under the kneecap pulsing with each step",
  "the point pulses with a walking cadence", "one pulse per second", "none", "absent", "—",
  "low", PR, "clean", "CU", "low = the spot made big and important", "deep", "deep", *ANAT, "—", "mechanism", False, "MUS-EDU", eg="EG04", camera=R4, mx=15)
R("M-04a", A, (56, 58), "whole", "mechanism — comparative (F1)", "—", "L-N-KITCHEN", "N-D1c",
  "overhead: the heap of braces and sleeves beside the pill bottles and the syringe box on the table",
  "none — held", "about two seconds", "none", "absent", "—",
  "overhead", FR, "clean", "MEDIUM", "overhead = the whole routine laid out", "deep", "deep", *KIT, "morning", "problem: grey", False, "MUS-EDU", ledger="F1", camera=R4, mx=15)
R("M-05a", A, (59, 61), "pressure", "mechanism", "—", "—", "—",
  "ANAT-A: the knee with a generic sleeve drawn faintly around the whole joint, the red point under the kneecap glowing through it, pressure lines running down the thigh into the point",
  "pressure pulses down the leg", "one pulse per second", "none", "absent", "—",
  "eye", PR, "clean", "MEDIUM", "profile shows the load path down the leg", "deep", "deep", *ANAT, "—", "mechanism", False, "MUS-EDU", eg="EG04", camera=R4, mx=15)
R("M-05b", A, (62, 63), "weight", "mechanism — protection (HT11, FP03)", "—", "—", "—",
  "ANAT-A: the strap seated under the kneecap, the pad on the spot, the red fading to calm blue",
  "the red fades to blue as the pad takes the load", "one fade, about two seconds", "none", "worn (anatomical)", "—",
  "low", TQ, "clean", "CU", "low = the fix, resolve", "deep", "deep", *ANAT, "—", "mechanism", False, "MUS-EDU", eg="EG04", camera=R4, mx=15)
R("M-06a", A, (64, 65), "gone", "outcome (F1)", "N feet", "L-N-STAIRS", "N-D3",
  "CU from the step below: her foot lands on the top step, strap on the bare right knee above, the family photos soft behind",
  "one foot lands on the step", "one step, about a second", "stairs: feet only, front", "worn", "VISIBLE",
  "ground", FR, "clean", "CU", "ground = the first step", "product", "medium", *STAIR_PM, "afternoon", "after: sun", False, "MUS-EDU", ledger="F1")

# ---------------- Act 5 — proof (134.2–159.2 s)
A = "Act 5"
R("PR-01a", A, (66, 66), "people", "proof (EG05 → one picture, §30H floor)", "one-off man, 60s", "L-MONT-1 porch", "G-1",
  "CU: a man of sixty-odd sits on a porch step and seats the strap on his right knee — the strap at least a quarter of the frame wide",
  "slides the strap to contact", "one movement, about a second", "hands: start mid-movement, end on contact", "seated", "VISIBLE",
  "high", TQ, "clean", "CU", "high = his own view of the knee", "product", "medium", *SUN, "afternoon", "proof: daylight", False, "MUS-AFTER", eg="EG05 · 200,000+ overlay")
R("PR-02a", A, (67, 68), "doctors", "authority (F1, §19B)", "one-off sports doctor", "L-CLINIC", "G-5",
  "MCU: an approachable sports-medicine doctor in a polo shirt holds the strap up beside the knee model on her desk, front of the strap to the lens, then seats it under the model's kneecap",
  "she turns the strap to the lens and seats it on the model", "one turn, then one press, about three seconds", "hands: product rigid", "held", "VISIBLE",
  "eye", TQ, "clean", "MCU", "", "eyes", "medium", *CLIN, "afternoon", "authority: even daylight", True, "MUS-AFTER", ledger="F1", pin="yes")
R("PR-03a", A, (69, 70), "golf", "proof", "one-off, Loretta's husband", "L-GOLF", "G-6",
  "MEDIUM from the side: a Black man of 76 in a golf polo and khaki shorts mid-swing follow-through, the strap on his bare right knee",
  "finishes the follow-through and holds", "one follow-through, about a second", "one movement, feet planted", "worn", "VISIBLE",
  "low", PR, "clean", "FULL", "low = strong at 76", "deep", "deep", *SUN, "afternoon", "proof: sun", True, "MUS-AFTER")
R("PR-04a", A, (71, 72), "track", "proof", "one-off, niece 22", "L-TRACK", "G-7",
  "MEDIUM: a young Black woman jogging on a red running track in shorts, the strap on her right knee",
  "three jogging strides past the lens", "about two strides per second", "running across frame: camera still, side-on", "worn", "VISIBLE",
  "eye", TQ, "clean", "FULL", "", "deep", "deep", *SUN, "afternoon", "proof: sun", True, "MUS-AFTER")
R("PR-05a", A, (73, 73), "worn", "feature", "N", "L-N-BEDROOM", "N-D5",
  "CU on the bed edge in the morning: N seats the strap under her bare right kneecap",
  "slides the strap the last few centimetres", "one slide, about a second", "hands: start mid-movement, end on contact", "seated", "VISIBLE",
  "high", TQ, "clean", "CU", "high = her own view of her knee", "product", "medium", *BED, "morning", "after: fresh daylight", False, "MUS-AFTER")
R("PR-05b", A, (74, 75), "clothes", "feature — conceal (§9D)", "N", "L-N-BEDROOM", "N-D5",
  "CU from the side: her trouser leg drops over the strap and lies flat",
  "the trouser leg falls and settles", "one drop, about a second", "none", "worn", "REVEAL→CONCEALED",
  "eye", PR, "clean", "CU", "profile shows the flat trouser line", "product", "medium", *BED, "morning", "after: fresh daylight", False, "MUS-AFTER")
R("PR-06a", A, (76, 77), "pills", "feature", "—", "L-N-KITCHEN", "N-D5",
  "overhead: the kitchen table cleared — just a coffee mug and the strap lying beside it, front up; no bottles, no gel, no brace",
  "steam rises from the mug", "about two seconds", "none", "absent (strap on table)", "VISIBLE",
  "overhead", FR, "clean", "CU", "overhead = the same table, the routine gone", "product", "deep", *KIT, "morning", "after: sun", False, "MUS-AFTER", mirror="P-04a", camera=R4, mx=15)

# ---------------- Act 6 — the result, lived (160.5–178.1 s), yesterday, N-D6
A = "Act 6"
R("L-01a", A, (78, 79), "store", "result (F1, HT01)", "N", "L-STREET", "N-D6",
  "MEDIUM from behind: N walking away along the sidewalk of her tree-lined street, a tote bag on her shoulder",
  "three steps away from the lens", "one step per second", "walking away: waist-up, 3 steps, camera still", "worn (under trousers)", "HIDDEN",
  "eye", BH, "clean", "MEDIUM", "behind = we let her go, she doesn't need us", "deep", "deep", *SUN, "afternoon", "after: sun", False, "MUS-AFTER", ledger="F1")
R("L-01b", A, (80, 80), "Passed", "result", "N + one-offs", "L-STREET", "N-D6",
  "MEDIUM three-quarter: N overtakes three younger women strolling slowly on the sidewalk",
  "two steps as she draws level and passes", "one step per second", "walking across frame: camera still", "worn (under trousers)", "HIDDEN",
  "low", TQ, "clean", "MEDIUM", "low = she's the strong one", "deep", "deep", *SUN, "afternoon", "after: sun", True, "MUS-AFTER", tin=-0.85)
R("L-02a", A, (81, 82), "checkout", "result", "N + one-offs", "L-STORE", "N-D6",
  "MEDIUM: N standing square in a grocery checkout line with a full basket, shoppers ahead of her",
  "she moves the basket to her other hand, feet planted", "one movement, about a second", "none", "worn (under trousers)", "HIDDEN",
  "eye", TQ, "clean", "MEDIUM", "", "eyes", "deep", *STORE, "afternoon", "after: store light", True, "MUS-AFTER", ledger="VN07")
R("L-02b", A, (83, 84), "bags", "result (HT01)", "N", "L-STREET", "N-D6",
  "MEDIUM from behind: N walking up her front path to the porch, a grocery bag in each hand",
  "two steps up the path", "one step per second", "walking away: waist-up, 2 steps", "worn (under trousers)", "HIDDEN",
  "low", TQB, "clean", "MEDIUM", "low = resolve; she made it", "deep", "deep", *SUN, "afternoon", "after: sun", False, "MUS-AFTER")
R("L-03a", A, (85, 87), "husband", "result", "one-off, N's husband", "L-N-LIVING", "N-D6",
  "MEDIUM: her husband in his recliner lowers the newspaper (blank pages) and looks up toward the door, where N stands with a grocery bag in each hand, a small knowing smile",
  "lowers the paper and looks up", "one movement, about a second", "none", "absent", "—",
  "eye", TQ, "clean", "MEDIUM", "", "eyes", "deep", *LIV, "afternoon", "after: sun", True, "MUS-AFTER")

# ---------------- Act 7 — proof, name, authority, objection (178.1–200.9 s)
A = "Act 7"
R("C-01a", A, (88, 89), "strap", "result", "N", "L-N-BEDROOM", "N-D5",
  "CU: the strap on N's bare right knee as she sits on the bed edge, her hand resting beside it, thumb next to the shell",
  "her hand pats her knee once", "one pat, about a second", "hands: one movement", "worn", "VISIBLE",
  "eye", TQ, "clean", "CU", "", "product", "medium", *BED, "morning", "after: fresh daylight", False, "MUS-AFTER")
R("C-02a", A, (90, 90), "church", "proof", "3 one-offs (church ladies)", "L-CHURCH", "N-D4",
  "MCU from the sidewalk: three ladies in Sunday hats at the foot of the church steps, one nudging the next and nodding up toward the steps",
  "one nudge and a nod", "one movement, about a second", "none", "absent", "—",
  "eye", FR, "clean", "MCU", "", "eyes", "deep", *SUN, "afternoon", "after: Sunday sun", True, "MUS-AFTER", ledger="VN08")
R("C-02b", A, (91, 92), "steps", "proof (HT03)", "N + 3 one-offs", "L-CHURCH", "N-D4",
  "MEDIUM from the sidewalk: N comes down the church steps facing forwards, hands free, the three ladies watching from the side",
  "one step down, facing forwards", "one step, about a second", "stairs: camera at the bottom, subject 1 step, hands free", "worn (under the dress)", "HIDDEN",
  "low", TQ, "clean", "MEDIUM", "low = resolve; she's the proof", "deep", "deep", *SUN, "afternoon", "after: Sunday sun", True, "MUS-AFTER", ledger="VN08")
R("C-03b", A, (93, 93), "Stryde", "name (F5)", "—", "—", "—",
  "ANAT-A: the strap seated on the knee in the anatomical register, calm blue at the spot (labels in the edit)",
  "a slow soft glow at the pad", "about two seconds", "none", "worn (anatomical)", "—",
  "eye", TQ, "clean", "CU", "", "deep", "deep", *ANAT, "—", "mechanism", False, "MUS-OFFER", eg="EG04 · labels in the edit", ledger="F5", camera=R4, mx=15)
R("C-04a", A, (94, 96), "surgeons", "authority (§19B)", "one-off surgeon + patient", "L-CLINIC", "G-8",
  "MEDIUM: an approachable orthopaedic surgeon in scrubs fits the real strap on a seated patient's bare right knee, the shell and wordmark to the lens",
  "presses the strap flat under the kneecap", "one press, about a second", "hands: one movement", "seated", "VISIBLE",
  "eye", OT, "clean", "MEDIUM", "over the shoulder = we're the patient", "hands", "medium", *CLIN, "afternoon", "authority: even daylight", True, "MUS-OFFER")
R("C-05a", A, (97, 99), "knock-offs", "objection (F6, §10, FP08)", "one-off hands", "L-N-KITCHEN", "N-D5",
  "CU on a plain table: two cheap copies of the same shape being stretched between two hands, the band sagging, the shell flexing — no brand, no packaging, no screen",
  "the hands stretch the copy and it sags", "one stretch, about two seconds", "hands: one movement", "absent (fakes, §10)", "—",
  "high", TQ, "clean", "CU", "high = looked down on", "foreground", "medium", *KIT, "morning", "objection", False, "MUS-OFFER", ledger="F6")

# ---------------- Act 8 — offer, guarantee, close (200.9–222.7 s)
A = "Act 8"
R("C-06a", A, (100, 101), "Two", "offer (EG06, FP09)", "N", "L-N-LIVING", "N-D5",
  "MCU: N on her sofa holds up two straps, one in each hand, looking at them with a grin, fronts to the lens",
  "lifts both straps a little higher", "one lift, about a second", "hands: product rigid in both hands", "held, two units", "VISIBLE",
  "eye", FR, "clean", "MCU", "", "product", "medium", *LIV, "morning", "offer: bright daylight", True, "MUS-OFFER", eg="EG06 · offer overlay")
R("C-07a", A, (102, 103), "Sixty", "guarantee", "—", "L-N-KITCHEN", "N-D5",
  "overhead on the kitchen table: the open box with two straps side by side, small on the table",
  "her hand sets the lid beside the box", "one movement, about a second", "hands: straps do not move", "box open, two units", "VISIBLE",
  "overhead", FR, "clean", "CU", "overhead = the table, the reveal", "product", "deep", *KIT, "morning", "offer: bright daylight", False, "MUS-OFFER", eg="60-day overlay")
R("C-08a", A, (104, 104), "years", "outcome (F1)", "N", "L-N-STAIRS", "N-D0",
  "MEDIUM from the hall: N on the stairs the old way — side-on, both hands on the rail, one foot feeling for the step below",
  "one slow step down", "one step, about two seconds", "stairs: side, waist-up, camera still", "absent", "—",
  "high", PR, "through", "MEDIUM", "high through the balusters = the years of it", "deep", "deep", *STAIR_AM, "morning", "problem: grey", False, "MUS-OFFER", ledger="F1")
R("C-08b", A, (105, 105), "step", "outcome (F1)", "N", "L-N-STAIRS", "N-D3",
  "MEDIUM from the hall floor, the same flight: N takes a step down facing forwards, hands free, the strap on her bare right knee",
  "one step down, facing forwards", "one step, about a second", "stairs: camera at the bottom, subject 1 step, hands free", "worn", "VISIBLE",
  "low", FR, "clean", "MEDIUM", "low = resolve", "deep", "deep", *STAIR_PM, "afternoon", "after: sun", True, "MUS-OFFER", ledger="F1", mirror="R-07a")
R("C-09a", A, (106, 106), "sister", "close", "N hands", "L-N-KITCHEN", "N-D5",
  "CU: she ties a ribbon around a second closed box on the kitchen table",
  "pulls the ribbon's bow tight", "one pull, about two seconds", "hands: large in frame", "box closed", "—",
  "high", TQ, "clean", "CU", "high = her own view", "hands", "medium", *KIT, "morning", "after", False, "MUS-OFFER")
R("C-09c", A, (107, 108), "stairs", "close (HT03)", "one-off sister + N", "L-N-STAIRS", "N-D7",
  "MEDIUM from the landing looking down: the sister, a ribboned box under one arm, climbing the family-photo stairs toward the camera, hands off the rail, N's shoulder at the top edge of frame watching",
  "two steps up, hands free", "one step per second", "stairs: camera at the top, subject coming up 2 steps, hands free", "worn (the sister's, under the dress)", "HIDDEN",
  "high", FR, "clean", "MEDIUM", "high = from N's place at the top, the mirror of the hook", "deep", "deep", *STAIR_PM, "afternoon", "after: Sunday sun", True, "MUS-OFFER", mirror="HK-02a")

def e6():
    """song-clocked spans (E6): cut = first lyric word onset − 0.25 s; on-screen to the next beat's cut; call = ceil(on + 0.4 + 0.5), 3–15, split over `max`."""
    for i, r in enumerate(ROWS):
        a = r["lines"][0]; lyric_cut = max(0.0, (r["t0"] if r.get("t0") is not None else LYR[a]["start"]) - LEAD + r["tin"]); r["lyric_cut"] = round(lyric_cut, 2); r["t_in"] = snap(lyric_cut) if i else 0.0
    for i, r in enumerate(ROWS):
        nxt = ROWS[i + 1]["t_in"] if i + 1 < len(ROWS) else VOCAL_END
        on = round(nxt - r["t_in"], 2); r["t_out"] = round(nxt, 2); r["on_screen"] = on
        call = math.ceil(on + SKIP + HANDLE); call = max(3, min(15, call))
        r["duration"] = min(call, r["max"]); r["split"] = call > r["max"]; r["flash"] = on < 2.0
        r["bars"] = round(on / BAR * 2) / 2; r["section"] = next((n for n, s0, e0 in SECTIONS if s0 <= r["t_in"] < e0), SECTIONS[-1][0])

if __name__ == "__main__":
    e6()
    json.dump(ROWS, open(HERE / "actmap_rows.json", "w"), indent=1, ensure_ascii=False)
    ang = [dict(beat=r["beat"], group=r["act"], type=r["type"], subject=r["subject"], **r["angle"], mirror_of=r["mirror_of"], mode=2,
                speaking=False, product_beat=not r["product"].startswith("absent") and r["visibility"] != "HIDDEN",
                focus=r["focus"], story_day=r["story_day"], face=r["face"], light=r["light"]) for r in ROWS]
    json.dump(ang, open(HERE / "angles.json", "w"), indent=1)
    cols = ["Beat", "Act", "Song t (s)", "Section · bars", "Lines", "Lyric (verbatim)", "Key", "Function", "Subject", "Location", "Day", "Framing", "Action · pace", "Staging (§27G)",
            "Pin end", "Camera", "Angle (§30I)", "Focus (§30J)", "Light (§30K)", "Product · visibility", "Layout · EG", "Call (E6)", "Music (§40A)", "Ledger"]
    md, cur = [], None
    for r in ROWS:
        if r["act"] != cur:
            cur = r["act"]; md += ["", f"### {cur}", "", "| " + " | ".join(cols) + " |", "|" + "---|" * len(cols)]
        a, f, l = r["angle"], r["focus"], r["light"]
        md.append("| " + " | ".join(str(x).replace("|", "/") for x in [
            r["beat"], r["act"], f'{r["t_in"]:.2f} → {r["t_out"]:.2f} ({r["on_screen"]:.1f})', f'{r["section"].split(" — ")[1]} · {r["bars"]:g}', f'{r["lines"][0]}–{r["lines"][1]}', r["line"], r["key"], r["function"], r["subject"], r["location"], r["story_day"], r["framing"],
            f'{r["action"]} · {r["pace"]}', r["staging"], r["pin_end"] + (" · waived (user 2026-10-01)" if r.get("pin_waived") else ""), r["camera"],
            f'{a["height"]} · {a["side"]} · {a["fg"]} · {a["scale"]}' + (f' — {a["why"]}' if a["why"] else ""),
            f'{f["plane"]} · {f["dof"]}', f'{l["source"]} · key {l["key_side"]} · {l["time"]} · {l["arc"]} · {l["kelvin"]}K',
            f'{r["product"]} · {r["visibility"]}', r["layout"] + (f' · {r["eg"]}' if r["eg"] else ""),
            f'{r["duration"]}s' + (" · SPLIT" if r["split"] else ""), r["music"], r["ledger"] or "—"]) + " |")
    (HERE / "actmap.md").write_text("\n".join(md).strip() + "\n")
    plan = {"master": "intake/song.mp3", "script": "work/lyrics.txt", "fps": 24,
            "broll": [{"beat": r["beat"], "phrase": r["line"], "key": r["key"], "max": r["max"], "layout": r["layout"], "in_cut": r["t_in"], "section": r["section"], "bars": r["bars"], "clip": f"renders/{r['beat']}.mp4"} for r in ROWS]}
    json.dump(plan, open(HERE / "plan.json", "w"), indent=1, ensure_ascii=False)
    covered = set(); [covered.update(range(r["lines"][0], r["lines"][1] + 1)) for r in ROWS]
    print(len(ROWS), "rows ·", "lines covered", len(covered), "of 108 · missing", sorted(set(range(1, 109)) - covered),
          "· splits", [r["beat"] for r in ROWS if r["split"]], "· FLASH", [(r["beat"], r["on_screen"]) for r in ROWS if r["flash"]], "· total on-screen", round(sum(r["on_screen"] for r in ROWS), 1))
