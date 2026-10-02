#!/usr/bin/env python3
"""§30M Visual Pitch for facelove-returning-it — three candidates per B-roll row, the top one picked (the act map's row)."""
import json, pathlib
HERE = pathlib.Path(__file__).parent
def s(st, li, fe, sp, fr, mk): return dict(stop=st, line=li, feel=fe, specific=sp, fresh=fr, makeable=mk)
def row(beat, line, cands, hero=False):
    c = [dict(route=r, picture=p, score=sc) for r, p, sc in cands]
    tot = [sum(x["score"].values()) for x in c]
    return dict(beat=beat, line=line, candidates=c, pick=tot.index(max(tot)), hero=hero)
G = [
 dict(group="Act 1", role="proof", idea="the fake-out: every 'it's not because' is the stick working on her real skin, then the counter woman who said it couldn't", rows=[
  row("B01", "And it is not because it goes on pure white", [
   ("PRODUCT", "the balm's flat crest pressing onto her bare, red cheekbone and drawing one clean white stripe", s(2, 2, 1, 2, 2, 2)),
   ("LITERAL", "the uncapped stick held up white end to the lens", s(1, 2, 0, 1, 1, 2)),
   ("DETAIL", "a macro of the white balm crest alone, no skin", s(1, 1, 0, 2, 1, 2))]),
  row("B02", "and then turns into my exact shade", [
   ("PROOF", "side-on macro: the brush circles through the white stripe and the white becomes her olive skin right behind the crown, still white ahead of it", s(2, 2, 2, 2, 2, 1)),
   ("CONTRAST", "two stills: white stripe, then blended cheek, cut together", s(1, 2, 1, 1, 1, 2)),
   ("LITERAL", "the brush end held up to the lens", s(1, 1, 0, 1, 1, 2))], hero=True),
  row("B03", "and melts in like it was made for my skin.", [
   ("REACTION", "two fingertips pat the finished cheek, then her eyes come to the lens, quietly pleased; her crow's feet still there", s(2, 2, 2, 2, 1, 2)),
   ("PROOF", "a slow look at the blended cheek in window light", s(1, 2, 1, 1, 1, 2)),
   ("SYMBOL", "the capped stick set down on the vanity", s(1, 0, 1, 1, 1, 2))]),
  row("B05", "told me my redness was too tricky to match and I should not bother.", [
   ("STAKES", "over the saleswoman's shoulder: she holds a bottle beside the creator's red jaw, three swatch stripes matching nothing, and slowly shakes her head", s(2, 2, 2, 2, 2, 2)),
   ("DETAIL", "three beige swatch stripes on her red jaw, none matching", s(2, 2, 1, 2, 1, 2)),
   ("WORLD", "the whole beauty hall, the creator small at one counter", s(1, 1, 1, 1, 2, 2))])]),
 dict(group="Act 2", role="proof", idea="the reasons pile up: each problem named is covered on her face, then the world notices", rows=[
  row("B06", "It is not because it covered the redness,", [
   ("CONTRAST", "her cheek half done — even on one side, red on the other — the brush stopping right on the border", s(2, 2, 2, 2, 2, 2)),
   ("PROOF", "the whole cheek blended, red gone", s(1, 2, 1, 1, 1, 2)),
   ("LITERAL", "a close-up of red skin", s(1, 1, 1, 1, 0, 2))], hero=True),
  row("B07", "the hyperpigmentation, the old post-acne marks,", [
   ("DETAIL", "from under the jaw: the balm crest glides over the small brown marks, a thin white line laid on them", s(2, 2, 1, 2, 2, 2)),
   ("CONTRAST", "the marks, then the blended jaw", s(1, 2, 1, 1, 1, 1)),
   ("LITERAL", "a macro of the brown marks alone", s(1, 1, 1, 1, 1, 2))]),
  row("B08", "and every tired line and dark circle", [
   ("PROOF", "the brush pats under her eye: the dark circle evens out while the crow's feet stay exactly where they were", s(2, 2, 2, 2, 2, 1)),
   ("STAKES", "her tired eye in the mirror before", s(1, 1, 2, 1, 1, 2)),
   ("LITERAL", "a macro of the dark circle", s(1, 1, 1, 1, 1, 2))]),
  row("B08b", "I have been hiding for years, in one swipe.", [
   ("PROOF", "one brush swipe across her cheekbone, then her whole face even, every line still there, eyes to the lens", s(2, 2, 2, 2, 1, 2)),
   ("REACTION", "her raised-eyebrow look to the lens", s(1, 1, 2, 1, 1, 2)),
   ("SYMBOL", "the concealer and three bottles she used to hide it pushed into a drawer", s(1, 1, 1, 2, 2, 1))]),
  row("B09", "And it is definitely not because three of my friends this week", [
   ("WORLD", "over her shoulder at the café: three friends lean in at once, coffees in hand, eyes on her face", s(2, 2, 2, 2, 2, 2)),
   ("REACTION", "one friend's eyebrows going up", s(1, 1, 1, 1, 1, 2)),
   ("LITERAL", "three coffees on a table", s(1, 1, 0, 1, 1, 2))]),
  row("B10", "asked what I am using,", [
   ("REACTION", "the auburn friend touches her own cheek with two fingers and raises her brows, asking", s(2, 2, 2, 2, 2, 2)),
   ("PRODUCT", "the stick slid across the café table", s(1, 1, 1, 1, 1, 2)),
   ("POV", "the friend's face from the creator's seat, mouthing the question", s(1, 2, 1, 1, 1, 1))])]),
 dict(group="Act 3", role="after", idea="the easy morning: one swipe at the hall mirror and out of the door", rows=[
  row("B11", "throw this one stick on before the grocery store,", [
   ("PRODUCT", "keys on one finger, one swipe across her cheek in the round brass hall mirror, cap on", s(2, 2, 2, 2, 2, 2)),
   ("WORLD", "the grocery store aisle", s(1, 1, 1, 1, 1, 2)),
   ("LITERAL", "the stick in her tote bag", s(1, 1, 0, 1, 1, 2))]),
  row("B12", "and feel completely confident walking out the door.", [
   ("WORLD", "from low on the path: she pulls the door shut and walks two steps toward us in the morning sun, chin up", s(2, 2, 2, 2, 2, 2)),
   ("REACTION", "her smile in the car mirror", s(1, 1, 2, 1, 1, 2)),
   ("LITERAL", "a front door opening", s(1, 1, 0, 1, 1, 2))], hero=True)]),
 dict(group="Act 4", role="offer", idea="the twist: the deal laid out on her vanity, and the one stick going back", rows=[
  row("B13", "Two full Foundation Sticks for almost the price of one,", [
   ("PRODUCT", "from above the vanity: her hand sets a second stick upright beside the first, both wordmarks to the lens", s(2, 2, 2, 2, 2, 2)),
   ("LITERAL", "two sticks on a white background", s(1, 2, 0, 1, 1, 2)),
   ("CONTRAST", "one stick, then two", s(1, 2, 1, 1, 1, 2))], hero=True),
  row("B14", "plus a free primer, a mystery gift,", [
   ("PRODUCT", "level with the vanity: the primer and the small gift box set down beside the two sticks", s(2, 2, 1, 1, 1, 2)),
   ("DETAIL", "level with the vanity: her hand sets the primer and the small gift box beside the two sticks, the box lid ajar on a fold of tissue paper", s(2, 2, 1, 2, 2, 2)),
   ("LITERAL", "the primer tube alone", s(1, 1, 0, 1, 1, 2))]),
  row("B14b", "and a full thirty day money back guarantee.", [
   ("PRODUCT", "low on the vanity: her hand slides the whole bundle — two sticks, primer, gift box — toward the lens", s(2, 2, 1, 2, 2, 2)),
   ("SYMBOL", "a calendar page with thirty days", s(1, 1, 0, 1, 1, 1)),
   ("REACTION", "her shrug — nothing to lose", s(1, 1, 1, 1, 1, 2))]),
  row("B15b", "and buying the deal like I should have.", [
   ("WORLD", "on her front step in the morning sun she picks up the delivery box and tucks it under her arm with a grin", s(2, 2, 2, 2, 2, 2)),
   ("PRODUCT", "the bundle unboxed on the vanity", s(1, 2, 1, 1, 1, 2)),
   ("LITERAL", "a parcel on a doorstep", s(1, 1, 0, 1, 1, 2))])]),
 dict(group="Act 5", role="offer", idea="the formula, not her skin: her finished face and the stick in one frame", rows=[
  row("B16", "It was never your skin. It was the formula.", [
   ("PROOF", "she lifts the stick beside her even cheek, wordmark to the lens, every line of her face still there", s(2, 2, 2, 2, 2, 2)),
   ("PRODUCT", "the stick alone standing on the vanity", s(1, 1, 1, 1, 1, 2)),
   ("CONTRAST", "her bare face cut to her finished face", s(2, 2, 2, 1, 1, 1))], hero=True)]),
]
json.dump(dict(build="facelove-returning-it", hooks=[], groups=G), open(HERE / "visual_plan.json", "w"), indent=1, ensure_ascii=False)
