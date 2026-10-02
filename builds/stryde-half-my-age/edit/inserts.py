"""Cutaways for the slowed stretches (user 2026-10-02, edit v5: "you can add more videos if needed cause sometimes its
noticable the slowdowns", and L049 "this feels like an image only").

Where edit v4 slowed a take's speech-free picture below about ×0.7 to make room for the narration, edit v5 cuts away
instead: the take plays at its own speed up to the middle of that stretch, a new insert of the same scene fills the
time the slow-down used to buy, then the take picks up where it left off. The sound under the insert is the take's own
(music out), so the room never drops. Each insert is one Seedance 2.5 call on the scene's own ingredients, silent
(no dialogue, generate_audio false), one small action, the camera locked.

L049: SHOT 2 of SC08-T3 v4 (the strap on Her's knee) is a locked ECU where the finger barely moves and the last 1.6 s
freeze. Its picture is replaced by INS-L049 (Barbara's finger presses the shell, then Her straightens her leg and the
strap rides with the knee); Barbara's line stays the take's own sound.

  python3 edit/inserts.py write      # writes body/INSERTS/<id>.call.json + .prompt.txt, runs preflight
  python3 edit/inserts.py run [ids]  # generates (Kie, Seedance 2.5), unmusic check
"""
import json, re, subprocess, sys
from pathlib import Path

B = Path(__file__).resolve().parents[1]
ROOT = B.parents[1]
S = ROOT / ".claude" / "skills" / "ai-prompt-engineer" / "scripts"
DIR = B / "body" / "INSERTS"
TEMPLATE = B / "body" / "SC03" / "SC03-SH06.call.json"   # the build's silent single-shot call: rig, body, state and negatives

HER = ("Her, a slight, narrow-shouldered woman of seventy-one with a steel-grey blunt chin-length bob and a heavy straight "
       "fringe")
STRAP = ("the strap of the product photo, small and rigid — the matte-black moulded shell about 12 by 5 centimetres with "
         "two rounded peaks around a centre notch, the grey stryde wordmark toward us, a slim chrome slide at each end and "
         "the soft black knit band; it never bends, slides or changes size")

# id: base call, the take it cuts into, scene so far, the shot, state carried, focus, extra negatives, risks, duration
INSERTS = {
    "INS-SC03-A": dict(
        base="body/SC03/SC03-SH06.call.json", take="SC03-SH06", vo="L023 L024", dur=5,
        scene=("THE SCENE SO FAR, the same evening in her bedroom, one continuous moment: the bedside lamp is lit, warm "
               "2800K, the window dark blue with dusk behind the net curtains. The bottom drawer of the chest stands "
               "pulled half open, crammed with braces, sleeves and supports exactly as the drawer card shows it; the "
               "hinged brace of the prop card lies on top of the pile."),
        shot=("THE SHOT: an ECU looking straight down into the open bottom drawer from above, the pile of braces, "
              "sleeves and supports filling the frame. Her right hand, in the slate-grey cardigan sleeve, comes in from "
              "the top of frame and presses down slowly on the pile, flat-palmed, pushing it down to make it fit; the "
              "pile gives a little and springs back as her hand lifts away and leaves frame. That is all that happens."),
        state="her hand in the cardigan sleeve, the drawer half open and crammed",
        state_except="her hand has pressed the pile once and gone",
        focus="the pile of braces and sleeves is sharp; the drawer's front edge falls soft",
        neg="no bottles, no clear tubes, no drawer moving, no drawer bigger than the chest, no brand or writing in the drawer, no face in frame",
        risks=[("the pile turns into bottles (v1 of SH06)", "drawer card, braces/sleeves named, bottle negatives"),
               ("the drawer grows or moves", "drawer card, drawer negatives"),
               ("a second action", "one press, then the hand leaves")]),
    "INS-SC03-B": dict(
        base="body/SC03/SC03-SH09-10.call.json", take="SC03-SH09-10", vo="L027", dur=5,
        scene=("THE SCENE SO FAR, the same evening in her bedroom, one continuous moment: the bedside lamp is lit, warm "
               "2800K, the window dark blue with dusk behind the net curtains. Her, in the outfit of the card, sits on the "
               "near edge of the bed with the champagne-gold phone held to her right ear, listening to her sister."),
        shot=("THE SHOT: a CU at knee height, three-quarter from the front: her left hand resting on her own left knee "
              "over the flesh-tone tights, the hem of the navy knee-length skirt just above it, the pale green candlewick "
              "bedspread behind. While she listens, her fingers slowly rub the side of the knee in two small circles, "
              "then rest still on it. Her face is out of frame. That is all that happens."),
        state="sitting on the edge of the bed, the phone at her right ear",
        state_except="her left hand rubs her knee and rests",
        focus="her hand and knee are sharp; the bedspread falls soft",
        neg="no phone in the left hand, no strap, no brace on the knee, no face in frame, no bare legs",
        risks=[("she grows a second phone or the hand changes", "one phone at her right ear, out of frame; hand negatives"),
               ("bare legs instead of tights", "outfit card, tights named, negative"),
               ("a brace appears on the knee", "brace and strap negatives")]),
    "INS-SC04": dict(
        base="body/SC04/SC04-T2.call.json", take="SC04-T2", vo="L034", dur=5,
        scene=("THE SCENE SO FAR, a June evening at her granddaughter's wedding reception, one continuous evening: the "
               "fairy lights and candle jars are lit, warm 2700K, the tall windows dark blue behind the curtains; the "
               "parquet floor is full of guests dancing, and Barbara, in the outfit of her card, dances in the middle of it."),
        shot=("THE SHOT: what Her is watching, a low MEDIUM at knee height from the edge of the dance floor: Barbara from "
              "the waist down, in the outfit of her card, dancing on the parquet — the hem of the royal-blue lace midi "
              "dress swinging about her calves, her legs bending and straightening freely at the knee on every beat, her weight rocking from foot to foot, a little turn on the spot; other guests' legs move "
              "soft around her. Her face is out of frame. That is all that happens."),
        state="dancing in the middle of the floor, in the outfit of her card",
        state_except="the dance carries on",
        focus="Barbara's knees and feet are sharp; the other dancers fall soft",
        neg="no brace, no strap visible, no face in frame, no Her in frame, no stumble",
        risks=[("Barbara's outfit changes", "her wedding outfit card"),
               ("a strap or brace appears on her knees", "strap and brace negatives"),
               ("Her steps into frame", "Her-in-frame negative, 'what Her is watching'")]),
    "INS-SC05": dict(
        base="body/SC05/SC0506-T1.call.json", take="SC0506-T1", vo="L037 L039", dur=5,
        scene=("THE SCENE SO FAR, a bright morning the week after the wedding, one continuous moment in her kitchen: soft "
               "morning daylight about 5600K from the side window. Barbara, in her own gilet and navy shorts, sits at the "
               "pine table with " + STRAP + ", on her bare right knee exactly as her knee card shows it."),
        shot=("THE SHOT: an ECU low and front-on at knee height: Barbara's bare right knee filling the frame, the strap "
              "seated just below the kneecap, the bottom of the kneecap in the shell's centre notch, the shell about a "
              "third of the frame wide, the hem of her navy shorts at the top of frame. Her right index finger traces "
              "slowly along the top edge of the shell from one chrome slide to the other, then lifts away. The strap "
              "does not move. Her face is out of frame. That is all that happens."),
        state="the strap on her bare right knee, seated just below the kneecap",
        state_except="her finger has traced the shell once",
        focus="the strap and kneecap are sharp; the table leg behind falls soft",
        neg="no strap over the kneecap, no oversized strap, no strap on the left knee, no box, no packaging, no face in frame",
        risks=[("the strap grows or sits on the kneecap (FP placement)", "product photo + knee card, 'a third of the frame wide', size negatives"),
               ("the shell bends under the finger", "'rigid… never bends', the finger only traces the top edge"),
               ("the strap on the wrong knee", "'bare right knee', left-knee negative")]),
    "INS-SC07": dict(
        base="body/SC07/SC07-T.call.json", take="SC07-T", vo="L045", dur=5,
        scene=("THE SCENE SO FAR, the same bright morning, one continuous moment: soft morning daylight about 5600K "
               "through the frosted landing window; the lamps are off. Her, in the outfit of her card, wears " + STRAP +
               ", on her RIGHT knee only, exactly as her knee card shows it, her left leg bare."),
        shot=("THE SHOT: an ECU low and front-on on the stairs, a few treads below her, from the knees down: Her comes "
              "DOWN one step toward the camera — the right foot in its white plimsoll leaves the tread, the right knee "
              "bends under the strap and takes her weight as the foot lands on the next tread down, flat and sure, then "
              "the left foot follows onto the same tread. Both hands stay out of frame and free; nothing is held. "
              "THE SIDES OF THE STAIRS, as the stairs plate shows them seen from below: the dark wooden banister and its "
              "balusters run up the RIGHT side of the frame, the cream wall with its row of framed photographs on the "
              "LEFT side of the frame. That is all that happens."),
        fix=("v1 (user, 2026-10-02): \"flip this cause the stairs should be on the left side not the right\" — v1 had the "
             "banister on the left and the photo wall on the right, mirrored from the house's stairs plate and Scene 2 "
             "→ the sides written out: seen from below, the banister on the RIGHT of frame, the photo wall on the LEFT; "
             "a mirror flip of v1 is not used because it would move the strap to her left knee and reverse the wordmark"),
        state="coming down the stairs facing forwards, the strap on her right knee",
        state_except="she has come down one more step",
        focus="the right knee and the strap are sharp; the treads above fall soft",
        neg="no hand on the banister, no banister on the left of frame, no photo wall on the right of frame, no going up, no seen from behind, no strap on the left knee, no oversized strap, no face in frame",
        risks=[("she goes up instead of down", "'comes DOWN… toward the camera', going-up negative"),
               ("the strap moves or grows", "knee card, 'never bends, slides or changes size'"),
               ("a hand on the rail (L56)", "'both hands out of frame and free', banister negative")]),
    "INS-SC12": dict(
        base="body/SC11/SC12-T3.call.json", take="SC12-T3", vo="L068", dur=5,
        scene=("THE SCENE SO FAR, a weekday late morning a few weeks later, one continuous moment in the café: honeyed "
               "daylight about 4800K from the big front window on the left. One strap of the product photo lies flat on "
               "the round wooden table between the coffee cups, front side up."),
        shot=("THE SHOT: a CU looking down at a steep angle over the round table, wide enough that two coffee cups on "
              "their saucers stand either side of " + STRAP + ", lying flat on the wood, front side up, its knit band one "
              "small closed loop folded flat under the shell, smaller than either saucer. The fingertips of the friend in "
              "the mustard jacket come in from the right, rest on the shell and slide the whole strap slowly a hand's "
              "width across the wood toward the empty chair, flat the whole way, then lift off. Faces are out of frame. "
              "That is all that happens."),
        state="the strap on the table between the cups",
        state_except="it has been lifted, looked at and set back",
        focus="the strap is sharp in her fingers; the cups and window fall soft",
        neg="no strap bending, no strap stretching, no strap lifted off the table, no strap bigger than a saucer, no second strap, no box, no packaging, no face in frame",
        fix="v1 (agent): the shell bent and the band stretched open as she lifted it, and the strap read bigger than the cups → it is never lifted: fingertips slide it flat across the wood; framed from above between two saucers so its size reads against them",
        risks=[("the shell bends in her hand", "never lifted: fingertips slide it flat, 'no strap lifted' negative"),
               ("a second strap appears", "one strap, second-strap negative"),
               ("the strap grows", "'about 12 by 5 centimetres', smaller than the saucer")]),
    "INS-SC13": dict(
        base="body/SC11/SC13-T1.call.json", take="SC13-T1", vo="L071", dur=5,
        scene=("THE SCENE SO FAR, a Sunday afternoon some weeks later, one continuous moment in her kitchen: warm "
               "afternoon light about 5000K from the window over the sink; on the scrubbed pine table, the small black "
               "box of the box photo with its lid off beside it, exactly two straps lying side by side in its tray."),
        shot=("THE SHOT: an ECU, high three-quarter over the table: Her's hands, in the cream cardigan sleeves, slide the "
              "open box slowly across the wood toward the empty place opposite her, set for a guest with a cup and "
              "saucer, and leave it there, her fingers resting on the box's edge a moment before they draw back. The "
              "two straps stay in their tray. Faces are out of frame. That is all that happens."),
        state="the open box with two straps in front of her",
        state_except="she has slid the box toward the guest's place",
        focus="the box and the two straps are sharp; the far side of the table falls soft",
        neg="no third strap, no strap leaving the tray, no box growing, no face in frame",
        risks=[("a third strap or the straps fall out", "'exactly two straps… stay in their tray', negatives"),
               ("the box grows", "box photo, 'size of a paperback book'"),
               ("a second action", "one slide, then the hands draw back")]),
    "INS-L049": dict(
        base="body/SC07/SC08-T3.call.json", take="SC08-T3", vo="L049", dur=6,
        scene=("THE SCENE SO FAR, the same bright morning, one continuous moment, back in her kitchen after the stairs: "
               "soft morning daylight about 5600K from the side window. Her, in the outfit of her card, sits at the near "
               "end of the pine table with " + STRAP + ", on her RIGHT knee exactly as Image7 shows it; Barbara, in her "
               "gilet, sits across the table."),
        shot=("THE SHOT: an ECU low and front-on at knee height beside her chair: Her's bare right knee, turned a little "
              "out from under the table, the strap seated on it — the bottom of the kneecap in the shell's notch, the "
              "shell about a third of the frame wide, her dress hem above it. Barbara's hand reaches in from the right "
              "of frame and her index finger presses the shell once, right on the spot under the kneecap, and draws "
              "away; then Her slowly straightens her leg forward, the knee lifting and the foot sliding out, the strap "
              "riding with the knee exactly where it sits, and bends it back again, easy and light. Faces are out of "
              "frame. That is all that happens."),
        state="the strap on her right knee, seated just below the kneecap",
        state_except="Barbara's finger has pressed the shell and Her has straightened and bent the knee once",
        focus="the strap and kneecap are sharp, the focus holding on them as the leg moves; the chair falls soft",
        neg="no strap over the kneecap, no oversized strap, no strap on the left knee, no strap sliding, no box, no packaging, no face in frame",
        risks=[("the shot reads as a still (the user, 2026-10-02: 'this feels like an image only')", "two actions in motion: the press, then the leg straightening and bending"),
               ("the strap slides or grows as the knee moves", "'riding with the knee exactly where it sits', knee card, size negatives"),
               ("the strap on the wrong knee (FP18)", "knee card, 'RIGHT knee', left-knee negative")]),
}


def head(base):
    p = json.loads((B / base).read_text())["prompt"]
    h = p[:p.index("THE SCENE SO FAR")]
    h = h.replace("she is only ever soft in the background here", "in this shot she is seen from the waist down")
    return re.sub(r"@audio\d is .*?in this shot\. ", "", h)


def body_parts():
    t = json.loads(TEMPLATE.read_text())["prompt"]
    rig = t[t.index("Camera on a tripod, framed and locked"):t.index("HER still carries")]
    neg = t[t.index("NEGATIVES:"):]
    neg = neg.replace("no bottles, no clear tubes, no drawer moving, no drawer bigger than the chest, no brand or writing in the drawer, ", "")
    return rig, neg


def make(iid):
    d = INSERTS[iid]
    base = json.loads((B / d["base"]).read_text())
    rig, neg = body_parts()
    who = "BARBARA" if iid in ("INS-SC04", "INS-SC05") else "THE FRIEND" if iid == "INS-SC12" else "HER"
    prompt = (head(d["base"]) + d["scene"] + " " + d["shot"] + " " + rig
              + f"{who} still carries exactly what this scene has done to them so far: {d['state']}. None of it resets: it "
              f"is the same as in the previous shot, except {d['state_except']}. It holds in every frame. FOCUS: {d['focus']}. "
              "The blur is optical: soft and round, never smeared. The clip carries no dialogue and no voice at all: nobody "
              "speaks. " + neg.replace("NEGATIVES: ", "NEGATIVES: " + d["neg"] + ", "))
    c = {"beat": iid, "build": "stryde-half-my-age", "connector": "seedance", "model": "bytedance/seedance-2-5", "mode": 4,
         "kind": "broll", "take": iid, "insert_into": d["take"], "duration": d["dur"], "resolution": "720p", "aspect_ratio": "9:16",
         "start_image": None, "ingredients_approved": True, "files": base["files"], "audios": [], "generate_audio": False,
         "dialogue": None, "script_line": None, "vo": d["vo"], "pace": "unhurried",
         "subject_motion": "travels" if iid == "INS-SC07" else "in_place", "prefer_multi_shots": "false", "generation": 1,
         "user_go": "the user 2026-10-02: \"you can add more videos if needed cause sometimes its noticable the slowdowns\"; "
                    "\"this feels like an image only\" (L049); \"automate them just give met the final one\"",
         "risks": [{"risk": r, "prevented_by": p} for r, p in d["risks"]], "scene": base.get("scene"),
         "title": f"Insert · {d['take']}", "taste": ["HT02", "HT17", "HT18", "HT22", "HT23"], "prompt": prompt}
    if d.get("fix"):
        c["generation"] = 2; c["fix_note"] = d["fix"]
    if iid == "INS-L049":
        c["generation"] = 5
        c["fix_note"] = ("the user (2026-10-02): this feels like an image only → v4's SHOT 2 is a locked ECU where the finger "
                         "barely moves and the last 1.6 s freeze; the new picture moves the whole time (the press, then the "
                         "leg straightens and bends, the strap riding with the knee), as an insert over v4's own sound")
        c["fix_notes_all"] = base.get("fix_notes_all", []) + ["v4 (user): this feels like an image only"]
    return c


def write():
    DIR.mkdir(parents=True, exist_ok=True)
    ok = True
    for iid in INSERTS:
        c = make(iid)
        f = DIR / f"{iid}.call.json"
        f.write_text(json.dumps(c, indent=1, ensure_ascii=False))
        (DIR / f"{iid}.prompt.txt").write_text(c["prompt"])
        r = subprocess.run([sys.executable, str(S / "preflight.py"), str(f)], capture_output=True, text=True, cwd=B)
        last = [l for l in r.stdout.splitlines() if "PREFLIGHT" in l or "FAIL" in l]
        print(iid, len(c["prompt"]), "chars;", " | ".join(last))
        ok &= r.returncode == 0
    return ok


def run(ids):
    for iid in ids:
        c = json.loads((DIR / f"{iid}.call.json").read_text())
        g = c["generation"] if iid != "INS-L049" else 1
        out = DIR / f"{iid}_v{g}.mp4"
        if out.exists():
            continue
        log = DIR / f"{iid}.v{g}.kie.log"
        with open(log, "w") as lf:
            subprocess.run([sys.executable, str(S / "kie.py"), "seedance", "--prompt-file", str(DIR / f"{iid}.prompt.txt"),
                            "--ref-image", *c["files"], "--duration", str(c["duration"]), "--no-audio", "--out", str(out)],
                           stdout=lf, stderr=subprocess.STDOUT, cwd=B)
        print(iid, out.exists(), log.read_text()[-300:])


if __name__ == "__main__":
    if sys.argv[1] == "write":
        sys.exit(0 if write() else 1)
    run(sys.argv[2:] or list(INSERTS))
