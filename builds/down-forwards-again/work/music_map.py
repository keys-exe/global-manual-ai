#!/usr/bin/env python3
"""§40A (V7.75.0) — the Music Register Map and the music cues for down-forwards-again (user, 2026-10-01: "USE THE LATEST BGM UPDATE").
One music family for the whole video (low bowed cello / string drone, sparse felt piano, a soft ticking pulse), varied by part.
Each hook variant carries its own MUS-OPEN cue cut to the hook's length; the body cue is identical across variants (§30H).
Section edges sit on the words, read off the locked VO's word timings (acts/plan/words.json for TH-A1…A5, hooks/plan/words.json for the hooks),
the body's act starts = the cumulative TH-A lengths. Writes edit/music/<cue>.cue.json, work/music_map.md and board/doc_music.json."""
import json, pathlib, re, time
B = pathlib.Path(__file__).parents[1]
AW = json.load(open(B / "acts/plan/words.json")); HW = json.load(open(B / "hooks/plan/words.json"))
ACT = {"A1": 31.92, "A2": 25.08, "A3": 33.01, "A4": 39.74, "A5": 18.52}          # TH-A lengths on the board (the body = their run)
HOOK = {"HK1": 12.2, "HK2": 8.64, "HK3": 7.64}
start, t = {}, 0.0
for a, d in ACT.items(): start[a] = round(t, 2); t += d
BODY = round(t, 2)
norm = lambda w: re.sub(r"[^a-z0-9]", "", w.lower())
def at(words, phrase, base=0.0):
    """start time of the first occurrence of the phrase (word sequence) — 0.15 s before its first word, so the change lands under it."""
    p = [norm(x) for x in phrase.split()]; w = [norm(x[0]) for x in words]
    for i in range(len(w) - len(p) + 1):
        if w[i:i + len(p)] == p: return round(base + max(0.0, words[i][1] - 0.15), 2)
    raise SystemExit(f"phrase not found: {phrase!r}")
FAMILY = ["one music family: low bowed cello and string drone, sparse felt piano, a slow soft heartbeat pulse",
          "instrumental, sits quietly under a speaking voice"]
AVOID = ["drums", "trailer hits", "EDM", "synth lead", "brass", "guitar"]
LOUD = {"low": "quiet and sparse", "mid": "fuller, a clear step louder", "high": "full and present, the loudest part"}
def sec(name, s, e, energy, reg, styles):
    return {"name": name, "start": s, "end": e, "energy": energy, "register": reg,
            "styles": [reg + ": " + styles[0]] + styles[1:] + [LOUD[energy], "carries straight on from the section before with no pause, never stops or goes silent"]}
A = lambda a, ph: at(AW[a]["words"], ph, start[a])
S = [sec("The patient", 0, A("A1", "2 cm below"), "low", "MUS-OPEN",
         ["investigative documentary suspense", "low sustained drone, slow heartbeat pulse, sparse felt piano", "minor, unresolved, no melody"]),
     sec("The band", A("A1", "2 cm below"), start["A2"], "low", "MUS-EDU",
         ["inquisitive tension", "a repeating soft piano figure over the drone", "clean and curious, minor or modal, the viewer leans in"]),
     sec("That is why", start["A2"], start["A3"], "mid", "MUS-EXPOSE",
         ["darker and lower", "long low drones, dissonant intervals", "the pulse more present, a soft low stinger on the last line", "no warmth yet"]),
     sec("What has been tried", start["A3"], A("A3", "this does"), "mid", "MUS-EXPOSE",
         ["the same tension, held", "the tension holds, no resolution", "unresolved"]),
     sec("This does", A("A3", "this does"), start["A4"], "high", "MUS-TURN",
         ["the release", "the drone lifts into the first warm chord", "a slow cello line starts to move over moving piano chords",
          "the pulse opens into gentle movement", "a new key arrives", "clearly audible and moving the whole time, never a single held tone"]),
     sec("Proof", start["A4"], start["A5"], "high", "MUS-AFTER",
         ["warm and hopeful", "lifted, strings and piano moving forward", "dignified, never jingly"]),
     sec("Move the load", start["A5"], A("A5", "two for one"), "high", "MUS-OFFER",
         ["confident steady pulse", "a little fuller and more forward"]),
     sec("The offer", A("A5", "two for one"), A("A5", "nothing to lose"), "mid", "MUS-OFFER",
         ["held back under the price and the copies warning", "the same pulse, thinner, so the words carry"]),
     sec("Go and do your stairs", A("A5", "nothing to lose"), BODY, "high", "MUS-OFFER",
         ["steady and resolved", "plays at level to the end"]),
     {"name": "Tail", "start": BODY, "end": round(BODY + 2, 2), "energy": "silent", "register": "MUS-OFFER", "styles": ["the last held chord fades out to silence"]}]
NEGM = ["cute", "cheerful", "upbeat", "ukulele", "whistling", "hand claps", "corporate jingle", "stock advert jingle", "pop beat", "humming"]
CUES = {"BODY": {"scene": "MUS-BODY", "length_s": round(BODY + 2, 2), "theme": FAMILY, "avoid": AVOID + NEGM + ["ticking clock", "fast hi-hat"], "tempo": "slow", "bpm": 66,
                 "registers": {x["name"]: x["register"] for x in S}, "sections": S}}
HOOKQ = {"HK1": ("without an operation", "The result", "Without — and here is how"),
         "HK2": ("it takes", "The doctor's instruction", "Ten seconds, not a prescription"),
         "HK3": ("i have started", "The scans", "A different question")}
for h, (ph, n1, n2) in HOOKQ.items():
    cut = at(HW[h]["words"], ph); L = round(HOOK[h] + 2, 2)
    # the register's own theme is written out here without its "soft ticking percussion": the ticking read as 170–185 BPM (v1 TEMPO FAIL)
    CUES[h] = {"scene": f"MUS-OPEN-{h}", "registers": {"all": "MUS-OPEN"}, "length_s": L,
               "theme": ["investigative documentary suspense", "low sustained drone", "sparse piano", "low plucked and bowed strings", "minor or modal",
                         "unresolved", "no melody"] + FAMILY,
               "avoid": AVOID + NEGM + ["resolving major cadence", "ticking clock", "fast hi-hat"], "tempo": "slow", "bpm": 66,
               "sections": [{"name": n1, "start": 0, "end": cut, "energy": "low",
                             "styles": ["fades in softly over the first second", "very quiet: only the low drone and a slow heartbeat pulse",
                                        "one sparse low piano note", "a question hanging"]},
                            {"name": n2, "start": cut, "end": HOOK[h], "energy": "mid", "_short": HOOK[h] - cut < 3,
                             "styles": ["clearly louder and fuller", "bowed low strings join the drone", "the pulse more present",
                                        "still unresolved, continuous, never goes silent"]},
                            {"name": "Hand-over", "start": HOOK[h], "end": L, "energy": "silent",
                             "styles": ["the drone fades out to silence"]}]}
# The body is composed in two parts split on the turn word "This does." (v1–v3 of the single 152 s body rendered the turn section as one flat
# held tone with silences around it). Part A: the patient → the failed fixes, fading on the turn word; Part B opens on the turn with the
# release. §40A: "silence on the turn word, then the new key arrives" — the join sits there. Mixed by work/bgm_mix.py.
TURN = A("A3", "this does")
def part(name, lo, hi, tail_name, tail_styles):
    xs = [dict(x, start=round(max(x["start"], lo) - lo, 2), end=round(min(x["end"], hi) - lo, 2)) for x in S if x["name"] != "Tail" and x["end"] > lo and x["start"] < hi]
    L = round(hi - lo + 2, 2)
    return {"scene": name, "length_s": L, "theme": FAMILY, "avoid": CUES["BODY"]["avoid"], "tempo": "slow", "bpm": 66,
            "registers": {x["name"]: x["register"] for x in xs},
            "sections": xs + [{"name": tail_name, "start": round(hi - lo, 2), "end": L, "energy": "silent", "styles": tail_styles}]}
CUES["BODY_A"] = part("MUS-BODY-A", 0, TURN, "To the turn", ["fades out to near silence, the tension left hanging"])
CUES["BODY_B"] = part("MUS-BODY-B", TURN, BODY, "Tail", ["the last held chord fades out to silence"])
# B v1: "starting from near silence" gave 14 s of silence, and the quiet offer + silent tail went silent from 73 s → the release plays from the
# first second; the offer and the close are one section that plays at level to the very end; the fade-out is done in the mix, not asked for.
xs = CUES["BODY_B"]["sections"]
off = [x for x in xs if x["name"] == "The offer"][0]; L = CUES["BODY_B"]["length_s"]
CUES["BODY_B"]["sections"] = [x for x in xs if x["name"] not in ("The offer", "Go and do your stairs", "Tail")] + [
    {"name": "The offer — go and do your stairs", "start": off["start"], "end": L, "energy": "high", "register": "MUS-OFFER",
     "styles": ["MUS-OFFER: confident, steady and resolved", "the same steady pulse and warm strings", "plays at a steady level right to the very end of the track",
                "carries straight on with no pause, never stops or goes silent, no ending before the last second"]}]
CUES["BODY_B"]["sections"][0]["styles"] = ["MUS-TURN: the release, audible from the very first second", "the drone lifts into the first warm chord",
    "a slow cello line moves over moving piano chords", "the pulse opens into gentle movement", "a new key arrives",
    "clearly audible and moving the whole time, never a single held tone", LOUD["high"]]
# The close (B decays to silence ~15 s before the VO ends): its own short cue from "Two for one" to the end, crossfaded in under the price.
OFFER = A("A5", "two for one"); NOTH = A("A5", "nothing to lose"); LC = round(BODY - OFFER + 4, 2)
CUES["BODY_C"] = {"scene": "MUS-BODY-C", "length_s": LC, "theme": FAMILY, "avoid": CUES["BODY"]["avoid"], "tempo": "slow", "bpm": 66,
    "registers": {"The offer": "MUS-OFFER", "Go and do your stairs": "MUS-OFFER"},
    "sections": [{"name": "The offer", "start": 0, "end": round(NOTH - OFFER, 2), "energy": "mid", "register": "MUS-OFFER",
                  "styles": ["MUS-OFFER: confident steady pulse, held back so the words carry", "warm strings and piano, the same family",
                             "audible from the very first second", "carries straight on, never stops or goes silent"]},
                 {"name": "Go and do your stairs", "start": round(NOTH - OFFER, 2), "end": LC, "energy": "high", "register": "MUS-OFFER",
                  "styles": ["MUS-OFFER: steady and resolved, a little fuller", "lands on one warm held resolving chord",
                             "plays at a steady level right to the very end of the track, no fade, no silence"]}]}
for h in HOOKQ:
    sx = CUES[h]["sections"]
    if sx[1].pop("_short"):
        sx[0].update(name=sx[0]["name"] + " — " + sx[1]["name"], end=sx[1]["end"],
                     styles=sx[0]["styles"] + ["rises one small step over its last seconds, bowed low strings joining", "continuous, never goes silent"])
        del sx[1]
for k, c in CUES.items(): (B / f"edit/music/{k}.cue.json").write_text(json.dumps(c, ensure_ascii=False, indent=1))
LINES = {"HK1/HK2/HK3": "the hook (each its own cue, cut to its length)", **{x["name"]: "" for x in S}}
rows = ["| Part | Starts on | What the script is doing | Register | Cue in plain words | Level |", "|---|---|---|---|---|---|",
        "| Hooks HK1 · HK2 · HK3 | the first word | the callout: a result, a doctor's instruction, a different question — opens the loop | MUS-OPEN | a low drone and a slow heartbeat pulse, one low piano note; rises a step on the second sentence; no tune | low → mid |"]
DOING = {"The patient": "a patient's story and what her scan does not show — the contradiction",
         "The band": "the education: the band of tendon, seventeen times bodyweight, the self-test, why coming down is worse",
         "That is why": "agitation: backwards on the stairs, three tries at the chair, the list she said no to; 'never how hard she tried'",
         "What has been tried": "the failed fixes: sleeve, hinged brace, gel — 'none of them move the load'",
         "This does": "the turn: 'This does. It is called Stryde.' — where it sits, the pad, the placement",
         "Proof": "proof: 34% less strain, surgeons, 200,000 people, the stairs test, the two identical scans",
         "Move the load": "the conclusion: you cannot strengthen your way out of a load problem",
         "The offer": "the offer: two for one, sixty days, the Stryde site, the copies warning",
         "Go and do your stairs": "the close: nothing to lose but the pain"}
PLAIN = {"MUS-OPEN": "investigative-documentary suspense: low drone, slow heartbeat pulse, sparse felt piano, minor, unresolved",
         "MUS-EDU": "the same drone with a repeating soft piano figure — curious, leaning in, still minor",
         "MUS-EXPOSE": "darker and lower: long drones, dissonant intervals, the pulse more present; no warmth",
         "MUS-TURN": "the release: the drone lifts into the first warm chord, the pulse starts to move, a new key",
         "MUS-AFTER": "warm and hopeful: strings and piano moving forward, dignified, never jingly",
         "MUS-OFFER": "confident steady pulse, a little fuller; thinner under the price; resolves on a held chord"}
first = {"The patient": "A patient of mine", "The band": "Two centimetres below your kneecap", "That is why": "That is why she came down backwards",
         "What has been tried": "A sleeve squeezes the whole knee", "This does": "This does.", "Proof": "Thirty four percent less strain",
         "Move the load": "You cannot strengthen your way out", "The offer": "Two for one", "Go and do your stairs": "Nothing to lose but the pain"}
for x in S:
    if x["name"] == "Tail": continue
    rows.append(f"| {x['name']} ({x['start']:.2f}–{min(x['end'], BODY):.2f} s of the body) | \"{first[x['name']]}\" | {DOING[x['name']]} | {x['register']} | {PLAIN[x['register']]} | {x['energy']} |")
md = ("One music family for the whole video — a low bowed cello and string drone, sparse felt piano and a slow soft heartbeat pulse — that changes mood with the "
      "script. It opens like an investigative documentary (suspense, curiosity), goes darker under the failed fixes, lifts at \"This does.\", turns warm "
      "under the proof and ends steady and confident. No cute, cheerful or upbeat music anywhere the script educates, warns or exposes (§40A). "
      "Music sits about 18 dB under the voice and ducks ~8 dB more while the doctor speaks; it drops under the price.\n\n" + "\n".join(rows))
(B / "work/music_map.md").write_text("### Music Register Map (§40A)\n\n" + md + "\n")
doc = {"title": "Music register map", "step": 5, "order": 4, "source": "builds/down-forwards-again/work/music_map.md", "build": "down-forwards-again",
       "updatedAt": int(time.time() * 1000), "sections": [{"title": "Music Register Map (§40A)", "md": md}]}
json.dump(doc, open(B / "board/doc_music.json", "w"), ensure_ascii=False, indent=1)
print("body", BODY, "act starts", start); [print(f"  {x['name']:22s} {x['start']:7.2f}–{x['end']:7.2f} {x['register']:10s} {x['energy']}") for x in S]
for h in HOOKQ: print(h, CUES[h]["length_s"], [(s["name"], s["start"], s["end"]) for s in CUES[h]["sections"]])
