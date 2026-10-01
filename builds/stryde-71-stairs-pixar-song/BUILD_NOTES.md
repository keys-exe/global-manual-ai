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

- same session, ~16:08–16:20 UTC — user **"the hk1 should show woman half her age behind her and the hk02-03 should be different location"** (on the plaza round).
  HK-01a/b keep the plaza (P8-PLAZA): the crowd is replaced by **one woman half her age** (thirty-five, grey sweatshirt, black leggings, white
  trainers) stopped four steps behind her, bent with both hands on her knees; HK-01b her pump mid-stride past that woman's stopped trainers.
  HK-02a/03a move to a **different location — the church steps (L-CHURCH, confirmed plate P5-CHURCH)**: the line is "Last Sunday, my daughter
  walked behind me the whole way up", so the Sunday church is the story's own place and it is not the plaza; both are image edits of P5 seen from
  its top step (§6A rule 3, HT17): HK-02a SH-HIGH down the flight at the daughter on the 4th of 8 steps, HK-03a SH-OTS over the mother's shoulder,
  the daughter one step down. Four §6A v9 prompts (`hooks/build_hooks.py --v9`, `hooks/<BEAT>.v9.prompt.txt`, all PASS, 1,168–1,185 chars; the
  first HK-02a/03a drafts failed preflight — "Keep this church…" is not the rule-3 opener and 1,225 chars — rewritten to "Keep this photo exactly
  as it is — the church…" and trimmed). Act map (`work/actmap.py`: HK-01a/b subject + framing, HK-02a/03a L-CHURCH), `STEP4_5.md` (locations:
  L-CHURCH now carries HK-02a–HK-03a, L-PLAZA HK-01a–HK-01b), `docs/actmap` (Current/Plan v10), `docs/locations` (v4); angles.py PASS. 8 renders,
  one per call (`hooks/jobs.json` `<BEAT>@v9A/B`), Higgsfield nano_banana_pro (logged nano_banana_2); balance 9,471.15 after (shared account).
  Board: **HK-01a v9/v10, HK-01b v13/v14, HK-02a v11/v12, HK-03a v15/v16** To check (`hooks/v9_cards.py`, `hooks/patch/v9.ids.json`); the v8
  plaza pairs copied to Old (Old docs HK-01a v4, HK-01b v6, HK-02a v5, HK-03a v7), marked `archived` + `archiveAsset`, deleted from Current.
  Seen (no judgement — the user checks): HK-01a A/B both on the P8 flight, N mid-flight, one younger woman in grey bent hands-on-knees below her
  (A four steps below in the same lane, B further down and one lane left); HK-01b A/B the pump mid-stride and one pair of stopped trainers with a
  hand on the knee. **HK-02a A came back with brick steps and brick treads, not P5's concrete flight** (B keeps the concrete steps, hedges, cars).
  **HK-03a A and B both put the mother in a yellow tee and jeans, not the green church dress and hat** (the N sheet's wardrobe won over the prompt);
  B also looks at the church from across the street, not down its own steps. The daughter at church is in the wardrobe lock's sweatshirt and
  shorts (N-D4 wardrobe map) — a Fix note can change it. Kie not needed; the fallback stands.

- same session, 16:20 UTC hourly Fix check + user message, ~16:20–16:35 UTC — **HK-02a Fix "this should show walking behind her"** → v10: the daughter walking up the
  church steps two steps behind her mother, both in frame from the sidewalk at the foot of the steps (SH-LOW FULL, an image edit of the confirmed P5,
  `hooks/HK-02a.v10.prompt.txt`, PASS 1,189 chars after a trim from 1,309; actmap row HK-02a re-angled low/three-quarter-back). **HK-02a v13/v14** To check;
  v11/v12 to Old (Old doc v6). Seen: both renders — N ahead in the green dress and hat on the 6th step, the daughter two steps behind with her hand on
  the black rail, the church front and doors above; on model. **P8-PLAZA confirmed by the user** (status use).
  Then the user: **"I'm seventy-one, and I take the stairs faster than women half my age — should be 1 broll here showing her walking faster going up
  the stairs and at her back woman walking behind and she likes walking faster and left them"** → **HK-01 is one B-roll for lines 1–2 (0.00 → 8.01 s)**:
  HK-01a re-planned (`work/actmap.py`: lines (1, 2), `mx=10`, N + two women half her age, "three quick steps up, N pulling away; the women behind
  climb slowly and fall further back"), **HK-01b dropped** — its Current doc deleted, its v13/v14 files copied to Old and every version kept on the Old
  HK-01b doc (`dropped: true`); act map 60 rows, 108/108 lines, angles.py PASS; `STEP4_5.md`, `docs/actmap` (v12), `docs/locations` (v5) synced.
  v11 prompt (`hooks/HK-01a.v11.prompt.txt`, PASS 1,171 chars, edit of the confirmed P8): N mid-stride on the 15th step, chin up, a small pleased smile
  in part profile; two women of thirty-five in grey and navy sweatshirts walking up slowly on the 11th and 10th steps behind her, one hand on the rail,
  looking up at her back. **HK-01a v11/v12** To check (`hooks/v11_cards.py`); v9/v10 to Old (Old doc v5). Seen: A — N ahead smiling in part profile,
  the two women three and four steps behind, one hand on the left rail; B — the same, N a step higher and turned a little more to the lens. The clip
  will be one 8 s Kling shot from the picked frame (no end frame — waived). Higgsfield balance 9,309.65.
  `fix_patterns.py` re-run (66 notes): the note that repeated today is the line's relationship — "woman half her age behind her", "walking behind
  her", "at her back woman walking behind" → **House Taste HT24 (V7.79.2)**: every person a line names as ahead, behind, beside or watching is in the
  one frame in that relation, from the side or behind, never a POV of one of them; a comparing hook line is one B-roll with all of them in it
  (standards §34A + changelog, skill summary synced).

- same session, ~16:30–16:45 UTC — user **"hk01 she is facing the wrong way"** (the v11 pair had N side-on across the steps). v12: her back to the
  lens, facing up the flight to the doors, climbing away, the edge of a smile past the hat brim; the two women behind her with their backs to the
  lens too (`hooks/HK-01a.v12.prompt.txt`, PASS 1,177 chars after two trims; `face: True` — preflight refuses a face block on a no-face call; the
  actmap framing updated). **HK-01a v13/v14** To check (`hooks/v12_cards.py`); v11/v12 to Old (Old doc v6). Seen: A — N from behind on the 15th step,
  head turned a little so her cheek and smile show, the two women two and four steps below her, one hand on the right rail; B — the same from a
  touch lower, N glancing back over her left shoulder, the women closer together on the left lane. Higgsfield balance 9,190.15 (shared account).
  Merged the default branch first (V7.80.0 arrived from another session; this build's rules unchanged).

- same session, ~16:50–17:05 UTC — user **"fix those and generate the confirmed"**. Board state read: **HK-01a v13 (A) confirmed**, **HK-02a v13 (A) confirmed**
  (their B renders v14 moved to Old — Old docs v7/v7, files deleted from Current); **HK-03a Fix "this should be the same as the hk02 location but should
  be them talking to each other"**. No `restore` requests on the Old board.
  **HK-03a v13** (`hooks/HK-03a.v13.prompt.txt`, PASS 1,194 chars): an image edit of the confirmed HK-02a v13 A (the church steps from the sidewalk,
  HT17) — N stopped on the 6th step and turned back to her daughter, hand on hip, a small smile; the daughter two steps below, hand on the black rail,
  face up, mouth open mid-word (HT24, both in frame); actmap row re-angled low/three-quarter MEDIUM from the sidewalk, `docs/actmap` v14.
  **HK-03a v17/v18** To check (`hooks/v13_cards.py`); v15/v16 to Old (Old doc v8). Seen: both renders — the same church front and steps, N turned
  back on the step looking down at the daughter, the daughter looking up with her mouth open; A has N's hand on her hip, B the hand lower.
  **Clips (§35A, Kling kling-video-v3_0, 1080p, silent, one render each, no end frame — waived):** HK-01a clip **v3** from v13 A, 8 s / 64 cr
  (`clips/HK-01a.v3.call.json`, PASS, the card's motion plan verbatim; `clips/HK-01a_v3.mp4`, 7.0 MB), HK-02a clip **v2** from v13 A, 5 s / 40 cr
  (`clips/HK-02a.v2.call.json`, PASS; `clips/HK-02a_v2.mp4`, 8.1 MB). Both To check. Seen on the contact sheets: HK-02a — N climbs two steps toward
  the doors hands free, the daughter follows two behind, hand on the rail, as planned. **HK-01a — N climbs the whole flight fast, reaches the top
  and goes in through a door that opens, while the two women stay low on the steps; faster and further than the plan's three steps** (the user
  asked for "walking faster"; their call — a Fix note can slow it). The earlier home-stairs clips stay on the cards as versions. Kling balance
  42,739 after; Higgsfield 9,019.15.

- same session, ~17:00–17:10 UTC — user "fix those": board read — **HK-01a clip v3 and HK-02a clip v2 confirmed (status use)**; **HK-03a Fix "thry should
  be at the door already for this scene"**. v14 (`hooks/HK-03a.v14.prompt.txt`, PASS 1,190 chars): the same edit of the confirmed HK-02a v13 A, the
  mother on the top landing in front of the white doors turned back, the daughter on the top step with her hand on the top of the rail (actmap row
  updated, `docs/actmap` v15). **HK-03a v19/v20** To check (`hooks/v14_cards.py`); v17/v18 to Old (Old doc v9). Seen (the user checks): **both renders
  kept the women where the source frame had them — N on the 5th–6th step, the daughter at the foot of the flight; neither is at the doors.** The
  frame edit held the positions; if the user sends it back, the next pair is built on the empty P5 plate (the women placed at the top) rather than
  on the HK-02a frame. Default branch merged (V7.81.0; its new `angles.py` anatomy-beat check, §12A-1, fails this build's locked act map — a system
  update, not applied to this running build). Higgsfield balance 8,888.15.

- same session, ~17:15–17:25 UTC — user "fix those" + board note on the v14 pair: **"i want a new angle they should be inside like at the door step"**.
  v15 (`hooks/HK-03a.v15.prompt.txt`, PASS 1,197 chars after three trims): a new setup on the user's call — from inside the church's open front doorway
  looking out, the mother on the threshold turned back to her daughter on the doorstep, hand on the rail end, mouth open mid-word, the sunlit sidewalk
  beyond (refs P5 plate, N and C2 sheets; no plate match — nothing shows the inside; actmap row: eye · three-quarter · through · MEDIUM, `docs/actmap`
  v16). **HK-03a v21/v22** To check (`hooks/v15_cards.py`); v19/v20 to Old (Old doc v10). Seen: both from inside the doorway, the two at the doorstep
  turned to each other on model; A a dim vestibule with the white door leaves either side, B brighter with dark wood door frames and the street and
  houses behind. Higgsfield balance 8,840.15.

- 17:20 UTC hourly Fix check — **HK-03a Fix on the v15 pair: "make it a close up shot"**. v16 (`hooks/HK-03a.v16.prompt.txt`, PASS 1,125 chars; the first
  draft failed §6A rule 4 "every visible hand placed" — hands stated out of frame): the same doorway setup in close, an image edit of v21 A, both
  faces filling the frame, the mother in three-quarter profile turned back, the daughter beyond her mouth open mid-word (actmap row: eye · three-quarter
  · through · CU, shallow; `docs/actmap` v17). **HK-03a v23/v24** To check (`hooks/v16_cards.py`); v21/v22 to Old (Old doc v11). Seen: A — the daughter
  left in the frame facing the mother at right, the mother's profile under the hat brim, the white door leaf and the sunlit street behind; B — the
  mother at left in profile, the daughter at right facing her, both on model. No restore requests on Old. `fix_patterns.py` re-run (73 notes): the
  HK-03a run of notes is one beat being staged (talking → at the door → inside → close up), not a repeat across beats — no new rule. Default branch
  merged (V7.83.0; this build's locks unchanged). Higgsfield balance 8,676.65.

- same session, ~17:30–17:50 UTC — user **"confirm proceed"** ×2: **HK-03a v24 (B) confirmed** (v23 to Old, Old doc v12); **HK-03a clip v1** from it
  (`clips/HK-03a.v1.call.json`, PASS; Kling 4 s / 32 cr, `clips/HK-03a_v1.mp4` 3.5 MB) on the board To check — seen: the daughter's head tilts and
  her smile opens, the mother's smile widens, the frame holds. **Act 1 (the problem, N-D1) started:** eight §6A beat prompts, every one an image edit
  of its confirmed plate (P0 stairs, P2 kitchen v2, P7 clinic; N sheet; the N-D1 wardrobe) in `body/build_act1.py` → `body/<BEAT>.v<n>.prompt.txt`.
  **My error, caught before the board:** the v1 pair (16 renders, ~34 cr) came back as photographs — the body prompts had dropped the Mode 2 render
  line that every hook prompt carried. Fixed at the source: `preflight.py` now fails any Mode 2/3/5 image call without the mode's render line
  (`MODE_LINE`; proven on the v1 call = FAIL, v2 = PASS), **LESSONS L10** (numbered L09 before the merge). The v1 pair went to the Old board as a kept version (Old docs for the eight
  beats; P-03b v1 A failed on Higgsfield, no file) and was never shown as To check. v2 (the render line restored, all PASS 991–1,187 chars):
  **P-01a v3/v4, P-01b v3/v4, P-02a v3/v4, P-03a v3/v4, P-03b v3/v4, P-04a v3/v4, P-04b v3/v4, P-05a v3/v4** To check (`body/act_cards.py`,
  `body/patch/v2.ids.json`). Seen (the user checks): the Pixar look is back on all; P-01a A has her coming down facing forward, not backwards as the
  row says; P-04b A shows the therapist's face (the prompt asked shoulders down); P-05a B the heap pushed away as planned. Higgsfield balance
  8,409.15; Kling 42,707. Note: `assemble.py --sheet` placement (V7.80.0) is newer than this build's step-5 lock — the act map is already timed on
  the song's words by `work/actmap.py` (108/108 lines); not re-run here (system updates never touch a running build).

- ~18:00 UTC — user **"fixed those and proceed"** (board: HK-03a clip v1 confirmed; P-03a / P-04a / P-04b / P-05a picked A (v3); Fix notes on
  P-01a "should be looking up the stairs and stepping backwardd", P-01b "this should be the backwards also", P-02a "this should be her at the top
  of the stairs looking down", P-03b "the brace here should be same as the p03a"). **Act map re-angled for the three stairs beats** (`work/actmap.py`,
  60 rows, 108/108; `STEP4_5.md`, `docs/actmap` v18 on Current and Plan): P-01a low · behind from the foot of the stairs (her back to the lens,
  face up to the landing, one foot reaching back down), P-01b feet backwards (toes up the stairs, heel lowering to the step below), P-02a low ·
  front from the hall floor (the whole flight, her on the top step looking down it). **v3 prompts** (`body/build_act1.py 3`, PASS 1,163–1,197
  chars; P-03b attaches the confirmed P-03a frame as Image 2 "the brace, copied exactly"): **P-01a v5/v6, P-01b v5/v6, P-02a v5/v6, P-03b v5/v6**
  To check (`body/patch/v3.ids.json`, `act_cards.py` now takes per-beat `notes` and a `P03A` frame ref); their v3/v4 pairs and the four unused B
  renders (v4 of P-03a/P-04a/P-04b/P-05a) copied to Old (Old docs v2), archived on Current, the Current files deleted. Seen (the user checks):
  P-01a both from the foot of the flight, her back to the lens, face up to the landing, hands on the rail — a still can't show the direction of
  the step, the clip will; P-01b A/B the heel reaching down, toes up the stairs; P-02a A three-quarter / B frontal, on the top step looking down the
  full flight; P-03b A/B the P-03a brace (round hinges, wide straps) around the ankle. **Act 1 clips** from the confirmed A frames
  (`clips/build_act1_clips.py`, §35A PASS 564–684 chars; Kling 3.0 1080p, no audio): **P-03a v1** 5 s / 40 cr, **P-04a v1** 4 s / 32 cr, **P-04b v1**
  5 s / 40 cr, **P-05a v1** 6 s / 48 cr — To check (`clips/<BEAT>.v1.card.json`). Seen: P-03a one pull and the brace sags back; P-04a the hands
  push the pile apart but the framing drifts and the top of her head enters at the bottom edge; P-04b the knee bends further and holds; P-05a the
  push lands, then the heap thins out and vanishes by the end and her mouth moves as if talking (told the user; a Fix is theirs to call). Higgsfield
  balance 8,257.15; Kling 42,007 (build doc v20).

- 18:20 UTC hourly Fix check + user message **"p03a and b should be connected so same braces"**. Board: P-01b picked v5 A, P-02a picked v6 B;
  P-04a / P-04b clips confirmed; P-03a clip still To check; **P-01a Fix "she should be at the top of the middle of the stairs she should never be at
  the bottom"**; **P-05a (video) Fix "make this into 3 brolls"**. Done: **P-01a v7/v8** (`body/P-01a.v4.prompt.txt`, PASS 1,200 chars — two steps
  below the landing, the crop on the upper half of the flight; act-map framing updated) — seen: both renders still put her on the lower half of the
  flight (the model kept her mid-flight; told the user; the next Fix will crop the plate to the top of the flight first). **P-03b v7/v8**
  (`P-03b.v4.prompt.txt`, PASS; `match: "frame"`, a direct image edit of the confirmed P-03a frame, job 549092c2) — seen: A seated, the P-03a brace
  around the ankle, hand on the knee; B keeps the P-03a standing pose with the brace at the ankle; the earlier v5/v6 pair to Old. **P-05 split**
  (`work/actmap.py`: P-05a lines 16–16 · P-05b 17–17 · P-05c 18–18, 62 rows, 108/108; `STEP4_5.md`, `docs/actmap` v19 on Current and Plan): on the
  song's clock P-05a gets 1.6 s, P-05b 2.4 s, P-05c 0.8 s (the T-01a cut snaps to the grid at 42.97 — FLASH on P-05a and P-05c; the user asked for
  three, told them). New cards **P-05b v1/v2** (the heap at the far edge, `P-05b.v1.prompt.txt`) and **P-05c v1/v2** (her face sat back,
  `P-05c.v1.prompt.txt`) To check; **P-05a clip v2** (3 s / 24 cr, §22X: every object stays to the last frame, mouth closed — seen: the push lands,
  the heap stays, she sits back) To check, v1 kept as a version. **P-01b clip v1** (4 s / 32 cr — seen: the heel settles on the step below, the other
  foot follows, feet stay turned up the stairs) and **P-02a clip v1** (6 s / 48 cr — seen: she looks down the flight and away; her mouth opens into a
  smile mid-clip as if speaking; told the user) To check; the unused P-01b v6 and P-02a v5 to Old (Old docs v3). `act_cards.py` now sets new beats
  (`set`, base fields) and strips `__delete__` on a set (first batch was refused for it). `fix_patterns.py` re-run: "connected" repeats across P1-LANDING
  and P-03a/b → **FP14** in `products/stryde/fix_patterns.md` (the second beat on one prop is an edit of the first's confirmed frame). No restore
  requests on Old. Balances as printed: Higgsfield 8,167.15; Kling 41,743 (build doc v21).

- ~18:50 UTC — user **"i want new ones on the brolls. i dont like these, you should never talk the lyrics/script in broll"**; board: **P-01a Fix
  "she should be starting from the top to show case the moving backwards"**, **P-01b clip Fix "this hsould be stepping backwards"**, P-01b picked v5 A,
  P-02a picked v6 B. **Rule fixed at the source (V7.83.3):** §35A rule 6 + House Taste HT25 — nobody in a B-roll mouths the line; every beat video
  prompt says `mouth closed, she never speaks or sings` / `nobody speaks`; `preflight.py` fails a B-roll call without it (`NOSPEAK`; proven on the
  old P-03a call = FAIL); skill summary, CLAUDE.md version, **LESSONS L15**. **New clips** (`clips/build_act1_clips.py`, PASS): **P-01b v2** 4 s / 32 cr
  (seen: the first heel settles on the step below, but the second foot swings up and forward — still reads as climbing; a third generation waits for
  the user; the fix I'd propose is a pinned end frame with the feet one step lower, §27G rule 10 — the user waived pins on this build, so it is their
  call), **P-02a v2** 6 s / 48 cr (seen: looks down the flight and away, mouth closed throughout), **P-05a v3** 3 s / 24 cr (third generation on the
  user's own ask; seen: the push, she sits back, mouth closed, a few bottles stay to the end) — all To check; the replaced clips (P-01b v1, P-02a v1,
  P-05a v1/v2) copied to Old and archived. P-03a clip v1 (knee only, no mouth) left To check — not regenerated. **P-01a:** v7/v8 to Old; a v5 prompt on a
  crop of the plate (`plates/P0-PROP-N_top.png`, Higgsfield media 692d9e49) **still put her at the newel** (the crop kept the bottom of the flight) —
  **v9/v10 never shown**, straight to Old as kept versions (4.28 cr, agent error → **LESSONS L16**: a render that contradicts the user's note is never
  put up; fix the source first). v6 prompt (`body/P-01a.v6.prompt.txt`, PASS 1,147 chars): a direct image edit of the confirmed **P-02a v6 B** frame (her
  on the top step, the whole flight from the hall floor), stood up with her back to the lens and a foot reaching down (FP14) → **P-01a v11/v12** To
  check — seen: both at the head of the stairs from behind, hands on the rail, one slipper reaching down the step. `docs/actmap` v20 on Current and
  Plan (P-01a framing: starting from the top). Balances as printed: Higgsfield 8,085.15; Kling 41,559 (build doc v22).

- ~19:00 UTC — board: **P-01a picked v12 (B)** → **P-01a clip v1** 5 s / 40 cr To check (seen: from the top step she lowers one foot to the step
  below and the other follows, back to the lens, nobody speaks); v11 to Old. User **"THE WHOLE P03 I NEED NEW ONES THERE / FIX THEM ALL"** + board
  P-03a "NEW IMAGE", P-03b "USE THE P03A AS REFERENCE FOR THE BRACE": both beats re-staged (`work/actmap.py`: P-03a low · profile at knee height, seated
  on the kitchen chair; P-03b the same side at floor level, an edit of the P-03a frame; `STEP4_5.md`, `docs/actmap` v21): **P-03a v5/v6**
  (`body/P-03a.v7.prompt.txt`, PASS, edit of the P2 plate — seen: A seated with the right leg out, the hinged brace at the knee, hand on its top
  strap; B seated square to the table, the brace below the knee) and **P-03b v9/v10** (`P-03b.v7.prompt.txt`, PASS, a direct edit of the new P-03a A —
  seen: both the same seat and side at floor level, the brace bunched at the ankle, evening light; **if the user picks P-03a B, P-03b is made again
  from B**) To check. P-03a's old image (v3) and clip (v1) and P-03b's v7/v8 copied to Old (Old docs v3/v4), deleted from Current. Balances as printed:
  Higgsfield 8,054.15; Kling 41,519 (build doc v23).

- 19:20 UTC hourly Fix check — seven Fixes on the board. **P-01a clip** "SHOULD NOT BE STEPPING SO FAR DOWN IT SHOULD BE 1 STEP AT A TIME" → **clip v2**
  5 s / 40 cr (one slow step only, then she holds; seen: one foot lowers to the step below, the other joins, she holds), v1 to Old. **P-01b** "USE THE
  P01A AS REFERENCE HERE" → **v7/v8**, a direct edit of the confirmed P-01a v12 B frame closed in on her feet at the top of the flight (act map: low ·
  behind; seen: both from below on the top steps, slippers toes-up, the heel reaching down); the v5 image and clip v2 to Old. **P-02a** "USE A DIFFERENT
  CAMERA ANGLES" → **v7/v8** from the landing behind her shoulder, high, looking down the whole flight (act map: high · over-the-shoulder, no face;
  seen: A sitting on the top step, head down to the hall; B standing at the top with a hand on the newel — not sitting); the v6 image and clip v2 to
  Old. **P-03a** "MAKE THE BRACE A BIT MORE SHORT MUCH EASIER TO SHOW" → **v7/v8**, a short hinged brace a hand's length above and below the knee (seen:
  both seated from the side, the short brace at the knee, hand on its strap); v5/v6 to Old. **P-03b** "USE THE P03A AS REFERENCE AGAIN" → **v11/v12**,
  a direct edit of the new P-03a A (seen: the same seat at floor level, the short brace around the ankle, evening; if P-03a B is picked, P-03b is made
  again from B); v9/v10 to Old. **P-05b** "I NEED A DIFFERENT ONES HERE" → **v3/v4**, a different picture: at floor level by her chair, a dropped knee
  sleeve and a pill bottle beside her slipper (seen: both as asked, A with the bottle rolled, B the bottle open); v1/v2 to Old. **P-05c** same note →
  **v3/v4**, from behind her shoulder, high, head bowed over the heap on the table, no face (seen: A from behind at the table, the heap in front; B a
  wider three-quarter from behind, a sliver of profile); v1/v2 to Old. Act map rows re-staged (`work/actmap.py`, `STEP4_5.md`, `docs/actmap` v22 on
  Current and Plan). All replaced files copied to Old (Old docs: P-01a v7, P-01b v5, P-02a v5, P-03a v4, P-03b v5, P-05b/P-05c new) and deleted from
  Current. `fix_patterns.py`: the "use X as reference" notes (P1↔P0, P-03a↔P-03b, P-01a↔P-01b) are FP14 again — no new rule. No restore requests on
  Old. Balances as printed: Higgsfield 7,990.15; Kling 41,279 (build doc v24).

- ~19:40 UTC — user **"FIX THOSE"** (board: P-01a clip "SHOULD BE GOING BACK WARDS NOT UP", P-01b "SHE IS TOO BIG HERE", P-02a "WRONG LOCATION",
  P-05b / P-05c "WRONG PERSON ALSO SHOULD USE DIFFERENT TYPE OF BROLL"; P-03a picked v7 A, P-03b picked v11 A). **P-03a clip v2** 5 s / 40 cr (the hand
  pulls the short brace's strap, it sags back) and **P-03b clip v1** 4 s / 32 cr (one small foot shift) To check; the unused B renders to Old. **P-01b
  v9/v10** (`body/P-01b.v9.prompt.txt`, the same edit of the P-01a frame, a wider crop — seen: her legs small at the top, eight steps below). **P-02a
  v9/v10** (an edit of the confirmed P-02a v6 B frame, her own flight — the over-the-shoulder try had invented a landing; asked closer from mid-flight,
  **the render kept the wide framing** — told the user; a crop of the frame is the next step if they want it closer). **P-05b v5/v6** (a different kind
  of B-roll: the kitchen drawer stuffed with sleeves, a brace and pills, her hand pushing it shut — seen: A a brown hand, **B a pale hand, told the
  user**). **P-05c v5/v6** (N at the kitchen window in profile, her cast sheet attached — seen: both on model, looking out). Act map re-staged for the
  four (`docs/actmap` v23). **P-01a clip:** the third generation from the start frame alone (direction named three ways: down toward the lens, larger
  in the frame, farther from the landing; 40 cr) **still read as climbing — never shown (L16), kept on Old as v3**. The fix moves to **§27G rule 10, a
  pinned end frame**: card **P-01a-END** (v1/v2, an edit of the confirmed P-01a frame with her one step lower — seen: A both feet on the second step,
  B one foot lifting down) To check; once the user picks it, the P-01a clip runs first-and-last frame. Replaced files to Old (Old docs P-01a v9,
  P-01b v6, P-02a v6, P-03a v5, P-03b v6, P-05b v2, P-05c v2), deleted from Current. Balances as printed: Higgsfield 7,897.15; Kling 41,127 (build doc v26).

**Waiting on:** picks or Fix notes on P-01b v9/v10, P-02a v9/v10, P-05b v5/v6, P-05c v5/v6, **P-01a-END v1/v2** (the end frame); Confirm or Fix on the
clips P-03a v2, P-03b v1, P-05a v3. Then the P-01a pinned clip and the clips from the picks; then Act 2 (the wedding).

## 2026-10-01 — "FIC THESE" round (20:00–20:15 UTC)

- **P-01b** "I WANT A CLOSE SHOT OF THE LEGS HERE GOING DOWN BACLWRDS" → v11/v12 (A/B): a close side shot at step height on her legs alone (edit of the stair plate P0), the lower slipper on its step, the upper heel reaching back and down. To check. v9/v10 to Old.
- **P-05b** "WRONG DRAWER AND LOCATION" → v7/v8 (A/B): the middle drawer of the row right of the stove in her own kitchen (edit of the kitchen plate P2), pulled open and stuffed, her brown hand on its edge. To check. v5/v6 to Old.
- **P-02a** picked v9 A → clip v3 (Kling 3.0, 6 s, 48 cr): seated on the top step she looks down the flight, holds, turns her face aside, mouth closed. To check. Unused v10 to Old.
- **P-05c** picked v5 A → clip v1 (3 s, 24 cr): at the window she looks out, then her eyes drop to the sink. To check. Unused v6 to Old.
- **P-01a** — user: "I DONT NEED END FRAME IN P01" → the `P-01a-END` card dropped (its v1 A/B pair kept on **Old versions 2**, 4.28 cr), `pinEnd` removed. Clip **v4** from the confirmed start frame alone (gen 4 on the user's word; §22X: v1–v3 all read her stance on the top step, facing the landing, as a climb → the motion renamed as *backing away from the landing*: she sinks lower in the frame, her head drops below the window, the landing stays empty; 4 s, 32 cr). What I see: she backs down the flight toward the lens one step at a time, about four steps — the direction is finally right. To check; "Use only up to here" trims it to one step if wanted.
- **Old board full (1 GB).** The asset copy of the END pair failed `quota_or_state`; a new **Old 2** overflow board was published from the template (`BOARD_ROLE "old"`, title "STRYDE · 71 Stairs Pixar Song Old Versions 2") — https://claude.ai/artifact/SpS5N8dHyFM449QEpvgX4j — with its `builds` doc (`boards.old2`) and the `P-01a-END` Old doc. From now on replaced / unchosen renders go to Old 2; `boards.old2` + `boardsNote` written on all four build docs. `body/old_ids.json` marks Old 2 ids with an `old2:` prefix.
- Balances: Higgsfield 7814.15 · Kling 40793.
- Standards on the default branch moved to V7.85.0 (the Visual Pitch) — not applied to this running build (step-2 lock).

Waiting on: picks or Fix notes on P-01b v11/v12, P-05b v7/v8; Confirm or Fix on the clips P-01a v4, P-02a v3, P-05c v1, P-03a v2, P-03b v1.

## 2026-10-01 — P-01a clip v5 (user: "P01 SHOULD BE WALKING BACKRWARDS SLOWLY ONE STEP AT A TIME NOT SKIPPING STEPS OF THE STAIRS", 20:12 UTC)

- The user had pressed Confirm on v4 on the board, then sent this Fix in chat — the chat Fix is the later word, so v4 was replaced: copied to **Old 2** (`c74a4cf5…`, its Old doc there), deleted from Current.
- **Clip v5** (Kling 3.0, 5 s, 40 cr) from the same confirmed start frame: the "backs away from the landing" framing kept (it was what finally made v4 go down), the pace named outright — slowly, one step at a time, each heel to the step directly below, both feet on it before the next, two steps in the whole clip, never a step skipped. What I see: she backs down toward the lens slowly, one step at a time onto consecutive steps, face to the landing. To check.
- **Lesson L18 / V7.85.1** (PR #340, merged): the v1 note "1 STEP AT A TIME" was treated as settled once v4 went the right way — every Fix note on a shot now stays in force for every later generation: §22X, `preflight.py` fails a generation 3+ call without `fix_notes_all` (the clip builder writes it: `FIXALL`), LESSONS L18.
- Balances: Higgsfield 7814.15 · Kling 40633.

Waiting on: Confirm or Fix on the clip P-01a v5; picks or Fix notes on P-01b v11/v12, P-05b v7/v8; Confirm or Fix on the clips P-02a v3, P-05c v1, P-03a v2, P-03b v1.

## 2026-10-01 — 20:21 UTC hourly Fix check

- **P-03a** image Fix "THE BRACE SHOULD BE IN SHOULD ONE KNEE" (the v7 A frame's lower cuff sat behind the near shin and read as a brace across both legs) → v9/v10 (A/B): an edit of that confirmed frame changing only the brace — one short hinged brace on her right leg alone, both cuffs on that leg, the left leg bare and apart. To check. v7 A → **Old 2** (`185b07ce…`); the clip v2 made from it → Old 2 (`4fe78942…`), archived; the card waits for the new pick (status `ready`). **P-03b was made as an edit of the old P-03a frame (FP14)** — it is confirmed and untouched; if the user wants it to match the new P-03a brace, that is their call.
- **P-05c** clip Fix "NO TALKING ABOUT THE MUSIC" (the face strip at 6 fps shows her mouth opening as if singing along, although the prompt carried the mouth-closed clause at its end) → clip v2 (3 s, 24 cr): the lips clause first and strongest — lips sealed, jaw still, a silent clip, only the eyes move. Checked at 6 fps: lips closed first frame to last. To check. v1 → Old 2 (`6c1e2f26…`).
- `fix_patterns.py` on Current + Old + Old 2: two repeats written as rules — the mouth moved on three beats with the clause late in the prompt (HT25: the lips clause leads the prompt on any face-visible shot, V7.85.2); the team has dropped every pinned end frame on this build (hooks, P-01a) → `products/stryde/fix_patterns.md` FP15.
- Balances: Higgsfield 7706.15 · Kling 40579.

Waiting on: picks on P-03a v9/v10, P-01b v11/v12, P-05b v7/v8; Confirm or Fix on the clips P-01a v5, P-02a v3, P-05c v2, P-03b v1.
