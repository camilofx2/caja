// P01 Bienvenida
{const f=await scr('P01','Bienvenida',0,'neutral/900');scene(f,412,520);await sbar(f,'8:40 p. m.','neutral/0');
const c=box(f,'Contenido',16,0,380,{itemSpacing:24});await lockup(c,32,'neutral/0','primario/500','neutral/900');
const t=AL(c,'VERTICAL',{itemSpacing:12});await T(t,'Tu trayecto,\nacompañado.','disp','neutral/0');await T(t,'Encuentra personas verificadas que hacen tu mismo recorrido de noche y avisa a quien te espera.','base','neutral/400');
const a=AL(c,'VERTICAL',{itemSpacing:12,paddingTop:8});await pill(a,'Crear cuenta','a','Ir:P02');await pill(a,'Ya tengo cuenta','ow','Ir:P02');bottom(c,32);out.push(f.id);}
// P02 Inicio
{const f=await scr('P02','Inicio',1);mapBg(f,412,917);await route(f,[[0,200],[0,110],[110,0],[230,0]],80,250,['f','now',null,'o']);await gchip(f,'Calle 45',100,430);await gchip(f,'Portal Sur',248,214);await sbar(f,'8:52 p. m.');
const tp=figma.createAutoLayout('HORIZONTAL',{name:'Saludo',paddingLeft:8,paddingRight:16,cornerRadius:28,counterAxisAlignItems:'CENTER',itemSpacing:12});f.appendChild(tp);tp.resize(380,56);tp.primaryAxisSizingMode='FIXED';tp.counterAxisSizingMode='FIXED';tp.x=16;tp.y=44;glass(tp,0.4);circ(tp,40,0,0,'neutral/400');await T(tp,'Hola, Daniela','strong');icon(tp,'bell',24,'neutral/900');
await nav(f,'Hoy');
const cd=box(f,'Tarjeta de hoy',16,0,380,{itemSpacing:16,paddingLeft:20,paddingRight:20,paddingTop:20,paddingBottom:20,cornerRadius:28});cd.fills=P('neutral/0');cd.effects=shadow();
await T(cd,'Hoy · de la U a la casa','label','neutral/600');await T(cd,'Sales a las 9:00 p. m.','h1');await person(cd,'Laura M. y 1 persona más','✓ Verificadas · salen a tu hora');await pill(cd,'Ver las 2 personas','n','Ir:P03');cd.y=917-16-72-12-cd.height;out.push(f.id);}
// P03 Personas compatibles
{const f=await scr('P03','Personas compatibles',2,'neutral/100');await sbar(f,'8:53 p. m.');
const c=box(f,'Contenido',16,56,380,{itemSpacing:24});const h=AL(c,'VERTICAL',{itemSpacing:4});await T(h,'Personas compatibles','h1');await T(h,'Hoy · 9:00 p. m. · Calle 45 → Bosa Centro','label','neutral/600');
const ch=AL(c,'HORIZONTAL',{itemSpacing:8});await chip(ch,'Filtros · 2',false);await chip(ch,'Solo mujeres',true);await chip(ch,'Mi universidad',true);
const L=AL(c,'VERTICAL',{itemSpacing:12});
for(const [n,v,a,b,t,bars,go] of [['Laura M.','✓ Verificada · Universidad','Calle 45 → Portal Sur','14 trayectos · 2 conocidos en común','9:05',[1,1,0],'Ir:P04'],['Sara P.','✓ Verificada por su círculo','Portal Sur → Bosa Centro','6 trayectos acompañados','9:10',[0,0,1],'Tarjeta']]){
const cd=AL(L,'VERTICAL',{name:go,itemSpacing:16,paddingLeft:20,paddingRight:20,paddingTop:20,paddingBottom:20,cornerRadius:24});cd.fills=P('neutral/0');cd.effects=shadow(0.05);
const r=AL(cd,'HORIZONTAL',{itemSpacing:12,counterAxisAlignItems:'CENTER'});circ(r,56,0,0,'neutral/200');const col=AL(r,'VERTICAL',{itemSpacing:2});col.layoutSizingHorizontal='FILL';await T(col,n,'h2');await T(col,v,'label','primario/500');const tm=AL(r,'VERTICAL',{counterAxisAlignItems:'MAX'},true);await T(tm,t,'h2','neutral/900',{hug:true});await T(tm,'p. m.','hint','neutral/600',{hug:true});
const tb=AL(cd,'VERTICAL',{itemSpacing:8});const br=AL(tb,'HORIZONTAL',{itemSpacing:4});for(const x of bars){const s=rect(br,40,6,0,0,x?'primario/500':'neutral/200',3);s.layoutSizingHorizontal='FILL';}await T(tb,a+' · '+bars.filter(x=>x).length+' de 3 tramos en común','label','neutral/900');await T(tb,b,'hint','neutral/600');}
await T(c,'No mostramos destino final, apellido ni celular.','hint','neutral/600');await nav(f,'Matches');out.push(f.id);}
// P04 Detalle (y base de P05)
async function detalle(f){await sbar(f,'8:54 p. m.');await back(f);
const c=box(f,'Contenido',16,100,380,{itemSpacing:24});await person(c,'Laura M.','✓ Verificada · Universidad',['Correo institucional · desde marzo de 2026'],{d:72,big:true});
const mp=FR_(c,380,220,0,0,'Tramo en común');mp.cornerRadius=24;mp.clipsContent=true;mapBg(mp,380,220);await route(mp,[[0,150],[0,90],[90,0],[220,0]],70,40,['f',null,null,'o']);await gchip(mp,'Se unen · Calle 45',94,160);await gchip(mp,'Se separan · Portal Sur',150,52);
const st=AL(c,'HORIZONTAL',{itemSpacing:12});for(const [n,l] of [['14','trayectos'],['14','confirmados'],['0','reportes']]){const s=AL(st,'VERTICAL',{itemSpacing:2,paddingLeft:16,paddingTop:16,paddingBottom:16,cornerRadius:20});s.fills=P('neutral/100');s.layoutSizingHorizontal='FILL';await T(s,n,'h1');await T(s,l,'hint','neutral/600');}
await T(c,'Encuentro 8:55 p. m. en la entrada norte · 1 h juntas · prefiere espera + trayecto','label','neutral/600');
const a=box(f,'Acciones',16,0,380,{itemSpacing:8});await pill(a,'Pedirle el trayecto','n','Ir:P05');await pill(a,'Bloquear o reportar','t');bottom(a,16);}
{const f=await scr('P04','Detalle de Laura',3);await detalle(f);out.push(f.id);}
{const f=await scr('P05','Pedir el trayecto',4);await detalle(f);const sh=await sheet(f);await T(sh,'Pedirle el trayecto a Laura','h2');await T(sh,'Si acepta, se abren el chat, el punto de encuentro y un código para reconocerse.','base','neutral/600');
const q=AL(sh,'VERTICAL',{itemSpacing:8,paddingBottom:8});await T(q,'Mensaje rápido (opcional)','label','neutral/600');const w=AL(q,'HORIZONTAL',{itemSpacing:8,layoutWrap:'WRAP',counterAxisSpacing:8});await chip(w,'Salgo a las 9:00');await chip(w,'Te espero en la entrada norte',true);await chip(w,'Hola, voy para el sur');
await pill(sh,'Enviar solicitud','n','Ir:P06');sh.y=917-sh.height;out.push(f.id);}
return out;
