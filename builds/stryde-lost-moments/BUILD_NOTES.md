# Build notes — stryde-lost-moments (STRYDE · Lost Moments, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1UD92i5fATH3qiiez2jqI2WFQXYxxuPLc
- User message: "run manual. british" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 5 in script.
- Script (legacy `.dot`) read out word for word → `intake/script.txt`; per-variant `work/script_<A–E>.txt` and `.lines.txt`.
- Product Sheet V7.49.32 (wordmark lock) came with the folder → now `products/stryde/`.
- **Board:** https://claude.ai/artifact/BahH1QuzHm4bQ9FAdxXfKj
- **Hourly Fix check:** `trig_01G3hn1iQuLVknpWifsZ4Hcp` (:47 UTC, bound to session_01H4ZN9xQDenS8RsLkEHVFiq, this board only).

## Sessions
- session_01H4ZN9xQDenS8RsLkEHVFiq (2026-09-28 13:00–13:20 UTC): steps 1–3. Absorption, ledger, phrase inventory,
  claims, Mode & Model Lock; 7 avatar sheets generated on Higgsfield (Sunburst, 2k, one each) and put on the board as
  To check; `docs/absorption` written. Higgsfield 19,676 credits before the cast.

- same session, 2026-09-28 13:25–14:05 UTC: user confirmed all 7 avatars ("I'VE CONFIRM PROCEED"; F1/F3/F4 not answered →
  voiced as written, flags open). Steps 4–5: 10 plates + DOG-BRAMBLE + GK1/GK2 sheets generated (Sunburst, one each) → board,
  To check. Act map for all five variants (`work/actmap.py` is the source; 76 beats, 125 cuts; `angles.py` PASS ×5);
  76 planned cards + docs/actmap, docs/wardrobe, docs/locations on the board. §22U step 1: narrator voice-source frame
  submitted (job b933463d…, nano_banana_pro requested — Higgsfield logs nano_banana_2 again, §5 routing fault as in stryde-identity).

## Where it stands
- **Waiting on the user's check:** 10 plates, DOG-BRAMBLE, GK1-AMARA, GK2-TOBI, and N-VOICE-IMG (the narrator's voice-source frame).
- **Next on the voice frame's Confirm:** §22U step 2 — two Kling takes (`voice/N_G1.kling.json`, `voice/N_G2.kling.json`,
  ≤2,500 chars, same image, VOICE-NARR first in delivery), then `voice_source.py` → clone source for the user to clone
  in ElevenLabs (name `LostMoments-Narrator`, or `Lost` if free).
- Then: five voice masters in one TTS request (all hooks + all bodies), house cut, `assemble.py --lengths` for durations,
  then step 6 hooks one by one (Hook 1 = A first).
- Open flags: F1, F3, F4 (claims), F11 (`package_closed.jpg`).
