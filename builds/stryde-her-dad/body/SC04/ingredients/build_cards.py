"""Scene 4 (story day D3, the GP appointment) — Tony's outfit card for the Seedance takes (HT26). Same recipe as hooks/SC01/ingredients:
the face-and-hair crop of the confirmed sheet as Image 1, Sunburst image-to-image on Kie, one render. The GP wears her sheet's
work clothes on D3 (wardrobe map), so her sheet goes into the takes whole and needs no card."""
import json, importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[2]
_s = importlib.util.spec_from_file_location("c1", B / "hooks/SC01/ingredients/build_cards.py"); C1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(C1)
base = C1.CARDS
CARDS = {
 "OUT-C1-D3": dict(base["OUT-C1-D1"],
   wear=("his going-out clothes for a doctor's appointment: a plain navy zip-up fleece jacket with a stand collar, worn zipped halfway over a plain grey crew-neck T-shirt, "
         "dark-blue straight-leg jeans that reach his shoes so both knees are covered, a worn brown leather belt, and polished brown leather lace-up shoes"),
   nots="no shorts, no bare knees, no work boots, no sweatshirt, no work trousers, no knee support, no hat, no watch showing",
   cap="TONY · Day D3 (the GP appointment): navy zip fleece, grey T-shirt, dark jeans, brown leather shoes"),
}

# v2 (2026-10-03, board Fix, owner: "create another one"): a new render of the same D3 outfit. Read off v1 beside the confirmed D2 card:
# v1 drew him leaner and narrower in the shoulders than the D2 card's broad, heavy builder. v2 adds the confirmed D2 card as Image 2 —
# his face and build only, its clothes never worn — so he is the same man as on the other days.
D2_CARD = "body/SC03/ingredients/OUT-C1-D2_v1.png"
def prompt_v2(c):
    p = C1.prompt(c)
    return p.replace("Image 1 is the man's face and hair only — ",
        "Image 1 is the man's face and hair only, and Image 2 is the same man on another day, for his face and his build only — his clothes in Image 2 are never worn here — ").replace(
        "he is a broad, heavy-shouldered builder of sixty-four with a slight stoop",
        "he is a broad, heavy-shouldered builder of sixty-four with a thick chest, a solid middle and a slight stoop, exactly as heavy and broad as in Image 2")

if __name__ == "__main__" and "--v2" in __import__("sys").argv:
    for k, c in CARDS.items():
        p = prompt_v2(c)
        (H / f"{k}.v2.prompt.txt").write_text(p)
        (H / f"{k}.v2.call.json").write_text(json.dumps({"beat": k, "build": "stryde-her-dad", "kind": "image", "connector": "kie",
            "model": "gpt-image-2-5-sunburst-image-to-image", "aspect_ratio": "9:16", "refs": [c["face"], D2_CARD], "prompt": p,
            "fix_note": "create another one", "noteOwner": True}, indent=1, ensure_ascii=False))
        print(k, "v2", len(p))
elif __name__ == "__main__":
    for k, c in CARDS.items():
        p = C1.prompt(c)
        (H / f"{k}.prompt.txt").write_text(p)
        (H / f"{k}.call.json").write_text(json.dumps({"beat": k, "build": "stryde-her-dad", "kind": "image", "connector": "kie",
            "model": "gpt-image-2-5-sunburst-image-to-image", "aspect_ratio": "9:16", "refs": [c["face"]], "prompt": p}, indent=1, ensure_ascii=False))
        print(k, len(p))
