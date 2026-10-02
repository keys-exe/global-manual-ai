# stryde-the-impression — build notes

- **Task:** "A - VID | AI Drama VSL | TOF | Discovery Story | New | The Impression" — Drive `1myOChLFKSUBiQqn-Z5EoZ7ROwJ9sXeq2`
- **Run:** **Manual**, **Mode 4 — Realistic Film**, AI Drama VSL (§3B), 9:16, **British** (user: "run manual. british"). Seedance 2.5 on Kie at 720p (ingredients, takes). Standards V7.91.4.
- **Account:** GitHub `mike-sj` — not the owner (`keys-exe`): build work in `builds/` only, no system change, no lessons (CLAUDE.md, §34B).
- **Boards:** Current https://claude.ai/artifact/C7iJiu9zayETRq6wRpHERk · Old https://claude.ai/artifact/YHyjDG7UugdwLqpjL2Artq · Final https://claude.ai/artifact/7jESdNE8iA6sW9qtKVWMJr · Plan https://claude.ai/artifact/YR9p35toXVXK1EE1uPywym (owned by pldthomecamarinessur@gmail.com)
- **Hourly Fix check:** `trig_01QYbXK5CcpCVJ8G5fXhgBfx`, :43 UTC, bound to session_01CmSgGcenFywMTJj8JuGiaB.
- **Connectors (§5, `work/connectors.md`):** images Higgsfield (private workspace, 5,616.9 cr before), Seedance Kie (99,229.6 cr), voice/music ElevenLabs API, HeyGen API (unused — film). No Drive connector.

## State (2026-10-02)
- Steps 1–3 delivered (`BUILD_SHEET.md`): Absorption Sheet (inspo = Kivora "Sea Bass", 389 s, 156 shots, 165 wpm — the script is a scene-for-scene port), Film Look Sheet (`LOOK-IMPRESSION`, Alexa 35 + Cooke S4/i; `edit/LUT-IMPRESSION.cube` PASS), Visual Instruction Ledger VN01–VN38, phrase inventory L001–L115 (911 words), claims, Mode & Model Lock.
- **Nine cast sheets** on the Current board as To check (Sunburst 2k, 2.75 cr each, 24.75 cr): N-HAZEL, C1-ROY, C2-EMMA, C3-DAN, C4-OSCAR, C5-WENDY, X1-ASSISTANT, X2-MUM, X3-LOLLIPOP. **Waiting on the user's avatar decision** (§18B).
- Absorption and the connector map on the Plan board (`docs/absorption` not yet confirmed).
- Product: repo sheet V7.49.38 kept (Drive's V7.49.32 older); the 12 Drive images are identical to `products/stryde/stryde_refs/`.

- 2026-10-02 **Cast confirmed** (the user pressed Confirm on all nine on the board, then "CONFIRMED ALL PROCEED"); absorption confirmed. Flags applied as recommended (F11 bare knee in her nightdress, then trousers off screen; F10 banister on steps 1–2 only; F13 right knee; F15 no product in hand at the close; F12 one film).
- 2026-10-02 **Steps 4–5 delivered** (`STEP4_5.md`):
  - Property Sheet: a Victorian gritstone terrace on a West Yorkshire hill.
  - **9 plates** (16:9 Sunburst, 2.75 cr each, 24.75 cr): P-HOUSE first, then L-STAIRS, L-DINING, L-KITCHEN and L-BEDROOM built against it, plus L-CHEMIST, L-HILL, L-GATE and L-CAR. All To check on the Current board.
  - The plan, all checks PASS: the act map (`step5/act_map.json`, 148 shots in 16 scenes) and **52 Seedance takes** (`takes.py`); `angles.py`; the wardrobe map with 11 story days (`wardrobe.py`); the Visual Pitch (`visual_plan.py`; hook concept A, 12/12); the Music Register Map (MUS-TURN on SC09-SH13, Wendy's hem); ingredients per take.
  - Docs on the Plan board, and on Current as text: property, actmap, takes, wardrobe, visualplan, music, ingredients.
  - Estimated run time ~8:00 (the inspo is 6:29). Seedance ≈ 506 s × 63 ≈ 31,900 Kie cr for one pass.
- **19 outfit cards** (OUT-<person>-<day>) and the info cards (INFO-WORN-WENDY, INFO-SEAT) are made scene by scene as each scene starts. The 9 §24I voice masters come next.

- 2026-10-02 **Plates confirmed** on the board, then "CONFIRMED ALL PROCEED".
- **Voice stage (§24I):** 9 neutral voice masters on Kie Seedance 2.5 (`voice/build_masters.py`, preflight PASS). Each is 2–3 plain script lines read back to back, 10–15 s clips (7,245 Kie cr), from a face crop of the confirmed sheet. The audio is stream-copied, untouched (`voice/<k>_voice_master.m4a`; an mp3 copy for Kie). All 9 are on the Current board **To check** (`VOICE-<k>`, audio cards).
  - Kie caps a call's reference audio at 30 s in total. On three-speaker takes each master goes in as its first ~10 s, cut at a pause (`voice/<k>_voice_ref10.mp3`); the masters stay untouched.
- **Hook A (SC01) written:** 5 Seedance takes in `film/SC01/` (`film/lib.py` + `film/build_sc01.py`, all preflight PASS). Each prompt carries a fixed dining-room geography block, the seats, and THE EXCHANGE in order, with one voice master per speaker. 48 s ≈ 3,000 Kie cr. They're on the board as `ready`, waiting for the voice masters' Confirm. D1 outfits are the sheets', so there are no outfit cards for Hook A.
- New V7.92.0 rule: every Seedance clip goes through `unmusic.py --check` the turn it lands (torch CPU installed this session).

- 2026-10-02 **Voices confirmed** ("CONFIRMED ALL PROCEED"), so all 9 voices are locked.
- **Hook A (SC01) v1 rendered:** 5 Kie Seedance takes, 48.3 s, 3,024 Kie cr (T1 630, T2 693, T3 882, T4 567, T5 252). `unmusic.py --check`:
  - T1, T2, T3 and T5 came back CLEAN.
  - **T4 had MUSIC** (−23.6 dB of the mix). It was cleaned with `unmusic.py`: v2 re-checks CLEAN, voice and effects kept, 0 cr. The v1 with music went to the Old board.
  - All 5 are on the Current board **To check**. Kie balance is 84,116.6.

- 2026-10-02 **Hook A consistency Fix** (user, chat: "make the hook consistent review the script guide"). Seen in the v1 frames:
  - The table changed: food in T1/T4, cleared in T2, Roy eating in T4. The script says "the table cleared".
  - The seats moved in every wide shot.
  - Oscar's route differed: across the front of the table in T1, down the far side in T2.
  - Hazel's background changed: the window, then bookshelves.
  - My ROOM block had 3 chairs on one side, while the plate has 2 per side plus the ends.
  - **Fix:** layout card `INFO-TABLE-SC01` (the cleared table from above, Sunburst edit-ref of L-DINING, 2.75 cr), now on the board To check. The take prompts were rewritten as gen 2 (all preflight PASS):
    - the seats tied to the plate (Hazel at the far end; Emma and Oscar on the sideboard side; Roy and Dan on the fireplace side; the near-end chair empty);
    - what is behind each person, named;
    - the table fixed: empty plates, glasses, one jug, no food;
    - Oscar's one route along the sideboard;
    - the card attached to every take.
  - SC01-T1…T5 are on `regenerate` and are sent once the card is confirmed. Each v1 moves to Old when its v2 lands.

## Open (Flags in BUILD_SHEET.md)
F1 price (£30 for two) · F2 "two centimetres" · F3 "replace them at seventy-one" · F6 "Facebook copies" · F7 getstryde.co · F11 strap on under trousers vs FP13 (proposed: bare knee in her nightdress, trousers on after) · F12 one hook → one film · F15 close without the product in hand.

## Next
Hook A gate (§18 step 6): the user's Confirm or Fix on SC01-T1…T5. Then SC02 (the hall film, D1 night), then the body scene by scene. Done before this: the §24I voice masters (9 speakers, Seedance, from face crops of the sheets) → Hook A (SC01, 5 takes: the D1 outfits are all the cast sheets', so no outfit cards; ingredients C4/C3/C2/C1/N + L-DINING + P-HOUSE + the voice masters). After that, the body scene by scene. ~~Steps 4–5 (Property Sheet — Hazel & Roy's stone terrace: dining room, hall kitchen→door, stairs, kitchen, bedroom — + 16:9 plates; the chemist, the hill + postbox, the school gate, Emma's car; scene list + Scene Bibles, act map with takes, wardrobe map per story day, ingredient lists, `angles.py` / `takes.py` / `wardrobe.py` / `visual_plan.py`), then §24I voice masters, then Hook A on Seedance.~~

## For the owner
- Add this build's row to the CLAUDE.md board table (this account can't change CLAUDE.md): `stryde-the-impression` (STRYDE · The Impression, AI Drama VSL, Mode 4, Manual, British — Drive `1myOChLFKSUBiQqn-Z5EoZ7ROwJ9sXeq2`) | Current https://claude.ai/artifact/C7iJiu9zayETRq6wRpHERk · Old https://claude.ai/artifact/YHyjDG7UugdwLqpjL2Artq · Final https://claude.ai/artifact/7jESdNE8iA6sW9qtKVWMJr · Plan https://claude.ai/artifact/YR9p35toXVXK1EE1uPywym; hourly Fix check `trig_01QYbXK5CcpCVJ8G5fXhgBfx`, :43 UTC, session_01CmSgGcenFywMTJj8JuGiaB.
- `takes.py` SPLIT check: `split: "length"` fails whenever two takes together have ≤ 4 shots, even when they run over 15 s (it counts shots, not seconds — L51 says "length means the running time over 15 s"). On this build that forced extra coverage rows: SC04-SH09, SC09-SH17b, SC09-SH20, and the close cut into 14 phrase shots. Suggest the check also allows "length" when the joined seconds exceed `--max-seconds`.
