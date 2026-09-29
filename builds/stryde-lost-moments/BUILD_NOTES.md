# Build notes — stryde-lost-moments (STRYDE · Lost Moments, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1UD92i5fATH3qiiez2jqI2WFQXYxxuPLc
- User message: "run manual. british" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 5 in script.
- Script (legacy `.dot`) read out word for word → `intake/script.txt`; per-variant `work/script_<A–E>.txt` and `.lines.txt`.
- Product Sheet V7.49.32 (wordmark lock) came with the folder → now `products/stryde/`.
- **Boards (since 2026-09-29, account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/HuZVrvs1M47vyzGNWmY1qU · Old https://claude.ai/artifact/4YwhNR2SEyter4U7XvfzJo · Final https://claude.ai/artifact/LHHTb3VdrPK6jf6usYXU5G · Plan https://claude.ai/artifact/3HLCjbPj6rHkMZ6gVxfFX9
- First board (other account, not readable from this one): https://claude.ai/artifact/BahH1QuzHm4bQ9FAdxXfKj
- **Hourly Fix check:** `trig_01QpbwhQm7KT5WJc8zDfvTip` (:47 UTC, session_01LDF4chVVFx9eyVTx6g8W8j, new boards). Old one on the other account: `trig_014cgd2iBMe2YGBTHFEEGFrY` (:47 UTC, bound to session_01QFtjcJsQcS8p957wEAS4kb, this board only; replaced `trig_01G3hn1iQuLVknpWifsZ4Hcp` on resume 2026-09-28 16:02 UTC).

## Sessions
- session_01H4ZN9xQDenS8RsLkEHVFiq (2026-09-28 13:00–13:20 UTC): steps 1–3. Absorption, ledger, phrase inventory,
  claims, Mode & Model Lock; 7 avatar sheets generated on Higgsfield (Sunburst, 2k, one each) and put on the board as
  To check; `docs/absorption` written. Higgsfield 19,676 credits before the cast.

- same session, 2026-09-28 13:25–14:05 UTC: user confirmed all 7 avatars ("I'VE CONFIRM PROCEED"; F1/F3/F4 not answered →
  voiced as written, flags open). Steps 4–5: 10 plates + DOG-BRAMBLE + GK1/GK2 sheets generated (Sunburst, one each) → board,
  To check. Act map for all five variants (`work/actmap.py` is the source; 76 beats, 125 cuts; `angles.py` PASS ×5);
  76 planned cards + docs/actmap, docs/wardrobe, docs/locations on the board. §22U step 1: narrator voice-source frame
  submitted (job b933463d…, nano_banana_pro requested — Higgsfield logs nano_banana_2 again, §5 routing fault as in stryde-identity).

- 14:00–14:15 UTC: user "I'VE CONFIRM PROCEED" — board shows the 10 plates confirmed; N-VOICE-IMG, DOG-BRAMBLE, GK1, GK2
  still To check (Kling voice takes wait for N-VOICE-IMG's Confirm, §22X). Step 6 started: Hook 1 images A-HKa (NB2) and A-HKb
  (NBP, SEAT_LOCK) generated → board To check (`work/beats.py` builds beat T2Is from Appendix A + Product Sheet). Product refs
  uploaded to Higgsfield: `work/higgsfield_media.json`. D-10 revised: never both knees (SIDE_RULE 3) → worn right + second strap held.
  Higgsfield logs NB2 as nano_banana_flash and NBP as nano_banana_2 (routing labels; recorded on the cards).

- 14:50–16:05 UTC (same session): narrator talking-head frame (N-VOICE-IMG) redone on the user's chat notes — v2 redo,
  v3 rebuilt around the script (own stairs, strap worn), v4 kitchen, v5 facing the camera, v6 straight-on eye-level chest-up.
  User asked for another option → N2-VOICE-IMG option B (Black British man, 66, south London), text-only person, To check.
  Board: DOG-BRAMBLE, GK1-AMARA, GK2-TOBI confirmed by the user (15:12).

- session_01QFtjcJsQcS8p957wEAS4kb (2026-09-28 16:00 UTC): resumed from the Drive link; merged `claude/vigilant-cannon-wre8v5`
  into `claude/amazing-bohr-tsowwg`; hourly Fix check moved here.

- 16:20 UTC: user "PROCEED TO VOICE" → narrator = option A (N-VOICE-IMG v6, the one the user kept refining after B was offered).
  Kling takes G1/G2 re-fitted to the v6 chest-up frame (hands rest on the table, small nod on the stress word instead of a hand lift;
  audio only is used), `preflight.py` PASS both (`voice/N_G*.call.json`). **Blocked: Kling balance 3.0 credits** — not sent.

- 16:20–19:50 UTC (session_01QFtjcJsQcS8p957wEAS4kb): **voice** — Kling had 3 credits → user: "use kie ai if not enough credits in kling" (now §5, V7.65.0).
  G1/G2 on Kie `kling-3.0/video` (pro, sound) → `voice_source.py` PASS (202.5 Hz both, 33.2s) → ElevenLabs clone **`Lost` `D20hb4HQVPwtiDd89W7m`**.
  VO: all five variants in one eleven_v3 request (4,802 chars, verbatim PASS), 4 takes; T1 split per variant; user confirmed VO-T1-HK1…HK5
  (old butt-join cut). Merged **V7.65.0** (blissful-brown): house cut with natural pauses — T1–T4 re-cut to `vo/trim/` (144–151 wpm, cap 179);
  not yet on the board. T1 V5 ends clipped (last word cut by the TTS) — user confirmed it anyway; flag.
  **Hook 1 done** (user confirmed both clips): A-HKa = from the foot of the stairs, down backwards holding both rails (user reference
  clip `hooks/ref_stairs_user.mp4`); A-HKb = strap snug under the kneecap, 3/4 side view like the user's photo `hooks/ref_strap_placement_user.jpg`
  (v7: strap lifted by hand + GPT Image 2.5 seam cleanup — Nano Banana edits kept lowering it). A-HKb took 4 video generations (user's go).
  Hook 2 started: B-HKa (struggling onto the bench) and B-HKb (placement like the user's photo) images on the board, To check.
  Lessons for every hook: show the struggle; product framed like the user's placement photo, notch against the kneecap, no hands over it.

## Where it stands
- Hooks 1–3 confirmed (C-HKb: frame v4 coffee mug + clip v4, 4th generation on the user's go). Hook 4: D-HKa, D-HKb frames v1 To check → their clips (5s, Kie kling-3.0 while Kling is short) after the Confirm. Then Hook 5 (E, Clifton).
- Lessons: GPT Image 2.5 edits need `resolution: 2k` and "same crop, do not zoom out" (1k default zoomed out and moved the strap). `kie.py kling --out` is the MP4 path, not a task file — log the full output to keep the task id.
- Put the V7.65.0 VO re-cuts (vo/trim) on the board as new versions; then `assemble.py --lengths` per variant on the chosen cut.
- Open flags: F1, F3, F4 (claims), F11 (`package_closed.jpg`); VO V5 last word clipped on T1.

- session_01LDF4chVVFx9eyVTx6g8W8j (2026-09-29 09:00 UTC, account iamnotkeysi@gmail.com): resumed; the first board set and sessions
  belong to the user's other account and can't be read here → user: "NEW BOARD". Four new boards from the template. Rebuilt from
  the repo + connectors: 9 cast, 11 plates/dog, narrator frame v6 (Higgsfield job URLs), hook frames + clips (Higgsfield / Kie task
  URLs), 66 planned B-roll cards from `work/actmap_rows.json`, plan docs. Only current versions moved (old versions stay on the first
  Old board). Take 1 re-downloaded from ElevenLabs history (AGEjLCNEsKA4hCC0ADOI), split at `split_T1.json` cuts, house cut →
  VO-T1-HK1…5 To check (V3: breath at 18.79s kept; V4: breath 32.14s + long pause 28.11–28.75s; V5: last word clipped by the TTS).
  **C-HKb clip v4 not recovered** (its Kie task id was never logged) — the user downloads it from the old board.
  D-HKa image Fix (user): "MAKE IT STRUGGLING ON HIS KNEE PAIN" → v5 nano_banana_pro edit of v4 (job 93103d12-eb4e-444a-b035-84ebaf026a33).
