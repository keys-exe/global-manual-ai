### The family

One family, two pieces (V7.78.0): the investigation — ticking, a low synth pulse, plucked and staccato strings, single piano notes; tense and curious, never sad — runs until the product's first frame. The product first shows at R-03a (“…something? She pulled up her pant leg”, the strap revealed) at **70.4 s** (cut 7: every B-roll now cuts on its line's first word, so R-03a starts 1.9 s earlier) in the finished video — nothing before it shows the strap (the hooks and T-02a have it hidden). On that frame the music changes: after a one-second held breath, a full warm major chord lands (70.41 s), and the same instruments carry on warm and hopeful to the end. Both hooks share the track.

### The map

| Part | Lines | Register | Cue in plain words | In – out (finished video) |
|---|---|---|---|---|
| Hook — the callout | “I'm 71…” → “Mama, when did that happen?” | `MUS-OPEN` | true-crime investigation opening, ticking clock, low synth pulse, muted plucked strings, a question hanging, tension, not sadness | 0.0–10.9 s |
| Act 1 — the stairs backwards, the failed fixes | “Six weeks ago…” → “Nothing gave me my life back.” | `MUS-EXPOSE` | investigation tension, pulsing low synth, staccato string ostinato, soft deep hits on the reveals, taut and suspenseful | 10.9–39.0 s |
| Act 2 — Loretta on the dance floor | “Then my grandbaby got married…” → “mine was past fixing.” | `MUS-OPEN` | curiosity, the pulse continues, a questioning pizzicato motif, light suspense, clue-finding | 39.0–57.6 s |
| Act 3 — the kitchen table, the routine | “Loretta came to stay…” → “Baby, can I show you…” | `MUS-EDU` | the investigation closes in, pulse a little quicker, rising tension, thinning to almost nothing in the last second, as if holding its breath | 57.6–70.4 s |
| The strap appears — the change | “…something? She pulled up her pant leg…” (R-03a, the strap's first frame) → “walk down them stairs.” | `MUS-TURN` | opens on the very first beat with a full warm major chord — strings, piano and the pulse together, bright, hopeful, curious, clearly a new key from the first second | 70.4–88.8 s |
| Act 3 — I did. The first step | “I did.” → “Both feet. Forwards.” | `MUS-TURN` | full release, warm strings enter, major key, forward movement, uplifting | 88.8–100.1 s |
| Act 4 — why it works | “Everything else you tried…” → “Pain gone. Just like that.” | `MUS-TURN` | confident and warm, major key, clean steady pulse, bright piano figure, explaining with a smile | 100.1–128.2 s |
| Acts 5–6 — the proof, the walk, the husband | “Over 200,000 people…” → “I said, ‘I know.’” | `MUS-AFTER` | warm hopeful theme, major, strings, piano and light percussion with movement, dignified lift, the investigation motif now warm and resolved | 128.2–171.8 s |
| Act 7 — the name, the offer, her sister | “That was six weeks…” → “on her own.” | `MUS-OFFER` | confident steady pulse, a little brighter, the theme held calm, the final major chord sustained for the last four seconds, no early fade | 171.8–210.6 s |

### Reference vs script

The reference ad has no music bed (EG07); on the user's ask a quiet bed runs under the voice — about 18 dB under in pauses, about 26 dB while she speaks, 4 dB lower again under the link, the price and the guarantee.

### Check

ElevenLabs Music, two compositions (MUS-A investigation, MUS-B warm). A single 212 s track (earlier versions) never changed character at the product — the change was only a level step — so the two pieces are joined on the product frame by work/music_splice.py: A's last bars repeated so the investigation runs to 69.4 s; B placed so its first full chord (7.2 s into B) lands at 70.41 s (cut 7, `MUS-FINAL.v6.cue.json`, bed v6; cut 5–6 had 72.30 s); B's offer section repeated to cover her last line. music.py plan: PASS (the change on product_at 70.41 ± 0.25 s, nothing sad before it). music.py check on the bed: LENGTH, ENERGY order, DROPOUT, VOCALS (none) pass; TEMPO 66 BPM (slow). CLICK flags located: the first note at 0.4 s, the chord hit at 72.2 s, and B's pulse beats — none at a join.
