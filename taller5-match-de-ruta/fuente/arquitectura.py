from svglib import *

W = 5800
M = 120
CW = W - 2 * M

Q1 = "¿Cómo funciona la verificación a través del círculo cercano?"
Q2 = "¿Qué información me muestra la plataforma cuando reviso los posibles perfiles?"
Q3 = "¿Dónde agrego los contactos que serán avisados?"
Q4 = "¿Qué información contiene el detalle de un match?"

COLS = [
    ("0", "Acceso y bienvenida", "Primera vez", [
        ("Bienvenida (3 pantallas)", ["Qué es Match de ruta", "Cómo se verifica a las personas", "Qué pasa con tu ubicación"], None),
        ("Crear cuenta", ["Celular + código por SMS", "Nombre y apellido", "Fecha de nacimiento (solo mayores de 18)", "Género (para la preferencia de match)"], None),
        ("Permisos", ["Ubicación: solo mientras la app está en uso", "Notificaciones"], None),
        ("Términos y datos personales", ["Política de tratamiento de datos (Ley 1581 de 2012)", "Aceptar y continuar"], None),
        ("Iniciar sesión / recuperar cuenta", ["Celular + código"], None),
    ]),
    ("1", "Verificación", "Antes de hacer match", [
        ("Elegir método", ["Correo institucional", "Círculo cercano (si no tiene correo)"], None),
        ("Correo institucional", ["Buscar universidad o empresa", "Escribir correo @institución", "Código de 6 dígitos al correo", "Foto de perfil tomada en el momento (no de galería)", "Insignia: “Verificada · Universidad X”"], None),
        ("Círculo cercano (avales)", ["Pedir 2 avales a personas ya verificadas", "Enviar la solicitud por la app o por enlace", "Quien avala confirma: “La conozco en persona”", "Relación: familia, amistad, trabajo o barrio", "Tiempo de conocerse", "Con 2 avales: “Verificada por círculo”", "Reglas: máx. 5 avales por persona; si una cuenta avalada es suspendida, se revisan sus avales"], Q1),
        ("Estado de la cuenta", ["Sin verificar: solo configura rutas", "Pendiente (1 de 2 avales)", "Verificada", "En revisión / suspendida"], None),
        ("Mis círculos", ["Universidad", "Trabajo", "Barrio o amigos"], None),
    ]),
    ("2", "Perfil", "Pestaña de la barra", [
        ("Perfil público (lo ven tus matches)", ["Foto", "Nombre + inicial del apellido", "Insignia y método de verificación", "Institución o círculo", "Trayectos acompañados", "Confirmaciones recibidas / sin reportes"], None),
        ("Datos privados (nadie más los ve)", ["Celular", "Fecha de nacimiento", "No se pide dirección: solo paraderos"], None),
        ("Preferencias de match", ["Género: solo mujeres / cualquiera", "Alcance: mi institución / mi círculo / ambos", "Compañía: solo la espera / espera + trayecto"], None),
        ("Contactos de confianza", ["Agregar desde la agenda o a mano (máx. 3)", "Nombre, celular y relación", "Canal del aviso: SMS o WhatsApp", "Avisos: inicio, separación, llegada y retraso", "El contacto acepta recibir avisos", "Contacto predeterminado"], Q3),
        ("Privacidad", ["Ocultar destino exacto (activado por defecto)", "Personas bloqueadas", "Descargar mis datos", "Eliminar cuenta"], None),
        ("Ajustes", ["Notificaciones", "Ahorro de batería", "Ayuda y cómo funciona", "Cerrar sesión"], None),
    ]),
    ("3", "Mis rutas", "Pestaña de la barra", [
        ("Rutas guardadas", ["Nombre de la ruta", "Días y hora", "Estado: activa / pausada", "Personas compatibles hoy"], None),
        ("Crear / editar ruta", ["Punto de partida: estación o paradero", "Tramos: medio (troncal, alimentador, SITP, intermunicipal), estación de subida y de bajada", "Destino: paradero final, no dirección", "Hora de salida + rango (±15 min)", "Días de la semana", "Nombre de la ruta"], None),
        ("Trayecto de una sola vez", ["Fuera de la rutina: hoy, a una hora"], None),
        ("Pausar / eliminar ruta", [], None),
    ]),
    ("4", "Inicio (hoy)", "Pestaña de la barra", [
        ("Próximo trayecto", ["Ruta y hora", "Estado del match: sin match / pendiente / confirmado"], None),
        ("Personas disponibles hoy", ["Resumen: “2 personas de tu U salen a tu hora”"], None),
        ("Solicitudes pendientes", ["Recibidas y enviadas"], None),
        ("Botón “Iniciar trayecto”", [], None),
        ("Tiempos de llegada", ["Capa secundaria: cuándo llega el bus o el alimentador"], None),
    ]),
    ("5", "Matches", "Pestaña de la barra", [
        ("Personas compatibles (lista)", ["Foto", "Nombre + inicial del apellido", "Insignia + institución o círculo", "Tramo en común (ej. “Calle 45 → Portal Sur, 2 de 3 tramos”)", "Hora de salida y diferencia (“9:05 · 5 min después”)", "Punto de encuentro sugerido", "Trayectos acompañados", "Conocidos en común", "NO muestra: destino final, apellido ni celular"], Q2),
        ("Filtros y orden", ["Hora", "Solo mujeres", "Solo mi institución", "Más tramos en común"], None),
        ("Detalle del match", ["Perfil público ampliado", "Mapa del tramo compartido: dónde se unen y dónde se separan", "Punto y hora de encuentro", "Tiempo estimado juntos", "Verificación: método y fecha", "Reputación: trayectos, confirmaciones, sin reportes", "Preferencia de compañía (espera / trayecto)", "Acciones: enviar solicitud, bloquear, reportar"], Q4),
        ("Solicitudes", ["Enviadas / recibidas", "Aceptar o rechazar", "Vencen cuando empieza el horario"], None),
        ("Confirmación mutua", ["Ambos aceptan → se habilitan el chat y el punto de encuentro"], None),
        ("Sin matches", ["Ampliar el rango horario", "Avisarme cuando aparezca alguien", "Invitar a alguien de mi círculo"], None),
        ("Compañía frecuente", ["Con quién ya viajaste (solo nombre y fecha)"], None),
    ]),
    ("6", "Chat breve", "Dentro de un match", [
        ("Disponible solo tras la confirmación mutua", [], None),
        ("Mensajes rápidos", ["“Ya llegué al punto”", "“Voy 5 min tarde”", "“Estoy en la puerta 2”", "“Cancelo”"], None),
        ("Texto libre", ["Sin fotos ni archivos"], None),
        ("Código de encuentro", ["Dos palabras para confirmar en persona (ej. “Naranja-12”)"], None),
        ("Borrado y seguridad", ["Se borra 24 h después del trayecto", "Reportar desde el chat"], None),
    ]),
    ("7", "Trayecto activo", "Banner fijo mientras dura", [
        ("Antes de salir", ["Confirmar la compañía", "Elegir a qué contactos avisar", "Revisar el punto de encuentro"], Q3),
        ("Encuentro", ["“Ya llegué” (cada persona)", "Confirmar el código", "Si no llega en 10 min: esperar 5 más, buscar a otra persona o seguir solo con aviso"], None),
        ("En curso", ["Mapa con ambas personas (solo durante el trayecto)", "Tramo actual y siguiente", "Tiempo de llegada (capa secundaria)", "“Tu mamá está viendo tu trayecto”", "Botón “Dejar de compartir”", "Botón “¿Algo no está bien?”: llamar al 123, avisar a mis contactos, reportar"], None),
        ("Separación", ["Si la compañía se baja antes: aviso a ti y al contacto"], None),
        ("Llegada", ["Detecta el paradero final o botón “Llegué”", "La ubicación se apaga sola", "Aviso al contacto"], None),
        ("Retraso", ["15 min tarde: “¿Todo bien?”", "Sin respuesta en 5 min: aviso al contacto con la última ubicación"], None),
    ]),
    ("8", "Confianza", "Después del trayecto", [
        ("Confirmación mutua", ["¿Se encontraron? Sí / No", "Suma un trayecto acompañado a ambos perfiles"], None),
        ("¿Volverías a viajar con esta persona?", ["Respuesta privada, sin estrellas públicas"], None),
        ("Reportar conducta", ["Motivo: no se presentó, actitud inapropiada, acoso, suplantación, otro", "Descripción (opcional)", "Bloqueo inmediato", "Revisión por moderación", "Advertencia o suspensión"], None),
        ("Sin historial", ["Se guarda: fecha, persona y confirmación", "Se borra: ubicaciones (al llegar) y chat (a las 24 h)"], None),
    ]),
    ("9", "Vista del contacto", "Web, sin instalar la app", [
        ("Invitación", ["SMS o WhatsApp: “Daniela te agregó como contacto de confianza”", "Aceptar o rechazar avisos"], None),
        ("Enlace del trayecto", ["Con quién va: foto, nombre y verificación", "Mapa en vivo", "Hora estimada de llegada"], None),
        ("Avisos que recibe", ["Inicio", "Separación de la compañía", "Llegada", "Retraso sin respuesta"], None),
        ("Caducidad", ["El enlace deja de funcionar al llegar"], None),
    ]),
]


def build(out):
    s = Svg(W)
    y = M
    y = header(
        s, M, y, CW, "03 · ANALIZAR · ARQUITECTURA DE LA INFORMACIÓN", "Arquitectura de la información",
        "Qué contiene la plataforma y cómo se organiza: 10 secciones, cada una con sus pantallas y lo que muestra cada una. "
        "La barra inferior tiene 4 pestañas (Inicio · Mis rutas · Matches · Perfil); el trayecto activo aparece como banner fijo y el contacto "
        "avisado ve una página web sin instalar la app. Las cajas amarillas responden las preguntas de la profe.",
        "“La arquitectura necesita mayor profundidad. ¿Cómo funciona la verificación a través del círculo cercano? ¿Qué información me muestra "
        "la plataforma cuando reviso los posibles perfiles durante el recorrido? ¿Dónde agrego los contactos que serán avisados? ¿Qué información "
        "contiene el detalle de un match? La arquitectura debería permitirnos responder este tipo de preguntas.”",
    )

    # Leyenda
    s.g("Leyenda")
    lx = M
    for lab, bg, st, dash in [("Nivel 1 · sección", BLUE, None, None), ("Nivel 2 · pantalla o módulo", WHITE, LINE, None),
                              ("Nivel 3 · contenido y acciones (viñetas)", None, None, None), ("Responde una pregunta de la profe", LYEL, YEL, None),
                              ("Fuera de la app (web)", WHITE, BLUE, "10 6")]:
        if bg:
            s.rect(lx, y, 44, 30, bg, stroke=st, sw=3, r=8, dash=dash)
            s.text(lx + 58, y + 3, lab, 22, 400, INK)
        else:
            s.text(lx, y + 3, "•  " + lab, 22, 400, INK)
        lx += 70 + measure(lab, 22) + 60
    s.endg()
    y += 90

    # Raíz
    rootw, rooth = 760, 120
    rx = M + CW / 2 - rootw / 2
    s.g("Raíz")
    s.rect(rx, y, rootw, rooth, INK, r=60)
    s.text(rx + rootw / 2, y + 26, "Match de ruta verificado", 40, 700, WHITE, center=True)
    s.text(rx + rootw / 2, y + 78, "App móvil + vista web del contacto", 20, 400, WHITE, center=True, mono=True)
    s.endg()
    busy = y + rooth + 60
    n = len(COLS)
    gap = 36
    colw = (CW - gap * (n - 1)) / n
    s.path([(rx + rootw / 2, y + rooth), (rx + rootw / 2, busy)], INK, 3)
    s.path([(M + colw / 2, busy), (M + CW - colw / 2, busy)], INK, 3)
    top = busy + 60
    maxy = top
    for i, (num, title, sub, nodes) in enumerate(COLS):
        cx = M + i * (colw + gap)
        web = num == "9"
        s.g(f"{num} · {title}")
        s.arrow([(cx + colw / 2, busy), (cx + colw / 2, top)], INK, 3)
        hh = 150
        s.rect(cx, top, colw, hh, WHITE if web else BLUE, stroke=BLUE if web else None, sw=3, dash="10 6" if web else None, r=20)
        tc = BLUE if web else WHITE
        s.text(cx + 24, top + 22, num.zfill(2), 22, 700, tc if web else YEL, mono=True)
        s.text(cx + 24, top + 56, title, 30, 700, tc, maxw=colw - 48, lh=1.1)
        s.text(cx + 24, top + 112, sub, 17, 400, tc, mono=True, maxw=colw - 48)
        yy = top + hh + 30
        spx = cx + 22
        last_mid = None
        for (nt, kids, q) in nodes:
            nx, nw = cx + 50, colw - 50
            inner = nw - 44
            qh = (16 + text_h("RESPONDE: " + q, 16, 700, inner, 1.3, mono=True) + 10) if q else 0
            h = 20 + qh + text_h(nt, 23, 700, inner, 1.25) + (10 + sum(text_h("• " + k, 19, 400, inner, 1.35) + 6 for k in kids) if kids else 0) + 18
            s.rect(nx, yy, nw, h, LYEL if q else WHITE, stroke=YEL if q else LINE, sw=4 if q else 2, r=14)
            ty = yy + 20
            if q:
                ty += s.text(nx + 22, ty, "RESPONDE: " + q, 16, 700, BROWN, maxw=inner, lh=1.3, mono=True) + 10
            ty += s.text(nx + 22, ty, nt, 23, 700, INK, maxw=inner, lh=1.25)
            if kids:
                ty += 10
                for k in kids:
                    ty += s.text(nx + 22, ty, "• " + k, 19, 400, INK if not k.startswith("NO ") else RED, maxw=inner, lh=1.35) + 6
            mid = yy + 34
            s.path([(spx, mid), (nx, mid)], MUTE, 2)
            last_mid = mid
            yy += h + 20
        s.path([(spx, top + hh), (spx, last_mid)], MUTE, 2)
        s.endg()
        maxy = max(maxy, yy)
    y = maxy + 100

    # Preguntas respondidas
    s.g("Las preguntas de la profe y dónde se responden")
    y += s.text(M, y, "LAS 4 PREGUNTAS DE LA PROFE", 22, 700, BLUE, mono=True, ls=0.08) + 16
    y += s.text(M, y, "Qué responde la arquitectura (y en qué flujo se ve paso a paso)", 56, 700, INK) + 44
    ans = [
        (Q1, "1 · Verificación → Círculo cercano", "Flujo 02",
         "Quien no tiene correo institucional pide 2 avales a personas que ya están verificadas. Cada persona que avala confirma que la conoce en "
         "persona, la relación (familia, amistad, trabajo o barrio) y desde cuándo. Con 2 avales la cuenta queda “Verificada por círculo”; con 1 queda "
         "pendiente y solo puede configurar rutas. Cada persona puede avalar máximo 5 cuentas, y si una cuenta avalada es suspendida se revisan sus avales: "
         "así quien avala también responde por quien recomienda."),
        (Q2, "5 · Matches → Personas compatibles", "Flujo 05",
         "Cada tarjeta muestra lo justo para decidir sin exponer a nadie: foto, nombre con inicial del apellido, insignia e institución o círculo, "
         "el tramo que comparten, la hora de salida y la diferencia con la tuya, el punto de encuentro sugerido, los trayectos acompañados y los conocidos en común. "
         "No muestra el destino final, el apellido ni el celular."),
        (Q3, "2 · Perfil → Contactos de confianza (y 7 · Antes de salir)", "Flujo 03",
         "Se agregan en Perfil → Contactos de confianza (máximo 3), desde la agenda o a mano, con relación, canal (SMS o WhatsApp) y qué avisos reciben. "
         "El contacto debe aceptar. Antes de cada trayecto la app pregunta a quién avisar esa noche y deja cambiarlo."),
        (Q4, "5 · Matches → Detalle del match", "Flujo 05",
         "El perfil público ampliado, el mapa del tramo compartido (dónde se unen y dónde se separan), el punto y la hora de encuentro, el tiempo "
         "estimado juntos, la verificación (método y fecha), la reputación (trayectos, confirmaciones, sin reportes), la preferencia de compañía y "
         "las acciones: enviar solicitud, bloquear o reportar."),
    ]
    cw2 = (CW - 3 * 40) / 4
    hs = [40 + text_h(q, 28, 700, cw2 - 80, 1.25) + 20 + text_h("→ " + w_ + " · " + f, 18, 700, cw2 - 80, 1.35, mono=True) + 16 + text_h(a, 22, 400, cw2 - 80, 1.5) + 40 for q, w_, f, a in ans]
    ch = max(hs)
    for i, (q, where, fl, a) in enumerate(ans):
        x = M + i * (cw2 + 40)
        s.rect(x, y, cw2, ch, WHITE, stroke=YEL, sw=4, r=24)
        yy = y + 40
        yy += s.text(x + 40, yy, q, 28, 700, INK, maxw=cw2 - 80, lh=1.25) + 20
        yy += s.text(x + 40, yy, "→ " + where + " · " + fl, 18, 700, BROWN, maxw=cw2 - 80, lh=1.35, mono=True) + 16
        s.text(x + 40, yy, a, 22, 400, INK, maxw=cw2 - 80, lh=1.5)
    s.endg()
    y += ch + M
    s.save(out, y)


if __name__ == "__main__":
    import sys
    build(sys.argv[1])
