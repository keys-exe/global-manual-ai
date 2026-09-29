# Build notes — stryde-too-bad (STRYDE · Too Bad, voice-only Short VSL, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1sRxZ8thrNmqmo1hVO3MJxY_-dCHGlsxE
- User message: "RUN MANUAL. BRITISH" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 2 in script (A TooSmall, B Gimmick), **each with its own body** → 2 videos.
- Script header (ADJUST): different voice than the reference (British, ElevenLabs), different B-roll and editing, ~50% Black people on the B-roll, add music.
- Inspo came as `INSPO VIDEO` (no extension) → `intake/inspo.mp4`; script `Untitled document.docx` → `intake/script.docx`; spoken parts `work/script_{HK1,BODY1,HK2,BODY2}.txt`.
- Product Sheet in the folder is V7.49.29; the repo's V7.49.37 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/DW6GGWmvHtVhDJrWaxT1JZ · Old https://claude.ai/artifact/GFL3d6zEr8E4bPENfKkyTq · Final https://claude.ai/artifact/3phx9ujBsxcHiEcsgm3xPN · Plan https://claude.ai/artifact/D5erRJZXiEc2YeMYMyo829
- **Hourly Fix check:** `trig_01HgUSKGTLcAkdqfwiatEx76` (:57 UTC) → session_01Ch2ZePb5MrH51Vk5hxbwTx

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

## Where it stands
- **Waiting on the user:** Confirm/Fix the narrator frame N-VOICE-IMG v2 (paid video waits on it, §22X); script flags F2, F4, F5, F7, F8, F9.
- **Next, no stop:** Kie Kling takes G1–G3 → `voice_source.py` (medium trim, ×1.2, gate, loop ≥30s) → `elevenlabs_clone.py` `TooBad` → `tts_api.py` eleven_v4 speed ~0.85, takes on the board → `vo_trim.py` house cut per variant. Then hooks HK1-01, HK2-01 (step 6).
