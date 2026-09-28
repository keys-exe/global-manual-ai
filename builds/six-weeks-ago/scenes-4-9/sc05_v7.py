# SC05 v7 clip plan: one Seedance 2.5 clip per approved v7 frame (renders/SC05/v7).
# Each clip opens on its frame (first_frame_url) as one continuous shot; the edit cuts them together.
# Beat: (n, file-slug, speaker|None, line|None, action, rig, product, seating)
#   rig: "F2" locked tripod, "F1" slow dolly push
#   product: True when the strap is in frame
#   seating: "across" (01-04, Barbara at the door end), "move" (05-07), "beside" (08 on)
import sys, math, json
sys.path.insert(0, '.'); sys.path.insert(0, '..')
from strings import S
import voice, extras

B = [
 (1, "OPEN", None, None, "Margaret sets the ice pack down last at the end of her line of two pills, the gel and the brace, and straightens it with one finger; Barbara watches her over her mug and does not drink", "F2", False, "across"),
 (2, "B-EVERY-MORNING", "BARBARA", "You've done this every morning since I got here. Two pills, the gel, the brace and an ice pack.", "gently, counting the items off with small nods toward them; turns on 'every morning'; under the line she's worried and hides it behind the list, leaking only through her mug going still in her hands", "F2", False, "across"),
 (3, "M-ELEVEN-YEARS", "MARGARET", "For eleven years.", "flat, eyes back on her pills; stress on 'eleven'; under the line shame she won't show, leaking through a small swallow after it", "F2", False, "across"),
 (4, "B-SHOW-YOU", "BARBARA", "Can I show you something?", "quiet, deciding; she sets the mug down on the oilcloth as she asks", "F1", False, "across"),
 (5, "BACK-UP", None, None, "Barbara pushes her chair back from the table with both hands on the seat, the chair legs scraping on the vinyl, rises and stands facing Margaret", "F2", False, "move"),
 (6, "CHAIR-BEHIND", None, None, "Barbara carries her wooden chair round behind the table, holding it by the back rail against her hip, and sets it down on Margaret's left beside her, both chairs now on the far side of the table with the window behind them", "F2", False, "move"),
 (7, "SAT-BESIDE", None, None, "Barbara lowers herself onto the chair beside Margaret, a hand on the table edge to take her weight, and settles, turning toward her", "F2", False, "beside"),
 (8, "REVEAL", None, None, "Barbara draws the hem of her wide black trouser leg up above her knee in one unhurried movement; the strap is already in place just under her kneecap and stays exactly where it is; Margaret leans in a little to look", "F2", True, "beside"),
 (9, "B-ITS-CALLED-STRYDE", "BARBARA", "It's called Stryde. I had it on at the wedding. All night.", "plainly proud; stress on 'All night'; under the line she wants Margaret to remember the dance floor, leaking through a small lift of the chin", "F2", False, "beside"),
 (10, "M-LITTLE-THING", "MARGARET", "That little thing? Barbara, that can't possibly work on knees like mine.", "sceptical, almost laughing it off; turns on 'knees like mine'; under the line she's afraid to hope, leaking through a glance away at the end", "F2", False, "beside"),
 (11, "B-OWN-STAIRS", "BARBARA", "That's exactly what I said. Last winter I was sleeping on my sofa because I couldn't get up my own stairs.", "dry, unhurried; stress on 'my own stairs'; under the line the memory still stings, leaking through a breath held before 'sofa'", "F1", False, "beside"),
 (12, "M-LISTEN-STAIRS", None, None, "LISTEN: 'my own stairs' has landed; Margaret's eyes drop slowly to the pills on the table and stay there; mouth closed, a small breath out through the nose", "F2", False, "beside"),
 (13, "INSERT-BRACE", "BARBARA", "Every brace you've ever bought was made to keep you comfortable while your knee got worse.", "Barbara's hand turns the old black brace on the oilcloth a quarter turn and lets go; her voice is heard off screen, firm, leaning on 'worse'", "F2", False, "beside"),
 (14, "M-JAW-SETS", None, None, "LISTEN: on 'got worse' Margaret's jaw tightens; she looks at the brace, then back up at Barbara", "F2", False, "beside"),
 (15, "2S-SIDEWAYS", "BARBARA", "A sleeve just squeezes the knee. A brace just stops it going sideways. Does your knee hurt going sideways?", "practical, a teacher's rhythm, her flat hand tilting side to side on 'sideways'; turns on the question, eyebrows up; Margaret listens beside her", "F2", False, "beside"),
 (16, "M-NO", "MARGARET", "No.", "small, honest, a little surprised by her own answer", "F2", False, "beside"),
 (17, "B-FINGER-UNDER", "BARBARA", "It hurts coming down the stairs. Put your finger just under your kneecap.", "knowing; stress on 'down'; she points to the spot just under her own strapped kneecap, and Margaret starts to copy on her own knee", "F2", True, "beside"),
 (18, "INSERT-PRESS-IN", "BARBARA", "Two centimetres down. Press in. Feel that band?", "Margaret's forefinger presses into her trouser just below her kneecap, on the tendon, and holds there; Barbara's strapped knee stays still beside it; Barbara's voice is heard off screen, patient", "F2", True, "beside"),
 (19, "M-YES", "MARGARET", "Yes.", "quiet recognition; brows lift a fraction, eyes down on her knee", "F2", False, "beside"),
 (20, "B-THATS-THE-TENDON", "BARBARA", "That's the tendon. Every step you take lands right there. Seventeen times your bodyweight goes through it. Every stride.", "slow and weighted, one word leaned on per sentence; stress on 'right there'", "F1", False, "beside"),
 (21, "M-EVERY-STRIDE", None, None, "LISTEN: on 'every stride' Margaret breathes out slowly, her shoulders dropping, eyes lowered", "F2", False, "beside"),
 (22, "M-BONE-ON-BONE", "MARGARET", "Barbara, my knees are bone on bone. There's nothing left in there.", "despairing but quiet; turns on 'nothing left'; under the line eleven years of being told this, leaking through her voice thinning", "F2", False, "beside"),
 (23, "B-MINE-TOO", "BARBARA", "Mine too. This doesn't put anything back.", "immediate, flat and kind", "F2", False, "beside"),
 (24, "B-NO-TIME-TO-LIE", "BARBARA", "Nothing can, and anyone who tells you otherwise is lying to you. I'm seventy-four, Margaret. I haven't got time to lie to you.", "hard honesty, slowing on the last sentence; stress on 'time'; under the line she's frightened of her own age, leaking through one blink held long", "F1", False, "beside"),
 (25, "M-WHAT-DOES-IT-DO", "MARGARET", "Then what does it do?", "opening up, almost a whisper", "F2", False, "beside"),
 (26, "INSERT-WEIGHT-LANDS", "BARBARA", "It changes where the weight lands. It sits just under the kneecap, right on that band.", "Barbara's fingertip rests on the peak of the strap's shell under her kneecap and taps it once; her voice is heard off screen, plain and exact", "F2", True, "beside"),
 (27, "B-PAD-ONE-SPOT", "BARBARA", "There's a silicone pad on the inside. The pad presses on that one spot, instead of spreading the pressure around the whole knee like a sleeve does.", "explaining with her hands: one flat palm for 'the whole knee', one fingertip pressed into it for 'that one spot'", "F2", False, "beside"),
 (28, "2S-THIRTY-FOUR", "BARBARA", "It catches the weight and moves it off the worn part, before it gets to the joint. They measured it. Thirty four percent less strain, every step.", "certain, matter-of-fact, no selling; stress on 'catches'; Margaret beside her listens hard", "F2", False, "beside"),
 (29, "B-THATS-THE-SPOT", "BARBARA", "Bone on bone, arthritis, worn cartilage, meniscus. Whichever one your doctor said it was, that's the spot taking the weight.", "a list said like she's heard every one of them; stress on 'that's the spot'; behind her, on 'meniscus', Margaret almost nods", "F2", False, "beside"),
 (30, "B-NOT-THAT-SPOT", "BARBARA", "Every brace and every injection you've had was aimed at the whole knee. Not that spot. That's why nothing worked.", "slower; the turn word is 'Not that spot'; under the line she's angry on Margaret's behalf, leaking through a tightened jaw", "F1", False, "beside"),
 (31, "M-PILLS-EYES-FILL", None, None, "LISTEN: the words land; Margaret's eyes fill a little as she looks at her line of pills, one slow swallow, no tears falling", "F1", False, "beside"),
 (32, "2S-STILL-THERE", "BARBARA", "Your arthritis will still be there. The weight just won't be landing where it hurts.", "gentle, honest, her hand resting over Margaret's on the table", "F2", False, "beside"),
 (33, "M-IT-LL-SLIP", "MARGARET", "It'll slip. They all slip.", "the old objection, tired; stress on 'all'", "F2", False, "beside"),
 (34, "2S-TEN-SECONDS", "BARBARA", "It's adjustable, and it doesn't go over the joint, so there's nothing to bunch up or roll down. Ten seconds to put on.", "patient, ticking points off on two fingers; Margaret beside her watches her hands", "F2", False, "beside"),
 (35, "M-LOOKS-AT-KNEE", None, None, "LISTEN: Margaret looks down at Barbara's knee below frame, holds there a moment, then brings her eyes back up to Barbara", "F2", False, "beside"),
 (36, "B-SITS-FLAT", "BARBARA", "It sits flat under your trousers, and you forget it's there. They spent three years building it with orthopaedic surgeons.", "plain facts, no pitch; stress on 'forget'; her palm smooths the trouser leg flat over her knee", "F2", False, "beside"),
 (37, "INSERT-HANDS-STILL", "BARBARA", "Over two hundred thousand people wear one.", "Margaret's hands on the oilcloth go completely still; Barbara's voice is heard off screen, quietly, almost an afterthought", "F2", False, "beside"),
 (38, "M-HOPES-UP", "MARGARET", "I can't try another thing that doesn't work, Barbara. I can't get my hopes up again.", "quietly, the voice nearly going on 'again'; under the line she's more afraid of hope than pain, leaking through her fingers tightening", "F1", False, "beside"),
 (39, "B-WALK-DOWN-STAIRS", "BARBARA", "Then don't get your hopes up. Just put it on and walk down the stairs.", "dry kindness; stress on 'walk'", "F2", False, "beside"),
 (40, "INSERT-STRAP-IN-PALM", None, None, "Barbara presses the second strap into Margaret's open palm and lets go; Margaret's fingers close slowly around it", "F2", True, "beside"),
 (41, "2S-HAND-ON-RAIL", "BARBARA", "And keep your hand on the rail. I'm not crazy.", "deadpan; under the line affection, leaking through the corner of her mouth; Margaret holds the strap and looks at it", "F2", True, "beside"),
 (42, "M-ALMOST-SMILES", None, None, "LISTEN: Margaret looks at the strap in her hands; a small smile arrives slowly and she lets it stay; eyes on the strap", "F1", True, "beside"),
]

SEAT = {
 "across": "Blocking: Margaret sits at the window end of the table; Barbara sits at the door end with her mug. Nobody moves seat in this clip.",
 "move": "Blocking: Barbara is moving her chair from the door end of the table round BEHIND the table to Margaret's left side; she never passes in front of the table and never sits across from Margaret.",
 "beside": "Blocking: Margaret and Barbara sit side by side on the same side of the table, at the back with the window behind them, Barbara on Margaret's left. Nobody sits across the table; the near side of the table stays empty. Neither of them changes seat.",
}
NAME = {"MARGARET": "Margaret", "BARBARA": "Barbara"}
AUDIO_IDX = {"MARGARET": 1, "BARBARA": 2}


def dur(line):
    if not line:
        return 4
    w = len(line.split())
    return max(4, min(15, math.ceil(w / 2.5 + 1.2)))


def prompt(b):
    n, slug, who, line, act, rig, prod, seat = b
    # kie.ai: first_frame_url and reference_audio_urls are mutually exclusive.
    # Silent clips open on the frame (first-frame mode); speaking clips carry the frame as @image1 plus the speaker's voice master.
    if who:
        p = ["@image1 is the opening composition: the clip opens on exactly this framing, these people, this light, these props and this camera position, and nothing in it is re-composed. "
             "One continuous shot with no cuts. "
             f"@audio1 is {NAME[who]}'s voice: its timbre, pitch, accent and pace for the line she speaks; it sets who she sounds like, never how she feels in this shot."]
    else:
        p = ["The clip opens on exactly the first frame: the same framing, people, light, props and camera position, nothing re-composed. One continuous shot with no cuts."]
    p.append(SEAT[seat])
    if line and act.startswith(("Barbara's hand", "Barbara's fingertip", "Margaret's forefinger", "Margaret's hands")):
        a, _, rest = act.partition("; her voice is heard off screen") if "; her voice is heard off screen" in act else act.partition("; Barbara's voice is heard off screen")
        p.append(f"{a[0].upper()+a[1:]}. {NAME[who]} is heard off screen saying: \"{line}\" Played {rest.lstrip(', ').rstrip('.')}.")
    elif line:
        p.append(f"{NAME[who]} says: \"{line}\" Played {act}.")
    elif act.startswith("LISTEN:"):
        p.append(S["LISTEN-LINE"].replace("[NAME]", "Margaret").replace("[SPEAKER]", "Barbara")
                 .replace("[what lands, on which words, and the one named physical response]", act[7:].strip())
                 + " Silence on the soundtrack apart from the room: nobody speaks in this clip.")
    else:
        p.append(act[0].upper() + act[1:] + ". Nobody speaks in this clip; only the room and the movement are heard.")
    if who:
        p.append(f"{NAME[who]}'s voice: " + voice.VOICE[who])
    p.append(S["HOLD-C"].replace(" One small movement, completing inside the clip, subject fully in frame throughout, nothing leaving frame and returning.", ""))
    p.append(S["HOLD-HC"])
    if prod:
        p.append("The strap stays exactly as in the opening frame:a matte-black shell with a peaked notch, brushed chrome slides and the lowercase stryde wordmark; worn, it sits just under the kneecap over the patellar tendon and never slides, rotates or changes shape.")
    p.append(S["PHYS-MOTION-C"])
    p.append(S["RIG-" + rig].replace("[DISTANCE]", "20"))
    p.append(S["INHERIT-FILM"])
    p.append(S["AUD-FILM"] + " " + dict((a[0], a[2]) for a in extras.AUDIO)["L-KIT"])
    negs = [S["NEG-WARP-C"], S["NEG-SCENECUT"], S["NEG-DRAMA"], S["NEG-AUD"],
            "no microphone in frame, no boom pole, no film crew or equipment in frame, no generated music, no subtitles, no captions, no text on screen, no letterbox bars, no slow motion, no speed ramp, no actor looking into the lens",
            "nobody sitting across the table from Margaret" if seat == "beside" else "nobody walking in front of the table"]
    if prod:
        negs.append("no second unit unless one is already in the opening frame,no strap sliding, no strap rotating, no strap changing shape, no silicone pad visible")
    p.append("Avoid: " + ", ".join(negs) + ".")
    return "\n\n".join(p)


CLIPS = [dict(n=b[0], id=f"SC05-V7-C{b[0]:02d}", frame=f"SC05-V7-{b[0]:02d}-{b[1]}.png", speaker=b[2], line=b[3], dur=dur(b[3]), prompt=prompt(b)) for b in B]

if __name__ == "__main__":
    tot = sum(c["dur"] for c in CLIPS)
    print(len(CLIPS), "clips", tot, "s", "≈", tot * 63, "credits at 63/s")
    print(max(len(c["prompt"]) for c in CLIPS), "max prompt chars")
