# Build notes — stryde-not-your-cartilage (STRYDE · Not Your Cartilage, voice-only Short VSL, 3 hooks, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/13oUXl866Cxjts6mSxCZJAGcCsxeoxein
- User message: "Run manual British" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 3 in script (A, B, C), **one shared body** → 3 videos.
- Script header (ADJUST): different voice than the reference (British, ElevenLabs), different B-roll and editing, ~50% Black people on the B-roll, add music.
- Inspo `MY INSPO VIDEO.mp4` → `intake/inspo.mp4` — the same STRYDE "Too bad" ad as `stryde-too-bad` (also in `facebook-ad-creatives.zip`, byte-identical); script `Untitled document.docx` → `intake/script.docx`; spoken parts `work/script_{HK1,HK2,HK3,BODY}.txt`.
- Product Sheet in the folder is V7.49.32; the repo's V7.49.38 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/DUsxw9aB6Q4PE7uTa9FFLE · Old https://claude.ai/artifact/7qQDVB81c5s5JtejBqJZw1 · Final https://claude.ai/artifact/7bejwknnCQGFtV6AUN3Nxc · Plan https://claude.ai/artifact/7ntxnK1H2VmA62SndFADqW
- **Hourly Fix check:** `trig_01VVKAYxpqHJqE5dcw86Tp94` (:37 UTC) → session_01RZU34LVeJoqim4KzeYh4ju

## Sessions
- session_01RZU34LVeJoqim4KzeYh4ju (2026-09-29 ~12:40 UTC): steps 1–3. Absorption (inspo already measured for stryde-too-bad: 51.96s, 33 shots, ~180 wpm, male voice, no talking heads), ledger (VN-H1, VN-H2), phrase inventory (HK1–HK3 + B-01…B-14), claims (F4–F9), Mode & Model Lock.
  Cast on Higgsfield Sunburst 2k, one each: N-NARR (voice only), R1-FOLAKE, R2-DEREK, R3-HASSAN, R4-ELAINE. First R1 (Patrice) and R3 (Kwame) withdrawn by me before review — too close to stryde-failed-alternatives R1 Patricia / R3 Emmanuel — recast; the withdrawn renders are on the Old board. 7 Sunburst jobs; Higgsfield 17,384 credits before the cast.
  Four boards made; build doc on all four, cast on Current, docs/absorption on Plan + Current.

- 2026-09-29: user "I'VE CONFIRM PROCEED" — the five cast sheets confirmed on the board from the message; docs/absorption confirmed.
  Steps 4–5 (`STEP4_5.md`): seven 16:9 plates on Higgsfield Sunburst (P0-PROP-FO, P1-F-LOUNGE with P0 attached, P2-D-TOWPATH, P3-PROP-H, P4-H-KITCHEN with P3 attached, P5-E-BEDROOM, P6-CONSULT), To check;
  act map `work/actmap.py` (25 unique beats, 22 shots per video, `angles.py` PASS all three), wardrobe ledger; board: plates + 25 planned beats, docs locations/actmap/wardrobe on Plan + Current.
  §22U step 1: `voice/N_step1_v1.jpg` (job 001cafe9…, nano_banana_pro requested, job reports nano_banana_2), sheet + face crop (`voice/N_face_ref.jpg`, Higgsfield media 2d6c030f…) attached, on the board as N-VOICE-IMG, To check.
  Step 2 ready: `voice/N_G1..G3.call.json` (2,465–2,489 chars), preflight PASS except the frame's approval. **Kling connector has 3 credits → takes go via Kie `kling-3.0` (§5 fallback)**; Kie 169,864.8 credits.
  Step 8: `vo/ALL.enhanced.txt` (HK1+HK2+HK3+BODY, one request) verbatim PASS, 1,417 chars.

## Where it stands
- **Waiting on the user:** Confirm/Fix the seven plates and the narrator frame N-VOICE-IMG (paid video waits on it, §22X); script flags F2, F5, F6, F7.
- **Next, no stop once the frame is confirmed:** Kie Kling takes G1–G3 → `voice_source.py` (medium trim, ×1.2, gate, loop ≥30s) → `elevenlabs_clone.py` `NotYourCartilage` → `tts_api.py` eleven_v4 speed ~0.85, takes on the board → `vo_trim.py` house cut per variant. Then hooks HK1-01, HK2-01, HK3-01 (step 6).
