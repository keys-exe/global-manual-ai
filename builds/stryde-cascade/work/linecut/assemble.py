"""stryde-cascade only (user 2026-09-29: "the brolls stays even though the script line is done").
Runs the standard assemble.py with the hold rule off: a B-roll ends when its line ends. The 3 s
hold (HOLD) is disabled and the minimum on screen (MIN_FLASH) is 1.0 s, so no line's picture runs
over the next words. Everything else is the standard assemble.py. Not a system change (§34)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".claude/skills/ai-prompt-engineer/scripts"))
import assemble  # noqa: E402
assemble.HOLD = 0.0
assemble.MIN_FLASH = 1.0
if __name__ == "__main__":
    assemble.main()
