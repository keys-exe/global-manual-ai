"""stryde-cascade only: the standard variants.py, calling work/linecut/assemble.py (B-roll ends with its line)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[4] / ".claude/skills/ai-prompt-engineer/scripts"))
import variants  # noqa: E402
variants.HERE = Path(__file__).resolve().parent
if __name__ == "__main__":
    variants.main()
