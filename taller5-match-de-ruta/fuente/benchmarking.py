from svglib import *

W = 3600
M = 120
CW = W - 2 * M


def build(out):
    s = Svg(W)
    y = M
    y = header(
        s, M, y, CW, "01 · ANALIZAR · BENCHMARKING", "Benchmarking",
        "Comparé 6 soluciones que hoy resuelven una parte del problema: informar sobre el transporte, transportar, vigilar la ubicación "
        "o reaccionar ante una emergencia. Las evalué en 19 funcionalidades agrupadas en 6 categorías para encontrar qué patrones ya "
        "están probados, qué conviene evitar y dónde queda el espacio libre para Match de ruta verificado.",
        "“No es solo el cuadro comparativo: debe incluir la conclusión del ejercicio, con los hallazgos y cómo sustentan la propuesta de "
        "valor y la diferenciación frente a otras soluciones. El cuadro está muy limitado: apenas mencionas cuatro funcionalidades.”",
    )

    # ---------- Tabla ----------
    featW, colW = 640, (CW - 640) / 7
    cols = [("Moovit", "Informa sobre el transporte"), ("Google Maps", "Ubica y guía"), ("Uber", "Transporta (con pago)"),
            ("Life360", "Vigila a la familia"), ("bSafe", "Reacciona ante emergencias"),
            ("Waze Carpool", "Carro compartido · cerró en 2022"), ("Match de ruta", "Acompaña el trayecto")]
    ST = {"S": ("Sí", LGREEN, GREEN), "P": ("Parcial", LYEL, BROWN), "N": ("No", LGRAY, MUTE), "V": ("Por verificar", WHITE, MUTE)}
    data = [
        ("G", "MOVILIDAD"),
        ("Planear ruta en transporte público", "Combina buses, troncales y caminatas",
         ["S", "S", "P|Solo en algunas ciudades*", "N", "N", "N|Ruta en carro", "N|Usa la ruta que la persona ya conoce"]),
        ("Tiempos de llegada en tiempo real", "Cuándo llega el bus o el alimentador",
         ["S", "P|Depende de los datos de cada ciudad", "N", "N", "N", "N", "P|Capa secundaria (Could)"]),
        ("Alertas de servicio", "Desvíos, cierres o retrasos de las líneas",
         ["S", "P|Según la ciudad", "N", "N", "N", "N", "N"]),
        ("G", "UBICACIÓN Y AVISOS"),
        ("Compartir ubicación en vivo", "Otra persona ve dónde estás",
         ["V*", "S|Con contactos de Google", "S|Solo durante el viaje", "S|Permanente dentro del círculo", "S|Función “Follow me”*", "V*", "S|Solo durante el trayecto"]),
        ("Ubicación temporal que se apaga sola", "El permiso caduca sin que tengas que hacer nada",
         ["V*", "S|Eliges la duración", "S|Termina con el viaje", "N|Activa todo el tiempo", "P|Se activa y se apaga a mano*", "V*", "S|Se apaga al llegar"]),
        ("Aviso de llegada a contactos", "Alguien sabe que llegaste sin tener que preguntar",
         ["N", "P|Compartir el progreso del viaje en navegación", "P|El contacto ve que el viaje terminó", "S|Alertas al llegar a un lugar", "P|Alarma con temporizador*", "N", "S|Aviso automático al llegar"]),
        ("Sin historial de ubicaciones", "No queda registro de por dónde te mueves",
         ["V*", "P|Cronología opcional", "N|Guarda el historial de viajes", "N|Guarda historial (según plan)", "V*", "V*", "S|Se borra al terminar"]),
        ("G", "SEGURIDAD Y RESPUESTA"),
        ("Botón SOS / emergencia", "Pedir ayuda en un momento crítico",
         ["N", "N", "S|Botón de emergencia durante el viaje", "P|SOS según plan", "S|SOS a guardianes", "N", "P|Atajo a la línea 123 (propuesta)"]),
        ("Grabar o transmitir evidencia", "Audio o video como respaldo",
         ["N", "N", "P|Grabación de audio en algunos mercados*", "N", "S|Video y audio en vivo", "N", "N|Fuera del alcance del MVP"]),
        ("Llamada falsa", "Excusa para salir de una situación incómoda",
         ["N", "N", "N", "N", "S", "N", "N"]),
        ("G", "IDENTIDAD Y CONFIANZA"),
        ("Identidad verificada de la otra persona", "Sabes quién es antes de encontrarte",
         ["N|No aplica", "N|Compartes con tus contactos", "S|Conductor verificado por Uber", "P|Gente conocida, sin verificación", "P|Gente conocida, sin verificación", "P|Correo laboral opcional*", "S|Correo institucional o avales del círculo"]),
        ("Verificación por institución", "Universidad o empresa como filtro de confianza",
         ["N", "N", "N", "N", "N", "S|Filtro por empresa o universidad*", "S|Correo institucional"]),
        ("Red de confianza elegida", "Contactos que tú escoges",
         ["N", "S|Contactos", "S|Contactos de confianza", "S|Círculos", "S|Guardianes", "N", "S|Círculo cercano + contactos avisados"]),
        ("Calificación o reporte de personas", "Consecuencias por mal comportamiento",
         ["N", "N", "S|Calificación mutua", "N", "N", "S|Calificación*", "S|Confirmación mutua + reporte"]),
        ("Preferencia de género", "Elegir con quién te emparejan",
         ["N", "N", "P|Solo en algunos países*", "N", "N", "S|Mismo género*", "S|Solo mujeres / cualquiera"]),
        ("G", "ACOMPAÑAMIENTO"),
        ("Emparejamiento por ruta y horario", "Conecta personas que van hacia el mismo lado",
         ["N", "N", "P|UberX Share: desconocidos, en carro*", "N", "N", "S|En carro: conductor + pasajero", "S|En transporte público"]),
        ("Compañía física en la espera y el trayecto", "Alguien real a tu lado en el paradero",
         ["N", "N", "N|Te saca del transporte público", "N", "P|Acompañamiento virtual", "N", "S|Persona verificada a tu lado"]),
        ("Chat entre usuarios", "Coordinar el encuentro",
         ["N", "N", "S|Con el conductor", "V*", "N", "S|Conductor y pasajero*", "S|Solo tras confirmación mutua"]),
        ("G", "MODELO"),
        ("Costo para quien la usa", "",
         ["T|Gratis + Moovit+ de pago", "T|Gratis", "T|Pago por viaje", "T|Gratis + planes de pago", "T|Gratis + premium*", "T|Costo compartido por viaje", "T|Gratis (propuesta)"]),
    ]

    s.g("Tabla comparativa")
    tx, ty = M, y
    # cabecera
    hh = 150
    s.rect(tx, ty, CW, hh, INK, r=0)
    s.text(tx + 28, ty + 32, "FUNCIONALIDAD", 20, 700, WHITE, mono=True, ls=0.06)
    for i, (n, d) in enumerate(cols):
        cx = tx + featW + i * colW
        if i == 6:
            s.rect(cx, ty, colW, hh, BLUE)
        s.text(cx + 22, ty + 28, n, 30, 700, YEL if i == 6 else WHITE)
        s.text(cx + 22, ty + 74, d, 19, 400, WHITE, maxw=colW - 44, lh=1.3)
    ty += hh
    nfeat = 0
    for d in data:
        if d[0] == "G":
            s.rect(tx, ty, CW, 58, LGRAY)
            s.text(tx + 28, ty + 18, d[1], 18, 700, BLUE, mono=True, ls=0.1)
            ty += 58
            continue
        nfeat += 1
        # alto de la fila
        h = 24 + text_h(d[0], 24, 700, featW - 56, 1.25) + (6 + text_h(d[1], 18, 400, featW - 56, 1.3) if d[1] else 0) + 24
        for c in d[2]:
            k, _, note = c.partition("|")
            ch = 24 + (0 if k == "T" else 34 + (8 if note else 0)) + (text_h(note, 18 if k != "T" else 20, 400, colW - 40, 1.3) if note else 0) + 24
            h = max(h, ch)
        s.rect(tx + featW + 6 * colW, ty, colW, h, LBLUE)
        yy = ty + 24
        yy += s.text(tx + 28, yy, d[0], 24, 700, INK, maxw=featW - 56, lh=1.25)
        if d[1]:
            s.text(tx + 28, yy + 6, d[1], 18, 400, MUTE, maxw=featW - 56, lh=1.3)
        for i, c in enumerate(d[2]):
            k, _, note = c.partition("|")
            cx = tx + featW + i * colW + 20
            cy = ty + 24
            if k == "T":
                s.text(cx, cy, note, 20, 500, INK, maxw=colW - 40, lh=1.3)
                continue
            star = k.endswith("*")
            k = k.rstrip("*")
            lab, bg, fg = ST[k]
            lab = lab + (" *" if star else "")
            cw = measure(lab, 17, 700, True) + 32
            s.rect(cx, cy, cw, 34, bg, stroke=LINE if k == "V" else None, dash="6 4" if k == "V" else None, r=17)
            s.text(cx + 16, cy + 7, lab, 17, 700, fg, mono=True)
            if note:
                s.text(cx, cy + 42, note, 18, 400, INK, maxw=colW - 40, lh=1.3)
        s.path([(tx, ty + h), (tx + CW, ty + h)], LINE, 1.5)
        ty += h
    s.rect(tx, y, CW, ty - y, "none", stroke=LINE, sw=2, r=0)
    s.endg()
    y = ty + 28
    s.g("Leyenda")
    y += s.text(M, y, "Sí = la plataforma lo ofrece · Parcial = existe con límites (por país, plan o forma de uso) · No = no lo ofrece · "
                "Por verificar = no encontré evidencia suficiente para afirmarlo.", 20, 400, MUTE, maxw=CW, lh=1.4) + 6
    y += s.text(M, y, "* Dato para confirmar en la app o en su página oficial antes de la entrega: la disponibilidad cambia según el país, "
                "el plan de pago y las actualizaciones. Waze Carpool se incluye como antecedente: Google cerró el servicio en 2022.",
                20, 400, MUTE, maxw=CW, lh=1.4)
    s.endg()
    y += 110

    # ---------- Conclusión ----------
    s.g("Conclusión del benchmarking")
    y += s.text(M, y, "CONCLUSIÓN DEL EJERCICIO", 22, 700, BLUE, mono=True, ls=0.08) + 20
    y += s.text(M, y, "6 hallazgos y lo que significan para Match", 64, 700, INK) + 48
    hall = [
        ("El mercado se divide en informar, transportar y reaccionar.",
         "Moovit y Google Maps informan; Uber y Waze Carpool transportan; Life360 y bSafe vigilan o reaccionan. Ninguna acompaña a quien ya va en transporte público.",
         "Match no compite en tiempos ni en transporte: ocupa el espacio de la compañía."),
        ("Compartir ubicación ya es un estándar, no un diferencial.",
         "Cinco de las seis plataformas lo ofrecen de alguna forma.",
         "Para Match es un requisito básico. El diferencial está en cómo se comparte: solo durante el trayecto, se apaga sola y sin historial."),
        ("La confianza se construye de dos maneras y ninguna app las combina.",
         "Life360 y bSafe confían en gente que ya conoces, sin verificar identidad. Uber verifica a sus conductores, pero no a tu red.",
         "Match une las dos: correo institucional y avales del círculo cercano."),
        ("El emparejamiento por ruta ya existe, pero en carro.",
         "UberX Share empareja desconocidos que pagan. Waze Carpool usaba empresa, universidad y género como filtros, y Google lo cerró en 2022.",
         "Los filtros por institución y género ya se usaron en otros servicios. El riesgo que hay que cuidar es la masa crítica: sin personas en la misma ruta y hora, no hay match."),
        ("Las apps de seguridad actúan cuando el riesgo ya ocurrió.",
         "El SOS, la grabación y la llamada falsa (bSafe, Uber) son respuestas a un incidente.",
         "Match es preventivo: baja la exposición antes de que algo pase (insight 03: buscan dejar de estar solos). No duplica el SOS; ofrece un atajo a la línea 123."),
        ("Nadie diseña para la espera en el paradero.",
         "Ninguna función cubre el momento más expuesto: esperar el alimentador de noche.",
         "La espera acompañada es el centro del producto, no un extra."),
    ]
    cardW = (CW - 2 * 40) / 3
    rows = [hall[0:3], hall[3:6]]
    for ri, rowc in enumerate(rows):
        hs = []
        for t, ev, imp in rowc:
            inner = cardW - 80
            hs.append(40 + 40 + 16 + text_h(t, 32, 700, inner, 1.2) + 18 + text_h(ev, 22, 400, inner, 1.45) + 28 + 30 + text_h(imp, 22, 500, inner - 40, 1.45) + 30 + 40)
        ch = max(hs)
        for ci, (t, ev, imp) in enumerate(rowc):
            n = ri * 3 + ci + 1
            cx = M + ci * (cardW + 40)
            inner = cardW - 80
            s.g(f"Hallazgo {n}")
            s.rect(cx, y, cardW, ch, WHITE, stroke=LINE, sw=2, r=24)
            yy = y + 40
            s.circle(cx + 60, yy + 20, 20, BLUE)
            s.text(cx + 60, yy + 7, str(n), 22, 700, WHITE, mono=True, center=True)
            yy += 40 + 16
            yy += s.text(cx + 40, yy, t, 32, 700, INK, maxw=inner, lh=1.2) + 18
            yy += s.text(cx + 40, yy, ev, 22, 400, MUTE, maxw=inner, lh=1.45) + 28
            ih = 30 + text_h(imp, 22, 500, inner - 40, 1.45) + 30
            s.rect(cx + 40, yy, inner, ih, LBLUE, r=16)
            s.text(cx + 60, yy + 30, "→ " + imp, 22, 500, INK, maxw=inner - 40, lh=1.45)
            s.endg()
        y += ch + 40
    s.endg()
    y += 60

    # Propuesta de valor
    s.g("Propuesta de valor")
    pv = ("Para estudiantes y trabajadores que dependen del transporte público de noche, Match de ruta verificado los conecta con personas "
          "verificadas de su universidad, su trabajo o su círculo cercano que hacen el mismo trayecto a la misma hora, para que no esperen "
          "ni viajen solos.")
    pv2 = ("A diferencia de Life360 o bSafe, no vigila ni reacciona: acompaña. A diferencia de Uber, no saca a la persona del transporte "
           "público ni le cobra. Y a diferencia de Waze Carpool, empareja por tramos de transporte público, no por viajes en carro.")
    inner = CW - 160
    ph = 70 + 24 + 20 + text_h(pv, 44, 700, inner, 1.3) + 30 + text_h(pv2, 28, 400, inner, 1.45) + 70
    s.rect(M, y, CW, ph, BLUE, r=32)
    yy = y + 70
    yy += s.text(M + 80, yy, "PROPUESTA DE VALOR", 22, 700, YEL, mono=True, ls=0.08) + 20
    yy += s.text(M + 80, yy, pv, 44, 700, WHITE, maxw=inner, lh=1.3) + 30
    s.text(M + 80, yy, pv2, 28, 400, WHITE, maxw=inner, lh=1.45)
    s.endg()
    y += ph + 80

    # Diferenciación
    s.g("Diferenciación")
    y += s.text(M, y, "Diferenciación: qué tomo, qué evito y qué solo hace Match", 48, 700, INK) + 36
    dif = [
        ("TOMO (patrones ya probados)", LGREEN, GREEN, [
            "Círculos de confianza → Life360",
            "Compartir un viaje que termina solo → Uber y Google Maps",
            "Calificación y reporte entre personas → Uber",
            "Filtros por institución y por género → Waze Carpool",
            "Tiempos de llegada como capa secundaria → Moovit",
        ]),
        ("EVITO (lo que genera desconfianza)", LRED, RED, [
            "Ubicación permanente e historial de movimientos (Life360)",
            "Emparejar a desconocidos (UberX Share)",
            "Cobrar por sentirse seguro (Uber)",
            "Actuar solo cuando ya pasó algo (bSafe)",
        ]),
        ("SOLO HACE MATCH", LBLUE, BLUE, [
            "Emparejar por tramo de transporte público y horario",
            "Verificación doble: institución + avales del círculo",
            "Acompañar la espera en el paradero",
            "Ubicación que se apaga sola, sin historial",
            "Aviso al contacto sin que tenga que instalar la app",
        ]),
    ]
    colw = (CW - 80) / 3
    hs = []
    for t, bg, fg, items in dif:
        hs.append(40 + 30 + 24 + sum(text_h("• " + it, 24, 400, colw - 80, 1.4) + 14 for it in items) + 30)
    ch = max(hs)
    for i, (t, bg, fg, items) in enumerate(dif):
        cx = M + i * (colw + 40)
        s.rect(cx, y, colw, ch, bg, r=24)
        yy = y + 40
        yy += s.text(cx + 40, yy, t, 20, 700, fg, mono=True, ls=0.06) + 24
        for it in items:
            yy += s.text(cx + 40, yy, "• " + it, 24, 400, INK, maxw=colw - 80, lh=1.4) + 14
    s.endg()
    y += ch + 80

    # Riesgos
    s.g("Riesgos que revela el benchmarking")
    y += s.text(M, y, "Riesgos que revela el benchmarking y cómo los abordo", 48, 700, INK) + 36
    rk = [
        ("Masa crítica", "Si no hay personas en la misma ruta y hora, la app no sirve.",
         "Lanzar por institución (una universidad piloto), emparejar por tramo y no por ruta completa, y usar un rango horario de ±15 min."),
        ("Suplantación", "Alguien se hace pasar por otra persona en el encuentro.",
         "Foto tomada en el momento, código de encuentro de dos palabras y reporte con bloqueo inmediato."),
        ("Exponer la rutina", "Que otra persona sepa a qué hora sale y dónde vive.",
         "No mostrar el destino exacto, el apellido ni el celular; solo el tramo en común. El perfil solo lo ven personas compatibles."),
    ]
    hs = [40 + text_h(a, 30, 700, colw - 80) + 14 + text_h(b, 22, 400, colw - 80, 1.45) + 24 + text_h("→ " + c, 22, 500, colw - 80, 1.45) + 40 for a, b, c in rk]
    ch = max(hs)
    for i, (a, b, c) in enumerate(rk):
        cx = M + i * (colw + 40)
        s.rect(cx, y, colw, ch, WHITE, stroke=LINE, r=24)
        yy = y + 40
        yy += s.text(cx + 40, yy, a, 30, 700, INK, maxw=colw - 80) + 14
        yy += s.text(cx + 40, yy, b, 22, 400, MUTE, maxw=colw - 80, lh=1.45) + 24
        s.text(cx + 40, yy, "→ " + c, 22, 500, BLUE, maxw=colw - 80, lh=1.45)
    s.endg()
    y += ch + M
    s.save(out, y)
    return nfeat


if __name__ == "__main__":
    import sys
    print(build(sys.argv[1]))
