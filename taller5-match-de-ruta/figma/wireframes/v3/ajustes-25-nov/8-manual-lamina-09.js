const vars=await figma.variables.getLocalVariablesAsync('COLOR');const V=n=>vars.find(x=>x.name===n);
const paint=n=>figma.variables.setBoundVariableForPaint({type:'SOLID',color:{r:0,g:0,b:0}},'color',V(n));
for(const [f,s] of [['Figtree','Regular'],['Figtree','Medium'],['Figtree','SemiBold'],['Figtree','Bold'],['Bricolage Grotesque','Bold'],['Bricolage Grotesque','ExtraBold']])await figma.loadFontAsync({family:f,style:s});
const ip=figma.root.children.find(p=>p.name.includes('Identidad'));await ip.loadAsync();await figma.setCurrentPageAsync(ip);
const HX={'90:236':'#14112B','90:243':'#252140','90:250':'#5A5577','90:257':'#A29DBA','90:264':'#E7E4F2','90:270':'#F5F3FB'};const log=[];
for(const [id,h] of Object.entries(HX)){const t=await figma.getNodeByIdAsync(id);await figma.loadFontAsync(t.fontName);t.characters=h;}
{const t=await figma.getNodeByIdAsync('90:230');await figma.loadFontAsync(t.fontName);t.characters='Neutros con tinte noche';}
{const t=await figma.getNodeByIdAsync('91:6');await figma.loadFontAsync(t.fontName);t.characters='Bricolage Grotesque en títulos, Figtree en textos';}
// tablero 09
const F=figma.createFrame();F.name='09 · Ajustes del 25 de noviembre';ip.appendChild(F);F.x=0;F.y=4680;F.resize(1440,900);F.fills=[paint('neutral/0')];
F.layoutMode='VERTICAL';F.itemSpacing=40;F.paddingLeft=F.paddingRight=80;F.paddingTop=F.paddingBottom=72;F.primaryAxisSizingMode='AUTO';F.counterAxisSizingMode='FIXED';
async function T(par,str,family,style,size,color,opts={}){const t=figma.createText();par.appendChild(t);t.fontName={family,style};t.fontSize=size;t.characters=str;t.fills=[paint(color)];if(opts.ls!==undefined)t.letterSpacing={unit:'PERCENT',value:opts.ls};if(opts.lh)t.lineHeight={unit:'PIXELS',value:opts.lh};if(opts.w){t.resize(opts.w,t.height);t.textAutoResize='HEIGHT';}return t;}
const hdr=figma.createFrame();hdr.name='Encabezado';hdr.fills=[];hdr.layoutMode='VERTICAL';hdr.itemSpacing=16;F.appendChild(hdr);hdr.layoutAlign='STRETCH';hdr.primaryAxisSizingMode='AUTO';
await T(hdr,'09 · AJUSTES DEL 25 DE NOVIEMBRE','Figtree','Bold',14,'primario/500',{ls:10});
await T(hdr,'Una identidad propia, de noche.','Bricolage Grotesque','ExtraBold',64,'neutral/900',{ls:-2.5,lh:70,w:1280});
await T(hdr,'La profesora vio la interfaz muy parecida a Uber. Uber es blanco y negro puro. Match pasa a una base índigo de noche, títulos con más carácter y un recurso gráfico que sale del logo: la línea de tramos.','Figtree','Regular',20,'neutral/600',{lh:28,w:900});
function row(){const r=figma.createFrame();r.fills=[];r.layoutMode='HORIZONTAL';r.itemSpacing=24;F.appendChild(r);r.layoutAlign='STRETCH';r.primaryAxisSizingMode='FIXED';r.counterAxisSizingMode='AUTO';return r;}
function card(par,name){const c=figma.createFrame();c.name=name;c.fills=[paint('neutral/100')];c.cornerRadius=24;c.layoutMode='VERTICAL';c.itemSpacing=14;c.paddingLeft=c.paddingRight=28;c.paddingTop=c.paddingBottom=28;par.appendChild(c);c.layoutGrow=1;c.primaryAxisSizingMode='AUTO';return c;}
const r1=row();
{const c=card(r1,'Color');await T(c,'Color · de negro a noche','Bricolage Grotesque','Bold',24,'neutral/900');
 const sw=figma.createFrame();sw.fills=[];sw.layoutMode='HORIZONTAL';sw.itemSpacing=10;c.appendChild(sw);sw.primaryAxisSizingMode='AUTO';sw.counterAxisSizingMode='AUTO';
 for(const [n,h] of [['neutral/900','#14112B'],['neutral/700','#3B3658'],['neutral/500','#6F6A8A'],['neutral/200','#E7E4F2'],['primario/500','#5B3DF5'],['candidata/b-lima','#C8F560']]){const col=figma.createFrame();col.fills=[];col.layoutMode='VERTICAL';col.itemSpacing=6;sw.appendChild(col);col.primaryAxisSizingMode='AUTO';col.counterAxisSizingMode='AUTO';const s=figma.createRectangle();col.appendChild(s);s.resize(64,64);s.cornerRadius=16;s.fills=[paint(n)];s.strokes=[paint('neutral/300')];s.strokeWeight=1;await T(col,h,'Figtree','Medium',12,'neutral/600');}
 await T(c,'Los neutros llevan un tinte índigo. Textos, botones y fondos oscuros ya no son negro puro.','Figtree','Regular',16,'neutral/600',{lh:22,w:520});}
{const c=card(r1,'Tipografía');await T(c,'Tipografía · más carácter','Bricolage Grotesque','Bold',24,'neutral/900');
 await T(c,'Laura aceptó.','Bricolage Grotesque','ExtraBold',56,'neutral/900',{ls:-2});
 await T(c,'Ya tienen chat, punto seguro y código para reconocerse.','Figtree','Regular',18,'neutral/600',{lh:24,w:520});
 await T(c,'Títulos: Bricolage Grotesque ExtraBold. Textos: Figtree. Las dos son de Google Fonts con licencia libre (OFL).','Figtree','Regular',14,'neutral/500',{lh:20,w:520});}
const r2=row();
const cp=figma.root.children.find(p=>p.name==='Sistema de diseño · Componentes');await cp.loadAsync();
{const c=card(r2,'Recurso gráfico');await T(c,'Recurso propio · la línea de tramos','Bricolage Grotesque','Bold',24,'neutral/900');
 const tm=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Tarjeta de match');const i=tm.children[0].createInstance();c.appendChild(i);
 await T(c,'Es la misma idea del logo: dos rutas que comparten un tramo. Aparece en las tarjetas de match, en el detalle y en el trayecto.','Figtree','Regular',16,'neutral/600',{lh:22,w:400});}
{const c=card(r2,'Seguridad en el encuentro');await T(c,'Seguridad en el encuentro','Bricolage Grotesque','Bold',24,'neutral/900');
 const ph=figma.createFrame();ph.fills=[];ph.layoutMode='HORIZONTAL';ph.itemSpacing=10;c.appendChild(ph);ph.primaryAxisSizingMode='AUTO';ph.counterAxisSizingMode='AUTO';
 for(const id of ['214:48','214:60','214:68','214:87','214:102','214:123']){const i=(await figma.getNodeByIdAsync(id)).createInstance();ph.appendChild(i);i.resize(56,56);}
 const ps=(await figma.getNodeByIdAsync('218:97')).createInstance();c.appendChild(ps);
 await T(c,'Foto verificada de cada persona y puntos de encuentro con vigilancia: porterías, recepciones y CAI. Al encontrarse se confirma la foto y el código.','Figtree','Regular',16,'neutral/600',{lh:22,w:400});}
{const c=card(r2,'Modo de compañía');await T(c,'Modo de compañía','Bricolage Grotesque','Bold',24,'neutral/900');
 const ch=cp.findOne(n=>n.type==='COMPONENT_SET'&&n.name==='Chip');const sel=ch.children.find(v=>v.name==='Estado=Seleccionado'),def=ch.children.find(v=>v.name==='Estado=Default');const k=Object.keys(ch.componentPropertyDefinitions).find(x=>x.startsWith('Texto'));
 const w=figma.createFrame();w.fills=[];w.layoutMode='HORIZONTAL';w.layoutWrap='WRAP';w.itemSpacing=8;w.counterAxisSpacing=8;c.appendChild(w);w.layoutAlign='STRETCH';w.primaryAxisSizingMode='FIXED';w.counterAxisSizingMode='AUTO';
 for(const [v,t] of [[sel,'Solo mujeres'],[def,'Solo hombres'],[def,'Cualquier persona']]){const i=v.createInstance();w.appendChild(i);i.setProperties({[k]:t});}
 await T(c,'Cada persona elige con quién viaja. Solo hay match si las dos preferencias son compatibles.','Figtree','Regular',16,'neutral/600',{lh:22,w:300});}
for(const r of [r1,r2])for(const c of r.children){c.layoutGrow=1;c.layoutAlign='STRETCH';}
return {frame:F.id,h:Math.round(F.height)};
