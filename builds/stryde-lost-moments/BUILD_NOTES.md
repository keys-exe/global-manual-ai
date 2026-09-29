# Build notes — stryde-lost-moments (STRYDE · Lost Moments, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1UD92i5fATH3qiiez2jqI2WFQXYxxuPLc
- User message: "run manual. british" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 5 in script.
- Script (legacy `.dot`) read out word for word → `intake/script.txt`; per-variant `work/script_<A–E>.txt` and `.lines.txt`.
- Product Sheet V7.49.32 (wordmark lock) came with the folder → now `products/stryde/`.
- **Board:** https://claude.ai/artifact/BahH1QuzHm4bQ9FAdxXfKj
- **Hourly Fix check:** `trig_014cgd2iBMe2YGBTHFEEGFrY` (:47 UTC, bound to session_01QFtjcJsQcS8p957wEAS4kb, this board only; replaced `trig_01G3hn1iQuLVknpWifsZ4Hcp` on resume 2026-09-28 16:02 UTC).

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

## Where it stands
- **Blocked:** Kling has 3.0 credits — the two 10s voice takes (1080p, audio) can't run until it's topped up. Kling has no fallback (§5).
- **Waiting on the user's check:** Hook 1 images A-HKa, A-HKb. Narrator = option A (from "PROCEED TO VOICE"); N2 option B dropped unless the user says otherwise.
- **Confirmed:** all 7 avatars, 10 plates, DOG-BRAMBLE, GK1-AMARA, GK2-TOBI.
- **Next on the voice frame's Confirm:** §22U step 2 — two Kling takes (`voice/N_G1.kling.json`, `voice/N_G2.kling.json`,
  ≤2,500 chars, same image, VOICE-NARR first in delivery), then `voice_source.py` → clone source for the user to clone
  in ElevenLabs (name `LostMoments-Narrator`, or `Lost` if free).
- Then: five voice masters in one TTS request (all hooks + all bodies), house cut, `assemble.py --lengths` for durations,
  then step 6 hooks one by one (Hook 1 = A first).
- Open flags: F1, F3, F4 (claims), F11 (`package_closed.jpg`).
