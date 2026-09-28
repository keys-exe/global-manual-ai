# Build notes — down-forwards-again (STRYDE · Down Forwards Again, Doctor VSL · Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1m1H8YO6MEVQBnoD2gkWPfn-y__PW0Bbk
- User message: the Drive link + "RUN MANUAL". MODE blank → Mode 1; HOOKS → 3 in script (A/B/C) → 3 finished videos; VOICE derived (the script's "his" → male doctor, British).
- Script is a native Google Doc: `fetch_drive.py` exported it as .docx → `intake/script.txt`; spoken lines `work/script.lines.txt`, split into `work/HK1–HK3.lines.txt` and `work/BODY.lines.txt` (576 words). Hook labels / "(the reference's construction, exactly)" are authoring notes (VN01–VN03), not voiced.
- Inspo = a doctor-authority menopause supplement ad (the script's "Reference" link), 142.1s, 40 shots, 360×640 download, renamed `intake/inspo.mp4`; transcript `intake/inspo_transcript.txt`; measurements `intake/inspo_report.json`.
- Product Sheet V7.49.32 → `products/stryde/` (was V7.49.31 on this branch).
- **Boards:** Current https://claude.ai/artifact/UqVKJB21YyfBZTjxh5dNNT · Old https://claude.ai/artifact/8eXUW9NwJq49zRfPHtgC5Y · Final https://claude.ai/artifact/W11NPXayafpTXoY4FqMccb · Plan https://claude.ai/artifact/5Wzyk63o5viz5t4wLVZUu7
- **Hourly Fix check:** `trig_01XNVEi8936asCGsYpstFCaw` (:41 UTC, bound to session_01YaVWUyhH3VYNdrBjxmx6TC).

## Sessions
- session_01YaVWUyhH3VYNdrBjxmx6TC (2026-09-28 19:05–19:25 UTC): steps 1–3. Absorption, ledger, phrase inventory, claims,
  Mode & Model Lock; 2 avatar sheets (D-DOC, P-PATIENT) on Higgsfield (Sunburst, high, 2k, one each) → board To check;
  `docs/absorption` on Plan + Current. Higgsfield 17,998.5 credits before the cast.

- Same session 19:48 UTC: user "USE BRITISH ETNICITY" → D-DOC recast white British (v2 `71b20c5a`), v1 moved to Old; VOICE-DOC → light Yorkshire. Hourly check 19:41 found no Fixes.

- Same session ~20:00 UTC: user "go ahead with steps 4–5" → STEP4_5.md: PROP-P (Victorian terrace, stairs on the left wall),
  plates P0 hall/stairs, P1 front room, P2 kitchen (both with P0 attached), P3 consulting room; LEFT-knee worn refs W-L-FRONT/REAR/BENT
  (sent as nano_banana_pro, Higgsfield job record says nano_banana_2 — flagged on the cards); act map 44 rows (8 TH, 4 MECH),
  angles.py PASS; wardrobe map; 51 cards on Current; docs locations/actmap/wardrobe on Plan + Current. Higgsfield 17,894 after.
- Same session ~20:10 UTC: user "THE HOUSE LOOKS SMALL AND COMPRESSED" → cause: v1 prompts asked for a narrow Victorian terrace hall + galley
  kitchen, framed through doorways. Rebuilt as a large Edwardian semi (wide hall/stairs, ~3 m ceilings, shot from inside each room, no-cramped
  negative): P0 v2 `176c5c39`, P1 v2 `d0eeaf2a`, P2 v2 `abc2c220` (both against P0 v2); v1s on the Old board. Layout unchanged, angles PASS. Higgsfield 17,879.75.

- Same session ~20:20 UTC: user "go ahead with the voice stage" (every avatar/plate/ref was Confirmed on the board). Step 1 frame D-VOICE-IMG
  (job edd8434b, reported nano_banana_2) → board To check. G1–G3 Kling calls written + preflighted (PASS but 'start image approved'). Enhanced VO text
  locked (verbatim PASS, 3,180 chars). **STOP: Kling 3.0 credits** (§5 CREDIT_CAP, no reroute). See voice/VOICE_SOURCE.md.

- ~20:30 UTC: user "USE KEI AI AS SUBSTITUTE FOR NOW" → ADJUST recorded in BUILD_SHEET (Mode & Model Lock): every Kling call routes through
  Kie `kling-3.0-omni/image-to-video` (same Kling 3.0 Omni, prompt ≤3,072) via `voice/kie_kling.py` (refuses without preflight PASS), until Kling
  is topped up. Kie 186,607.8 credits. G1–G3 preflight: only 'start image approved' left (D-VOICE-IMG still To check).

## Where it stands
- **Confirmed on the board:** D-DOC v2, P-PATIENT, P0–P2 v2, P3, W-L-FRONT/REAR/BENT.
- **Waiting on the user:** Confirm/Fix D-VOICE-IMG (Kling credits no longer block: Kie substitute).
- **Then straight through (§22U, no stop):** G1–G3 → voice_source.py → clone "Down" (elevenlabs_clone.py) → eleven_v4 ×4 (vo/tts_enhanced.txt)
  → split HK1/HK2/HK3/BODY → house cut → HeyGen Avatar V TH ×8 (motion prompt each) → E11 trim. Then hooks (step 6).
- Flags still open: F2, F4, F5 (claims, voiced as written), F8 (built left), F9 (natural pace).
