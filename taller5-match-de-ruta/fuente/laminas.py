"""Láminas 1920 × 1080 con la estética de la presentación (fondo azul, acentos amarillos)."""
from svglib import Svg, measure, wrap, text_h, YEL, WHITE, INK
import contenido as C

W, H = 1920, 1080
M = 120
CW = W - 2 * M
BLUE = "#084FE9"
CARD = "#2160EB"     # blanco al 10 % sobre el azul
CARD2 = "#3A73EE"    # blanco al 20 %
LINE = "#5285F0"     # blanco al 30 %
SOFT = "#C7D7FB"     # texto secundario
TOTAL = 15
BOTTOM = 950         # límite inferior del contenido


def slide(n, tag, title, sub=None, tsize=76):
    s = Svg(W, H, BLUE)
    s.text(M, 88, tag, 18, 700, YEL, mono=True, ls=0.06)
    lab = "Match de ruta verificado"
    s.text(W - M - measure(lab, 18, 400, True), 88, lab, 18, 400, SOFT, mono=True)
    s.text(M, 126, title, tsize, 700, WHITE, lh=1.05)
    y = 126 + tsize * 1.1 + 14
    if sub:
        y += s.text(M, y, sub, 22, 400, SOFT, maxw=1500, lh=1.4) + 10
    # pie: línea, puntos de avance y número
    s.path([(0, 990), (W, 990)], LINE, 1.5)
    for i in range(TOTAL):
        cx = M + i * 22
        if i == n - 1:
            s.circle(cx, 990, 7, YEL)
        else:
            s.circle(cx, 990, 4, LINE)
    pg = f"{n:02d} / {TOTAL}"
    s.text(W - M - measure(pg, 18, 400, True), 1018, pg, 18, 400, SOFT, mono=True)
    return s, y + 30


def check(y, name):
    assert y <= BOTTOM + 2, f"{name}: el contenido se sale ({y:.0f} > {BOTTOM})"


# ------------------------------------------------------------------ símbolos
def symbol(s, cx, cy, k):
    r = 12
    if k == "S":
        s.circle(cx, cy, r, YEL)
    elif k == "P":
        s.circle(cx, cy, r, BLUE, stroke=YEL, sw=3)
        s.pathd(f"M {cx} {cy - r} A {r} {r} 0 0 0 {cx} {cy + r} Z", YEL)
    elif k == "N":
        s.circle(cx, cy, r, BLUE, stroke=SOFT, sw=2)
    elif k == "V":
        s.circle(cx, cy, r, BLUE, stroke=SOFT, sw=2)
        s.text(cx, cy - 9, "?", 16, 700, SOFT, mono=True, center=True)


def legend(s, x, y):
    for k, lab in [("S", "Sí"), ("P", "Parcial"), ("N", "No"), ("V", "Por verificar")]:
        symbol(s, x + 12, y + 12, k)
        s.text(x + 32, y + 2, lab, 17, 400, WHITE, mono=True)
        x += 32 + measure(lab, 17, 400, True) + 34
    s.text(x, y + 2, "* confirmar en la app antes de entregar", 17, 400, SOFT, mono=True)


def bench_table(n, part, groups, note=None):
    s, y = slide(n, "04 · ANALIZAR · BENCHMARKING", f"Benchmarking ({part})", tsize=56)
    y -= 10
    featW = 430
    colW = (CW - featW) / 7
    # cabecera
    hl = len(s.els)
    for i, (nm, d) in enumerate(C.BENCH_COLS):
        cx = M + featW + i * colW
        s.text(cx + 12, y, nm, 22, 700, YEL if i == 6 else WHITE, maxw=colW - 20, lh=1.1)
        s.text(cx + 12, y + 30, d, 14, 400, SOFT, maxw=colW - 20, lh=1.25, mono=True)
    s.text(M, y + 4, "Funcionalidad", 18, 700, SOFT, mono=True)
    y += 78
    top = y
    rows = []
    cur = None
    for r in C.BENCH_ROWS:
        if r[0] == "G":
            cur = r[1]
            continue
        if cur in groups:
            rows.append((cur, r))
    last = None
    body = []
    for g, r in rows:
        if g != last:
            body.append(("G", g))
            last = g
        body.append(("R", r))
    # columna resaltada de Match
    yy = y
    hs = []
    for kind, r in body:
        if kind == "G":
            hs.append(40)
            continue
        h = 10 + text_h(r[0], 20, 700, featW - 20, 1.2) + (4 + text_h(r[1], 14, 400, featW - 20, 1.3) if r[1] else 0) + 10
        for c in r[2]:
            k, _, nt = c.partition("|")
            ch = 10 + (0 if k == "T" else 30) + (text_h(nt, 14, 400, colW - 24, 1.25) if nt else 0) + 10
            h = max(h, ch)
        hs.append(h)
    total = sum(hs)
    s.rect(M + featW + 6 * colW, top - 92, colW, total + 92 + 8, CARD2, r=18)
    s.els.insert(hl, s.els.pop())
    for (kind, r), h in zip(body, hs):
        if kind == "G":
            s.text(M, yy + 12, r, 15, 700, YEL, mono=True, ls=0.1)
            yy += h
            continue
        s.path([(M, yy), (M + CW, yy)], LINE, 1)
        t = yy + 10
        t += s.text(M, t, r[0], 20, 700, WHITE, maxw=featW - 20, lh=1.2)
        if r[1]:
            s.text(M, t + 4, r[1], 14, 400, SOFT, maxw=featW - 20, lh=1.3)
        for i, c in enumerate(r[2]):
            k, _, nt = c.partition("|")
            cx = M + featW + i * colW + 12
            if k == "T":
                s.text(cx, yy + 12, nt, 16, 500, WHITE, maxw=colW - 24, lh=1.25)
                continue
            star = k.endswith("*")
            k = k.rstrip("*")
            symbol(s, cx + 12, yy + 24, k)
            if star:
                s.text(cx + 30, yy + 12, "*", 18, 700, YEL, mono=True)
            if nt:
                s.text(cx, yy + 42, nt, 14, 400, WHITE if i == 6 else SOFT, maxw=colW - 24, lh=1.25)
        yy += h
    s.path([(M, yy), (M + CW, yy)], LINE, 1)
    yy += 22
    legend(s, M, yy)
    yy += 36
    if note:
        yy += s.text(M, yy, note, 17, 400, SOFT, maxw=CW, lh=1.4)
    check(yy, f"Benchmarking {part}")
    return s


def cards_grid(s, y, items, ncols, render, gap=28, bottom=BOTTOM):
    w = (CW - gap * (ncols - 1)) / ncols
    nrows = (len(items) + ncols - 1) // ncols
    for ri in range(nrows):
        row = items[ri * ncols:(ri + 1) * ncols]
        h = max(render(None, 0, 0, w, it, measure_only=True) for it in row)
        for ci, it in enumerate(row):
            render(s, M + ci * (w + gap), y, w, it, h=h)
        y += h + gap
    return y - gap


def bullets_card(s, x, y, w, it, h=None, measure_only=False, size=23):
    title, items = it[0], it[1]
    inner = w - 56
    hh = 28 + 16 * 1.35 + 14 + sum(text_h("• " + t, size, 400, inner, 1.4) + 8 for t in items) + 20
    if measure_only:
        return hh
    s.rect(x, y, w, h or hh, CARD, r=20)
    yy = y + 28
    yy += s.text(x + 28, yy, title, 16, 700, YEL, mono=True, ls=0.06) + 14
    for t in items:
        yy += s.text(x + 28, yy, "• " + t, size, 400, WHITE, maxw=inner, lh=1.4) + 8
    return hh


def build_all():
    out = {}
    n = 0

    # ---------------- Benchmarking
    n += 1
    out["B1 · Benchmarking (1 de 4)"] = bench_table(n, "1 de 4", ["MOVILIDAD", "SEGURIDAD Y RESPUESTA"])
    n += 1
    out["B2 · Benchmarking (2 de 4)"] = bench_table(n, "2 de 4", ["UBICACIÓN Y AVISOS", "MODELO"])
    n += 1
    out["B3 · Benchmarking (3 de 4)"] = bench_table(n, "3 de 4", ["IDENTIDAD Y CONFIANZA"])
    n += 1
    out["B4 · Benchmarking (4 de 4)"] = bench_table(
        n, "4 de 4", ["ACOMPAÑAMIENTO"],
        "Evalué 6 soluciones en 19 funcionalidades. Las celdas con * dependen del país, del plan de pago o de actualizaciones de la app. "
        "Waze Carpool se incluye como antecedente: Google cerró el servicio en 2022.")

    n += 1
    s, y = slide(n, "04 · ANALIZAR · BENCHMARKING", "Conclusión · ¿Qué encontré?")

    def hall(s, x, y, w, it, h=None, measure_only=False):
        i, (t, ev, imp) = it
        inner = w - 52
        hh = 26 + 34 + text_h(t, 23, 700, inner, 1.2) + 10 + text_h(ev, 16, 400, inner, 1.35) + 12 + text_h("→ " + imp, 17, 500, inner, 1.35) + 24
        if measure_only:
            return hh
        s.rect(x, y, w, h or hh, CARD, r=20)
        s.circle(x + 42, y + 42, 16, YEL)
        s.text(x + 42, y + 31, str(i), 18, 700, INK, mono=True, center=True)
        yy = y + 26 + 34
        yy += s.text(x + 26, yy, t, 23, 700, WHITE, maxw=inner, lh=1.2) + 10
        yy += s.text(x + 26, yy, ev, 16, 400, SOFT, maxw=inner, lh=1.35) + 12
        s.text(x + 26, yy, "→ " + imp, 17, 500, YEL, maxw=inner, lh=1.35)
        return hh
    y = cards_grid(s, y, list(enumerate(C.HALLAZGOS, 1)), 3, hall, gap=24)
    check(y, "Conclusión")
    out["B5 · Conclusión"] = s

    n += 1
    s, y = slide(n, "04 · ANALIZAR · BENCHMARKING", "Oportunidad de diseño")
    q = "“No se trata de dar más información sobre el bus. Se trata de que nadie tenga que esperar ni viajar solo.”"
    y += s.text(M, y, q, 34, 700, YEL, maxw=CW - 100, lh=1.25) + 30
    s.rect(M, y, CW, 0, CARD)
    ph = 30 + 16 * 1.35 + 12 + text_h(C.PROPUESTA, 32, 500, CW - 80, 1.4) + 30
    s.rect(M, y, CW, ph, CARD, r=20)
    yy = y + 30
    yy += s.text(M + 40, yy, "PROPUESTA DE VALOR", 16, 700, YEL, mono=True, ls=0.06) + 12
    s.text(M + 40, yy, C.PROPUESTA, 32, 500, WHITE, maxw=CW - 80, lh=1.4)
    y += ph + 28

    def vs(s, x, y, w, it, h=None, measure_only=False):
        a, b = it
        hh = 26 + 20 * 1.35 + 12 + text_h(b, 27, 400, w - 52, 1.4) + 26
        if measure_only:
            return hh
        s.rect(x, y, w, h or hh, BLUE, stroke=LINE, sw=2, r=20)
        yy = y + 26
        yy += s.text(x + 26, yy, a, 20, 700, YEL, mono=True) + 12
        s.text(x + 26, yy, b, 27, 400, WHITE, maxw=w - 52, lh=1.4)
        return hh
    y = cards_grid(s, y, C.PROPUESTA_VS, 4, vs, gap=24)
    check(y, "Oportunidad")
    out["B6 · Oportunidad de diseño"] = s

    n += 1
    s, y = slide(n, "04 · ANALIZAR · BENCHMARKING", "Diferenciación")

    def dif(s, x, y, w, it, h=None, measure_only=False):
        t, sub, items = it
        inner = w - 56
        hh = 30 + 40 + 6 + 22 + 18 + sum(text_h("• " + i, 26, 400, inner, 1.4) + 14 for i in items) + 20
        if measure_only:
            return hh
        hi = t == "SOLO MATCH"
        s.rect(x, y, w, h or hh, YEL if hi else CARD, r=20)
        fg = INK if hi else WHITE
        yy = y + 30
        yy += s.text(x + 28, yy, t, 34, 700, INK if hi else YEL) + 6
        yy += s.text(x + 28, yy, sub, 16, 400, INK if hi else SOFT, mono=True) + 18
        for i in items:
            yy += s.text(x + 28, yy, "• " + i, 26, 400, fg, maxw=inner, lh=1.4) + 14
        return hh
    y = cards_grid(s, y, C.DIFERENCIACION, 3, dif, gap=24)
    check(y, "Diferenciación")
    out["B7 · Diferenciación"] = s

    n += 1
    s, y = slide(n, "04 · ANALIZAR · BENCHMARKING", "Riesgos que revela el benchmarking")

    def rk(s, x, y, w, it, h=None, measure_only=False):
        a, b, c = it
        inner = w - 56
        hh = 30 + 34 * 1.2 + 12 + text_h(b, 24, 400, inner, 1.4) + 24 + 16 * 1.35 + 10 + text_h(c, 27, 500, inner, 1.4) + 30
        if measure_only:
            return hh
        s.rect(x, y, w, h or hh, CARD, r=20)
        yy = y + 30
        yy += s.text(x + 28, yy, a, 34, 700, WHITE) + 12
        yy += s.text(x + 28, yy, b, 24, 400, SOFT, maxw=inner, lh=1.4) + 24
        yy += s.text(x + 28, yy, "CÓMO LO ABORDO", 16, 700, YEL, mono=True, ls=0.06) + 10
        s.text(x + 28, yy, c, 27, 500, WHITE, maxw=inner, lh=1.4)
        return hh
    y = cards_grid(s, y, C.RIESGOS, 3, rk, gap=24)
    check(y, "Riesgos")
    out["B8 · Riesgos"] = s

    # ---------------- Persona
    n += 1
    s, y = slide(n, "04 · ANALIZAR · USER PERSONA", "User persona")
    F = C.PERSONA_FICHA
    lx, lw = M, 560
    s.rect(lx, y, lw, 660, CARD, r=24)
    s.circle(lx + 110, y + 110, 70, YEL)
    s.text(lx + 110, y + 70, "D", 72, 700, INK, center=True)
    yy = y + 200
    yy += s.text(lx + 36, yy, F["nombre"], 36, 700, WHITE, maxw=lw - 72, lh=1.15) + 12
    yy += s.text(lx + 36, yy, F["linea"], 18, 400, SOFT, maxw=lw - 72, lh=1.45) + 20
    yy += s.text(lx + 36, yy, F["cita"], 28, 700, YEL, maxw=lw - 72, lh=1.25) + 10
    s.text(lx + 36, yy, "PERSONA PRINCIPAL · [E] entrevistas · [S] supuesto", 14, 400, SOFT, mono=True, maxw=lw - 72)
    rx = lx + lw + 30
    rw = W - M - rx
    resumen = [
        ("OBJETIVO", "Llegar a casa tranquila, sin depender de que la recojan ni de pagar un carro cada noche."),
        ("NECESIDADES", "Saber quién de su universidad hace su mismo tramo a la misma hora · que su mamá sepa que llegó sin escribirle · que la otra persona esté verificada."),
        ("FRUSTRACIONES", "La app le da horarios, no tranquilidad · compartir la ubicación es manual · no confía en desconocidos."),
        ("MOTIVACIONES", "No sentirse sola en el momento más expuesto · autonomía · tranquilizar a su mamá."),
    ]
    yy = y
    for t, d in resumen:
        hh = 22 + 16 * 1.35 + 8 + text_h(d, 21, 400, rw - 56, 1.4) + 22
        s.rect(rx, yy, rw, hh, CARD, r=18)
        s.text(rx + 28, yy + 22, t, 16, 700, YEL, mono=True, ls=0.06)
        s.text(rx + 28, yy + 22 + 16 * 1.35 + 8, d, 21, 400, WHITE, maxw=rw - 56, lh=1.4)
        yy += hh + 12
    # recorrido emocional
    steps = ["Sale", "Camina", "Troncal", "Portal", "Espera", "Camina", "Llega"]
    hot = {4, 5}
    s.text(rx, yy + 6, "RECORRIDO", 16, 700, YEL, mono=True, ls=0.06)
    yy += 40
    px = rx
    for i, st in enumerate(steps):
        wdt = measure(st, 19, 700) + 30
        s.rect(px, yy, wdt, 40, YEL if i in hot else CARD2, r=20)
        s.text(px + 15, yy + 9, st, 19, 700, INK if i in hot else WHITE)
        px += wdt
        if i < len(steps) - 1:
            s.text(px + 6, yy + 8, "→", 20, 700, SOFT)
            px += 34
    check(max(y + 660, yy + 40), "Persona resumen")
    out["P1 · User persona · resumen"] = s

    def persona_cols(n, title, blocks, name):
        s, y = slide(n, "04 · ANALIZAR · USER PERSONA", title)
        y = cards_grid(s, y, blocks, 3, bullets_card, gap=24)
        check(y, name)
        return s

    n += 1
    out["P2 · Quién es y su contexto"] = persona_cols(n, "Daniela: quién es y su contexto", C.PERSONA_BLOQUES_1, "P2")

    n += 1
    s, y = slide(n, "04 · ANALIZAR · USER PERSONA", "Su trayecto de un martes")
    st = C.PERSONA_TRAYECTO
    k = len(st)
    gap = 14
    sw = (CW - gap * (k - 1)) / k
    ch = max(24 + 16 * 1.3 + 8 + text_h(t, 21, 700, sw - 32, 1.2) + 8 + text_h(d, 15, 400, sw - 32, 1.35) + 20 for _, t, d, _, _ in st)
    for i, (hr, t, d, lvl, emo) in enumerate(st):
        x = M + i * (sw + gap)
        s.rect(x, y, sw, ch, YEL if lvl >= 4 else CARD, r=16)
        fg = INK if lvl >= 4 else WHITE
        yy = y + 24
        yy += s.text(x + 16, yy, hr, 16, 700, INK if lvl >= 4 else YEL, mono=True) + 8
        yy += s.text(x + 16, yy, t, 21, 700, fg, maxw=sw - 32, lh=1.2) + 8
        s.text(x + 16, yy, d, 15, 400, fg, maxw=sw - 32, lh=1.35)
    gy = y + ch + 24
    gh = 200
    s.rect(M, gy, CW, gh, CARD, r=16)
    s.text(M + 20, gy + 16, "NIVEL DE TENSIÓN", 14, 700, SOFT, mono=True)
    pts = [(M + i * (sw + gap) + sw / 2, gy + gh - 36 - (e[3] - 1) * (gh - 90) / 3) for i, e in enumerate(st)]
    s.path(pts, YEL, 4)
    for (cx, cy), e in zip(pts, st):
        s.circle(cx, cy, 10, YEL if e[3] >= 4 else WHITE)
        s.text(cx + 16, cy - 28, e[4], 16, 700, WHITE)
    y = gy + gh + 20
    y += s.text(M, y, "→ El momento más expuesto no es el bus: es la espera del alimentador y la caminata final. Ahí actúa Match.", 22, 700, YEL, maxw=CW)
    check(y, "P3")
    out["P3 · Trayecto y tensión"] = s

    n += 1
    out["P4 · Necesidades, comportamiento y frustraciones"] = persona_cols(n, "Lo que necesita, hace y le frustra", C.PERSONA_BLOQUES_2, "P4")
    n += 1
    out["P5 · Motivaciones, miedos y situaciones"] = persona_cols(n, "Motivaciones, miedos y decisiones", C.PERSONA_BLOQUES_3, "P5")

    n += 1
    s, y = slide(n, "04 · ANALIZAR · USER PERSONA", "Escenario y otras personas")
    eh = 26 + 16 * 1.35 + 10 + text_h(C.PERSONA_ESCENARIO, 22, 400, CW - 64, 1.45) + 26
    s.rect(M, y, CW, eh, YEL, r=20)
    s.text(M + 32, y + 26, "ESCENARIO: UN MARTES CON MATCH", 16, 700, INK, mono=True, ls=0.06)
    s.text(M + 32, y + 26 + 16 * 1.35 + 10, C.PERSONA_ESCENARIO, 22, 400, INK, maxw=CW - 64, lh=1.45)
    y += eh + 24

    def sec(s, x, y, w, it, h=None, measure_only=False):
        nm, tag, rol, items, imp = it
        inner = w - 56
        hh = 26 + 15 * 1.35 + 8 + 30 * 1.2 + 14 + sum(text_h("• " + i, 21, 400, inner, 1.4) + 8 for i in items) + 8 + text_h("→ " + imp, 21, 700, inner, 1.4) + 24
        if measure_only:
            return hh
        s.rect(x, y, w, h or hh, CARD, r=20)
        yy = y + 26
        yy += s.text(x + 28, yy, tag, 15, 700, YEL, mono=True, ls=0.05) + 8
        yy += s.text(x + 28, yy, f"{nm} · {rol}", 30, 700, WHITE, lh=1.2) + 14
        for i in items:
            yy += s.text(x + 28, yy, "• " + i, 21, 400, WHITE, maxw=inner, lh=1.4) + 8
        s.text(x + 28, yy + 8, "→ " + imp, 21, 700, YEL, maxw=inner, lh=1.4)
        return hh
    y = cards_grid(s, y, C.PERSONAS_SEC, 2, sec, gap=24)
    check(y, "P6")
    out["P6 · Escenario y personas secundarias"] = s

    # ---------------- Arquitectura: preguntas
    n += 1
    s, y = slide(n, "04 · ANALIZAR · ARQUITECTURA", "Las 4 preguntas de la profe")
    ans = [
        (C.Q1, "Verificación → Círculo cercano · Flujos 07 y 08",
         "Quien no tiene correo institucional pide 2 avales a personas ya verificadas. Quien avala confirma que la conoce en persona, la relación y desde cuándo. "
         "Con 2 avales queda “Verificada por círculo”. Cada persona avala máximo 5 cuentas; si una avalada es suspendida, se revisan sus avales."),
        (C.Q2, "Matches → Personas compatibles · Flujo 13",
         "Foto, nombre con inicial del apellido, insignia e institución o círculo, tramo en común, hora de salida y diferencia, punto de encuentro, "
         "trayectos acompañados y conocidos en común. Nunca el destino final, el apellido ni el celular."),
        (C.Q3, "Perfil → Contactos de confianza · Flujo 21",
         "En Perfil → Contactos de confianza (máximo 3), desde la agenda o a mano, con relación, canal (SMS o WhatsApp) y avisos. El contacto debe aceptar. "
         "Antes de cada trayecto se confirma a quién avisar."),
        (C.Q4, "Match → Detalle del match · Flujo 13",
         "Perfil público ampliado, mapa del tramo compartido (dónde se unen y se separan), punto y hora de encuentro, tiempo juntos, verificación, "
         "reputación, preferencia de compañía y acciones: solicitar, bloquear o reportar."),
    ]

    def qa(s, x, y, w, it, h=None, measure_only=False):
        q, where, a = it
        inner = w - 56
        hh = 28 + text_h(q, 27, 700, inner, 1.25) + 12 + text_h(where, 16, 700, inner, 1.3, mono=True) + 14 + text_h(a, 21, 400, inner, 1.45) + 28
        if measure_only:
            return hh
        s.rect(x, y, w, h or hh, CARD, r=20)
        yy = y + 28
        yy += s.text(x + 28, yy, q, 27, 700, WHITE, maxw=inner, lh=1.25) + 12
        yy += s.text(x + 28, yy, where, 16, 700, YEL, maxw=inner, lh=1.3, mono=True) + 14
        s.text(x + 28, yy, a, 21, 400, WHITE, maxw=inner, lh=1.45)
        return hh
    y = cards_grid(s, y, ans, 2, qa, gap=24)
    check(y, "Preguntas")
    out["A2 · Las 4 preguntas de la profe"] = s
    assert n == TOTAL, n
    return out


if __name__ == "__main__":
    import os
    import sys
    d = sys.argv[1]
    os.makedirs(d, exist_ok=True)
    for name, s in build_all().items():
        fn = os.path.join(d, name.split(" · ")[0] + ".svg")
        s.save(fn)
        print(name, os.path.getsize(fn))
