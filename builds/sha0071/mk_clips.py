import json, sys
from strings import *
LISTEN = lambda name, spk, what: (f"{name} is listening, not waiting to speak. As {spk} talks, {name} takes it in: {what}. The reaction arrives a beat after the words that cause it, never before them. Mouth closed, face alive and never frozen, eyes on {spk}.")
BUS = lambda during, name, bus, pace, tell=None: (f"While {during}, {name} keeps doing one thing with their hands: {bus}, at {pace}. It is ordinary and unhurried, and the hands never stop to gesture." + (f" {tell}" if tell else ""))
STATE = {
 "PAULA": lambda ex="nothing": f"PAULA still carries exactly what this scene has done to her so far: eyes dry, hair in its low bun with the loose wisps at the temples, blazer open, the buff manila folder held against her waist in both hands with the white VISITOR badge clipped to its top corner, standing a step out from the meeting-room glass facing Robin. None of it resets: it is the same as in the previous shot, except {ex}. It holds in every frame.",
 "ROBIN": lambda ex="nothing": f"ROBIN still carries exactly what this scene has done to her so far: eyes dry, hair loose, navy blazer buttoned, the black leather padfolio held closed and low at her right hip in her right hand, standing about two metres down the corridor facing Paula. None of it resets: it is the same as in the previous shot, except {ex}. It holds in every frame."}
def DRAMA(char, moment, to, playing, entry, turn_word, turn_what, exit_, stress, voice_now, under, tell):
    return (f"{VOICE[char]} IN THIS MOMENT: {moment}. Speaking to {to}. PLAYING: {playing}. Opens {entry}; turns on the exact word '{turn_word}', where {turn_what}; exits {exit_}. Stress on '{stress}'. "
            f"VOICE NOW: {voice_now}, and matching the face in this shot. UNDER THE LINE: {under}, which leaks only through {tell}. Played small and true, for a camera close enough to see a thought. Never theatrical, never pushed, never performed to the lens. " + AUD_FILM)
def MANIFEST(frame_desc, scene_desc, chars, voices):
    if frame_desc == "MASTER": scene_desc = None
    s = f"INGREDIENTS. @image1 is the opening composition: the clip opens on exactly this framing, light and camera position, and nothing in it is re-composed. "
    n = 2
    if scene_desc and not frame_desc == "MASTER":
        s += f"@image{n} is this scene: {scene_desc}, and it sets the room, the light side, the blocking and every prop's position. "; n += 1
    for c in chars:
        s += f"@image{n} is {c.title()}: face, age, hair and build only, with the wardrobe taken from the scene frames and never from this face reference. "; n += 1
    for i, v in enumerate(voices, 1):
        s += f"@audio{i} is {v.title()}'s voice, its timbre, pitch, accent and pace, for every line {v.title()} speaks; it sets who they sound like, never how they feel in this shot. "
    return s + "These references set what things ARE; the prose below sets what HAPPENS, and nothing in them is a shot to cut to."
FOCUS = lambda plane: f"FOCUS: {plane} is in sharp focus; the room behind falls to a soft, recognisable shape. The blur is optical: soft and round, never smeared."
NEGS = lambda extra="": "NEGATIVES: " + ", ".join(x for x in [NEG_WARP, NEG_FILM, NEG_SCENECUT, NEG_DRAMA, NEG_SOUND, NEG_LIGHT_C, extra] if x)
def clip(action_prose, rig, business, listen, state, dialogue_block, focus, manifest, extra_neg=""):
    parts = [manifest, INHERIT, action_prose, rig, HOLD_C, HOLD_HC, PHYS_MOTION, business]
    if listen: parts.append(listen)
    parts += state
    parts += [focus]
    if dialogue_block: parts.append(dialogue_block)
    parts.append(NEGS(extra_neg))
    return " ".join(parts)
EMO_P = {"entry":"braced and composed, jaw set, eyes steady on Robin", "flat":"the news landed, lids heavier, mouth pressed flat"}
C = {}
# SH01 — master, Robin speaks L1
C["SC01-SH01"] = dict(kind="dialogue", duration=5, frame="F-MASTER", chars=["PAULA","ROBIN"], voices=["ROBIN"], line="Paula. Hi. Do you have a second?", subject_motion="still", prompt=clip(
 "The clip opens mid-moment: Robin has just stopped in front of Paula in the corridor. On the first frame Robin says, gently and at once: \"Paula. Hi. Do you have a second?\" Paula, holding very still, watches her face as she says it. Nobody walks; both stand exactly where they are.",
 RIG_F2,
 BUS("Robin speaks", "Robin", "her right hand tightening once on the edge of the black padfolio at her hip and easing again", "one slow squeeze across the line"),
 LISTEN("Paula", "Robin", "on 'second' her breath stops for a moment and her thumb stills on the badge, reading what Robin's face already says"),
 [STATE["ROBIN"](), STATE["PAULA"]()], 
 "DIALOGUE (Robin, verbatim): \"Paula. Hi. Do you have a second?\" " + DRAMA("ROBIN", "she has come straight from the panel with bad news and wants to give it kindly, away from anyone else", "Paula, a woman she respects and has worked beside for years", "draws aside", "warm but careful, brows lifted a little in the middle", "second", "her voice drops and slows", "holding Paula's eyes", "second", "warm, a little quieter than normal conversation, a careful breath before 'Paula', steady", "she already knows the answer is no and dreads saying it", "the one squeeze of her hand on the padfolio"),
 FOCUS("Robin's face and Paula's nearest eye"),
 MANIFEST("MASTER", "the scene master", ["PAULA","ROBIN"], ["ROBIN"])))
# SH02 — Paula OTS, L2
C["SC01-SH02"] = dict(kind="dialogue", duration=4, frame="F-PAULA-OTS", chars=["PAULA","ROBIN"], voices=["PAULA"], line="They went with someone else.", subject_motion="still", prompt=clip(
 "The clip opens mid-moment on Paula, seen past Robin's shoulder. Before Robin can say it, Paula says it for her, quietly and evenly: \"They went with someone else.\" On the last word her eyes drop to the folder in her hands.",
 RIG_F2,
 BUS("Paula speaks", "Paula", "her right thumb moving slowly along the edge of the white VISITOR badge on the folder's corner", "one slow stroke across the line", "On the word 'else' the thumb stops for a beat, then carries on."),
 None, [STATE["PAULA"](), STATE["ROBIN"]("she is seen only as a soft shoulder and hair in the foreground, not moving")],
 "DIALOGUE (Paula, verbatim): \"They went with someone else.\" " + DRAMA("PAULA", "she has read Robin's face and would rather say the verdict herself than hear it", "Robin, a decent colleague who is about to be kind to her", "pre-empts", "braced and composed, jaw set", "else", "her eyes drop to the folder", "looking down at the badge, still", "else", "low and level, dry, no catch, conversational volume, a small breath before 'They'", "the third no after twenty six years here, and shame at wearing a visitor badge in her own building", "the thumb stopping on the badge"),
 FOCUS("the nearest eye of Paula"),
 MANIFEST("", "the scene master", ["PAULA","ROBIN"], ["PAULA"]), "no lift doors behind Paula"))
# INS01 — badge insert, no dialogue
C["SC01-INS01"] = dict(kind="insert", duration=4, frame="F-INS-BADGE", chars=["PAULA"], voices=[], line=None, subject_motion="still", prompt=clip(
 "INSERT. The clip opens on Paula's hands already holding the tipped folder. Her right thumb slides slowly across the white VISITOR badge on the folder's corner, once, and comes to rest on the red band. Nothing else moves. No one speaks in this clip.",
 RIG_F2, "", None, [STATE["PAULA"]("her eyes have dropped to the folder and she has tipped it toward her")],
 None, FOCUS("the hands and the badge they hold"), MANIFEST("", "the scene master", ["PAULA"], []), "no speech, no mouth, no face in frame"))
# SH03 — Robin OTS, L3
C["SC01-SH03"] = dict(kind="dialogue", duration=4, frame="F-ROBIN-OTS", chars=["ROBIN","PAULA"], voices=["ROBIN"], line="They did. I am sorry.", subject_motion="still", prompt=clip(
 "The clip opens mid-moment on Robin, seen past Paula's shoulder. Robin answers softly and plainly: \"They did. I am sorry.\"",
 RIG_F2,
 BUS("Robin speaks", "Robin", "her right hand tightening on the edge of the padfolio at her hip", "one slow squeeze", "On the word 'sorry' the hand eases open a little."),
 None, [STATE["ROBIN"](), STATE["PAULA"]("she is seen only as a soft charcoal shoulder and the back of her bun in the foreground, not moving")],
 "DIALOGUE (Robin, verbatim): \"They did. I am sorry.\" " + DRAMA("ROBIN", "Paula has said it for her, and she will not pretend otherwise", "Paula, whom she respects", "apologises to", "caught, brows lifted in the middle", "sorry", "her eyes soften and hold", "holding Paula's eyes, sorry", "sorry", "quiet and plain, a little lower than before, unhurried, continuing from how Robin sounded on her last line", "she thinks the panel got it wrong", "the hand easing on the padfolio"),
 FOCUS("the nearest eye of Robin"),
 MANIFEST("", "the scene master", ["ROBIN","PAULA"], ["ROBIN"])))
# SH04 — Paula OTS, L4
C["SC01-SH04"] = dict(kind="dialogue", duration=4, frame="F-PAULA-OTS", chars=["PAULA","ROBIN"], voices=["PAULA"], line="That is three now.", subject_motion="still", prompt=clip(
 "The clip opens mid-moment on Paula, seen past Robin's shoulder. She lifts her eyes back to Robin and says, flat and quiet, almost to herself: \"That is three now.\"",
 RIG_F2,
 BUS("Paula speaks", "Paula", "her right thumb resting on the edge of the white VISITOR badge, pressing it once", "one press across the line"),
 None, [STATE["PAULA"]("the news has settled: her lids are a touch heavier and her mouth pressed flat"), STATE["ROBIN"]("she is seen only as a soft shoulder and hair in the foreground, not moving")],
 "DIALOGUE (Paula, verbatim): \"That is three now.\" " + DRAMA("PAULA", "counting, keeping it factual so it does not break her", "Robin, and partly herself", "deflects", "the news landed, lids heavier, mouth pressed flat", "three", "her jaw sets", "still, eyes on Robin", "three", "flatter and a little lower than her last line, level, no catch, continuing from how Paula sounded before", "three interviews, three no's, forty one applications, and a fear of what it means", "the one press of her thumb on the badge"),
 FOCUS("the nearest eye of Paula"),
 MANIFEST("", "the scene master", ["PAULA","ROBIN"], ["PAULA"]), "no lift doors behind Paula"))
# SH05 — master, Robin looks over shoulder then L5
C["SC01-SH05"] = dict(kind="dialogue", duration=8, frame="F-MASTER", chars=["PAULA","ROBIN"], voices=["ROBIN"], line="Can I tell you something I am really not meant to tell you?", subject_motion="in_place", prompt=clip(
 "The clip opens on the two women standing where they stand. Robin turns her head to glance back over her right shoulder down the corridor toward the lift, a slow look, checking nobody is there, then turns her head back to Paula, and says, lower and closer: \"Can I tell you something I am really not meant to tell you?\" Only Robin's head turns; her feet stay planted. Paula stays still, watching her.",
 RIG_F2,
 BUS("Robin speaks", "Robin", "her right hand holding the padfolio still at her hip", "unmoving through the line"),
 LISTEN("Paula", "Robin", "on 'not meant' her eyes narrow slightly, careful, and her chin lifts a fraction"),
 [STATE["ROBIN"]("she glances back down the corridor and back, her head only"), STATE["PAULA"]("the news has settled into her face: lids heavier, mouth flat")],
 "DIALOGUE (Robin, verbatim): \"Can I tell you something I am really not meant to tell you?\" " + DRAMA("ROBIN", "she has decided to break a rule to be kind", "Paula, quietly, as an ally", "confides in", "checking the corridor, uneasy", "really", "her voice drops almost to a murmur and she leans in a fraction", "waiting for Paula's permission", "really", "lower and more private than before, a little breathy, slower, continuing from her last line", "she is risking her job for this and knows it", "the backward glance down the corridor"),
 FOCUS("Robin's face and Paula's nearest eye"),
 MANIFEST("MASTER", "the scene master", ["PAULA","ROBIN"], ["ROBIN"]), "no walking, no feet moving"))
# SH06 — Paula OTS, "Please."
C["SC01-SH06"] = dict(kind="dialogue", duration=4, frame="F-PAULA-OTS", chars=["PAULA","ROBIN"], voices=["PAULA"], line="Please.", subject_motion="still", prompt=clip(
 "The clip opens mid-moment on Paula, seen past Robin's shoulder, holding Robin's eyes. After a small breath she says one word, quiet and steady: \"Please.\" Then she waits, completely still.",
 RIG_F2,
 BUS("Paula speaks", "Paula", "both hands tightening once on the folder against her waist", "one slow grip, then still"),
 None, [STATE["PAULA"]("lids heavier, mouth flat, eyes now fixed on Robin"), STATE["ROBIN"]("she is seen only as a soft shoulder and hair in the foreground, not moving")],
 "DIALOGUE (Paula, verbatim): \"Please.\" " + DRAMA("PAULA", "she wants the truth more than comfort", "Robin, who is offering to break a rule for her", "invites", "still, bracing", "Please", "she holds Robin's eyes", "waiting, very still", "Please", "quiet, low and steady, a small breath before it, continuing from her last line", "she is afraid of what she is about to hear", "the tightening of both hands on the folder"),
 FOCUS("the nearest eye of Paula"),
 MANIFEST("", "the scene master", ["PAULA","ROBIN"], ["PAULA"]), "no lift doors behind Paula"))
# SH07A — Robin low, part 1
C["SC01-SH07A"] = dict(kind="dialogue", duration=10, frame="F-ROBIN-LOW", chars=["ROBIN"], voices=["ROBIN"], line="You gave the best answers in that room. Nobody else was even close on the operations question.", subject_motion="still", prompt=clip(
 "The clip opens mid-moment on Robin, seen from low, decided now. She tells Paula, warmly and firmly, holding her eyes: \"You gave the best answers in that room. Nobody else was even close on the operations question.\" At the end she takes a small breath, as if there is more.",
 RIG_F2,
 BUS("Robin speaks", "Robin", "her right hand holding the padfolio at her hip, thumb running once along its spine", "one slow stroke across the line", "On the word 'close' the thumb stops for a beat, then carries on."),
 None, [STATE["ROBIN"]("she has checked the corridor and turned back, now decided")],
 "DIALOGUE (Robin, verbatim): \"You gave the best answers in that room. Nobody else was even close on the operations question.\" " + DRAMA("ROBIN", "she wants Paula to know she was the best, before the hard part", "Paula, as an ally telling the truth", "levels with", "decided, chin lifted a fraction", "close", "her voice firms", "a small breath, about to go on", "best", "low and private, firm and warm, unhurried, continuing from her last line", "she is ashamed of what the panel wrote", "the thumb stopping on the padfolio"),
 FOCUS("the nearest eye of Robin"),
 MANIFEST("", "the scene master", ["ROBIN"], ["ROBIN"])))
json.dump(C, open("clips.json","w"), indent=1)
for k,v in C.items(): print(k, len(v["prompt"]))
# SH07B — Paula MCU listening, Robin off screen, F1 push
C["SC01-SH07B"] = dict(kind="listener", duration=12, frame="F-PAULA-MCU", chars=["PAULA","ROBIN"], voices=["ROBIN"], line="But the note that came back was, and these are their words, she seemed tired. We want someone with more energy.", subject_motion="still", prompt=clip(
 "The clip stays on Paula the whole time. Robin, off screen to frame left and never seen, says quietly and carefully: \"But the note that came back was, and these are their words, she seemed tired. We want someone with more energy.\" Paula does not speak; her mouth stays closed. She simply stops.",
 RIG_F1(30),
 BUS("listening", "Paula", "her right thumb moving slowly along the edge of the white VISITOR badge on the folder's corner", "one slow stroke every two or three seconds", "On the word 'tired' the thumb stops, and it does not move again."),
 LISTEN("Paula", "Robin", "on 'tired' her breath stops and her eyes lose their focus a little; on 'energy' nothing moves at all — no nod, no blink held for effect, just stillness"),
 [STATE["PAULA"]("lids heavier, mouth flat, eyes fixed on Robin just off frame left")],
 "OFF-SCREEN DIALOGUE (Robin, verbatim, heard but not seen): \"But the note that came back was, and these are their words, she seemed tired. We want someone with more energy.\" " + DRAMA("ROBIN", "she is repeating the panel's words because Paula deserves the truth", "Paula, as an ally, hating every word", "confesses to", "low and careful", "tired", "her voice drops and nearly stops", "quiet, done", "tired", "low, private and slower than before, a small breath before 'she seemed tired', the words placed carefully, continuing from her last line", "she is ashamed on the company's behalf", "the pause before 'she seemed tired'"),
 FOCUS("the nearest eye of Paula"),
 MANIFEST("", "the scene master", ["PAULA","ROBIN"], ["ROBIN"]), "no lift doors behind Paula, Paula's lips never move, no second person in frame"))
# SH08 — Paula CU, "Energy."
C["SC01-SH08"] = dict(kind="dialogue", duration=4, frame="F-PAULA-CU", chars=["PAULA"], voices=["PAULA"], line="Energy.", subject_motion="still", prompt=clip(
 "The clip opens on Paula's face, completely still. After a beat she repeats one word, flat, quiet, almost a question: \"Energy.\" Then she holds, still, and does not move.",
 RIG_F2,
 BUS("she speaks", "Paula", "both hands resting still on the folder below frame, shoulders unmoving", "no movement at all"),
 None, [STATE["PAULA"]("the word has landed: eyes a little unfocused, jaw loose, face emptied")],
 "DIALOGUE (Paula, verbatim): \"Energy.\" " + DRAMA("PAULA", "the word has hit the thing she fears most about her own face", "Robin, and herself", "tests", "stopped, emptied", "Energy", "her voice almost lifts into a question and doesn't", "holding still", "Energy", "the quietest she has been, flat and low, barely above a breath, a little hollow, continuing from her last line", "twenty six years here and they saw a tired old woman", "the word almost becoming a question"),
 FOCUS("the nearest eye of Paula"),
 MANIFEST("", "the scene master", ["PAULA"], ["PAULA"]), "no lift doors behind Paula, no tears"))
json.dump(C, open("clips.json","w"), indent=1)
