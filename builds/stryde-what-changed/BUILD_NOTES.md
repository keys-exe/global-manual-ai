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
