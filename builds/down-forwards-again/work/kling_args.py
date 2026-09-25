import json,sys
U="https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20260925_"
urls=dict(l.split() for l in open('urls.txt') if l.strip())
rows={r['beat_id']:r for r in json.load(open('../act_map.json'))}
out=[]
for b in sys.argv[1:]:
    f=f'../beats/{b}.v2.i2v.json'
    try: p=open(f).read()
    except FileNotFoundError: p=open(f'../beats/{b}.i2v.json').read()
    out.append(dict(beat=b,duration=str(rows[b]['duration']),prompt="图片1 is the first frame of this clip. "+p,url=U+urls[b]+".png"))
print(json.dumps(out,ensure_ascii=False))
