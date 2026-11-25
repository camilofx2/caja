const KEY='Foto#214:0';const ID={Daniela:'214:48',Laura:'214:60',Sara:'214:68',Camila:'214:87',Gloria:'214:102',Andrés:'214:123'};
const comp={};for(const [k,id] of Object.entries(ID))comp[k]=await figma.getNodeByIdAsync(id);
const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const screens={};for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))screens[f.name.split(' ')[0]]=f;}}
const log=[];let set=0;const unknown=[];
for(const [c,s] of Object.entries(screens)){for(const i of s.findAll(n=>n.type==='INSTANCE')){const m=await i.getMainComponentAsync();if(!m||!m.parent||m.parent.name!=='Persona')continue;
  const t=i.findOne(x=>x.type==='TEXT'&&x.name==='Nombre');const name=t?t.characters:'';const who=Object.keys(ID).find(k=>name.startsWith(k));
  if(!who){unknown.push(c+':'+name);continue;}
  try{i.setProperties({[KEY]:ID[who]});set++;}catch(e){log.push('ERR '+c+' '+name+' '+e.message);}}}
const LOOSE={C06:'Daniela',E06:'Laura',G02:'Laura',G07:'Laura',H07:'Gloria',I03:'Daniela',I09:'Daniela'};
for(const [c,who] of Object.entries(LOOSE)){const s=screens[c];const e=s.findOne(n=>n.type==='ELLIPSE'&&n.name==='Foto');if(!e){log.push('sin foto '+c);continue;}
 const par=e.parent;const idx=par.children.indexOf(e);const d=Math.round(e.width);const i=comp[who].createInstance();i.name='Foto · '+who;par.insertChild(idx,i);
 if(par.layoutMode&&par.layoutMode!=='NONE'){i.resize(d,d);i.layoutAlign=e.layoutAlign;}else{i.resize(d,d);i.x=e.x;i.y=e.y;}
 const ctx=s.findAll(n=>n.type==='TEXT'&&n.visible).map(t=>t.characters.slice(0,40)).slice(1,4).join(' | ');e.remove();log.push(c+'→'+who+' ('+ctx+')');}
return {set,unknown,log};
