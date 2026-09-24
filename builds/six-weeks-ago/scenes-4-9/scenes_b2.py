# Scenes 4-9 (SC05-SC11) + end card. Film coverage only, no B-roll.
# Frame: id, scale, rig, who(list in frame), desc (blocking/action at the frozen moment), emo {NAME: physical state}, product (None|'reveal-B'|'worn-M'|'held'|'reveal-M'|'palm'), key (True = scene master)
# Clip: id, frame (opening), shots[(scale, rig, speaker|None, line|None, direction)], dur
SC = {}

SC["SC05"] = dict(title="Scene 4 · Kitchen, a week later", day="D3", loc="L-KIT", house=True,
 time="breakfast time on a weekday", light="soft cool morning daylight from the west window at the far end of the galley, no direct sun",
 blocking="Margaret sits at the window end of the drop-leaf table facing down the galley; Barbara sits at the door end, side-on to camera, a mug in both hands",
 axis="along the table between the two women", side="cabinet (left)",
 props="two pills, a tube of gel, a knee brace and an ice pack lined up on the oilcloth in front of Margaret; Barbara's mug",
 cast=["MARGARET","BARBARA"], vis={"BARBARA":"left","MARGARET":"right"},
 frames=[
  dict(id="SC05-F01-MASTER", scale="WIDE", rig="F2", key=True, who=["MARGARET","BARBARA"],
   desc="Margaret is setting the last item, the ice pack, into her morning line on the table; Barbara watches over her mug",
   emo={"MARGARET":"a practised, flat routine: jaw set, eyes down on her hands, shoulders rounded","BARBARA":"quietly watchful, head tilted, mug held under her chin"}),
  dict(id="SC05-F02-B-MCU", scale="MCU", rig="F2", who=["BARBARA"], off="Margaret across the table, screen-left (Barbara looks screen-left)",
   desc="Barbara leans forward over the table, mug set down, about to speak", emo={"BARBARA":"gently probing: brows raised a fraction, mouth just opening, eyes steady on Margaret"}),
  dict(id="SC05-F03-M-CU", scale="CU", rig="F2", who=["MARGARET"], off="Barbara across the table, screen-right (Margaret looks screen-right)",
   desc="Margaret looks up from her pills at Barbara", emo={"MARGARET":"resigned and a little defensive: jaw tight, eyes tired, a slow breath out through the nose"}),
  dict(id="SC05-F04-REVEAL", scale="INSERT", rig="F4", who=["BARBARA"], product="reveal-B",
   desc="Seated, Barbara's left leg drawn up a little, her hand holding the hem of her wide black trouser leg gathered above the knee; the strap already in place under her left kneecap", emo={}),
  dict(id="SC05-F05-B-MCU-CANDID", scale="MCU", rig="F1", who=["BARBARA"], off="Margaret across the table, screen-left (Barbara looks screen-left)",
   desc="Barbara, her trouser leg still gathered above her left knee below frame, talks with one hand flat on the table", emo={"BARBARA":"candid and certain: chin level, a dry half-smile gone, eyes holding Margaret's"}),
  dict(id="SC05-F06-M-CU-SCEPTIC", scale="CU", rig="F2", who=["MARGARET"], off="Barbara across the table, screen-right (Margaret looks screen-right)",
   desc="Margaret glances down at Barbara's knee and back up", emo={"MARGARET":"sceptical: one brow drawn down, mouth pressed thin, head drawn back a little"}),
  dict(id="SC05-F07-FINGER", scale="INSERT", rig="F2", who=["MARGARET"],
   desc="Margaret's right forefinger pressing into her stone chinos just under her right kneecap, her knee bent under the table edge", emo={}),
  dict(id="SC05-F08-B-CU-TRUTH", scale="CU", rig="F1", who=["BARBARA"], off="Margaret across the table, screen-left (Barbara looks screen-left)",
   desc="Barbara, closer, both forearms on the table", emo={"BARBARA":"hard honesty: jaw firm, eyes wet at the rims but steady, no smile"}),
  dict(id="SC05-F09-M-CU-RAW", scale="CU", rig="F1", who=["MARGARET"], off="Barbara across the table, screen-right (Margaret looks screen-right)",
   desc="Margaret, hands still in her lap", emo={"MARGARET":"raw and close to tears: chin tucked, lower lip held still with effort, eyes glassy and lowered"}),
  dict(id="SC05-F10-PALM", scale="INSERT", rig="F2", who=["MARGARET","BARBARA"], product="palm",
   desc="Barbara's hand pressing a second strap into Margaret's open right palm over the oilcloth, the strap closed and whole, chrome slides catching the window", emo={}),
 ],
 clips=[
  dict(id="SC05-C01", frame="SC05-F01-MASTER", dur=12, shots=[
    ("WIDE","F2",None,None,"Margaret sets the ice pack last in her line of two pills, gel and brace; Barbara watches over her mug"),
    ("MCU","F2","BARBARA","You've done this every morning since I got here. Two pills, the gel, the brace and an ice pack.","gently, counting the items off; turns on 'every morning'; under the line she's worried and hides it behind the list, leaking only through the mug going still in her hands")]),
  dict(id="SC05-C02", frame="SC05-F03-M-CU", dur=10, shots=[
    ("CU","F2","MARGARET","For eleven years.","flat, eyes back on her pills; stress on 'eleven'; under the line shame she won't show, leaking through a small swallow"),
    ("MCU","F1","BARBARA","Can I show you something?","quiet, deciding; the push lands as she asks"),
    ("INSERT","F4",None,None,"Barbara draws the hem of her wide trouser leg clear of her left knee in one unhurried movement; the strap is already there under the kneecap and comes into view unchanged")]),
  dict(id="SC05-C03", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F1","BARBARA","It's called Stryde. I had it on at the wedding. All night.","plainly proud; stress on 'All night'; under the line she wants Margaret to remember the dance floor, leaking through a small lift of the chin"),
    ("CU","F2","MARGARET","That little thing? Barbara, that can't possibly work on knees like mine.","sceptical, almost laughing it off; turns on 'knees like mine'; under the line she's afraid to hope, leaking through a glance away")]),
  dict(id="SC05-C04", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F2","BARBARA","That's exactly what I said. Last winter I was sleeping on my sofa because I couldn't get up my own stairs.","dry, unhurried; stress on 'my own stairs'; under the line the memory still stings, leaking through a breath held before 'sofa'"),
    ("CU","F2","MARGARET",None,"LISTEN: Margaret takes in 'my own stairs' and her eyes drop to the table; mouth closed")]),
  dict(id="SC05-C05", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F2","BARBARA","Every brace you've ever bought was made to keep you comfortable while your knee got worse.","firm, leaning on 'worse'; one hand turns the old brace on the table a quarter turn"),
    ("CU","F2","MARGARET",None,"LISTEN: on 'got worse' Margaret's jaw tightens; she looks at the brace, then back")]),
  dict(id="SC05-C06", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F2","BARBARA","A sleeve just squeezes the knee. A brace just stops it going sideways. Does your knee hurt going sideways?","practical, a teacher's rhythm; turns on the question, eyebrows up"),
    ("CU","F2","MARGARET","No.","small, honest, a little surprised by her own answer")]),
  dict(id="SC05-C07", frame="SC05-F02-B-MCU", dur=13, shots=[
    ("MCU","F2","BARBARA","It hurts coming down the stairs. Put your finger just under your kneecap.","knowing; stress on 'down'"),
    ("INSERT","F2","BARBARA","Two centimetres down. Press in. Feel that band?","off screen, patient; Margaret's right forefinger presses into her trouser just under the kneecap and finds the spot"),
    ("CU","F2","MARGARET","Yes.","quiet recognition; brows lift a fraction")]),
  dict(id="SC05-C08", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F1","BARBARA","That's the tendon. Every step you take lands right there. Seventeen times your bodyweight goes through it. Every stride.","slow and weighted, one word leaned on per sentence; stress on 'right there'"),
    ("CU","F2","MARGARET",None,"LISTEN: Margaret's finger still pressed to her knee below frame; on 'every stride' she breathes out")]),
  dict(id="SC05-C09", frame="SC05-F09-M-CU-RAW", dur=11, shots=[
    ("CU","F2","MARGARET","Barbara, my knees are bone on bone. There's nothing left in there.","despairing but quiet; turns on 'nothing left'; under the line eleven years of being told this, leaking through her voice thinning"),
    ("CU","F1","BARBARA","Mine too. This doesn't put anything back.","immediate, flat and kind")]),
  dict(id="SC05-C10", frame="SC05-F08-B-CU-TRUTH", dur=13, shots=[
    ("CU","F1","BARBARA","Nothing can, and anyone who tells you otherwise is lying to you. I'm seventy-four, Margaret. I haven't got time to lie to you.","hard honesty, slowing on the last sentence; stress on 'time'; under the line she's frightened of her own age, leaking through one blink held long")]),
  dict(id="SC05-C11", frame="SC05-F09-M-CU-RAW", dur=11, shots=[
    ("CU","F2","MARGARET","Then what does it do?","opening up, almost a whisper"),
    ("MCU","F2","BARBARA","It changes where the weight lands. It sits just under the kneecap, right on that band.","plain and exact; her fingertip touches the shell on her own left knee below frame")]),
  dict(id="SC05-C12", frame="SC05-F05-B-MCU-CANDID", dur=13, shots=[
    ("MCU","F2","BARBARA","There's a silicone pad on the inside. The pad presses on that one spot, instead of spreading the pressure around the whole knee like a sleeve does.","explaining with her hands, one flat palm for 'the whole knee', one fingertip for 'that one spot'")]),
  dict(id="SC05-C13", frame="SC05-F05-B-MCU-CANDID", dur=14, shots=[
    ("MCU","F2","BARBARA","It catches the weight and moves it off the worn part, before it gets to the joint.","certain; stress on 'catches'"),
    ("MCU","F1","BARBARA","They measured it. Thirty four percent less strain, every step.","matter-of-fact, no selling; the push eases on 'every step'")]),
  dict(id="SC05-C14", frame="SC05-F08-B-CU-TRUTH", dur=12, shots=[
    ("CU","F2","BARBARA","Bone on bone, arthritis, worn cartilage, meniscus. Whichever one your doctor said it was, that's the spot taking the weight.","a list said like she's heard every one of them; stress on 'that's the spot'"),
    ("CU","F2","MARGARET",None,"LISTEN: on 'meniscus' Margaret almost nods; eyes on Barbara")]),
  dict(id="SC05-C15", frame="SC05-F08-B-CU-TRUTH", dur=12, shots=[
    ("CU","F1","BARBARA","Every brace and every injection you've had was aimed at the whole knee. Not that spot. That's why nothing worked.","slower; the turn word is 'Not that spot'; under the line she's angry on Margaret's behalf, leaking through a tightened jaw"),
    ("CU","F2","MARGARET",None,"LISTEN: the words land; Margaret's eyes fill a little and she looks at her line of pills")]),
  dict(id="SC05-C16", frame="SC05-F02-B-MCU", dur=11, shots=[
    ("MCU","F2","BARBARA","Your arthritis will still be there. The weight just won't be landing where it hurts.","gentle, honest"),
    ("CU","F2","MARGARET","It'll slip. They all slip.","the old objection, tired; stress on 'all'")]),
  dict(id="SC05-C17", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F2","BARBARA","It's adjustable, and it doesn't go over the joint, so there's nothing to bunch up or roll down. Ten seconds to put on.","patient, ticking points off on two fingers"),
    ("CU","F2","MARGARET",None,"LISTEN: Margaret looks at Barbara's knee below frame, then back up")]),
  dict(id="SC05-C18", frame="SC05-F05-B-MCU-CANDID", dur=12, shots=[
    ("MCU","F2","BARBARA","It sits flat under your trousers, and you forget it's there. They spent three years building it with orthopaedic surgeons.","plain facts, no pitch; stress on 'forget'"),
    ("CU","F2","MARGARET",None,"LISTEN: Margaret's hands go still in her lap")]),
  dict(id="SC05-C19", frame="SC05-F09-M-CU-RAW", dur=13, shots=[
    ("MCU","F2","BARBARA","Over two hundred thousand people wear one.","quietly, almost an afterthought"),
    ("CU","F1","MARGARET","I can't try another thing that doesn't work, Barbara. I can't get my hopes up again.","quietly, the voice nearly going on 'again'; under the line she's more afraid of hope than pain, leaking through her fingers tightening")]),
  dict(id="SC05-C20", frame="SC05-F08-B-CU-TRUTH", dur=11, shots=[
    ("CU","F2","BARBARA","Then don't get your hopes up. Just put it on and walk down the stairs.","dry kindness; stress on 'walk'"),
    ("INSERT","F2",None,None,"Barbara presses a second strap into Margaret's open right palm; Margaret's fingers close slowly around it")]),
  dict(id="SC05-C21", frame="SC05-F10-PALM", dur=8, shots=[
    ("INSERT","F2",None,None,"Margaret's hand holding the strap on the table"),
    ("CU","F2","BARBARA","And keep your hand on the rail. I'm not crazy.","deadpan; under the line affection, leaking through the corner of her mouth"),
    ("CU","F1","MARGARET",None,"LISTEN: Margaret almost smiles, and doesn't quite; eyes on the strap")]),
 ])

SC["SC06"] = dict(title="Scene 5 · The stairs", day="D3", loc="L-STAIR", house=True,
 time="late morning, minutes later", light="flat soft daylight from the landing window high on the north side, the frosted front door glowing at the foot",
 blocking="Margaret stands on the landing at the top of the flight, gripping the brass-capped newel post, her right trouser leg drawn up above the knee with the strap in place; Barbara stands in the hall at the foot of the stairs looking up",
 axis="up and down the flight", side="photo-wall (right, looking up)",
 props="Margaret's right trouser leg gathered above the knee; nothing loose",
 cast=["MARGARET","BARBARA"], vis={"MARGARET":"right"},
 frames=[
  dict(id="SC06-F01-MASTER", scale="WIDE", rig="F2", key=True, who=["MARGARET","BARBARA"], product="worn-M-small",
   desc="From the hall looking up the flight: Barbara at the foot in the foreground, back three-quarter to camera; Margaret at the top, small in frame, gripping the newel post",
   emo={"MARGARET":"frozen with fear: shoulders up, both hands white on the post","BARBARA":"steady, feet planted, hands loose at her sides"}),
  dict(id="SC06-F02-M-MCU", scale="MCU", rig="F2", who=["MARGARET"], off="Barbara at the foot of the stairs, below camera",
   desc="Margaret at the top, looking down the flight, low angle from a few treads below her", emo={"MARGARET":"terror held in: jaw clenched, eyes on the treads, breath high in the chest"}),
  dict(id="SC06-F03-B-MCU", scale="MCU", rig="F2", who=["BARBARA"], off="Margaret at the top of the stairs, above camera",
   desc="Barbara at the foot, looking up, high angle from partway up the flight", emo={"BARBARA":"calm and certain, a small nod, eyes up at Margaret"}),
  dict(id="SC06-F04-M-FULL-STEP", scale="FULL", rig="F2", who=["MARGARET"], product="worn-M",
   desc="Margaret on the first tread down, facing forwards, right knee bent taking her weight, strap on the tendon under the kneecap, her right hand resting open on the wall rail without gripping", emo={"MARGARET":"bracing for the knee to give: lips parted, eyes down"}),
  dict(id="SC06-F05-M-CU-WONDER", scale="CU", rig="F1", who=["MARGARET"], off="Barbara below, camera-right",
   desc="Margaret halfway down the flight", emo={"MARGARET":"wonder breaking through: eyes full, brows lifted, mouth open on a breath"}),
  dict(id="SC06-F06-HAND", scale="INSERT", rig="F2", who=["MARGARET"],
   desc="Margaret's right hand resting open on the brass-bracket wall rail, fingers loose, not gripping", emo={}),
  dict(id="SC06-F07-FOOT", scale="MEDIUM", rig="F2", who=["MARGARET","BARBARA"],
   desc="At the foot of the stairs in the hall: Margaret on the bottom tread, one hand over her mouth, Barbara stepping in to hold her", emo={"MARGARET":"weeping with relief, hand over mouth, eyes shut","BARBARA":"eyes wet, reaching for her"}),
 ],
 clips=[
  dict(id="SC06-C01", frame="SC06-F01-MASTER", dur=10, shots=[
    ("WIDE","F2",None,None,"Margaret at the top gripping the post; Barbara waits at the foot"),
    ("MCU","F2","MARGARET","I can't, Barbara. I haven't come down these forwards in two years.","terror kept small; stress on 'forwards'; under the line humiliation, leaking through her knuckles tightening on the post")]),
  dict(id="SC06-C02", frame="SC06-F03-B-MCU", dur=11, shots=[
    ("MCU","F2","BARBARA","Hand on the rail. One step. That's all I'm asking.","steady, slow, no pressure"),
    ("FULL","F2",None,None,"Margaret lets go of the post, puts her right hand on the wall rail, and takes the first step down forwards, slowly, the right knee taking her weight; she waits for it to give")]),
  dict(id="SC06-C03", frame="SC06-F04-M-FULL-STEP", dur=12, shots=[
    ("MCU","F2","BARBARA","Feel that under the kneecap? That's the weight going somewhere else.","coaching, low and even"),
    ("FULL","F2",None,None,"Uncut: the second step, then the third, reciprocal steps, her hand resting open on the rail; her eyes fill")]),
  dict(id="SC06-C04", frame="SC06-F05-M-CU-WONDER", dur=11, shots=[
    ("CU","F1","MARGARET","Barbara... I'm not gripping it.","tears running, wonder more than words; stress on 'not'"),
    ("INSERT","F2",None,None,"Her right hand resting open on the rail, fingers loose, sliding along it without holding"),
    ("CU","F1","BARBARA","I know, love. Keep coming.","her own eyes wet, voice held level")]),
  dict(id="SC06-C05", frame="SC06-F04-M-FULL-STEP", dur=12, shots=[
    ("FULL","F5",None,None,"She comes the rest of the way down, both feet, forwards, an even reciprocal gait, the camera gliding back ahead of her"),
    ("MEDIUM","F2","MARGARET","I can't believe it. I can't believe it.","at the bottom, hand over her mouth, weeping; the second time almost a laugh")]),
  dict(id="SC06-C06", frame="SC06-F07-FOOT", dur=10, shots=[
    ("MEDIUM","F2",None,None,"Barbara holds her"),
    ("MEDIUM","F2","BARBARA","Well, don't just stand there. Put the kettle on.","brisk and dry into Margaret's shoulder; under the line she's crying too, leaking through a sniff"),
    ("MEDIUM","F2",None,None,"Margaret laughs through her tears")]),
 ])

SC["SC07"] = dict(title="Scene 6 · Doctor's office, a month later", day="D4", loc="L-GP", house=False,
 time="midday", light="daylight through the vertical blinds on the right, flat overhead panels",
 blocking="The doctor sits at the L-shaped desk on the left, turned to the monitor showing a knee X-ray; Margaret sits in the near plastic chair facing him",
 axis="across the corner of the desk", side="window (right)",
 props="the X-ray on the monitor, the anatomical knee model on the desk",
 cast=["MARGARET","DOCTOR"], vis={"MARGARET":"right"},
 frames=[
  dict(id="SC07-F01-MASTER", scale="WIDE", rig="F2", key=True, who=["MARGARET","DOCTOR"],
   desc="Margaret has just walked in and is sitting down unaided in the near chair; the doctor at the desk glances from the monitor to her",
   emo={"MARGARET":"quietly composed, a private pride held down","DOCTOR":"clinical attention, reading glasses on"}),
  dict(id="SC07-F02-D-MCU", scale="MCU", rig="F2", who=["DOCTOR"], off="Margaret in the chair, camera-right",
   desc="The doctor turned half to the monitor, one hand on the mouse", emo={"DOCTOR":"clinical, then puzzled: brow creased, eyes moving from screen to patient"}),
  dict(id="SC07-F03-M-CU", scale="CU", rig="F2", who=["MARGARET"], off="the doctor at the desk, camera-left",
   desc="Margaret seated, hands folded on her bag", emo={"MARGARET":"calm with a secret: a closed small smile, eyes level"}),
  dict(id="SC07-F04-REVEAL", scale="INSERT", rig="F4", who=["MARGARET"], product="reveal-M",
   desc="Seated, Margaret's hand holding the hem of her charcoal wide-leg trouser gathered above her right knee; the strap already in place under the kneecap, knee bent", emo={}),
 ],
 clips=[
  dict(id="SC07-C01", frame="SC07-F01-MASTER", dur=12, shots=[
    ("WIDE","F2",None,None,"Margaret sits down unaided; the doctor looks up"),
    ("MCU","F2","DOCTOR","Your new X-ray looks exactly like the old one, Margaret. Bone on bone, both knees.","level and exact, eyes on the screen; stress on 'exactly'")]),
  dict(id="SC07-C02", frame="SC07-F03-M-CU", dur=11, shots=[
    ("CU","F2","MARGARET","I know.","calm, a hint of a smile"),
    ("MCU","F1","DOCTOR","So how did you just walk in here like that?","genuinely curious; turns on 'walk'"),
    ("INSERT","F4",None,None,"Margaret draws the hem of her trouser clear of her right knee in one unhurried movement; the strap is already there and comes into view unchanged")]),
  dict(id="SC07-C03", frame="SC07-F02-D-MCU", dur=12, shots=[
    ("MCU","F1","DOCTOR","That makes sense. It's moving the weight off the worn part. Keep wearing it.","leaning in, nodding once; plain professional approval"),
    ("CU","F2","MARGARET","I wasn't planning on taking it off.","wry, pleased; stress on 'planning'")]),
 ])

SC["SC08"] = dict(title="Scene 7 · Front door", day="D5", loc="L-HALL", house=True,
 time="late afternoon", light="soft skylight through the frosted east-facing front door, the kitchen at the far end glowing warm from its west window",
 blocking="Margaret has just come in through the front door with two bags of shopping; Frank stands in the hall by the coat hooks with his wax jacket half on",
 axis="down the hall, front door to kitchen", side="coat-hook (right)",
 props="two full shopping bags in Margaret's hands; Frank's jacket half on",
 cast=["MARGARET","FRANK"], vis={},
 frames=[
  dict(id="SC08-F01-MASTER", scale="FULL", rig="F5", key=True, who=["MARGARET","FRANK"],
   desc="The front door swinging shut behind Margaret as she steps in with two shopping bags; Frank by the coat hooks, one arm in his jacket",
   emo={"MARGARET":"brisk and easy, a little flushed from walking","FRANK":"worried, caught mid-hurry"}),
  dict(id="SC08-F02-F-MCU", scale="MCU", rig="F2", who=["FRANK"], off="Margaret by the door, camera-left",
   desc="Frank with his jacket half on", emo={"FRANK":"worry turning to puzzlement: brows up, mouth slightly open"}),
  dict(id="SC08-F03-M-CU", scale="CU", rig="F2", who=["MARGARET"], off="Frank by the coat hooks, camera-right",
   desc="Margaret with the bags still in her hands", emo={"MARGARET":"calm, quietly pleased with herself"}),
  dict(id="SC08-F04-TWO", scale="TWO-SHOT", rig="F2", who=["MARGARET","FRANK"],
   desc="Margaret, bags now on the hall carpet, takes Frank's hand", emo={"MARGARET":"tender resolve","FRANK":"eyes wet, voice gone"}),
 ],
 clips=[
  dict(id="SC08-C01", frame="SC08-F01-MASTER", dur=12, shots=[
    ("FULL","F5",None,None,"Margaret steps in with the shopping; Frank turns from the hooks"),
    ("MCU","F2","FRANK","I was just coming to look for you. You were gone a long time.","relieved and cross at once, quick"),
    ("CU","F2","MARGARET","I know.","easy, unbothered")]),
  dict(id="SC08-C02", frame="SC08-F02-F-MCU", dur=12, shots=[
    ("MCU","F2","FRANK","Where did you go?","puzzled"),
    ("CU","F2","MARGARET","Into town.","matter-of-fact"),
    ("MCU","F1","FRANK","You walked into town? That's two miles.","astonished; stress on 'walked'"),
    ("CU","F2","MARGARET","Each way.","putting the bags down; quiet triumph she doesn't show")]),
  dict(id="SC08-C03", frame="SC08-F02-F-MCU", dur=9, shots=[
    ("CU","F1",None,None,"Frank looks at her for a long moment"),
    ("MCU","F2","FRANK","I called the stairlift man.","a confession, looking down"),
    ("CU","F2","MARGARET","Frank...","bracing, soft")]),
  dict(id="SC08-C04", frame="SC08-F02-F-MCU", dur=13, shots=[
    ("CU","F1","FRANK","I told him not to come. All those nights I lay there thinking, if it's me that goes first...","slowed right down; his voice goes on 'first'; under the line terror he's carried for years, leaking through his chin trembling"),
    ("TWO-SHOT","F2","MARGARET","Then I'll manage the stairs.","taking his hand; tender, certain")]),
 ])

SC["SC09"] = dict(title="Scene 8 · Sunday, the stairs", day="D6", loc="L-STAIR", house=True,
 time="midday on Sunday", light="brighter daylight from the landing window, the frosted front door glowing at the foot",
 blocking="Margaret climbs the flight forwards at a normal pace; Sarah follows two treads behind with her arms out",
 axis="up the flight", side="photo-wall (right, looking up)",
 props="nothing loose",
 cast=["MARGARET","SARAH"], vis={"MARGARET":"right"},
 frames=[
  dict(id="SC09-F01-MASTER", scale="FULL", rig="F5", key=True, who=["MARGARET","SARAH"],
   desc="From the hall looking up: Margaret halfway up the flight climbing forwards, hands free at her sides; Sarah two treads behind with her arms out",
   emo={"MARGARET":"easy and upright","SARAH":"anxious habit, arms hovering"}),
  dict(id="SC09-F02-S-MCU", scale="MCU", rig="F2", who=["SARAH"], off="Margaret above her on the stairs, camera-left",
   desc="Sarah on the stairs, arms out, looking up", emo={"SARAH":"protective habit: brows knitted, lips pressed"}),
  dict(id="SC09-F03-M-MCU-TOP", scale="MCU", rig="F2", who=["MARGARET"], off="Sarah below on the stairs, camera-right",
   desc="Margaret on the landing at the top, turned back to look down the flight, hands free", emo={"MARGARET":"gentle mischief: eyes crinkled, a held smile"}),
  dict(id="SC09-F04-S-CU", scale="CU", rig="F1", who=["SARAH"], off="Margaret at the top, camera-left",
   desc="Sarah halfway up, arms slowly lowering", emo={"SARAH":"stunned, tears rising: mouth open, eyes wet"}),
  dict(id="SC09-F05-REVEAL", scale="INSERT", rig="F4", who=["MARGARET"], product="reveal-M",
   desc="Margaret seated on the top step, her hand holding the hem of her navy wide-leg trouser gathered above her right knee; the strap already in place under the kneecap, knee bent", emo={}),
  dict(id="SC09-F06-M-MCU-SEATED", scale="MCU", rig="F2", who=["MARGARET"], off="Sarah a few treads below, camera-right", product="worn-M-small",
   desc="Margaret sitting on the top step, trouser leg drawn up above the right knee, talking down to Sarah", emo={"MARGARET":"assured and warm"}),
 ],
 clips=[
  dict(id="SC09-C01", frame="SC09-F01-MASTER", dur=10, shots=[
    ("FULL","F5",None,None,"Margaret climbs forwards at a normal pace, hands free; Sarah follows with her arms out"),
    ("MCU","F2","SARAH","Slowly, Mum. I'm right behind you.","habit, a little breathless")]),
  dict(id="SC09-C02", frame="SC09-F03-M-MCU-TOP", dur=11, shots=[
    ("MCU","F2","MARGARET","You can put your arms down now, love.","gentle, amused"),
    ("MEDIUM","F1",None,None,"Sarah halfway up with her arms still out; she lowers them slowly"),
    ("CU","F1","SARAH","Mum... when did that happen?","tearing up; stress on 'when'")]),
  dict(id="SC09-C03", frame="SC09-F03-M-MCU-TOP", dur=11, shots=[
    ("MCU","F2","MARGARET","Six weeks ago. Barbara happened.","warm, a little proud; she sits down on the top step"),
    ("MCU","F2","SARAH","What does that even mean?","laughing through confusion"),
    ("INSERT","F4",None,None,"Seated on the top step, Margaret draws the hem of her trouser clear of her right knee; the strap comes into view unchanged")]),
  dict(id="SC09-C04", frame="SC09-F06-M-MCU-SEATED", dur=12, shots=[
    ("MCU","F2","MARGARET","It sits on the tendon under my kneecap and moves the weight off the worn part. My knees are still seventy-one.","plain, assured; stress on 'still'")]),
  dict(id="SC09-C05", frame="SC09-F06-M-MCU-SEATED", dur=11, shots=[
    ("MCU","F2","MARGARET","It's not because the arthritis has gone. It's because the weight isn't landing where it hurts.","simple and certain"),
    ("CU","F2","SARAH",None,"LISTEN: Sarah sits on the stair below, taking it in, wiping her eyes")]),
 ])

SC["SC10"] = dict(title="Scene 8 (later) · Kitchen dance", day="D6", loc="L-KIT", house=True,
 time="late afternoon on Sunday", light="low warm sun from the west window raking along the galley floor",
 blocking="Margaret stands at the sink end; Emily comes in from the hall door; Sarah stays in the doorway",
 axis="along the galley", side="cabinet (left)",
 props="the cream radio on the windowsill switched on",
 cast=["MARGARET","EMILY","SARAH"], vis={},
 frames=[
  dict(id="SC10-F01-MASTER", scale="WIDE", rig="F2", key=True, who=["MARGARET","EMILY","SARAH"],
   desc="The galley in low sun: Margaret by the sink in slippers, Emily a step inside holding out both hands, Sarah leaning in the hall doorway",
   emo={"MARGARET":"surprised delight","EMILY":"playful, hopeful","SARAH":"watching, soft"}),
  dict(id="SC10-F02-E-MCU", scale="MCU", rig="F2", who=["EMILY"], off="Margaret by the sink, camera-left",
   desc="Emily holding out both hands", emo={"EMILY":"playful, a dare in her smile"}),
  dict(id="SC10-F03-DANCE", scale="FULL", rig="F4", who=["MARGARET","EMILY"],
   desc="Margaret and Emily holding hands mid-step in a slow dance down the galley, Margaret in her slippers", emo={"MARGARET":"joy, eyes wet and bright","EMILY":"laughing"}),
 ],
 clips=[
  dict(id="SC10-C01", frame="SC10-F01-MASTER", dur=10, shots=[
    ("WIDE","F2",None,None,"The radio is on; Emily holds out her hands"),
    ("MCU","F2","EMILY","Grandma. You still owe me a dance.","playful, drawing out 'Grandma'"),
    ("CU","F1","MARGARET","I always keep my promises.","joy held just under the surface; stress on 'always'")]),
  dict(id="SC10-C02", frame="SC10-F03-DANCE", dur=12, shots=[
    ("FULL","F4",None,None,"Uncut: Margaret takes her hands and they dance slowly down the galley and back, Margaret in her slippers, easy reciprocal steps"),
    ("MCU","F1",None,None,"Sarah in the doorway, laughing and crying at the same time")]),
 ])

SC["SC11"] = dict(title="Scene 9 · Phone call", day="D7", loc="L-LIV", house=True,
 time="mid-afternoon", light="soft even light from the east bay window, no direct sun",
 blocking="Margaret sits in the dusky-pink wingback in the bay with the cordless phone to her ear; two straps rest in her lap",
 axis="from the armchair to the fireplace", side="fireplace (right)",
 props="the cordless phone at her ear; two straps in her lap",
 cast=["MARGARET"], vis={},
 frames=[
  dict(id="SC11-F01-MASTER", scale="MCU", rig="F2", key=True, who=["MARGARET"], off="nobody in the room; she talks on the phone, eyes resting on the fireplace, camera-right", product="lap",
   desc="Margaret in the wingback, cordless phone to her left ear, two straps resting in her lap", emo={"MARGARET":"purposeful, warm, the look of someone about to tell good news"}),
 ],
 clips=[
  dict(id="SC11-C01", frame="SC11-F01-MASTER", dur=9, shots=[
    ("MCU","F2","MARGARET","Joan, it's me. I've found something for your knees.","purposeful, warm"),
    ("MCU","F2",None,None,"PHONE LISTEN: Margaret listens to Joan's reply with a knowing half-smile (Joan's line is laid in from her voice master in the edit)")]),
  dict(id="SC11-C02", frame="SC11-F01-MASTER", dur=11, shots=[
    ("MCU","F1","MARGARET","That's exactly what I said. It's called Stryde. Barbara gave me one. Get it from their website, the real one.","amused recognition, then firm on 'the real one'")]),
  dict(id="SC11-C03", frame="SC11-F01-MASTER", dur=9, shots=[
    ("MCU","F2","MARGARET","There are copies out there. It's two for one right now, so you can do both knees.","practical; she lifts the two straps from her lap on 'both knees'")]),
  dict(id="SC11-C04", frame="SC11-F01-MASTER", dur=12, shots=[
    ("MCU","F2","MARGARET","And if it doesn't work, you get your money back. Sixty days, and you keep the straps.","reassuring; stress on 'keep'"),
    ("MCU","F2",None,None,"PHONE LISTEN: she listens, smiling (Joan's second line laid in from her voice master)")]),
  dict(id="SC11-C05", frame="SC11-F01-MASTER", dur=8, shots=[
    ("CU","F1","MARGARET","Nothing. Come over on Sunday. You're walking up my stairs on your own.","warm certainty; stress on 'your own'; ends at rest")]),
 ])
