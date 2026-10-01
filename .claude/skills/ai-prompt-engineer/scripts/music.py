#!/usr/bin/env python3
"""§24M — one film scene's music: build its composition plan, compose it, and check it against the plan.

Usage:
  music.py plan    CUE.json [--out CUE.plan.json]          # free — builds the ElevenLabs composition plan
  music.py compose CUE.json --out SC-03.music.mp3          # paid — ONE generation (§5 one render per call)
  music.py check   CUE.json SC-03.music.mp3 [--json]       # the agent's listening pass, by instrument

CUE.json — the scene's music cue, from its sound plan:
  {"scene": "SC-03", "length_s": 24.6,                   # the scene's locked length
   "theme":    ["warm intimate film score", "solo felt piano", "soft cello", "slow tempo"],   # Look Sheet field 9
   "avoid":    ["vocals", "drums", "synthesizers"],
   "tempo":    "slow" | "moderate" | "fast",
   "sections": [{"name": "Before the turn", "start": 0,    "end": 11.2, "energy": "low",
                 "styles": ["sparse felt piano"], "avoid": ["strings"]},
                {"name": "The turn",        "start": 11.2, "end": 13.0, "energy": "silent",
                 "styles": ["near silence", "single fading piano note"]},
                {"name": "After",           "start": 13.0, "end": 24.6, "energy": "mid",
                 "styles": ["cello enters", "warm theme"]}]}
  Section edges sit on the scene's cut cues or its turn (§24M). The last section runs 2s past the scene.
  "register": "MUS-OPEN" (or --register): the §40A register of the script part — MUS-OPEN, MUS-EXPOSE,
  MUS-EDU, MUS-TURN, MUS-AFTER, MUS-OFFER — pre-fills the theme and tempo, adds the NEG-MUSIC negatives,
  and refuses a tense register (OPEN / EXPOSE / EDU) whose theme asks for cute, cheerful or upbeat music.

plan:    writes the composition plan (global styles = theme + always "instrumental"; negatives = avoid + "vocals",
         "lyrics", "singing"; one plan section per cue section at its exact duration). Free — no generation.
compose: POST /v1/music with the plan and respect_sections_durations (ELEVENLABS_API_KEY). One track.
         (Route unverified until its first render is checked.)
check:   measures the track against the cue — any FAIL means regenerate with the fault named (§22X diagnosis):
           LENGTH   within 0.5s of the plan
           ENERGY   each section's loudness in the order its energy labels say (silent < low < mid < high,
                    at least 2 dB apart); a "silent" section at least 20 dB under the loudest section
           DROPOUT  no silence longer than 0.8s inside a non-silent section (a cut-out or a restart)
           CLICK    no sudden jump of more than 12 dB between consecutive 100 ms windows (a splice)
           VOCALS   faster-whisper finds no run of confident words (sung lyrics)
           TEMPO    the estimated beat rate sits in the cue's tempo band (slow < 90, moderate 85–120, fast > 115 BPM)
         Also reports each section's brightness (spectral centroid) for the reader. Thresholds unverified — tuned
         on the first build.
"""
import argparse, json, os, re, subprocess, sys, urllib.request
from pathlib import Path

import imageio_ffmpeg
import numpy as np

FF = imageio_ffmpeg.get_ffmpeg_exe()
SR = 22050
# §40A music registers (V7.75.0): the part's register pre-fills the theme and tempo and adds the NEG-MUSIC negatives.
REGISTERS = {
    "MUS-OPEN":   {"theme": ["investigative documentary suspense", "low sustained drone", "slow felt pulse", "sparse piano", "low plucked and bowed strings", "soft ticking percussion", "minor or modal", "unresolved", "no melody"], "tempo": "slow"},
    "MUS-EXPOSE": {"theme": ["dark investigative tension", "long low drones", "dissonant intervals", "present slow pulse", "short stingers", "minor", "unresolved", "no warmth"], "tempo": "slow"},
    "MUS-EDU":    {"theme": ["inquisitive light tension", "repeating pulse or arpeggio", "clean piano or electronic figures", "low to mid energy", "minor or modal"], "tempo": "moderate"},
    "MUS-TURN":   {"theme": ["release", "the drone lifting", "first warm chord", "pulse opening into movement", "new key arriving"], "tempo": "moderate"},
    "MUS-AFTER":  {"theme": ["warm hopeful forward score", "lifted or major", "strings pads and piano with movement", "dignified lift"], "tempo": "moderate"},
    "MUS-OFFER":  {"theme": ["confident steady pulse", "brighter", "a little faster", "held resolve ending"], "tempo": "moderate"},
}
NEG_MUSIC = ["cute", "cheerful", "upbeat", "ukulele", "whistling", "hand claps", "corporate jingle", "stock advert jingle", "pop beat", "vocals", "lyrics", "humming"]
TENSE = {"MUS-OPEN", "MUS-EXPOSE", "MUS-EDU"}
NEG_WORDS = re.compile(r"\b(?:cute|cheerful|upbeat|happy|ukulele|whistl\w*|claps?|corporate|jingle|pop beat|bouncy|playful|bright)\b", re.I)


def apply_register(cue, reg):
    """§40A: fold the register into the cue; refuse a tense register whose theme carries a NEG-MUSIC word."""
    if not reg:
        return cue
    if reg not in REGISTERS:
        sys.exit(f"unknown register {reg}; one of {', '.join(REGISTERS)}")
    r = REGISTERS[reg]
    cue = dict(cue)
    cue["register"] = reg
    cue["theme"] = list(dict.fromkeys(r["theme"] + list(cue.get("theme") or [])))
    cue.setdefault("tempo", r["tempo"])
    cue["avoid"] = list(dict.fromkeys(list(cue.get("avoid") or []) + NEG_MUSIC + (["resolving major cadence"] if reg in TENSE else [])))
    if reg in TENSE:
        bad = [t for t in (cue.get("theme") or []) + [x for sec in cue.get("sections", []) for x in sec.get("styles", [])] if NEG_WORDS.search(t)]
        if bad:
            sys.exit(f"{reg} cannot carry {bad}: the script here educates, warns or exposes — no cute, cheerful or upbeat music (§40A, NEG-MUSIC)")
    return cue


ORDER = {"silent": 0, "low": 1, "mid": 2, "high": 3}
TEMPO = {"slow": (40, 90), "moderate": (85, 120), "fast": (115, 200)}


def build_plan(cue):
    secs = []
    for i, s in enumerate(cue["sections"]):
        end = s["end"] + (2.0 if i == len(cue["sections"]) - 1 else 0.0)
        secs.append({"section_name": s["name"],
                     "positive_local_styles": s.get("styles", []) or ["continue the theme"],
                     "negative_local_styles": s.get("avoid", []),
                     "duration_ms": int(round((end - s["start"]) * 1000)),
                     "lines": []})
    return {"positive_global_styles": list(dict.fromkeys(cue["theme"] + ["instrumental", f"{cue.get('tempo', 'slow')} tempo"])),
            "negative_global_styles": list(dict.fromkeys(cue.get("avoid", []) + ["vocals", "lyrics", "singing"])),
            "sections": secs}


def compose(plan, out):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("ELEVENLABS_API_KEY is not set")
    body = json.dumps({"composition_plan": plan, "respect_sections_durations": True}).encode()
    req = urllib.request.Request("https://api.elevenlabs.io/v1/music?output_format=mp3_44100_128", data=body,
                                 headers={"xi-api-key": key, "Content-Type": "application/json"}, method="POST")
    with urllib.request.urlopen(req, timeout=600) as r:
        Path(out).write_bytes(r.read())


def load(path):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def db(x):
    return 20 * np.log10(max(float(np.sqrt(np.mean(x ** 2))) if len(x) else 0.0, 1e-6))


def tempo_bpm(y):
    hop = 512
    frames = len(y) // hop
    if frames < 64:
        return None
    env = np.array([np.sqrt(np.mean(y[i * hop:(i + 1) * hop] ** 2)) for i in range(frames)])
    onset = np.maximum(0, np.diff(env))
    onset -= onset.mean()
    ac = np.correlate(onset, onset, "full")[len(onset) - 1:]
    fps = SR / hop
    lo, hi = int(fps * 60 / 200), int(fps * 60 / 40)
    if hi >= len(ac):
        return None
    lag = lo + int(np.argmax(ac[lo:hi]))
    return round(60 * fps / lag, 1)


def vocals(path):
    try:
        from faster_whisper import WhisperModel
    except ImportError:
        return {"checked": False, "note": "faster-whisper not installed"}
    m = WhisperModel("base.en", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(path), vad_filter=True, word_timestamps=True)
    words = [w for s in segs for w in (s.words or []) if w.probability > 0.6]
    return {"checked": True, "confident_words": len(words), "text": " ".join(w.word for w in words)[:200]}


def check(cue, path):
    y = load(path)
    total = len(y) / SR
    res, fails = {"file": str(path), "length_s": round(total, 2)}, []
    want = cue["sections"][-1]["end"] + 2.0
    if abs(total - want) > 0.5:
        fails.append({"check": "LENGTH", "detail": f"{total:.2f}s vs plan {want:.2f}s"})
    secs = []
    for i, s in enumerate(cue["sections"]):
        a, b = int(s["start"] * SR), int(min(total, s["end"] + (2.0 if i == len(cue["sections"]) - 1 else 0)) * SR)
        seg = y[a:b]
        spec = np.abs(np.fft.rfft(seg[: SR * 10])) if len(seg) else np.zeros(1)
        freqs = np.fft.rfftfreq(min(len(seg), SR * 10), 1 / SR) if len(seg) else np.zeros(1)
        centroid = float((spec * freqs).sum() / max(spec.sum(), 1e-9))
        win = int(0.1 * SR)
        wins = [db(seg[k:k + win]) for k in range(0, max(0, len(seg) - win), win)]
        secs.append({"name": s["name"], "energy": s["energy"], "rms_db": round(db(seg), 1),
                     "brightness_hz": round(centroid), "wins": wins})
    loud = max(x["rms_db"] for x in secs)
    for x in secs:
        if x["energy"] == "silent" and x["rms_db"] > loud - 20:
            fails.append({"check": "ENERGY", "detail": f"'{x['name']}' should be near silent: {x['rms_db']} dB vs loudest {loud} dB"})
        if x["energy"] != "silent":
            run = best = 0
            for w in x["wins"]:
                run = run + 1 if w < loud - 40 else 0
                best = max(best, run)
            if best * 0.1 > 0.8:
                fails.append({"check": "DROPOUT", "detail": f"'{x['name']}' drops out for {best * 0.1:.1f}s"})
        jumps = [abs(x["wins"][k + 1] - x["wins"][k]) for k in range(len(x["wins"]) - 1)]
        if jumps and max(jumps) > 12 and x["energy"] != "silent":
            fails.append({"check": "CLICK", "detail": f"'{x['name']}' jumps {max(jumps):.1f} dB in 100 ms"})
    ranked = [x for x in secs if x["energy"] != "silent"]
    for p in ranked:
        for q in ranked:
            if ORDER[p["energy"]] > ORDER[q["energy"]] and p["rms_db"] < q["rms_db"] + 2:
                fails.append({"check": "ENERGY", "detail": f"'{p['name']}' ({p['energy']}) not louder than '{q['name']}' ({q['energy']}): {p['rms_db']} vs {q['rms_db']} dB"})
    bpm = tempo_bpm(y)
    band = TEMPO.get(cue.get("tempo", "slow"))
    if bpm and band and not (band[0] <= bpm <= band[1]) and not (band[0] <= bpm / 2 <= band[1]) and not (band[0] <= bpm * 2 <= band[1]):
        fails.append({"check": "TEMPO", "detail": f"~{bpm} BPM outside {cue.get('tempo')} ({band[0]}–{band[1]})"})
    v = vocals(path)
    if v.get("checked") and v["confident_words"] >= 4:
        fails.append({"check": "VOCALS", "detail": f"{v['confident_words']} confident words: {v['text']!r}"})
    for x in secs:
        x.pop("wins")
    res.update({"sections": secs, "tempo_bpm": bpm, "vocals": v, "fails": fails,
                "status": "PASS" if not fails else "FAIL"})
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["plan", "compose", "check"])
    ap.add_argument("cue")
    ap.add_argument("track", nargs="?")
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--register", help="§40A register: " + ", ".join(REGISTERS))
    a = ap.parse_args()
    cue = apply_register(json.loads(Path(a.cue).read_text()), a.register or json.loads(Path(a.cue).read_text()).get("register"))
    if a.what == "plan":
        plan = build_plan(cue)
        out = a.out or str(Path(a.cue).with_suffix(".plan.json"))
        Path(out).write_text(json.dumps(plan, indent=2))
        print(json.dumps({"status": "OK", "plan": out, "sections": len(plan["sections"]),
                          "length_s": sum(s["duration_ms"] for s in plan["sections"]) / 1000}, indent=2))
    elif a.what == "compose":
        if not a.out:
            sys.exit("--out is required")
        compose(build_plan(cue), a.out)
        print(json.dumps({"status": "OK", "track": a.out}, indent=2))
    else:
        if not a.track:
            sys.exit("check needs the track")
        r = check(cue, a.track)
        if a.json:
            print(json.dumps(r, indent=2))
        else:
            for x in r["sections"]:
                print(f"{x['name']:22} {x['energy']:7} {x['rms_db']:7} dB  brightness {x['brightness_hz']} Hz")
            print(f"length {r['length_s']}s  tempo ~{r['tempo_bpm']} BPM  vocals {r['vocals']}")
            for f in r["fails"]:
                print(f"FAIL  {f['check']:8} {f['detail']}")
            print(f"MUSIC {r['status']}")
        sys.exit(0 if r["status"] == "PASS" else 2)


if __name__ == "__main__":
    main()
