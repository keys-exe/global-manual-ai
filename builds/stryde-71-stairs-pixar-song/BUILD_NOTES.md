# Build notes — stryde-71-stairs-pixar-song (STRYDE · 71 Stairs Pixar Song · Manual · Mode 2)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1VZ709_1L6_cNjSadgDKn-BIKDGy89a5C — task "A - VID | Pixar Song | TOF | Pure Mechanism | Iteration | 71 Stairs Black American Woman"
- User message: the Drive link + "run manual, the song is inside". → RUN: MANUAL; **Mode 2 — 3D Pixar** (the task title); HOOKS → 1 (the song is one fixed piece); no VOICE to make.
- **The song is the voice master:** `intake/song.mp3` (copy of `71 Stairs Afro American Woman.mp3`), 228.02 s, vocal 0–222.7 s, ~165 sung wpm, ≈74 bpm (unverified). The script sung word for word (VN01). Lyrics `work/lyrics.txt` (108 lines, 615 words); word-timed lines `work/lyrics.timed.json` (faster-whisper small; 603/615 words aligned, "Stryde." at line 37 not heard — F4). Never re-voice, trim or speed it.
- Inspo = the original 71 Stairs ad (same file as `stryde-71-stairs`): 155.55 s, 9:16, 82 shots, mean 1.9 s, no silences (`intake/inspo_report.json`, frames in `intake/frames/`).
- Script doc is a native Google Doc (exported .docx by the fetch). Product Sheet V7.49.32 in the folder = older than the repo's V7.49.38 → repo sheet kept. 11 product photos byte-identical to `products/stryde/stryde_refs/`.
- Cast = the `stryde-71-stairs` cast recast in Pixar (VN04 "same Afro American Black Woman and entourage"): N, C1 Loretta, C2 the daughter.
- **Boards:** Current https://claude.ai/artifact/NPMPgJeXr6cgTvtuFGhkZc · Old https://claude.ai/artifact/3pEQz2pWLJwTNX5TuBdccV · Final https://claude.ai/artifact/FYK7PCvgLG4SLzj72YdBPn · Plan https://claude.ai/artifact/VEE8gmwPVbvhVMNSC5rBLY (owner keysibaldonado@gmail.com)
- **Hourly Fix check:** `trig_01YXJhp6bfhh6W1Khk5oAPrk` (:20 UTC, bound to session_014b6n9bhiR2XgZ38wPBL12w).

## Sessions
- session_014b6n9bhiR2XgZ38wPBL12w (2026-10-01 ~10:00–10:30 UTC): steps 1–3. Four boards published from `dashboard/generation_board.html` (V7.75.1 template after the default-branch merge);
  absorption (song-clocked structure map, Edit Grammar `EDIT-STRYDE-71-SONG`), ledger VN01–VN05, phrase inventory with song times (42 phrases, 615 words),
  claims, Mode 2 & Model Lock; 3 Pixar avatar sheets on Higgsfield (`nano_banana_pro` requested, **logged `nano_banana_2`** — §5 routing fault, 2 cr each)
  → Current board To check (assets 78a2cc62…, dd77d413…, 6adbaf4d…); `docs/absorption` on Plan + Current. Higgsfield 11,355.4 before the cast.
  **Mode 2 sheet form built here (F10)** — `cast/build_sheets.py`: the master has no Mode 2 sheet recipe; proposed as a Pending Amendment on the user's word.
  **Waiting on the user's avatar decision** and F2 (full Pixar vs hybrid), F3 (sung-to-camera bookends or none), F4 (is "Stryde." sung at 84–87 s).

- same session, ~10:25–10:35 UTC — **Fix round 1 (user: "i want new ones and loretta should not be too thin they should be the same size as the narrator")**:
  three new characters written (`cast/build_sheets.py` v2 — N oval face / silver twist-out / mustard + denim; C1 square face / silver bob / teal + khaki,
  **the narrator's build**; C2 heart face / afro puff / olive + black), "no writing on the canvas" + one-side marker clauses added (v1 drew panel titles
  and mirrored the marker). 3 jobs on Higgsfield (nano_banana_pro requested, logged nano_banana_2, 2 cr each) → v2 on Current as To check
  (assets 21896d82…, f0d9e11e…, fda069ae…); v1 files copied to the Old board (a86adc7f…, f0b774bc…, 3128f425…), Old docs written, v1 deleted
  from Current. VN04 re-read: same roles, new faces (user's call). `fix_patterns.py` run on the Current + Old dumps (`work/fix_patterns.md`): 3 notes (6 rows, each seen on both boards), one beat each — no repeating rule yet; the Loretta build note is a beat fix.

- same session, ~10:35–10:50 UTC — user **"CONFIRMED ALL PROCEED"**: the three v2 avatars set `use`, `docs/absorption` confirmed; F2 full Mode 2,
  F3 variant A (no singing to camera), F4 caption carries "Stryde." — all on my recommendations. **Steps 4–5 delivered (`STEP4_5.md`):**
  Property Sheet PROP-N (7 fields), location derivation (8 plates + incidentals), light plans; **8 Pixar plates** (16:9, nano_banana_pro → logged
  nano_banana_2, 2 cr each; P1/P2 with P0 attached as `image_references`) on Current as To check (`plates/build_plates.py`, Mode 2 plate form);
  **act map on the song's clock** — 76 B-roll rows, no talking heads, all 108 lyric lines covered in order, E6 call lengths from the lyric word
  timestamps (no `pending-master`, no splits), `angles.py` PASS (`work/actmap.py` → `actmap_rows.json`, `angles.json`, `actmap.md`, `plan.json`);
  wardrobe map, story-day map, ledger assigned; 76 planned cards + `docs/actmap`, `docs/wardrobe`, `docs/locations` on Current + Plan.
  Flags F14 (Loretta's pant leg vs FP13), F15, F16. Higgsfield 11,355.4 → ~11,323 after the cast and plates (14 renders × 2 cr).

- same session, ~10:50–11:05 UTC — **V7.76.0 landed on the default branch (§3C Music Video)** and describes this build: adopted (nothing was generated
  against the act map yet). Boards republished on the V7.76.0 template (Music stage); build doc `kind: "music"`, `voices` removed, `music` block; the song
  on Current as **MUS-BODY** (audio card, mp3 wrapped in mp4, To check; `music/MUS-BODY.cue.json` = the §40A register map with the lyric lines per section,
  `music.py check` report on the card; beat grid `music/MUS-BODY.grid.json`, 73.8 bpm pinned). **Act map re-gridded (§3C):** every cut on the last beat at or
  before the lyric cut (never late), rows carry `section` + `bars`; 15 rows under the 2.0 s floor merged into their neighbours (the EG05 montage is one card)
  → **61 rows**, 108/108 lines, no FLASH, no split, `angles.py` PASS. Board: 15 planned cards deleted, 61 rewritten, `docs/actmap` rewritten (Current + Plan).

- same session, ~11:00–11:10 UTC — user **"FIX THOSE"**: six plates confirmed (P0, P3–P7); **Fix round 2** on two: P1-LANDING "NOT THE SAME AS THE P0 PROP N"
  → v2 as an image edit of the confirmed P0 (Image 1 as `image_references`, the same flight from its top, sides restated for the new angle — HT17);
  P2-KITCHEN "I NEED A NEW UNIQUE ARANGEMENTS HERE" → v2 a personal Southern grandmother's kitchen of the same house (sage-green cabinets, yellow
  counter, breakfast nook, skillets, church fan, crayon drawings), P0 attached. `plates/build_plates.py` V2 block, `plates/*.v2.prompt.txt`.
  Both on Current as To check; v1 files on the Old board (2aa94055…, fce7cec3…), deleted from Current. fix_patterns: the "same as P0" note is the
  third build with it (HT17 already covers it) — no new rule.

- same session, ~11:25–11:40 UTC — P2-KITCHEN v2 **confirmed** by the user. **Fix round 3 on P1-LANDING** (user: "FIX THE P1 I WANT IT CONNECTED TO THE
  P0", board note "STILL NOT CONNECTED"): v2 had drawn a return stair with a half-landing. v3 = an image edit of P0 on **Kie `nano-banana-pro`** (true Pro —
  Higgsfield reroutes every Pro call to nano_banana_2; §5 "can't run" case), P0 uploaded to Kie as `image_input`, the prompt counting one straight flight of
  fourteen steps from its top, every side restated (`plates/P1-LANDING.v3.prompt.txt`). **Kie spend measured 963 credits** (262,932.8 → 261,969.8 — far
  above the 18 noted on not-your-cartilage; unverified why). The render keeps the camera at the hall floor (reads as P0's own view with a short extra flight
  in the foreground) — on Current as To check with that said on the card; v2 to Old (d696aabd…). If it fails again: §30G says hall, stairs and landing are
  TRAVERSED (no location plate — they take the property plate), so the landing beats (HK-03a, P-02a) can be made as edits of P0 looking up the flight.

- same session, ~12:10–12:20 UTC — **Fix round 4 on P1-LANDING** (board note "it should be the 2nd floor view"): diagnosis — the long prompts restating
  the whole hall anchored the model to P0's own viewpoint. v4 = a **short** edit of P0 (1,937 chars) with an HT22 geography block (camera upstairs, the hall one
  storey below, exactly one straight flight, sides stated), Higgsfield nano_banana_pro (logged NB2, 2 cr). The render is the view from the top of the flight
  looking down to the front door, photo wall left, rail right — but the model also drew a gallery balustrade across the top of the frame and a second
  landing rail on the right (not in P0). On Current as To check; v3 to Old (b7ddb7b6…). Default branch merged (V7.77.1, HT22).

- same session, ~12:25 UTC — user **"drop that"**: the landing plate P1 is dropped (§30G: hall, stairs and landing are TRAVERSED — they take the property
  plate). HK-03a and P-02a become image edits of P0 (the top of the flight, HT17); act map / STEP4_5 / docs updated; P1 card removed from Current, all four
  versions on the Old board. All seven remaining plates are confirmed → **step 6 (the hook) is unlocked.**

- same session, ~12:35–12:50 UTC — **Step 6, the hook: A/B start frames + pinned end frames on the Current board, all To check.** Four §6A short
  prompts (`hooks/build_hooks.py` → `hooks/<BEAT>.prompt.txt`, 1,183–1,199 chars, `preflight.py` kind image PASS on all seven): HK-01a and HK-03a are
  image edits of P0 (HT17, Image 1 = the plate, 9:16 crop on the flight / on the top of the flight), HK-01b (feet CU, no sheet) and HK-02a (C2 from the
  top looking down) carry P0 as a reference. Both renders of each pair on Higgsfield `nano_banana_pro` (logged `nano_banana_2` again, §5 fault noted on
  every card; Kie Pro not used — 963/render). **§27G rule 10 applied:** every stairs-class row is pinned — `actmap.py` now sets `pin_end = yes` on any
  `stairs:` staging (13 rows incl. PR-02a), act map / STEP4_5 / `docs/actmap` on Current + Plan re-synced, the 12 stairs cards carry `pinEnd: yes` +
  `endFrame`. The hook's three stairs beats got their end frames the same turn as their own cards — `HK-01a-END`, `HK-01b-END`, `HK-02a-END` (A = an
  edit of start A, B = of start B; "Use A with start A"). HK-03a (a head turn, staging none) is unpinned. 14 renders = 30 Higgsfield credits measured
  (10,377.65 → 10,347.65; 2.14 each on the cards). Assets `hooks/assets.json`, jobs `hooks/jobs.json`, connector links `hooks/urls.json`.
  What I saw (information only — the picks are the user's): HK-01a A/B both on P0's staircase, N two–three steps up (not the 6th), C2's hand on the newel;
  HK-01b A has a white top edge at the daughter's waist, B is shot through the balusters; HK-02a A has bare oak treads and a hall mat, B a tiled hall floor
  (both off the plate); HK-03a A puts N on the hall floor at the foot of the stairs (wrong end), B has her on the landing behind the balusters with C2 on
  the top step. Video pilot: HK-01a is the build's first stairs clip (§27G rule 10) — it runs alone after the picks, the other stairs clips wait on its Confirm.

- same session, ~13:00–13:20 UTC — user **"we dont need end frame generate new ones"** (after Use A on HK-01a and its END card). **End frames waived:**
  §27G rule 10's pin recorded as `pin_waived` on every stairs row (`actmap.py`: `pin_end: no · waived (user 2026-10-01)`; STEP4_5 / `docs/actmap` on
  Current + Plan re-synced; the 12 stairs cards `pinEnd: no`, `pinWaived`), the three END cards removed from Current and kept on Old with both renders.
  **New pairs** (v3/v4 = A/B) for HK-01b, HK-02a, HK-03a from rewritten prompts (`hooks/<BEAT>.v2.prompt.txt`, preflight PASS: HK-01b names the
  sweatshirt hem at the top edge; HK-02a asks for the runner, a rod on every step and the bare oak floorboards of the plate; HK-03a states the landing is a
  storey above the hall and the mother stands on the landing floor above the top step); v1 pairs to Old. Seen: HK-03a A again puts the mother at the foot of
  the stairs on the hall floor, B has both at the top; HK-02a A/B both on the runner with the oak floor below now. Higgsfield balance moved 82.25 for the
  6 renders (10,347.65 → 10,265.4) — far more than the 2.14/render measured on the first batch; cards carry 2.14, unverified why.
  **HK-01a clip (stairs pilot)** on Kling `kling-video-v3_0` (the lock said omni; v3_0 is the single-image first-frame route per who_am_i — same Kling 3.0),
  5 s, 1080p, `prefer_multi_shots false`, `enable_audio false` (the song is the sound), start = v1 A via its Higgsfield CDN link, §35A prompt 908 chars,
  preflight PASS with `pin_waived` + `pilot: first`; 40 Kling credits (44,563 → 44,523); 1072×1928, 5.04 s, 24 fps; on the card as To check
  (`clips/HK-01a_v1.mp4`, contact sheet `clips/HK-01a_v1.contact.jpg`: she climbs hands-free, the daughter's hand on the rail, camera still).

- same session, ~13:35–13:50 UTC — user **"FIX THOSE"** (board notes: HK-01b "WRONG CHARACTER", HK-02a "INCORRECT PLACEMENTS OF PICTURE FRAMES FIX THE
  LOCATION", HK-03a "WRONG LOCATION"). Default branch merged first (V7.78.1 — HT23 "one scene, one continuous moment"). Diagnosis: all three faults are
  fidelity to the confirmed scene — the characters in a no-sheet feet shot, the photo wall and the landing drawn free-hand from the plate. Fix at the source
  (HT17): each v3 pair is an **image edit of the confirmed HK-01a frame A** (Image 1 = that frame, the user's own pick — right staircase, right two women,
  right photo wall), with the HT23 "Scene so far" line on every prompt (`hooks/<BEAT>.v3.prompt.txt`, 1,182–1,200 chars, preflight PASS, `match: frame`).
  HK-02a's camera therefore bends to the frame's (from the hall floor, the daughter side-on near the top, face in profile) — the act map's "from the landing
  looking down" would have had to invent the wall again. v5/v6 = the new A/B; v3/v4 to Old. `fix_patterns.py` run (27 notes): the repeating note on this
  build is "use the location / connected to P0" (P1 ×3, HK-02a, HK-03a) — already HT17, now applied as edits of the confirmed frame; no new rule.

- same session, ~14:55 UTC — the six v3 Fix renders landed after ~65 min in Higgsfield's queue (the user asked for Kie if Higgsfield faulted; it cleared
  before a reroute was needed). v5/v6 on the Current board as To check, v3/v4 on Old. Seen: every render keeps the confirmed frame's camera, staircase,
  photo wall and both women (the three faults are gone), but the model kept the women low on the flight — HK-01b is a wide, not the feet close-up;
  HK-02a has the daughter at the newel with the mother mid-flight; HK-03a has the mother a few steps up turning back, the daughter at the foot. The
  user's picks decide. Higgsfield balance 10,091.15 (shared account — other users' renders move it between our batches).

- same session, ~15:00–15:15 UTC — user **"USE THE CINEMATIC CAMERA ANGLES CAUSE THIS HOOK IS TOO WEAK"** (after confirming the HK-01a clip, HK-02a A
  and HK-03a B, and a Fix "THEY ARE SO BIG" on HK-01b). The hook re-angled per §30I with the §24K part 7 shot names on the user's explicit call (the
  library is Modes 4–5; applied here as the user's instruction): HK-01a SH-LOW full from the foot through the newel, HK-01b SH-GROUND feet through the
  balusters (feet at true scale — the "so big" note), HK-02a SH-HIGH from the landing straight down the flight, HK-03a SH-OTS over the daughter's shoulder
  onto the mother on the landing with the window behind her. `actmap.py` rows rewritten (angles.py PASS), STEP4_5 / `docs/actmap` re-synced, cards carry
  `shot`. New viewpoints, so not edits: Image 1 = the confirmed HK-01a frame A (scene fidelity) + sheets (+ P0 on HK-02a); `hooks/<BEAT>.v4.prompt.txt`,
  preflight PASS. v4 pairs on Current as To check; the confirmed v1 A (and its clip, status use), v5 A and v6 B stay as versions; HK-01b/02a/03a v5–v6
  files to Old. Seen: HK-01b, HK-02a and HK-03a took the new angles (HK-02a B's daughter drifts off model); HK-01a stayed close to the confirmed frame's
  view in both renders — the frame reference dominated; if the user wants the low full shot, the next round drops the frame ref and uses P0 + sheets.

- same session, ~15:20–15:35 UTC (hourly Fix check) — the user picked the re-angled pairs: **HK-01a v3 (A)**, **HK-01b v7 (A)**, **HK-02a v7 (A)**
  confirmed; **HK-03a** Fix "wrong location" on the OTS pair (the model invented a bright landing room with a window — no plate exists for the landing).
  v5 = the OTS kept but built as an image edit of the user's confirmed v6 (the top of the flight from the hall), viewpoint moved up the flight
  (`hooks/HK-03a.v5.prompt.txt`, PASS); v9/v10 To check, v7/v8 to Old. Seen: both renders keep the P0 staircase; the camera landed at the foot
  behind the daughter, the mother mid-flight turning back. Unused picks (HK-01a v4, HK-01b v8, HK-02a v8) to Old. **Clips** from the three picks on
  Kling `kling-video-v3_0` (§35A, preflight PASS; HK-01a = clip v2 from the new frame, clip v1 kept as a version): HK-01a 5 s / 40 cr, HK-01b 5 s / 40 cr,
  HK-02a 6 s / 48 cr (44,019 before). `fix_patterns.py` re-run (29 notes): the repeated note of this build is still the location one (now 6 beats) —
  HT17; the new "THEY ARE SO BIG" is a one-off (scale against the steps written into every stairs prompt since).

- same session, ~15:35 UTC — the three hook clips landed (Kling `kling-video-v3_0`, 1072×1928, 24 fps): HK-01a clip v2 (5.04 s, from image v3 — both
  climbing away from the low viewpoint, hands free), HK-01b v1 (5.04 s — the pump and trainer climbing through the balusters), HK-02a v1 (6.04 s — the
  daughter climbing toward the high lens, face up). All To check (`clips/`, contact sheets beside). Kling 43,851 after (128 for the three).

- same session, ~15:45 UTC — user **"hk01 a and b should be a different location cause its woman half her age should be outside"**: HK-01a and HK-01b
  moved to the **church front steps (P5)** — the same Sunday (N-D4, church dress + the wide-brim hat per the wardrobe map), two one-off women in their
  thirties on the steps below her (HT05: the stakes in the picture). `actmap.py` rows rewritten (L-CHURCH, open-sky light; angles.py PASS), STEP4_5 /
  `docs/actmap` re-synced. HK-01a = an image edit of P5 (HT17, Image 1 = the plate, Image 2 = N's sheet); HK-01b = feet CU on the steps with P5 as the
  reference (`hooks/<BEAT>.v6.prompt.txt`, PASS). The home-stairs clips on both cards are superseded — kept as versions; new clips follow the new picks.

- same session, ~15:40–15:55 UTC — **HK-01a/b church pairs landed** (v5/v6 on HK-01a, v9/v10 on HK-01b, To check; the home-stairs picks and clips stay
  as versions on the cards — their files are still used by the clip versions, so not moved). Seen: N in the hat climbing past two younger women on the
  P5 steps; the feet CU on the concrete steps with the sandals. **HK-02a clip confirmed** by the user. **HK-03a** Fix "this should be at the second
  floor": v7 = an image edit of the user's confirmed HK-02a v7 (the view down the flight from the landing — the second floor the user confirmed), the
  mother's shoulder in the near foreground (OTS from the landing), the daughter on the top step (`hooks/HK-03a.v7.prompt.txt`, PASS; actmap row:
  high · ots · through, angles.py PASS). v11/v12 To check, v9/v10 to Old. Higgsfield 9,668.15 after (shared account).

## Open (Flags in BUILD_SHEET.md)
F1 sung claims to confirm · F2 full Mode 2 (locked) vs hybrid · F3 narrator never sings to camera (default) vs two bookends · F4 "Stryde." · F10 Mode 2 sheet amendment / true Pro route on Kie · F12 BPM · F13 clipped master.

## Next
**Waiting on:** picks on HK-01a (church, v5/v6), HK-01b (church, v9/v10) and HK-03a (second floor, v11/v12); HK-02a image + clip confirmed. Then the HK-01a/01b/03a clips; then the body acts. Then their clips (no end frames — waived; §35A ≤ 1,000 chars, preflight PASS); then the body acts in order; CapCut block with lyric captions and the outro end card.

(Earlier plan, done:) steps 4–5 (property sheet + 16:9 Pixar plates on nano_banana_pro: house stairs/landing/kitchen, reception, store checkout, church steps, street; act map on the song's clock — E6 lengths from `work/lyrics.timed.json`, cuts on 3–4 beats, `angles.py` PASS; wardrobe map). No voice stage. Then hook (0–15.5 s) at step 6, body acts at step 7, CapCut block with lyric captions.
- same session, ~15:50–16:05 UTC — **"i want new ones cause these hooks looks the same as the others i want more powerfull hooks" → the plaza hook.**
  A new hook concept, not another fix of the old one (HT05: the hook sells out in the world, the stakes in the picture): one monumental public
  staircase — the great outdoor entrance steps of a downtown arena plaza on a Sunday afternoon (new location L-PLAZA, plate **P8-PLAZA**, 16:9,
  `plates/build_plates.py --p8`, Higgsfield nano_banana_pro (logged nano_banana_2), on the Current board as To check — generated together with the
  hooks so the round didn't wait on a plate pick; it is the reference of all four hook frames). The younger crowd stopped on the steps is the stakes
  N climbs past. Act map, `STEP4_5.md` (locations table: L-PLAZA · PLATED · P8-PLAZA; light row), `docs/actmap` (Current v9 / Plan v9) and
  `docs/locations` (v3) re-planned on L-PLAZA; angles.py PASS (61 rows); stairs pin stays waived. Four §6A v8 prompts (`hooks/build_hooks.py --v8`,
  `hooks/<BEAT>.v8.prompt.txt`, all PASS, 1,148–1,198 chars): HK-01a an image edit of P8 (`match: plate`, HT17; Image 1 = P8, Image 2 = N sheet),
  SH-LOW FULL from the plaza, N on the 15th of 30 steps, a dozen younger people stalled below her; HK-01b SH-GROUND CU profile at tread height, her
  pumps past the stopped trainers (ref P8); HK-02a SH-HIGH MEDIUM from the top landing, the daughter ten steps below (refs C2, P8); HK-03a SH-OTS
  over the mother's shoulder from the top, the daughter stopped at the rail (refs N, C2, P8). 8 renders, one per call (jobs in `hooks/jobs.json`
  `<BEAT>@v8A/B`), ~2.14 cr each; Higgsfield balance 9,642.15 after. Board: **HK-01a v7/v8, HK-01b v11/v12, HK-02a v9/v10, HK-03a v13/v14** To check
  (`hooks/v8_cards.py`); the church pairs (HK-01a v5/v6, HK-01b v9/v10) and the second-floor pair (HK-03a v11/v12) copied server-side to Old
  (Old docs HK-01a v3, HK-01b v5, HK-03a v6), marked `archived` + `archiveAsset` on Current and deleted from Current. Kept on Current: HK-01a v1/v3
  and HK-02a v7 (their clips were made from them), HK-01b v7. The home-stairs clips (HK-01a v1/v2, HK-01b v1, HK-02a v1) stay as versions,
  superseded — new clips follow the plaza picks. Seen in the renders (no judgement, the user checks): all eight sit on the P8 flight (three lanes,
  two steel rails, glass doors, towers); HK-01a A/B each hold N in the middle lane with eight younger people on the lower steps (two bent hands on
  knees, one on the rail); HK-01b both show the black pump mid-step beside two pairs of white trainers; HK-02a both look down the flight from the
  landing at the daughter, hand on the rail, the plaza crowd behind; HK-03a both frame the daughter from over the mother's hat and shoulder with the
  towers behind. Higgsfield cleared the queue; Kie not needed (standing fallback stays).

**Waiting on:** the user's picks on the four plaza pairs and the P8-PLAZA plate (A/B on each card; Fix with a note if neither). Then the hook clips
(§35A, no end frames — waived); then the body acts in order; CapCut block with lyric captions and the outro end card.
