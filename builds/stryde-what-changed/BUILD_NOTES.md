# Build notes — stryde-what-changed (STRYDE · What Changed, podcast, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1zFGMzZ-olam9tpD63hM5MvHlUMkUVHKW
- User message: "RUN MANUAL. BRITISH" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 3 in script (A/B/C) + one shared body → 3 videos.
- Script file had no extension (Word 2007+) → `intake/script.docx`; spoken lines `work/script_lines.txt`, per part `work/script_{HK1,HK2,HK3,BODY}.txt`
  (the "A —" / "B —" labels and the hook quotation marks removed by hand; no spoken word touched).
- Product Sheet in the folder is V7.49.29; the repo's V7.49.37 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/3uy6935ZTAivEZgysENYvq · Old https://claude.ai/artifact/T3RZo3ak1QfC2ue6yaV9LD · Final https://claude.ai/artifact/6aiYxibqFq5F9R8tMiqp2z · Plan https://claude.ai/artifact/SGxFerhs4WKGiy3uV5bh8R

## Sessions
- session_01F5f9WBysAi6Tgspjop271s (2026-09-29 11:20 UTC): steps 1–3. Inspo measured (195.5s, 115 shots, 176 wpm, host ~55% on camera,
  cut-out PiP on most B-roll), absorption, ledger (VN01 = hook line 1 as VO over B-roll), phrase inventory, claims (F2–F11), Mode & Model Lock.
  Cast: H-HOST, R1-MAUREEN, R2-DESMOND (landed 11:50, board To check) on Higgsfield (Sunburst, 2k, one each; R2's first call returned 503 before starting, sent once more).
  Higgsfield 17,537 credits before the cast. Four boards made; docs/absorption on Plan + Current.

- 12:08 UTC hourly Fix check: H-HOST Fix "change host avatar to more attractive or have pleasing personality" → v2 (job b9242d45…, Sunburst):
  attractive/warm face fill, 44, `NEG-DEFAULT-FACE` without "catalogue-model bone structure" and its last two clauses, "unflattering" dropped
  from `SKIN-T` (H only; §34 correction for this sheet, `cast/build_sheets.py` `host=True`). v1 moved to Old (asset 10c81baa…), deleted from Current.

- 12:25 UTC user "fix": H-HOST Fix "change the host, i want different person have pleasing personlaity" → v3 (job e6a49b97…): a new person —
  white British woman, 41, honey-blonde, freckles, beauty mark, cream cable-knit; same warm face register as v2. v2 moved to Old (asset 700dc380…).

- 12:45 UTC user "I'VE CONFIRM PROCEED": H-HOST v3, R1, R2 confirmed (flags unanswered → voiced as written, open).
  Steps 4–5: plates P0-STUDIO, P1-PROP-M, P2-PROP-D, P3-STREET, P4-KITCHEN, P5-CONSULT (Sunburst 16:9) + S1-SURGEON sheet (§19B)
  + H-VOICE-IMG (§22U step 1, nano_banana_pro requested, logged nano_banana_2) → board To check. Act map `work/actmap.py`
  (61 rows: 44 B-roll + 17 TH; pip on B06, B12, B20; `angles.py` PASS HK1–HK3), wardrobe map, `STEP4_5.md`; docs/locations,
  docs/actmap, docs/wardrobe on Plan + Current; 44 planned beat cards. Kling takes G1/G2 built (`voice/H_G*.kling.json`, 2,441 / 2,417).

- 13:00 UTC user "fix those": board → all 6 plates + S1-SURGEON confirmed; H-VOICE-IMG Fix "medium shot only, not too wide" →
  v2 (job bccb1cd0…, waist-up, face ~¼ frame height, no knees/legs; nano_banana_pro requested, logged nano_banana_2). v1 to Old (asset 0b58b0a8…).

- 13:08 hourly check: H-VOICE-IMG v2 confirmed → §22U straight through. Kling at 3 credits → Kie `kling-3.0/video` (pro, sound, 10s):
  G1 057fb576… (15 words, cut from HK1's first clause to pass the 20-word 10s budget), G2 c252fcb9… (19 words); preflight PASS both.
  `voice_source.py` PASS (190.5 / 188.2 Hz, 31.9 s) → ElevenLabs IVC **`Changed` = YlKDROvtue2RvBG9MAKL**. Enhance run by hand on
  HK1+HK2+HK3+BODY (`vo/enhanced.fitted.txt`, 5,025 chars, `[slowly]`/`[pause]`, verbatim PASS) → 4 eleven_v4 takes at speed 0.9
  (T1 174, T2 177, T3 174, T4 172 wpm). Take check `work/take_check.py` (cut_points.py's number map lacks 5,000 / 70 million):
  T1 PASS (small.en missed "your"; medium.en hears it) = **working take**; T3 "that is" → "that's". Cuts T1: 10.34 / 25.91 / 41.82 s.
  User (mid-run) "CONFIRM ALL LOCATION. PROCEED"; "VOICE ID: PROCEED" → asked: keep `Changed` (answer: keep).
  HeyGen photo avatar 1f288b8b… (H-VOICE-IMG v2); Avatar V rejected motionPrompt (no digital twin) → Avatar V without it (§22U (c)),
  video 20d477e9…, 254.06 s → cut HK1/HK2/HK3 + BODY → `trim.py` natural PASS: HK1 213.2 s 182 wpm, HK2 217.8 s 185, HK3 218.8 s 181.
  Board: user chose the 4 Mbps re-encode (trim.py output ~320 MB each); TH-ALL-T1 untrimmed (133 MB, parts) + TH-HK1…3 (~112 MB).
  Hook 1 images HK1-a (Maureen's legs on her stairs, NB2 → logged nano_banana_flash) + HK1-b (ANAT-A hot spot) → To check.

- 15:07 hourly check: user confirmed VO parts on the board — **HK1 + HK2 = T4, HK3 + BODY = T2** (VO locked, `voLocked`).
  §22U step 10 → talking heads regenerated: `vo/VO_LOCK.mp3` (T4 HK1 + T4 HK2 + T2 HK3 + T2 BODY, untrimmed, cuts 10.44 / 25.76 / 41.39 s)
  → HeyGen Avatar V in one go (video 2de76968…, 249.4 s, no motionPrompt) → cut + `trim.py` natural: HK1 3:30 185 wpm, HK2 3:34 188,
  HK3 3:36 183, all PASS → 4 Mbps board encode (`vo/th/lock/`). T1 talking heads (4 cards) + the 12 unchosen VO parts moved to the
  Old board, their files deleted from Current. One upload part began with '<' and was refused as markup → boundary moved one byte
  (TH-ALL-LOCK parts: 14,999,999 + 7,500,001 + 7,500,000 + …; the join is byte-exact).

- 16:40 user "confirm": board shows HK1-a + HK1-b images confirmed; talking heads (TH-ALL-T1, TH-HK1…3) set to `use` on that word.
  Hook 1 clips (`work/clips.py`, §27G, locked-off tripod, `preflight.py` PASS): E6 from the trimmed HK1 variant's word timings
  (HK1-a 0–4.28 s → 6 s; HK1-b 4.28–7.64 s → 5 s). Kling at 3 credits → Kie kling-3.0: HK1-a 7bbb2401… (108 cr), HK1-b 6b510627… (90 cr) → To check.

## Where it stands
- **Waiting on the user:** Confirm/Fix Hook 1's clips HK1-a, HK1-b (step 6 gate), then Hook 2's images. Their clips (Kie Kling 3.0 while Kling is short) follow each image's Confirm; E6 lengths from the T1 cuts.
- Board storage: Current ≈ 0.65 GB used of 1 GB after the talking heads — B-roll clips will need the Final/Old split or a second store.
- Open flags: F2, F3, F5, F6, F8, F9, F11 (claims).

### 2026-09-29 — Hook 2 images
- Hook 1 images and clips confirmed (board `use`). Hook 2 start images generated (`work/beats.py HK2-a HK2-b`, nano_banana_2 2k 9:16, one render each; HK2-b refs R2 sheet + P2 plate; new light `D-GREY-L`, colour `D-STAIRS-AM` 6500K). Jobs e16327a8 (HK2-a), a7ba052b (HK2-b); on the board as To check (`hooks/HK2-*_v1.png`).
- HK2-a shows no thumb against the tendon (F2 unanswered).
- Video connector: Kie AI `kling-3.0/video` (Kling account 3 credits) — told the user.
- User "CONFIRM": HK2-a / HK2-b images confirmed. Hook 2 clips (`work/clips.py`, §27G locked-off, `preflight.py` PASS), E6 from the trimmed HK2
  variant (HK2-a 0–3.36 s → 5 s; HK2-b 3.36–6.80 s → 5 s). Kie kling-3.0: HK2-a 1cbc2673… (90 cr), HK2-b f2445f70… (90 cr) → To check.
- User Fix on HK2-a image: "GIVE ME DIFFERENT BROLL" → HK2-a re-planned (act map + `beats.py`): no longer ANAT-A (too close to HK1-b) —
  MCU Desmond seated on his bottom stair tying his right trainer, bent bare knee nearest the lens, high three-quarter (angles.py PASS).
  v2 job f20c462e (refs R2 + P2) → To check. v1 image + v1 clip moved to the Old board, deleted from Current. HK2-a clip in
  `clips.py` still describes the anatomy swell — rewrite it (one lace tug) once v2 is confirmed. HK2-b clip still waiting on the user's check.
- User Fixes: HK2-a "I WANT ANATOMY B ROLL HERE" → anatomy again but an ECU of the tendon as a band, high three-quarter
  (ANAT_A_POINT_TIGHT kept), v3 job 512cb5a0. HK2-b "GIVE ME DIFFERENT BROLL HERE" → Desmond rising out of a deep squat with a heavy
  box of old football kit in his hall, low front, v2 job fd0fae7c (refs R2 + P2). Act map rows updated, angles.py PASS. Replaced
  versions (HK2-a v2 image; HK2-b v1 image + v1 clip) moved to the Old board, deleted from Current. Both clips in `clips.py` need
  rewriting to the new shots once the images are confirmed (HK2-a: the band draws taut once; HK2-b: one lift out of the squat).
- HK2-a v3 image confirmed on the board → clip rewritten to the band shot (`clips.py`: the band draws taut once, spot brightens once;
  preflight PASS), Kie kling-3.0 497adfd7… (90 cr), 5 s → To check (video v2; v1 was the old front-view shot, already on Old).
- HK2-b Fix "FIX THIS" (no detail) → read off v2: face partly in frame, Nike logos on the trainers, "OLD KIT" on the box, shallow squat with
  the box in front of the knees. v3 prompt fixes all four (top edge across the chest, plain unbranded trainers, unmarked box, deep squat with
  the box between the knees), job ec0b55bb → To check. v2 image moved to Old, deleted from Current.
- HK2-b Fix "FIX THE BROLL" → v3 still had the face in frame and the box floating between the legs with the hands on the knees.
  Front-on keeps pulling the face in → re-planned side-on, cropped at the waist (act map LOW/PRO, angles.py PASS), both hands under the
  box's bottom corners, no face identity text in the prompt. v4 job a9e02dbb → To check; v3 moved to Old, deleted from Current.
- User "CONFIRM, GO": HK2-b v4 image confirmed, HK2-a clip set to `use`. HK2-b clip (`clips.py`: one lift from the deep squat to thigh
  height, head never enters; preflight PASS) Kie kling-3.0 ba2bf463… (90 cr), 5 s → To check.
- Hook 3 images started on "GO": HK3-a (Maureen walking towards a ground-level lens on the pavement, cropped at the waist, refs R1 + P3,
  job 4eefcbcd) and HK3-b (act map changed to MS: the whole leg hip to foot, one small spot — a third anatomy look, not HK1-b's profile or
  HK2-a's band ECU; job a1ea8928) → To check. Faceless beats now carry no face identity text (the HK2-b lesson).
- User "CONFIRM GO": HK2-b clip `use`, HK3-a / HK3-b images confirmed. Hook 3 clips (`clips.py`, preflight PASS): HK3-a three walking
  steps towards the ground-level lens, 6 s (0–4.14 s), Kie 2d1677aa… 108 cr — 15.18 MB, split into 2 board parts (join byte-exact);
  HK3-b six stacking pulses on the one spot, 8 s (4.14–10.28 s; anatomy, not a human-motion beat), Kie b4e5fdd4… 144 cr → To check.
- User Fixes on Hook 3: HK3-a clip "FIX BROLL, WALKING/ STEPPING FAST" → §22X fault = motion pace (three steps at ~1/s) → two slow
  steps of ~2 s each, pace named, fast-walk negatives; same confirmed start frame; gen 2 preflight PASS (fix_note); Kie 023bd1e6…
  108 cr, 21.9 MB → 2 board parts → To check. HK3-b image "GIVE ME BETTER DIFFERENT BROLL" → re-planned (act map, angles.py PASS):
  from above and behind on Maureen's stairs, her plimsoll landing on the one worn pale patch at the centre of a tread, every tread
  worn the same — forty years of steps (refs R1 + P1), job 1206e3e7 → To check. Replaced versions (HK3-a v1 clip; HK3-b v1 image + clip)
  moved to the Old board, deleted from Current.
- User Fixes again: HK3-a "FASTER WALKING, NOT SLOW MO" (on the image field; the image is fine) → the first note "WALKING/ STEPPING
  FAST" was a request FOR a fast walk, misread as too fast in v2. v3 clip prompt written (`clips.py`: brisk real-time walk, about two
  steps a second, five or six steps, slow-motion negatives) — NOT SENT: a third video generation of one shot waits for the user's go
  (§22X); card left on `regenerate`. HK3-b "ANATOMY BROLL HERE" → anatomy again, a fourth look: low front three-quarter, knee bent under
  a landing, spot hot (act map + `beats.py`, angles.py PASS), v3 job 15bd1d26 → To check; v2 (worn stairs) moved to Old.
- User "FIX" in reply to the go request → the user's go for the third HK3-a clip (recorded as `user_go`): brisk real-time walk,
  Kie b8350fd2… 108 cr, 16.8 MB → 2 board parts → To check; v2 moved to Old. HK3-b v3 image confirmed on the board → clip (the knee
  takes a landing once a second, the spot flares brighter each time; 8 s, preflight PASS), Kie 3125c088… 144 cr → To check.
- User "PROCEED": all three hooks `use` (HK1–HK3 images and clips). Step 7 body B-roll started — Act 1 images, 12 beats
  (`work/beats.py`; `broll/<beat>_v1.png`; jobs in `broll/act1_images.json`), all nano_banana_2 2k 9:16, one render each → To check:
  B01a ANAT-B ghost limb (the tendon band), B01b Desmond ECU stepping down, B02 Maureen's fingertip below her kneecap, B04a Desmond
  climbing from behind, B04b Desmond stepping down through the spindles, B04c ANAT-C silhouette landing, B05 ANAT-B cutaway cartilage
  thinning (no glow), B06 ANAT-A pip (knee upper right, lower-left clear for the host cut-out), B07 Maureen pausing at the top of the stairs,
  B08a Maureen picking up her keys, B08b over Desmond's shoulder straightening a team photo, B08c Desmond rising off the bottom stair.
  Anatomy helper now takes the stack (ANAT-A/B/C) and slot overrides; eye-level angle lines drop the "not eye-level" clause.
- User (2026-09-29): "LET'S DO IT ONE BROLL AT A TIME, AND PUT BROLL FOR NEEDED SCRIPT LINE. BROLL FOR EVERY LINE."
  → (1) from now on one B-roll at a time, in cut order: its image → the user's check → its clip → the user's check → the next beat.
  The 12 Act 1 images already made stay on the board and are checked in that order. (2) Every script line gets its own B-roll:
  the 14 body talking-head lines each get a `-BR` shot (B01-BR, B03-BR, B06-BR, B07-BR, B08-BR, B08-BR2, B09-BR, B11-BR, B15-BR,
  B18-BR, B19-BR, B19-BR2, B21-BR, B22-BR), placed right after their line in `BODY`; the host's take stays on the timeline
  under it. Act map now 75 rows, 58 B-roll; angles.py PASS on all three variants; `docs/actmap` updated on the Plan and Current
  boards; 14 planned cards added. Hooks unchanged (VN01: the host on camera for each hook's last line — the script's own note).
  Build-specific, not a system change.
- User on the B01b line ("It sits two centimetres below your kneecap, on the front of the joint, and every step you take lands on
  it."): "PUT DIFFERENT BROLLS HERE" → the line split in two (act map 76 rows / 59 B-roll, angles.py PASS): B01b "…on the front of the
  joint," = ECU front of Desmond's straight bare knee, the tendon ridge under the skin (job c2453c7e); B01c "and every step you take
  lands on it." = ground level side-on, Maureen's plimsoll stepping down off the kerb (refs R1 + P3, job 656ef52d). Both → To check.
  Old B01b (Desmond stepping down the stairs) moved to the Old board, deleted from Current.
- User: B01b + B01c "CONFIRM, GO" → clips (`clips.py`, preflight PASS): B01b the knee straightens a touch, the ridge firms, 5 s
  (3.78 s line), Kie d1ad48dd… 90 cr; B01c one step down off the kerb, 4 s (≈2.4 s line, hold ≥ 3 s), Kie 70f34a9f… 72 cr → To check.
  B02 Fix "POINTING HER FINGER BELOW HER KNEECAP" (v1's finger sat on the thigh above the kneecap) → v2: whole kneecap visible, fingertip
  on the band just under its bottom edge, with negatives for above/on the kneecap; job 6fd48533 → To check; v1 moved to Old.
- B01c clip Fix "WALKING SINCE THE SCRIPT LINE IS 'EVERY STEP'" → §22X fault = motion (one step down, no walking) → she steps down
  and keeps walking out of frame, three or four real-time steps at ~2/s; same confirmed start frame; gen 2 preflight PASS; Kie 977ed02f…
  72 cr → To check; v1 clip moved to Old.
- B02 Fix "SHOW THE FRONT OF THE KNEE POINTING THE 'BELOW KNEECAP/ KNEE TENDON'" (v2 was side-on, the finger on the side of the
  knee) → act map B02 now eye/front CU (angles.py PASS); v3 front-on, kneecap centred, fingertip on the midline tendon just under it;
  job 5d3a123f → To check; v2 moved to Old.
- User: B02 image "CONFIRM, GO" → clip (fingertip presses once on the tendon and holds; 3 s floor, line ≈ 1 s; preflight PASS),
  Kie 7356567f… 54 cr → To check. B03 line ("It is not a big thing … since you were a teenager.") "BROLL HERE" → B03-BR image:
  overhead on the kitchen table, Maureen's hand at the page of a photo album, a faded 1970s snapshot of a teenage girl mid-stride on a
  seaside promenade (refs R1 + P4; no thumb shown, F2); job 62aeddb0 → To check. `beats.py` gains KITCHEN / KITCH-L/R / KITCH-AM.
- B01b + B01c clips confirmed on the board (`use`).
- User on the B03 line: "PUT DIFFERENT BROLLS HERE" → split in three (act map 78 rows / 61 B-roll, angles.py PASS): B03a "It is not a big
  thing. It is about as wide as your thumb," = ANAT-A low front, the big thigh muscle narrowing to the small band (F2: no thumb; job
  fabbd7d4); B03b "…taking your whole bodyweight, multiplied," = Maureen in the kitchen lifting a heavy cast-iron pot from a low
  cupboard, knees bent (job 46596a96); B03c "since you were a teenager." = the photo-album image (was B03-BR; card and file renamed).
  All three → To check.
- User: B03a / B03b / B03c "CONFIRM GO" → clips (`clips.py`, preflight PASS; screen times estimated at the locked VO pace):
  B03a the thigh muscle tightens, the load runs into the band, the spot brightens once (5 s, Kie 85f4f3a2… 90 cr); B03b she rises with
  the heavy pot (5 s, Kie c6f4e987… 90 cr); B03c her hand lifts the page edge (3 s — first Kie job 8a80c318 failed "Internal Error",
  0 credits, resubmitted once: Kie 3624872a… 54 cr). All → To check.
- User: B04a Fix "NEGATIVE BROLL, STRUGGLING TO Going up the stairs." → v2 Desmond struggling up, one hand gripping the rail, the other
  pushing on his thigh, face set with effort (eye/three-quarter MEDIUM, face in frame; job cf751279). B04b Fix "GOING DOWN WHILE HOLDING THE
  BANISTER, CHANGE THE BROLL" → v2 Maureen coming down towards a low front lens gripping the oak handrail, stepping carefully (job 7286093e).
  Act map rows updated, angles.py PASS; v1s moved to Old. B04c image "CONFIRM" → clip (the landing flares the spot once; 5 s, Kie
  441653e6… 90 cr). All → To check.
- User: B04a v2 image CONFIRM → clip (he levers himself up one step with effort; 4 s, Kie 84d457d0… 72 cr). B04b Fix "SHE'S GOING
  DOWN THE STAIR, NOT YET AT THE LAST STEP" → v3 halfway down the flight, six or seven treads up (job 0ae147b1); v2 to Old. B04c clip Fix
  "GOING DOWN THE STAIR" → §22X fault = motion (the leg did not visibly step down) → gen 2 names the descent (foot lowers and lands, the
  leg travels down), same confirmed start frame, preflight PASS; Kie 55ed7ddd… 90 cr; v1 to Old. All → To check.
- User image Fixes: B04b "HIGHER LAYER IN STAIR, STRUGGLING A LITTLE BIT" → v4 near the top of the flight, a hand braced on the wall,
  a small wince (job dc076019). B04c "WALKING DOWN THE STAIR" (image) → v2 ANAT-C silhouette figure, waist-down, walking down a short
  flight of visible steps, the leading foot landing (act map MEDIUM; job 6ae8e4ac) — both earlier clips (v1, v2) moved to Old, the clip
  is redone after this image is confirmed. B06 'ANATOMY "MORE DETAILS"' → v2 detailed joint (thin worn cartilage, menisci, collateral +
  cruciate ligaments, fat pad, fibrous tendon, muscle striation, bone texture), pip layout kept (job 32b9a21d). angles.py PASS; replaced
  versions on Old, deleted from Current. All → To check.
- User: B04b v4 + B04c v2 images CONFIRM → clips (preflight PASS): B04b two careful steps down, 6 s, Kie 6cb6e900… 108 cr; B04c the
  silhouette figure walks two steps down the visible stairs, the spot flaring at each landing, 5 s (new shot from image v2), Kie aefb1da6…
  90 cr. Both → To check.
- User Fixes: B04c clip "BOTH KNEE ARE LIGHTING" → §22X fault = anatomy (both knees glowed as each foot landed) → gen 2 of the image-v2
  shot: only the leading knee glows, the other named dark throughout; preflight PASS; Kie 702f6b72… 90 cr; v3 clip to Old. B06 image
  'PUT SOME ARROW POINTING THE patellar tendon, PUT SOME MOVEMENT, MORE DETAILED' → v3: one clean glowing arrow, no text, pointing at the
  tendon (the user's call overrides the no-arrow house default for this beat), the leg caught mid-step under load, higher anatomical
  detail, pip layout kept; job 47c5dbd5; v2 to Old. Both → To check.
- **Where it stands:** waiting on the user's check of the B02, B03a–c, B04a, B04b, B04c v4 clips and the B06 v3 and B01a images.

- 2026-09-29 — B06-BR ("It happens to everybody."): user asked for 2–3 people with knee trouble, then "NOT SAME AGE". Act map row rewritten (three people, a man in his seventies on the bus-stop bench rubbing his knee, a woman in her forties at the shelter post easing her knee, a man of about 25 in running kit limping past); angles PASS. Image v1 (nano_banana_2, ref P3) on the Current board as To check.
- 2026-09-29 — B06-BR image confirmed ("GO CONFIRM") → clip v1 (Kie kling-3.0, 3 s, 54 cr): the runner limps towards camera, the older man rubs his knee, the woman eases her knee at the post. On the board as To check.
- 2026-09-29 — B06 image Fix "MORE ARROWS, MORE DETAILS" → v4: several force arrows pour down the thigh onto the one tendon spot + one pointer arrow, more anatomy (quad heads, bursa, capsule, blood vessels). v3 moved to the Old board. To check.
- 2026-09-29 — B06 image v4 confirmed → clip v1 (Kie kling-3.0, 6 s, 108 cr): light pulses down the arrows onto the spot. Seen on my check: the pointer arrow drifts in and out and a faint second-limb edge shows at the right mid-clip. To check.
- 2026-09-29 — B07-BR split per user ("The cushion gets thinner. (CUSHION IN KNEE GETS THINNER)" / "The weight stays exactly the same. MAKE ME A BROLL HERE"): B07-BRa ANAT-B front-on cushion worn thin; B07-BRb Maureen waist-down, low front, coming down her stairs with a laundry basket (replaces the planned worn-plimsoll shot). Act map 79 rows / 62 B-roll, angles PASS. Both image v1 To check. Seen on B07-BRb: the crop reaches her chin (not the waist), the basket is on her right hip, the landing foot hovers, and the stair wall is on the left (the plate has the wall on the right).
- 2026-09-29 22:08 hourly Fix check — no Fix notes on the Current or Final board. B01a image had been confirmed on the board with no clip yet → clip v1 (Kie kling-3.0, 3 s, 54 cr). Seen on my check: the model turns to three-quarter by the end (it was told not to move) and the glow slides down onto the top of the shin. To check.
- 2026-09-29 — B06 video Fix "MOVING ALL ARROW, DETAILED FOCUS ON THE TENDON" → v2 (gen 2, Kie 6 s, 108 cr): arrows travel in onto the spot, slow push-in onto the tendon. Seen on my check: the push-in works, but the arrows are gone after about 2 s (they leave the frame as it closes in). v1 moved to the Old board. To check. A third B06 video waits for the user's go (§22X).
- 2026-09-29 — B07-BRa and B07-BRb images confirmed ("CONFIRM GO"; the user kept both shots) → clips v1 (Kie kling-3.0, 3 s each, 54 cr each). B07-BRa: the gap between the bones closes and the cushion flattens; a small red dot shows in the joint gap. B07-BRb: she takes two steps down towards the lens with the basket, legs clean. To check.
- 2026-09-29 — user "The load does not thin with it — BROLL HERE" → new B06-BR2 (after B06-BR): Desmond on the pavement, knee height side-on, one heavy step, his whole weight on the knee. Act map 80 rows / 63 B-roll, angles PASS. Image v1 (refs R2, P3) To check. Seen on my check: the front foot is flat rather than just at heel strike; plain trainers, no face.
- 2026-09-29 — B07 image Fix "GIVE ME DIFFERENT BROLL HERE" → v2, a new shot: Maureen in her kitchen first thing in the morning, stopping half-risen from the table with a hand to her knee (refs R1, P4). v1 (top of the stairs) moved to the Old board. Seen on my check: she stands with one foot up on the chair seat rather than half-risen from it. To check.
- 2026-09-29 — B08-BR (user FIX on "Nothing about the way you walk changed, so you assume nothing changed.") scoped to that sentence; image v1: Maureen from behind walking down her hall to the front door. The rest of B08-TH ("And here is the part that catches people out…") is a new planned card B08-BRb (her plimsolls set down by the door). Act map 81 rows / 64 B-roll, angles PASS.
- 2026-09-29 — B06-BR2 image Fix "FOCUS ON KNEE" → v2: close-up of Desmond's right knee, side-on at knee height, shorts hem to mid-shin (act map framing → ECU; angles PASS). A small scab-like mark shows on the knee. v1 moved to the Old board. To check.
- 2026-09-29 — B07-BRa video Fix "THINNER" → v2 (gen 2, Kie 4 s, 72 cr): the cushion wears away to almost nothing, bones close together, no red dot. v1 moved to the Old board. To check.
- 2026-09-29 — B07 image v2 confirmed → clip v1 (Kie 4 s, 72 cr): she rubs her knee and looks down at it, puzzled; foot still up on the chair seat as in the image. To check.
- 2026-09-29 23:08 hourly Fix check — no Fix notes on the Current or Final board. B08-BR image had been confirmed on the board → clip v1 (Kie 5 s, 90 cr): she walks away down the hall to the front door, never turns; clean. To check.
- 2026-09-30 — B06-BR2 image confirmed → clip v1 rendered on Kie (task 7988372f634c448f8b4109b9f1b7de43, 3 s); the first download was cut short and the user stopped the re-download, so it is not on the board yet (card still `generating`).
- 2026-09-30 — user "give me brolls here" on "And here is the part that catches people out. You do not have to have done anything to your knees for this to happen.": split into B08-BRb (Desmond stopping on his stairs, hand to his knee, caught out; seen from the landing) and new B08-BRc (Maureen filling the kettle at her kitchen sink, an ordinary morning; replaces the planned plimsolls shot, too close to B08-BR2's boots). Act map 82 rows / 65 B-roll, angles PASS. Both images v1 To check. Seen on B08-BRb: he faces up the stairs towards the camera (reads as coming up, not down), and the trainers carry a swoosh-like logo.
- 2026-09-30 — B08-BRb and B08-BRc images confirmed → clips submitted to Kie (3 s and 5 s). B06-BR2 clip: Kie's file host is very slow today (~16 KB/s); downloading with curl resume.
- 2026-09-30 — B08a and B08b image Fixes "GIVE ME DIFFERENT BROLL HERE" → v2: B08a Maureen pulling a tartan shopping trolley along her street (refs R1, P3); B08b Desmond on his bottom stair holding an old scuffed leather football, face out of frame (refs R2, P2). Act map rows rewritten; angles PASS. v1s moved to the Old board. Seen on my check: in B08a she looks towards the lens; in B08b he holds the ball up in front of his chest rather than on his lap.
- 2026-09-30 — B08-BRc clip v1 (Kie 5 s, 90 cr) on the board: she switches the kettle on and looks out of the window; clean. To check.
- 2026-09-30 — user "FIX THOSE" (board notes: B08a "GIVE ME DIFFERENT BROLL HERE", B08b "CHANGE THIS IMAGE") → v3s: B08a overhead into her understairs cupboard, never-worn running trainers with a shop tag beside her worn plimsolls (refs R1, P1); B08b a hall shelf of old tarnished football trophies and a club pennant, his hand setting one back (refs R2, P2). Angles re-balanced (window rule): B08a overhead/front, B08b eye/three-quarter; PASS. v2s moved to the Old board. Seen on my check: B08a has half-readable lettering on a shopping bag at the back of the cupboard; B08b's pennant carries readable text ("CLUB … FOOTBALL", a year).
- Kie's file host is still slow: B06-BR2 and B08-BRb clips downloading.
- 2026-09-30 — B06-BR2 clip v1 (Kie 3 s, 54 cr) downloaded at last and on the board. Seen on my check: the frame drifts with his step, a hand hangs in at the top of the frame mid-clip, and a trainer with a swoosh-like mark swings into view at the end. To check. B08a/B08b cards: cleared a stale `regenerate` video status I had left on them.
- 2026-09-30 — user "FIX THOSE" (board notes B08a/B08b "CREATE NEW IMAGE FOR THIS LINE") → v4s with people instead of objects: B08a Maureen seated at the bus stop on her street, handbag on her lap (refs R1, P3); B08b Desmond jogging along his street in running kit (refs R2, P3). Act map rows rewritten; angles PASS. v3s moved to the Old board. Seen on my check: B08b's leading trainer shows a swoosh-like logo.
- 2026-09-30 — B08-BRb clip v1 (Kie 3 s, 54 cr) on the board: he holds his knee and looks down at it, stays on the stair; clean. To check.
- 2026-09-30 — B08a v4 confirmed → clip submitted to Kie (5 s). B08b and B08c Fixes "GIVE ME DIFFERENT IMAGE HERE": B08b v5 a veterans' Sunday football game on a park pitch, a grey-haired man in his sixties striking the ball (one-off extras, no plate, §19B); B08c v2 Maureen rising from her kitchen chair, side-on waist-down (refs R1, P4). v4/v1 moved to the Old board. User "BROLLS HERE" on B08-TH2: split into B08-BR2 "It makes almost no difference," (Desmond's old muddy football boots, refs R2, P2) and new B08-BR3 "because the load is not coming from what you did." (Maureen's plimsoll over her front doorstep, refs R1, P1). Act map 83 rows / 66 B-roll, angles PASS. Seen on my check: B08c reads as leaning at the table rather than rising from the chair; B08-BR2 shows the boots dangling from his hand by the door, not set on a rack, and a wood floor in his hall.
- 2026-09-30 — B08a clip v1 (Kie 5 s, 90 cr) on the board: she settles her handbag and turns to look up the road for the bus; clean. To check.
- 2026-09-30 — B08a clip: user "GO" → status `use`. B08b Fix "DIFFERENT IMAGE HERE, LIKE HOLDING PAST PICTURE" → v6: Desmond on his stairs smiling at an old faded photo of his 1980s amateur team, young him in the front row (refs R2, P2). Act map row rewritten; angles PASS. v5 moved to the Old board. To check.
- 2026-09-30 — B08b Fix "POV ANGLE" → v7: POV looking down from his seat on the stairs, his hands holding the old 1980s team photo, his knees and trainers below (refs R2, P2). B08c Fix "CHANGE TO FROM SITTING TO STAND UP AND WALK, OUTSIDE" → v3: Desmond getting up off a low front-garden wall on his street (refs R2, P3). Act map rows rewritten; angles PASS. Replaced versions moved to the Old board. Seen on my check: B08c's trainers carry large, clear swoosh logos (brand marks) despite the negatives; in B08b the young Black player in the photo is the goalkeeper in the back row, not the front row.
- 2026-09-30 — B06 Fix "MORE EFFECTS, MAKE IT 2 BROLLS HERE" (board: "GIVE ME NEW IMAGE HERE ADD MORE EFFECT"): line split. B06 "Seventeen times your bodyweight is still arriving, every step," → image v5: whole leg mid-step, glowing wave-fronts travelling down inside the thigh, bursting as a ripple at the knee (pip layout kept). New B06b "in exactly the same place." → image v1: front-on ECU, a glowing target spot with concentric rings of light. Effects kept inside the body (no external energy); shockwave/burst/arrow negatives lifted for these two only. Act map 84 rows / 67 B-roll, angles PASS. Old B06 image v4 and video v2 moved to the Old board. NOTE: B06 has had two videos, so its next video is gen 3 and needs the user's explicit go (§22X). Seen on my check: B06b's target sits on the joint line where tendon meets bone, a little lower than "just below the kneecap" reads.
- 2026-09-30 — B08b v7 and B08c v3 images confirmed → clips submitted to Kie (3 s and 4 s).
- 2026-09-30 — B06 v6 and B06b v2 from user Fix "ADD MORE EFFECT": five wave-fronts, energy threads along the fibres, a red-orange heat glow and a big impact flare (B06); a blazing target core with five rings, fibre streaks, a heat halo and a particle swirl (B06b). Effects kept inside the body; the ANAT "mid-intensity / one small spot" state lines were lifted for these two only. v5/v1 moved to the Old board. Seen on my check: B06's impact rings spill a little outside the leg outline.
- 2026-09-30 — B08b clip v1 (3 s, 54 cr) and B08c clip v1 (4 s, 72 cr) on the board. Seen on my check: in B08b the photo drifts around in his hands (faces in it stay stable); in B08c he rises and stands clean, swoosh logos still on the trainers as in the confirmed image.
- 2026-09-30 — user CONFIRM B06 v6 and B06b v2 images. B06b → clip v1 (Kie kling-3.0, 3 s, task 1b900ff4e06b4b830e5c04c7d16e23ee): impacts land on the one core once a second, a new ring ripples out each time, streaks race along the fibres; ANAT-LOAD stack/compress clause trimmed to the tendon (the stack is out of frame in the ECU); preflight PASS. B06's next video is its third generation → waiting for the user's explicit go (§22X).
- 2026-09-30 — user CONFIRM B08-BR2 image → clip v1 (Kie kling-3.0, 3 s, task 85027d9776c9cdeb4ec5b01f259e6436): his hand lowers the old muddy boots and sets them on the hall floor (the image shows the boots held in his hand, so the clip sets them down rather than onto a rack); preflight PASS.
- 2026-09-30 — user "BROLL HERE" on "Which is why most of what gets sold for this cannot work." → B09-BR (already in the act map, covers B09-TH): image v1 (refs R1, P4): Maureen's kitchen table, a grey knit sleeve, a black hinged brace, a plain white gel tube and a blister pack, her hand setting the pack down. All unbranded, no readable text. To check. Seen on my check: the table reads as warm pine rather than pale oak; the brace has black velcro straps (a brace, not like the product).
- 2026-09-30 — user CONFIRM B06 / B06b / B09-BR. B09-BR → clip v1 (Kie kling-3.0, 5 s, task 93c879546ee1288e26fdef92f30b7c54): her hand slides the blister pack into line and rests; preflight PASS. B08-BR2 clip v1 on the board (3 s, 54 cr); seen on my check: the boots twist to show their soles as he lowers them, then he drops them onto the doormat and they end half out of frame at the bottom. B06: third-video call written in clips.py (v6 image, wave-fronts travelling down the thigh, locked camera, 4 s, preflight PASS) but NOT submitted — the permission check held it because "CONFIRM" isn't the explicit "B06 GO" I asked for; waiting for the user's go.
- 2026-09-30 — user "GIVE ME BROLLS HERE" on B10a (sleeve) and B10b (brace). B10a act-map row rewritten: Maureen's own view down into her lap, pulling the grey sleeve up over her bare knee (was: sleeve on the table); angles PASS; docs/actmap v15 on Plan + Current. Images v1 (refs R1, P4 + the B09-BR image for the same sleeve and brace): To check. Seen on my check: B10a's sleeve sits like a cap over the kneecap rather than round the whole joint; B10b's brace is a bulky wrap with one long metal bar, her hands on the hinge.
- 2026-09-30 — B09-BR clip v1 on the board (Kie 5 s, 90 cr): her hand slides the blister pack into line and rests; the other things stay put; no text. To check. B06b clip download restarted from scratch (the first partial file had stalled).
- 2026-09-30 — B10a Fix "GIVE ME DIFFERENT IMAGE HERE" → image v2: low front-on, Maureen standing in her kitchen with the grey sleeve snug round her whole knee, her hands on it (act map row → LOW/FRO CU; angles PASS). v1 moved to the Old board. User confirmed v2 → clip v1 submitted (Kie 6 s, task 7a4db7563c074be79eef44f6f762d167, preflight PASS). B10b image confirmed → clip v1 (Kie 6 s, 108 cr, task aa743b219da3f4f0dc0385afb3f13208) on the board; seen on my check: in the last seconds the brace tips over and flattens, and its metal bar looks shorter.
- 2026-09-30 — **Current board storage full** (1 GB; 119 files, all current renders; the four talking heads are 466 MB). User chose a fifth board: **Current 2** https://claude.ai/artifact/Qd4yz771BETzysCzeReLCU (same template, BOARD_ROLE current). B10a–B23b cards (33) and the B10a/B10b images moved there; the plan docs are copied too; its builds doc has boards.current = Current 2. New B10+ renders go on Current 2. Hourly Fix check prompt updated to read both Current boards.
- 2026-09-30 — B06b clip v1 finally downloaded (the tempfile link was stuck; Kie's `POST /common/download-url` gives a fresh direct R2 link that downloads at full speed — use it for slow Kie downloads) and on the Current board (3 s, 54 cr). Seen on my check: the rings sit on the knee joint rather than on the tendon below it, and a bright white band runs down the shin.
- 2026-09-30 — Current 2 republished from the V7.74.1 template (merged in from the default branch). The other four stryde-what-changed boards (Current, Old, Final, Plan) still show the previous template.
- 2026-09-30 — user "BROLLS HERE" on the B10a and B10b lines: each split in two. B10a = "A sleeve squeezes the whole knee", new B10a2 = "and leaves that band carrying everything." (ANAT-B three-quarter: a faint grey knit sleeve squeezing the whole knee, the tendon band under it still lit and taut). B10b = "A hinged brace stops the knee going sideways,", new B10b2 = "and it was never going sideways." (ground-level front-on, waist-down: Maureen walking towards the lens across her kitchen, knees bending straight forwards; refs R1, P4). Act map 86 rows / 69 B-roll, angles PASS; docs/actmap updated on Plan, Current, Current 2. Both images v1 on Current 2, To check. Seen on my check: in B10a2 the glow sits right at the top of the tendon by the joint line; in B10b2 the camera reads nearer shin height than floor level.
- 2026-09-30 — B10a clip v1 on Current 2 (Kie 6 s, 108 cr): her hands smooth the sleeve round the knee, she stays standing; clean on my check.
- 2026-09-30 — user "BROLL HERE" on "Seventeen times your bodyweight is still arriving, every step": split. B06 = "Seventeen times your bodyweight" (the anatomy pip; its third video still waits for the user's go), new B06a2 = "is still arriving, every step," — from Desmond's landing, high and behind, him going down his stairs (refs R2, P2). Act map 87 rows / 70 B-roll, angles PASS; docs/actmap updated on Plan, Current, Current 2. Image v1 on the Current board (Current has ~12 MB left), To check. Seen on my check: a swoosh-like mark on his right trainer, and he stands with both feet on one tread rather than mid-step; more of his back is in frame than waist-down.
- 2026-09-30 — user "B06 GO" (explicit answer to the third-video question) → B06 video gen 3 submitted (Kie kling-3.0, 3 s now the line is "Seventeen times your bodyweight", task e37dca5c60e5c09dfbf6bc8d1ed1e0bb). Checked with the build's own preflight (the version from before the V7.71–V7.74 merge): the new §35A rules (≤ 1,000-char video prompts, confirmed motion plan, A/B image pairs) are a system update and, per CLAUDE.md, do not apply to this existing build unless the user says so.
- 2026-09-30 — B06 video v3 on the Current board (Kie 3 s, 54 cr). Seen on my check: the light waves travel on past the knee and end as rings round the shin, the leg bends and lifts through the clip rather than staying put, and a second limb edge shows at the top right late on. To check.
- 2026-09-30 — user CONFIRM B10a2 image → clip v1 submitted (Kie 4 s, task 97416a88fba20a8e473c7850225a717e; build preflight PASS). User CONFIRM on B10b → its video v1 set to Confirmed (the image was already confirmed). B10b2 Fix "GIVE ME DIFFERENT IMAGE HERE" → v2: ANAT-A in exact profile from slightly below, the knee bent forwards like a hinge in one flat plane, nothing turned sideways (act map row → ANAT LOW/PRO CU; angles PASS; docs/actmap on Plan, Current, Current 2). v1 moved to the Old board. To check. Seen on my check: the bones read a little oddly (a slim shaft in front of the tibia) and the glow sits low, on the front of the shin bone rather than on the tendon just under the kneecap.
- 2026-09-30 — B10a2 clip v1 on Current 2 (Kie 4 s, 72 cr). Seen on my check: the knee bends forwards a little and straightens during the clip instead of holding still; the sleeve stays put and the glow stays one spot. To check.
- 2026-09-30 — user "BROLLS HERE" on "Gel sits on the skin. A painkiller turns the alarm off and leaves the load exactly where it was.": B10c rewritten (Maureen seated, clear gel smoothed over her bare knee, a glossy film on the skin; was gel on fingertips); B10d split — B10d = "A painkiller turns the alarm off" (her thumb pops a tablet from a plain blister pack, glass of water), new B10d2 = "and leaves the load exactly where it was." (floor level at the foot of her stairs, her plimsoll landing on the bottom stair, knee taking her weight; refs R1, P1). Act map 88 rows / 71 B-roll, angles PASS; docs/actmap on Plan, Current, Current 2. All three images v1 on Current 2, To check. Seen on my check: B10c — the gel is on her knee but her hand rests on her thigh rather than smoothing it; B10d — the blister pack reads small and the pop isn't clear; B10d2 — she stands at the foot of the stairs rather than stepping down, camera nearer knee height than floor.
- 2026-09-30 — hourly Fix check: user Fix on the B06 image "REROLL THIS IMAGE / FOCUS ON THE KNEE / CLOSE UP / ADD MORE EFFECTS" → image v7: ANAT-A close-up on the knee joint, low three-quarter, wave-fronts pouring into the joint, energy threads along the tendon, heat glow, a big impact flare with four rings, arcs across the joint and a particle swirl (pip kept; act map framing updated, angles PASS). v6 moved to the Old board. To check. Seen on my check: the blazing core sits on the kneecap rather than just below it, particles drift outside the leg outline, and the knee sits left of centre so the lower-left isn't fully clear for the host cut-out. The B06 video v3 (made from v6) stays as a version; a new video from v7 would be the fourth and needs the user's go.
- 2026-09-30 — user CONFIRM GO on B10c, B10d, B10d2 → clips v1 submitted on Kie (B10c 3 s ad4b63c0…, B10d 3 s 0c6f2ff4…, B10d2 4 s 52a701a1…; build preflight PASS). Motion written to what each image shows: B10c her hand slides down and smooths the gel once over the knee; B10d her thumb pops one tablet into her palm; B10d2 she steps up onto the bottom stair, the knee taking her weight.
- 2026-09-30 — user CONFIRM B06 image v7, then "B06 GO" (explicit answer to the fourth-video question) → B06 video gen 4 submitted from the close-up (Kie 3 s, task 61d5734828eb83429b3416bd61bd9ce0; build preflight PASS). v3's faults fixed at the source: the waves now end at the knee, the knee holds its pose, the second limb named out.
- 2026-09-30 — B10c, B10d, B10d2 clips v1 on Current 2 (Kie 3 s / 3 s / 4 s). Seen on my check: B10c her hand smooths the gel over the knee, clean; B10d the tablet pops into her palm, clean; B10d2 she steps up onto the bottom stair and ends standing on it, clean. To check.
- 2026-09-30 — B06 video v4 on the Current board (Kie 3 s, 54 cr); v3 moved to the Old board. Seen on my check: the same fault as v3 — the rings of light still travel on down the shin despite "end at the knee" in the prompt, and the flare at the knee goes out mid-clip and returns at the end; the knee holds its pose and no second limb shows. Kling keeps reading "rings" as travelling. If the user asks for another, options: drop the rings from the motion (only the flare pulses and the particles turn), or a gentle push-in on a still frame.
- 2026-09-30 — user "BROLLS HERE" on "None of them are aimed at the spot. What that band actually needs is for less of your weight to land on it.": B11-BR rewritten (Maureen's fingertip on the spot just below her kneecap, the four remedies unused on the table behind — was an ANAT sleeve shot too close to B10a2); B12 split — B12 = "What that band actually needs" (ANAT-A profile, the tendon spot glowing hot, pip), new B12b = "is for less of your weight to land on it." (ANAT-B close on the tendon, the spot cooling to a calm pearly glow). Act map 89 rows / 72 B-roll, angles PASS; docs/actmap on Plan, Current, Current 2. Images v1 on Current 2, To check. Seen on my check: B11-BR is her own view looking down, and her finger sits on the side of the upper shin rather than just under the kneecap; B12's knee is on the left, not the upper right, so the lower-left isn't clear for the host; B12b is front-on rather than from above.
- 2026-09-30 — user "fix those and progress the confirm": the board held a Fix on B11-BR ("fix this, give me different image") and Confirms on B12 and B12b. B11-BR v2: ANAT-A front-on, a ghosted grey sleeve round the joint, ghosted brace side bars and hinges, a gel film on the skin — all around the knee, the one spot on the tendon below the kneecap glowing untouched (act map row → ANAT EYE/FRO; angles PASS; docs/actmap updated). v1 moved to the Old board. To check; seen on my check: the gel film barely reads. B12 and B12b clips submitted (Kie 3 s fa43c5ed…, 4 s 96438ea6…; build preflight PASS): B12 the spot pulses hotter with a step, B12b the spot cools to a calm pearly glow.
- 2026-09-30 — B12 and B12b clips v1 on Current 2 (Kie 3 s / 4 s). Seen on my check: B12 the spot pulses, but the leg drifts slightly and a thin sliver of a second limb shows at the right edge; B12b the hot spot cools and fades to a calm pearly band, clean. To check.
- 2026-09-30 — user confirm B11-BR v2 → clip v1 submitted (Kie 3 s, task f6cb6ecd781159545488b6284669fe6d; build preflight PASS): the spot pulses once, the ghosted sleeve and brace bars stay still.
- 2026-09-30 — B11-BR clip v1 on Current 2 (Kie 3 s, 54 cr). Seen on my check: the spot pulses as asked, but the frame drifts in slightly closer, the ghosted brace bars fade partly out mid-clip, and a thin edge of a second limb shows at the top right. To check.

### 2026-09-30 — "fix b10d2 / brolls for b13 to b14c"
- **B10d2 v2** (board Fix "give me different broll here"): Desmond, low side-on, pushing up off his bottom stair, hands on his thighs, both knees under his whole weight (R2, P2; act map row now LOW PRO). v1 image + its video moved to Old (`c5d64b50…`, `34435af8…`), deleted from Current 2; the video waits for the new image's Confirm. Flaw seen: the trainers carry a Nike swoosh despite the negative, and he reads as standing rather than rising off the stair.
- **B13 v1** (NBP; front.webp as Image 1, R1, P4): strap across one open palm, wordmark to the lens. Flaw seen: the band stands up as a stiff ring (FP05) and the shell's two peaks read weak.
- **B14a v1** (NBP; front.webp, worn_front.jpg, R1, P1): seated on her bottom stair, both hands seating the strap under the kneecap, wordmark readable. Flaw seen: bare feet (plimsolls asked).
- **B14b v1** (NBP; back_inner.jpg as Image 1, inner_face.jpg, R1, P4 — both imported to Higgsfield this round: `a4613068…`, `7bd450f9…`): the pad to the lens in one hand; pad matches the photo. Act map row: pad shown as the frame itself, video = a small tilt through the light (no pinned end frame).
- **B14c v1** (NB2 anatomy): strap drawn on the knee, glow below. Flaw seen: the shell sits over the kneecap / joint line rather than on the tendon below it, and the spot still reads red.
- All five on Current 2 as `review`; docs/actmap updated on Plan, Current and Current 2.

### 2026-09-30 — B10d2 confirm; Fixes on B13, B14a, B14b, B14c
- **B10d2** image v2 confirmed → video v2 (Kie Kling 3.0, 4 s, task `696c2659…`): he pushes up off his thighs to standing, feet planted, clean. The Nike swoosh from the image is still on the trainers (blur in the edit if kept). On Current 2 as `review`.
- **B13 v2** (Fix "fix the product"): held up by fingertips behind, band hanging soft. **Flaw: the shell came out as a plain rounded rectangle — no peaks, no notch — so it is still not the strap.** Next try if Fixed again: an image edit built on front.webp itself (the photo composited into her hand) rather than a fresh render.
- **B14a v2** (Fix "fix the woman"): read as "not Maureen" — v1 legs/hands looked younger and tanned, bare feet. v2: very pale older legs, age-spotted hands, plimsolls. Flaw: framed wider than asked and the strap is small in frame (below a quarter of the width, FP11).
- **B14b v2** (Fix "too big, fix size"): the strap now sits in one hand at true size, pad to the lens, matches the pad photo. Held upright, not sideways across the fingers as asked.
- **B14c v2** (Fix "fix the product"): now NBP with front.webp attached, front-on at eye level (act map row EYE FRO, NBP): the real strap seated on the tendon below the kneecap, wordmark readable. Reads well.
- v1s of B13/B14a/B14b/B14c moved to Old (docs + files), deleted from Current 2.

### 2026-09-30 — B13 Fix again; B14a, B14b confirmed → videos
- **B13 v3** (Fix "fix the product stryde"): made as an image edit of v2 with front.webp as Image 2 — only the shell swapped. The shell now has the two peaks, the notch, the chevron slides and the wordmark. Flaw: two gold rings on her hand. v2 moved to Old.
- **B14a video v1** (5 s, task `4d22c403…`, split in 2 parts on the board): the hands settle the strap and lift away; the strap stays put. Flaw: the hands fiddle rather than making one clean slide, and the shell turns a little on the knee.
- **B14b video v1** (5 s, task `5f9d667a…`): **flaw — the strap bends like rubber mid-clip (FP05/§27G rigid shell broken).** If Fixed, next try: a much smaller move (a slow push-in on a still hand) rather than a wrist tilt.
- **B13 v4** (Fix "fix the hand holding the stryde"): image edit of v3, only the hand changed — one ring, fingers curled behind, thumb at the lower-left corner; strap kept. Flaw: two fingertips still peek over the shell's top edge by the left peak. v3 moved to Old.

### 2026-09-30 — Fixes on B14a (video), B14b, B14c
- **B14a v3** (video Fix "FIX THE PLACEMENT, BELOW THE KNEECAP"): root cause was the start frame (strap at kneecap height, turned to the side), so fixed at the source as an image edit of v2 — **the edit barely moved the strap: v3 still has it high and turned. Not fixed.** Next go: a fresh render, not an edit — front-on (EYE FRO) seated knee, strap already seated on the tendon (PLACE_LOCK_C), hands at the slides, then a short "fingers lift away" video. Image v2 + video v1 moved to Old.
- **B14b v3** (Fix "FIX THE PRODUCT"): edit of v2 with back_inner.jpg as Image 1 — outline and pad closer to the photo; still held upright. Image v2 + video v1 (rubbery) moved to Old.
- **B14c v3** (Fix "FIX SIZE BIGGER"): edit of v2 — the strap now spans the whole front of the leg, slide to slide, below the kneecap, wordmark readable. v2 moved to Old.
- Learned: an image edit swaps or resizes a product well (B13, B14c) but does not move a worn product to a new place on the body (B14a) — placement changes need a fresh render.

### 2026-09-30 — "FIX AND CONFIRM": B13 v5, B14a v4, B14b v4; B14c GO → video
- **B13 v5** (Fix "CHANGE THE IMAGE, MAKE SURE THE PRODUCT IS RIGHT AND THE SIZE"): new image — the strap across her one open palm, two peaks + notch, chevron slides, wordmark readable, about palm-width (true size), band hanging behind. Shot came out front-on rather than from above.
- **B14a v4** (Fix "MAKE SURE THE STRAP STAY IN THAT PLACE"): fresh render asked front-on with the strap already seated below the kneecap. **Flaw: the model went side-on again and the strap sits on the side of the knee — third miss on placement.** Next go: an image edit built on worn_front.jpg (the real worn-placement photo, front-on) — her legs, skirt and stairs put round the real strap — rather than a render or an edit of our own frames.
- **B14b v4** (Fix "FIX THE PRODUCT SHOWING THE STRAP"): edit of v3 — the whole strap now, the band one closed loop with its keeper, pad to the lens. Reads right.
- **B14c video v1** (user "GO", 4 s, task `f7e3bbda…`): the glow calms, but **flaws: the camera pushes in a little and the strap creeps up to the kneecap in the last second.** Trim to the first ~2.5 s in the edit, or Fix.
- Replaced versions moved to Old (docs + files).

### 2026-09-30 — B13/B14b size Fixes; B14a confirmed → video v2; B14c video confirmed
- **B13 v6** (Fix "FIX THE SIZE") and **B14b v5** (Fix "FIX SIZE"): edits of v5 / v4 with the strap made smaller (read as "too big", every earlier size note on this product — FP02). Both came out smaller, but by less than the two thirds asked (about 85%).
- **B14a video v2** (image v4 confirmed; generation 2 — v1 slid and turned the strap, so this motion never touches it): the strap stays on the knee. Flaws: the camera drifts round towards the front, and her hands shift and clasp rather than lifting cleanly away.
- **B14c video v1**: user CONFIRM → `status: use` (the board had it at `ready`).

### 2026-09-30 — "CONFIRM GO": B13 and B14b videos (B14a, B14c videos confirmed on the board)
- **B13 video v1** (4 s, task `149f25fa…`): **flaw — the wrist turns and the shell bends round her palm instead of staying rigid.**
- **B14b video v2** (4 s, task `d972d0e8…`, generation 2): **flaw — the hand still moves and the strap twists and flexes.** A third video of B14b waits for the user's go.
- Learned (both beats): Kling bends the rigid shell whenever it sits in a hand in motion. Next go for a held product shot: a still image in the edit with a slow CapCut push-in (no generated motion), or a locked-off clip where nothing but the light changes.

### 2026-09-30 — "BROLLS HERE" B15-BR, B15, B16a, B16b, B16c
- New approach for worn shots (after three misses on B14a): **image edits of worn_front.jpg** (the real strap worn front-on, correctly placed) — only the leg, clothes and room change. Act map rows B15 and B16a moved to front-on (EYE FRO) to match.
- **B15** (Maureen, pale leg, denim hem, her hall) and **B16a** (Desmond, khaki shorts, his stairs): the strap sits exactly right, wordmark readable — the approach works.
- **B16c** (Desmond walking on the pavement): placement right; flaw — a Nike logo on the trainer at the bottom of the frame.
- **B15-BR** (fresh render): flaw — she stands on the stairs instead of sitting, and her fingers rest on her thigh rather than measuring the spot below the kneecap; the strap in her palm reads right.
- **B16b** (S1 at his desk, knee model, strap held up): reads well; the strap's peaks are soft.
- All five on Current 2 as `review`; docs/actmap updated on Plan, Current, Current 2.

### 2026-09-30 — "GIVE ME BROLLS FOR B17A TO B17C"
- Built as image edits of the worn shots that came out right (B16a v1 for Desmond, B15 v1 for Maureen). Act map rows B17a (HIGH FRO), B17b (LOW FRO, ECU), B17c (EYE FRO) moved to front-on; B15 and B16a relabelled LOW FRO (knee-height camera) so the angle check passes.
- **B17b** (her fingertip on smooth unmarked skin below the strap's edge) and **B17c** (his hand holding the bunched navy tracksuit hem above the strapped knee) read right.
- **B17a**: flaw — the tracksuit leg was not rolled up: the strap sits OVER the trouser fabric. Next go: build it from B17c's frame (knee bare, hem bunched above) with his hands at the slide ends.

### 2026-09-30 — "CONFIRM AND FIX THOSE"
- **Old 2 board** https://claude.ai/artifact/GeqiDkeUa1eYhvuFnt87Gq created (the Old board's 1 GB store is full); Current 2's build doc now points `boards.old` at it. Replaced renders from B15 on go there. Hourly Fix-check prompt updated to use it.
- **Videos (images confirmed): B15, B16a, B16c** (4 s each, Kie Kling 3.0). The strap stays in place in all three; the shell wobbles slightly in B15 and B16a; B16c's last half-second passes the lens.
- **Image Fixes:** B15-BR v2 ("FIX THE PRODUCT": the strap in her palm swapped for front.webp — peaks, notch, chevrons right); B16b v2 ("FIX THE SIZE, TOO BIG": smaller); B17a v2 ("GIVE ME DIFFERENT IMAGE HERE": from B17c v1 — hem bunched above the bare knee, both hands pressing the strap's ends); B17b v2 ("GIVE ME DIFFERENT BROLL HERE": Maureen coming down onto her bottom stair, the strap still in place — "no rolling down"); B17c v2 ("GIVE ME DIFFERENT BROLL HERE": Desmond on his stairs side-on in navy tracksuit bottoms, nothing shows). Act map rows B17a–c updated; angles pass.
- v1s moved to Old 2 (docs + files), deleted from Current 2.

### 2026-09-30 — "CONFIRM AND GO / FIX": B15-BR, B16b, B17a, B17b videos; B17c v3
- **Videos** (4 s each): B15-BR (her other hand slides down to mark the spot; the hand holding the strap stays still), B16b (the surgeon looks up and nods; strap held still), B17a (hands press the strap, let go; it stays), B17b (she steps off the bottom stair; the strap stays). The "holding hand stays still" rule held — no strap bending in any of the four.
- **B17c v3** (Fix "FIX THIS, GIVE ME DIFFERENT BROLL"): Maureen at her kitchen table in long navy trousers, legs crossed, tea in hand — nothing shows. Act map row rewritten (R1, L-KITCHEN, EYE THR MEDIUM). Flaw: her face is in frame (asked chin down); the kitchen reads a little different from the plate. v2 moved to Old 2.

### 2026-09-30 — "FIX THOSE": B17b v3, B17c v4
- **B17b v3** (Fix "USING OR WALKING"): edit of B15 v1 — Maureen walking towards the lens on the pavement, the strap in use and in place. Image v2 + video v1 moved to Old 2; the video waits for the new image's Confirm.
- **B17c v4** (Fix "WALKING WEARING PANTS"): edit of B16c v1 — Desmond's same stride on the pavement in long navy trousers covering the knee; nothing shows. Flaw carried from B16c: a Nike logo on the trainer. v3 moved to Old 2.
- Act map rows B17b (L-STREET, LOW FRO) and B17c (L-STREET, GROUND FRO) rewritten; angles pass.

### 2026-09-30 — "FIX AND CONFIRM", then "CONFIRM": B16c ×3; B17b, B17c videos
- **B16c ×3** (Fix "GIVE ME 3 BROLLS FOR THIS LINE, WALKING WEARING STRYDE"): three one-off people out walking with the strap on, each an edit of worn_front.jpg — B16c v2 a British Indian woman in her sixties on a park path; new B16c2 a white British man about seventy on a seaside promenade (three-quarter); new B16c3 a Black British woman in her late fifties on a high street with a shopping bag. Act map rows added (91 rows, 74 B-roll); angles pass. B16c v1 image + video moved to Old 2.
- User confirmed all three images → walking videos (4 s each; B16c split in 2 parts on the board). The strap stays in place in all three.
- **B17b video v2** (Maureen walking on the pavement, strap stays) and **B17c video v1** (Desmond walking in long trousers, nothing shows) — both clean.
