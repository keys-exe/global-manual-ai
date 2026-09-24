# Opening delivery data (steps 1-5) for the Six Weeks Ago build.
META = dict(build="SWA — Six Weeks Ago", product="Stryde Precision Strap", fmt="AI Drama VSL (§3B)", mode="Mode 4 · Realistic Film", standards="V7.55.1")

MEASURED = [
 ("Duration · aspect · resolution","340.4 s · 9:16 · 1080×1920 · 30 fps (AV1)","Format lock: long-form drama; 9:16 matches our lock"),
 ("Scene-change detection (thr 0.27)","161 cuts → 162 shots · mean 2.10 s · median 1.9 s · p90 3.66 s · max 5.63 s","Pacing is measured, not felt: ~2 s shots throughout"),
 ("Cut rhythm by act","HK 1.50 s · Before 2.36 s · Problem 1.82 s · Turn 1.88 s · After 2.59 s · Close 2.77 s","Fast open, fastest in the conflict and mechanism, breathes in the After"),
 ("Silence detection −35 dB / 0.3 s","6 gaps in 340 s; longest 1.66 s at 330.2 s (before end card)","Wall-to-wall score and dialogue; one designed silence before the offer"),
 ("Silence detection −45 dB / 0.5 s","2 gaps (290.1 s, 330.2 s)","Held beats are rare and placed at the two biggest payoffs"),
 ("Volume statistics","−14.2 LUFS integrated · LRA 14.0 LU · mean −18.5 dB · peak 0.0 dB","Dynamic drama mix, not hot-compressed UGC. CapCut keeps range"),
 ("Luminance timeline (mean Y)","HK 78 · BF 82 · PB 77 · TN 83 · AF 95 · OC 112","Colour script: dim and cool until the Turn, then +34 Y by the close"),
 ("OCR pass","Word-by-word burned captions, keyword in yellow, on every line · DAY 90 / DAY 180 cards · phone search UI at 92–94 s · end-card stack: LIMITED SALE · ORDER NOW · Link Below · 30-DAY MONEY-BACK GUARANTEE","All post type; none enters a prompt (§17)"),
 ("TH / B-roll ratio","≈ 75 % character dialogue shots · 25 % inserts, renders, cutaways","Talking-head dense with a cutaway every 3–4 lines; renders cluster in the Turn"),
]

STRUCTURE = [
 ("0–12","HK","Car-park near miss: protagonist falls with the grandchild, daughter screams; cut home, 'Sit down'","CONSEQUENCE","Crisis cold open, caption 'I kept convincing myself it…'"),
 ("12–46","BF","Husband confronts her: their daughter was crying; 'you've got your legs'; mother's history; grandchild asks why grandma never swims","CONSEQUENCE","Two-hander, inserts: slippers ECU, child at pool (loop planted)"),
 ("46–90","PB","Doctor consult: exam, legs ECU, compression prescribed, she refuses; 'you don't have years'","CONSEQUENCE","Authority raises the stakes"),
 ("90–100","PB","Car, phone search 'without surgery'","ILLUSTRATE","Platform UI on screen"),
 ("100–152","PB→TN","Friend arrives, reveals the same condition; drawer of garments; before photo on phone","CONTRAST","Messenger's own proof"),
 ("152–226","TN","Deck talk: herb inserts, green-glow anatomy renders, objection handling ('Amazon' copies)","MECHANISM","Renders cut in cold"),
 ("226–246","TN","Product reveal in hand, dosage, 'and if it doesn't work? Then it doesn't work'","PRODUCT","Low-pressure close of the Turn"),
 ("246–275","AF","Routine insert; husband: 'You just stood up'; daughter; DAY 90","CONTRAST","Mirror of the husband scene"),
 ("276–296","AF","Grandchild on lap; DAY 180; doctor tape measure 39 vs 46 cm","CONTRAST / EVIDENCE","Measurement numerals as proof"),
 ("298–316","AF","Friend hug; daughter reconciles; pool with grandchild","CONTRAST","Pays the pool loop"),
 ("318–330","OC","Dinner, porch, protagonist VO: sale, links below, 'do this for you'","CTA","Narrator close"),
 ("330–340","OC","End card over lifestyle frames","OFFER","Post-type offer stack"),
]

STYLE_LOCK = [
 ("Delivery register","Naturalistic family drama. Restrained, tears held then released; characters talk to each other, never to lens. VO only in the close"),
 ("Edit rhythm","Mean shot 2.1 s; hook 1.5 s; conflict and mechanism 1.8–1.9 s; After 2.6 s. Our cut targets the same by act"),
 ("Visual grammar","Singles at MCU/CU with shallow background, reverses on a held axis, ECU inserts on hands, legs and objects. Few wides; walks and arrivals on a follow"),
 ("Location register","Lived-in domestic interiors plus one clinical room; one golden-hour exterior-feel for the After"),
 ("Density pattern","Dialogue wall-to-wall; cutaway every 3–4 lines; renders only in the Turn; two designed silences at the biggest payoffs"),
 ("Retention architecture","Crisis cold open → loop planted early (pool / dance) → messenger with her own proof → objection handled → mirror-scene payoffs with time cards → offer spoken in-story"),
 ("Colour script","Cool, desaturated, low-key until the Turn; warm and lifted after. Measured +34 Y from Before to close"),
 ("Copy voice","Short plain sentences, lots of fragments, family names, repeated beats ('That's it.' 'That's it.'). Your script already sits in this register"),
]

SURFACED = [
 ("Burned word-by-word captions","Post type (§17)","CapCut caption layer, not generated"),
 ("Phone search UI on screen","Platform UI banned (§10A)","Our script has no search beat; if one is added it shows a generic, unbranded browser"),
 ("Tape-measure numerals as proof (39 vs 46 cm)","Measurement instruments fabricate evidence (§43)","Our proof is behavioural: stairs forwards, two miles each way, the dance. X-ray shows no numerals"),
 ("Named marketplace ('Amazon')","§10A","Our line is 'their website, the real one' — no platform named"),
 ("Green-glow stock anatomy renders","Position, not look","Same slot in the Turn, rendered in the §12A register and entered via Barbara's phone (SCREEN route)"),
 ("Their claims (herbs, 30-day guarantee)","Never inherited (§43A)","Our claims are tiered separately on the Claims tab"),
 ("DAY 90 / DAY 180 progress cards","Position, not look","Our '6 weeks ago' card, plus optional 'A week later / A month later / Sunday' cards (decision D8)"),
]

BEAT_IT = [
 ("Hook spends 12 s across two locations before the conflict lands","Each of our hooks is one location, one action, 12–18 s, conflict inside 3 s","HKA / HKB / HKC"),
 ("Mechanism cut in cold as stock-looking renders","Barbara shows the render on her phone first, then we cut inside (SCREEN → INSIDE)","TN-SC05-SH15, SH20, SH22"),
 ("Proof relies on a measured number","Proof is shown uncut: the first forward descent in two years","TN-SC06-SH04 to SH10"),
 ("Product reveal is a bottle held up to camera","Reveal lives inside the scene: Barbara pulls up her trouser leg","TN-SC05-SH05"),
 ("Offer delivered as VO over lifestyle frames","Offer spoken character-to-character on a phone call, then the end card","OC-SC11"),
 ("One mirror payoff per loop","Four mirror scenes: stairs (HKA↔SC06/SC09), tea tray↔kettle, wedding↔kitchen dance, 'who gets you down'↔'I'll manage the stairs'","AF-SC08 to SC10"),
 ("Runtime 5:40","Ours estimates 6:40–7:45 (unverified). Scene 5 alone is ~2:30, so it is paced at the reference's Turn rhythm (1.9 s) with inserts and renders","D10"),
]

FILM_LOOK = [
 ("1 · Genre and reference","British domestic family drama in the Sunday-night TV register: grounded, intimate, a tearjerker that resolves warm","Script + inspo"),
 ("2 · Camera and glass","Large-format digital cinema body, spherical primes: 24 mm wides, 35 mm MCU, 50 mm CU, 85 mm ECU and inserts; T2.0; faces isolated, room readable but soft on MCU","Inspo (shallow DoF by shot scale)"),
 ("3 · Light","Motivated by windows and practicals. Soft key, 4:1 in Before and Problem, 2:1 from the Turn on; lamps and streetlight at night; low warm sun in the After","Inspo + plates"),
 ("4 · Palette","Sets: sage carpet, cream walls, dark wood, dusky-pink upholstery, brass fittings. Wardrobe muted until the After. Colour script cool → warm by act","Plates + inspo"),
 ("5 · Grade","Before and Problem: slate-teal shadows, desaturated, low-key. From the Turn: amber highlights, lifted mids. Skin held natural in both","Inspo luminance"),
 ("6 · Optical texture","Soft highlight roll-off, light halation on backlit After shots, no diffusion on skin","Inspo"),
 ("7 · Motion","F2 locked for masters and inserts, F1 slow push on turns, F3 shoulder for arguments and the fall, F5 follow for arrivals, F4 slider for product and establishing","Inspo cut rhythm"),
 ("8 · Performance","Restrained. British understatement; tears arrive late and are fought","Script"),
 ("9 · Sound and post texture","Sparse piano score under dialogue; room tone; foley on stairs and bags; −14 LUFS with ~14 LU range; one LUT + one grain pass in the edit, never generated","Inspo audio"),
]
LOOK_STRING = ("A grounded British family drama shot on a large-format digital cinema camera with spherical primes, "
 "shallow depth of field that isolates faces while the room stays readable, soft motivated window light with practical lamps, "
 "a palette of sage green, cream, dark wood and dusky pink, slate-teal shadows and natural skin before the turn, "
 "amber highlights and lifted mids after it, soft highlight roll-off, no diffusion, no grain.")

LOCKS = [
 ("Format","AI Drama VSL, six acts HK · BF · PB · TN · AF · OC","§3B","Declared by the script header"),
 ("Mode","Mode 4 · Realistic Film","§2, §24G","Read from 'AI Drama' + a film-look inspo. Confirm (D0)"),
 ("Aspect","9:16, never letterboxed","§1, §24G","Locked"),
 ("Camera","CAM-FILM per Film Look Sheet field 2. No phone capture","§22, §24G","Locked"),
 ("Look","LOOK-SWA (Film Look tab), one LUT and one grain pass in post","§24G","Locked at step 2"),
 ("Sheets (cast)","Supplied five-panel sheets accepted; §19 panel check passed visually on all six","§19","Identity strings read off the sheets"),
 ("Readable wordmark with a body (worn, held, seating)","nano_banana_pro, 2k","§18A","Only model allowed"),
 ("Face seeds, MCU and tighter","nano_banana_pro, 2k","§18A","Measured candid register"),
 ("Volume frames with a person, no wordmark","nano_banana_2, 2k","§18A","Fast volume"),
 ("Frames with no person","nano_banana_2 · Sunburst (variant sunburst, quality high, 2k)","§18A","End card: Sunburst quality xhigh"),
 ("Mechanism renders","nano_banana_2 · nano_banana_pro","§18A, §12A","Anatomical register (Product Sheet)"),
 ("GPT Image on any body frame","Never","§18A rule 7","—"),
 ("Video — dialogue and MULTI-SHOT scenes","Seedance 2.5, ingredients mode, 720p","§18A, §44.5","Voice masters attached"),
 ("Video — single-shot inserts","Kling 3.0 (kling3_0), start image, ≤2,500 chars","§4, §44.5","—"),
 ("Voice","Supplied voice masters per character, all British (confirmed); Joan to be supplied or cast","§22D","D7"),
 ("Declared side","Margaret RIGHT (Hook C 'her right knee') · Barbara LEFT","Product Sheet §7","Held on every beat"),
 ("Product first appearance","TN-SC05-SH05 (Barbara's reveal). Nothing before the Turn","§9, §3B","Hook B strap concealed (D4)"),
 ("Product references","Canonical composite (front · three-quarter · rear) on every product call + REF-PROD. Placement refs: FRONT on straight-leg worn beats, BENT on seated / stairs / flexed beats, REAR on rear and turning beats","Product Sheet registry","The four product images you sent. Self-test passed: 18 strings, 24 checks"),
 ("Seating beats","Straight leg, strap starts mid-shin and seats on the tendon (SEAT-LOCK)","Product Sheet RULINGS","Bent-knee seating was tested and dropped"),
 ("Mechanism route","SCREEN on Barbara's phone first, then INSIDE","§24G","MODEL unavailable: the knee model is in SC07, after the Turn"),
]

CLAIMS = [
 ("P-030","Seventeen times your bodyweight goes through it. Every stride.","3","Not on the Product Sheet register. Generated as scripted, flagged; no numeral on screen","warn"),
 ("P-035","They measured it. Thirty four percent less strain, every step.","3","Product Sheet: generate normally as scripted creative. Any on-screen numeral is post","warn"),
 ("P-039","They spent three years building it with orthopaedic surgeons.","3","Product Sheet: surgeon claim, generate as scripted","warn"),
 ("P-039","Over two hundred thousand people wear one.","3","Product Sheet: volume claim, generate as scripted","warn"),
 ("P-036","Bone on bone, arthritis, worn cartilage, meniscus… that's the spot taking the weight… That's why nothing worked.","3","Efficacy across four named conditions. Flagged; not on the register","warn"),
 ("P-034 · P-052 · P-069","It changes where the weight lands / moves the weight off the worn part","—","A load-path mechanism. Product Sheet locks 'protection' (D1)","warn"),
 ("P-034","There's a silicone pad on the inside.","—","Advertiser-stated, unphotographed (Product Sheet inner_face_script). Inner face never rendered (D2)","info"),
 ("P-074","It's two for one right now.","—","BOGO terms unconfirmed. Generate as simulated promo","info"),
 ("P-074","Sixty days, and you keep the straps.","—","Guarantee unconfirmed. Generate as simulated promo","info"),
 ("P-039","Ten seconds to put on.","—","Observable; shown as a §9B seating demo, no timer on screen","ok"),
 ("P-052","Doctor: 'Keep wearing it.'","§19B","A generic doctor may recommend. The mechanism wording rides on D1","ok"),
 ("P-058–059","Two miles, each way","—","Story outcome, not a product claim. Typicality is the advertiser's call","info"),
]

DECISIONS = [
 ("D0","Mode","The script says 'AI Drama', which §3B runs in Mode 4 or 5. Mode 4 is explicit-instruction-only, so I've read the header as that instruction.","Confirm Mode 4. Your plates already sit in this look."),
 ("D1","Mechanism claim","The script pitches load-path (weight moved off the worn part) in P-034, P-052 and P-069. The Product Sheet locks 'protection' and marks load-path retired for this product. The Product Sheet outranks the script.","The lines are unchanged. Renders follow the sheet unless you switch MECHANISM_CLAIM for this build. Recommend switching: the whole Turn argues load-path"),
 ("D2","'Silicone pad on the inside'","Already logged on the Product Sheet (UNSETTLED inner_face_script, V7.49.12): advertiser-stated, unphotographed. The inner face is never shown.","The line plays as written. No beat shows the inside of the shell, so the pad is never rendered"),
 ("D3","'A small black strap'","The shell spans the whole front of the knee. 'Small' pulls the render undersized (NEG-PLACE bans it).","Direction ignored for render; 'That little thing?' still plays as dialogue"),
 ("D4","Hook B hem","A strap under the kneecap cannot show 'below a cropped trouser hem'. The hem covers the knee. §9 also keeps the product out until the Turn.","Default: CONCEALED, knees moving freely under the trousers. Alternate written alongside: a skirt clearly above the knee with the strap VISIBLE, flagged against §9"),
 ("D5","Hook C 'buckles sideways'","In P-027 Margaret says her knee doesn't hurt going sideways. Barbara's argument depends on it.","Render as buckling forwards under load on the bend. Flagged, line untouched"),
 ("D6","Scene 8 'hand resting on the rail'","Product Sheet after-state: reciprocal gait, never hovering near a rail.","Default: hands free at her sides on SC09. Say if you want the rail kept"),
 ("D7","Joan","Two lines, voice only on the phone. No voice master supplied.","Keep her off-screen, phone-filtered. Send a Joan voice or I cast one to a §22D brief"),
 ("D8","Time cards","Script headings 'that night', 'a week later', 'a month later', 'Sunday'. The reference used DAY 90 / DAY 180 cards.","Recommend cards for 'A week later' and 'A month later' only; the others read from the light"),
 ("D9","Doctor plate X-ray","The monitor X-ray is labelled 'L'. Margaret's strap is on the RIGHT knee.","Regenerate the monitor as a bilateral knee film with no letters"),
 ("D10","Runtime","About 919 words of dialogue plus ~38 silent shots: estimate 6:40–7:45 (unverified) against the reference's 5:40. Scene 5 is 417 words (~2:30).","No script change. Scene 5 is paced at the reference Turn rhythm. Your call if you want a trim pass"),
 ("D11","'Mom' in British mouths","You've confirmed the voices are British. 'Mom' is American and appears in P-001, P-064, P-066 and Hook A (Sarah's lines). A British voice saying 'Mom' will sound off, and NEG-DEFAULT-VOICE bans American vowel colouring.","Recommend changing to 'Mum' in all four places. It's a script edit, so it's yours to approve; until then the lines stay as written"),
 ("D12","Hook A/C time card","The '6 weeks ago' card after Hooks A and C jumps back from a moment that is itself in the Before.","Keep as the title device. It reads cleanly only after Hook B"),
 ("D13","Hall plate handrail","The stairs plate shows a brass-bracket wall handrail; the hall plate's stair wall has none.","Redress the hall plate with the wall rail before any hall master is built"),
]

CAST = [
 dict(id="MARGARET",role="Protagonist, 71",sheet="Silver-grey chin-length bob with a side part; hazel eyes; broad face, soft jowl, fine forehead lines, a small healed mark on the nose bridge; fair skin with pink cheeks; heavy-set, rounded shoulders",
      voice="Master supplied · F0 ≈ 163 Hz · 172 wpm · 10.1 s",note="Sample says 'Kirsty' where the script says 'Sarah'. Use as voice master only, never as a take",beats=0),
 dict(id="BARBARA",role="Cousin, 74 · the messenger",sheet="Short spiky white-silver crop; pale blue eyes; weathered, deeply lined skin, a raised mole on the left neck; stocky, heavy-set; signature purple",
      voice="Master supplied · F0 ≈ 178 Hz · 159 wpm · 11.7 s",note="Only 15 Hz above Margaret. In their 2:30 two-hander, separate them by pace and energy: Barbara brisker and drier",beats=0),
 dict(id="FRANK",role="Husband, 70s",sheet="Swept-back white hair, bushy white brows, grey-blue eyes, ruddy nose, heavy jowls; oatmeal cable cardigan over blue check shirt (signature cardigan)",
      voice="Master supplied · F0 ≈ 142 Hz · 235 wpm · 7.7 s",note="235 wpm is fast for a night-time line in the dark. Direct SC03 and SC08 slower",beats=0),
 dict(id="SARAH",role="Daughter, about 50",sheet="Dark brown jaw-length bob, grey threads at the part; brown eyes; lean, long face, fine lines; grey crew jumper, black jeans, white trainers",
      voice="Master supplied · F0 ≈ 213 Hz · 174 wpm · 9.7 s",note="—",beats=0),
 dict(id="EMILY",role="Granddaughter, the bride",sheet="Long straight mid-brown hair, centre part; hazel-green eyes, light freckles; slim; cream cable jumper, light jeans, tan boots",
      voice="Master supplied · F0 ≈ 208 Hz · 176 wpm · 7.1 s",note="The sheet reads mid-30s. Fine for Sarah's daughter; say if you want her younger",beats=0),
 dict(id="DOCTOR",role="Knee doctor, 40s–50s",sheet="Dark curly hair greying at the temples, brown eyes, stubble, lean long face; light-blue shirt, rolled sleeves, navy knit tie, navy chinos, tan brogues",
      voice="Master supplied · F0 ≈ 108 Hz · 213 wpm · 11.0 s",note="Generic role, no real clinician or institution named (§19B)",beats=0),
 dict(id="JOAN",role="Friend · phone only",sheet="Not sheeted (off-screen)",voice="Not supplied",note="D7",beats=0),
 dict(id="W1 · W2",role="Commuters, late 40s · Hook B only",sheet="One-off subjects, not sheeted (§13)",voice="Seedance-generated in scene",note="—",beats=0),
]

LOCATIONS = [
 dict(id="L-KIT",name="Kitchen",dwelling=True,status="PLATED · supplied",scenes="HKC · SC02 · SC05 · SC10",
      anchors="Galley run of maple-effect cabinets on the left, cooker and kettle; sink under a garden window with a rotary line and fence beyond; teal tile stripe; cream retro radio on the sill; cork board and calendar; small drop-leaf table with floral oilcloth and two pine chairs on the right; beige vinyl floor with a worn patch; swirl-textured ceiling",
      light="Garden window, back of the house. Soft daylight from frame centre; warm low sun in SC10"),
 dict(id="L-STAIR",name="Staircase (from the landing)",dwelling=True,status="PLATED · supplied",scenes="HKA · SC06 · SC09",
      anchors="Straight flight, about 13 treads, sage floral carpet with brass stair rods; dark-wood handrail on white panelled balustrade (left, descending); brass-bracket wall rail on the right; framed family photos climbing the wall; newel post with a brass pyramid cap at the top; wicker laundry basket on the landing",
      light="Landing window upper left; frosted front door glows at the foot"),
 dict(id="L-HALL",name="Hall and front door",dwelling=True,status="PLATED · supplied · redress (D13)",scenes="HKA · SC08 · SC09",
      anchors="Frosted-glass uPVC front door; sage carpet; stairs rising on the left with the photo wall; hexagonal brass lantern pendant; coat hooks with a navy and a stone jacket; mahogany telephone table with a corded phone; kitchen visible through the open door at the end",
      light="Front door is the key; kitchen window warms the far end"),
 dict(id="L-BED",name="Bedroom",dwelling=True,status="PLATED · supplied",scenes="SC03 · insert BF-SC02-SH09",
      anchors="Double bed with quilted ivory spread and waffle throw; dark-wood wardrobe and chest; open drawer with old knee braces spilling out; bedside table with glasses, water glass and blister packs; floral curtains over net; door ajar to the landing",
      light="Night: streetlight through the nets, a sliver of landing light at the door"),
 dict(id="L-LIV",name="Living room",dwelling=True,status="PLATED · supplied",scenes="SC11",
      anchors="Dusky-pink wingback armchair with lace antimacassar in the bay; matching sofa; nest of tables with a cordless phone, coasters, newspaper and glasses; marble fire surround with a brass gas fire; wedding photos on the mantel",
      light="Bay window at the front, soft and bright"),
 dict(id="L-WED",name="Wedding reception room",dwelling=False,status="PLATED · supplied · add guests in the master",scenes="SC04",
      anchors="Golf-club function room: leaded windows and a picture window onto the course, parquet dance floor, DJ booth with light bar, three-tier cake, round tables in white with ivory chair sashes, fairy lights",
      light="Low golden sun through the picture window, fairy lights as practicals"),
 dict(id="L-GP",name="Doctor's consulting room",dwelling=False,status="PLATED · supplied · fix monitor (D9)",scenes="SC07",
      anchors="L-shaped wooden desk, monitor with a knee X-ray, keyboard, glove box, anatomical knee model; blue exam couch with paper roll; vertical blinds onto a car park; two plastic chairs; green-tinted ceiling panels",
      light="Window from the right, flat overhead panels"),
 dict(id="L-STN",name="Station staircase",dwelling=False,status="NOT PLATED · generate before Hook B",scenes="HKB",
      anchors="Wide commuter staircase with rails at both sides and one down the middle; rush-hour crowd",
      light="Morning daylight from the concourse above, warm AF grade"),
]
PROPERTY_CHECKS = [
 ("C0 · rooms of one dwelling","Kitchen, stairs, hall, bedroom, living room","PASS","One house. A Property Sheet and property plate are written first (§30G)"),
 ("Finishes consistent across rooms","Sage floral carpet, cream walls, swirl ceilings, sapele doors, brass fittings match in all five","PASS","—"),
 ("Stair geometry, hall vs landing view","Balustrade and photo wall sit on matching sides","PASS","—"),
 ("Stair rails","Landing plate has a wall rail; hall plate has none","FAIL","D13: redress the hall plate"),
 ("Orientation","Front: hall door and living-room bay. Back: kitchen window onto the garden","PASS","Light profiles reconciled to it"),
 ("Script props present","Braces drawer, pills, radio, kettle, table, newel post, coat hooks, phone","PASS","—"),
]
