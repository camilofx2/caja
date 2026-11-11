// 1) Variables: escala de neutrales 0–900 y primario
const REN={'neutro/blanco':'neutral/0','neutro/gris-100':'neutral/100','neutro/gris-200':'neutral/200','neutro/gris-400':'neutral/400','neutro/gris-600':'neutral/600','neutro/gris-800':'neutral/800','neutro/negro':'neutral/900','acento/principal':'primario/500','acento/suave':'primario/100','acento/sobre-acento':'primario/sobre'};
for(const [a,b] of Object.entries(REN)){if(V[a]&&!V[b]){V[a].name=b;V[b]=V[a];delete V[a];}}
const mode=col.modes[0].modeId;
function cv(name,h){let v=V[name];if(!v){v=figma.variables.createVariable(name,col,'COLOR');V[name]=v;}const c=hex(h);v.setValueForMode(mode,{r:c.r,g:c.g,b:c.b,a:1});}
for(const [n,h] of [['neutral/300','D4D4D8'],['neutral/500','71717A'],['neutral/700','3F3F46'],['primario/700','3F22C9'],['semantico/exito-suave','DCFCE7'],['semantico/alerta-suave','FEF3C7'],['semantico/peligro-suave','FEE2E2']])cv(n,h);
let cs=exTS.find(x=>x.name==='Marca/Código 24');if(!cs){cs=figma.createTextStyle();cs.name='Marca/Código 24';}cs.fontName={family:'Figtree',style:FB};cs.fontSize=24;cs.lineHeight={unit:'PIXELS',value:32};S.code=cs;
// manual: etiquetas de las muestras
const man=figma.root.children.find(p=>p.name==='Identidad · Mini manual v0.1');await man.loadAsync();
const LB={'negro':'neutral/900','gris-800':'neutral/800','gris-600':'neutral/600','gris-400':'neutral/400','gris-200':'neutral/200','gris-100':'neutral/100','blanco':'neutral/0'};
for(const t of man.findAll(n=>n.type==='TEXT'&&LB[n.characters])){await figma.loadFontAsync(t.fontName);t.characters=LB[t.characters];}
// 2) Página de componentes
if(!cp){cp=figma.createPage();cp.name='Componentes · Match';}
await figma.setCurrentPageAsync(cp);
const proto=figma.root.children.find(p=>p.name==='Prototipo v3 · prueba 1');await proto.loadAsync();
let lib=cp.children.find(n=>n.name==='Biblioteca · iconos');if(!lib){lib=proto.children.find(n=>n.name==='Biblioteca · iconos');cp.appendChild(lib);}lib.x=0;lib.y=200;
async function icon(p,name,size,cn){const c=lib.findOne(n=>n.type==='COMPONENT'&&n.name==='Icono/'+name);const n=c.createInstance();p.appendChild(n);n.resize(size,size);for(const v of n.findAll(x=>x.type==='VECTOR'))v.fills=P(cn);return n;}
const combos=(o)=>{let r=[{}];for(const [k,vals] of Object.entries(o)){const nr=[];for(const x of r)for(const v of vals)nr.push(Object.assign({},x,{[k]:v}));r=nr;}return r;};
let Y=400;
async function vset(name,axes,build,props,W=1200){const old=cp.children.find(n=>n.name===name);if(old)old.remove();const comps=[];
for(const c of combos(axes)){const k=figma.createComponent();cp.appendChild(k);k.name=Object.entries(c).map(([a,b])=>a+'='+b).join(', ');k.fills=[];await build(k,c);comps.push(k);}
const set=figma.combineAsVariants(comps,cp);set.name=name;set.layoutMode='HORIZONTAL';set.layoutWrap='WRAP';set.itemSpacing=24;set.counterAxisSpacing=24;set.paddingLeft=set.paddingRight=set.paddingTop=set.paddingBottom=32;set.primaryAxisSizingMode='FIXED';set.counterAxisSizingMode='AUTO';set.resize(W,100);set.fills=P('neutral/0');set.cornerRadius=24;stroke(set,'primario/500',1,'INSIDE');set.dashPattern=[6,6];
const keys={};for(const [pn,type,def,target] of (props||[]))keys[pn]=[set.addComponentProperty(pn,type,def),type,target||pn];
for(const v of set.children)for(const [pn,[key,type,target]] of Object.entries(keys))for(const n of v.findAll(n=>n.name===target)){if(type==='TEXT'&&n.type==='TEXT')n.componentPropertyReferences={characters:key};if(type==='BOOLEAN')n.componentPropertyReferences=Object.assign({},n.componentPropertyReferences||{},{visible:key});}
set.x=0;set.y=Y;const lbl=await T(cp,name,'h1');lbl.x=0;lbl.y=Y-56;Y+=set.height+140;return set;}
function auto(k,dir,o={}){k.layoutMode=dir;k.primaryAxisSizingMode=o.hug===false?'FIXED':'AUTO';k.counterAxisSizingMode=o.cfix?'FIXED':'AUTO';Object.assign(k,o.p||{});}
const out=[];
// Botón
out.push((await vset('Botón',{Tipo:['Primario','Acento','Secundario','Terciario','Peligro'],Estado:['Default','Disabled']},async(k,c)=>{auto(k,'HORIZONTAL',{cfix:true,p:{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',paddingLeft:24,paddingRight:24,cornerRadius:26}});k.resize(200,52);
const d=c.Estado==='Disabled';const M={Primario:['neutral/900','neutral/0'],Acento:['primario/500','primario/sobre'],Peligro:['semantico/peligro','neutral/0']};let tc;
if(M[c.Tipo]){k.fills=P(d?'neutral/200':M[c.Tipo][0]);tc=d?'neutral/400':M[c.Tipo][1];}else if(c.Tipo==='Secundario'){stroke(k,d?'neutral/300':'neutral/900',1.5);tc=d?'neutral/400':'neutral/900';}else tc=d?'neutral/400':'neutral/900';
await T(k,'Continuar','strong',tc,{hug:true,name:'Texto'});},[['Texto','TEXT','Continuar']])).id);
// Chip
out.push((await vset('Chip',{Estado:['Default','Seleccionado','Disabled']},async(k,c)=>{auto(k,'HORIZONTAL',{cfix:true,p:{counterAxisAlignItems:'CENTER',paddingLeft:16,paddingRight:16,cornerRadius:20}});k.resize(100,40);
let tc='neutral/900';if(c.Estado==='Seleccionado'){k.fills=P('neutral/900');tc='neutral/0';}else if(c.Estado==='Disabled'){k.fills=P('neutral/100');tc='neutral/400';}else stroke(k,'neutral/300',1);
await T(k,'Opción','label',tc,{hug:true,name:'Texto'});},[['Texto','TEXT','Opción']],800)).id);
// Casilla
out.push((await vset('Casilla',{Estado:['Off','On','Disabled']},async(k,c)=>{auto(k,'HORIZONTAL',{cfix:true,p:{itemSpacing:12,counterAxisAlignItems:'MIN'}});k.counterAxisSizingMode='AUTO';k.primaryAxisSizingMode='FIXED';k.resize(380,24);
const b=AL(k,'HORIZONTAL',{name:'Caja',primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:6},true);b.resize(24,24);b.primaryAxisSizingMode='FIXED';b.counterAxisSizingMode='FIXED';
if(c.Estado==='On'){b.fills=P('primario/500');await T(b,'✓','label','primario/sobre',{hug:true});}else if(c.Estado==='Disabled')b.fills=P('neutral/200');else stroke(b,'neutral/400',2);
const cl=AL(k,'VERTICAL',{itemSpacing:2});cl.layoutSizingHorizontal='FILL';await T(cl,'Texto de la casilla','base',c.Estado==='Disabled'?'neutral/400':'neutral/900',{name:'Label'});await T(cl,'Ayuda','hint','neutral/600',{name:'Ayuda'});},[['Label','TEXT','Texto de la casilla'],['Ayuda','TEXT','Ayuda'],['Con ayuda','BOOLEAN',false,'Ayuda']],1400)).id);
// Interruptor
out.push((await vset('Interruptor',{Estado:['On','Off','Disabled']},async(k,c)=>{auto(k,'HORIZONTAL',{p:{itemSpacing:12,counterAxisAlignItems:'CENTER'}});k.primaryAxisSizingMode='FIXED';k.resize(380,28);
const cl=AL(k,'VERTICAL',{itemSpacing:2});cl.layoutSizingHorizontal='FILL';await T(cl,'Interruptor','strong',c.Estado==='Disabled'?'neutral/400':'neutral/900',{name:'Label'});await T(cl,'Ayuda','hint','neutral/600',{name:'Ayuda'});
const tr=figma.createFrame();k.appendChild(tr);tr.name='Riel';tr.resize(48,28);tr.cornerRadius=14;tr.fills=P(c.Estado==='On'?'primario/500':c.Estado==='Off'?'neutral/300':'neutral/200');const kn=circ(tr,22,c.Estado==='On'?23:3,3,c.Estado==='Disabled'?'neutral/100':'neutral/0');kn.effects=shadow(0.15);},[['Label','TEXT','Interruptor'],['Ayuda','TEXT','Ayuda'],['Con ayuda','BOOLEAN',true,'Ayuda']],1400)).id);
// Opción
out.push((await vset('Opción',{Estado:['Default','Seleccionado']},async(k,c)=>{auto(k,'HORIZONTAL',{p:{itemSpacing:12,counterAxisAlignItems:'CENTER',paddingLeft:16,paddingRight:16,paddingTop:16,paddingBottom:16,cornerRadius:16}});k.primaryAxisSizingMode='FIXED';k.resize(380,60);
const s=c.Estado==='Seleccionado';k.fills=P(s?'primario/100':'neutral/0');stroke(k,s?'primario/500':'neutral/300',s?2:1);const r=circ(k,22,0,0,'neutral/0');stroke(r,s?'primario/500':'neutral/400',s?7:2);
const cl=AL(k,'VERTICAL',{itemSpacing:2});cl.layoutSizingHorizontal='FILL';await T(cl,'Título de la opción','strong','neutral/900',{name:'Título'});await T(cl,'Descripción','hint','neutral/600',{name:'Descripción'});},[['Título','TEXT','Título de la opción'],['Descripción','TEXT','Descripción'],['Con descripción','BOOLEAN',true,'Descripción']],900)).id);
// Aviso
out.push((await vset('Aviso',{Tipo:['Info','Éxito','Alerta','Error']},async(k,c)=>{auto(k,'HORIZONTAL',{p:{itemSpacing:12,counterAxisAlignItems:'CENTER',paddingLeft:16,paddingRight:16,paddingTop:12,paddingBottom:12,cornerRadius:16}});k.primaryAxisSizingMode='FIXED';k.resize(380,44);
const M={Info:['neutral/100','shield-check','neutral/900'],Éxito:['semantico/exito-suave','check-circle','semantico/exito'],Alerta:['semantico/alerta-suave','warning-circle','semantico/alerta'],Error:['semantico/peligro-suave','warning-circle','semantico/peligro']}[c.Tipo];k.fills=P(M[0]);await icon(k,M[1],20,M[2]);await T(k,'Mensaje del aviso','label','neutral/800',{name:'Mensaje'});},[['Mensaje','TEXT','Mensaje del aviso']],1700)).id);
// Barra de estado
out.push((await vset('Barra de estado',{Tema:['Claro','Oscuro']},async(k,c)=>{auto(k,'HORIZONTAL',{p:{counterAxisAlignItems:'CENTER',paddingLeft:28,paddingRight:28,primaryAxisAlignItems:'SPACE_BETWEEN'}});k.primaryAxisSizingMode='FIXED';k.counterAxisSizingMode='FIXED';k.resize(412,24);
const tc=c.Tema==='Claro'?'neutral/900':'neutral/0';await T(k,'8:40 p. m.','label',tc,{hug:true,name:'Hora'});const r=AL(k,'HORIZONTAL',{itemSpacing:4,counterAxisAlignItems:'CENTER'},true);for(const h of [6,9,12])rect(r,4,h,0,0,tc,1);const bt=rect(r,22,11,0,0,tc,3);},[['Hora','TEXT','8:40 p. m.']],1000)).id);
// Barra superior
out.push((await vset('Barra superior',{Tema:['Claro','Oscuro']},async(k,c)=>{auto(k,'HORIZONTAL',{p:{counterAxisAlignItems:'CENTER',paddingLeft:12,paddingRight:16,primaryAxisAlignItems:'SPACE_BETWEEN'}});k.primaryAxisSizingMode='FIXED';k.counterAxisSizingMode='FIXED';k.resize(412,56);
const tc=c.Tema==='Claro'?'neutral/900':'neutral/0';const l=AL(k,'HORIZONTAL',{name:'Atrás',itemSpacing:4,counterAxisAlignItems:'CENTER',paddingTop:8,paddingBottom:8,paddingRight:8},true);await icon(l,'caret-left',20,tc);await T(l,'Volver','label',tc,{hug:true,name:'Volver'});
await T(k,'Acción','label',c.Tema==='Claro'?'neutral/600':'neutral/300',{hug:true,name:'Acción'});},[['Volver','TEXT','Volver'],['Acción','TEXT','Acción'],['Con acción','BOOLEAN',false,'Acción']],1000)).id);
const tt=cp.children.find(n=>n.name==='Título de la página');if(tt)tt.remove();const h=await T(cp,'Componentes · Match · v0.1','disp');h.name='Título de la página';h.x=0;h.y=0;
const st=cp.children.find(n=>n.name==='Nota de la página');if(st)st.remove();const n2=await T(cp,'Neutrales 0–900 para texto, fondos y bordes. Primario solo para resaltar: foco, selección y acción principal. Todos los componentes usan auto layout y variables.','base','neutral/600',{w:1200});n2.name='Nota de la página';n2.x=0;n2.y=72;
return {out,Y};
