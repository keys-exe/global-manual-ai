ANGLE = [
 ("The argument","Every fix Margaret has tried treats the whole knee or gives up on it: sleeves squeeze it, braces stop sideways movement it doesn't have, injections and painkillers dull it, and a stairlift replaces her. Stryde works on the one spot the weight lands. It doesn't promise to cure the arthritis. It gives her the stairs back"),
 ("What others don't argue","Most knee ads sell relief or repair. This one tells the viewer their knees will stay 'bone on bone' and still wins, because the proof is independence (stairs forwards, two miles each way, a dance) and not a scan or a number"),
 ("Who makes it credible","A messenger older than the protagonist (74), with the same diagnosis and no reason to lie. A doctor confirms what he sees and doesn't sell. The friend referral at the end closes the loop the viewer is in"),
 ("The fear it answers","Losing independence, and what that does to a marriage and a family: 'A stairlift is how it starts.' 'Who gets you down the stairs?'"),
]

# §14A story-day map: day → scenes, acts, time, gap from the day before
DAYS = [
 ("HKA","Hook A","HK","A morning in the Before (alternate hook)","—","Stairs + hall"),
 ("HKB","Hook B","HK","A weekday morning after D6 (flash-forward)","—","Station"),
 ("HKC","Hook C","HK","A late afternoon in the Before (alternate hook)","—","Kitchen"),
 ("D1","SC02 · SC03","BF","Afternoon, then that night","Story start","Kitchen, bedroom"),
 ("D2","SC04","PB","Late afternoon","Days later (unstated)","Wedding venue"),
 ("D3","SC05 · SC06","PB → TN","Morning to late morning","A week after the wedding","Kitchen, stairs"),
 ("D4","SC07","AF","Midday","A month after D3","GP room"),
 ("D5","SC08","AF","Late afternoon","Between D4 and D6","Hall"),
 ("D6","SC09 · SC10","AF","Sunday midday to afternoon","Six weeks after D3 ('Six weeks ago. Barbara happened')","Stairs, kitchen"),
 ("D7","SC11","OC","Afternoon","After D6, before a coming Sunday","Living room"),
]
DAY_NOTES = [
 "Seven story days plus three hook days. The hooks are alternates; only one runs per test.",
 "Exception 1: D3 spans two acts. SC05 turns from Problem to Turn mid-scene, and SC06 follows without a cut in time.",
 "Exception 2: the After act spans three days (D4, D5, D6).",
 "SC03 is a nightwear event inside D1, not a new day.",
 "The six weeks from D3 to D6 is the title's time jump. Hook B happens after D6, so its '6 weeks ago' card is literally true.",
]

# §22C Part B, one line per location, locked per act (AUD-PATTERN). Mode 4 puts AUD-FILM ahead of it.
AUDIO = [
 ("L-KIT","Kitchen","Small galley with hard tiled walls, a vinyl floor and laminate worktops; short bright reflections with a quick tail. The voice is close to the boom with a little kitchen in the signal; no bass boost. Room tone: fridge hum; the radio only in SC10."),
 ("L-HALL","Hall and front door","Narrow carpeted hall with a hard uPVC door at one end; soft, damped reflections and almost no tail. The voice is close with a slight hallway narrowness in the signal. Room tone: faint street through the door glass."),
 ("L-STAIR","Stairs and landing","A tall stairwell, carpeted treads under hard painted walls; a soft vertical bloom with a short tail. The voice is close, with a touch more air when the speaker is at the top. Foley: soft footfalls on carpet, the brass rods ticking under a heel."),
 ("L-BED","Main bedroom","Small bedroom with soft furnishings, carpet, curtains and bedding; very dead, no tail. The voices are intimate and low, the boom close, almost no room. Room tone: near-silence, a car passing far off."),
 ("L-LIV","Living room","Medium living room with carpet, upholstered furniture and a bay; warm, damped, a short soft tail. The voice is close with a little warmth of the room. Room tone: a clock, the faint gas fire."),
 ("L-WED","Wedding reception room","A large function room, carpet around a parquet floor, big windows; long diffuse reflections under the music. Dialogue is close on the boom, the room and the crowd walla well behind it. Music plays in the room at low level under the dialogue (in-story, not score)."),
 ("L-GP","Doctor's consulting room","A small clinical room with hard walls, a vinyl floor and a suspended ceiling; bright, short reflections. The voice is close and slightly boxy. Room tone: the air-handling hum, a keyboard."),
 ("L-STN","Station staircase","A large hard concourse with concrete and tile; long bright reverberation and a crowd bed. The voice is close on the boom for the key lines, and the far lines ('Seventy-one!') sit well back in the space. Walla, footsteps, a distant announcement chime with no words."),
]

# §15A surface library for object beats: SURFACE (with wear, rotated) · CONTEXT (one or two, cropped) · DEPTH (a real room, one moving element)
SURFACES = [
 ("BF-SC02-SH01","Stairlift brochure slid across the table","Floral oilcloth on the drop-leaf table, creased in a grid from being folded, its print worn pale where forearms rest; directional shadow from the window at the far end","Sarah's mug cropped at the frame edge; the corner of the fruit bowl","The galley falling off towards the window, the radio's shape on the sill"),
 ("BF-SC02-SH07","The tea tray waiting on the counter","Speckled beige laminate worktop, a lifted edge at the front lip and a pale heat mark where the kettle stands","The kettle's base cropped at the left; a folded tea towel","The window light moving slightly on the tiles"),
 ("PB-SC05-SH01","Pills, gel, brace and ice pack lined up","Floral oilcloth again, this time with a small melted scorch near the edge and a knife-scored corner (menu rotated from SH01 of SC02)","Barbara's mug cropped at the right; the cork board edge behind","Morning light widening across the table as a cloud passes"),
 ("TN-SC05-SH10","Barbara turns the old hinged brace","Same oilcloth, with the fold creases and the sun-faded side nearest the window (rotated)","The pill blister at the frame edge","Margaret's shoulder soft in the foreground, the window beyond"),
 ("AF-SC10-SH01","The radio on the windowsill","Painted wooden windowsill, the gloss chipped at one corner and yellowed near the glass","A small spider plant, cropped","The garden through the glass, the washing line turning in the breeze"),
 ("HKC-SC01-SH01","A mug slides off the counter","Speckled laminate worktop with knife scoring near the edge and a chipped front lip","The kettle and a spoon","The kitchen falling off towards the door"),
 ("OC-SC12-SH01","End card: two units and the packaging","Declared exception: a clean sweep (§15A carve-out for guarantee and offer beats), lit and graded with the film's LUT","None","A soft falloff on the sweep; the camera still moves per R4"),
]
SURF_NOTE = ("Ring marks, cup rings and water rings never appear (standing exclusion). In image prompts they are crowded out by naming two or three real wear features; "
             "in video negatives: no ring marks, no cup rings, no water rings, no circular stains on the surface. Consecutive object beats never share the same two wear features.")
