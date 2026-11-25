import re,sys,json
D,OUT=sys.argv[1],sys.argv[2]
PIEL={'piel-1':'#c68642','piel-2':'#8d5524','piel-3':'#e0ac69'}
P={'Daniela':('a-woman-avatar','piel-1'),'Laura':('female-avatar','piel-3'),'Sara':('avatar-traveler','piel-2'),'Camila':('businesswoman-avatar','piel-3'),'Gloria':('professional-woman-avatar','piel-1'),'Andrés':('young-man-avatar','piel-2')}
SKIN={'#ed9da0','#ffb6b6','#ffb8b8','#a0616a','#9f616a','#feb8b8','#ffb9b9'}
M={'#f2f2f2':'#eeebfe','#090814':'#14112b','#2f2e41':'#14112b','#3f3d56':'#3b3658','#3f3d58':'#3b3658','currentcolor':'#5b3df5','#d6d6e3':'#d5d2e5','#fff':'#ffffff','#ffffff':'#ffffff'}
res={}
for who,(f,p) in P.items():
    s=open(f'{D}/{f}.svg').read()
    s=re.sub(r'<title>.*?</title>','',s,flags=re.S)
    # quitar contornos de círculo sin relleno
    s=re.sub(r'<circle[^>]*fill="none"[^>]*/>',lambda m:re.sub(r'stroke="[^"]*"','stroke="none"',m.group(0)),s)
    s=re.sub(r'<defs>.*?</defs>','',s,flags=re.S);s=re.sub(r'\sclip-path="[^"]*"','',s)
    used=set(re.findall(r'url\(#([^)]+)\)',s))
    s=re.sub(r'\s(data-name|xmlns:xlink)="[^"]*"','',s)
    s=re.sub(r'\sid="([^"]*)"',lambda m:m.group(0) if m.group(1) in used else '',s)
    miss=set()
    def rep(m):
        k=m.group(2).lower()
        if k in SKIN: return m.group(1)+PIEL[p]
        if k in M: return m.group(1)+M[k]
        if k=='none':return m.group(0)
        miss.add(k);return m.group(0)
    s=re.sub(r'((?:fill|stroke)=")(#[0-9a-fA-F]{3,6}|currentColor|none)',rep,s)
    s=re.sub(r'\s+',' ',s);s=re.sub(r'> <','><',s);s=re.sub(r'(\d+\.\d{2})\d+',r'\1',s)
    res[who]=s
    if miss:print('MISS',who,miss)
json.dump(res,open(OUT,'w'),ensure_ascii=False)
print({k:len(v) for k,v in res.items()})
