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
  "sung": true + "lines" per section — a music video (§3C, sung by default): the lyrics are the script's lines
  verbatim, in order. plan refuses a CROWDED section (over 2.5 words a second); the plan asks for one clear lead
  vocal with every word intelligible. check transcribes the vocal and FAILS LYRICS when a section's sung words
  match the script under 85% (missing words listed); --words-out saves the word timings for cuts.
  "bpm": 88 pins the tempo (and the cut grid).
cuts:    music.py cuts CUE TRACK --rows rows.json [--words words.json] — §3C/§30H for a music video. Sung, with a
         `phrase` per row: each row cuts 2 frames before the first sung word of its line, or on a beat at most 0.25s
         before it — never a full beat early, never under the line before (EARLY) — V7.91.4.
         Instrumental: rows hold their `bars` from cuts on bar lines, section changes on the music's. Prints every
         row's cut, time on screen and call length (E6); FLASH under 2.0s, SPLIT over 15s, NOT SUNG, HOLE.
render:  music.py render CUE TRACK --rows rows.json --out rough.mp4 — the rough cut: each clip from its 0.4s
         in-point for its time on screen, 9:16, joined frame-exact, the track whole under it.
  "product_at": 31.4 — the product's first frame (from the act map / cut sheet). plan refuses unless a section starts
  on it (±0.25s), every section before it is investigation (its "register" MUS-OPEN / -EXPOSE / -EDU, nothing sad
  or cute in its styles) and the section starting on it turns (MUS-TURN or later) — V7.78.0, §40A.
  Each section may carry its own "register": its theme and negatives are added to that section.
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
# V7.78.0 (user 2026-10-01: "i want an investigation not sad at first bgm and change when the product shows"):
# everything before the product's first frame is investigation — never sad — and the music changes on that frame.
NEG_SAD = ["sad", "melancholic", "mournful", "sorrowful", "tearful", "sentimental", "lament", "grief", "tragic",
           "weeping strings", "solo sad piano", "slow cello lament", "heartbreak ballad"]
NEG_WORDS = re.compile(r"\b(?:cute|cheerful|upbeat|happy|ukulele|whistl\w*|claps?|corporate|jingle|pop beat|bouncy|playful|bright"
                       r"|sad|melanchol\w*|mournful|sorrow\w*|tear\w*|weep\w*|lament\w*|grie\w*|sentimental|tragic|somb(?:er|re)|heartbr\w*|elegiac|wistful)\b", re.I)
AFTER_PRODUCT = {"MUS-TURN", "MUS-AFTER", "MUS-OFFER"}
PRODUCT_TOL = 0.25  # the music change sits within a quarter second of the product's first frame


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
    cue["avoid"] = list(dict.fromkeys(list(cue.get("avoid") or []) + NEG_MUSIC + (["resolving major cadence"] + NEG_SAD if reg in TENSE else [])))
    if reg in TENSE:
        bad = [t for t in (cue.get("theme") or []) + [x for sec in cue.get("sections", []) for x in sec.get("styles", [])] if NEG_WORDS.search(t)]
        if bad:
            sys.exit(f"{reg} cannot carry {bad}: the script here educates, warns or exposes — no cute, cheerful or upbeat music (§40A, NEG-MUSIC)")
    return cue


ORDER = {"silent": 0, "low": 1, "mid": 2, "high": 3}
TEMPO = {"slow": (40, 90), "moderate": (85, 120), "fast": (115, 200)}


VOCAL_NEG = {"vocals", "lyrics", "singing", "humming"}
# §3C sung music video: the lyrics are the script's lines verbatim, and every word must be made out.
SUNG_WPS = 2.5      # most words per second a section can carry and still be sung clearly (unverified)
SUNG_STYLES = ["one clear lead vocal up front in the mix", "every word intelligible", "sung at the rhythm of speech",
               "the lyrics sung exactly as written, no added words"]
SUNG_NEG = ["mumbled or slurred vocals", "heavy autotune", "vocal chops", "ad-libs", "added or repeated words",
            "a choir or backing vocals over the lead", "vocals buried under the instruments"]
LYRIC_MIN = 0.85    # word accuracy a section's sung lyrics must reach against the script (unverified)


def words_of(t):
    return re.findall(r"[a-z0-9']+", re.sub(r"[’‘]", "'", (t or "").lower()))


def product_change(cue):
    """V7.78.0: with `product_at` (the product's first frame, seconds) on the cue, a section must start on it (±0.25s);
    every section before it is investigation (MUS-OPEN / -EXPOSE / -EDU) and never sad; the one starting on it turns
    (MUS-TURN, or later registers). Section registers come from each section's `register`."""
    pa = cue.get("product_at")
    if pa is None:
        return
    secs = cue["sections"]
    starts = [s["start"] for s in secs]
    k = min(range(len(secs)), key=lambda i: abs(starts[i] - pa))
    errs = []
    if abs(starts[k] - pa) > PRODUCT_TOL:
        errs.append(f"no section starts on the product's first frame ({pa}s; nearest '{secs[k]['name']}' at {starts[k]}s) — the music changes when the product shows")
    for s in secs[:k]:
        reg = s.get("register")
        if reg and reg not in TENSE:
            errs.append(f"'{s['name']}' is before the product but carries {reg} — before the product the music is investigation (MUS-OPEN / MUS-EXPOSE / MUS-EDU)")
        bad = [t for t in s.get("styles", []) if NEG_WORDS.search(t)]
        if bad:
            errs.append(f"'{s['name']}' is before the product but asks for {bad} — investigation, never sad or cute")
    reg = secs[k].get("register")
    if reg and reg not in AFTER_PRODUCT:
        errs.append(f"'{secs[k]['name']}' starts on the product but carries {reg} — the product's first frame is MUS-TURN")
    if errs:
        sys.exit("PRODUCT CHANGE (§40A, V7.78.0):\n  " + "\n  ".join(errs))


def build_plan(cue):
    product_change(cue)
    sung = bool(cue.get("sung"))      # §3C: a sung music video, only on the user's call — lyrics = the script's lines verbatim
    secs = []
    for i, s in enumerate(cue["sections"]):
        end = s["end"] + (2.0 if i == len(cue["sections"]) - 1 else 0.0)
        sreg = REGISTERS.get(s.get("register"), {})
        secs.append({"section_name": s["name"],
                     "positive_local_styles": list(dict.fromkeys((sreg.get("theme") or []) + s.get("styles", []))) or ["continue the theme"],
                     "negative_local_styles": list(dict.fromkeys(s.get("avoid", []) + (NEG_SAD + NEG_MUSIC[:8] if s.get("register") in TENSE else []))),
                     "duration_ms": int(round((end - s["start"]) * 1000)),
                     "lines": list(s.get("lines", [])) if sung else []})
    tempo = f"{cue['bpm']} BPM" if cue.get("bpm") else f"{cue.get('tempo', 'slow')} tempo"
    if sung:
        crowded = []
        for i, s in enumerate(cue["sections"]):
            n = len(words_of(" ".join(s.get("lines", []))))
            dur = s["end"] - s["start"]
            if n and n / max(dur, 0.1) > SUNG_WPS:
                crowded.append(f"'{s['name']}': {n} words in {dur:.1f}s ({n / dur:.1f}/s, max {SUNG_WPS}/s) — lengthen the section, never cut a word")
        if crowded:
            sys.exit("CROWDED — the lyrics cannot be sung clearly in the time:\n  " + "\n  ".join(crowded))
    pos = cue["theme"] + (SUNG_STYLES if sung else ["instrumental"]) + [tempo]
    neg = [x for x in cue.get("avoid", []) if not (sung and x in VOCAL_NEG)] + (SUNG_NEG if sung else ["vocals", "lyrics", "singing"])
    return {"positive_global_styles": list(dict.fromkeys(pos)),
            "negative_global_styles": list(dict.fromkeys(neg)),
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


def transcribe(path):
    from faster_whisper import WhisperModel
    # V7.91.4 (L56): the cut words are timed with medium.en, as assemble.py (V7.80.0) — base.en placed sung words up to 0.7 s off
    m = WhisperModel("medium.en", device="cpu", compute_type="int8")
    segs, _ = m.transcribe(str(path), vad_filter=False, word_timestamps=True)
    return [{"w": w.word.strip(), "t": round(w.start, 3), "end": round(w.end, 3), "p": round(w.probability, 2)}
            for s in segs for w in (s.words or [])]


def lyric_match(cue, heard):
    """Per section: the script's lyric words against the words heard in that section's time (±1s)."""
    import difflib
    out = []
    for i, s in enumerate(cue["sections"]):
        want = words_of(" ".join(s.get("lines", [])))
        if not want:
            continue
        hi = s["end"] + (2.0 if i == len(cue["sections"]) - 1 else 1.0)
        got = [x for x in heard if s["start"] - 1.0 <= x["t"] <= hi]
        gw = [w for x in got for w in words_of(x["w"])]
        sm = difflib.SequenceMatcher(None, want, gw, autojunk=False)
        hit = sum(b.size for b in sm.get_matching_blocks())
        matched = set()
        for b in sm.get_matching_blocks():
            matched.update(range(b.a, b.a + b.size))
        out.append({"name": s["name"], "accuracy": round(hit / len(want), 3),
                    "missing": [w for k, w in enumerate(want) if k not in matched], "heard": " ".join(gw)})
    return out


def lyrics_check(cue, path):
    """§3C: transcribe the sung track and hold every section's lyrics to the script, word for word."""
    try:
        heard = transcribe(path)
    except ImportError:
        return {"checked": False, "note": "faster-whisper not installed"}
    return {"checked": True, "sections": lyric_match(cue, heard), "words": heard}


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
    if cue.get("sung"):
        v = lyrics_check(cue, path)
        for x in v.get("sections", []):
            if x["accuracy"] < LYRIC_MIN:
                fails.append({"check": "LYRICS", "detail": f"'{x['name']}' sung words match the script {x['accuracy']:.0%} (< {LYRIC_MIN:.0%}): missing {x['missing'][:8]} · heard {x['heard'][:120]!r}"})
        if not v.get("checked"):
            fails.append({"check": "LYRICS", "detail": "not checked: " + v.get("note", "")})
    else:
        v = vocals(path)
        if v.get("checked") and v["confident_words"] >= 4:
            fails.append({"check": "VOCALS", "detail": f"{v['confident_words']} confident words: {v['text']!r}"})
    for x in secs:
        x.pop("wins")
    res.update({"sections": secs, "tempo_bpm": bpm, "vocals": v, "fails": fails,
                "status": "PASS" if not fails else "FAIL"})
    return res


def grid(y, bpm=None):
    """Beat and bar times of a track: the tempo (detected, or the cue's bpm), the beat phase that best fits the
    onsets, and the bar phase (4/4) whose downbeats carry the most energy. Unverified on generated tracks."""
    hop = 512
    fps = SR / hop
    frames = len(y) // hop
    env = np.array([np.sqrt(np.mean(y[i * hop:(i + 1) * hop] ** 2)) for i in range(frames)])
    onset = np.maximum(0, np.diff(env, prepend=env[:1]))
    bpm = float(bpm or tempo_bpm(y) or 90.0)
    while bpm < 60:
        bpm *= 2
    while bpm > 160:
        bpm /= 2
    period = 60.0 / bpm
    total = len(y) / SR
    best, phase = -1.0, 0.0
    for k in range(48):
        ph = period * k / 48
        idx = (np.arange(ph, total, period) * fps).astype(int)
        idx = idx[idx < len(onset)]
        sc = float(onset[idx].sum()) if len(idx) else 0.0
        if sc > best:
            best, phase = sc, ph
    beats = [round(float(t), 3) for t in np.arange(phase, total, period)]
    bar_best, bar0 = -1.0, 0
    for k in range(4):
        idx = (np.array(beats[k::4]) * fps).astype(int)
        idx = idx[idx < len(env)]
        sc = float(env[idx].sum()) if len(idx) else 0.0
        if sc > bar_best:
            bar_best, bar0 = sc, k
    return {"bpm": round(bpm, 1), "beat_s": round(period, 3), "beats": beats, "bars": beats[bar0::4], "length_s": round(total, 2)}


def snap(t, grid_times):
    """The grid line at or before t (never after: a cut never lands late)."""
    prev = [g for g in grid_times if g <= t + 1e-6]
    return prev[-1] if prev else (grid_times[0] if grid_times else t)


def phrase_onset(phrase, heard, full=False, after=-1.0):
    """Onset of the first word of `phrase` in the sung words (sequence match of its first three words), searching
    only after `after` seconds so a repeated phrase finds its own line, not an earlier one (V7.91.4).
    full=True also returns the end of the sung word just before it (the previous line's last word)."""
    want = words_of(phrase)[:3]
    if not want:
        return (None, None) if full else None
    flat = [(w, x["t"], x.get("end", x["t"])) for x in heard for w in words_of(x["w"])]
    for k in range(len(flat) - len(want) + 1):
        if flat[k][1] > after and [f[0] for f in flat[k:k + len(want)]] == want:
            return (flat[k][1], flat[k - 1][2] if k else None) if full else flat[k][1]
    return (None, None) if full else None


LEAD = 2 / 24      # the picture lands 2 frames before the line's first sung word (§30H)
BEAT_PULL = 0.25   # a beat this close before the word takes the cut instead (on the beat, never early)
TAIL = 0.15        # sung words run legato: the transcript ends a word where the next begins, so a cut up to
                   # 0.15 s before that end is still clear of the line before; earlier than that is EARLY


def lyric_cuts(rows, g, heard, skip=0.4, handle=0.5):
    """§3C sung (V7.91.4, L56): each row cuts on the first sung word of its `phrase`, 2 frames ahead of it, or on a
    beat at most 0.25 s before that word — never a full beat early — and never while the previous line's last sung
    word is still sounding (EARLY). It holds to the next row's cut; the first row starts at 0, the last ends with
    the track. The old rule (the beat at or before the word) brought the picture in up to one beat early (0.8 s at
    74 bpm), under the end of the line before."""
    import math
    beats = g["beats"]
    cuts, fails, last_on = [], [], -1.0
    for i, r in enumerate(rows):
        if i == 0:
            cuts.append(0.0)
            if r.get("phrase"):
                last_on = phrase_onset(r["phrase"], heard) or -1.0
            continue
        on, prev_end = phrase_onset(r.get("phrase", ""), heard, full=True, after=last_on + 0.01) if r.get("phrase") else (None, None)
        if on is not None:
            last_on = on
        if on is None:
            fails.append(f"NOT SUNG: {r['beat']} — its phrase {r.get('phrase')!r} is not heard in the track")
            cuts.append(cuts[-1] + 2.0)
            continue
        near = [b for b in beats if on - BEAT_PULL <= b <= on]
        cut = float(near[-1]) if near else on - LEAD
        if prev_end is not None and cut < prev_end - TAIL:
            cut = max(cut, min(prev_end - TAIL, on - LEAD))
        if prev_end is not None and cut < prev_end - TAIL:
            fails.append(f"EARLY: {r['beat']} cuts at {cut:.2f}s while the line before is still sung (to {prev_end:.2f}s)")
        cuts.append(round(cut, 3))
    out = []
    for i, r in enumerate(rows):
        end = cuts[i + 1] if i + 1 < len(rows) else g["length_s"]
        on = round(end - cuts[i], 3)
        call = min(15, max(3, math.ceil(on + skip + handle - 1e-9)))
        out.append({"beat": r["beat"], "phrase": r.get("phrase", ""), "cut_s": round(cuts[i], 3), "end_s": round(end, 3),
                    "on_screen_s": on, "call_s": call})
        if on < 2.0 and not r.get("flash_ok"):
            fails.append(f"FLASH: {r['beat']} on screen {on}s < 2.0s — merge it with the next line's row")
        if on + skip + handle > 15:
            fails.append(f"SPLIT: {r['beat']} needs {on}s, over one 15s clip — split the row")
    return {"grid": {k: g[k] for k in ("bpm", "beat_s", "length_s")}, "rows": out, "fails": fails,
            "status": "PASS" if not fails else "FAIL"}


def cut_sheet(cue, rows, g, hold_bars=2, skip=0.4, handle=0.5):
    """§3C/§30H on a music video. Rows run in order; each holds its bars (default 2) from its cut, cutting on bar
    lines; the last row of a section ends exactly where the next section's music begins (its edge: the nearest bar
    line within half a beat, else the section's own start — the composed change), and the last row ends with the
    track. Fails: FLASH (under 2.0s), SPLIT (over one 15s clip), OVERFLOW (a section's rows need more time than
    its music), HOLE (the picture stops before the track). Call length = time on screen + 0.4s + 0.5s, rounded
    up, Kling 3-15s (E6)."""
    import math
    bars, half = g["bars"], g["beat_s"] / 2
    secs = {s["name"]: s for s in cue["sections"]}

    def edge(t):
        near = min(bars, key=lambda b: abs(b - t)) if bars else t
        return float(near) if abs(near - t) <= half else float(t)

    out, fails, t = [], [], 0.0
    for i, r in enumerate(rows):
        start = float(t)
        n = max(1, int(r.get("bars", hold_bars)))
        later = [b for b in bars if b > start + half]
        end = float(later[n - 1]) if len(later) >= n else g["length_s"]
        nxt = rows[i + 1] if i + 1 < len(rows) else None
        if nxt is None:
            end = g["length_s"]
        elif nxt.get("section") != r.get("section") and nxt.get("section") in secs:
            e = edge(secs[nxt["section"]]["start"])
            if e <= start + 1e-6:
                fails.append(f"OVERFLOW: section '{r.get('section')}' needs more time than its music — fewer bars or fewer rows before {nxt['beat']}")
            end = e
        on = round(end - start, 3)
        call = min(15, max(3, math.ceil(on + skip + handle - 1e-9)))
        out.append({"beat": r["beat"], "section": r.get("section"), "text": r.get("text", ""), "cut_s": round(start, 3),
                    "end_s": round(end, 3), "on_screen_s": on, "call_s": call})
        if on < 2.0:
            fails.append(f"FLASH: {r['beat']} on screen {on}s < 2.0s — give it more bars or merge the rows")
        if on + skip + handle > 15:
            fails.append(f"SPLIT: {r['beat']} needs {on}s, over one 15s clip — split the row")
        t = end
    if out and abs(out[-1]["end_s"] - g["length_s"]) > 0.05:
        fails.append("HOLE: the picture stops before the track ends")
    return {"grid": {k: g[k] for k in ("bpm", "beat_s", "length_s")}, "rows": out, "fails": fails,
            "status": "PASS" if not fails else "FAIL"}


def render(sheet, track, clips, out, w=1080, h=1920, fps=24, skip=0.4):
    """Rough cut of a music video: each row's clip from its in-point for its time on screen, scaled to 9:16,
    joined frame-exact, the track laid under it whole. No speed change, no slowed clip."""
    import tempfile
    tmp = Path(tempfile.mkdtemp())
    parts = []
    for i, r in enumerate(sheet["rows"]):
        src = clips.get(r["beat"])
        if not src:
            sys.exit(f"no clip for {r['beat']}")
        seg = tmp / f"{i:03d}.mp4"
        subprocess.run([FF, "-v", "error", "-y", "-ss", str(skip), "-i", src, "-t", str(r["on_screen_s"]), "-an",
                        "-vf", f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={fps},setsar=1",
                        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "16", str(seg)], check=True)
        parts.append(seg)
    lst = tmp / "list.txt"
    lst.write_text("".join(f"file '{p}'\n" for p in parts))
    subprocess.run([FF, "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-i", str(track),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", str(out)], check=True)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("what", choices=["plan", "compose", "check", "cuts", "render"])
    ap.add_argument("cue")
    ap.add_argument("track", nargs="?")
    ap.add_argument("--rows", help="cuts/render: JSON list of the act-map rows in order: {beat, section, bars?, text?, clip?}")
    ap.add_argument("--hold-bars", type=int, default=2)
    ap.add_argument("--words", help="cuts/render on a sung track: the word timings saved by check --words-out (else transcribed)")
    ap.add_argument("--words-out", help="check on a sung track: save the sung word timings here")
    ap.add_argument("--out")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--register", help="§40A register: " + ", ".join(REGISTERS))
    a = ap.parse_args()
    cue = apply_register(json.loads(Path(a.cue).read_text()), a.register or json.loads(Path(a.cue).read_text()).get("register"))
    if a.what in ("cuts", "render"):
        if not (a.track and a.rows):
            sys.exit(f"{a.what} needs the track and --rows")
        rows = json.loads(Path(a.rows).read_text())
        g = grid(load(a.track), cue.get("bpm"))
        if cue.get("sung") and any(r.get("phrase") for r in rows):
            heard = json.loads(Path(a.words).read_text()) if a.words else transcribe(a.track)
            sheet = lyric_cuts(rows, g, heard)
        else:
            sheet = cut_sheet(cue, rows, g, a.hold_bars)
        if a.what == "cuts":
            print(json.dumps(sheet, indent=2))
            sys.exit(0 if sheet["status"] == "PASS" else 2)
        if sheet["status"] != "PASS":
            print(json.dumps(sheet["fails"], indent=2))
            sys.exit(2)
        if not a.out:
            sys.exit("--out is required")
        render(sheet, a.track, {r["beat"]: r.get("clip") for r in rows}, a.out)
        print(json.dumps({"status": "OK", "rough_cut": a.out, "rows": len(sheet["rows"])}, indent=2))
        return
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
        if a.words_out and isinstance(r.get("vocals"), dict) and r["vocals"].get("words"):
            Path(a.words_out).write_text(json.dumps(r["vocals"]["words"]))
        if isinstance(r.get("vocals"), dict):
            r["vocals"].pop("words", None)
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
