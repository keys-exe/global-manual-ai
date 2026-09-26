# Narrator VO — §22U steps 6–10 (stryde-identity)

**Clone (steps 6–7):** by API on the user's instruction, 2026-09-26 09:30 UTC. `Identity-Narrator` · voice ID
**`F5vpA7jC44a7w7td6GdQ`** · source `voice/Identity_clone_source.mp3` (41.27s) · background-noise removal on.
`Identity` was already on the account (Carol, `identity-callout-v2`), so the suffix was added (§22U step 7).

## One-go VO (user's instruction, 2026-09-26 09:47 UTC)

"Generate it in one go, all hooks and body, for consistent voice-over, then trim them. Delete the previous ones."
The first round (hooks and body as separate requests) was deleted from the board, the build tree and ElevenLabs history.

**Text (step 8):** `ALL.tagged.txt` = HK1, HK2, HK3, body, in script order, one request. Lock against the whole
`script.lines`: **PASS** · 1,354 chars · rung 1 · 8 tags (`[serious]` opens; body tags as before, its opening
`[serious]` dropped because HK1's already sets it).

**TTS (step 9):** ElevenLabs connector, `eleven_v3`, 4 takes, flow `tEAVkrzG6BhDg0yzhlqU` (≈ 5,416 credits).

**Split** (`split_vo.py`): medium.en word timestamps on each full take → cut in the middle of the silence after
"bone." / "work." / "anymore." → `HK1` `HK2` `HK3` `BODY`. **Trim** (E11, `trim.py`): every piece, air between words only.

| Take | History id | Full | HK1 | HK2 | HK3 | Body (trimmed) | Words |
|---|---|---|---|---|---|---|---|
| T1 | `2baqdPMjT7hW66E19TDG` | 77.28s | 3.92 | 3.87 | 4.34 | 50.34s · ~210 wpm | ✓ |
| **T2** | `3oxVQwX6A3skqRLYMczK` | 80.16s | 3.97 | 4.18 | 4.41 | **53.08s · ~199 wpm** | ✓ |
| T3 | `H8WKX1YAAElMu9TLyHzF` | 79.28s | 3.87 | 3.79 | 4.02 | 50.96s · ~207 wpm | ✓ |
| T4 | `ZzBlBJ4fBT3haBAlh0Rp` | 82.56s | 3.89 | 4.21 | 4.26 | 53.32s · ~198 wpm | ✓ |

Words: every take has every word in order — checked on the full take (medium.en) and again on each trimmed piece;
the two small-model doubts (T2 "has gone", T1 "feet all day") were re-read with medium.en beam 5 and are correct.
All 16 trims PASS E1 (entry ≤ cap, tail ≤ cap, no gap > 0.4s).

**Recommended: T2** — pace closest to the reference's 191 wpm, and every word read cleanly by both models.
T4 is the same pace; T1/T3 run faster (~207–210 wpm). Each variant = HKn + BODY of the **same take**, so the
voice is identical across the seam.

**Step 10 (Manual): the user listens and picks the take** (board → Voice, cards `VO-T<n>-<part>`). Accent and
realism are the ear's call (unverified by instrument).
