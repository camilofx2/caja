const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const S={};for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))S[f.name.split(' ')[0]]=f;}}
const sh=S.E03.findOne(n=>n.name==='Hoja inferior');sh.y=S.E03.height-sh.height;
const t=S.E02.findOne(n=>n.type==='TEXT'&&n.characters==='Modo solo mujeres');let p=t.parent;while(p.type!=='INSTANCE')p=p.parent;const k=Object.keys(p.componentProperties).find(x=>x.startsWith('Texto'));p.setProperties({[k]:'Solo mujeres'});
const ip=figma.root.children.find(p=>p.name.includes('Identidad'));await ip.loadAsync();
const hexes=ip.findAll(n=>n.type==='TEXT'&&/#[0-9A-Fa-f]{6}|Figtree|neutral|Neutr/.test(n.characters)).map(n=>{let f=n;while(f.parent&&f.parent.type!=='PAGE')f=f.parent;return f.name+' | '+n.id+' | '+n.characters.replace(/\n/g,' / ').slice(0,90);});
let maxX=0,minY=1e9;for(const n of ip.children){maxX=Math.max(maxX,n.x+n.width);minY=Math.min(minY,n.y);}
const frames=ip.children.map(n=>n.name+'|'+Math.round(n.x)+','+Math.round(n.y)+','+Math.round(n.width)+'x'+Math.round(n.height));
return {e03:Math.round(sh.y),hexes,frames,maxX};
