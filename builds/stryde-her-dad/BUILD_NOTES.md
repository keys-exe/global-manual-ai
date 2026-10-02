# stryde-her-dad — build notes

- **Task:** "A - VID | AI Drama VSL | TOF | Discovery Story | New | Her Dad" — Drive `1HiQYsCmreGmcdUU2a-HF0hmxW68gFfz8`
- **Run:** **Manual**, **Mode 4 — Realistic Film** (the script: "AI Drama VSL, photoreal, like a short film" — F0), AI Drama VSL (§3B), 9:16, Seedance 2.5 on Kie at 720p. Standards V7.91.3.
- **Account:** GitHub `mike-sj` (a collaborator, not `keys-exe`) → build work only under `builds/`; no system change, no lesson (CLAUDE.md, §34B).
- **Boards:** Current https://claude.ai/artifact/Ki6d6eeXAgujWT1vAKTu8B · Old https://claude.ai/artifact/KnhxtqiFtKW7x4AJXdDtmQ · Final https://claude.ai/artifact/FTaYbfPdGNzgvtW7H5D3V9 · Plan https://claude.ai/artifact/GGfqqXJgZNEKzVmicQv5Ps (template V7.91.3, `capabilities: {db, assets, downloads}`)
- **Hourly Fix check:** `trig_01GJT8uYDNJMUpSnfjBcTu7q`, :32 UTC, bound to session_01AXsRKuUk5KWYVjQ5Jv5TB4.
- **Connectors (§5):** `work/connectors.md` — images Higgsfield (private workspace, Max), Seedance Kie API, voice/music/SFX ElevenLabs API; all default except SFX (ElevenLabs API, rung 2) and Drive (public link). Talking heads not used (film).

## State (2026-10-02)
- Steps 1–3 delivered (`BUILD_SHEET.md`): intake, Absorption Sheet (the Lymphoria drama, a line-for-line port), Film Look Sheet (`LOOK-HERDAD`, `edit/LUT-HERDAD.cube` PASS), Edit Grammar EG01–EG07, Visual Instruction Ledger VN01–VN20, phrase inventory L001–L061 (702 words), claims, Mode & Model Lock.
- Cast: 5 sheets on the Current board as To check — C1-TONY, C2-SUE, C3-GARY, C4-LAD, C5-GP (Sunburst high 2k, 2.75 cr each, 13.75 total; Higgsfield 5,869.65 → 5,855.90). Prompts `cast/*.prompt.txt`, builder `cast/build_sheets.py`.
- **2026-10-02, avatars:** C1-TONY, C3-GARY, C4-LAD, C5-GP **confirmed**. C2-SUE Fix "change the avatar" → v2, a new person (honey-blonde jaw bob, camel coat; job `1ad76bc3…`, 2.75 cr; Higgsfield → 5,853.15) on the board To check; v1 moved to Old (asset `22c7d900…`), its file deleted from Current.
- **2026-10-02, "confirm and proceed":** Sue v2 confirmed (on the board by the user); F0–F5 run on the recommendations (Mode 4, one hook → one film, a separate male narrator, claims voiced as written).
- **Steps 4–5 delivered (`STEP4_5.md`):** Property Sheet P-HOUSE + 9 Location Sheets; **10 plates** (Sunburst 16:9 2k, 2.75 cr each = 27.50; the three house rooms made with P-HOUSE attached) on the Current board To check — jobs `plates/jobs.json`. Act map `step5/act_map.json` (89 shots, 10 scenes, **35 takes**; `angles.py` PASS, `takes.py` PASS), wardrobe per story day D1–D9 (`wardrobe.py` PASS), Visual Pitch (`visual_plan.py` PASS), Music Register Map (product's first frame SC05-SH21 ≈ 3:40). Plan docs on the Plan board and Current (text): locations, actmap, takes, wardrobe, visualplan, music. Planned shot time 5:38.
- Higgsfield balance 5,755.65 at 16:12 UTC — other work on the same account also spends from it (Nano Banana Pro charges that aren't this build's).
- **Waiting on the user:** Confirm / Fix the 10 plates. Then: §24I voice masters (Tony, Sue, Gary, the Lad, the GP, labourer, neighbour, offer narrator), then the hook SC01 (takes SC01-T1…T3) on Seedance.

## Next
Steps 4–5 on the go: Property Sheet + plates (16:9) — the terraced house (stairs, bedroom drawer, kitchen, back garden), the garden-centre car park (one plate for SC01 and SC09), the car interior, the GP's room, the builders' yard, the street; act map with takes (`takes.py`), wardrobe per story day (`wardrobe.py`), Visual Pitch (`visual_plan.py`), music register map (§40A), placement; then the §24I voice masters; then the hook.

## For the owner (keys-exe)
- Add this build's row to the CLAUDE.md board table: `stryde-her-dad` (STRYDE · Her Dad, AI Drama VSL, Mode 4, Manual — Drive `1HiQYsCmreGmcdUU2a-HF0hmxW68gFfz8`) | Current https://claude.ai/artifact/Ki6d6eeXAgujWT1vAKTu8B · Old https://claude.ai/artifact/KnhxtqiFtKW7x4AJXdDtmQ · Final https://claude.ai/artifact/FTaYbfPdGNzgvtW7H5D3V9 · Plan https://claude.ai/artifact/GGfqqXJgZNEKzVmicQv5Ps; and its Fix check: `trig_01GJT8uYDNJMUpSnfjBcTu7q`, :32 UTC, session_01AXsRKuUk5KWYVjQ5Jv5TB4.
- The Drive folder carries a new product photo, `intake/831541848_1776104753638147_6983687178981367124_n.png` — a studio back view of the closed strap (grey grooved pad, chrome slides, band and two keepers). It may belong in `products/stryde/stryde_refs/` beside `back_ref_v2_band.png`; not added from this account.
- `takes.py` SPLIT check: for `split: "length"` it counts only shots (`len(a)+len(b) <= max_shots`), so two takes that together run over 15 s still fail when they hold ≤ 4 shots. It should also compare the summed `duration` with `--max-seconds`. Worked around here by breaking long monologues into coverage.
- The supplied Product Sheet is V7.49.32 (older than the repo's V7.49.38); the repo's was used.
