# Build notes — stryde-too-bad (STRYDE · Too Bad, voice-only Short VSL, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1sRxZ8thrNmqmo1hVO3MJxY_-dCHGlsxE
- User message: "RUN MANUAL. BRITISH" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 2 in script (A TooSmall, B Gimmick), **each with its own body** → 2 videos.
- Script header (ADJUST): different voice than the reference (British, ElevenLabs), different B-roll and editing, ~50% Black people on the B-roll, add music.
- Inspo came as `INSPO VIDEO` (no extension) → `intake/inspo.mp4`; script `Untitled document.docx` → `intake/script.docx`; spoken parts `work/script_{HK1,BODY1,HK2,BODY2}.txt`.
- Product Sheet in the folder is V7.49.29; the repo's V7.49.37 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/DW6GGWmvHtVhDJrWaxT1JZ · Old https://claude.ai/artifact/GFL3d6zEr8E4bPENfKkyTq · Final https://claude.ai/artifact/3phx9ujBsxcHiEcsgm3xPN · Plan https://claude.ai/artifact/D5erRJZXiEc2YeMYMyo829
- **Hourly Fix check:** `trig_01EXxSghcfLknvjrcVydXT8E` (:57 UTC) → session_01HJGJHPXbrGqt1pRRPaR5y2 (moved 2026-09-29 16:15 UTC; old `trig_01HgUSKGTLcAkdqfwiatEx76` deleted)

## Sessions
- session_01Ch2ZePb5MrH51Vk5hxbwTx (2026-09-29 ~11:45 UTC): steps 1–3. Inspo measured (51.96s, 33 shots, mean 1.57s, ~180 wpm, male voice 132 Hz, no talking heads),
  absorption, ledger (VN-H1, VN01, VN02), phrase inventory (HK1 + B1-01…13, HK2 + B2-01…12), claims (F4–F9), Mode & Model Lock.
  Cast on Higgsfield Sunburst 2k, one each: N-NARR (voice only), R1-GRACE, R2-ALAN, R3-KOFI, R4-FIONA. Higgsfield 17,527 credits before the cast.
  Four boards made; build doc on all four, cast on Current, docs/absorption on Plan + Current.

- 2026-09-29: user confirmed R1 Denise and said proceed. Steps 4–5 (`STEP4_5.md`): six 16:9 plates on Higgsfield (P0 kitchen, P1 garden with P0 attached, P2 lounge, P3 shop, P4 consult, P5 PROP-F hall/stairs), To check;
  act map `work/actmap.py` (29 unique beats, 20 shots per video, `angles.py` PASS both), wardrobe ledger; board: plates + 29 planned beats, docs locations/actmap/wardrobe on Plan + Current.

- 2026-09-29: user "CONFIRM ALL LOCATION. PROCEED" — P0–P4 confirmed on the board, P5 confirmed from the message.
  §22U step 1: `voice/N_step1_v1.png` (job 7ae0b05d…, requested nano_banana_pro, job reports nano_banana_2 — the known logging mismatch) on the board as N-VOICE-IMG, To check.
  Step 2 ready: `voice/N_G1..G3.call.json` (2,441–2,482 chars, §37 TH ladder steps 1+4), preflight PASS except the frame's approval.
  **Kling connector has 3 credits → takes go via Kie `kling-3.0` (§5 fallback)**; Kie 175,036.8 credits. Step 8: `vo/ALL.enhanced.txt` (HK1+BODY1+HK2+BODY2, one request) verbatim PASS, 2,434 chars.

- 2026-09-29: N-VOICE-IMG sent to Fix ("fix this"). Diagnosed: v1 drew a second phone in her hand, a pen mug and a garbled newspaper in front of her (my prompt's "phone propped against a mug of pens"). Fixed at the prompt (bare desk, no device in frame, added negatives) → v2 (job 055e39b6…), To check; v1 moved to Old. Take calls now point at v2.

- 2026-09-29: N-VOICE-IMG v2 sent to Fix ("USE MY AVATAR NARRATOR"). Diagnosed: v2 ignored the sheet (younger, brown hair) and drew a camera-app screen. Fixed: the sheet's face close-up cropped (`voice/N_face_ref.png`, Higgsfield media 4a0599ba…) attached as image 2 beside the sheet, identity restated, camera-UI negatives → v3 (job 847461ac…), To check; v2 on Old. Every job still reports nano_banana_2 though nano_banana_pro is requested.

- 2026-09-29: user "CONFIRMED PROCEED" (N-VOICE-IMG v3). §22U straight through: 3 Kie Kling takes (G3 resent once after Kie "Internal Error") → `voice_source.py` PASS (13.57s, 40.75s looped; lead-ins of G2/G3 cut first, whisper stretched the first word) → clone **TooBad `5Iu9piJEpm2ewCIAa3Wm`** → TTS: T1–T4 (v1 text, pace tags) finish 154–161 wpm; **`speed` has no effect on eleven_v4 (measured)**; T5–T8 (v3 text, Enhance tags only) 166–172 wpm, 55–57s per video → house cut per video, every one PASS. Working take T5. Records: `voice/VOICE_SOURCE.md`, `vo/VO.md`.

- 2026-09-29: board outage (HTTP 503) held the VO cards; after it cleared all 32 VO part cards (T1–T8 × HK1/BODY1/HK2/BODY2) went on the board (`vo/assets.json`). User "VOICE ID: PROCEED" → narrator voice TooBad marked **locked**.

- 2026-09-29: user "CONFIRMED PROCEED" — **VO locked on T8** for HK1, BODY1, HK2, BODY2 (`vo/cut/T8_V1.mp3`, `T8_V2.mp3` are the masters; 55.38s / 54.69s). Step 6: hook start images HK1-01 (NBP, refs front+back product photos, Denise sheet, lounge plate) and HK2-01 (NB2, Alan sheet, kitchen plate) — `hooks/build_hooks.py`, refs `hooks/refs.json` — on the board To check. Jobs report nano_banana_2 / nano_banana_flash.

- 2026-09-29 ~16:15 UTC, resumed in session_01HJGJHPXbrGqt1pRRPaR5y2: board read — Act 1 has B1-01a confirmed, the other 19 images To check, no Fix notes; Act 2 not started. Hourly Fix check moved here.
  B1-01a is a pinned beat (product placed): its end-frame prompt `broll/B1-01a-END.t2i.txt` (refs: B1-01a v1 job 3c9bea78…, product front, back) is written in `build_broll.py` (END dict).
  **Higgsfield no longer lists `nano_banana_pro`, `nano_banana_2` or `gpt_image_2_5`** ("unknown model"; balance 15,854.5 — not the §5 out-of-credits case).
- 2026-09-29 ~16:25 UTC: user reviewed Act 1 on the board — confirmed B1-05b, B1-08, B1-09a, B1-09b, B1-10, B1-11, B1-12a, B1-13a, MECH-04, MECH-S1, MECH-S2 (with B1-01a: 12 of 20);
  Fix notes on 7, then "FIX THOSE". Fixed at the prompt (`build_broll.py`, a `# v2 Fix` note on each):
  B1-02 "FIX THIS IMAGE" (third leg, finger on the shin → two legs counted, fingertip under the kneecap) · B1-04b "WRONG PRODUCT" (neoprene band with a chevron patch → exact-object lock, W outline, worn_front ref) ·
  B1-06 "MAKE IT SMALL" (held at the lens → arm's length, a fifth of the frame, cm size) · B1-13b "REMOVE THE STRAP" (no strap, product refs out) ·
  CARD-12b "Show two straps placed on the table" (floating card → lying on the lounge's oak table, lounge plate ref) ·
  MECH-03 "CREATE NEW ANATOMY" (side view to the hip → the confirmed MECH-S1 look, front, knee filling the frame) · MECH-05 "ADD A MUSCLE" (bone-only ANAT-B → ANAT-A muscle over bone, MECH-04 style ref).
  **Images now go through Kie AI** (`broll/run_kie_fix.py`, same models: nano-banana-pro / nano-banana-2 / gpt-image-2-5-sunburst-image-to-image, 2K; results `broll/kie_fix.json`) — the user's Fix could only run there. All 7 v2 renders + **B1-01a-END v1** on the Current board as To check; the 7 v1s moved to the Old board (copied, archived on Current, deleted from Current).
- 2026-09-29 ~16:45 UTC: user "Add B-roll to every line in Body 1. Create a B-roll for every line". Body 1 timed off the T8 master (Whisper word timings, 52.4s, 24 sentences).
  Three lines had no live-action picture of their own → **B1-02a** (Denise holds the strap beside her bare knee — "They're small on purpose"), **B1-03a** (Alan steps down one low step in his kitchen — "Seventeen times your bodyweight…"; MECH-02 moves to "centimetres"), **B1-07a** (Alan rubs his knee at the kitchen table — "Perfect for bone on bone, arthritis…"; MECH-05 moves to "cartilage"). B1-02's anchor moved to "one", B1-07a's is "bone", so every hold is ≥ 2.0s.
  Not split: "No slipping. No sores. No rolling down." (2.6s) and "Too small to work? Try it on your own stairs. Nothing to lose but the pain." — per-sentence shots there would be under 1s, below the 2.0s floor (§30H).
  Act map (`work/actmap.py`, STEP4_5.md): Video 1 now 23 shots, 32 unique beats; `angles.py` PASS both videos. The three start images made on Kie (one each) and on the Current board as To check.

## Where it stands
- **Hooks, 2026-09-29:** HK1-01 (v2 image, HK1-01-END end frame, pinned clip v1, Kie task 800927cb…) and HK2-01 (image + clip v1, Kie task b080e98e…) all confirmed by the user.
- **Act 1 B-roll images, 2026-09-29 (user "CONFIRMED PROCEED"):** 20 start images made with `broll/build_broll.py "Act 1"` (Higgsfield, one render each: 12 nano_banana_pro, 7 nano_banana_2, CARD-12b gpt_image_2_5 sunburst 2k), all on the board as To check. Job ids `broll/jobs_act1.json`, CDN links `broll/urls_act1.json`, board assets `broll/assets_act1.json`. Product refs: hooks/refs.json + the STRYDE worn/package reference media (`broll/refs.json`). The nano_banana_2 renders come back at 768×1376 (the jobs report nano_banana_flash). Pin-end beats in Act 1 (B1-01a product placed, B1-04b ends seated, B1-06 product turns) need an end frame each once their start images are confirmed.
- **Waiting on the user:** Confirm/Fix the 7 Act 1 v2 images, B1-01a-END, MECH-02 (still unreviewed) and the new B1-02a, B1-03a, B1-07a; script flags F2, F4, F5, F7, F8, F9.
- **Next:** Act 1 end frames (B1-01a, B1-04b, B1-06) and clips for the confirmed images (Kling 3.0 on Kie, E6 lengths, preflight); then Act 2 (9 beats).
