# Narrator VO — §22U steps 6–10 (stryde-identity)

**Clone (step 6–7):** done by API on the user's instruction ("clone the voice and generate the VO"), 2026-09-26 09:30 UTC.
`Identity-Narrator` · voice ID **`F5vpA7jC44a7w7td6GdQ`** · source `voice/Identity_clone_source.mp3` (41.27s) · background-noise removal on.
The name `Identity` was already on the account (Carol, `identity-callout-v2`, `bZKwARZ93x98MmNw9MTG`), so the suffix was added (§22U step 7).

**Text (step 8):** `script.lines` verbatim, tags only. Lock `tts_budget.py --script-lines`: **PASS** on HK1, HK2, HK3 and BODY
(the hook lines keep the script's quote marks; they are not spoken). Body 1,113 chars, rung 1 (full tagging), 8 tags.
Tags: hooks `[serious]`; body `[serious]` → `[confident]` (numbers) → `[warm]` / `[measured]` (the stress-register turn on
"Not because the arthritis has gone") → `[casual]` → `[building anticipation]` (offer) → `[sincere]` → `[gentle]`.

**TTS (step 9):** ElevenLabs connector, `eleven_v3`, 4 takes each. Flows: BODY `kWZLwIiKsVXE1o6lnplN` · HK1 `McNGpaB8c7KTL5Q2VAIB` ·
HK2 `txKDkP2aeydTxUO5AHhv` · HK3 `EqRsRhlnpdSqVxfUyQcM`. HK3 take 4 failed (account concurrency limit, 15), so HK3 has 3 takes.
Spend ≈ 4 × 1,113 + 8 × 85 + 3 × 98 ≈ 5,425 ElevenLabs credits.

## Body — checked against the script (medium.en transcript), then E11 trim

| Take | Raw | Words (1) | Gaps > 0.6s | After E11 trim | Verdict |
|---|---|---|---|---|---|
| **T1 `gjdy…`** | 77.52s · 129 wpm | ✓ | 14 | **59.90s** (−17.70s) · ~176 wpm · no gap > 0.4s · PASS | **Recommended master** |
| T2 `ACeF…` | 80.40s · 124 wpm | ✓ | 14 | 59.95s (−20.51s) · PASS | alternate |
| `Fuxv…` | 70.72s | ✗ "the arthritis **is** gone" | 12 | — | out on (1) |
| `h2Rk…` | 80.64s | ✗ "the arthritis **is** gone" | 17 | — | out on (1) |

All raw takes paused ~0.6–1.5s at every line break (124–141 wpm against `VOICE-NARR`'s ~185). The E11 trim
closes that air between words only — no word is touched — and brings the body to the reference's pace
(≈ 5s hook + 60s body, as the absorption forecast). The untrimmed files stay beside the trims.
`trim.py` got an audio-only path in this session (it assumed a video stream).

## Hooks — every take verbatim (small.en), no gaps

| Hook | Takes (s · wpm · F0) | Pick by measurement |
|---|---|---|
| HK1 | T1 3.92·236·114 · **T2 3.92·236·118** · T3 4.00·231·114 · T4 4.00·234·115 | T2 |
| HK2 | T1 4.32·229·115 · T2 4.32·233·113 · **T3 4.64·216·119** · T4 4.88·202·117 | T3 |
| HK3 | **T1 4.72·211·119** · T2 5.04·203·113 · T3 5.20·196·119 | T1 |

Seam: the body's opening line measures 116–119 Hz (T1/T2), the hooks 113–119 Hz — no pitch jump at hook → body.

**Step 10 (Manual): the user listens and picks** one body master and one take per hook (board, stage Voice). The picks
by measurement are above; accent and realism are the ear's call (unverified by instrument).
