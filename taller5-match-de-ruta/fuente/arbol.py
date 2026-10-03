"""Arquitectura de la información en árbol (de arriba hacia abajo), al estilo de la referencia."""
from svglib import Svg, measure, text_h, wrap

BG = "#F4F4F5"
DARK = "#1F1F1F"
ARROW = "#3A3A3A"
Q = "#FFB81C"

# (título, color fuerte, color claro, hijos); hijo = (nombre, [subítems], pregunta o None)
SECCIONES = [
    ("INGRESO", "#1F1F1F", "#D9D9D9", [
        ("Bienvenida", ["Qué es Match", "Cómo se verifica", "Qué pasa con tu ubicación"], None),
        ("Crear cuenta", ["Celular + código SMS", "Nombre y fecha de nacimiento", "Género", "Permisos", "Términos y datos (Ley 1581)"], None),
        ("Iniciar sesión", ["Celular + código SMS"], None),
        ("Recuperar cuenta", ["Por celular", "Por correo institucional"], None),
    ]),
    ("VERIFICACIÓN", "#15803D", "#D3F2DC", [
        ("Correo institucional", ["Buscar institución", "Correo @institución", "Código de 6 dígitos", "Foto en el momento", "Insignia “Verificada”"], None),
        ("Círculo cercano (avales)", ["Pedir 2 avales", "Quien avala la conoce en persona", "Relación y tiempo", "Máx. 5 avales por persona", "Insignia “Verificada por círculo”"], 1),
        ("Estado de la cuenta", ["Sin verificar", "Pendiente (1 de 2 avales)", "Verificada", "En revisión / suspendida"], None),
        ("Mis círculos", ["Universidad", "Trabajo", "Barrio o amigos"], None),
    ]),
    ("INICIO", "#084FE9", "#D6E3FD", [
        ("HOY", ["Próximo trayecto", "Personas disponibles hoy", "Solicitudes pendientes", "Iniciar trayecto", "Tiempos de llegada"], None),
        ("MIS RUTAS", ["Rutas guardadas", "Crear / editar ruta", "Partida y tramos", "Paradero final", "Hora ±15 min y días", "Trayecto de una sola vez", "Pausar / eliminar"], None),
        ("MATCHES", ["Personas compatibles", "Filtros", "Solicitudes", "Compañía frecuente", "Sin matches"], None),
        ("PERFIL", ["Perfil público", "Datos privados", "Preferencias de match", "!Contactos de confianza", "Privacidad", "Ajustes"], -3),
    ]),
    ("MATCH", "#7C3AED", "#E6DCFD", [
        ("Personas compatibles", ["Foto", "Nombre + inicial", "Insignia e institución", "Tramo en común", "Hora y diferencia", "Punto de encuentro", "Trayectos acompañados", "Sin destino ni celular"], 2),
        ("Detalle del match", ["Mapa del tramo compartido", "Punto y hora de encuentro", "Tiempo juntos", "Verificación", "Reputación", "Solicitar / bloquear / reportar"], 4),
        ("Solicitud", ["Enviar", "Aceptar o rechazar", "Vence al iniciar el horario"], None),
        ("Confirmación mutua", ["Habilita chat y punto"], None),
        ("Chat breve", ["Mensajes rápidos", "Código de encuentro", "Sin fotos ni archivos", "Se borra en 24 h"], None),
    ]),
    ("TRAYECTO ACTIVO", "#C2410C", "#FDE2CC", [
        ("Antes de salir", ["Confirmar compañía", "Contactos a avisar", "Punto de encuentro"], 3),
        ("Encuentro", ["“Ya llegué”", "Confirmar código", "Si no llega en 10 min"], None),
        ("En curso", ["Mapa de ambas", "Tramo y tiempo de llegada", "Dejar de compartir", "¿Algo no está bien?"], None),
        ("Separación", ["Aviso: sigue sola"], None),
        ("Llegada", ["Apaga la ubicación", "Aviso al contacto"], None),
        ("Retraso", ["“¿Todo bien?”", "Aviso con última ubicación"], None),
    ]),
    ("CONFIANZA", "#BE185D", "#FBD5E5", [
        ("Confirmar trayecto", ["¿Se encontraron?", "Suma un trayecto"], None),
        ("¿Volverías a viajar?", ["Respuesta privada"], None),
        ("Reportar y bloquear", ["Motivo", "Moderación", "Advertencia o suspensión"], None),
        ("Sin historial", ["Se guarda: fecha y persona", "Se borra: ubicaciones y chat"], None),
    ]),
    ("VISTA DEL CONTACTO (WEB, SIN APP)", "#525252", "#E5E5E5", [
        ("Invitación", ["SMS o WhatsApp", "Aceptar avisos"], None),
        ("Enlace del trayecto", ["Con quién va", "Mapa en vivo", "Hora estimada"], None),
        ("Avisos", ["Inicio", "Separación", "Llegada", "Retraso"], None),
        ("Caducidad", ["Se apaga al llegar"], None),
    ]),
]

CW_ = 270      # ancho de cada columna hija
GAP = 22
CENTER_GAP = 90
FS = 16


def pill(s, cx, y, text, fill, fg, bold=False, w=None, stroke=None, size=FS, dash=None):
    w = w or measure(text, size, 700 if bold else 400) + 40
    lines = wrap(text, size, 700 if bold else 400, w - 24)
    h = max(36, len(lines) * size * 1.3 + 16)
    s.rect(cx - w / 2, y, w, h, fill, stroke=stroke, sw=3, r=min(h / 2, 18), dash=dash)
    s.text(cx, y + (h - len(lines) * size * 1.3) / 2 + 1, "\n".join(lines), size, 700 if bold else 400, fg, lh=1.3, center=True)
    return h


def arrow_down(s, x, y1, y2):
    s.arrow([(x, y1), (x, y2)], ARROW, 2.5, hs=10)


def build(path):
    W = 2600
    cx = W / 2
    s = Svg(W, None, BG)
    y = 80
    s.text(80, y, "03 · ANALIZAR · ARQUITECTURA DE LA INFORMACIÓN", 22, 700, "#084FE9", mono=True, ls=0.06)
    y += 40
    s.text(80, y, "Arquitectura de la información", 72, 700, DARK)
    y += 100
    y += s.text(80, y, "Qué contiene la plataforma, de arriba hacia abajo. Barra inferior: Hoy · Mis rutas · Matches · Perfil. "
                "El trayecto activo aparece como banner fijo y el contacto avisado ve una página web sin instalar la app. "
                "Las cajas con borde amarillo responden las preguntas de la profe.", 24, 400, "#525252", maxw=1900, lh=1.45) + 30
    # leyenda de preguntas
    qs = ["1 · ¿Cómo funciona la verificación por círculo cercano?", "2 · ¿Qué muestra al revisar los posibles perfiles?",
          "3 · ¿Dónde agrego los contactos que serán avisados?", "4 · ¿Qué contiene el detalle de un match?"]
    lx = 80
    for qtxt in qs:
        w = measure(qtxt, 18, 700) + 60
        s.rect(lx, y, w, 40, "#FFFFFF", stroke=Q, sw=3, r=20)
        s.text(lx + 18, y + 10, qtxt, 18, 700, DARK)
        lx += w + 16
    y += 110
    prev_bottom = None
    for title, strong, light, kids in SECCIONES:
        web = title.startswith("VISTA")
        if prev_bottom is not None:
            arrow_down(s, cx, prev_bottom, y)
        s.g(title.capitalize())
        h = pill(s, cx, y, title, "#FFFFFF" if web else strong, strong if web else "#FFFFFF", bold=True,
                 w=measure(title, 20, 700) + 60, size=20, stroke=strong if web else None, dash="8 6" if web else None)
        top = y + h
        n = len(kids)
        nl = n // 2
        nr = n - nl
        xs = []
        for i in range(nl):
            xs.append(cx - CENTER_GAP / 2 - (nl - i - 1) * (CW_ + GAP) - CW_ / 2)
        for i in range(nr):
            xs.append(cx + CENTER_GAP / 2 + i * (CW_ + GAP) + CW_ / 2)
        bus = top + 34
        s.path([(cx, top), (cx, bus)], ARROW, 2.5)
        s.path([(min(xs), bus), (max(xs), bus)], ARROW, 2.5)
        bottoms = []
        for x, (nm, subs, q) in zip(xs, kids):
            ky = bus + 34
            arrow_down(s, x, bus, ky)
            whole = bool(q) and q > 0
            if q:
                s.circle(x + CW_ / 2 - 6, ky - 4, 15, Q)
                s.text(x + CW_ / 2 - 6, ky - 14, str(abs(q)), 17, 700, DARK, mono=True, center=True)
            kh = pill(s, x, ky, nm, strong, "#FFFFFF", bold=True, w=CW_, size=17, stroke=Q if whole else None)
            sy = ky + kh + 10
            for sub in subs:
                hi = whole or sub.startswith("!")
                sub = sub.lstrip("!")
                sh = pill(s, x, sy, sub, light, DARK, w=CW_ - 20, size=FS, stroke=Q if hi else None)
                sy += sh + 8
            bottoms.append(sy)
        prev_bottom = max(bottoms) + 10
        if title != SECCIONES[-1][0]:
            s.path([(cx, bus), (cx, prev_bottom)], ARROW, 2.5)
        s.endg()
        y = prev_bottom + 70
        # el eje central sigue entre las columnas
    s.save(path, y + 40)


if __name__ == "__main__":
    import sys
    build(sys.argv[1])
