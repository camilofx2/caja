await figma.setCurrentPageAsync(cp);
const lib=cp.children.find(n=>n.name==='Biblioteca · iconos');
async function icon(p,name,size,cn){const c=lib.findOne(n=>n.type==='COMPONENT'&&n.name==='Icono/'+name);const n=c.createInstance();p.appendChild(n);n.resize(size,size);for(const v of n.findAll(x=>x.type==='VECTOR'))v.fills=P(cn);return n;}
const combos=(o)=>{let r=[{}];for(const [k,vals] of Object.entries(o)){const nr=[];for(const x of r)for(const v of vals)nr.push(Object.assign({},x,{[k]:v}));r=nr;}return r;};
async function vset(name,axes,build,props,W=1200){const old=cp.children.find(n=>n.name===name&&n.type==='COMPONENT_SET');if(old)old.remove();const ol=cp.children.find(n=>n.name==='Etiqueta · '+name);if(ol)ol.remove();const comps=[];
for(const c of combos(axes)){const k=figma.createComponent();cp.appendChild(k);k.name=Object.entries(c).map(([a,b])=>a+'='+b).join(', ');k.fills=[];await build(k,c);comps.push(k);}
const set=figma.combineAsVariants(comps,cp);set.name=name;set.layoutMode='HORIZONTAL';set.layoutWrap='WRAP';set.itemSpacing=24;set.counterAxisSpacing=24;set.paddingLeft=set.paddingRight=set.paddingTop=set.paddingBottom=32;set.primaryAxisSizingMode='FIXED';set.resize(W,100);set.fills=P('neutral/0');set.cornerRadius=24;stroke(set,'primario/500',1,'INSIDE');set.dashPattern=[6,6];
const keys={};for(const [pn,type,def,target] of (props||[]))keys[pn]=[set.addComponentProperty(pn,type,def),type,target||pn];
for(const v of set.children)for(const [pn,[key,type,target]] of Object.entries(keys))for(const n of v.findAll(n=>n.name===target)){if(type==='TEXT'&&n.type==='TEXT')n.componentPropertyReferences={characters:key};if(type==='BOOLEAN')n.componentPropertyReferences=Object.assign({},n.componentPropertyReferences||{},{visible:key});}
return set;}
function auto(k,dir,p={}){k.layoutMode=dir;k.primaryAxisSizingMode='AUTO';k.counterAxisSizingMode='AUTO';Object.assign(k,p);}
const out=[];
// Campo
out.push((await vset('Campo',{Tipo:['Texto','Lista'],Estado:['Default','Active','Filled','Disabled','Error','Success']},async(k,c)=>{auto(k,'VERTICAL',{itemSpacing:8});k.counterAxisSizingMode='FIXED';k.resize(380,100);
const s=c.Estado,d=s==='Disabled';await T(k,'Label','label',d?'neutral/400':'neutral/900',{name:'Label'});
const bx=AL(k,'HORIZONTAL',{name:'Caja',paddingLeft:16,paddingRight:16,itemSpacing:8,counterAxisAlignItems:'CENTER',cornerRadius:12});bx.layoutSizingVertical='FIXED';bx.resize(380,52);bx.fills=P(d?'neutral/100':'neutral/0');
const B={Default:['neutral/300',1],Active:['primario/500',2],Filled:['neutral/400',1],Disabled:['neutral/200',1],Error:['semantico/peligro',2],Success:['semantico/exito',2]}[s];stroke(bx,B[0],B[1]);if(s==='Active')ring(bx,'primario/100');
const vc=s==='Default'?'neutral/500':d?'neutral/400':'neutral/900';
if(s==='Active'){await T(bx,'Escribe aquí','base',vc,{hug:true,name:'Valor'});const cr=rect(bx,2,22,0,0,'primario/500',1);cr.name='Cursor';const sp=AL(bx,'HORIZONTAL',{name:'Espacio'});sp.layoutSizingHorizontal='FILL';}else await T(bx,'Escribe aquí','base',vc,{name:'Valor'});
if(c.Tipo==='Lista')await T(bx,'▾','base',d?'neutral/400':'neutral/600',{hug:true});
if(s==='Error')await icon(bx,'warning-circle',20,'semantico/peligro');if(s==='Success')await icon(bx,'check-circle',20,'semantico/exito');
await T(k,'Texto de ayuda','hint',s==='Error'?'semantico/peligro':s==='Success'?'semantico/exito':d?'neutral/400':'neutral/600',{name:'Ayuda'});},[['Label','TEXT','Label'],['Valor','TEXT','Escribe aquí'],['Ayuda','TEXT','Texto de ayuda'],['Con ayuda','BOOLEAN',true,'Ayuda'],['Con label','BOOLEAN',true,'Label']],1400)).id);
// Código
out.push((await vset('Código',{Estado:['Vacío','Activo','Lleno','Error']},async(k,c)=>{auto(k,'HORIZONTAL',{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:12});k.primaryAxisSizingMode='FIXED';k.counterAxisSizingMode='FIXED';k.resize(52,64);k.fills=P('neutral/0');
const B={Vacío:['neutral/300',1],Activo:['primario/500',2],Lleno:['neutral/400',1],Error:['semantico/peligro',2]}[c.Estado];stroke(k,B[0],B[1]);if(c.Estado==='Activo'){ring(k,'primario/100');rect(k,2,28,0,0,'primario/500',1).name='Cursor';}
else await T(k,c.Estado==='Vacío'?' ':'4','code',c.Estado==='Error'?'semantico/peligro':'neutral/900',{hug:true,name:'Dígito'});},[['Dígito','TEXT','4']],700)).id);
// Pasos
const PC=[];for(const t of [2,3,4])for(let p=1;p<=t;p++)PC.push({Total:String(t),Paso:String(p)});
{const old=cp.children.find(n=>n.name==='Pasos'&&n.type==='COMPONENT_SET');if(old)old.remove();const comps=[];
for(const c of PC){const k=figma.createComponent();cp.appendChild(k);k.name='Total='+c.Total+', Paso='+c.Paso;k.fills=[];auto(k,'VERTICAL',{itemSpacing:8});k.counterAxisSizingMode='FIXED';k.resize(380,30);await T(k,'Paso '+c.Paso+' de '+c.Total+' · Etapa','label','neutral/600',{name:'Etiqueta'});const b=AL(k,'HORIZONTAL',{itemSpacing:4,name:'Barra'});for(let i=1;i<=+c.Total;i++){const r=rect(b,40,4,0,0,i<=+c.Paso?'primario/500':'neutral/200',2);r.layoutSizingHorizontal='FILL';}comps.push(k);}
const set=figma.combineAsVariants(comps,cp);set.name='Pasos';set.layoutMode='HORIZONTAL';set.layoutWrap='WRAP';set.itemSpacing=24;set.counterAxisSpacing=24;set.paddingLeft=set.paddingRight=set.paddingTop=set.paddingBottom=32;set.primaryAxisSizingMode='FIXED';set.resize(1300,100);set.fills=P('neutral/0');set.cornerRadius=24;stroke(set,'primario/500',1);set.dashPattern=[6,6];
const key=set.addComponentProperty('Etiqueta','TEXT','Paso 1 de 3 · Etapa');for(const v of set.children)for(const t of v.findAll(n=>n.name==='Etiqueta'))t.componentPropertyReferences={characters:key};out.push(set.id);}
// Persona
out.push((await vset('Persona',{Tipo:['Tarjeta','Plana','Grande']},async(k,c)=>{auto(k,'HORIZONTAL',{itemSpacing:12,counterAxisAlignItems:'CENTER'});k.primaryAxisSizingMode='FIXED';k.resize(380,48);
if(c.Tipo==='Tarjeta'){Object.assign(k,{paddingLeft:16,paddingRight:16,paddingTop:16,paddingBottom:16,cornerRadius:20});k.fills=P('neutral/0');stroke(k,'neutral/200',1);}
circ(k,c.Tipo==='Grande'?72:48,0,0,'neutral/200').name='Foto';const cl=AL(k,'VERTICAL',{itemSpacing:2});cl.layoutSizingHorizontal='FILL';await T(cl,'Laura M.',c.Tipo==='Grande'?'h1':'strong','neutral/900',{name:'Nombre'});await T(cl,'✓ Verificada · Universidad','label','primario/500',{name:'Verificación'});await T(cl,'Detalle','hint','neutral/600',{name:'Detalle'});},[['Nombre','TEXT','Laura M.'],['Verificación','TEXT','✓ Verificada · Universidad'],['Detalle','TEXT','Detalle'],['Con verificación','BOOLEAN',true,'Verificación'],['Con detalle','BOOLEAN',true,'Detalle']],1400)).id);
// Menú inferior
out.push((await vset('Menú inferior',{Activo:['Hoy','Mis rutas','Matches','Perfil']},async(k,c)=>{auto(k,'HORIZONTAL',{itemSpacing:4,paddingLeft:6,paddingRight:6,paddingTop:6,paddingBottom:6,cornerRadius:36});k.primaryAxisSizingMode='FIXED';k.counterAxisSizingMode='FIXED';k.resize(380,72);glass(k,0.6);
for(const [ic,l] of [['house','Hoy'],['path','Mis rutas'],['users','Matches'],['user','Perfil']]){const a=l===c.Activo;const t=AL(k,'VERTICAL',{name:'Tab '+l,itemSpacing:2,counterAxisAlignItems:'CENTER',primaryAxisAlignItems:'CENTER',cornerRadius:30});t.layoutSizingHorizontal='FILL';t.layoutSizingVertical='FILL';if(a)t.fills=P('neutral/0',0.9);await icon(t,a&&ic==='house'?'house-fill':ic,24,a?'neutral/900':'neutral/600');await T(t,l,'hint',a?'neutral/900':'neutral/600',{hug:true});}},[],1700)).id);
// Reordenar la página: alto real de cada grupo de variantes
let Y=400;const order=['Botón','Chip','Casilla','Interruptor','Opción','Aviso','Campo','Código','Pasos','Persona','Menú inferior','Barra de estado','Barra superior'];
for(const n of cp.children.filter(n=>n.type==='TEXT'&&order.includes(n.characters)))n.remove();
for(const name of order){const s=cp.children.find(n=>n.type==='COMPONENT_SET'&&n.name===name);if(!s)continue;let mh=0;for(const c of s.children)mh=Math.max(mh,c.y+c.height);s.resize(s.width,mh+32);s.x=0;s.y=Y;const l=await T(cp,name,'h1');l.name='Etiqueta · '+name;l.x=0;l.y=Y-56;Y+=s.height+140;}
return {out,Y};
