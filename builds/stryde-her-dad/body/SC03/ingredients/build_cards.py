"""Scene 3 (story day D2, a weekday at rock bottom) — outfit cards for the Seedance takes (HT26). Same recipe as hooks/SC01/ingredients:
the face-and-hair crop of the confirmed sheet as Image 1, Sunburst image-to-image on Kie, one render each."""
import json, importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[2]
_s = importlib.util.spec_from_file_location("c1", B / "hooks/SC01/ingredients/build_cards.py"); C1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(C1)
base = C1.CARDS
CARDS = {
 "OUT-C1-D2": dict(base["OUT-C1-D1"],
   wear=("his weekday work clothes: a plain olive-green crew-neck work sweatshirt with ribbed cuffs (no logo), grey cotton work trousers that reach his boots so both knees are covered, "
         "a worn black belt, and worn tan leather lace-up work boots"),
   nots="no shorts, no bare knees, no navy sweatshirt, no charcoal sweatshirt, no navy trousers, no knee support, no hat, no watch showing",
   cap="TONY · Day D2 (a weekday at rock bottom): olive work sweatshirt, grey work trousers, tan boots"),
 "OUT-C2-D2": dict(base["OUT-C2-D1"],
   wear=("her weekday clothes: a burgundy hip-length rain jacket with a hood down and a front zip, worn zipped halfway, a plain grey T-shirt under it, black slim jeans, and plain grey trainers"),
   nots="no camel coat, no navy quilted jacket, no light jeans, no white trainers, no handbag, no scarf, no sunglasses",
   cap="SUE · Day D2 (a weekday): burgundy rain jacket, black jeans, grey trainers"),
}

if __name__ == "__main__":
    for k, c in CARDS.items():
        p = C1.prompt(c)
        (H / f"{k}.prompt.txt").write_text(p)
        (H / f"{k}.call.json").write_text(json.dumps({"beat": k, "build": "stryde-her-dad", "kind": "image", "connector": "kie",
            "model": "gpt-image-2-5-sunburst-image-to-image", "aspect_ratio": "9:16", "refs": [c["face"]], "prompt": p}, indent=1, ensure_ascii=False))
        print(k, len(p))
