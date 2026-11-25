const vars=await figma.variables.getLocalVariablesAsync('COLOR');const V=n=>vars.find(x=>x.name===n);
const paint=n=>figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',V(n));
const ST={fuerte:'S:048b231bca83ffbd3ecb2a7c90ecf0f23332b040,',pista:'S:16c16e3a51a15bb6c352175d9c969ea52fab8d83,',label:'S:5c50006a44888e235ba164f37d15ee1b7892b22e,',titulo:'S:3e2348d5f489eff20cd166ab32a57415e517356d,'};
for(const [f,s] of [['Figtree','Regular'],['Figtree','Medium'],['Figtree','SemiBold'],['Figtree','Bold'],['Bricolage Grotesque','Bold'],['Bricolage Grotesque','ExtraBold']])await figma.loadFontAsync({family:f,style:s});
async function T(parent,str,style,color){const t=figma.createText();parent.appendChild(t);await t.setTextStyleIdAsync(ST[style]);t.characters=str;t.fills=[paint(color)];return t;}
const log=[];
// ---- componente Punto seguro
const cp=figma.root.children.find(p=>p.name==='Sistema de diseño · Componentes');await cp.loadAsync();await figma.setCurrentPageAsync(cp);
const fotoSet=await figma.getNodeByIdAsync('214:134');
const c=figma.createComponent();c.name='Punto seguro';cp.appendChild(c);c.x=fotoSet.x;c.y=fotoSet.y+fotoSet.height+120;
c.layoutMode='HORIZONTAL';c.itemSpacing=14;c.paddingLeft=16;c.paddingRight=16;c.paddingTop=14;c.paddingBottom=14;c.counterAxisAlignItems='CENTER';c.resize(380,72);c.primaryAxisSizingMode='FIXED';c.counterAxisSizingMode='AUTO';c.cornerRadius=16;c.fills=[paint('primario/100')];
const b=figma.createFrame();b.name='Escudo';c.appendChild(b);b.resize(40,40);b.cornerRadius=20;b.fills=[paint('primario/500')];b.layoutMode='HORIZONTAL';b.primaryAxisAlignItems='CENTER';b.counterAxisAlignItems='CENTER';
const ic=(await figma.getNodeByIdAsync('109:39')).createInstance();b.appendChild(ic);ic.resize(22,22);for(const v of ic.findAll(n=>'fills' in n&&n.fills!==figma.mixed&&n.fills.length))v.fills=[paint('neutral/0')];for(const v of ic.findAll(n=>'strokes' in n&&n.strokes.length))v.strokes=[paint('neutral/0')];
const col=figma.createFrame();col.name='Texto';col.fills=[];c.appendChild(col);col.layoutMode='VERTICAL';col.itemSpacing=2;col.layoutGrow=1;col.counterAxisSizingMode='FIXED';col.primaryAxisSizingMode='AUTO';
const eb=await T(col,'PUNTO SEGURO','pista','primario/700');eb.fontName={family:'Figtree',style:'Bold'};eb.letterSpacing={unit:'PERCENT',value:8};
const lugar=await T(col,'Portería principal de la U','fuerte','neutral/900');const det=await T(col,'Vigilancia en la entrada','pista','neutral/600');
for(const t of [eb,lugar,det]){t.layoutAlign='STRETCH';t.textAutoResize='HEIGHT';}
const kL=c.addComponentProperty('Lugar','TEXT','Portería principal de la U');const kD=c.addComponentProperty('Detalle','TEXT','Vigilancia en la entrada');
lugar.componentPropertyReferences={characters:kL};det.componentPropertyReferences={characters:kD};
c.description='Lugar de encuentro con vigilancia definido por la plataforma: portería de universidad, recepción o CAI.';
log.push('Punto seguro '+c.id);
// ---- pantallas
const wp=figma.root.children.find(p=>p.name.startsWith('Pantallas en alta'));await wp.loadAsync();await figma.setCurrentPageAsync(wp);
const S={};for(const sec of wp.children){if(sec.type!=='SECTION')continue;for(const f of sec.children){if(f.type==='FRAME'&&/^[A-I]\d\d/.test(f.name))S[f.name.split(' ')[0]]=f;}}
async function setText(scr,from,to){const t=S[scr].findOne(n=>n.type==='TEXT'&&n.characters===from);if(!t){log.push('NO '+scr+' «'+from+'»');return null;}
 const ref=t.componentPropertyReferences&&t.componentPropertyReferences.characters;
 if(ref){let p=t.parent;while(p&&!(p.type==='INSTANCE'&&p.componentProperties&&p.componentProperties[ref]))p=p.parent;if(p){p.setProperties({[ref]:to});log.push(scr+' prop «'+to+'»');return t;}}
 const fonts=t.fontName===figma.mixed?t.getRangeAllFontNames(0,t.characters.length):[t.fontName];for(const f of fonts)await figma.loadFontAsync(f);t.characters=to;log.push(scr+' «'+to+'»');return t;}
function punto(lugarTxt,detTxt){const i=c.createInstance();i.setProperties({[kL]:lugarTxt,[kD]:detTxt});return i;}
// E04
await setText('E04','Se unen · encuentro 8:55 p. m. en la entrada norte','Se unen · llegan caminando juntas desde la U');
{const cont=S.E04.findOne(n=>n.name==='Contenido');const i=punto('Portería principal de la U','Se encuentran a las 8:50 p. m. Hay vigilancia en la entrada y caminan juntas 8 min a la estación.');cont.insertChild(1,i);i.layoutAlign='STRETCH';}
await setText('E04','Espera + trayecto','Solo mujeres · espera y trayecto');
// E05
await setText('E05','Te espero en la entrada norte','Te espero en la portería');
await setText('E05','Si acepta, se habilitan el chat, el punto de encuentro y el código para reconocerse.','Si acepta, se habilitan el chat y el código para reconocerse. Solo proponemos puntos con vigilancia.');
{const sheet=S.E05.findOne(n=>n.name==='Hoja inferior');const bottom=sheet.y+sheet.height;const g=figma.createFrame();g.name='Punto de encuentro';g.fills=[];g.layoutMode='VERTICAL';g.itemSpacing=12;sheet.insertChild(3,g);g.layoutAlign='STRETCH';g.primaryAxisSizingMode='AUTO';
 await T(g,'Dónde se encuentran','label','neutral/900');
 const op=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Opción');const sel=op.children.find(v=>v.name==='Estado=Seleccionado'),def=op.children.find(v=>v.name==='Estado=Default');
 const keys=Object.keys(op.componentPropertyDefinitions);const kT=keys.find(k=>k.startsWith('Título')),kDe=keys.find(k=>k.startsWith('Descripción')),kC=keys.find(k=>k.startsWith('Con descripción'));
 const o1=sel.createInstance();g.appendChild(o1);o1.layoutAlign='STRETCH';o1.setProperties({[kT]:'Portería principal de la U · punto seguro',[kDe]:'Vigilancia en la entrada · a 8 min de la estación',[kC]:true});
 const o2=def.createInstance();g.appendChild(o2);o2.layoutAlign='STRETCH';o2.setProperties({[kT]:'CAI junto a la Estación Calle 45 · punto seguro',[kDe]:'Policía en el lugar · a 1 min de la estación',[kC]:true});
 sheet.y=bottom-sheet.height;log.push('E05 hoja '+Math.round(sheet.height)+' y '+Math.round(sheet.y));}
// E07, E09, F01
await setText('E07','Te espero en la entrada norte','Te espero en la portería');
await setText('E09','Encuentro · 8:55 p. m.','Encuentro · 8:50 p. m. · punto seguro');
await setText('E09','Entrada norte, Estación Calle 45','Portería principal de la U');
await setText('E09','Listo, te espero adentro, junto a la taquilla.','Listo, te espero junto al vigilante de la portería.');
await setText('F01','Encuentro 8:55 p. m. · entrada norte Calle 45','Encuentro 8:50 p. m. · portería de la U');
// F02
await setText('F02','tú y la entrada norte de la estación','Punto seguro · portería de la U');
await setText('F02','Entrada norte · Calle 45','Portería principal de la U');
// F03
{const cont=S.F03.findOne(n=>n.name==='Contenido');const per=cont.children.findIndex(n=>n.name==='Persona');const i=punto('Estás en un punto seguro','Portería principal de la U · el vigilante está a la vista.');cont.insertChild(per+1,i);i.layoutAlign='STRETCH';}
// F05: foto + código
{const s=S.F05;await setText('F05','¿Laura te dijo este código?','¿Es Laura?');await setText('F05','Pídele que te lo diga en voz alta','2 · Pídele que te diga el código');
 const cont=s.findOne(n=>n.name==='Contenido');const ti=cont.children.findIndex(n=>n.name==='Título');
 const blk=figma.createFrame();blk.name='Foto verificada';blk.fills=[];blk.layoutMode='VERTICAL';blk.itemSpacing=12;blk.counterAxisAlignItems='CENTER';cont.insertChild(ti+1,blk);blk.layoutAlign='STRETCH';blk.primaryAxisSizingMode='AUTO';
 const ring=figma.createFrame();ring.name='Aro';blk.appendChild(ring);ring.resize(128,128);ring.cornerRadius=64;ring.fills=[];ring.strokes=[paint('primario/500')];ring.strokeWeight=4;ring.strokeAlign='INSIDE';ring.layoutMode='HORIZONTAL';ring.primaryAxisAlignItems='CENTER';ring.counterAxisAlignItems='CENTER';
 const f=(await figma.getNodeByIdAsync('214:60')).createInstance();ring.appendChild(f);f.resize(112,112);f.name='Foto · Laura';
 const cap=await T(blk,'1 · ¿Es la persona de la foto?','fuerte','neutral/900');cap.textAlignHorizontal='CENTER';
 const sub=await T(blk,'Foto tomada en el momento al verificarse · marzo de 2026','pista','neutral/600');sub.textAlignHorizontal='CENTER';
 await setText('F05','Sí, coincide','Sí, es ella y coincide');await setText('F05','No coincide','No es ella o no coincide');}
return log;
