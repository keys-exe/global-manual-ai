"""Scene 5 (story day D4, the builders' yard) — outfit cards for the Seedance takes (HT26), the SC01 recipe: Sunburst image-to-image on Kie,
the face-and-hair crop of the confirmed sheet as Image 1, one render each. Tony takes his confirmed D2 card as Image 2 for his face and
build only (what made OUT-C1-D3 v2 right). Gary's D4 clothes differ from his sheet, and he wears the strap on his bare right knee all day,
so his card carries it from the supplied photo stryde_refs/worn_front.jpg (Image 2, the strap and its seat only)."""
import json, importlib.util
from pathlib import Path

H = Path(__file__).parent
B = H.parents[2]
_s = importlib.util.spec_from_file_location("c1", B / "hooks/SC01/ingredients/build_cards.py"); C1 = importlib.util.module_from_spec(_s); _s.loader.exec_module(C1)
D2_CARD = "body/SC03/ingredients/OUT-C1-D2_v1.png"
WORN = "../../products/stryde/stryde_refs/worn_front.jpg"
base = C1.CARDS
CARDS = {
 "OUT-C1-D4": dict(base["OUT-C1-D1"],
   wear=("his work clothes for the yard: a plain grey marl pullover hoodie with the hood down and the sleeves pushed to the forearm, khaki canvas work shorts "
         "ending just above the knee so both knees are bare, grey work socks and worn tan leather lace-up work boots"),
   nots="no long trousers, no covered knees, no knee support, no strap, no sweatshirt, no fleece, no jeans, no hat, no watch showing",
   cap="TONY · Day D4 (the builders' yard): grey marl hoodie, khaki work shorts, grey socks, tan work boots"),
 "OUT-C3-D4": dict(face="voice/C3_face.jpg", who="the man", pr="He", pos="his",
   id_=("copy his long lean face, strong hooked nose, sharp cheekbones, small bright pale-blue eyes under bushy white brows, thin mouth, short neat white beard, "
        "shaved tanned bald head and the small notch missing from the top rim of his right ear exactly; he is a tall, lean, wiry man of seventy, straight-backed, "
        "with long ropey arms and weathered skin over the knees"),
   wear=("his work clothes for the yard: a sand-coloured canvas work jacket worn open over a faded black crew-neck T-shirt, navy canvas work shorts ending just above "
         "the knee so both knees are bare, rolled grey socks and scuffed brown rigger boots; and on his bare RIGHT knee only, the knee strap exactly as in Image 2 — "
         "the black moulded shell across the front of the knee with its two rounded peaks and the concave notch between them, the bottom of his kneecap seated into "
         "the notch with no gap, the kneecap's face uncovered, the black woven band round the back of the leg, the small chrome slide at each end"),
   nots="no buffalo-check overshirt, no flannel shirt, no long trousers, no strap on the left knee, no strap above or over the kneecap, no extra brace or sleeve, no hat, no watch showing",
   cap="GARY · Day D4 (the builders' yard): sand canvas jacket, black T-shirt, navy work shorts, the strap on his right knee"),
}


def prompt(k, c):
    p = C1.prompt(c)
    if k == "OUT-C1-D4":
        return p.replace("Image 1 is the man's face and hair only — ",
            "Image 1 is the man's face and hair only, and Image 2 is the same man on another day, for his face and his build only — his clothes in Image 2 are never worn here — ").replace(
            "he is a broad, heavy-shouldered builder of sixty-four with a slight stoop",
            "he is a broad, heavy-shouldered builder of sixty-four with a thick chest, a solid middle and a slight stoop, exactly as heavy and broad as in Image 2")
    return p.replace("Image 1 is the man's face and hair only — ",
        "Image 1 is the man's face and hair only, and Image 2 is the knee strap and where it sits, for the strap only — the leg and shorts in Image 2 are never copied — ")


if __name__ == "__main__":
    for k, c in CARDS.items():
        p = prompt(k, c)
        refs = [c["face"], D2_CARD if k == "OUT-C1-D4" else WORN]
        (H / f"{k}.prompt.txt").write_text(p)
        (H / f"{k}.call.json").write_text(json.dumps({"beat": k, "build": "stryde-her-dad", "kind": "image", "connector": "kie",
            "model": "gpt-image-2-5-sunburst-image-to-image", "aspect_ratio": "9:16", "refs": refs, "prompt": p}, indent=1, ensure_ascii=False))
        print(k, len(p), refs)
