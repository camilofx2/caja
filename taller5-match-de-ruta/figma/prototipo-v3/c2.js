// P06 Solicitud enviada
{const f=await scr('P06','Solicitud enviada',5);await sbar(f,'8:55 p. m.');
const c=box(f,'Contenido',16,0,380,{itemSpacing:24,counterAxisAlignItems:'CENTER'});const av=FR_(c,152,96,0,0,'Fotos');circ(av,96,0,0,'neutral/200');const a2=circ(av,96,56,0,'neutral/400');stroke(a2,'neutral/0',4,'OUTSIDE');
const t=AL(c,'VERTICAL',{itemSpacing:12});await T(t,'Le avisamos a Laura','h1','neutral/900',{align:'CENTER'});await T(t,'Te contamos apenas responda. La solicitud vence a las 9:00 p. m.','base','neutral/600',{align:'CENTER'});
const n=AL(c,'HORIZONTAL',{itemSpacing:8,paddingLeft:16,paddingRight:16,paddingTop:12,paddingBottom:12,cornerRadius:16,counterAxisAlignItems:'CENTER'});n.fills=P('primario/100');icon(n,'bell',20,'primario/500');await T(n,'En esta prueba Laura responde sola en 3 segundos.','label','primario/500');
c.y=Math.round((917-c.height)/2/4)*4-40;const a=box(f,'Acciones',16,0,380,{});await pill(a,'Volver al inicio','o','Ir:P02');bottom(a,24);out.push(f.id);}
// P07 Laura aceptó
{const f=await scr('P07','Laura aceptó',6,'primario/500');await sbar(f,'8:56 p. m.','neutral/0');
const c=box(f,'Contenido',24,96,364,{itemSpacing:24});await symbol(c,120,'neutral/0','neutral/0','primario/500');
const t=AL(c,'VERTICAL',{itemSpacing:12});await T(t,'Laura aceptó.','disp','neutral/0');await T(t,'Ya tienen chat, punto de encuentro y un código para reconocerse.','base','neutral/0',{op:0.85});
const cd=AL(c,'VERTICAL',{itemSpacing:4,paddingLeft:24,paddingRight:24,paddingTop:20,paddingBottom:20,cornerRadius:24,counterAxisAlignItems:'CENTER'});cd.fills=P('neutral/0');await T(cd,'Su código de encuentro','label','neutral/600',{align:'CENTER'});await T(cd,'Naranja-12','disp','neutral/900',{align:'CENTER'});await T(cd,'Pídele que te lo diga en voz alta','hint','neutral/600',{align:'CENTER'});
const a=box(f,'Acciones',16,0,380,{itemSpacing:12});await pill(a,'Abrir el chat','w','Ir:P08');await pill(a,'Ver punto de encuentro','ow','Ir:P09');bottom(a,24);out.push(f.id);}
// P08 Chat
{const f=await scr('P08','Chat con Laura',7);await sbar(f,'8:57 p. m.');await back(f);
const hd=figma.createAutoLayout('HORIZONTAL',{name:'Encabezado',itemSpacing:8,counterAxisAlignItems:'CENTER',fills:[]});f.appendChild(hd);circ(hd,32,0,0,'neutral/200');await T(hd,'Laura M.','strong','neutral/900',{hug:true});hd.x=120;hd.y=48;
const cc=figma.createAutoLayout('HORIZONTAL',{name:'Código',paddingLeft:12,paddingRight:12,paddingTop:6,paddingBottom:6,cornerRadius:16});f.appendChild(cc);cc.fills=P('primario/100');await T(cc,'Naranja-12','label','primario/500',{hug:true});cc.x=412-16-cc.width;cc.y=50;
const dv=rect(f,412,1,0,100,'neutral/200');
const c=box(f,'Mensajes',16,0,380,{itemSpacing:12});
const mt=AL(c,'HORIZONTAL',{itemSpacing:12,paddingLeft:16,paddingRight:16,paddingTop:12,paddingBottom:12,cornerRadius:16,counterAxisAlignItems:'CENTER'});mt.fills=P('neutral/100');icon(mt,'map-pin',20,'neutral/900');const mc=AL(mt,'VERTICAL',{itemSpacing:2});mc.layoutSizingHorizontal='FILL';await T(mc,'Encuentro · 8:55 p. m.','strong');await T(mc,'Entrada norte, Estación Calle 45','hint','neutral/600');
async function msg(t,me,h){const r=AL(c,'HORIZONTAL',{primaryAxisAlignItems:me?'MAX':'MIN'});const b=AL(r,'VERTICAL',{itemSpacing:4,paddingLeft:14,paddingRight:14,paddingTop:10,paddingBottom:10,cornerRadius:20},true);b.fills=P(me?'primario/500':'neutral/100');b.resize(280,40);b.primaryAxisSizingMode='AUTO';await T(b,t,'base',me?'primario/sobre':'neutral/900');await T(b,h,'hint',me?'primario/sobre':'neutral/600',{op:me?0.8:1});}
await msg('Ya salí de clase, voy para la entrada.',false,'Laura · 8:47 p. m.');await msg('Listo, te espero adentro, junto a la taquilla.',true,'Tú · 8:49 p. m.');
const q=AL(c,'HORIZONTAL',{itemSpacing:8,layoutWrap:'WRAP',counterAxisSpacing:8});await chip(q,'Ya salí, voy para allá',false,'Ir:P09');await chip(q,'Voy 5 min tarde');await chip(q,'Estoy en la puerta 2');
const inp=AL(c,'HORIZONTAL',{itemSpacing:8,counterAxisAlignItems:'CENTER',paddingLeft:20,paddingRight:6,cornerRadius:26});inp.fills=P('neutral/100');inp.layoutSizingVertical='FIXED';inp.resize(380,52);await T(inp,'Escribe un mensaje','base','neutral/600');const sd=AL(inp,'HORIZONTAL',{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:20},true);sd.fills=P('neutral/900');sd.resize(40,40);sd.primaryAxisSizingMode='FIXED';sd.counterAxisSizingMode='FIXED';await T(sd,'↑','strong','neutral/0',{hug:true});
await T(c,'El chat se borra 24 h después del trayecto. Sin fotos ni archivos.','hint','neutral/600',{align:'CENTER'});bottom(c,24);out.push(f.id);}
// P09 Antes de salir
{const f=await scr('P09','Antes de salir',8);await sbar(f,'8:58 p. m.');await back(f);
const c=box(f,'Contenido',16,0,380,{itemSpacing:24});const t=AL(c,'VERTICAL',{itemSpacing:12});await T(t,'Antes de salir','disp');await T(t,'Revisa con quién vas y a quién le avisamos esta noche.','base','neutral/600');
const lc=AL(c,'VERTICAL',{paddingLeft:16,paddingRight:16,paddingTop:16,paddingBottom:16,cornerRadius:24});lc.fills=P('neutral/100');await person(lc,'Laura M.','✓ Verificada · Universidad',['Encuentro 8:55 p. m. · entrada norte, Calle 45']);
const w=AL(c,'VERTICAL',{itemSpacing:0});await T(w,'¿A quién le avisamos?','h2');
for(const [n,s,on] of [['Gloria Gómez · Mamá','WhatsApp · inicio, separación, llegada y retraso',true],['Andrés Gómez · Hermano','SMS',false]]){const r=AL(w,'HORIZONTAL',{itemSpacing:12,paddingTop:16,paddingBottom:16,counterAxisAlignItems:'CENTER',name:'Contacto'});const ck=AL(r,'HORIZONTAL',{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:6},true);ck.resize(24,24);ck.primaryAxisSizingMode='FIXED';ck.counterAxisSizingMode='FIXED';if(on){ck.fills=P('primario/500');await T(ck,'✓','label','neutral/0',{hug:true});}else stroke(ck,'neutral/400',2);const cl=AL(r,'VERTICAL',{itemSpacing:2});cl.layoutSizingHorizontal='FILL';await T(cl,n,'strong');await T(cl,s,'hint','neutral/600');}
const nt=AL(c,'HORIZONTAL',{itemSpacing:12,paddingLeft:16,paddingRight:16,paddingTop:12,paddingBottom:12,cornerRadius:16,counterAxisAlignItems:'CENTER'});nt.fills=P('neutral/100');icon(nt,'shield-check',20,'neutral/900');await T(nt,'Tu ubicación solo se comparte durante el trayecto y se apaga al llegar.','label','neutral/600');
const a=box(f,'Acciones',16,0,380,{});await pill(a,'Iniciar trayecto','a','Ir:P10');bottom(a,24);c.y=Math.round((88+(a.y-24-88-c.height)/2)/4)*4;out.push(f.id);}
// P10 En curso (y base de P11)
async function encurso(f){mapBg(f,412,917);await route(f,[[0,260],[0,150],[110,40],[230,40],[230,0]],80,180,['f','now',null,'o','o']);await gchip(f,'Portal Sur',236,232);await gchip(f,'Bosa Centro',236,144);await sbar(f,'9:20 p. m.');
const tp=figma.createAutoLayout('HORIZONTAL',{name:'Barra de trayecto',paddingLeft:16,paddingRight:16,cornerRadius:28,counterAxisAlignItems:'CENTER',itemSpacing:8});f.appendChild(tp);tp.resize(380,56);tp.primaryAxisSizingMode='FIXED';tp.counterAxisSizingMode='FIXED';tp.x=16;tp.y=44;glass(tp,0.4);circ(tp,10,0,0,'primario/500');await T(tp,'Trayecto activo · Tu mamá ve tu trayecto','label');
const sh=box(f,'Hoja tintada',16,0,380,{itemSpacing:20,paddingLeft:20,paddingRight:20,paddingTop:24,paddingBottom:20,cornerRadius:32});glass(sh,0.85,24);
const hd=AL(sh,'VERTICAL',{itemSpacing:4});await T(hd,'10:38 p. m.','disp');await T(hd,'Llegada estimada · faltan 40 min a Portal Sur','label','neutral/600');
await person(sh,'Laura M.','Va contigo hasta Portal Sur',[],{subc:'neutral/600'});
const bt=AL(sh,'VERTICAL',{itemSpacing:12});await pill(bt,'Llegué','a','Ir:P13');await pill(bt,'¿Algo no está bien?','o','Ir:P11');bottom(sh,16);}
{const f=await scr('P10','En curso',9);await encurso(f);out.push(f.id);}
{const f=await scr('P11','¿Algo no está bien?',10);await encurso(f);const sh=await sheet(f,12);await T(sh,'¿Algo no está bien?','h2');await T(sh,'Elige qué necesitas. Tu mamá sigue viendo tu trayecto.','base','neutral/600');
const g=AL(sh,'VERTICAL',{itemSpacing:12,paddingTop:8});await pill(g,'Llamar al 123','r','Atrás');await pill(g,'Avisar a mis contactos','o','Atrás');await pill(g,'Reportar a Laura','o','Atrás');await pill(g,'Cancelar','t','Atrás');
await T(sh,'Match no reemplaza a las autoridades. El 123 es la línea de emergencias.','hint','neutral/600',{align:'CENTER'});sh.y=917-sh.height;out.push(f.id);}
return out;
