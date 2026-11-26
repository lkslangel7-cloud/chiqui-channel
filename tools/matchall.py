import json,re,subprocess,html,difflib,sys,os,glob
out=sys.argv[1]
SC=[]
for e in range(26,41):
    for s in json.load(open(f'/home/user/chiqui-channel/episodes/ep{e}/scenes.json')): SC.append((f'ep{e}',s['id'],s['img']))
for code in sys.argv[2:]:
    t=html.unescape(subprocess.run(["curl","-sSL","-m","40",f"https://higgsfield.ai/s/{code}"],capture_output=True,text=True).stdout)
    m=re.search(r'line-clamp-2">([^<]+)<',t); p=m.group(1).strip() if m else ""
    r=sorted(((difflib.SequenceMatcher(None,p,i).ratio(),e,sid) for e,sid,i in SC),reverse=True)[:3]
    print(code,[(e,s,round(x,3)) for x,e,s in r])
