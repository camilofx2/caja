"""Empaca los SVG en scripts de la API de plugins de Figma (cada uno < 49 000 caracteres)."""
import json
import os
import re
import sys

BASE = os.path.join(os.path.dirname(__file__), "..", "figma")
LIMIT = 48500
GAP = 80
PAD = 100

TOKENS = [
    ('font-family="Space Grotesk"', "§G"), ('font-family="Space Mono"', "§M"), ("<tspan x=\"", "§t"), ("</tspan>", "§u"),
    ('font-weight="400"', "§4"), ('font-weight="700"', "§7"), ('font-weight="500"', "§5"), ("<text y=\"", "§x"), ("</text>", "§X"),
    ('fill="#FFFFFF"', "§W"), ('fill="#1F1F1F"', "§D"), ('fill="#C7D7FB"', "§S"), ('fill="#2160EB"', "§C"), ('fill="#FFB81C"', "§Y"),
    ("<rect x=\"", "§r"), ("<path d=\"M ", "§p"), ("<polygon points=\"", "§o"), ("<circle cx=\"", "§c"), (" stroke-width=\"", "§w"),
    ("font-size=\"", "§z"), (" height=\"", "§h"), (" width=\"", "§v"), ("\" dy=\"", "§d"),
]


def svg_size(txt):
    w = int(re.search(r'width="(\d+)"', txt).group(1))
    h = int(re.search(r'height="(\d+)"', txt).group(1))
    return w, h


def compress(txt):
    for a, b in TOKENS:
        assert b not in txt
        txt = txt.replace(a, b)
    return txt


def load(folder, name):
    with open(os.path.join(BASE, folder, name + ".svg"), encoding="utf-8") as f:
        return f.read()


def plan():
    """Devuelve la lista de (sección, nombre del frame, svg, x, y) y el tamaño de cada sección."""
    items = []
    sections = []
    sy = 0
    # 1 · Benchmarking (2 filas × 4)
    bench = [("B1", "B1 · Benchmarking 1 de 4"), ("B2", "B2 · Benchmarking 2 de 4"), ("B3", "B3 · Benchmarking 3 de 4"),
             ("B4", "B4 · Benchmarking 4 de 4"), ("B5", "B5 · Conclusión"), ("B6", "B6 · Oportunidad de diseño"),
             ("B7", "B7 · Diferenciación"), ("B8", "B8 · Riesgos")]
    pers = [("P1", "P1 · User persona"), ("P2", "P2 · Quién es y su contexto"), ("P3", "P3 · Trayecto y tensión"),
            ("P4", "P4 · Necesidades, comportamiento y frustraciones"), ("P5", "P5 · Motivaciones, miedos y decisiones"),
            ("P6", "P6 · Escenario y otras personas")]
    mvp = [("M1", "M1 · MVP"), ("M2", "M2 · MoSCoW")]
    for sname, lst, ncol in [("00 · MVP", mvp, 2), ("01 · Benchmarking", bench, 4), ("02 · User persona", pers, 3)]:
        for i, (f, nm) in enumerate(lst):
            items.append((sname, nm, load("laminas", f), PAD + (i % ncol) * (1920 + GAP), PAD + (i // ncol) * (1080 + GAP), f))
        rows = (len(lst) + ncol - 1) // ncol
        sw, sh = 2 * PAD + ncol * 1920 + (ncol - 1) * GAP, 2 * PAD + rows * 1080 + (rows - 1) * GAP
        sections.append((sname, 0, sy, sw, sh))
        sy += sh + 200
    # 3 · Arquitectura
    a1 = load("tableros", "A1")
    w1, h1 = svg_size(a1)
    items.append(("03 · Arquitectura", "A1 · Arquitectura de la información", a1, PAD, PAD, "A1"))
    items.append(("03 · Arquitectura", "A2 · Las 4 preguntas de la revisión", load("laminas", "A2"), PAD + w1 + GAP, PAD, "A2"))
    sections.append(("03 · Arquitectura", 0, sy, 2 * PAD + w1 + GAP + 1920, 2 * PAD + max(h1, 1080)))
    sy += 2 * PAD + max(h1, 1080) + 200
    # 4 · User flows (apilados)
    y = PAD
    wmax = 0
    names = ["F00 · Notación e índice", "F01–F04 · Acceso", "F05–F08 · Verificación", "F09–F12 · Inicio y Mis rutas",
             "F13–F16 · Matches", "F17–F19 · Trayecto activo", "F20–F23 · Perfil", "F24–F25 · Confianza y contacto avisado"]
    for f, nm in zip(["F00", "F01g", "F02g", "F03g", "F04g", "F05g", "F06g", "F07g"], names):
        t = load("flujos", f)
        w, h = svg_size(t)
        items.append(("04 · User flows", nm, t, PAD, y, f))
        y += h + GAP
        wmax = max(wmax, w)
    sections.append(("04 · User flows", 0, sy, 2 * PAD + wmax, y - GAP + PAD))
    return items, sections


PRELUDE = r"""
const T = %s;
const S = %s;
const fonts = [["Space Grotesk","Regular"],["Space Grotesk","Medium"],["Space Grotesk","Bold"],["Space Mono","Regular"],["Space Mono","Bold"]];
await Promise.all(fonts.map(([family, style]) => figma.loadFontAsync({family, style})));
const page = figma.currentPage;
function sec(name) {
  const d = S.find(s => s[0] === name);
  let s = page.findChild(n => n.type === "SECTION" && n.name === name);
  if (!s) { s = figma.createSection(); s.name = name; }
  s.x = d[1]; s.y = d[2];
  s.resizeWithoutConstraints(d[3], d[4]);
  return s;
}
function expand(z) { for (const [a, b] of T) z = z.split(b).join(a); return z; }
const made = [];
function place(secName, name, z, x, y) {
  const s = sec(secName);
  const old = s.findChild(n => n.name === name);
  if (old) old.remove();
  const f = figma.createNodeFromSvg(expand(z));
  f.name = name;
  s.appendChild(f);
  f.x = x; f.y = y;
  made.push({id: f.id, name, w: Math.round(f.width), h: Math.round(f.height), texts: f.findAllWithCriteria({types: ["TEXT"]}).length});
}
"""


def build_calls(only=None):
    items, sections = plan()
    if only:
        items = [it for it in items if it[5] in only]
    pre = PRELUDE % (json.dumps(TOKENS, ensure_ascii=False), json.dumps(sections, ensure_ascii=False))
    calls = []
    for it in items:
        z = compress(it[2])
        line = f"place({json.dumps(it[0], ensure_ascii=False)}, {json.dumps(it[1], ensure_ascii=False)}, {json.dumps(z, ensure_ascii=False)}, {it[3]}, {it[4]});\n"
        if len(line) + len(pre) + 200 > LIMIT:
            raise SystemExit(f"{it[1]} no cabe en una sola llamada ({len(line)} caracteres)")
        for c in calls:
            if sum(map(len, c)) + len(pre) + len(line) + 200 <= LIMIT:
                c.append(line)
                break
        else:
            calls.append([line])
    # la primera llamada borra las secciones anteriores para reconstruir todo desde cero
    # quita frames con nombres anteriores que ya no existen
    reset = "for (const n of page.findAll(n => n.name === \"A2 · Las 4 preguntas de la profe\")) n.remove();\n"
    out = []
    for i, c in enumerate(calls):
        out.append(pre + (reset if i == 0 else "") + "".join(c) + "return made;\n")
    return out


if __name__ == "__main__":
    d = sys.argv[1]
    os.makedirs(d, exist_ok=True)
    only = set(sys.argv[2].split(",")) if len(sys.argv) > 2 else None
    for i, js in enumerate(build_calls(only), 1):
        p = os.path.join(d, f"llamada{i:02d}.js")
        with open(p, "w", encoding="utf-8") as f:
            f.write(js)
        print(p, len(js), js.count("place(") - 1)
