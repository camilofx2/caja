async function okcard(p,title,sub,dark){const r=AL(p,'HORIZONTAL',{itemSpacing:12,paddingLeft:16,paddingRight:16,paddingTop:16,paddingBottom:16,cornerRadius:20,counterAxisAlignItems:'CENTER'});r.fills=P(dark?'neutral/800':'neutral/100');icon(r,'check-circle',24,dark?'neutral/0':'semantico/exito');const c=AL(r,'VERTICAL',{itemSpacing:2});c.layoutSizingHorizontal='FILL';await T(c,title,'strong',dark?'neutral/0':'neutral/900');await T(c,sub,'label',dark?'neutral/400':'neutral/600');return r;}
// P12 Laura se bajó
{const f=await scr('P12','Laura se bajó',11);mapBg(f,412,917);await route(f,[[0,260],[0,150],[110,40],[230,40],[230,0]],80,180,['f',null,null,'f',null]);await route(f,[[0,80],[0,0]],310,140,['now','o']);await gchip(f,'Bosa Centro',236,96);await sbar(f,'10:01 p. m.');
const tp=figma.createAutoLayout('HORIZONTAL',{name:'Barra de trayecto',paddingLeft:16,paddingRight:16,cornerRadius:28,counterAxisAlignItems:'CENTER',itemSpacing:8});f.appendChild(tp);tp.resize(380,56);tp.primaryAxisSizingMode='FIXED';tp.counterAxisSizingMode='FIXED';tp.x=16;tp.y=44;glass(tp,0.4);circ(tp,10,0,0,'primario/500');await T(tp,'Trayecto activo · Tu mamá ve tu trayecto','label');
const sh=box(f,'Hoja tintada',16,0,380,{itemSpacing:20,paddingLeft:20,paddingRight:20,paddingTop:24,paddingBottom:20,cornerRadius:32});glass(sh,0.85,24);
const hd=AL(sh,'VERTICAL',{itemSpacing:8});await T(hd,'Laura se bajó en Portal Sur','h1');await T(hd,'Sigues sola tu último tramo. Llegada estimada 10:38 p. m.','base','neutral/600');
await okcard(sh,'Le avisamos a Gloria','“Daniela sigue sola desde Portal Sur” · 10:00 p. m.');
const bt=AL(sh,'VERTICAL',{itemSpacing:12});await pill(bt,'Llegué','a','Ir:P13');await pill(bt,'¿Algo no está bien?','o','Ir:P11');bottom(sh,16);out.push(f.id);}
// P13 Llegaste (y base de P14)
async function llegada(f){scene(f,412,520);await sbar(f,'10:40 p. m.','neutral/0');const tt=await T(f,'Llegaste,\nDaniela.','disp','neutral/0',{w:364});tt.x=24;tt.y=96;}
{const f=await scr('P13','Llegaste',12,'neutral/900');await llegada(f);
const c=box(f,'Contenido',16,0,380,{itemSpacing:12});await okcard(c,'Gloria ya sabe que llegaste','Recibió el aviso a las 10:40 p. m.',true);await okcard(c,'Tu ubicación se apagó','No queda historial de este trayecto.',true);
const a=AL(c,'VERTICAL',{paddingTop:12});await pill(a,'Continuar','w','Ir:P14');bottom(c,24);out.push(f.id);}
// P14 ¿Cómo te fue?
{const f=await scr('P14','¿Cómo te fue?',13,'neutral/900');await llegada(f);const sh=await sheet(f,16);f.findOne(n=>n.type==='RECTANGLE'&&n.name==='Atrás').fills=P('neutral/900',0.25);
await T(sh,'¿Cómo te fue con Laura?','h2');
const q1=AL(sh,'VERTICAL',{itemSpacing:8});await T(q1,'¿Se encontraron?','label','neutral/600');const r1=AL(q1,'HORIZONTAL',{itemSpacing:8});await chip(r1,'Sí, nos encontramos',true);await chip(r1,'No se presentó');
const q2=AL(sh,'VERTICAL',{itemSpacing:8});await T(q2,'¿Volverías a viajar con Laura?','label','neutral/600');const r2=AL(q2,'HORIZONTAL',{itemSpacing:8});await chip(r2,'Sí',true);await chip(r2,'Prefiero que no');
await T(sh,'Tu respuesta es privada. Laura no ve lo que contestas.','hint','neutral/600');await pill(sh,'Confirmar','n','Ir:P15');await pill(sh,'Reportar algo que pasó','t');sh.y=917-sh.height;out.push(f.id);}
// P15 Confirmado
{const f=await scr('P15','Trayecto confirmado',14);await sbar(f,'10:41 p. m.');
const c=box(f,'Contenido',16,0,380,{itemSpacing:24,counterAxisAlignItems:'CENTER'});const ok=AL(c,'HORIZONTAL',{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:48},true);ok.fills=P('primario/500');ok.resize(96,96);ok.primaryAxisSizingMode='FIXED';ok.counterAxisSizingMode='FIXED';icon(ok,'check-circle',48,'primario/sobre');
const b=AL(c,'VERTICAL',{itemSpacing:0});await T(b,'4','disp','neutral/900',{align:'CENTER'});await T(b,'trayectos acompañados','label','neutral/600',{align:'CENTER'});
const t=AL(c,'VERTICAL',{itemSpacing:12});await T(t,'Gracias por confirmar','h1','neutral/900',{align:'CENTER'});await T(t,'Cuando Laura también confirme, el trayecto suma en los dos perfiles.','base','neutral/600',{align:'CENTER'});
const nx=AL(c,'VERTICAL',{itemSpacing:2,paddingLeft:16,paddingRight:16,paddingTop:16,paddingBottom:16,cornerRadius:20});nx.fills=P('neutral/100');await T(nx,'Tu próxima ruta','strong');await T(nx,'Mañana · 9:00 p. m. · De la U a la casa','label','neutral/600');
c.y=Math.round((917-100-c.height)/2/4)*4;const a=box(f,'Acciones',16,0,380,{});await pill(a,'Volver al inicio','n','Ir:P02');bottom(a,24);out.push(f.id);}
// P16 Mis rutas
{const f=await scr('P16','Mis rutas',15,'neutral/100');await sbar(f,'8:50 p. m.');
const c=box(f,'Contenido',16,56,380,{itemSpacing:24});const h=AL(c,'VERTICAL',{itemSpacing:4});await T(h,'Mis rutas','h1');await T(h,'Te mostramos personas compatibles para cada una.','label','neutral/600');
for(const [n,d,stops,m] of [['De la U a la casa','Lunes a viernes · sale 9:00 p. m.',['Calle 45','Portal Sur','Bosa Centro'],'2 personas compatibles hoy'],['De la casa a la U','Lunes a viernes · sale 6:30 a. m.',['Bosa Centro','Portal Sur','Calle 45'],'Sin personas todavía']]){
const cd=AL(c,'VERTICAL',{itemSpacing:16,paddingLeft:20,paddingRight:20,paddingTop:20,paddingBottom:20,cornerRadius:24,name:'Ruta'});cd.fills=P('neutral/0');cd.effects=shadow(0.05);const hh=AL(cd,'VERTICAL',{itemSpacing:2});await T(hh,n,'h2');await T(hh,d,'label','neutral/600');
const rl=FR_(cd,340,44,0,0,'Línea');await line(rl,[[0,0],[320,0]],10,10,'primario/500',6);for(let i=0;i<3;i++){const x=10+i*160;const nd=circ(rl,16,x-8,2,i===2?'neutral/0':'neutral/900');if(i===2)stroke(nd,'primario/500',4);}
const lb=AL(cd,'HORIZONTAL',{primaryAxisAlignItems:'SPACE_BETWEEN'});for(const s of stops)await T(lb,s,'hint','neutral/600',{hug:true});
await T(cd,m,'label',m.startsWith('2')?'primario/500':'neutral/600');}
await pill(c,'+ Nueva ruta','o');await nav(f,'Mis rutas');out.push(f.id);}
// P17 Perfil
{const f=await scr('P17','Perfil',16);await sbar(f,'8:50 p. m.');
const c=box(f,'Contenido',16,56,380,{itemSpacing:24});await person(c,'Daniela G.','✓ Verificada · Universidad',['Desde marzo de 2026'],{d:72,big:true});
const st=AL(c,'HORIZONTAL',{itemSpacing:12});for(const [n,l] of [['4','trayectos'],['3','confirmados'],['0','reportes']]){const s=AL(st,'VERTICAL',{itemSpacing:2,paddingLeft:16,paddingTop:16,paddingBottom:16,cornerRadius:20});s.fills=P('neutral/100');s.layoutSizingHorizontal='FILL';await T(s,n,'h1');await T(s,l,'hint','neutral/600');}
const m=AL(c,'VERTICAL',{name:'Menú'});for(const [t,s] of [['Perfil público','Cómo te ven las personas compatibles'],['Preferencias de match','Con quién y cómo viajas'],['Contactos de confianza','1 activo · Gloria Gómez'],['Privacidad y datos','Ubicación, chat, bloqueos y cuenta']]){const r=AL(m,'HORIZONTAL',{itemSpacing:12,paddingTop:16,paddingBottom:16,counterAxisAlignItems:'CENTER'});const cl=AL(r,'VERTICAL',{itemSpacing:2});cl.layoutSizingHorizontal='FILL';await T(cl,t,'strong');await T(cl,s,'hint','neutral/600');await T(r,'›','h2','neutral/400',{hug:true});const dv=rect(m,10,1,0,0,'neutral/200');dv.layoutSizingHorizontal='FILL';}
await nav(f,'Perfil');out.push(f.id);}
// Encabezado de la página
{const old=page.children.find(n=>n.name==='Encabezado de la prueba');if(old)old.remove();const h=figma.createAutoLayout('VERTICAL',{name:'Encabezado de la prueba',itemSpacing:12,fills:[]});page.appendChild(h);h.resize(2600,100);h.counterAxisSizingMode='FIXED';h.primaryAxisSizingMode='AUTO';h.x=0;h.y=0;await T(h,'Prototipo v3 · prueba 1 · El trayecto de Daniela','disp');await T(h,'Diseño de marca aplicado (acento provisional) y botones conectados. Para probar: menú Presentar (▶) o la flecha de inicio “Prueba 1”. P06 y P13 avanzan solos; P10 pasa a “Laura se bajó” a los 5 segundos si no tocas nada.','base','neutral/600');}
// Conexiones
const frames=page.children.filter(n=>n.type==='FRAME'&&/^P\d\d · /.test(n.name));const byCode={};for(const f of frames)byCode[f.name.slice(0,3)]=f;
const SHEETS=['P05','P11','P14'];const tr=(code)=>SHEETS.includes(code)?{type:'DISSOLVE',easing:{type:'EASE_OUT'},duration:0.2}:{type:'SMART_ANIMATE',easing:{type:'EASE_OUT'},duration:0.3};
const nav_=(code)=>({type:'NODE',destinationId:byCode[code].id,navigation:'NAVIGATE',transition:tr(code),preserveScrollPosition:false});
let links=0,backs=0;const miss=[];
for(const f of frames){for(const n of f.findAll(n=>n.name.startsWith('Ir:')||n.name==='Atrás')){if(n.name==='Atrás'){await n.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[{type:'BACK'}]}]);backs++;continue;}const code=n.name.slice(3);if(!byCode[code]){miss.push(code);continue;}if(byCode[code]===f)continue;await n.setReactionsAsync([{trigger:{type:'ON_CLICK'},actions:[nav_(code)]}]);links++;}}
for(const [a,b,t] of [['P06','P07',2500],['P13','P14',3500],['P10','P12',5000]]){await byCode[a].setReactionsAsync([{trigger:{type:'AFTER_TIMEOUT',timeout:t},actions:[nav_(b)]}]);}
page.flowStartingPoints=[{nodeId:byCode['P01'].id,name:'Prueba 1 · El trayecto de Daniela'}];
out.push({links,backs,miss,timeout:byCode['P06'].reactions[0].trigger});
return out;
