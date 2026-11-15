import re,sys,os,json
SRC=sys.argv[1];OUT=sys.argv[2];os.makedirs(OUT,exist_ok=True)
V={'neutral/900':'#0a0a0a','neutral/800':'#27272a','neutral/700':'#3f3f46','neutral/600':'#5e5e66','neutral/500':'#71717a','neutral/400':'#a1a1aa','neutral/300':'#d4d4d8','neutral/200':'#e4e4e7','neutral/100':'#f4f4f5','neutral/0':'#ffffff','primario/500':'#5b3df5','primario/700':'#3f22c9','primario/100':'#eeebfe','candidata/c-coral':'#e8461e','candidata/b-lima':'#c8f560','ilustracion/piel-1':'#c68642','ilustracion/piel-2':'#8d5524','ilustracion/piel-3':'#e0ac69'}
LIGHT={'currentcolor':'primario/500','#090814':'neutral/900','#2f2e41':'neutral/900','#3f3d56':'neutral/700','#3a3768':'primario/700','#575a89':'primario/700',
'#e6e6e6':'neutral/300','#e5e5e5':'neutral/300','#e4e4e4':'neutral/300','#dedede':'neutral/300','#d6d6e3':'neutral/300','#f2f2f2':'neutral/200','#f0f0f0':'neutral/200',
'#ccc':'neutral/400','#cbcbcb':'neutral/400','#cacaca':'neutral/400','#b3b3b3':'neutral/400','#707070':'neutral/600','#fff':'neutral/0',
'#ffb8b8':'ilustracion/piel-3','#ffb6b6':'ilustracion/piel-3','#ffb9b9':'ilustracion/piel-3','#feb8b8':'ilustracion/piel-3','#9f616a':'ilustracion/piel-2','#a0616a':'ilustracion/piel-2','#ed9da0':'ilustracion/piel-1','#ff6584':'candidata/c-coral'}
DARK=dict(LIGHT);DARK.update({'#3f3d56':'neutral/600','#e6e6e6':'neutral/500','#e5e5e5':'neutral/500','#f2f2f2':'neutral/700','#f0f0f0':'neutral/700','#ccc':'neutral/400','#d6d6e3':'neutral/400','#fff':'neutral/0','#ff6584':'candidata/b-lima'})
def adapt(name,mode):
    s=open(f'{SRC}/{name}.svg').read();M=LIGHT if mode=='light' else DARK;miss=set()
    s=re.sub(r'<title>.*?</title>','',s,flags=re.S)
    usados=set(re.findall(r'url\(#([^)]+)\)',s))
    s=re.sub(r'\s(data-name|xmlns:xlink|role|artist|source)="[^"]*"','',s)
    s=re.sub(r'\sid="([^"]*)"',lambda m:m.group(0) if m.group(1) in usados else '',s)
    def rep(m):
        k=m.group(2).lower()
        if k in('none',) or k.startswith('url'):return m.group(0)
        if k not in M:miss.add(k);return m.group(0)
        return m.group(1)+V[M[k]]
    s=re.sub(r'((?:fill|stroke|stop-color)="\s*)(#[0-9a-fA-F]{3,6}|currentColor|none|url\([^)]*\))',rep,s)
    s=re.sub(r'((?:fill|stroke)\s*:\s*)(#[0-9a-fA-F]{3,6}|currentColor)',rep,s)
    if miss:print('MISSING',name,miss)
    open(f'{OUT}/{name}.svg','w').write(s);return len(s)
J=json.load(open(sys.argv[3]))
for t,(n,mode) in J.items():print(t,n,mode,adapt(n,mode))
