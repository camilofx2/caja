// 01 Portada
{const b=await board(1,'00 · Portada',null,true);b.minHeight=900;b.primaryAxisAlignItems='SPACE_BETWEEN';
const m=AL(b,'HORIZONTAL',{itemSpacing:56,counterAxisAlignItems:'CENTER',name:'Marca'});await symbol(m,220,'neutro/blanco','acento/principal','neutro/negro');
const mc=AL(m,'VERTICAL',{itemSpacing:16});mc.layoutSizingHorizontal='FILL';await T(mc,'match','mhero','neutro/blanco');await T(mc,'Mini manual de marca · v0.1','mp','neutro/blanco');await T(mc,'Compañía verificada para los trayectos de noche.','mp','neutro/gris-400');
const ft=AL(b,'HORIZONTAL',{itemSpacing:48,counterAxisAlignItems:'MAX',primaryAxisAlignItems:'SPACE_BETWEEN'});await T(ft,'Diseño e Interacción · Taller 5\nJuan Camilo Orozco Galindo · Octubre de 2026','label','neutro/gris-400',{w:560});
const nt=AL(ft,'VERTICAL',{itemSpacing:4,paddingLeft:20,paddingRight:20,paddingTop:16,paddingBottom:16,cornerRadius:16},true);nt.fills=P('neutro/gris-800');nt.resize(520,40);nt.primaryAxisSizingMode='AUTO';await T(nt,'Acento provisional: violeta','strong','neutro/blanco');await T(nt,'Está guardado como variable (acento/principal). Al elegir el color definitivo se cambia en un solo lugar y se actualiza todo el manual.','label','neutro/gris-400');
out.push(b.id);}
// 02 Concepto
{const b=await board(2,'01 · Concepto','Dos rutas, un tramo.');b.minHeight=900;
await T(b,'Match une a personas verificadas que hacen el mismo recorrido de noche. Toda la marca sale de la línea del trayecto: dos puntos de origen que se encuentran, comparten un tramo y llegan.','mp','neutro/gris-600',{w:900});
const [c1,c2]=colsRow(b,2,80);await T(c1,'Personalidad','h2');
for(const [a,d] of [['Tranquila','Acompaña sin alarmar. El rojo se guarda para emergencias.'],['Precisa','Horas, tramos y nombres concretos. Nada de “pronto” ni “cerca”.'],['Discreta','Muestra solo lo necesario: sin apellido, sin dirección, sin historial.'],['Cercana','Habla de tú, con frases cortas y el nombre de la persona.']]){const w=AL(c1,'VERTICAL',{itemSpacing:4});await T(w,a,'strong');await T(w,d,'base','neutro/gris-600');}
await T(c2,'Voz','h2');const tb=AL(c2,'VERTICAL',{itemSpacing:0,name:'Así sí / así no'});
const hr=AL(tb,'HORIZONTAL',{itemSpacing:24,paddingBottom:12});const h1=await T(hr,'Así sí','label','acento/principal');const h2=await T(hr,'Así no','label','neutro/gris-600');
for(const [y,n] of [['Laura llega en 4 min.','¡Tu compañera ya casi está aquí! 🚀'],['¿Todo bien, Daniela?','ALERTA: no has respondido'],['Llegaste.','¡Viaje completado con éxito!'],['Laura no está disponible hoy.','Tu solicitud fue rechazada.']]){const dv=rect(tb,10,1,0,0,'neutro/gris-200');dv.layoutSizingHorizontal='FILL';const r=AL(tb,'HORIZONTAL',{itemSpacing:24,paddingTop:16,paddingBottom:16});await T(r,y,'strong');await T(r,n,'base','neutro/gris-600');}
out.push(b.id);}
// 03 Referencias
{const b=await board(3,'02 · Referencias','Qué tomamos y qué no');b.minHeight=900;
const cs=colsRow(b,3,32);
const R=[['Uber','Rediseño de marca de 2018',['Base en blanco y negro, con mucho aire','Ilustraciones de formas simples, líneas limpias y color limitado','Un dato grande por pantalla'],['La tipografía Uber Move: es propietaria','La lógica de servicio: aquí no hay conductor ni tarifa']],['Apple · Liquid Glass','Presentado en la WWDC de 2025 (iOS 26)',['Capas flotantes translúcidas para la navegación y las hojas','El mapa o la ilustración pasan por debajo y se siguen viendo'],['Vidrio en todo: en iOS 26.1 Apple agregó la opción “Tintado” por quejas de legibilidad','Texto largo sobre fondos que cambian']],['Mapas de transporte','Harry Beck, metro de Londres (1933) · Massimo Vignelli, metro de Nueva York (1972)',['Líneas solo a 0°, 45° y 90°','Nodos claros: origen, encuentro y llegada','El diagrama pesa más que la geografía exacta'],['Muchos colores por línea: aquí solo importa una ruta, la tuya']]];
for(let i=0;i<3;i++){const c=cs[i];const [n,src,y,no]=R[i];const ph=AL(c,'HORIZONTAL',{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:16,name:'Referencia visual'});ph.fills=P('neutro/gris-100');ph.layoutSizingVertical='FIXED';ph.resize(ph.width,240);stroke(ph,'neutro/gris-200',1);await T(ph,'Pega aquí una captura de referencia','label','neutro/gris-600',{hug:true});
const hh=AL(c,'VERTICAL',{itemSpacing:4});await T(hh,n,'h2');await T(hh,src,'label','neutro/gris-600');
await T(c,'Tomamos','label','acento/principal');await bullets(c,y);await T(c,'No tomamos','label','neutro/gris-600');await bullets(c,no);}
out.push(b.id);}
// 04 Logo
{const b=await board(4,'03 · Logo','El símbolo es el producto');b.minHeight=900;
const [c1,c2]=colsRow(b,2,80);
const g=FR_(c1,400,400,0,0,'Construcción');g.fills=P('neutro/gris-100');g.cornerRadius=24;g.clipsContent=true;for(let i=1;i<8;i++){rect(g,1,400,i*50,0,'neutro/gris-200');rect(g,400,1,0,i*50,'neutro/gris-200');}const sy=await symbol(g,400,'neutro/negro','acento/principal','neutro/gris-100');
await T(c1,'Retícula de 80 × 80 unidades y trazo de 12. Dos orígenes (puntos llenos) se unen en un tramo compartido, en color de acento, y terminan en la llegada (círculo abierto). Es la misma línea del trayecto que aparece en la app.','base','neutro/gris-600');
const L=[['neutro/blanco','neutro/negro','acento/principal','neutro/blanco',true],['neutro/negro','neutro/blanco','acento/principal','neutro/negro'],['acento/principal','neutro/blanco','neutro/blanco','acento/principal']];
for(const [bg,ink,acc,ring,br] of L){const cd=AL(c2,'HORIZONTAL',{paddingLeft:40,paddingTop:32,paddingBottom:32,cornerRadius:24,name:'Versión'});cd.fills=P(bg);if(br)stroke(cd,'neutro/gris-200',1);await lockup(cd,72,ink,acc,ring);}
const ic=AL(c2,'HORIZONTAL',{itemSpacing:24,counterAxisAlignItems:'CENTER',name:'Ícono de app'});
for(const [bg,ink,acc] of [['neutro/negro','neutro/blanco','acento/principal'],['acento/principal','neutro/blanco','neutro/blanco']]){const a=AL(ic,'HORIZONTAL',{primaryAxisAlignItems:'CENTER',counterAxisAlignItems:'CENTER',cornerRadius:28},true);a.fills=P(bg);a.resize(120,120);a.primaryAxisSizingMode='FIXED';a.counterAxisSizingMode='FIXED';await symbol(a,76,ink,acc,bg);}
await T(ic,'Ícono de app','label','neutro/gris-600');
await bullets(c2,['Área de seguridad: el alto de un punto de origen alrededor de todo el logo.','Tamaño mínimo: símbolo de 24 px; logo horizontal de 96 px de ancho.','No rotar, no deformar, no ponerlo sobre vidrio ni sobre fotos.','El tramo compartido va en el acento o en el mismo color del resto. Nunca en un tercer color.'],'label');
out.push(b.id);}
// 05 Color
{const b=await board(5,'04 · Color','Blanco y negro, y un solo acento');
await T(b,'La base es neutra, como en Uber. El acento solo marca lo que importa: la línea del trayecto, el match y la acción principal. Si todo tiene color, nada destaca.','mp','neutro/gris-600',{w:900});
async function sw(p,n,hx,use,cr,h=96){const w=AL(p,'VERTICAL',{itemSpacing:4,name:'Muestra · '+n});w.layoutSizingHorizontal='FILL';const r=rect(w,10,h,0,0,n,16);r.layoutSizingHorizontal='FILL';if(hx==='FFFFFF')stroke(r,'neutro/gris-200',1);const sp=AL(w,'VERTICAL',{itemSpacing:2,paddingTop:8});await T(sp,n.split('/')[1],'strong');await T(sp,'#'+hx,'hint','neutro/gris-600');await T(sp,use,'hint','neutro/gris-600');if(cr)await T(sp,cr,'hint','neutro/negro');return w;}
await T(b,'Neutros','h2');const r1=AL(b,'HORIZONTAL',{itemSpacing:16});
for(const [n,h,u,c] of [['neutro/negro','0A0A0A','Texto y botón principal','19,8:1 sobre blanco'],['neutro/gris-800','27272A','Fondos oscuros','14,9:1'],['neutro/gris-600','5E5E66','Texto secundario','6,4:1'],['neutro/gris-400','A1A1AA','Bordes y desactivado','2,6:1 · no para texto'],['neutro/gris-200','E4E4E7','Divisores',''],['neutro/gris-100','F4F4F5','Fondo de tarjetas',''],['neutro/blanco','FFFFFF','Fondo','']])await sw(r1,n,h,u,c);
const r2=AL(b,'HORIZONTAL',{itemSpacing:48});const ca=AL(r2,'VERTICAL',{itemSpacing:16});ca.layoutSizingHorizontal='FILL';const cb=AL(r2,'VERTICAL',{itemSpacing:16});cb.layoutSizingHorizontal='FILL';
await T(ca,'Acento · 3 candidatas (elige una)','h2');const rr=AL(ca,'HORIZONTAL',{itemSpacing:16});
await sw(rr,'candidata/a-violeta','5B3DF5','A · Violeta noche · provisional','Texto blanco: 6,1:1 ✓',140);
await sw(rr,'candidata/b-lima','C8F560','B · Lima señal','Solo con texto negro: 15,7:1 · como texto sobre blanco: 1,3:1 ✗',140);
await sw(rr,'candidata/c-coral','E8461E','C · Coral','Texto blanco: 3,9:1 · solo títulos de 24 px o más · se confunde con alerta',140);
await T(cb,'Semánticos','h2');const rs=AL(cb,'HORIZONTAL',{itemSpacing:16});
await sw(rs,'semantico/exito','15803D','Llegada confirmada','5,0:1',140);await sw(rs,'semantico/alerta','B45309','Retraso','5,0:1',140);await sw(rs,'semantico/peligro','D92D20','123 y reportes','4,8:1',140);
await T(b,'Proporción de uso por pantalla','h2');const bar=AL(b,'HORIZONTAL',{itemSpacing:4,name:'Proporción'});
for(const [n,pc,l] of [['neutro/gris-100',70,'70 % blanco y grises claros'],['neutro/negro',22,'22 % negro y grises'],['acento/principal',6,'6 % acento'],['semantico/peligro',2,'2 %']]){const s=AL(bar,'VERTICAL',{itemSpacing:8},true);s.layoutSizingHorizontal='FILL';s.layoutGrow=pc;const rb=rect(s,10,32,0,0,n,8);rb.layoutSizingHorizontal='FILL';if(n==='neutro/gris-100')stroke(rb,'neutro/gris-200',1);await T(s,l,'hint','neutro/gris-600');}
out.push(b.id);}
return out;
