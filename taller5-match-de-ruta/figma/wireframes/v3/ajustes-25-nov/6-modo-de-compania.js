const vars=await figma.variables.getLocalVariablesAsync('COLOR');const V=n=>vars.find(x=>x.name===n);
const paint=n=>figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',V(n));
const ST={pista:'S:16c16e3a51a15bb6c352175d9c969ea52fab8d83,'};
for(const [f,s] of [['Figtree','Regular'],['Figtree','Medium'],['Figtree','SemiBold'],['Figtree','Bold'],['Bricolage Grotesque','Bold'],['Bricolage Grotesque','ExtraBold']])await figma.loadFontAsync({family:f,style:s});
const log=[];
const cp=figma.root.children.find(p=>p.name==='Sistema de diseño · Componentes');await cp.loadAsync();
const opSet=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Opción');const sel=opSet.children.find(v=>v.name==='Estado=Seleccionado'),def=opSet.children.find(v=>v.name==='Estado=Default');
const ok=Object.keys(opSet.componentPropertyDefinitions);const kT=ok.find(k=>k.startsWith('Título')),kDe=ok.find(k=>k.startsWith('Descripción')),kC=ok.find(k=>k.startsWith('Con descripción'));
const avSet=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Aviso');const avInfo=avSet.children.find(v=>v.name==='Tipo=Info');const kM=Object.keys(avSet.componentPropertyDefinitions).find(k=>k.startsWith('Mensaje'));
const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const S={};for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))S[f.name.split(' ')[0]]=f;}}
async function setText(scr,from,to){const t=S[scr].findOne(n=>n.type==='TEXT'&&n.characters===from);if(!t){log.push('NO '+scr+' «'+from+'»');return null;}
 const ref=t.componentPropertyReferences&&t.componentPropertyReferences.characters;
 if(ref){let p=t.parent;while(p&&!(p.type==='INSTANCE'&&p.componentProperties&&p.componentProperties[ref]))p=p.parent;if(p){p.setProperties({[ref]:to});log.push(scr+' prop «'+to+'»');return t;}}
 const fonts=t.fontName===figma.mixed?t.getRangeAllFontNames(0,t.characters.length):[t.fontName];for(const f of fonts)await figma.loadFontAsync(f);t.characters=to;if(t.textAutoResize==='NONE')t.textAutoResize='HEIGHT';log.push(scr+' «'+to+'»');return t;}
// H03
{const s=S.H03;const lab=s.findOne(n=>n.type==='TEXT'&&n.characters==='Con quién viajas');const g=lab.parent;const chips=g.children.find(n=>n.name==='Chips');
 const opts=figma.createFrame();opts.name='Modos';opts.fills=[];opts.layoutMode='VERTICAL';opts.itemSpacing=10;g.insertChild(g.children.indexOf(chips),opts);opts.layoutAlign='STRETCH';opts.primaryAxisSizingMode='AUTO';chips.remove();
 const M=[[sel,'Solo mujeres','Solo ves mujeres verificadas y solo te ven mujeres.'],[def,'Solo hombres','Solo ves hombres verificados y solo te ven hombres.'],[def,'Cualquier persona','Ves a quienes también aceptan viajar con cualquier persona.']];
 for(const [v,t,d] of M){const i=v.createInstance();opts.appendChild(i);i.layoutAlign='STRETCH';i.setProperties({[kT]:t,[kDe]:d,[kC]:true});}
 const n=figma.createText();g.appendChild(n);await n.setTextStyleIdAsync(ST.pista);n.characters='Solo hay match si las dos personas eligieron modos compatibles.';n.fills=[paint('neutral/600')];n.layoutAlign='STRETCH';n.textAutoResize='HEIGHT';
 await setText('H03','Con quién viajas','Modo de compañía');
 const cont=s.findOne(n=>n.name==='Contenido');const sum=cont.children.reduce((a,c)=>a+c.height,0)+cont.itemSpacing*(cont.children.length-1);log.push('H03 contenido '+Math.round(sum)+' de '+Math.round(cont.height));}
// E02
{const s=S.E02;await setText('E02','Solo mujeres','Modo solo mujeres');const cont=s.findOne(n=>n.name==='Contenido');const chips=cont.children.find(n=>n.name==='Chips');
 const a=avInfo.createInstance();cont.insertChild(cont.children.indexOf(chips)+1,a);a.layoutAlign='STRETCH';a.setProperties({[kM]:'Modo solo mujeres: solo ves y te ven mujeres verificadas. Lo cambias en Perfil.'});}
// E03: agregar Solo hombres
{const s=S.E03;const t=s.findOne(n=>n.type==='TEXT'&&n.characters==='Cualquiera');let chip=t.parent;while(chip.type!=='INSTANCE')chip=chip.parent;const row=chip.parent;
 const nc=chip.clone();row.insertChild(row.children.indexOf(chip),nc);const k=Object.keys(nc.componentProperties).find(x=>x.startsWith('Texto'));nc.setProperties({[k]:'Solo hombres'});
 chip.setProperties({[k]:'Cualquier persona'});row.layoutWrap='WRAP';row.counterAxisSpacing=8;if(row.layoutMode==='HORIZONTAL'&&row.primaryAxisSizingMode==='AUTO'){row.primaryAxisSizingMode='FIXED';row.layoutAlign='STRETCH';}
 log.push('E03 chips '+row.children.map(c=>c.findOne(x=>x.type==='TEXT').characters).join(', ')+' ancho '+Math.round(row.width)+' alto '+Math.round(row.height));}
// D05, H02
await setText('D05','Martes y jueves · 9:00 p. m. (± 15 min)','Martes y jueves · 9:00 p. m. (± 15 min) · Modo solo mujeres');
await setText('H02','Espera + trayecto','Solo mujeres · espera y trayecto');
return log;
