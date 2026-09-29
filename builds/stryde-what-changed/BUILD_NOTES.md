# Build notes — stryde-what-changed (STRYDE · What Changed, podcast, Manual)

Read this first when resuming. Build Sheet: `BUILD_SHEET.md` (steps 1–3).

## Intake
- **Drive task folder:** https://drive.google.com/drive/folders/1zFGMzZ-olam9tpD63hM5MvHlUMkUVHKW
- User message: "RUN MANUAL. BRITISH" → RUN: MANUAL, VOICE: British. MODE blank → Mode 1. HOOKS → 3 in script (A/B/C) + one shared body → 3 videos.
- Script file had no extension (Word 2007+) → `intake/script.docx`; spoken lines `work/script_lines.txt`, per part `work/script_{HK1,HK2,HK3,BODY}.txt`
  (the "A —" / "B —" labels and the hook quotation marks removed by hand; no spoken word touched).
- Product Sheet in the folder is V7.49.29; the repo's V7.49.37 is used.
- **Boards (account iamnotkeysi@gmail.com):** Current https://claude.ai/artifact/3uy6935ZTAivEZgysENYvq · Old https://claude.ai/artifact/T3RZo3ak1QfC2ue6yaV9LD · Final https://claude.ai/artifact/6aiYxibqFq5F9R8tMiqp2z · Plan https://claude.ai/artifact/SGxFerhs4WKGiy3uV5bh8R

## Sessions
- session_01F5f9WBysAi6Tgspjop271s (2026-09-29 11:20 UTC): steps 1–3. Inspo measured (195.5s, 115 shots, 176 wpm, host ~55% on camera,
  cut-out PiP on most B-roll), absorption, ledger (VN01 = hook line 1 as VO over B-roll), phrase inventory, claims (F2–F11), Mode & Model Lock.
  Cast: H-HOST, R1-MAUREEN, R2-DESMOND (landed 11:50, board To check) on Higgsfield (Sunburst, 2k, one each; R2's first call returned 503 before starting, sent once more).
  Higgsfield 17,537 credits before the cast. Four boards made; docs/absorption on Plan + Current.

- 12:08 UTC hourly Fix check: H-HOST Fix "change host avatar to more attractive or have pleasing personality" → v2 (job b9242d45…, Sunburst):
  attractive/warm face fill, 44, `NEG-DEFAULT-FACE` without "catalogue-model bone structure" and its last two clauses, "unflattering" dropped
  from `SKIN-T` (H only; §34 correction for this sheet, `cast/build_sheets.py` `host=True`). v1 moved to Old (asset 10c81baa…), deleted from Current.

- 12:25 UTC user "fix": H-HOST Fix "change the host, i want different person have pleasing personlaity" → v3 (job e6a49b97…): a new person —
  white British woman, 41, honey-blonde, freckles, beauty mark, cream cable-knit; same warm face register as v2. v2 moved to Old (asset 700dc380…).

- 12:45 UTC user "I'VE CONFIRM PROCEED": H-HOST v3, R1, R2 confirmed (flags unanswered → voiced as written, open).
  Steps 4–5: plates P0-STUDIO, P1-PROP-M, P2-PROP-D, P3-STREET, P4-KITCHEN, P5-CONSULT (Sunburst 16:9) + S1-SURGEON sheet (§19B)
  + H-VOICE-IMG (§22U step 1, nano_banana_pro requested, logged nano_banana_2) → board To check. Act map `work/actmap.py`
  (61 rows: 44 B-roll + 17 TH; pip on B06, B12, B20; `angles.py` PASS HK1–HK3), wardrobe map, `STEP4_5.md`; docs/locations,
  docs/actmap, docs/wardrobe on Plan + Current; 44 planned beat cards. Kling takes G1/G2 built (`voice/H_G*.kling.json`, 2,441 / 2,417).

- 13:00 UTC user "fix those": board → all 6 plates + S1-SURGEON confirmed; H-VOICE-IMG Fix "medium shot only, not too wide" →
  v2 (job bccb1cd0…, waist-up, face ~¼ frame height, no knees/legs; nano_banana_pro requested, logged nano_banana_2). v1 to Old (asset 0b58b0a8…).

## Where it stands
- **Waiting on the user:** Confirm/Fix **H-VOICE-IMG v2** (the voice starts on its Confirm, §22X). Plates and S1 confirmed.
- Next: Kling G1/G2 (`preflight.py` first) → `voice_source.py` → `elevenlabs_clone.py` (name `Changed`) → Enhance → one v4 request
  HK1+HK2+HK3+BODY (`tts_api.py`) → HeyGen Avatar V on the untrimmed take → `cut_points.py` + `trim.py`. Then Hook 1 images.
- Open flags: F2, F3, F5, F6, F8, F9, F11 (claims).
