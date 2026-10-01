### The family

One music family: an investigative documentary score — ticking, a low synth pulse, plucked and staccato strings — tense and curious, never sad (no slow sad piano, no sad cello). It turns warm and major the moment the product appears (R-03a, “She pulled up her pant leg”, 72.3 s) and stays positive to the end. Both hooks share the track (same length, same body). User 2026-10-01: “i want a new one investigation and change when the product shows not a sad”.

### The map

| Part | Lines | What the script is doing | Register | Cue in plain words | In – out (finished video) |
|---|---|---|---|---|---|
| Hook — the callout | “I'm 71…” → “Mama, when did that happen?” | opens a loop — the callout, the question | `MUS-OPEN` | true-crime investigation opening, ticking clock, low synth pulse, muted plucked strings, a question hanging, tension, not sadness | 0.0–10.9 s |
| Act 1 — the stairs backwards, the failed fixes | “Six weeks ago…” → “Nothing gave me my life back.” | the problem, the failed fixes | `MUS-EXPOSE` | investigation tension, pulsing low synth, staccato string ostinato, soft deep hits on the reveals, taut and suspenseful, never sad | 10.9–39.0 s |
| Act 2 — Loretta on the dance floor | “Then my grandbaby got married…” → “mine was past fixing.” | opens a loop — the callout, the question | `MUS-OPEN` | curiosity, the pulse continues, a questioning pizzicato motif, light suspense, clue-finding | 39.0–57.6 s |
| Act 3 — the kitchen table, the routine | “Loretta came to stay…” → “can I show you something?” | curiosity — the investigation closing in / how it works | `MUS-EDU` | the investigation closes in, pulse a little quicker, rising tension, on the edge of a discovery | 57.6–72.3 s |
| Act 3 — the strap appears | “She pulled up her pant leg…” → “walk down them stairs.” | the product appears — it works | `MUS-TURN` | the pulse keeps going without a break, a warm major chord blooms over it, bright curious piano figure joins, positive and intrigued | 72.3–88.8 s |
| Act 3 — I did. The first step | “I did.” → “Both feet. Forwards.” | the product appears — it works | `MUS-TURN` | full release, warm strings enter, major key, forward movement, uplifting | 88.8–100.1 s |
| Act 4 — why it works | “Everything else you tried…” → “Pain gone. Just like that.” | curiosity — the investigation closing in / how it works | `MUS-EDU` | confident and inquisitive, major key, clean steady pulse, bright piano arpeggio, explaining with a smile | 100.1–128.2 s |
| Acts 5–6 — the proof, the walk, the husband | “Over 200,000 people…” → “I said, ‘I know.’” | proof and the life back | `MUS-AFTER` | warm hopeful theme, major, strings, piano and light percussion with movement, dignified lift, the investigation motif now warm and resolved | 128.2–171.8 s |
| Act 7 — the name, the offer, her sister | “That was six weeks…” → “on her own.” | the name, the real thing vs copies, the offer | `MUS-OFFER` | confident steady pulse, a little brighter, the theme held calm, the final major chord sustained for the last four seconds, no early fade | 171.8–210.6 s |

### Reference vs script

The reference ad has no music bed (EG07). The user asked for music on this build (“use the new bgm update”), so a quiet bed runs under the voice: about 18 dB under in pauses, about 26 dB under while she speaks, dipping 4 dB more under the link, the price and the guarantee.

### Check

ElevenLabs Music. This cue took three compositions: the first new track went silent for 19 s near the end, the second stopped dead for 7 s at the strap reveal — both discarded; the third plays continuously. music.py check on the bed: LENGTH, ENERGY order (−17 dB before the strap, −13.7 from it, −9.7 in the proof), DROPOUT, VOCALS (none) pass. CLICK flags are the first note at 0.4 s and the tail fading after the video ends; TEMPO reads 60 BPM on every track — the estimator's floor, not trusted. The final chord is extended past her last line with a 1.5 s crossfade (work/music_bed.py).
