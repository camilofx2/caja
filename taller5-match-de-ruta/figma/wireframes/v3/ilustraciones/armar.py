# Arma los scripts que se pegan en use_figma a partir de la plantilla y de los SVG ya recoloreados.
# Uso: python3 armar.py <carpeta con los SVG adaptados> <carpeta de salida>
import json,re,sys,os
src,out=sys.argv[1],sys.argv[2];os.makedirs(out,exist_ok=True)
here=os.path.dirname(os.path.abspath(__file__))
picks=json.load(open(os.path.join(here,'picks.json')))
tpl=open(os.path.join(here,'montar-en-figma.plantilla.js')).read()
grupos=[['Espera','Verificación','Ubicación'],['Encuentro','Llegada','Reporte','Aviso'],['Rutas','Paradero vacío']]
for i,g in enumerate(grupos):
    sv={};md={}
    for t in g:
        n,m=picks[t];s=open(f'{src}/{n}.svg').read()
        s=re.sub(r'\s+',' ',s);s=re.sub(r'> <','><',s);s=re.sub(r'(\d+\.\d{2})\d+',r'\1',s)
        sv[t]=s;md[t]=m
    code=tpl.replace('__SVGS__',json.dumps(sv,ensure_ascii=False)).replace('__MODE__',json.dumps(md,ensure_ascii=False))
    open(f'{out}/montar{i+1}.js','w').write(code);print(i+1,len(code))
