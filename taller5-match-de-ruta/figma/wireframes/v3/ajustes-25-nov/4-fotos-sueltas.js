const ID={Daniela:'214:48',Laura:'214:60',Sara:'214:68',Camila:'214:87',Gloria:'214:102',Andrés:'214:123'};
const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const screens={};for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))screens[f.name.split(' ')[0]]=f;}}
const LOOSE={C06:'Daniela',E06:'Laura',G02:'Laura',G07:'Laura',H07:'Gloria',I03:'Daniela',I09:'Daniela'};const log=[];
for(const [c,who] of Object.entries(LOOSE)){const s=screens[c];const f=s.findOne(n=>n.name==='Foto'&&n.type==='FRAME');if(!f){log.push('no '+c);continue;}
 const kids=f.children.map(k=>k.type+':'+k.name+':'+Math.round(k.width));const e=f.children.find(k=>k.type==='ELLIPSE'&&k.width>=80);
 if(!e){log.push(c+' sin elipse '+kids.join(','));continue;}
 const comp=await figma.getNodeByIdAsync(ID[who]);const i=comp.createInstance();i.name='Foto · '+who;const idx=f.children.indexOf(e);f.insertChild(idx,i);i.resize(e.width,e.height);i.x=e.x;i.y=e.y;e.remove();
 const ctx=s.findAll(n=>n.type==='TEXT'&&n.visible).map(t=>t.characters.slice(0,34)).slice(1,3).join(' | ');log.push(c+'→'+who+' ['+kids.join(',')+'] '+ctx);}
return log;
