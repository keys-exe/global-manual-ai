"""Write board cards VO-T<n>-HK<k> for one take from split_<take>.json + uploaded asset ids."""
import json,sys,time,os
take=sys.argv[1]; ids=sys.argv[2:7]
S='/tmp/claude-0/-home-user-global-manual-ai/969496f6-d119-5739-9d80-a2425c1aa43a/scratchpad/'
d=json.load(open(f'split_{take}.json'))[take]; log=json.load(open('full/tts_log.json'))[take]
now=int(time.time()*1000); V="ABCDE"
for k in range(1,6):
    x=d['parts'][f'V{k}']; t=x['trim']; v=t['verify']
    notes=[]
    if t['source_end_clipped']: notes.append(f"TTS cut the last word off (generation ends at {t['source_end_db']} dB) — fails §22U step 10 (4); not the working take")
    if v['breaths_left']: notes.append(f"breaths left mid-phrase at {', '.join(str(b[0])+'s' for b in v['breaths_left'])} (kept: a mid-phrase cut would clip a word)")
    f=f"board/VO_{take}_HK{k}.mp4"
    doc={"build":"stryde-lost-moments","beat":f"VO-{take}-HK{k}","stage":"vo","kind":"audio","act":f"Hook {k}",
      "title":f"VO {take} · Variant {V[k-1]} (Hook {k} + its body), house cut",
      "line":open(f'V{k}.lines.txt').read().strip(),
      "videoAsset":ids[k-1],"videoParts":[ids[k-1]],"videoType":"video/mp4","videoConnector":"ElevenLabs API","model":"eleven_v3 · voice Lost D20hb4HQVPwtiDd89W7m · stability 0.5 · one request, all five variants",
      "duration":round(x['trim_s'],2),"videoAt":now,"updatedAt":now,"status":"review",
      "note":"Raw "+str(x['raw_s'])+"s → house cut "+str(x['trim_s'])+"s · words verbatim (Whisper spelling variants only) · "+("; ".join(notes) if notes else "verify PASS"),
      "videoVersions":[{"v":1,"asset":ids[k-1],"parts":[ids[k-1]],"type":"video/mp4","connector":"ElevenLabs API","model":"eleven_v3","size":os.path.getsize(f),"at":now,"note":f"request {log['request_id']} · MP3 stream in MP4 container, not re-encoded"}]}
    json.dump(doc,open(S+f'VO-{take}-HK{k}.json','w'))
print("ok")
