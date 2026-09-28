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

## Where it stands
- **Waiting on the user:** Confirm/Fix the 8 plates and N-VOICE-IMG.
- **Blocked:** Kling has 3.0 credits. The two 10s voice takes (and every B-roll clip after) need Kling; §5 forbids a silent reroute to Kie.
  Top up Kling, or say "use Kie for Kling" to route through the Kie API (as stryde-lost-moments did).
- **Next on the frame's Confirm + credits:** G1/G2 → `voice_source.py` → `elevenlabs_clone.py` (name `Stairs`) → Enhance + `eleven_v4`
  (4 takes, one request) → house cut → HeyGen Avatar V talking heads TH-01…TH-16 → `trim.py` — no stop. Then `assemble.py --lengths`,
  hook images (HK-01a, HK-02a) → Hook 1 gate.
