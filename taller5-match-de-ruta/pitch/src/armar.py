# Arma la presentación en un solo archivo: mete las imágenes y el SVG dentro del HTML.
# Uso: python3 src/armar.py   (desde la carpeta pitch)
import base64,json,os,re
here=os.path.dirname(os.path.abspath(__file__));root=os.path.dirname(here)
src=open(os.path.join(here,'pitch.src.html'),encoding='utf-8').read()
img={}
for f in sorted(os.listdir(os.path.join(root,'img'))):
    if f.endswith('.webp'):
        img[f[:-5]]='data:image/webp;base64,'+base64.b64encode(open(os.path.join(root,'img',f),'rb').read()).decode()
svg=open(os.path.join(root,'img','personas.svg'),encoding='utf-8').read()
out=src.replace('/*__IMG__*/{}/*__IMG__*/',json.dumps(img)).replace('<!--SVG:personas-->',svg)
# 1) versión para publicar como artefacto (sin <html> ni <body>)
open(os.path.join(root,'match-pitch.artefacto.html'),'w',encoding='utf-8').write(out)
# 2) versión para abrir con doble clic
doc='<!doctype html>\n<html lang="es">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n<style>html,body{margin:0}[hidden]{display:none!important}</style>\n</head>\n<body>\n'+out+'\n</body>\n</html>\n'
open(os.path.join(root,'match-de-ruta-pitch.html'),'w',encoding='utf-8').write(doc)
print(len(out)//1024,'KB')
