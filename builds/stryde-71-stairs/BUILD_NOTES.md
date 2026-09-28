# Build notes — stryde-71-stairs (STRYDE · 71 Stairs, Black American Woman · Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1B2H-Kx8-NpEKsMoL0IvMqbvy8uAQIL5T
- User message: the Drive link + "RUN MANUAL". MODE blank → Mode 1; HOOKS → 1 in script ("same hook as 71 Stairs"); VOICE from the script note (Black American woman, 71, light Southern accent).
- Script is a native Google Doc: `fetch_drive.py` exported it as .docx → `intake/script.txt`; spoken lines `work/script.lines.txt` (613 words; the direction note is VN01–VN08, not voiced).
- Inspo = the original 71 Stairs ad (155.6s, 82 shots, selfie TH + B-roll, 231 wpm). Transcript kept in the Build Sheet structure map.
- Product Sheet V7.49.32 (same as stryde-lost-moments) → `products/stryde/`.
- **Boards:** Current https://claude.ai/artifact/Ev166tkWbX9QaE1P7VLjti · Old https://claude.ai/artifact/E3hbWw3ea9nS8vTgzGLLmd · Final https://claude.ai/artifact/QVBQW1v5WHJ7cJN4PGxcbY · Plan https://claude.ai/artifact/KZ6FRJSii34aQcCTp6XmNy
- **Hourly Fix check:** `trig_019vEknq3DfbCfaWGSyrTvy5` (:17 UTC, bound to session_01D42imWscMStnxPKqpqZQpb).

## Sessions
- session_01D42imWscMStnxPKqpqZQpb (2026-09-28 18:35–18:55 UTC): steps 1–3. Absorption, ledger, phrase inventory, claims,
  Mode & Model Lock; 3 avatar sheets (N-NARR, C1-LORETTA, C2-DAUGHTER) on Higgsfield (Sunburst, high, 2k, one each) → board
  To check; `docs/absorption` on Plan + Current. Higgsfield 18,072.75 credits before the cast.

- same session, 2026-09-28 19:00–19:15 UTC: user "CONFIRMED ALL" → the 3 avatars and the absorption confirmed on the board;
  flags closed on the recommendations (F1/F2/F4 voiced as written, F5 Amazon voiced never pictured, F9 1 hook, F11 verbatim, F12 natural pace).
  Steps 4–5: 8 plates (Sunburst, one each) → board To check; act map (75 rows: 59 B-roll + 16 TH, `work/actmap.py`, all 613 words
  covered in order, `angles.py` PASS) + wardrobe map + locations → `STEP4_5.md`, docs/actmap, docs/wardrobe, docs/locations on Plan + Current;
  75 planned cards on Current. §22U step 1: N-VOICE-IMG (selfie on the landing, nano_banana_pro requested, Higgsfield logs nano_banana_2)
  → board To check. Voice takes `voice/N_G1.call.json`, `N_G2.call.json` built; preflight PASS except "start image approved".
  Higgsfield 17,998.5 · Kling 3.0 · Kie 215,672.8.

- 19:20 UTC: user "FIX THOSE" → board Fixes: P1-LANDING ("THE PICTURES NOT THE SAME AS THE P0") regenerated with P0-PROP-N attached
  as reference, the photo wall written as P0's (v2, job a53b6e6b); P4-STORE ("FIX THE DISTORTIONS") regenerated as an empty store with
  straight-line geometry, no people, PHYS-FRAME-C body clause dropped (v2, job 751cd1e7). v1s moved to the Old board. N-VOICE-IMG was built
  against P1 v1 — if you want its photo wall to match too, press Fix on it.
- 19:30 UTC: user "FIX THE LOCATIONS FIRST" → second board Fixes: P1-LANDING v3 ("WRONG STAIRS": now P0's own straight open flight
  seen from the top — photo wall left, balusters + dark rail right, hall and front door at the bottom, P0 attached; job 2cc80516);
  P4-STORE v3 ("WRONG COUNTERS NOT REAL": a standard US checkout stand — belt, divider, register screen, scanner, card terminal on a post,
  bag carousel, impulse rack, lane light; job 87a0c23e). v2s moved to Old. Other 6 plates confirmed by the user. Voice waits on the
  locations (user's order) and on Kling credits.
- 19:45 UTC: user "LOCKED LOCATIONS FOR TH IMAGE DONT USE SELFIE STYLE" → all 8 plates confirmed (locked). §34 correction for this build:
  talking heads are **propped, never selfie** — TH-01…TH-16, C-06a and N-VOICE-IMG (act map, STEP4_5, Build Sheet EG02/§20, Kling
  voice calls: camera "Propped", hands at the waist). N-VOICE-IMG v2: standing at the top of her stairs, phone propped at chest height,
  waist-up; refs N sheet + P1 v3 + P0 (nano_banana_pro requested, logged nano_banana_2; job 6ceca5c9). v1 moved to Old.
  `angles.py` PASS.

- 19:50–20:05 UTC: user "USE KIE FOR KLING" (Kling connector 3.0 credits) → Kling voice takes run on Kie `kling-3.0/video`
  (pro 1080p, 10s, sound; `kie.py kling` brought in from claude/amazing-bohr-tsowwg). User "USE GPT IMAGE FOR THIS TH IMAGE" →
  N-VOICE-IMG v3 on gpt_image_2_5 Sunburst (§18A rule 7 overridden on the user's word), then "USE NANO BANANA PRO MUCH BETTER"
  → **v2 (nano_banana_pro) chosen and confirmed**; v1 + v3 on the Old board. Enhance pass written (`vo/ALL.enhanced.txt`,
  `tts_budget.py` verbatim PASS, 3,525 chars, 1 request). ElevenLabs check PASS (519 free slots).
  G1 (Kie ae8336fc, 190.5 Hz) ✓. G2 (Kie 773d0b83) 210.5 Hz = +10.5% → same-voice gate FAIL; cause in my prompt (quote "lighter,
  a little higher") → G2 v2 (Kie 4ea2119b, quote in her own voice) 222.2 Hz = +16.6% → FAIL again. Kie spend 810 credits.

## Where it stands
- **Voice stage stopped (§22X / §22U step 2):** two G2 generations failed the same-voice gate. A third needs the user's go.
  Recommendation: make the second take the next script line with no quoted speech — "Six weeks ago, I was going down my stairs
  backwards. One step at a time." (G3 rule) — the quote is what keeps lifting her pitch.
- **Locked:** 3 avatars, 8 plates, N-VOICE-IMG v2 (propped, nano_banana_pro).
- **Next on the go:** second take → `voice_source.py` → `elevenlabs_clone.py clone Stairs_clone_source.mp3 --name Stairs`
  → `eleven_v4` TTS ×4 from `vo/ALL.enhanced.fitted.txt` → house cut → HeyGen Avatar V TH-01…TH-16 → `trim.py`.
