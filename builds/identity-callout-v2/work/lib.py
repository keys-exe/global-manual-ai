"""Build-local helpers: Appendix A strings by ID from the master file, product strings by import."""
import re, sys, json, importlib.util
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
MASTER = ROOT / "standards/AI_Prompt_Engineer_Global_Standards.md"
BUILD = Path(__file__).resolve().parents[1]
_txt = MASTER.read_text()

def A(sid):
    """Return the fenced block following **`SID`** in the master file."""
    m = re.search(r"\*\*`%s`\*\*[^\n]*\n\n?```[a-z]*\n(.*?)\n```" % re.escape(sid), _txt, re.S)
    if not m:
        raise KeyError(sid)
    return m.group(1).strip()

_spec = importlib.util.spec_from_file_location("ps", BUILD / "intake/stryde_product_sheet_v7_49_13.py")
P = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(P)
SIDE = "right"
def PS(name):
    return P.fill(P.S[name], side=SIDE)

def ncount(s):
    return len(s.replace("\n", ""))

if __name__ == "__main__":
    for sid in sys.argv[1:]:
        try: s = A(sid)
        except KeyError: s = PS(sid)
        print(f"--- {sid} ({ncount(s)})\n{s}\n")
