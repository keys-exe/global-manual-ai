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

- 2026-09-29: all seven plates confirmed on the board. N-VOICE-IMG sent to Fix ("make it face in camera"). Diagnosed: my prompt turned her three-quarters to the camera. Fixed at the prompt (square to the lens, both eyes on it, turn negatives) → v2 (job 8f9d205f…), To check; v1 moved to Old. Take calls now point at v2.

- 2026-09-29: N-VOICE-IMG v2 sent to Fix ("REMOVE THE PHONE AND BELONGINGS IN THE TABLE"). Diagnosed: FRAME-PROPPED's "phone leaned against something on the table in front of them" kept drawing props. Fixed at the prompt: FRAME-PROPPED replaced by a tripod out of shot, no table — she sits on a kitchen chair, hands in her lap — foreground/belongings negatives; the take motion now lifts her hand "off her lap" → v3 (job 535077f9…), To check; v2 on Old. Take calls point at v3.

- 2026-09-29 (hourly check): N-VOICE-IMG v3 confirmed by the user → voice straight through (§22U). Kie `kling-3.0` takes G1–G3 (10s, sound on, 270 credits each; tasks a0816530…, 9008a950…, fadb474f…) on the board as N-G1…G3, To check.
  `voice_source.py`: same-voice gate PASS (197.5 / 195.1 / 205.1 Hz), joined 14.6s → looped 43.8s → `voice/NotYourCartilage_clone_source.mp3`. Cloned by API: **NotYourCartilage `HM4T2DuqaA2XtRHcA7us`**.
  `tts_api.py` eleven_v4 speed 0.85, `vo/ALL.enhanced.fitted.txt` (HK1+HK2+HK3+BODY one request): 4 takes, 71–72s, ~156 wpm; `cut_points.py` split each (all words present); `vo_trim.py` house cut per part → 16 pieces `VO-T<n>-<PART>`, all on the board To check.
  House-cut verify: T2 PASS on all four parts → **working take T2**; T1-HK1, T3-HK1 (a breath left at the hook's tail) and T4-BODY (a breath left at 17.5s) FAIL. Variants on T2: HK1+BODY 61.95s 156 wpm · HK2+BODY 62.21s 155 · HK3+BODY 62.72s 156 (≤ 180, the reference's rate).

- 2026-09-29: user "CONFIRMED PROCEED" — confirmed VO take **T4** on every part (T4-BODY keeps one breath at 17.5s, the user's choice) → VO locked (`voLocked`, voice N locked); T1–T3 moved to Old; N-G1…G3 confirmed.
  E6 lengths on the T4 master (`edit/plan_len_HK<n>.json`, `assemble.py --lengths`, no failures) → `edit/call_lengths.json`, written as `duration` on every beat. Masters: HK1 60.86s · HK2 61.04s · HK3 61.68s. B-01a's anchor moved to the body's first word ("Built") so each hook ends where the body starts (hooks 3.5–4.4s on screen).
  Step 6: HK1-01 image (ANAT-B, worn cartilage shown calm) — Higgsfield logged `nano_banana_flash` for `nano_banana_2` (job 11ce6cd7…) = failed generation (§5/§18A), not used; re-run on Kie `nano-banana-2` (task 14799498…, 12 credits) → on the board To check.

- 2026-09-29: HK1-01 image sent to Fix ("MAKE MORE DETAILS"). Diagnosed: ANAT-B (ghost limb) is empty inside by design. Fixed at the prompt: ANAT-A full stack + named fine detail (tendons, ligaments, menisci, bone grain), still calm, no emission; model `nano_banana_pro` (mechanism class allows it, §18A) on Kie (task 16cedf8c…, 18 credits) → v2 To check; v1 on Old.

- 2026-09-29: user "CONFIRMED PROCEED" — HK1-01 image v2 confirmed. HK1-01 video: `hooks/HK1-01.call.json` (RIG-RVD small lateral drift, the joint stays calm, 1,926 chars) preflight PASS → Kie `kling-3.0` 5s (task 0bc64313…, 90 credits) → on the board To check.

- 2026-09-29: user "CONFIRMED PROCEED" — HK1-01 video confirmed (hook 1 done). HK2-01 image (`hooks/build_hk2.py`: Folake in her armchair, a bad-knee morning, no strap; R1 sheet + P1 lounge attached) on Kie `nano-banana-2` (task 75717998…, 12 credits) → To check. F-D1 wardrobe: headwrap dropped (it would hide her braids, part of her identity).

## Where it stands
- **Waiting on the user:** Confirm/Fix the HK2-01 image; script flags F2, F5, F6, F7.
- **Next:** HK2-01 video (5s, one rub of the knee, a glance out of the window), then HK3-01 (image → video), then the body B-roll (step 7). Videos on Kie `kling-3.0`; NB2 images on Kie while Higgsfield logs flash.
