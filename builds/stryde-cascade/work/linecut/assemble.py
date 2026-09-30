"""stryde-cascade only (user 2026-09-29: "the brolls stays even though the script line is done",
then "the broll placements are so bad not timed on the right start and end of the script line").
Runs the standard assemble.py with, for this build only (not a system change, §34):
- HOLD off and MIN_FLASH 1.0 s: a B-roll ends when its line ends;
- word timings from medium.en (base.en ended words 0.1-0.4 s early and missed some line starts
  by up to 0.7 s);
- each word's end moved to where its sound actually stops (20 ms level falls under -38 dBFS),
  never past the next word's start, so a cut never lands on a word still sounding."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".claude/skills/ai-prompt-engineer/scripts"))
import subprocess  # noqa: E402
import numpy as np  # noqa: E402
import assemble  # noqa: E402

assemble.HOLD = 0.0
assemble.MIN_FLASH = 1.0
SR, WIN, FLOOR_DB, MAX_EXT = 16000, 320, -38.0, 0.5
_words = assemble.words


def _levels(path):
    raw = subprocess.run([assemble.FF, "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32)
    n = len(x) // WIN
    return 20 * np.log10(np.sqrt((x[:n * WIN].reshape(n, WIN) ** 2).mean(1)) + 1e-9)


def words(path, model):
    ws = _words(path, "medium.en")
    db = _levels(path)
    out = []
    for i, (s, e, w) in enumerate(ws):
        nxt = ws[i + 1][0] if i + 1 < len(ws) else e + MAX_EXT
        k = int(e * SR / WIN)
        stop = int(min(nxt, e + MAX_EXT) * SR / WIN)
        while k < min(stop, len(db)) and db[k] > FLOOR_DB:
            k += 1
        out.append((s, max(e, min(k * WIN / SR, nxt)), w))
    return out


assemble.words = words
if __name__ == "__main__":
    assemble.main()
