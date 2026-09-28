"""Appendix A string lookup — strings are imported, never retyped."""
import re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
STD = (ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md").read_text()
_pat = re.compile(r"\*\*`([A-Z0-9\-\[\]]+)`\*\*[^\n]*\n(?:[^\n`]*\n)*?```\n(.*?)\n```", re.S)
STR = {}
for m in _pat.finditer(STD):
    STR.setdefault(m.group(1), m.group(2).strip())
def s(k): return STR[k]
sys.path.insert(0, str(ROOT / "products/stryde"))
if __name__ == "__main__":
    for k in sys.argv[1:]: print(f"== {k} ({len(STR.get(k,''))})\n{STR.get(k,'MISSING')}\n")
    if len(sys.argv) == 1: print(len(STR), sorted(STR)[:400])
