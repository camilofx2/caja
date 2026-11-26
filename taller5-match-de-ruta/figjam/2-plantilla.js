// FigJam · Match de ruta · Parte 2: secciones 06–10 (datos inyectados desde fuente/contenido.py por generar-parte2.py)
const D = /*DATA*/null;
const h = (hex) => { const n = parseInt(hex.replace('#',''),16); return {r:((n>>16)&255)/255,g:((n>>8)&255)/255,b:(n&255)/255}; };
const solid = (hex) => [{type:'SOLID', color:h(hex)}];
for (const st of ['Medium','Bold','Regular']) await figma.loadFontAsync({family:'Inter',style:st});
const page = figma.currentPage;
for (const n of [...page.children]) if (/^(06|07|08|09|10) ·/.test(n.name)) n.remove();
const C = { ink:'#1E1E1E', muted:'#5a5577', violet:'#5b3df5', lima:'#c8f560', yellow:'#FFE8A3', green:'#CDF4D3', blue:'#C2E5FF',
  pink:'#FFC7DE', orange:'#FFD3A8', gray:'#E6E6E6', purple:'#DCCCFF', white:'#FFFFFF', red:'#FFB3B3', dark:'#14112b' };
const DESIGN = 'https://www.figma.com/design/B9iRO9GFetHn3IN3nbbWGJ?node-id=';

function txt(parent, s, x, y, size, o={}) {
  const t = figma.createText();
  t.fontName = {family:'Inter', style: o.bold ? 'Bold' : 'Medium'};
  t.characters = s; t.fontSize = size; t.fills = solid(o.color || C.ink);
  if (o.w) { t.textAutoResize = 'HEIGHT'; t.resize(o.w, t.height); }
  if (o.link) t.hyperlink = {type:'URL', value:o.link};
  parent.appendChild(t); t.x = x; t.y = y; return t;
}
function card(parent, s, x, y, w, hh, fill, o={}) {
  const sh = figma.createShapeWithText();
  sh.shapeType = o.shape || 'ROUNDED_RECTANGLE';
  sh.fills = solid(fill); sh.strokes = solid(o.stroke || fill); sh.strokeWeight = 2;
  sh.text.fontName = {family:'Inter', style:'Medium'};
  sh.text.characters = s; sh.text.fontSize = o.size || 22; sh.text.fills = solid(o.color || C.ink);
  const i = s.indexOf('\n');
  if (o.title !== false && i > 0) { sh.text.setRangeFontName(0, i, {family:'Inter',style:'Bold'}); sh.text.setRangeFontSize(0, i, o.tsize || (o.size||22)+4); }
  if (o.allBold) sh.text.fontName = {family:'Inter', style:'Bold'};
  parent.appendChild(sh); sh.resize(w, hh); sh.x = x; sh.y = y; return sh;
}
function sticky(parent, s, x, y, fill, wide=false) {
  const st = figma.createSticky(); st.text.fontName = {family:'Inter',style:'Medium'};
  st.text.characters = s; st.text.fontSize = 22; st.fills = solid(fill); if (wide) st.isWideWidth = true;
  parent.appendChild(st); st.x = x; st.y = y; return st;
}
function section(name, x, y, w, hh, fill) {
  const s = figma.createSection(); s.name = name; s.resizeWithoutConstraints(w, hh);
  s.x = x; s.y = y; s.fills = solid(fill); page.appendChild(s); return s;
}
function header(s, num, title, sub, link) {
  txt(s, num, 80, 70, 24, {bold:true, color:C.violet});
  txt(s, title, 80, 105, 64, {bold:true});
  if (sub) txt(s, sub, 80, 200, 24, {color:C.muted, w: 1700});
  if (link) txt(s, 'Ver la lámina completa en Figma Design ↗', s.width - 700, 90, 24, {bold:true, color:C.violet, link: DESIGN + link});
}
function conn(a, b, o={}) {
  const c = figma.createConnector();
  c.connectorStart = {endpointNodeId:a.id, magnet:o.from || 'RIGHT'}; c.connectorEnd = {endpointNodeId:b.id, magnet:o.to || 'LEFT'};
  c.strokes = solid(o.color || C.violet); c.strokeWeight = 3; c.connectorEndStrokeCap = 'ARROW_LINES';
  if (o.label) { c.text.fontName = {family:'Inter',style:'Bold'}; c.text.characters = o.label; c.text.fontSize = 18; }
  return c;
}
function fit(s) {
  let maxX = 0, maxY = 0;
  for (const c of s.children) { maxX = Math.max(maxX, c.x + c.width); maxY = Math.max(maxY, c.y + c.height); }
  s.resizeWithoutConstraints(Math.max(s.width, maxX + 80), maxY + 100);
}
const ids = {};
const ROW2 = 1900;

// ---------------- 02 · completar con patrones [E] de la persona
{
  const s02 = page.findOne(n => n.type==='SECTION' && n.name.startsWith('02 ·'));
  if (s02 && !s02.findOne(n => n.name === 'otros-patrones')) {
    const t = txt(s02, 'OTROS PATRONES QUE SE REPITIERON', 80, 1240, 20, {bold:true, color:C.muted}); t.name = 'otros-patrones';
    ['Esperan en paraderos con poca luz que se van quedando vacíos', 'Una persona entrevistada cuenta que la siguieron al bajarse del bus',
     'Con gente escuchan música; cuando quedan solos, la apagan y guardan el celular', 'Los hombres van alerta, no sacan el celular y a veces cambian de ruta',
     'En la familia quieren saber con quién van y que llegaron, sin tener que llamar', 'Usan Google Maps para ir a lugares nuevos']
     .forEach((n, i) => sticky(s02, n, 80 + i*290, 1280, C.blue));
    fit(s02);
  }
}

// ---------------- 06 · Benchmarking
{
  const s = section('06 · Benchmarking', 0, ROW2, 4300, 2600, '#F3F7FF'); ids.s06 = s.id;
  header(s, '06', 'Benchmarking', '6 apps comparadas en 18 funcionalidades y el costo. ● sí · ◐ parcial · ○ no · ? por verificar · * depende del país o del plan.', '7-2');
  const T = D.tabla, R = T.length, Cn = T[0].length;
  const tb = figma.createTable(R, Cn); s.appendChild(tb); tb.x = 80; tb.y = 290;
  tb.resizeColumn(0, 380); for (let c = 1; c < Cn; c++) tb.resizeColumn(c, 290);
  for (let r = 0; r < R; r++) for (let c = 0; c < Cn; c++) {
    const cell = tb.cellAt(r, c); let v = T[r][c]; const grp = T[r][0].startsWith('§');
    if (grp && c === 0) v = v.slice(1);
    if (c === 0 && r > 0 && !grp) v = v;
    cell.text.characters = v || ' ';
    cell.text.fontSize = r === 0 ? 22 : (grp ? 18 : 18);
    if (r === 0 || grp || c === 0) cell.text.fontName = {family:'Inter', style:'Bold'};
    if (r === 0) cell.fills = solid(c === Cn-1 ? C.violet : '#252140');
    if (r === 0) cell.text.fills = solid(C.white);
    else if (grp) cell.fills = solid('#DCE6FF');
    else if (c === Cn-1) cell.fills = solid('#EEEBFE');
    else cell.fills = solid(C.white);
  }
  const X = 2480 + 120, Wr = 1600;
  txt(s, '¿QUÉ ENCONTRÉ? · 6 HALLAZGOS', X, 290, 22, {bold:true, color:C.muted});
  D.hallazgos.forEach(([t, e, m], i) => card(s, `${i+1} · ${t}\n${e}\n→ ${m}`, X + (i%2)*810, 330 + Math.floor(i/2)*330, 780, 300, C.white, {size:18, tsize:22, stroke:'#9DB7F5'}));
  card(s, 'OPORTUNIDAD DE DISEÑO\n' + D.oportunidad, X, 1340, Wr, 170, C.violet, {size:22, color:C.white});
  card(s, 'PROPUESTA DE VALOR\n' + D.propuesta, X, 1540, Wr, 200, '#252140', {size:20, color:C.white});
  const difColor = {'TOMO':C.green, 'EVITO':C.red, 'SOLO MATCH':C.lima};
  D.dif.forEach(([t, sub, items], i) => card(s, `${t} · ${sub}\n` + items.map(x => '• ' + x).join('\n'), X + i*540, 1780, 520, 400, difColor[t] || C.gray, {size:17, tsize:20}));
  txt(s, 'RIESGOS Y CÓMO LOS ABORDO', X, 2220, 22, {bold:true, color:C.muted});
  D.riesgos.forEach(([t, d, r], i) => card(s, `${t}\n${d}\n→ ${r}`, X + i*540, 2260, 520, 260, C.orange, {size:17, tsize:22}));
  fit(s);
}

// ---------------- 07 · User persona
let s07;
{
  const s = section('07 · User persona', 4540, ROW2, 3000, 2600, '#FFF4FA'); ids.s07 = s.id; s07 = s;
  header(s, '07', 'User persona', 'Daniela es una composición basada en las 5 entrevistas. [E] = dato de las entrevistas · [S] = supuesto para completar el perfil.', '6-2');
  const F = D.ficha;
  card(s, `${F.nombre}\n${F.linea}\n\n${F.cita}\nObjetivo: llegar a casa tranquila, sin depender de que la recojan ni de pagar un carro cada noche.`, 80, 290, 2840, 260, C.dark, {size:22, tsize:44, color:C.white});
  txt(s, 'SU TRAYECTO DE UN MARTES · NIVEL DE TENSIÓN', 80, 600, 22, {bold:true, color:C.muted});
  const tc = {1:C.green, 2:C.yellow, 3:C.orange, 4:C.red};
  const nodes = D.trayecto.map(([hora, mom, det, lvl, est], i) =>
    card(s, `${hora} · ${mom}\n${det}\n${est.toUpperCase()}`, 80 + i*406, 640 + (4 - lvl)*60, 380, 260, tc[lvl], {size:17, tsize:20}));
  for (let i = 0; i < nodes.length - 1; i++) conn(nodes[i], nodes[i+1], {color:'#3b3658'});
  card(s, 'Lectura: la tensión más alta está en la espera del alimentador y en la caminata a casa. Match cubre la espera con compañía y la caminata con el aviso al contacto hasta tocar “Llegué”.', 80, 1130, 2840, 110, C.violet, {size:22, color:C.white, title:false});
  const bc = [C.white, C.white, C.white, C.blue, C.blue, C.blue, C.pink, C.pink, C.pink];
  D.bloques.forEach(([t, items], i) => card(s, t + '\n' + items.map(x => '• ' + x).join('\n'), 80 + (i%3)*955, 1290 + Math.floor(i/3)*470, 925, 440, bc[i], {size:17, tsize:20, stroke:'#F2A7C6'}));
  card(s, 'ESCENARIO CON MATCH\n' + D.escenario, 80, 2720, 1400, 400, C.yellow, {size:18, tsize:22});
  D.secundarias.forEach(([n, rol, sub, items, nota], i) => card(s, `${n} · ${sub}\n${rol}\n` + items.map(x => '• ' + x).join('\n') + '\n→ ' + nota, 1520 + i*710, 2720, 690, 400, C.white, {size:16, tsize:22, stroke:'#F2A7C6'}));
  fit(s);
}

// ---------------- 08 · Arquitectura (fila 3)
const ROW3 = ROW2 + Math.max(page.findOne(n=>n.name==='06 · Benchmarking').height, s07.height) + 300;
{
  const s = section('08 · Arquitectura de la información', 0, ROW3, 3600, 2400, '#F1FFF4'); ids.s08 = s.id;
  header(s, '08', 'Arquitectura de la información', 'Qué contiene la plataforma (no el paso a paso: eso son los flujos).', '5-2');
  const root = card(s, 'Match de ruta', 1500, 290, 600, 110, C.dark, {size:30, color:C.white, allBold:true});
  const L1 = [
    ['1 · Ingreso', ['Bienvenida', 'Crear cuenta: celular + código SMS, datos, permisos, términos y Ley 1581', 'Iniciar sesión', 'Recuperar cuenta']],
    ['2 · Verificación', ['Correo institucional', 'Círculo cercano (avales)', 'Estado de la cuenta', 'Mis círculos']],
    ['3 · Inicio (barra inferior)', ['HOY: próximo trayecto, personas disponibles, solicitudes, iniciar trayecto, tiempos de llegada', 'MIS RUTAS: guardadas, crear o editar (partida, tramos, paradero, hora ±15 min, días), una sola vez, pausar', 'MATCHES: compatibles, filtros, solicitudes, compañía frecuente, sin matches', 'PERFIL: perfil público, datos privados, preferencias, contactos de confianza, privacidad, ajustes']],
    ['4 · Match', ['Personas compatibles', 'Detalle del match', 'Solicitud', 'Confirmación mutua', 'Chat breve']],
    ['5 · Trayecto activo', ['Banner fijo mientras dura', 'Antes de salir', 'Encuentro', 'En curso', 'Separación', 'Llegada', 'Retraso']],
    ['6 · Confianza', ['Confirmar el trayecto', '“¿Volverías a viajar?” (privado)', 'Reportar y bloquear', 'Sin historial']],
    ['7 · Vista del contacto (web, sin app)', ['Invitación', 'Enlace del trayecto', 'Avisos', 'Caducidad']],
  ];
  const colW = 470, gap = 20;
  L1.forEach(([t, items], i) => {
    const x = 80 + i*(colW + gap);
    const n = card(s, t, x, 500, colW, 100, i === 2 ? C.violet : C.green, {size:22, color: i===2 ? C.white : C.ink, allBold:true});
    conn(root, n, {from:'BOTTOM', to:'TOP', color:'#3b3658'});
    let y = 640;
    items.forEach(it => { const hh = it.length > 60 ? 190 : (it.length > 30 ? 110 : 80);
      card(s, it, x, y, colW, hh, C.white, {size:18, title:false, stroke:'#8FD19E'}); y += hh + 14; });
  });
  txt(s, 'LAS 4 PREGUNTAS DE LA REVISIÓN', 80, 1500, 22, {bold:true, color:C.muted});
  [['¿Cómo funciona la verificación por círculo cercano?', '2 avales de personas ya verificadas, que confirman que la conocen, la relación y desde cuándo. Máximo 5 avales por persona; si una cuenta avalada es suspendida, se revisan sus avales. (F07, F08)'],
   ['¿Qué muestra la plataforma al revisar perfiles?', 'Foto, nombre con inicial del apellido, insignia y método de verificación, institución o círculo, tramo en común, hora, punto de encuentro, trayectos y conocidos en común. Nunca destino, apellido ni celular. (F13)'],
   ['¿Dónde agrego los contactos que serán avisados?', 'Perfil → Contactos de confianza (máximo 3), con relación, canal (SMS o WhatsApp) y avisos. El contacto acepta. Antes de cada trayecto se confirma a quién avisar. (F21, F17)'],
   ['¿Qué contiene el detalle de un match?', 'Perfil ampliado, mapa del tramo compartido, punto y hora de encuentro, tiempo juntos, verificación, reputación, preferencia de compañía y acciones: solicitar, bloquear o reportar. (F13)']]
  .forEach(([q, a], i) => card(s, q + '\n' + a, 80 + i*860, 1540, 830, 330, C.yellow, {size:18, tsize:22}));
  fit(s);
}

// ---------------- 09 · User flows
{
  const s8 = page.findOne(n => n.name.startsWith('08 ·'));
  const s = section('09 · User flows', s8.x + s8.width + 240, ROW3, 3600, 2400, '#FFF9EE'); ids.s09 = s.id;
  header(s, '09', 'User flows', '25 flujos en 7 grupos. Abajo, el flujo del trayecto (F17–F18) dibujado con la misma notación.', '1-2');
  const legend = [['Inicio o fin', 'ROUNDED_RECTANGLE', C.gray], ['Pantalla o proceso', 'SQUARE', C.purple], ['La persona ingresa datos', 'PARALLELOGRAM_RIGHT', C.blue], ['El sistema valida o consulta', 'ENG_DATABASE', C.green], ['Decisión (sí / no)', 'DIAMOND', C.orange]];
  legend.forEach(([t, sh, col], i) => card(s, t, 80 + i*360, 290, 320, sh === 'DIAMOND' ? 160 : 100, col, {shape:sh, size:18, title:false}));
  const grupos = [['Acceso', 'F01 Ingreso · F02 Crear cuenta · F03 Iniciar sesión · F04 Recuperar cuenta'],
    ['Verificación', 'F05 Elegir método · F06 Correo institucional · F07 Pedir avales · F08 Dar un aval'],
    ['Inicio y Mis rutas', 'F09 Inicio · F10 Crear ruta y horario · F11 Gestionar rutas · F12 Trayecto de una sola vez'],
    ['Matches', 'F13 Ver compatibles y enviar solicitud · F14 Responder solicitud · F15 Sin matches · F16 Chat breve'],
    ['Trayecto activo', 'F17 Iniciar trayecto y encuentro · F18 En curso y llegada · F19 Dejar de compartir y pedir ayuda'],
    ['Perfil', 'F20 Perfil · F21 Contactos de confianza · F22 Preferencias de match · F23 Privacidad'],
    ['Confianza y contacto', 'F24 Confirmar trayecto y reportar · F25 Vista del contacto avisado']];
  grupos.forEach(([g, f], i) => card(s, g + '\n' + f.split(' · ').join('\n'), 80 + (i%4)*860, 500 + Math.floor(i/4)*300, 830, 270, C.white, {size:18, tsize:22, stroke:'#F5C98B'}));
  txt(s, 'FLUJO F17–F18 · TRAYECTO: ENCUENTRO, RECORRIDO Y LLEGADA', 80, 1140, 22, {bold:true, color:C.muted});
  const Y = 1220, st = (t, x, y, sh, col, w=300, hh=120) => card(s, t, x, y, w, hh, col, {shape:sh, size:17, title:false});
  const a = st('Inicia el trayecto', 80, Y + 20, 'ROUNDED_RECTANGLE', C.gray, 240, 90);
  const b = st('Confirma a quién avisar', 400, Y, 'PARALLELOGRAM_RIGHT', C.blue);
  const c = st('Se activa la ubicación temporal', 780, Y, 'ENG_DATABASE', C.green);
  const d = st('Va al punto de encuentro y toca “Ya llegué”', 1160, Y, 'SQUARE', C.purple);
  const e = st('¿La otra persona llegó en 10 min?', 1540, Y - 30, 'DIAMOND', C.orange, 320, 180);
  const e2 = st('Aviso: “Laura no ha llegado” · esperar, cancelar o seguir sola', 1540, Y + 260, 'SQUARE', C.purple, 320, 140);
  const f = st('Confirman el código de encuentro', 1940, Y, 'PARALLELOGRAM_RIGHT', C.blue);
  const g = st('Trayecto en curso', 2320, Y, 'SQUARE', C.purple);
  const hq = st('¿La compañía se baja antes?', 2700, Y - 30, 'DIAMOND', C.orange, 320, 180);
  const h2 = st('Se avisa al contacto: “sigue sola desde…”', 2700, Y + 260, 'ENG_DATABASE', C.green, 320, 140);
  const i1 = st('Llega y toca “Llegué”', 3100, Y, 'SQUARE', C.purple, 260, 120);
  const j = st('Se apaga la ubicación y el contacto recibe “llegó”', 3100, Y + 260, 'ENG_DATABASE', C.green, 260, 160);
  const k = st('Fin', 3100, Y + 500, 'ROUNDED_RECTANGLE', C.gray, 260, 90);
  conn(a, b); conn(b, c); conn(c, d); conn(d, e); conn(e, f, {label:'Sí'}); conn(e, e2, {from:'BOTTOM', to:'TOP', label:'No'});
  conn(f, g); conn(g, hq); conn(hq, i1, {label:'No'}); conn(hq, h2, {from:'BOTTOM', to:'TOP', label:'Sí'}); conn(h2, i1, {from:'RIGHT', to:'BOTTOM'});
  conn(i1, j, {from:'BOTTOM', to:'TOP'}); conn(j, k, {from:'BOTTOM', to:'TOP'});
  const t1 = st('Si pasan 15 min de la hora estimada sin llegar', 400, Y + 520, 'SQUARE', C.purple, 340, 120);
  const t2 = st('“¿Todo bien?” ¿Responde en 5 min?', 820, Y + 490, 'DIAMOND', C.orange, 320, 180);
  const t3 = st('El contacto recibe la última ubicación', 1220, Y + 520, 'ENG_DATABASE', C.green, 320, 120);
  conn(t1, t2); conn(t2, t3, {label:'No'});
  txt(s, 'Rama de retraso (también en F18)', 80, Y + 470, 18, {bold:true, color:C.muted});
  fit(s);
}

// ---------------- 10 · Del hallazgo a la pantalla
{
  const s9 = page.findOne(n => n.name.startsWith('09 ·'));
  const s = section('10 · Del hallazgo a la pantalla', s9.x + s9.width + 240, ROW3, 2600, 2400, '#14112b'); ids.s10 = s.id;
  txt(s, '10', 80, 70, 24, {bold:true, color:C.lima});
  txt(s, 'Del hallazgo a la pantalla', 80, 105, 64, {bold:true, color:C.white});
  txt(s, 'Cada decisión del diseño en alta se puede rastrear hasta la investigación.', 80, 200, 24, {color:'#d5d2e5'});
  txt(s, 'Ver las pantallas en alta en Figma Design ↗', 1800, 90, 24, {bold:true, color:C.lima, link: DESIGN + '125-2'});
  const head = ['Hallazgo', 'Decisión de diseño', 'Pantallas en alta (v3)'];
  const rows = [
    ['Insight 1 · Tener información no quita el miedo', 'Emparejar con alguien que hace el mismo tramo a la misma hora', 'E02 Personas compatibles · E04 Detalle del match'],
    ['Insight 2 · El miedo viene de algo vivido', 'Verificación doble (correo institucional o 2 avales) y foto tomada en el momento', 'B04 Foto en el momento · C02 Elegir 2 personas · C08 Verificada por círculo'],
    ['Insight 3 · Buscan dejar de estar solos', 'Encuentro en un punto seguro (CAI, portería o recepción) y espera acompañada', 'E05 Enviar solicitud · F02 Ve al punto de encuentro · F03 Esperando a Laura'],
    ['Insight 4 · Avisar es un hábito manual', 'Aviso automático al contacto, que sigue el trayecto sin instalar la app', 'H04 Contactos de confianza · I05 Trayecto en vivo · I08 Aviso de llegada'],
    ['Insight 5 · El miedo cambia según el género', 'Preferencia de compañía: solo mujeres o cualquiera', 'H03 Preferencias de match · E03 Filtros'],
    ['Insight 6 · Nadie elige dónde esperar por una app', 'Tiempos de llegada como capa secundaria, no como centro', 'E01 Inicio · hoy'],
    ['Benchmarking · riesgo de suplantación', 'Código de encuentro que ambas personas confirman', 'F05 Confirmar el código'],
    ['Benchmarking · masa crítica', 'Estado sin matches con alternativas, y trayecto de una sola vez', 'D07 Sin matches · D10 Trayecto de una sola vez'],
    ['Persona · Daniela no quiere exponer su rutina', 'Nunca se muestran destino, apellido ni celular; la ubicación se apaga al llegar', 'H02 Perfil público · F11 Llegaste · H08 Privacidad'],
    ['Revisión 25 nov · profesora', 'Foto contra suplantación, puntos seguros, identidad propia (menos Uber) y modo solo mujeres', 'B04 · E05 · Sistema de identidad · H03'],
  ];
  const tb = figma.createTable(rows.length + 1, 3); s.appendChild(tb); tb.x = 80; tb.y = 290;
  tb.resizeColumn(0, 700); tb.resizeColumn(1, 900); tb.resizeColumn(2, 840);
  [head, ...rows].forEach((r, i) => r.forEach((v, j) => { const cell = tb.cellAt(i, j);
    cell.text.characters = v; cell.text.fontSize = i === 0 ? 22 : 20;
    if (i === 0 || j === 0) cell.text.fontName = {family:'Inter',style:'Bold'};
    cell.fills = solid(i === 0 ? C.violet : (j === 2 ? '#EEEBFE' : C.white)); if (i === 0) cell.text.fills = solid(C.white); }));
  fit(s);
}
return ids;
