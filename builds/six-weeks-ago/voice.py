NEGV = ("never a smooth announcer voice, never RP newsreader neutral, never audiobook-warm, never a generic voiceover artist, "
 "never the same voice as any other character in the build, never younger than the character, never a mid-pitch evenly paced "
 "narrator with no wear and no habits, no American vowel colouring, no studio polish, no generic intensity on emphatic lines, "
 "no voice that could read any script for any brand")

# measured off the supplied masters: pyin F0, semitone range p10-p90, syllables/s over speech time,
# pause total, phrase-final contour (st), spectral centroid, >4 kHz energy share (breath/rasp proxy)
MEAS = {
 "MARGARET":dict(f0=163,rng=6.9,syl=6.42,wpm=172,pause=2.3,dur=10.1,final="−1.2 to −5.6 st (gentle falls)",cent=1385,breath=0.083),
 "BARBARA": dict(f0=179,rng=9.5,syl=5.43,wpm=159,pause=1.6,dur=11.7,final="−1.7 to −8.8 st (hard falls)",cent=1514,breath=0.095),
 "FRANK":   dict(f0=140,rng=7.3,syl=6.58,wpm=235,pause=1.1,dur=7.7,final="−3.4 to +0.3 st",cent=1289,breath=0.062),
 "SARAH":   dict(f0=220,rng=8.1,syl=6.76,wpm=180,pause=1.5,dur=9.7,final="−7.1 to +0.9 st (one lift)",cent=1524,breath=0.098),
 "EMILY":   dict(f0=209,rng=6.7,syl=7.01,wpm=176,pause=1.6,dur=7.1,final="−2.0 to −6.0 st",cent=1398,breath=0.075),
 "DOCTOR":  dict(f0=107,rng=6.2,syl=6.78,wpm=219,pause=1.5,dur=11.0,final="−3.3 to −5.5 st (even)",cent=1178,breath=0.060),
}

VOICE = {
 "MARGARET": ("A woman of seventy-one, Nottinghamshire, low in the chest for her age, stop-start: short runs cut off by full stops she means. "
  "Short flat vowels and dropped h's, nothing southern, no RP. A little breath on the tone and a dry catch on long vowels. "
  "Measured pace, listing things off one at a time. Sentences land gently falling, never lifting. Soft consonants, glottal final t's. "
  "Held vowels waver and breath runs short on long lines. Emphasis goes quieter and slower, never louder. "
  "A short breath out through the nose before an admission; a dry laugh that stops early."),
 "BARBARA": ("A woman of seventy-four, Black Country, a wide swooping melody that crashes down hard at the end of every line, unhurried and weighted. "
  "Broad Black Country vowels, placed but never comic. Gravel in the throat, plenty of breath on the tone. "
  "Slow and steady, never rushed, leaning on one word per line. Lines swoop up through the middle and land low and final. "
  "Crisp t's and d's when she makes a point. The top of the voice thins and cracks when raised. "
  "Emphasis is slower and lower. A dry snort of a laugh; a brisk tut; a long exhale before she tells the truth."),
 "FRANK": ("A man of seventy-six, Nottinghamshire and broader than his wife, a light high-lying voice for his age that runs on in long unbroken strings. "
  "Rounded Midlands vowels, dropped g's, no RP. Clean and dry, little breath, a slight tremor on held notes. "
  "Quick, words tumbling together, few stops. Statements fall; questions stay flat rather than lifting. "
  "Soft consonants. Breath gives out at the end of long runs and the voice thins. "
  "Emphasis: he stops dead, then says the word quietly. Clears his throat before hard things; a shaky in-breath when his voice goes."),
 "SARAH": ("A woman of about fifty, Nottingham softened by years in an office, a bright breathy head voice that cracks upward under strain, quick and pressing. "
  "Midlands vowels trimmed, never broad, never RP. Breath audible in the tone, clear edges. "
  "Fast even runs with no hesitation. Sentences fall; pleading lines lift at the end. Crisp consonants. "
  "No age wear; strain shows as a tightening crack. Emphasis rises and cracks, then drops to almost a whisper. "
  "A sharp in-breath before she argues; a wet laugh through tears."),
 "EMILY": ("A woman of about thirty, Nottingham, light and high in the head with a quick bouncing rhythm and a smile audible in the vowels. "
  "Young Midlands, relaxed glottal t's, no RP. Higher and thinner than her mother's voice, clear, little breath. "
  "The fastest speaker in the family, syllables skipping. Lines end with a playful fall. Relaxed, slightly clipped consonants. "
  "No wear. Emphasis is a lift and a stretched vowel, never force. A quick giggle; 'Grandma' drawn out when she pleads."),
 "DOCTOR": ("A man in his late forties, educated Edinburgh, low and level with almost no melody, brisk and exact. "
  "Clipped Scottish vowels, rolled or tapped r's, no RP, nothing English. Low in the chest, clean and dry, no rasp. "
  "Quick even tempo, sentences in one breath. Every line lands on the same measured fall. Consonants fully sounded. "
  "No age wear. Emphasis by slowing down and spacing the words, never by raising pitch. "
  "A short exhale through the nose while he reads; a single low 'hm' of recognition."),
 "JOAN": ("A woman of seventy-three, Lincolnshire, a thin reedy head voice with a slow, weary drawl that sags at the end of every line. "
  "Flat Lincolnshire vowels, no RP. Nasal colouring, dry. Slow, long vowels, a pause before she gives in. Lines trail off downwards. "
  "Soft, lazy consonants. Wavering held vowels, breath short. Emphasis is a sigh on the key word. A long weary sigh; a small reluctant laugh."),
}

AXES = ["Face architecture","Hair","Age position","Build","Class / wardrobe register","Marker","Voice","Environment"]
A19 = {
 "MARGARET":["Broad round face, soft jowl, small straight nose, hazel eyes","Silver-white chin-length bob, side part","71, the band's middle","Heavy-set, pear-shaped, rounded shoulders","Tidy retired homemaker: shirt-dresses, knitwear, slippers","Small healed red scar across the bridge of the nose","163 Hz, stop-start, gentle falls","Her own 1970s semi: kitchen, stairs"],
 "BARBARA": ["Broad square weathered face, deep crow's feet, pale blue eyes, strong nose","Short spiky white crop","74, the band's far edge","Stocky, heavy, barrel-bodied","Faded-flamboyant: purple, glass beads, sandals","Raised brown mole on the left side of the neck","179 Hz, slow, wide swoops, hard falls","Guest in Margaret's house; the dance floor"],
 "FRANK":   ["Heavy jowled face, ruddy bulbous nose, grey-blue eyes","Swept-back white hair, long at the collar, bristling white brows","76, far edge","Tall-ish, soft belly, stooping slightly","Retired-respectable: cable cardigan, check shirt, pressed trousers","Bristling white eyebrows that stand up in tufts","140 Hz, fast run-on strings","The hall, the bed, the kitchen floor"],
 "SARAH":   ["Long narrow face, fine lines, brown eyes","Dark brown jaw-length bob with grey threads at the part","About 50, below the buyer band","Lean, narrow-shouldered","Busy working daughter: plain knit, black jeans, white trainers","Small raised blemish at the top of the forehead","220 Hz, breathy, fast, cracks upward","Arrives with shopping; the kitchen table"],
 "EMILY":   ["Oval face, freckled cheeks, hazel-green eyes","Long straight mid-brown hair, centre part","About 30, well below the band","Slim","Young creative: vintage patterned knits, wide cords, chunky boots (changed, see below)","Small crescent scar under the right eye","209 Hz, fast, bouncing, light","Wedding; grandma's kitchen"],
 "DOCTOR":  ["Lean long face, strong nose, deep crease between the brows","Dark curly hair greying at the temples, stubble","Late 40s","Lean, upright","Clinician without a white coat: pale shirt, knit tie, rolled sleeves","Deep vertical crease between the brows","107 Hz, level, brisk, even falls","NHS-style consulting room"],
}
CLEAR = [
 ("MARGARET","BARBARA","5 / 8","Face, hair, class, marker, voice differ. Age band, build and environment are shared (cousins in one house)","PASS"),
 ("MARGARET","SARAH","7 / 8","Only environment shared","PASS"),
 ("MARGARET","EMILY","7 / 8","Only environment shared","PASS"),
 ("MARGARET","FRANK","7 / 8","Environment shared","PASS"),
 ("SARAH","EMILY","4 → 6 / 8","As supplied, build, wardrobe register, voice and environment all match. Emily's wardrobe register is changed (vintage patterned knits, cords, boots) and her voice steered higher and lighter: now 6","FIXED"),
 ("FRANK","DOCTOR","8 / 8","—","PASS"),
 ("BARBARA","SARAH","7 / 8","—","PASS"),
]
SEP = [
 ("SARAH","EMILY","220 vs 209 Hz (5 %)","6.76 vs 7.01 syl/s (4 %)","1524 vs 1398 Hz (8 %)","FLAG","All three within 10 %: one voice in two costumes (§22D rule 4). They never speak in the same scene, but they share the film. Recommend a new Emily master pitched higher and lighter (about 235–250 Hz); until then her VOICE string steers her there"),
 ("MARGARET","BARBARA","163 vs 179 Hz (10 %)","6.42 vs 5.43 syl/s (15 %)","1385 vs 1514 Hz (9 %)","WATCH","Two of three inside 10 %, and they share a 2½-minute two-hander. Tempo separates them: keep Barbara slow with hard landings, Margaret stop-start with gentle falls"),
 ("MARGARET","SARAH","163 vs 220 Hz","6.42 vs 6.76","1385 vs 1524","PASS","—"),
 ("MARGARET","FRANK","163 vs 140 Hz","6.42 vs 6.58","1385 vs 1289","PASS","Pitch separates them"),
 ("MARGARET","EMILY","163 vs 209 Hz","6.42 vs 7.01","1385 vs 1398","PASS","—"),
 ("MARGARET","DOCTOR","163 vs 107 Hz","—","—","PASS","—"),
]

# §20 constraint sheets, Mode 4 settings (eyeline off-lens, F-rigs, AUD-FILM)
C20 = {
 "MARGARET": [("Accent","Nottinghamshire, placed (confirm against the master). Excludes RP, southern and American vowels"),
  ("Pacing","Stop-start, ~170 wpm, full stops honoured; fewer words per breath before the Turn"),
  ("Posture","Before the Turn: weight off the right leg, hand to the right knee or a surface before any bend, step-to gait. After: upright, reciprocal gait, hands free"),
  ("Rest position","Hands folded on the table edge or in her lap, inside frame at MCU"),
  ("Gesture register","Restrained; Economical on held-product beats"),
  ("Ocular default","Off-lens to the scene partner; breaks down and away on shame beats"),
  ("Camera rig","BF/PB: F2 locked, F3 in the fall and argument. TN: F1 push on turns. AF: F2/F5"),
  ("Audio","AUD-FILM, clean production dialogue"),
  ("Wardrobe never-list","No hem at the knee; no shorts; nothing exposing the right knee before the Turn"),
  ("Physical never-list","Before the Turn: no reciprocal gait on stairs, no easy kneel or squat. After: no hand pressed to the knee, no hovering at a rail. Never looks into the lens"),
  ("Eyeline","Off-lens in every act"),
  ("Voice spec","VOICE-MARGARET"),
  ("Stress register","Quieter and slower, never louder; the turn word nearly whispered"),
  ("Non-speech","Nasal exhale before an admission; a dry laugh that stops early; weeping held in the chest before it breaks (SC06)"),
  ("Mouth asymmetry","Assigned: speech pulls to the left corner. Confirm on her first seed")],
 "BARBARA": [("Accent","Black Country, placed (confirm against the master). Excludes Birmingham caricature and RP"),
  ("Pacing","Slow and weighted, ~160 wpm; the slowest speaker in the film"),
  ("Posture","Solid, planted, forward over the table when she argues; moves easily, reciprocal gait everywhere (she's already the after-state)"),
  ("Rest position","Forearms on the table, mug in both hands, inside frame at MCU"),
  ("Gesture register","Economical: one decisive hand, then still. Economical on held-product beats"),
  ("Ocular default","Holds Margaret's eyes; breaks down only on 'I haven't got time to lie to you'"),
  ("Camera rig","F2 locked, F1 on her truth line and the mechanism hand-off"),
  ("Audio","AUD-FILM"),
  ("Wardrobe never-list","No hem at the knee; trousers loose enough to pull above the knee on D3"),
  ("Physical never-list","Never hesitant on stairs, never touches her own knee in pain, never sells to the lens"),
  ("Eyeline","Off-lens, to Margaret"),
  ("Voice spec","VOICE-BARBARA"),
  ("Stress register","Slower and lower, leaning on one word"),
  ("Non-speech","Dry snort of a laugh; brisk tut; long exhale before the truth"),
  ("Mouth asymmetry","Assigned: right corner. Confirm on first seed")],
 "FRANK": [("Accent","Nottinghamshire, broader than Margaret's (confirm)"),("Pacing","Fast run-on strings (measured 235 wpm); slowed to ~180 in SC03 and on 'I told him not to come'"),
  ("Posture","Stiff getting down and up (his back), steady when standing"),("Rest position","Hands on the duvet (SC03), at his coat zip (SC08), inside frame"),
  ("Gesture register","Restrained"),("Ocular default","Off-lens; looks away when his voice goes"),("Camera rig","F2, F1 on SC08's confession"),("Audio","AUD-FILM"),
  ("Wardrobe never-list","No sportswear, no jeans"),("Physical never-list","Never lifts Margaret successfully (Hook C); never cries openly, only the voice goes"),
  ("Eyeline","Off-lens"),("Voice spec","VOICE-FRANK"),("Stress register","Stops dead, then says it quietly"),("Non-speech","Throat-clear; shaky in-breath"),("Mouth asymmetry","Assigned: left corner. Confirm")],
 "SARAH": [("Accent","Nottingham, trimmed (confirm). Says 'Mom' as scripted (D11)"),("Pacing","Fast, pressing, ~180 wpm"),
  ("Posture","Leans in, hands busy; arms out behind Margaret on the stairs"),("Rest position","Hands flat on the table either side of the brochure"),
  ("Gesture register","Continuous in SC02, Restrained in SC09"),("Ocular default","Locked on Margaret; breaks up and away fighting tears"),("Camera rig","F3 in SC02, F2/F1 in SC09"),("Audio","AUD-FILM"),
  ("Wardrobe never-list","No dresses except the wedding"),("Physical never-list","Never raises her voice at the lens; never touches Margaret's knee"),("Eyeline","Off-lens"),
  ("Voice spec","VOICE-SARAH"),("Stress register","Rises and cracks, then drops to near-whisper"),("Non-speech","Sharp in-breath; wet laugh"),("Mouth asymmetry","Assigned: right corner. Confirm")],
 "EMILY": [("Accent","Nottingham, young (confirm)"),("Pacing","Quick, bouncing"),("Posture","Open, hands outstretched to Margaret"),("Rest position","Hands held out, then at her sides"),
  ("Gesture register","Continuous, light"),("Ocular default","On Margaret"),("Camera rig","F2, F1 on the dance"),("Audio","AUD-FILM; kitchen radio under SC10"),
  ("Wardrobe never-list","Nothing her mother would wear: no plain grey knit, no black jeans"),("Physical never-list","Never sulks theatrically; the smile just drops"),("Eyeline","Off-lens"),
  ("Voice spec","VOICE-EMILY (steered above Sarah)"),("Stress register","A lift and a stretched vowel"),("Non-speech","Quick giggle"),("Mouth asymmetry","Assigned: left corner. Confirm")],
 "DOCTOR": [("Accent","Educated Edinburgh (confirm)"),("Pacing","Brisk, even, ~210 wpm"),("Posture","Seated at the desk, turns to the monitor, leans in once"),("Rest position","One hand on the mouse, one on the desk"),
  ("Gesture register","Restrained"),("Ocular default","Monitor, then Margaret"),("Camera rig","F2, F1 on 'So how did you just walk in here like that?'"),("Audio","AUD-FILM, small room"),
  ("Wardrobe never-list","No white coat, no stethoscope as costume, no readable name or hospital badge (§19B)"),("Physical never-list","Never touches the strap; never names a real institution"),("Eyeline","Off-lens"),
  ("Voice spec","VOICE-DOCTOR"),("Stress register","Slows and spaces the words"),("Non-speech","Nasal exhale; low 'hm'"),("Mouth asymmetry","Assigned: right corner. Confirm")],
}
