"""Hook SC01 (story day D1, the garden-centre car park) — outfit cards for the Seedance takes (HT26, §24O rule 9).
Tony's and Sue's D1 clothes differ from their sheets, so each goes into the takes as a face-and-hair crop of the confirmed
sheet (voice/<id>_face.jpg) plus this outfit card. The lad wears his sheet's uniform on D1: his sheet goes in whole.
Sunburst image-to-image on Kie (the build's image model, §18A), Image 1 = the face crop; one render each (count 1)."""
import json
from pathlib import Path

H = Path(__file__).parent
B = H.parents[2]
CAM = ("Photographed as a single frame from a US feature film, shot on an ARRI Alexa Mini LF in large format with an ARRI Signature Prime at 50mm and T4, "
       "the camera on a locked tripod at standing eye height, composed natively for a vertical 9:16 frame with no letterbox bars.")
CARDS = {
 "OUT-C1-D1": dict(face="voice/C1_face.jpg", who="the man", pr="He", pos="his",
   id_="copy his face, age, thick salt-and-pepper hair with its left parting, the crooked nose and the short white scar through his left eyebrow exactly; he is a broad, heavy-shouldered builder of sixty-four with a slight stoop",
   wear=("his ordinary Saturday clothes: a plain charcoal-grey crew-neck cotton sweatshirt with ribbed cuffs pulled down to the wrists (no logo), "
         "faded navy cotton work trousers that reach his boots so both knees are covered, a worn brown leather belt, and worn tan leather lace-up work boots"),
   nots="no shorts, no bare knees, no navy sweatshirt with pushed-up sleeves, no grey T-shirt showing, no knee support, no hat, no watch showing",
   cap="TONY · Day D1 (Saturday, the garden centre): charcoal sweatshirt, navy work trousers, tan boots"),
 "OUT-C2-D1": dict(face="voice/C2_face.jpg", who="the woman", pr="She", pos="her",
   id_="copy her face, age, honey-blonde jaw-length bob with its long side-swept fringe, light-blue eyes and the small pale scar on her chin exactly; she is a tall, lean, upright woman of fifty-two",
   wear=("her ordinary Saturday clothes: a navy quilted short jacket with a stand collar and a front zip, worn open, over a plain white crew-neck T-shirt, "
         "light-wash straight-leg blue jeans, and plain white low trainers"),
   nots="no camel coat, no roll-neck, no black trousers, no ankle boots, no handbag, no scarf, no sunglasses",
   cap="SUE · Day D1 (Saturday, the garden centre): navy quilted jacket, white tee, light jeans, white trainers"),
}


def prompt(c):
    return (f"{CAM} An outfit reference card for one story day: Image 1 is {c['who']}'s face and hair only — {c['id_']}. "
            f"{c['pr']} stands full length, dead centre, facing the camera, arms relaxed at {c['pos']} sides, against a plain seamless mid-grey studio backdrop in soft even daylight from the left, "
            "the whole figure from hair to shoes inside the frame and filling about two-thirds of its height. "
            f"{c['pr']} wears, and only these, {c['wear']}. Nothing else is worn or carried. "
            f"Across the bottom of the card, on a plain white strip below the figure, one caption line in small black sans-serif text: \"{c['cap']}\". "
            f"Negatives: {c['nots']}, no other people, no props, no set, no logos or lettering on the clothing, no text other than the caption.")


if __name__ == "__main__":
    for k, c in CARDS.items():
        p = prompt(c)
        (H / f"{k}.prompt.txt").write_text(p)
        (H / f"{k}.call.json").write_text(json.dumps({"beat": k, "build": "stryde-her-dad", "kind": "image", "connector": "kie",
            "model": "gpt-image-2-5-sunburst-image-to-image", "aspect_ratio": "9:16", "refs": [c["face"]], "prompt": p}, indent=1, ensure_ascii=False))
        print(k, len(p))
