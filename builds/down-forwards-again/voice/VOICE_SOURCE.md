# Doctor voice source — §22U steps 1–8 (down-forwards-again)

## Step 1 — talking-head frame
- Prompt `D_step1_image.prompt.txt` (9,624 chars), built by `build_voice.py` from Appendix A by ID (`CAM-LOCK`, `FRAME-SCALE` + `FRAME-PROPPED`,
  `APPROACH-PRO` (§19B), `LIGHT-SHOT` from the P3 light plan: north window, screen-left, `SKIN-B1/B3/B4`, `EYES-A`, `HAIR-A`, `NECK-A`, `TEETH-A`,
  `CAP-A`, `CAP-FILE`, negatives incl. `NEG-LIGHT`). Attached: D-DOC v2 (`71b20c5a…`) and P3 (`757817ea…`), both confirmed.
- Render: job `edd8434b-4ebe-463a-bb3d-ea88efbb129e`, 1536×2752, `D_step1_v1.png` (board asset `da9e90d5d31d61c330afe1d96b6b9fc4`).
  **Routing note:** requested `nano_banana_pro`; the job reports `nano_banana_2` (same mismatch as the W-L refs). Recorded, not rerolled. The check is yours.
- This frame is also the HeyGen avatar image (§22U step 11). **Rig note:** TH is `FRAME-PROPPED` / `RIG-R3C` (the §22U default for VSL talking heads) — the phone propped on his desk, not a tripod.

## Step 2 — Kling takes (written, preflighted, NOT SENT — Kling has 3 credits)
| Take | Line (verbatim, HK1) | Words | JSON chars | Preflight |
|---|---|---|---|---|
| G1 | In six weeks, this woman stopped coming down her own stairs backwards. | 12 | 2,479 | PASS except "start image approved" |
| G2 | Without an operation. Without another course of physio. Without one more brace going in the drawer. | 16 | 2,496 | PASS except "start image approved" |
| G3 | And here is how you can do that too. | 9 | 2,407 | PASS except "start image approved" |

`kling-video-v3_0_omni`, `image_1` = the step-1 frame, 9:16, 1080p, 10s, `enable_audio: true`, `prefer_multi_shots: false`, one generation per call.
§37 TH ladder to fit 2,500 (first pass 2,629–2,695): step 1 selected negatives (dropped `no shape shifting`, `no merging`, `no splitting`,
`no texture swimming`, `no smearing`, `no shadows sliding`, `no light following the subject`), step 3 room clause → "Phone a metre away.",
step 4 per-take delivery note tightened and "Not a narrator, not an advert." dropped (VOICE-DOC already says "Never a newsreader, never a salesman").
`VOICE-DOC`, `AUD-A` and `MOUTH-C` are whole.

**STOP — E2 `CREDIT_CAP` (§5: "Kling out of credits … is a stop, never a silent reroute").** Kling balance 3.0; three 10s takes need ~360.

## Step 8 — Enhance + lock (done)
`../vo/tts_enhanced.txt` = HK1, HK2, HK3, body in script order, one request. Lock against `../vo/all.lines.txt`: **verbatim PASS**, 3,180 chars,
rung 1, 15 tags (none unknown, none banned), emphasis: SIX, YOU, NOT ×2, THAT, MOVE.

## Then, straight through once Kling is topped up and the frame is confirmed
G1–G3 → `voice_source.py D_G1.mp4 D_G2.mp4 D_G3.mp4 --name Down` (same-voice gate) → `elevenlabs_clone.py clone` (name **Down**, from the title
"Down Forwards Again"; ElevenLabs check PASS, 517 free slots) → `eleven_v4` TTS, 4 takes → split HK1/HK2/HK3/BODY → house cut → HeyGen Avatar V
talking heads for the 8 TH segments (motion prompt on each) → E11 trim.
