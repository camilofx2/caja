// Figma Design · página "Evolución del proyecto": línea de tiempo, misma pantalla en v1/v2/v3 y ajustes del 25 nov.
// Clona pantallas reales de las páginas v1 (31:2), v2 (76:2) y v3 (125:2); no modifica los originales.
const NAME = 'Evolución del proyecto · de la hipótesis a la v3';
let page = figma.root.children.find(p => p.name === NAME);
if (!page) { page = figma.createPage(); page.name = NAME; figma.root.insertChild(1, page); }
await figma.setCurrentPageAsync(page);
for (const n of [...page.children]) n.remove();

const F = { t:{family:'Bricolage Grotesque',style:'ExtraBold'}, b:{family:'Figtree',style:'Regular'}, s:{family:'Figtree',style:'SemiBold'}, x:{family:'Figtree',style:'Bold'} };
for (const k in F) { try { await figma.loadFontAsync(F[k]); } catch(e) { F[k] = {family:'Inter', style: k==='b' ? 'Regular' : 'Bold'}; await figma.loadFontAsync(F[k]); } }
const h = (hex) => { const n = parseInt(hex.replace('#',''),16); return {r:((n>>16)&255)/255,g:((n>>8)&255)/255,b:(n&255)/255}; };
const solid = (hex, o=1) => [{type:'SOLID', color:h(hex), opacity:o}];
const C = { bg:'#14112b', s1:'#1a1730', s2:'#252140', line:'#3b3658', muted:'#a29dba', soft:'#d5d2e5', white:'#ffffff', violet:'#5b3df5', lima:'#c8f560' };

function T(parent, s, x, y, size, font='b', color=C.soft, w) {
  const t = figma.createText(); t.fontName = F[font]; t.characters = s; t.fontSize = size; t.fills = solid(color);
  t.lineHeight = {unit:'PERCENT', value: font==='t' ? 110 : 140};
  if (w) { t.textAutoResize = 'HEIGHT'; t.resize(w, t.height); }
  parent.appendChild(t); t.x = x; t.y = y; return t;
}
function R(parent, x, y, w, hh, fill, r=24, stroke) {
  const f = figma.createFrame(); f.resize(w, hh); f.x = x; f.y = y; f.fills = solid(fill); f.cornerRadius = r;
  if (stroke) { f.strokes = solid(stroke); f.strokeWeight = 2; }
  parent.appendChild(f); return f;
}
function board(name, x, y, w, hh) { const f = figma.createFrame(); f.name = name; f.resize(w, hh); f.x = x; f.y = y; f.fills = solid(C.bg); f.cornerRadius = 0; page.appendChild(f); return f; }
async function phone(parent, id, x, y, scale=0.5) {
  const src = await figma.getNodeByIdAsync(id);
  const c = src.clone(); parent.appendChild(c); c.rescale(scale); c.x = x; c.y = y;
  c.cornerRadius = 12; c.clipsContent = true; c.name = 'Copia · ' + src.name; return c;
}
const W = 2960;

// ---------- 01 · Línea de tiempo
const b1 = board('Evolución · 01 Línea de tiempo', 0, 0, W, 900);
T(b1, 'EVOLUCIÓN DEL PROYECTO', 96, 88, 22, 'x', C.lima);
T(b1, 'De una hipótesis equivocada a 90 pantallas en alta', 96, 124, 64, 't', C.white, 2200);
T(b1, 'Cada paso cambió el proyecto. Los números salen de los archivos: 5 entrevistas, 16 ideas, 39 → 82 → 90 pantallas.', 96, 210, 26, 'b', C.muted, 2400);
const hitos = [
  ['Brief', 'Hipótesis: “el problema es no saber cuánto tarda el bus”.'],
  ['Entrevistas', '5 personas. 5 de 5 usan apps de rutas y aun así sienten miedo.'],
  ['Síntesis', '6 insights. Problema replanteado: no falta información, falta compañía.'],
  ['Ideación', '16 ideas, MoSCoW y MVP: registro, match y trayecto.'],
  ['Análisis', 'Benchmarking (6 apps), persona, arquitectura y 25 flujos.'],
  ['Wireframes v1', '39 pantallas en grises, 7 flujos. Revisión del 24 de octubre.'],
  ['Wireframes v2', '82 pantallas, 9 fases: ingreso, rutas, reportes y vista del contacto.'],
  ['Sistema de diseño', 'Clase del 7 de nov.: estados de campos, neutrales 0–900, auto layout. 18 componentes.'],
  ['Alta v3', '90 pantallas con identidad y prototipo navegable (7 recorridos).'],
  ['Ajustes 25 nov.', 'Identidad de noche, foto + código, puntos seguros y modo de compañía.'],
];
const cw = 262, gap = 20, y0 = 330;
const ln = figma.createRectangle(); ln.resize(W - 192, 4); ln.x = 96; ln.y = y0 + 34; ln.fills = solid(C.line); b1.appendChild(ln);
hitos.forEach(([t, d], i) => {
  const x = 96 + i * (cw + gap), last = i === hitos.length - 1, v3 = i >= 8;
  const dot = figma.createEllipse(); dot.resize(28, 28); dot.x = x; dot.y = y0 + 22; dot.fills = solid(last ? C.lima : (v3 ? C.violet : C.soft)); b1.appendChild(dot);
  T(b1, String(i + 1).padStart(2, '0'), x, y0 + 72, 20, 'x', last ? C.lima : C.muted);
  const card = R(b1, x, y0 + 110, cw, 330, last ? C.violet : C.s2, 20);
  T(card, t, 20, 22, 28, 't', C.white, cw - 40);
  T(card, d, 20, 110, 19, 'b', C.soft, cw - 40);
});
T(b1, 'Las fases 01–05 están en el FigJam de investigación y en la página “Investigación”. Las 06–10, en las páginas de wireframes, sistema de diseño y alta.', 96, 820, 20, 'b', C.muted, 2600);

// ---------- 02 · Misma pantalla, tres versiones
const comps = [
  ['Bienvenida', '31:43', '76:41', '125:36',
   'v1: una sola pantalla con la promesa y las reglas de ubicación.\nv2: tres pasos con ilustración y un mensaje corto: “Nadie espera solo.”\nv3: identidad de noche e ilustración principal más llamativa.'],
  ['Foto en el momento', '31:261', '76:536', '131:546',
   'v1: la foto era un paso suelto del registro.\nv2: “Paso 3 de 3”, guía ovalada para el rostro y una pantalla para revisar la foto.\nv3: esa foto se usa después para reconocerse en el encuentro.'],
  ['Personas compatibles', '32:39', '79:60', '132:1376',
   'v1: cuatro filtros fijos ocupaban la parte de arriba.\nv2: un botón “Filtros · 2” abre su propia pantalla y las tarjetas quedan más cortas.\nv3: foto verificada y la línea de tramos en cada tarjeta.'],
  ['Detalle del match', '32:87', '79:185', '132:1525',
   'v1: el tramo era un bloque gris de mapa.\nv2: el tramo se dibuja: dónde se unen, dónde se separan y el último tramo sola. Reputación en números.\nv3: el mismo tramo con la línea de tramos de la identidad.'],
  ['Pedir el trayecto', '32:127', '79:249', '132:1599',
   'v1: solo existía “Solicitud enviada”; el punto se definía después.\nv2: pantalla para pedir el trayecto, con chat, punto y código al aceptar.\nv3: se elige un punto seguro con vigilancia: portería o CAI (25 nov.).'],
  ['Encuentro', '32:246', '79:618', '133:1316',
   'v1: el código aparecía dentro de la pantalla del encuentro.\nv2: pantalla propia para confirmar el código en voz alta.\nv3: doble chequeo: ¿es la persona de la foto? y ¿coincide el código? (25 nov.).'],
];
const rowH = 720, colW = 1420;
const b2 = board('Evolución · 02 Misma pantalla, tres versiones', 0, 1040, W, 260 + Math.ceil(comps.length / 2) * (rowH + 40));
T(b2, 'MISMA PANTALLA, TRES VERSIONES', 96, 88, 22, 'x', C.lima);
T(b2, 'Cómo cambió cada pantalla clave', 96, 124, 56, 't', C.white);
for (let i = 0; i < comps.length; i++) {
  const [name, a, b, c, txt] = comps[i];
  const x = 96 + (i % 2) * (colW + 24), y = 250 + Math.floor(i / 2) * (rowH + 40);
  const card = R(b2, x, y, colW, rowH, C.s1, 28, C.line);
  T(card, String(i + 1).padStart(2, '0') + ' · ' + name, 32, 32, 34, 't', C.white, 560);
  T(card, txt, 32, 100, 19, 'b', C.soft, 560);
  const labels = ['v1 · grises', 'v2 · grises', 'v3 · alta'];
  for (let k = 0; k < 3; k++) {
    const px = 640 + k * 256;
    T(card, labels[k], px, 32, 18, 'x', k === 2 ? C.lima : C.muted);
    await phone(card, [a, b, c][k], px, 70, 0.55);
  }
}

// ---------- 03 · Ajustes del 25 de noviembre
const y3 = b2.y + b2.height + 140;
const b3 = board('Evolución · 03 Ajustes del 25 de noviembre', 0, y3, W, 1000);
T(b3, 'REVISIÓN DEL 25 DE NOVIEMBRE', 96, 88, 22, 'x', C.lima);
T(b3, 'Cuatro comentarios, cuatro cambios', 96, 124, 56, 't', C.white);
const aj = [
  ['“Se parece mucho a Uber”', 'Identidad de noche: base índigo, títulos en Bricolage Grotesque y la línea de tramos como recurso propio.', 'Todas las pantallas · Identidad, lámina 09'],
  ['Evitar la suplantación', 'Foto tomada en el momento + código. Al encontrarse se confirman las dos cosas.', 'B04 Foto · F05 ¿Es Laura?'],
  ['Puntos de encuentro seguros', 'Solo se proponen puntos con vigilancia: porterías, recepciones y CAI.', 'E05 Pedir el trayecto · componente Punto seguro'],
  ['Modo solo mujeres (o al revés)', 'Modo de compañía: solo mujeres, solo hombres o cualquier persona. Solo hay match si ambas preferencias coinciden.', 'H03 Preferencias · E03 Filtros'],
];
aj.forEach(([c, d, p], i) => {
  const x = 96 + i * 702, card = R(b3, x, 250, 680, 360, i === 0 ? C.violet : C.s2, 24);
  T(card, 'COMENTARIO', 28, 28, 16, 'x', i === 0 ? C.white : C.muted);
  T(card, c, 28, 56, 30, 't', C.white, 620);
  T(card, d, 28, 150, 20, 'b', C.soft, 620);
  T(card, '→ ' + p, 28, 290, 18, 's', C.lima, 620);
});
const after = [['132:1599', 'E05 · punto seguro'], ['133:1316', 'F05 · foto + código'], ['132:1376', 'E02 · línea de tramos']];
for (let i = 0; i < after.length; i++) {
  T(b3, after[i][1], 96 + i * 300, 650, 18, 'x', C.lima);
  await phone(b3, after[i][0], 96 + i * 300, 684, 0.6);
}
T(b3, 'El prototipo se auditó después de los cambios: 170 enlaces, 0 destinos rotos y 7 recorridos de inicio.', 1100, 700, 24, 's', C.soft, 1700);
const hb = b3.children.reduce((m, n) => Math.max(m, n.y + n.height), 0); b3.resize(W, hb + 96);
return { page: page.id, b1: b1.id, b2: b2.id, b3: b3.id };
