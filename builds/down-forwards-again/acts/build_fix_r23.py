#!/usr/bin/env python3
"""Step 7 · BR-10c image v7 (the user, 2026-10-01: "i need a new br10c"; board Fix note on v6: "IT SHOULD BE THE PATELLAR TENDON NOT THE KNEE CAP").
Diagnosis: v4–v6 all lit the kneecap. Their ~5,000-character prompts named the kneecap a dozen times (every "not on the kneecap" line), and the
model put the glow where the word sat. v6's framing is right and shows the tendon clearly — the pale cord from the kneecap's bottom down to
the shin bone. v7 is a short targeted edit of v6 (§6A: short, positive, the one thing it shows): that cord glows red, the round bone above
goes back to plain ivory, nothing else changes. HT11 (the named structure exactly)."""
import json, pathlib
here = pathlib.Path(__file__).parent
PROMPT = ("Edit the attached image. Keep everything exactly as it is — the knee close-up, the muscles, the bones, the colours, the light, the "
          "framing — and change only the glow. The round bone at the front of the knee becomes plain ivory like the other bones, with no red "
          "and no glow on it. The pale vertical cord directly below it — running down from the bottom of that round bone to the top of the shin "
          "bone, in the centre of the image — now glows bright red along its whole length, near-white at its core: it is the one bright red "
          "thing in the image. The soft red streaks in the thigh muscle above stay as they are and lead down to that cord. "
          "No glow on the round bone, no red ring around the knee, no text, no labels.")
OUT = {"BR-10c": dict(v=7, refs=["7ee32818-3189-488b-be89-608809d77e44"], prompt=PROMPT, model="nano_banana_pro")}
(here / "BR-10c.image.r23.prompt.txt").write_text(PROMPT); json.dump(OUT, open(here / "fix_r23.json", "w"), indent=1); print("BR-10c v7", len(PROMPT))
