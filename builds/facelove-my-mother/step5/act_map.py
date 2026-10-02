#!/usr/bin/env python3
"""Step-5 act map (E4) for facelove-my-mother — Mode 4 film, Seedance takes (§24K part 5), checked by takes.py / angles.py / wardrobe.py."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
L = {
 "D1": dict(source="sun low behind the hosts' house and the warm bulb swags", time="evening", arc="the wound — warm and loud, then the drop", kelvin=3800),
 "PORCH": dict(source="the party's bulb glow through the back-door glass", time="evening", arc="the wound — alone in the dark hall", kelvin=4300),
 "KITCHEN": dict(source="overcast morning through the kitchen window", time="morning", arc="the disappearing — cool, flat", kelvin=6500),
 "GATHER": dict(source="big window behind the sofa", time="afternoon", arc="the disappearing — someone else's warm room", kelvin=5600),
 "MIRROR": dict(source="cool morning through the sheer curtains over the dressing table", time="morning", arc="the disappearing — cool, flat", kelvin=6500),
 "VANITY": dict(source="soft warm daylight through the sheer curtains over the dressing table", time="afternoon", arc="the turn — warm window daylight", kelvin=5000),
 "FRONT": dict(source="low late-afternoon sun behind the camera", time="afternoon", arc="the return — gold", kelvin=4300),
 "YARD2": dict(source="low late-afternoon sun and the warm bulb swags", time="evening", arc="the return — gold into string-light dusk", kelvin=4300),
 "HERO": dict(source="soft window daylight from the left", time="afternoon", arc="offer — clean, warm", kelvin=5000),
}
rows = []
def R(beat, scene, take, **k):
    lt = L[k.pop("lt")]; ks = k.pop("key", "L")
    r = {"beat": beat, "group": scene, "scene": scene, "take": take, "type": k.pop("type", "SHOT"), "mode": 4,
         "light": dict(lt, key_side=ks, **({"why": k.pop("lwhy")} if "lwhy" in k else {}))}
    r.update(k); rows.append(r)
F = lambda plane, dof, rack=None: {"plane": plane, "dof": dof, "rack": rack, "moving_subject": False}

# ---------- SC01 THE TOAST (hook / cold open) — D1 golden hour, L-YARD ----------
R("SC01-SH01", "SC01", "SC01-T1", take_kind="multi", lt="D1", key="L", subject="C1", cast=["C1", "N", "C2", "C3", "C5", "C6", "X1"], location="L-YARD", story_day="D1",
  height="eye", side="three-quarter", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("deep", "deep"),
  why="the whole long table in one look — thirty friends, the bulbs, the cake — so the room the wound happens in is known", rig="F2",
  lines="L001", action="Greg pushes up from his chair at the table's middle, sways a little and taps his wine glass with a fork; the table turns to him smiling", pace="one push up, two taps",
  start_pos="the table full on both sides under the bulbs; Greg seated mid-table on the far side facing camera, Susan beside him on his right, Paula opposite them on the near side, the cake between Susan and Paula; everyone mid-laugh, glasses on the table",
  cut="on 'Thirty years.'", ingredients=["C1", "N", "C2", "C3", "C5", "C6", "L-YARD", "VOICE-C1", "CAKE-CARD"])
R("SC01-SH02", "SC01", "SC01-T1", lt="D1", key="L", subject="C1", cast=["C1"], location="L-YARD", story_day="D1",
  height="low", side="three-quarter", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-LOW"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="low on Greg standing over the table: charming, in charge of the room — the four seconds before the drop", rig="F2",
  lines="L001", action="Greg, standing, glass raised, warm grin, delivers the toast to the table", pace="one gesture of the glass", cut="on 'right?'")
R("SC01-SH03", "SC01", "SC01-T1", lt="D1", key="L", subject="N", cast=["N", "X1"], location="L-YARD", story_day="D1",
  height="eye", side="front", scale="MCU", fg="clean", shot=["SH-EYE"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="Susan seated, almost smiling as the glasses go up around her — the last moment she is safe", rig="F2",
  lines="L001", action="glasses rise around her; Susan almost smiles and lifts her glass an inch", pace="one small lift",
  end_pos="Greg standing beside Susan on her left (frame right), glass raised; Susan seated, glass an inch off the table; the table mid-laugh", cut="on the laughter")
R("SC01-SH04", "SC01", "SC01-T2", split="length", take_kind="one-take", lt="D1", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D1",
  height="eye", side="three-quarter", scale="CU", fg="through", shot=["SH-CU", "SH-FGFOC"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="through the soft white cake: the camera lives on her face and pushes in while his words land (director's note 1)", rig="F1",
  lines="L002,L003", action="Greg's voice above her goes quiet; her almost-smile goes; her eyes stay level, not on him; her right hand finds the edge of the table", pace="slow push-in over the whole shot, one hand move",
  start_pos="Susan seated, Greg standing on her left just out of frame, the white cake soft in the near foreground between camera and her", end_pos="Susan still, hand on the table edge, eyes level",
  cut="on 'When did that happen?'", note="Greg heard off (VN05) — never cut to him once it's cruel")
R("SC01-SH05", "SC01", "SC01-T3", split="length", take_kind="multi", lt="D1", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D1",
  height="eye", side="profile", scale="CU", fg="clean", shot=["SH-CU", "SH-PROFILE"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="profile, turned up toward him: low, just to him, the distance between them", rig="F2",
  lines="L004", action="Susan, without moving her body, says it low to him", pace="two words, a beat, two words",
  start_pos="Susan seated in profile facing frame left toward Greg standing just out of frame left", cut="on 'Sit down.'")
R("SC01-SH06", "SC01", "SC01-T3", lt="D1", key="R", subject="C2", cast=["C2"], location="L-YARD", story_day="D1",
  height="high", side="front", scale="MCU", fg="clean", shot=["SH-HIGH"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="high on Paula across the table: the one beat to her, staring at her plate — named and mortified (VN07)", rig="F2",
  lines="L005", action="Greg's loose hand enters frame edge pointing across at her; Paula keeps her eyes on her plate", pace="one hand gesture, she does not move", cut="on 'Exact same.'")
R("SC01-SH07", "SC01", "SC01-T3", lt="D1", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D1",
  height="eye", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-EYE"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="back on her, held too long: the verdict landing (director's note 1)", rig="F2",
  lines="L005", action="Susan absolutely still, eyes level, breathing once", pace="held, one breath",
  end_pos="Susan still at the table, hand on the edge; Greg standing on her left", cut="on 'That's all I'm saying.'")
R("SC01-SH08", "SC01", "SC01-T4", split="length", take_kind="multi", lt="D1", key="L", subject="X1", cast=["N", "C1", "C2", "X1"], location="L-YARD", story_day="D1",
  height="high", side="three-quarter-back", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-HIGH"], speaking=False, face=False, product_beat=False, focus=F("deep", "deep"),
  why="high behind Susan: the whole table gone silent, Greg small — thirty forks not moving (VN08)", rig="F2",
  lines="", action="Greg drops back into his chair and reaches past the cake for his drink; nobody at the table moves", pace="one sit, one reach",
  start_pos="Greg standing beside Susan, the table frozen", cut="on the silence")
R("SC01-SH09", "SC01", "SC01-T4", type="INSERT", lt="D1", key="L", subject="CAKE", cast=[], location="L-YARD", story_day="D1",
  height="high", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-HIGH"], speaking=False, face=False, product_beat=False, focus=F("foreground", "shallow"),
  why="the untouched cake, a fork resting beside it — the silent thread planted", rig="F2",
  lines="", action="nothing moves; the bulb light flickers faintly on the white frosting", pace="still",
  end_pos="Greg seated with his drink, Susan beside him still, the cake untouched", cut="title 'YOU LOOK LIKE MY MOTHER.' lands (VN03)", ingredients=["L-YARD", "CAKE-CARD"])

# ---------- SC02 THE WHISPER — D1, L-YARD → deck ----------
R("SC02-SH01", "SC02", "SC02-T1", take_kind="multi", lt="D1", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D1",
  height="eye", side="three-quarter", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-34"], speaking=False, face=True, product_beat=False, focus=F("hands", "medium"),
  why="her hands, calm: folding the napkin is the restraint", rig="F2", lines="", action="Susan stands, folds her napkin once and sets it beside the cake", pace="stand, one fold, set down",
  start_pos="Susan seated at the table, napkin in her lap, the cake in front of her", cut="on the napkin down", ingredients=["N", "L-YARD", "CAKE-CARD"])
R("SC02-SH02", "SC02", "SC02-T1", lt="D1", key="R", subject="C5", cast=["C5", "C6", "N"], location="L-YARD", story_day="D1",
  height="eye", side="profile", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-PROFILE"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="the two friends in profile at the drinks table, heads together — Susan passes soft behind them mid-step (VN10)", rig="F2",
  lines="L006", action="Friend A, low, to Friend B; behind them Susan walks past toward the deck, soft", pace="Susan one step a second", cut="on 'of him.'")
R("SC02-SH03", "SC02", "SC02-T1", lt="D1", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D1",
  height="eye", side="front", scale="MCU", fg="clean", shot=["SH-EYE"], speaking=False, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="leading her face as she walks: she hears it and doesn't break stride", rig="F5",
  lines="L007", action="Susan walking toward the camera at a steady pace; her eyes flick once, she keeps walking", pace="one step a second, 4 steps",
  cut="on 'sad to watch.'", note="Friend B heard over her (off)")
R("SC02-SH04", "SC02", "SC02-T1", lt="D1", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D1",
  height="low", side="behind", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-REAR"], speaking=False, face=False, product_beat=False, focus=F("deep", "deep"),
  why="from behind and low on the lawn: she climbs the three deck steps and goes in; the door clicks shut", rig="F2",
  lines="", action="Susan climbs the three deck steps, opens the glass-paned back door and closes it behind her", pace="three steps, one door",
  end_pos="the back door shut, Susan gone inside; the party behind the camera", cut="on the door click (SFX)")

# ---------- SC03 INSIDE / THE VO — D1 dusk, L-PORCH-IN ----------
R("SC03-SH01", "SC03", "SC03-T1", take_kind="multi", lt="PORCH", key="back", lwhy="her back to the lit glass: the party is behind her, she is in the dark", subject="N", cast=["N"], location="L-PORCH-IN", story_day="D1",
  height="high", side="front", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-HIGH"], speaking=False, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="a little above her, small against the door: her back against the shut door, the party glow behind the glass, her face half in the dark (VN11)", rig="F2",
  lines="L008", action="Susan leans back against the shut door, eyes closed, one slow breath out", pace="one breath",
  start_pos="Susan just inside the shut back door, her back to the glass, the party glow behind her head", cut="on 'everyone we know.'", ingredients=["N", "L-PORCH-IN", "L-YARD"])
R("SC03-SH02", "SC03", "SC03-T1", lt="PORCH", key="back", lwhy="the glow only rims her; the near cheek in shadow", subject="N", cast=["N"], location="L-PORCH-IN", story_day="D1",
  height="eye", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-34"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="closer, half her face in dark: the VO's turn — they'd already decided", rig="F1",
  lines="L008", action="she opens her eyes and looks at nothing; jaw set", pace="slow push-in", end_pos="Susan against the door, eyes open", cut="on 'the same thing.'")

# ---------- SC04 DISAPPEARING — D2 morning (kitchen + mirror), D3 the birthday ----------
R("SC04-SH01", "SC04", "SC04-T1", type="INSERT", take_kind=None, lt="KITCHEN", key="R", subject="N-HANDS", cast=["N"], location="P-HOUSE", story_day="D2",
  height="high", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-HIGH"], speaking=False, face=False, product_beat=False, focus=F("hands", "shallow"),
  why="her hand on the island: the invite turned face-down, the phone laid on top — 'I stopped going. Muted the group chat.'", rig="F2",
  lines="L009", action="her hand turns a party invite face-down on the granite and sets her phone face-down on top of it", pace="one turn, one set-down",
  start_pos="a plain invite card face-up on the kitchen island, her hand coming in", end_pos="invite face-down under the phone, her hand leaving", cut="on 'Muted the group chat.'", ingredients=["N", "P-HOUSE", "INVITE-CARD"])
R("SC04-SH02", "SC04", "SC04-T2", take_kind=None, lt="GATHER", key="L", subject="N", cast=["N", "C4", "X2"], location="L-GATHERING", story_day="D3",
  height="eye", side="behind", scale="FULL", fg="clean", shot=["SH-REAR"], speaking=False, face=False, product_beat=False, focus=F("background", "medium"),
  why="behind her, holding the phone up: the family on the sofa in the photo and her outside it — 'Skipped the birthdays' (VN13)", rig="F2",
  lines="L009", action="the daughter waves her into the photo; Susan shakes her head, raises the phone and takes the picture of them, one step back", pace="one wave, one step back",
  start_pos="the family on the grey sectional around the cake, the daughter in the middle; Susan standing in the clear floor with the phone", end_pos="Susan one step further back, phone up", cut="on 'Skipped the birthdays.'", ingredients=["N", "C4", "L-GATHERING"])
R("SC04-SH03", "SC04", "SC04-T3", take_kind="multi", lt="MIRROR", key="R", subject="N", cast=["N"], location="L-VANITY", story_day="D2",
  height="eye", side="front", scale="MCU", fg="reflection", shot=["SH-EYE"], speaking=False, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="in the mirror: the morning ritual, the mirror agreeing with them", rig="F2",
  lines="L009", action="Susan at the dressing table dabs foundation from a plain unlabelled bottle onto her cheek with a sponge", pace="three slow dabs",
  start_pos="Susan seated on the stool at the dressing table facing the mirror, a plain unlabelled foundation bottle and a sponge on the table", cut="on 'agreed with them,'", ingredients=["N", "L-VANITY", "OLD-FOUNDATION-CARD"])
R("SC04-SH04", "SC04", "SC04-T3", type="INSERT", lt="MIRROR", key="R", subject="N-SKIN", cast=["N"], location="L-VANITY", story_day="D2",
  height="eye", side="three-quarter", scale="ECU", fg="clean", shot=["SH-MACRO"], speaking=False, face=True, product_beat=False, focus=F("foreground", "shallow"),
  why="macro on the smile line: the old foundation caking grey into it — the villain is the formula", rig="F2",
  lines="L009", action="the beige foundation sits grey and dry in the crease beside her mouth, flaking at the edges as she smiles slightly", pace="still, one small smile", cut="on 'every line I owned,'")
R("SC04-SH05", "SC04", "SC04-T3", lt="MIRROR", key="R", subject="N", cast=["N"], location="L-VANITY", story_day="D2",
  height="eye", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-34"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="she stops mid-application and just stops — the low point, held", rig="F2",
  lines="L009", action="the sponge stops halfway to her face; she lowers it slowly and just looks", pace="one stop, held", end_pos="Susan at the dressing table, sponge lowered, still", cut="on 'the word he used.'")

# ---------- SC05 BETH — D4 afternoon, L-VANITY / L-VANITY-REV ----------
R("SC05-SH01", "SC05", "SC05-T1", take_kind="multi", lt="VANITY", key="R", subject="C3", cast=["C3", "N"], location="L-VANITY", story_day="D4",
  height="eye", side="profile", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-PROFILE"], speaking=True, face=True, product_beat=False, focus=F("deep", "medium"),
  why="the plate's own view from the doorway: Beth walks in past the camera without knocking, garment bag over her shoulder, and stops in profile facing Susan (VN15)", rig="F2",
  lines="L010", action="Beth walks in from behind the camera, garment bag over her shoulder, stops in profile between the bed and the dressing table, looks at Susan and says it plainly", pace="three steps in, stops",
  start_pos="Susan sitting on the end of the bed (frame left) in her sweatshirt, facing the room; the dressing table and mirror on the right under the window; Beth just behind the camera in the doorway", cut="on 'You're coming.'", ingredients=["C3", "N", "L-VANITY", "VOICE-C3"])
R("SC05-SH02", "SC05", "SC05-T1", lt="VANITY", key="R", subject="N", cast=["N"], location="L-VANITY", story_day="D4",
  height="high", side="three-quarter", scale="MCU", fg="clean", shot=["SH-HIGH", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="high on her sitting on the bed: small, not moving — 'compare me to Paula again'", rig="F2",
  lines="L011", action="Susan doesn't get up; she says it to her hands", pace="still", end_pos="Susan on the end of the bed, Beth inside the door with the garment bag", cut="on 'Everyone saw it.'")
R("SC05-SH03", "SC05", "SC05-T2", split="length", take_kind="multi", lt="VANITY", key="L", subject="C3", cast=["C3"], location="L-VANITY", story_day="D4",
  height="eye", side="three-quarter", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="Beth easy and honest: agreeing with what Susan saw (the trust unlock)", rig="F2",
  lines="L012", action="Beth lays the garment bag on the bed and talks while she does it", pace="one lay-down",
  start_pos="Beth standing by the bed with the garment bag; Susan on the end of the bed", cut="on 'in twelve weeks.'")
R("SC05-SH04", "SC05", "SC05-T2", lt="VANITY", key="L", subject="C3", cast=["C3", "N"], location="L-VANITY", story_day="D4",
  height="eye", side="profile", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-PROFILE"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="softer, in profile: she pulls the stool out from the dressing table — 'Come sit. Watch this.'", rig="F2",
  lines="L013", action="Beth pulls the dressing-table stool out with one hand and nods Susan to it; Susan gets up from the bed and sits", pace="one pull, Susan three steps",
  end_pos="Susan seated on the stool facing the mirror; Beth standing at her left shoulder", cut="on 'Watch this.'")
R("SC05-SH05", "SC05", "SC05-T3", split="length", take_kind="multi", lt="VANITY", key="R", subject="C3", cast=["C3", "N"], location="L-VANITY", story_day="D4",
  height="high", side="three-quarter", scale="MCU", fg="clean", shot=["SH-34", "SH-HIGH"], speaking=True, face=True, product_beat=True, focus=F("product", "shallow"),
  why="high over the dressing table, the stick handed over like a secret: Beth tilts Susan's chin to the light and takes it out, her hand over the wordmark (VN16, F10)", rig="F2",
  lines="L014", action="Beth tilts Susan's chin to the window with two fingers, takes the closed violet stick from her pocket, her palm over the wordmark, and pulls the cap off the balm end", pace="one tilt, one cap off",
  start_pos="Susan seated facing the mirror, Beth at her left shoulder", end_pos="the balm end uncapped in Beth's right hand at Susan's cheek", cut="on 'made for us.'", ingredients=["C3", "N", "L-VANITY", "PROD-CLOSED", "PROD-BALM", "PROD-HAND-CARD"])
R("SC05-SH06", "SC05", "SC05-T4", split="insert", take_kind=None, type="INSERT", lt="VANITY", key="R", subject="PRODUCT", cast=["N", "C3"], location="L-VANITY", story_day="D4",
  height="eye", side="profile", scale="ECU", fg="clean", shot=["SH-MACRO", "SH-PROFILE"], speaking=False, face=True, product_beat=True, focus=F("product", "shallow"),
  why="macro in profile: one swipe up her cheek — a white stripe (VN17)", rig="F2",
  lines="L014", action="the balm's flat crest draws one white stripe up Susan's cheekbone", pace="one swipe, two seconds",
  start_pos="the balm end at her cheekbone", end_pos="a white stripe on her cheek, the stick lifting away", cut="on 'don't panic.'", ingredients=["N", "PROD-BALM", "COLOUR-FRONT-CARD"], note="Beth heard (off) — her mouth not in frame")
R("SC05-SH07", "SC05", "SC05-T5", split="insert", take_kind=None, type="INSERT", lt="VANITY", key="R", subject="PRODUCT", cast=["N", "C3"], location="L-VANITY", story_day="D4",
  height="eye", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-EYE"], speaking=False, face=True, product_beat=True, focus=F("product", "shallow"),
  why="the colour change in one continuous take, no cut (VN17): white ahead of the brush, her shade behind it", rig="F2",
  lines="L015", action="the brush end works the white stripe in small circles; behind the brush the white turns to her own skin tone, ahead of it the stripe stays white", pace="slow small circles, four seconds",
  start_pos="a white stripe on her cheek, the brush end touching its lower end", end_pos="the cheek evened, every line still there", cut="on 'cracking on top.'", ingredients=["N", "PROD-BRUSH", "COLOUR-FRONT-CARD"], note="one continuous take, no speed change; Beth heard (off)")
R("SC05-SH08", "SC05", "SC05-T6", split="insert", take_kind="multi", lt="VANITY", key="R", subject="C3", cast=["C3", "N"], location="L-VANITY", story_day="D4",
  height="eye", side="three-quarter", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="Beth steps back so Susan can see the mirror: cover, not erase — said plainly (L016)", rig="F2",
  lines="L016", action="Beth steps back one step behind Susan's shoulder and talks to her reflection", pace="one step back",
  start_pos="Susan seated facing the mirror, Beth at her left shoulder holding the closed stick", cut="on 'the first thing anyone sees.'")
R("SC05-SH09", "SC05", "SC05-T6", lt="VANITY", key="R", subject="N", cast=["N"], location="L-VANITY", story_day="D4",
  height="eye", side="front", scale="CU", fg="reflection", shot=["SH-CU", "SH-EYE"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="in the mirror: she stares at her own cheek, evened out, every line still there (VN19)", rig="F1",
  lines="L016", action="Susan leans an inch toward the mirror and looks at her cheek", pace="one lean", cut="on 'Thirty seconds.'")
R("SC05-SH10", "SC05", "SC05-T6", lt="VANITY", key="R", subject="N", cast=["N"], location="L-VANITY", story_day="D4",
  height="low", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-LOW"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="low and close: quiet disbelief — 'this is all you did?'", rig="F2",
  lines="L017", action="Susan turns her head a little toward Beth", pace="one turn", end_pos="Susan turned a little toward Beth", cut="on 'all you did?'")
R("SC05-SH11", "SC05", "SC05-T7", split="length", lt="VANITY", key="R", subject="C3", cast=["C3"], location="L-VANITY", story_day="D4",
  height="eye", side="three-quarter", scale="MCU", fg="clean", shot=["SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="Beth, plain: 'This is all I did.'", rig="F2",
  lines="L018", action="Beth nods once and says it", pace="one nod", start_pos="Susan seated at the mirror turned a little toward Beth behind her left shoulder", end_pos="Susan seated at the mirror, Beth standing behind her left shoulder", cut="on 'all I did.'")

# ---------- SC06 THERE SHE IS — D4, L-VANITY ----------
R("SC06-SH01", "SC06", "SC06-T1", take_kind="multi", lt="VANITY", key="R", subject="N", cast=["N"], location="L-VANITY", story_day="D4",
  height="low", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-LOW"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="a touch low, resolve — from beside the mirror, her eyes on her reflection just off the lens: not flinching for the first time (VN20)", rig="F1",
  lines="L019", action="Susan holds her own eyes in the mirror and says it almost to nothing", pace="still, slow push-in",
  start_pos="Susan seated at the mirror, Beth behind her left shoulder", cut="on 'there she is.'")
R("SC06-SH02", "SC06", "SC06-T1", lt="VANITY", key="R", subject="C3", cast=["C3", "N"], location="L-VANITY", story_day="D4",
  height="eye", side="ots", scale="MEDIUM", fg="reflection", shot=["SH-OTS", "SH-MED"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="over Susan's shoulder into the mirror: Beth behind her in the reflection — the mirror gives her back", rig="F2",
  lines="L020", action="Beth, in the reflection, rests a hand on Susan's shoulder and says it", pace="one hand down", end_pos="the two of them in the mirror, Beth's hand on Susan's shoulder", cut="on 'didn't believe them.'")

# ---------- SC07 SHE WALKS BACK IN — D5 Saturday ----------
R("SC07-SH01", "SC07", "SC07-T1", take_kind="multi", lt="FRONT", key="R", subject="CAR", cast=["N", "C3"], location="L-HOSTS-FRONT", story_day="D5",
  height="eye", side="profile", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-PROFILE"], speaking=False, face=False, product_beat=False, focus=F("deep", "deep"),
  why="across the street: her car at the curb, engine off, the balloons on the mailbox — 'The same yard I'd been hiding from'", rig="F2",
  lines="L021", action="a silver sedan sits parked at the curb outside the house; nobody gets out", pace="still",
  start_pos="the car parked at the curb in front of the house, Susan at the wheel, Beth in the passenger seat", cut="on 'for months.'", ingredients=["N", "C3", "L-HOSTS-FRONT", "L-YARD"])
R("SC07-SH02", "SC07", "SC07-T1", lt="FRONT", key="R", subject="N", cast=["N", "C3"], location="L-HOSTS-FRONT", story_day="D5",
  height="eye", side="three-quarter", scale="MCU", fg="through", shot=["SH-OCCL", "SH-34"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="through the driver's window: her hands on the wheel, Beth's hand on her arm — 'I almost turned the car around'", rig="F2",
  lines="L021", action="Susan's hands tighten on the wheel; Beth lays a hand on her forearm; Susan breathes out and takes the key out", pace="one tighten, one touch, one breath",
  end_pos="Susan and Beth in the car, about to get out", cut="on 'the car around.'")
R("SC07-SH03", "SC07", "SC07-T2", take_kind="multi", lt="YARD2", key="L", subject="N", cast=["N", "C3", "C5", "X1"], location="L-YARD", story_day="D5",
  height="eye", side="front", scale="WIDE", fg="clean", shot=["SH-WIDE"], speaking=False, face=True, product_beat=False, focus=F("deep", "deep"),
  why="the same yard, the same table: she comes in with Beth; conversation stalls, then Friend A lights up (VN21)", rig="F6",
  lines="", action="Susan and Beth walk in from the side of the house onto the lawn; heads at the table turn; the talk stops, then Friend A's face lights up", pace="four steps, heads turn",
  start_pos="the party at the long table under the bulbs, the cake on the table; Susan and Beth at the corner of the house", cut="on Friend A's smile", ingredients=["N", "C3", "C5", "C2", "L-YARD", "L-YARD-REV"], mirror_of="SC01-SH01")
R("SC07-SH04", "SC07", "SC07-T2", lt="YARD2", key="L", subject="C2", cast=["C2", "N"], location="L-YARD", story_day="D5",
  height="eye", side="three-quarter", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="Paula crosses to her first, both hands out — the boomerang (VN21)", rig="F5",
  lines="L022", action="Paula crosses the lawn to Susan, both hands out, and takes her hands", pace="five steps, hands out",
  end_pos="Paula and Susan facing each other on the lawn, holding hands", cut="on 'what are you doing?'")
R("SC07-SH05", "SC07", "SC07-T3", split="length", take_kind="multi", lt="YARD2", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D5",
  height="eye", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="easy, the smallest smile: the line that pays off 'ask her what she does'", rig="F2",
  lines="L023", action="Susan, holding Paula's hands, says it lightly", pace="still", start_pos="Paula and Susan facing each other on the lawn, holding hands", cut="on 'come ask you.'")
R("SC07-SH06", "SC07", "SC07-T3", lt="YARD2", key="L", subject="C2", cast=["C2", "N", "C1"], location="L-YARD", story_day="D5",
  height="eye", side="profile", scale="MEDIUM", fg="clean", shot=["SH-MED", "SH-PROFILE"], speaking=False, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="the two women laughing in profile; Greg small at the edge of the yard behind them, soft, going still (VN22)", rig="F2",
  lines="", action="Paula catches it, a surprised breath, then a real laugh, the two of them laughing together; far behind, Greg goes still", pace="one laugh",
  cut="on the laugh")
R("SC07-SH07", "SC07", "SC07-T3", type="INSERT", lt="YARD2", key="L", subject="CAKE", cast=["X1"], location="L-YARD", story_day="D5",
  height="high", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-HIGH"], speaking=False, face=False, product_beat=False, focus=F("foreground", "shallow"),
  why="the rhyme: the same cake shot, now being cut and passed — life moving (VN23)", rig="F2", mirror_of="SC01-SH09",
  lines="", action="a knife cuts a slice from the white sheet cake and a hand passes the plate along", pace="one cut, one pass",
  end_pos="the party going on, Susan and Paula together on the lawn", cut="on the pass", ingredients=["L-YARD", "CAKE-CARD"])

# ---------- SC08 THE REDIRECT — D5 dusk, L-YARD ----------
R("SC08-SH01", "SC08", "SC08-T1", take_kind="multi", lt="YARD2", key="R", subject="C1", cast=["C1", "N"], location="L-YARD", story_day="D5",
  height="eye", side="ots", scale="MEDIUM", fg="through", shot=["SH-OTS", "SH-MED"], speaking=True, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="over Susan's shoulder on Greg, quiet now at her shoulder: ashamed, human", rig="F2",
  lines="L024", action="Greg, at her shoulder, speaks low; his hand half lifts and drops", pace="one half-lift",
  start_pos="Susan standing on the lawn near the table with Beth and Paula a step away; Greg arriving at her right shoulder", cut="on 'Maybe we could talk—'", ingredients=["C1", "N", "C3", "C2", "L-YARD", "VOICE-C1", "VOICE-N"])
R("SC08-SH02", "SC08", "SC08-T1", lt="YARD2", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D5",
  height="eye", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-34"], speaking=True, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="kind, done: one line, no anger", rig="F2", lines="L025", action="Susan looks at him, kind, and says it", pace="still", cut="on 'Greg.'")
R("SC08-SH03", "SC08", "SC08-T1", lt="YARD2", key="L", subject="N", cast=["N", "C3", "C2", "C1"], location="L-YARD", story_day="D5",
  height="eye", side="three-quarter-back", scale="FULL", fg="clean", shot=["SH-REAR"], speaking=False, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="she turns back to Beth and Paula, laughing before he's finished; Greg left standing (VN24)", rig="F2",
  lines="L026", action="Susan turns away to Beth and Paula and laughs with them; Greg stays where he is", pace="one turn",
  end_pos="Susan with Beth and Paula by the table, Greg alone two steps behind", cut="on 'take him back.'")
R("SC08-SH04", "SC08", "SC08-T2", split="length", take_kind=None, lt="YARD2", key="L", subject="N", cast=["N", "C3", "C2", "C5", "C6", "C1", "X1"], location="L-YARD", story_day="D5",
  height="high", side="three-quarter", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-HIGH"], speaking=False, face=True, product_beat=False, focus=F("deep", "deep"),
  why="high wide — the rhyme of the frozen table: Susan in the middle of her friends under the bulbs, lit up; Greg alone at the edge (VN25)", rig="F1",
  lines="L026", action="Susan in the middle of the group by the table, talking and laughing; Greg alone at the edge of the lawn", pace="slow crane-down push",
  mirror_of="SC01-SH08", start_pos="Susan with Beth and Paula by the table, friends around; Greg alone two steps behind", end_pos="the same", cut="on 'counted me out.'")

# ---------- SC09 CTA + OFFER ----------
R("SC09-SH01", "SC09", "SC09-T1", take_kind="multi", lt="YARD2", key="L", subject="N", cast=["N", "C3", "C2"], location="L-YARD", story_day="D5",
  height="eye", side="three-quarter", scale="MCU", fg="through", shot=["SH-34", "SH-FGFOC"], speaking=False, face=True, product_beat=False, focus=F("eyes", "medium"),
  why="the cake going around: a plate passed to her past a friend's shoulder, she takes it laughing", rig="F2",
  lines="L027", action="a plate of cake is passed to Susan; she takes it, laughing at something Beth says", pace="one pass",
  start_pos="Susan at the table between Beth and Paula", end_pos="Susan with a plate of cake, laughing", cut="on 'the skin we have now.'", ingredients=["N", "C3", "C2", "L-YARD", "CAKE-CARD"])
R("SC09-SH02", "SC09", "SC09-T2", lt="YARD2", key="L", subject="X1", cast=["N", "C3", "C2", "C5", "C6", "X1"], location="L-YARD-REV", story_day="D5",
  height="eye", side="front", scale="WIDE", fg="clean", shot=["SH-WIDE", "SH-EYE"], speaking=False, face=True, product_beat=False, focus=F("deep", "deep"),
  why="from the deck down the full table into the dusk: the whole group, Susan in the middle of it", rig="F2",
  lines="L027", action="the long table full, people passing cake and talking under the bulbs", pace="still camera, life moving", start_pos="the long table full under the bulbs, Susan in the middle between Beth and Paula", end_pos="the table full", cut="on 'are on it.'")
R("SC09-SH03", "SC09", "SC09-T3", type="INSERT", take_kind=None, lt="HERO", key="L", subject="PRODUCT", cast=[], location="PRODUCT", story_day="P",
  height="high", side="front", scale="CU", fg="clean", shot=["SH-CU", "SH-HIGH"], speaking=False, face=False, product_beat=True, focus=F("product", "shallow"),
  why="a little above, the soft hero: two closed sticks and the primer tube on a pale surface — the offer, seen (VN26)", rig="F1",
  lines="L027", action="two closed violet sticks standing upright beside the white primer tube on a pale stone surface; slow push-in", pace="slow push-in",
  start_pos="the three products on the surface, wordmarks to camera", end_pos="the same, closer", cut="on 'thirty day guarantee.'", ingredients=["PROD-CLOSED", "PROD-PRIMER", "HERO-CARD"])
R("SC09-SH04", "SC09", "SC09-T4", take_kind=None, lt="YARD2", key="L", subject="N", cast=["N"], location="L-YARD", story_day="D5",
  height="low", side="three-quarter", scale="CU", fg="clean", shot=["SH-CU", "SH-LOW"], speaking=False, face=True, product_beat=False, focus=F("eyes", "shallow"),
  why="low and close, the bulbs behind her: lit up among her friends — the last word is hers", rig="F2",
  lines="L027", action="Susan, laughing with someone off frame, glances down at the table and smiles to herself", pace="one glance", start_pos="Susan at the table under the bulbs, friends around her", end_pos="the same, Susan smiling", cut="on 'The link's below.'", ingredients=["N", "L-YARD"])

MUS = {'SC01': 'none (room tone — script VN07)', 'SC02': 'none (room tone — script: no music under the heaviest beats)', 'SC03': 'MUS-OPEN', 'SC04': 'MUS-EXPOSE', 'SC06': 'MUS-AFTER', 'SC07': 'MUS-AFTER', 'SC08': 'MUS-AFTER', 'SC09': 'MUS-OFFER'}
DUR = {'SC01-SH01': 4, 'SC01-SH02': 5, 'SC01-SH03': 3, 'SC01-SH04': 13, 'SC01-SH05': 3, 'SC01-SH06': 6, 'SC01-SH07': 6, 'SC01-SH08': 4, 'SC01-SH09': 3, 'SC02-SH01': 3, 'SC02-SH02': 3, 'SC02-SH03': 5, 'SC02-SH04': 4, 'SC03-SH01': 7, 'SC03-SH02': 8, 'SC04-SH01': 5, 'SC04-SH02': 4, 'SC04-SH03': 4, 'SC04-SH04': 3, 'SC04-SH05': 4, 'SC05-SH01': 5, 'SC05-SH02': 6, 'SC05-SH03': 9, 'SC05-SH04': 5, 'SC05-SH05': 10, 'SC05-SH06': 3, 'SC05-SH07': 8, 'SC05-SH08': 7, 'SC05-SH09': 6, 'SC05-SH10': 2, 'SC05-SH11': 2, 'SC06-SH01': 3, 'SC06-SH02': 5, 'SC07-SH01': 3, 'SC07-SH02': 4, 'SC07-SH03': 5, 'SC07-SH04': 5, 'SC07-SH05': 3, 'SC07-SH06': 4, 'SC07-SH07': 3, 'SC08-SH01': 5, 'SC08-SH02': 2, 'SC08-SH03': 4, 'SC08-SH04': 7, 'SC09-SH01': 6, 'SC09-SH02': 5, 'SC09-SH03': 8, 'SC09-SH04': 5}
for r in rows:
    r["duration"] = DUR[r["beat"]]
    r["music"] = MUS.get(r["scene"]) or ("MUS-TURN" if r["beat"] == "SC05-SH05" else "MUS-AFTER" if r["beat"] > "SC05-SH05" else "MUS-EDU")
    if r["beat"] == "SC04-SH05": r["music"] = "none (drops out on the mirror — VN14)"
    r.setdefault("mirror_of", None); r.setdefault("ingredients", sorted(set(r.get("cast", [])) | {r["location"]}))
json.dump(rows, open(HERE / "act_map.json", "w"), indent=1, ensure_ascii=False)
print(len(rows), "rows,", len({r["take"] for r in rows}), "takes")
