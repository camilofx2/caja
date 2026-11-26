// FigJam · Match de ruta · Parte 1: portada y secciones 01–05 (contenido desde EXPLICACION-PROYECTO.md)
const h = (hex) => { const n = parseInt(hex.replace('#',''),16); return {r:((n>>16)&255)/255,g:((n>>8)&255)/255,b:(n&255)/255}; };
const solid = (hex) => [{type:'SOLID', color:h(hex)}];
await figma.loadFontAsync({family:'Inter',style:'Medium'});
await figma.loadFontAsync({family:'Inter',style:'Bold'});
await figma.loadFontAsync({family:'Inter',style:'Regular'});
const page = figma.currentPage;
for (const n of [...page.children]) n.remove();

const C = { ink:'#1E1E1E', muted:'#5a5577', violet:'#5b3df5', violetSoft:'#eeebfe', lima:'#c8f560',
  yellow:'#FFE8A3', green:'#CDF4D3', blue:'#C2E5FF', pink:'#FFC7DE', orange:'#FFD3A8', gray:'#E6E6E6', purple:'#DCCCFF', white:'#FFFFFF' };

function txt(parent, s, x, y, size, opts={}) {
  const t = figma.createText();
  t.fontName = {family:'Inter', style: opts.bold ? 'Bold' : (opts.regular ? 'Regular':'Medium')};
  t.characters = s; t.fontSize = size; t.fills = solid(opts.color || C.ink);
  if (opts.w) { t.textAutoResize = 'HEIGHT'; t.resize(opts.w, t.height); }
  parent.appendChild(t); t.x = x; t.y = y; return t;
}
function card(parent, s, x, y, w, fill, opts={}) {
  const sh = figma.createShapeWithText();
  sh.shapeType = opts.shape || 'ROUNDED_RECTANGLE';
  sh.fills = solid(fill); sh.strokes = solid(opts.stroke || fill); sh.strokeWeight = 2;
  sh.text.fontName = {family:'Inter', style: opts.bold ? 'Bold':'Medium'};
  sh.text.characters = s; sh.text.fontSize = opts.size || 20;
  sh.text.fills = solid(opts.color || C.ink);
  parent.appendChild(sh);
  sh.resize(w, opts.h || 120); sh.x = x; sh.y = y; return sh;
}
function sticky(parent, s, x, y, fill, wide=false) {
  const st = figma.createSticky();
  st.text.fontName = {family:'Inter',style:'Medium'};
  st.text.characters = s; st.fills = solid(fill);
  if (wide) st.isWideWidth = true;
  parent.appendChild(st); st.x = x; st.y = y; return st;
}
function section(name, x, y, w, hgt, fill) {
  const s = figma.createSection(); s.name = name; s.resizeWithoutConstraints(w, hgt);
  s.x = x; s.y = y; s.fills = solid(fill); page.appendChild(s); return s;
}
function header(s, num, title, sub) {
  txt(s, num, 80, 70, 24, {bold:true, color:C.violet});
  txt(s, title, 80, 105, 64, {bold:true});
  if (sub) txt(s, sub, 80, 200, 24, {color:C.muted, w: s.width - 160});
}
function conn(a, b, label) {
  const c = figma.createConnector();
  c.connectorStart = {endpointNodeId:a.id, magnet:'RIGHT'}; c.connectorEnd = {endpointNodeId:b.id, magnet:'LEFT'};
  c.strokes = solid(C.violet); c.strokeWeight = 4; c.connectorEndStrokeCap = 'ARROW_LINES';
  if (label) { c.text.fontName = {family:'Inter',style:'Medium'}; c.text.characters = label; c.text.fontSize = 16; }
  return c;
}
const W = 1920, H = 1200, GAP = 240;
const ids = {};

// ---------------- 00 · Portada
{
  const s = section('00 · Portada e índice', 0, -1500, W, 1100, '#14112b'); ids.s00 = s.id;
  txt(s, 'TALLER 5 · DISEÑO E INTERACCIÓN · INVESTIGACIÓN', 80, 90, 24, {bold:true, color:C.lima});
  txt(s, 'Match de ruta', 80, 140, 128, {bold:true, color:C.white});
  txt(s, 'Proceso de investigación: de la hipótesis inicial al producto', 80, 310, 40, {color:'#d5d2e5', w:1500});
  txt(s, 'Juan Camilo Orozco Galindo · Profesora María Camila Ayala', 80, 380, 24, {color:'#a29dba'});
  const idx = ['01 · Brief e hipótesis inicial','02 · Entrevistas: lo que encontramos','03 · Síntesis y análisis','04 · Ideación y MoSCoW','05 · MVP',
               '06 · Benchmarking','07 · User persona','08 · Arquitectura de la información','09 · User flows','10 · Del hallazgo a la pantalla'];
  idx.forEach((t,i) => card(s, t, 80 + (i%5)*352, 520 + Math.floor(i/5)*150, 320, i<5 ? '#252140' : '#3b3658', {color:C.white, size:22, h:120, bold:true}));
  txt(s, 'Cómo leer el tablero: cada sección es una lámina. Se leen de izquierda a derecha, fila por fila. Los datos con número salen de las 5 entrevistas; lo marcado [S] es supuesto.', 80, 860, 24, {color:'#d5d2e5', w:1700});
}

// ---------------- 01 · Brief e hipótesis
{
  const s = section('01 · Brief e hipótesis inicial', 0, 0, W, H, '#FFF8E1'); ids.s01 = s.id;
  header(s, '01', 'Brief e hipótesis inicial', 'Así empezó el proyecto, antes de hablar con nadie.');
  txt(s, 'EL BRIEF', 80, 300, 20, {bold:true, color:C.muted});
  card(s, 'María José planteó el problema: esperar el bus de noche en zonas oscuras, sin saber cuánto tarda.', 80, 340, 760, C.white, {size:28, h:220, stroke:'#E0C36A'});
  txt(s, 'HIPÓTESIS INICIAL', 80, 610, 20, {bold:true, color:C.muted});
  const hip = card(s, '“El problema es no saber cuánto tarda el bus.”', 80, 650, 760, C.yellow, {size:36, h:220, bold:true, stroke:'#E0C36A'});
  txt(s, 'SI LA HIPÓTESIS FUERA CIERTA…', 1000, 300, 20, {bold:true, color:C.muted});
  sticky(s, 'Quien ya usa apps de rutas y tiempos debería sentirse tranquilo esperando', 1000, 340, C.yellow);
  sticky(s, 'La solución sería otra app de tiempos de llegada', 1280, 340, C.yellow);
  sticky(s, 'Las personas elegirían dónde esperar según lo que dice la app', 1560, 340, C.yellow);
  txt(s, 'LO QUE SALIÓ AL VALIDAR (sección 02)', 1000, 640, 20, {bold:true, color:C.muted});
  const res = card(s, 'No se cumplió. 5 de 5 usan apps de rutas y aun así sienten miedo, y 0 de 5 eligen dónde esperar por una app.', 1000, 680, 800, '#FFD6D6', {size:26, h:190, stroke:'#E58A8A'});
  conn(hip, res, 'se puso a prueba con 5 entrevistas');
  card(s, 'Conclusión: no falta información, falta compañía. La hipótesis cambió y con ella el proyecto.', 80, 960, 1720, C.violet, {size:30, h:140, color:C.white, bold:true});
}

// ---------------- 02 · Entrevistas
{
  const s = section('02 · Entrevistas: lo que encontramos', W + GAP, 0, W, H, '#EAF6FF'); ids.s02 = s.id;
  header(s, '02', 'Entrevistas: lo que encontramos', '5 personas que se mueven de noche en transporte público. Cada nota es un hallazgo, agrupado por tema.');
  const people = [['María José, 21','Planteó el brief'],['Juan José, 21',''],['Luna Valentina, 25',''],['Kimberly, 21',''],['Daniel, 21','']];
  people.forEach(([n,d],i) => card(s, d ? n + '\n' + d : n, 80 + i*352, 270, 320, C.white, {size:22, h:100, bold:true, stroke:'#8FC9F0'}));
  const groups = [
    ['APPS Y MIEDO', C.yellow, ['5 de 5 usan apps de rutas', 'Aun así, los 5 sienten miedo de noche']],
    ['INCIDENTES', C.pink, ['5 de 5 cuentan un incidente concreto que vivieron', 'Las 3 mujeres hablan de violencia sexual', 'Los 2 hombres hablan de robo']],
    ['CAMBIAR DE PLAN', C.orange, ['4 de 5 cambiaron de plan alguna vez', 'Opciones: moto, carro, conductora mujer o dormir donde un amigo']],
    ['AVISAR A ALGUIEN', C.green, ['2 comparten la ubicación siempre', '2 avisan por mensaje', '1 no avisa a nadie']],
    ['DÓNDE ESPERAR', C.purple, ['0 de 5 eligen dónde esperar por una app', 'Eligen por la luz, la cercanía y la gente']],
  ];
  let gx = 80;
  groups.forEach(([title, color, notes]) => {
    txt(s, title, gx, 420, 20, {bold:true, color:C.muted});
    notes.forEach((n, j) => sticky(s, n, gx, 460 + j*250, color));
    gx += 352;
  });
}

// ---------------- 03 · Síntesis y análisis
{
  const s = section('03 · Síntesis y análisis', (W + GAP)*2, 0, W, H, '#F1EEFF'); ids.s03 = s.id;
  header(s, '03', 'Síntesis y análisis', 'De los hallazgos sacamos 6 insights. Cada uno termina en una decisión de diseño.');
  const ins = [
    ['1 · Tener información no quita el miedo', '5 de 5 usan apps de rutas y sienten miedo', 'Dar compañía real, no más datos'],
    ['2 · El miedo viene de algo vivido', '5 de 5 cuentan un incidente concreto', 'Diseñar para un riesgo real'],
    ['3 · Ante el riesgo, buscan no estar solos', '4 de 5 cambiaron de plan', 'Atacar la causa: estar solo'],
    ['4 · Avisar ya es un hábito, pero manual', '2 comparten ubicación, 2 escriben, 1 no avisa', 'Llevar el aviso a la app'],
    ['5 · El miedo cambia según el género', 'Mujeres: violencia sexual · hombres: robo', 'Preferencia de género (modo solo mujeres)'],
    ['6 · Nadie elige dónde esperar por una app', '0 de 5; eligen por luz, cercanía y gente', 'Tiempos de llegada como capa secundaria'],
  ];
  ins.forEach(([t, e, d], i) => {
    const x = 80 + (i%3)*590, y = 280 + Math.floor(i/3)*290;
    card(s, t + '\n\nEvidencia: ' + e + '\n→ ' + d, x, y, 560, C.white, {size:20, h:250, stroke:'#B9A8FF'});
  });
  card(s, 'PROBLEMA REPLANTEADO\n“Quien depende del transporte nocturno espera y viaja solo, sin saber si alguien de su entorno hace el mismo recorrido a la misma hora.”\nEntorno = misma universidad, mismo trabajo o mismo barrio.', 80, 880, 1120, C.violet, {size:22, h:260, color:C.white, bold:true});
  txt(s, 'CAMINOS DESCARTADOS', 1260, 860, 20, {bold:true, color:C.muted});
  sticky(s, 'App de tiempos de llegada: los 5 ya usan una y siguen con miedo', 1260, 900, C.gray);
  sticky(s, 'Acompañante desconocido: nadie confía en un extraño → verificación obligatoria', 1520, 900, C.gray);
}

// ---------------- 04 · Ideación y MoSCoW
{
  const s = section('04 · Ideación y MoSCoW', (W + GAP)*3, 0, W, H + 200, '#EFFBF0'); ids.s04 = s.id;
  header(s, '04', 'Ideación y MoSCoW', '16 ideas priorizadas. Solo la columna Must entra en el MVP.');
  const cols = [
    ['MUST · entra en el MVP', C.green, ['01 · 11 Registro verificado','02 Ruta y horario','03 Emparejamiento automático','04 Ubicación en vivo temporal']],
    ['SHOULD · segunda versión', C.blue, ['05 Dejar de compartir','09 Aviso a contacto','06 Preferencia de género','12 Reporte de conducta']],
    ['COULD · si hay tiempo', C.yellow, ['07 Chat para coordinar','08 Confirmación mutua','14 Solo acompañar la espera','16 Tiempos de llegada']],
    ["WON'T · no se hará", C.gray, ['10 Historial de ubicaciones','15 Reverificación periódica','13 Sugerir hora de salida']],
  ];
  cols.forEach(([t, color, ideas], i) => {
    const x = 80 + i*440;
    txt(s, t, x, 280, 22, {bold:true});
    ideas.forEach((n, j) => sticky(s, n, x, 330 + j*260, color));
  });
}

// ---------------- 05 · MVP
{
  const s = section('05 · MVP', (W + GAP)*4, 0, W, H, '#FFF0F6'); ids.s05 = s.id;
  header(s, '05', 'MVP', '“Una app para emparejarte con alguien verificado que hace tu mismo trayecto de noche.”');
  const parts = [
    ['REGISTRO', 'Te verificas con correo institucional o con 2 avales de tu círculo cercano', 'Ideas 01 y 11 · Ingreso y Verificación · F01–F08'],
    ['MATCH', 'Guardas ruta y horario; la app te muestra quién hace el mismo tramo a la misma hora', 'Ideas 02 y 03 · Mis rutas, Matches, Match · F10–F14'],
    ['TRAYECTO', 'Ubicación en vivo que solo dura el trayecto y se apaga al llegar', 'Idea 04 · Trayecto activo · F17–F18'],
  ];
  const nodes = parts.map(([t, d, r], i) => card(s, t + '\n\n' + d + '\n\n' + r, 80 + i*600, 320, 540, i===1 ? C.violet : C.white, {size:22, h:380, color: i===1 ? C.white : C.ink, stroke:'#F2A7C6'}));
  conn(nodes[0], nodes[1]); conn(nodes[1], nodes[2]);
  txt(s, 'AJUSTES AL MVP (y por qué)', 80, 780, 20, {bold:true, color:C.muted});
  sticky(s, '05 Dejar de compartir → Must. Respuesta a la retro: compartir la ubicación también es un riesgo', 80, 820, C.pink, true);
  sticky(s, '08 Confirmación mutua → Must. Sin el sí de las dos personas, el match conectaría sin permiso', 540, 820, C.pink, true);
  sticky(s, 'Código de encuentro (Should) y atajo al 123 (Could): salen del benchmarking y de los riesgos', 1000, 820, C.pink, true);
  sticky(s, 'La arquitectura muestra el producto completo; el MVP es solo la columna Must', 1460, 820, C.gray);
}
return ids;
