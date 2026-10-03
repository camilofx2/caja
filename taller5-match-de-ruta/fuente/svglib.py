"""Mini motor de layout para generar láminas SVG con texto editable en Figma."""
import os
from html import escape
from PIL import ImageFont

FONT_DIR = os.environ.get("FONT_DIR", os.path.expanduser("~/.fonts"))

BLUE = "#084FE9"
YEL = "#FFB81C"
INK = "#0B1B3F"
MUTE = "#5A6887"
WHITE = "#FFFFFF"
LBLUE = "#E6EEFE"
LINE = "#D3DBEA"
LYEL = "#FFF3D6"
LGRAY = "#EEF0F4"
BG = "#F3F6FC"
GREEN = "#127A3F"
LGREEN = "#DDF3E5"
BROWN = "#8A5A00"
RED = "#B42318"
LRED = "#FDECEA"

GROT = "Space Grotesk"
MONO = "Space Mono"

_cache = {}


def _font(size, weight, mono):
    key = (size, weight, mono)
    if key not in _cache:
        if mono:
            f = ImageFont.truetype(os.path.join(FONT_DIR, "SpaceMono-Bold.ttf" if weight >= 700 else "SpaceMono-Regular.ttf"), size)
        else:
            f = ImageFont.truetype(os.path.join(FONT_DIR, "SpaceGrotesk-VF.ttf"), size)
            f.set_variation_by_axes([weight])
        _cache[key] = f
    return _cache[key]


def measure(text, size, weight=400, mono=False, ls=0):
    return _font(size, weight, mono).getlength(text) + ls * size * len(text)


def wrap(text, size, weight, maxw, mono=False, ls=0):
    out = []
    for para in text.split("\n"):
        words = para.split(" ")
        cur = ""
        for w in words:
            cand = (cur + " " + w).strip()
            if measure(cand, size, weight, mono, ls) <= maxw or not cur:
                cur = cand
            else:
                out.append(cur)
                cur = w
        out.append(cur)
    return out


class Svg:
    def __init__(self, w, h=None, bg=WHITE):
        self.w, self.h, self.bg = w, h, bg
        self.els = []

    def add(self, s):
        self.els.append(s)

    def g(self, name):
        self.add(f'<g id="{escape(name, quote=True)}">')

    def endg(self):
        self.add("</g>")

    def rect(self, x, y, w, h, fill=WHITE, stroke=None, sw=2, r=0, dash=None, name=None, opacity=None):
        a = f'x="{x:.0f}" y="{y:.0f}" width="{w:.0f}" height="{h:.0f}" fill="{fill}"'
        if r:
            a += f' rx="{r}" ry="{r}"'
        if stroke:
            a += f' stroke="{stroke}" stroke-width="{sw}"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        if opacity is not None:
            a += f' fill-opacity="{opacity}"'
        if name:
            a += f' id="{escape(name, quote=True)}"'
        self.add(f"<rect {a}/>")

    def circle(self, cx, cy, r, fill, stroke=None, sw=2):
        a = f'cx="{cx:.0f}" cy="{cy:.0f}" r="{r}" fill="{fill}"'
        if stroke:
            a += f' stroke="{stroke}" stroke-width="{sw}"'
        self.add(f"<circle {a}/>")

    def poly(self, pts, fill, stroke=None, sw=2):
        p = " ".join(f"{x:.0f},{y:.0f}" for x, y in pts)
        a = f'points="{p}" fill="{fill}"'
        if stroke:
            a += f' stroke="{stroke}" stroke-width="{sw}"'
        self.add(f"<polygon {a}/>")

    def path(self, pts, stroke=INK, sw=3, dash=None):
        d = "M " + " L ".join(f"{x:.0f} {y:.0f}" for x, y in pts)
        a = f'd="{d}" fill="none" stroke="{stroke}" stroke-width="{sw}" stroke-linejoin="round"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        self.add(f"<path {a}/>")

    def arrow(self, pts, stroke=INK, sw=3, hs=14):
        self.path(pts[:-1] + [self._shorten(pts[-2], pts[-1], hs - 2)], stroke, sw)
        (x1, y1), (x2, y2) = pts[-2], pts[-1]
        s = hs
        if abs(x2 - x1) >= abs(y2 - y1):
            d = 1 if x2 > x1 else -1
            tri = [(x2, y2), (x2 - d * s * 1.3, y2 - s * 0.75), (x2 - d * s * 1.3, y2 + s * 0.75)]
        else:
            d = 1 if y2 > y1 else -1
            tri = [(x2, y2), (x2 - s * 0.75, y2 - d * s * 1.3), (x2 + s * 0.75, y2 - d * s * 1.3)]
        self.poly(tri, stroke)

    @staticmethod
    def _shorten(a, b, n):
        (x1, y1), (x2, y2) = a, b
        if x1 == x2:
            return (x2, y2 - n if y2 > y1 else y2 + n)
        return (x2 - n if x2 > x1 else x2 + n, y2)

    def pathd(self, d, fill, stroke=None, sw=2, dash=None):
        a = f'd="{d}" fill="{fill}"'
        if stroke:
            a += f' stroke="{stroke}" stroke-width="{sw}"'
        if dash:
            a += f' stroke-dasharray="{dash}"'
        self.add(f"<path {a}/>")

    def text(self, x, y, s, size=22, weight=400, color=INK, maxw=None, lh=1.35, mono=False, ls=0, center=False, name=None):
        """Escribe un bloque de texto (y = borde superior). Devuelve la altura usada."""
        lines = wrap(s, size, weight, maxw, mono, ls) if maxw else s.split("\n")
        fam = MONO if mono else GROT
        lsa = f' letter-spacing="{ls * size:.2f}"' if ls else ""
        nm = f' id="{escape(name, quote=True)}"' if name else ""
        base = y + size * 0.92
        parts = []
        for i, ln in enumerate(lines):
            lx = x
            if center:
                lx = x - measure(ln, size, weight, mono, ls) / 2
            dy = 0 if i == 0 else size * lh
            parts.append(f'<tspan x="{lx:.0f}" dy="{dy:.0f}">{escape(ln)}</tspan>')
        self.add(f'<text{nm} y="{base:.0f}" font-family="{fam}" font-size="{size}" font-weight="{weight}" fill="{color}"{lsa}>' + "".join(parts) + "</text>")
        return len(lines) * size * lh

    def save(self, path, h=None):
        h = h or self.h
        head = f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w}" height="{h:.0f}" viewBox="0 0 {self.w} {h:.0f}">'
        bg = f'<rect id="Fondo" x="0" y="0" width="{self.w}" height="{h:.0f}" fill="{self.bg}"/>'
        with open(path, "w", encoding="utf-8") as f:
            f.write(head + bg + "\n".join(self.els) + "</svg>")
        import xml.dom.minidom
        xml.dom.minidom.parse(path)  # falla si el SVG no es XML válido


def text_h(s, size, weight, maxw, lh=1.35, mono=False, ls=0):
    return len(wrap(s, size, weight, maxw, mono, ls)) * size * lh


def header(svg, x, y, w, tag, title, intro, retro):
    """Encabezado común de cada lámina. Devuelve la nueva y."""
    svg.g("Encabezado")
    y += svg.text(x, y, tag, 22, 700, BLUE, mono=True, ls=0.08) + 24
    y += svg.text(x, y, title, 104, 700, INK, lh=1.05) + 28
    if intro:
        y += svg.text(x, y, intro, 30, 400, MUTE, maxw=min(w, 2400), lh=1.45) + 40
    if retro:
        inner = w - 80
        hh = 32 + 18 * 1.35 + 14 + text_h(retro, 26, 400, inner, 1.45) + 32
        svg.rect(x, y, w, hh, LYEL, r=20, name="Lo que pidió la profe")
        yy = y + 32
        yy += svg.text(x + 40, yy, "LO QUE PIDIÓ LA PROFE", 18, 700, INK, mono=True, ls=0.08) + 14
        svg.text(x + 40, yy, retro, 26, 400, INK, maxw=inner, lh=1.45)
        y += hh + 56
    svg.endg()
    return y
