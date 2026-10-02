import json,subprocess,sys,os
idx=json.load(open('batch_index.json')); jobs=json.load(open('jobs.json'))
urls=json.load(open('urls.json')) if os.path.exists('urls.json') else {}
for a in sys.argv[1:]:
    i,ts=a.split(':'); j=jobs[i]; b,p,d,t=idx[i]
    url=f"https://d8j0ntlcm91z4.cloudfront.net/user_3FfA2p8f93sSZ3B9iUyv7t5zrAL/hf_20261002_{ts}_{j}.png"
    f=f"../{d}/{b}_{t}{p}.png"
    subprocess.run(['curl','-sS','-o',f,url],check=True)
    subprocess.run(['convert',f,'-resize','1000x','-quality','85',f.replace('.png','.jpg')])
    urls[f'{b}@{t}{p}']={'url':url,'job':j,'file':f}
json.dump(urls,open('urls.json','w'),indent=1)
print(len(urls))
