from svglib import *

W = 3600
M = 120
CW = W - 2 * M


def card(s, x, y, w, title, items, bg=WHITE, stroke=LINE, tcolor=BLUE, size=24, measure_only=False, forced_h=None):
    inner = w - 80
    h = 40 + 18 * 1.35 + 20 + sum(text_h("• " + it, size, 400, inner, 1.45) + 12 for it in items) + 28
    if measure_only:
        return h
    h = forced_h or h
    s.rect(x, y, w, h, bg, stroke=stroke, r=24)
    yy = y + 40
    yy += s.text(x + 40, yy, title, 18, 700, tcolor, mono=True, ls=0.08) + 20
    for it in items:
        yy += s.text(x + 40, yy, "• " + it, size, 400, INK, maxw=inner, lh=1.45) + 12
    return h


def grid(s, y, specs, ncols, gap=40):
    """specs: lista de (titulo, items, bg, stroke, tcolor). Devuelve nueva y."""
    w = (CW - gap * (ncols - 1)) / ncols
    for r in range(0, len(specs), ncols):
        row = specs[r:r + ncols]
        h = max(card(s, 0, 0, w, *sp[:2], measure_only=True) for sp in row)
        for i, sp in enumerate(row):
            t, items, bg, st, tc = sp
            x = M + i * (w + gap)
            s.g(t.capitalize())
            card(s, x, y, w, t, items, bg, st, tc, forced_h=h)
            s.endg()
        y += h + gap
    return y


def build(out):
    s = Svg(W)
    y = M
    y = header(
        s, M, y, CW, "02 · ANALIZAR · USER PERSONA", "User persona",
        "Construido con las 5 entrevistas (3 mujeres y 2 hombres, de 21 a 25 años), el mapa de empatía y los 6 insights. "
        "Lo que viene de la investigación lleva la marca [E]; lo que es supuesto y se valida en la próxima ronda lleva [S].",
        "“El perfil es demasiado general: podría representar a cualquier persona que se desplaza de noche. Necesitamos entender quién es "
        "específicamente, en qué contexto se encuentra, qué necesidades tiene, cómo se comporta y qué situaciones afectan sus decisiones.”",
    )

    # ----- Ficha principal -----
    s.g("Persona principal · Daniela")
    fh = 440
    s.rect(M, y, CW, fh, BLUE, r=32)
    s.circle(M + 190, y + 190, 110, YEL)
    s.text(M + 190, y + 130, "D", 110, 700, INK, center=True)
    s.text(M + 102, y + 330, "PERSONA PRINCIPAL", 18, 700, YEL, mono=True, ls=0.08)
    x2 = M + 380
    yy = y + 70
    yy += s.text(x2, yy, "Daniela Gómez, 22 años", 72, 700, WHITE) + 10
    yy += s.text(x2, yy, "Estudiante de 8.º semestre de Comunicación Social · Vive en Bosa, estudia en Chapinero (Bogotá) · "
                 "Sale de clase a las 9:00 p. m. los martes y jueves · Viaja sola en TransMilenio + alimentador", 28, 400, WHITE, maxw=CW - 460, lh=1.45) + 30
    yy += s.text(x2, yy, "“La app me informa, pero no me protege.” [E]", 44, 700, YEL, maxw=CW - 460) + 10
    s.text(x2, yy, "“Si veo que alguien de la U va para el mismo lado, me quedo hasta tarde estudiando sin pensarlo dos veces.” [S]",
           28, 400, WHITE, maxw=CW - 460, lh=1.45)
    s.endg()
    y += fh + 48

    y = grid(s, y, [
        ("QUIÉN ES", [
            "Mujer, 22 años, estudiante de 8.º semestre [S: carrera y semestre]",
            "Vive con su mamá y su hermano menor en Bosa [S]",
            "Práctica de medio tiempo en las mañanas; clases de 6 a 9 p. m. martes y jueves [S]",
            "No tiene carro ni moto: depende del transporte público [E]",
            "Celular Android de gama media, plan prepago: cuida la batería y los datos [S]",
        ], WHITE, LINE, BLUE),
        ("SU CONTEXTO", [
            "Su trayecto dura cerca de 1 h 40 min e incluye una troncal y un alimentador [S]",
            "El tramo más largo lo hace de pie y con el celular guardado [S]",
            "Espera el alimentador en un paradero con poca luz que se va quedando vacío [E: brief de María José]",
            "En su curso hay gente que sale a la misma hora, pero no sabe quién va hacia el sur [S]",
            "Ya vivió un incidente: la siguieron una cuadra al bajarse [E: “Me persiguieron”]",
        ], WHITE, LINE, BLUE),
        ("TECNOLOGÍA QUE USA", [
            "App oficial del transporte para ver rutas y horarios (como 5 de 5) [E]",
            "Google Maps cuando va a un lugar nuevo (como 2 de 5) [E]",
            "Comparte su ubicación en tiempo real con su mamá (como 2 de 5 que la comparten siempre) [E; el canal, WhatsApp, es S]",
            "Escucha música cuando hay gente; la apaga y guarda el celular cuando se queda sola [E: datos de la espera]",
            "Nivel digital alto: no necesita tutoriales, sí reglas claras de privacidad [S]",
        ], WHITE, LINE, BLUE),
    ], 3)

    # ----- Trayecto (journey) -----
    s.g("Su trayecto de un martes")
    y += 40
    y += s.text(M, y, "SU TRAYECTO DE UN MARTES", 22, 700, BLUE, mono=True, ls=0.08) + 16
    y += s.text(M, y, "Dónde y cuándo se siente más expuesta", 56, 700, INK) + 50
    steps = [
        ("9:00 p. m.", "Sale de clase", "Revisa en la app cuándo pasa la troncal.", 1, "Tranquila"),
        ("9:05 p. m.", "Camina a la estación", "8 minutos por una calle con poca luz. Se quita un audífono.", 3, "Alerta"),
        ("9:15 p. m.", "Troncal de TransMilenio", "40 minutos de pie. Hay gente; guarda el celular en la maleta de adelante.", 2, "Atenta"),
        ("9:55 p. m.", "Llega al portal", "Busca el paradero del alimentador; cada vez hay menos gente.", 3, "Tensa"),
        ("10:00 p. m.", "Espera el alimentador", "De 10 a 20 min sin saber cuánto tarda. Se para cerca de la luz y de otras personas.", 4, "Máxima tensión"),
        ("10:30 p. m.", "Se baja y camina a casa", "6 minutos a pie. Mira hacia atrás varias veces.", 4, "Miedo"),
        ("10:40 p. m.", "Llega a casa", "Le escribe “llegué” a su mamá y apaga la ubicación (cuando se acuerda).", 1, "Alivio"),
    ]
    n = len(steps)
    sw = (CW - (n - 1) * 24) / n
    top = y
    cardh = max(30 + 20 + 12 + text_h(t, 28, 700, sw - 56, 1.2) + 12 + text_h(d, 21, 400, sw - 56, 1.4) for _, t, d, _, _ in steps) + 30
    for i, (h, t, d, lvl, emo) in enumerate(steps):
        x = M + i * (sw + 24)
        hot = lvl >= 4
        s.rect(x, top, sw, cardh, LYEL if hot else WHITE, stroke=YEL if hot else LINE, r=20)
        yy = top + 30
        yy += s.text(x + 28, yy, h, 20, 700, BLUE, mono=True) + 12
        yy += s.text(x + 28, yy, t, 28, 700, INK, maxw=sw - 56, lh=1.2) + 12
        s.text(x + 28, yy, d, 21, 400, MUTE, maxw=sw - 56, lh=1.4)
    # curva de tensión
    gy = top + cardh + 40
    gh = 220
    s.rect(M, gy, CW, gh, BG, r=20)
    s.text(M + 24, gy + 18, "NIVEL DE TENSIÓN", 16, 700, MUTE, mono=True, ls=0.08)
    pts = []
    for i, st in enumerate(steps):
        cx = M + i * (sw + 24) + sw / 2
        cy = gy + gh - 40 - (st[3] - 1) * (gh - 100) / 3
        pts.append((cx, cy))
    s.path(pts, BLUE, 5)
    for (cx, cy), st in zip(pts, steps):
        s.circle(cx, cy, 14, YEL if st[3] >= 4 else BLUE, stroke=WHITE, sw=4)
        s.text(cx + 22, cy - 34, st[4], 20, 700, INK)
    s.endg()
    y = gy + gh + 30
    y += s.text(M, y, "→ El momento más expuesto no es el bus: es la espera del alimentador y la caminata final. Ahí es donde Match tiene que actuar.",
                26, 700, BLUE, maxw=CW) + 70

    # ----- Necesidades, comportamientos, etc. -----
    y = grid(s, y, [
        ("NECESIDADES", [
            "Funcional: saber quién de su universidad hace su mismo tramo a la misma hora [E: insight 03]",
            "Funcional: que su mamá sepa que llegó sin tener que escribirle [E: insight 04]",
            "Emocional: no sentirse sola en la espera del alimentador [E]",
            "Seguridad: que la otra persona esté verificada y, si lo prefiere, sea mujer [E: insight 05]",
            "Privacidad: que nadie sepa su dirección ni su rutina completa [S]",
        ], LBLUE, None, BLUE),
        ("CÓMO SE COMPORTA", [
            "Revisa la app oficial antes de salir, aunque eso no le quita el miedo [E: 5 de 5]",
            "Elige dónde esperar por la luz, la cercanía y la gente, no por una app [E: 0 de 5 usa una app]",
            "Guarda el celular y se queda en alerta cuando el paradero se vacía [E]",
            "Comparte la ubicación por WhatsApp; a veces se le olvida apagarla [E/S]",
            "Pregunta en el grupo del curso “¿alguien va para el sur?”, pero casi nunca coincide [S]",
        ], WHITE, LINE, BLUE),
        ("FRUSTRACIONES", [
            "La app le da horarios, no tranquilidad [E]",
            "Pedir un carro todas las noches no le alcanza [S]",
            "Compartir la ubicación es manual y queda activa más tiempo del necesario [E/S]",
            "No confía en desconocidos: “acompañante” no puede ser cualquiera [E: idea descartada]",
            "Los grupos de WhatsApp no sirven para coordinar a última hora [S]",
        ], LRED, None, RED),
        ("MOTIVACIONES", [
            "No sentirse sola en el momento más expuesto [E]",
            "Terminar la carrera sin evitar las materias de la noche [S]",
            "Autonomía: no depender de que alguien la recoja [S]",
            "Tranquilizar a su mamá [E: la mayoría le avisa a alguien]",
        ], LGREEN, None, GREEN),
        ("MIEDOS", [
            "Violencia sexual (lo mencionaron las 3 mujeres) [E]",
            "Robo y agresión (lo mencionaron las 5 personas) [E]",
            "Que la sigan al bajarse del bus [E: “Me persiguieron”]",
            "Que una app exponga su ubicación a quien no debe [S: planteado en la retro]",
        ], LYEL, None, BROWN),
        ("SITUACIONES QUE CAMBIAN SUS DECISIONES", [
            "Después de las 10 p. m. ya no espera el alimentador: pide un carro o se queda donde una amiga [E: 4 de 5 cambiaron de plan]",
            "Si llueve, el paradero se vacía y la espera se siente más larga [S]",
            "Con menos del 20 % de batería deja de compartir la ubicación [S]",
            "Si va con alguien conocido, se queda hasta tarde sin problema [S]",
            "En semana de parciales sale más tarde de la biblioteca [S]",
            "A final de mes decide si le alcanza para un carro [S]",
        ], WHITE, LINE, BLUE),
    ], 3)

    # ----- Escenario -----
    s.g("Escenario con Match")
    y += 40
    sc = ("Martes, 8:40 p. m. Daniela abre Match: hay 2 personas de su universidad que salen entre las 9:00 y las 9:15 hacia el Portal. "
          "Revisa a Laura (verificada con correo institucional, 14 trayectos acompañados, comparten 2 de 3 tramos) y le envía una solicitud. "
          "Laura acepta. Se encuentran en la entrada de la estación y confirman el código “Naranja-12”. Su mamá recibe un enlace por WhatsApp "
          "y ve el trayecto sin instalar nada. En el portal, Laura espera con ella hasta que llega el alimentador. A las 10:38 Daniela llega: "
          "la ubicación se apaga sola y su mamá recibe “Daniela llegó”.")
    inner = CW - 160
    h = 70 + 22 * 1.35 + 20 + text_h(sc, 30, 400, inner, 1.5) + 70
    s.rect(M, y, CW, h, INK, r=32)
    yy = y + 70
    yy += s.text(M + 80, yy, "ESCENARIO: UN MARTES CON MATCH", 22, 700, YEL, mono=True, ls=0.08) + 20
    s.text(M + 80, yy, sc, 30, 400, WHITE, maxw=inner, lh=1.5)
    s.endg()
    y += h + 90

    # ----- Personas secundarias -----
    y += s.text(M, y, "OTRAS PERSONAS QUE AFECTAN EL PRODUCTO", 22, 700, BLUE, mono=True, ls=0.08) + 16
    y += s.text(M, y, "Persona secundaria y segmento complementario", 56, 700, INK) + 40
    colw = (CW - 40) / 2
    sec = [
        ("Gloria, 49 · mamá de Daniela", "PERSONA SECUNDARIA · CONTACTO AVISADO", [
            "Quién es: trabaja de día y espera despierta a que Daniela llegue [S]",
            "Qué hace hoy: si son las 10:30 y no sabe nada, la llama; Daniela no contesta porque guardó el celular [S]",
            "Necesita: saber que llegó, con quién va y si algo cambió, sin tener que llamar [E: usuario secundario validado]",
            "No quiere: instalar otra app ni aprender a usarla [S]",
            "→ Implicación: los avisos llegan por SMS o WhatsApp con un enlace web; no necesita la app.",
        ]),
        ("Daniel, 21 · estudiante", "SEGMENTO COMPLEMENTARIO · HOMBRES", [
            "Quién es: estudiante que sale de noche del trabajo o de la universidad [E]",
            "Su miedo principal: el robo, no la violencia sexual [E: los 2 hombres]",
            "Qué hace hoy: va en alerta, no saca el celular y a veces cambia de ruta [E]",
            "Necesita: no ir solo en los tramos de riesgo y poder ayudar a alguien de su comunidad [S]",
            "→ Implicación: la preferencia de género es opcional; él puede acompañar a cualquier persona que lo acepte.",
        ]),
    ]
    hs = []
    for t, tag, items in sec:
        hs.append(40 + 18 * 1.35 + 12 + 40 * 1.35 + 24 + sum(text_h(it, 24, 400, colw - 80, 1.45) + 12 for it in items) + 30)
    ch = max(hs)
    for i, (t, tag, items) in enumerate(sec):
        x = M + i * (colw + 40)
        s.g(t)
        s.rect(x, y, colw, ch, WHITE, stroke=BLUE, sw=3, r=24)
        yy = y + 40
        yy += s.text(x + 40, yy, tag, 18, 700, BLUE, mono=True, ls=0.08) + 12
        yy += s.text(x + 40, yy, t, 40, 700, INK) + 24
        for it in items:
            imp = it.startswith("→")
            yy += s.text(x + 40, yy, it if imp else "• " + it, 24, 700 if imp else 400, BLUE if imp else INK, maxw=colw - 80, lh=1.45) + 12
        s.endg()
    y += ch + M
    s.save(out, y)


if __name__ == "__main__":
    import sys
    build(sys.argv[1])
