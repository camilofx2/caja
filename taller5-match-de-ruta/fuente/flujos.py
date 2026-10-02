from svglib import *

W = 5900
M = 120
CW = W - 2 * M
NW = 310          # ancho de nodo
CP = NW + 120     # paso entre columnas
RG = 90           # espacio entre filas
FS = 20           # tamaño del texto de los nodos

TYPES = {
    "start": ("INICIO", INK, None, WHITE, None),
    "end": ("FIN", INK, None, WHITE, None),
    "screen": ("PANTALLA", WHITE, BLUE, INK, None),
    "action": ("ACCIÓN", LBLUE, None, INK, None),
    "system": ("SISTEMA", LGRAY, MUTE, INK, "8 6"),
    "other": ("OTRA PERSONA", LGREEN, GREEN, INK, None),
    "decision": ("DECISIÓN", YEL, None, INK, None),
}

# Cada flujo: (código, título, actor, objetivo, entrada, arquitectura, nodos, aristas, notas)
# nodo: clave -> (tipo, columna, fila, texto)
# arista: (desde, hacia, etiqueta, estilo opcional)
FLOWS = [
    ("01", "Registro y verificación con correo institucional", "Daniela (usuaria nueva)",
     "Crear la cuenta y quedar verificada para poder hacer match.", "Abre la app por primera vez.", "0 · Acceso · 1 · Verificación",
     {
         "a": ("start", 0, 0, "Abre la app por primera vez"),
         "b": ("screen", 1, 0, "Bienvenida: qué es, cómo se verifica y qué pasa con la ubicación"),
         "c": ("action", 2, 0, "Escribe su celular y el código que llega por SMS"),
         "d": ("screen", 3, 0, "Datos básicos: nombre, fecha de nacimiento y género"),
         "e": ("screen", 4, 0, "Permisos: ubicación (solo en uso) y notificaciones"),
         "f": ("decision", 5, 0, "¿Tiene correo institucional?"),
         "g": ("action", 6, 0, "Busca su universidad y escribe su correo"),
         "h": ("system", 7, 0, "Envía un código de 6 dígitos al correo"),
         "i": ("decision", 8, 0, "¿El código es correcto?"),
         "j": ("action", 9, 0, "Toma su foto de perfil en el momento"),
         "k": ("system", 10, 0, "Asigna la insignia “Verificada · Universidad”"),
         "l": ("end", 11, 0, "Cuenta verificada → crear su primera ruta (Flujo 04)"),
         "m": ("end", 5, 1, "Va a verificación por círculo cercano (Flujo 02)"),
         "n": ("action", 8, 1, "Pide reenviar el código (máximo 3 intentos)"),
     },
     [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "g", "Sí"), ("f", "m", "No"), ("g", "h"), ("h", "i"),
      ("i", "j", "Sí"), ("i", "n", "No"), ("n", "h", None, "hv"), ("j", "k"), ("k", "l")],
     "Después de 3 intentos fallidos se bloquea el reenvío por 15 minutos. Sin verificar, la persona puede crear rutas pero no ver ni enviar matches."),

    ("02", "Verificación por círculo cercano (avales)", "Daniela pide · Laura avala",
     "Verificar a quien no tiene correo institucional, con el respaldo de personas ya verificadas.", "Elige “Círculo cercano” en la verificación.",
     "1 · Verificación → Círculo cercano",
     {
         "a": ("start", 0, 0, "No tiene correo institucional"),
         "b": ("screen", 1, 0, "Explica: necesitas 2 avales de personas verificadas que te conozcan"),
         "c": ("action", 2, 0, "Elige 2 personas verificadas de sus contactos o les envía un enlace"),
         "d": ("system", 3, 0, "Envía la solicitud de aval a cada persona"),
         "e": ("other", 4, 0, "Laura recibe la solicitud con la foto y el nombre de Daniela"),
         "f": ("decision", 5, 0, "¿La conoce en persona?"),
         "g": ("other", 6, 0, "Confirma la relación (familia, amistad, trabajo o barrio) y desde cuándo"),
         "h": ("decision", 7, 0, "¿Ya tiene 2 avales?"),
         "i": ("system", 8, 0, "Asigna la insignia “Verificada por círculo · 2 avales”"),
         "j": ("end", 9, 0, "Cuenta verificada"),
         "k": ("other", 5, 1, "Rechaza el aval (Daniela no ve el motivo)"),
         "l": ("system", 6, 1, "Le sugiere pedir el aval a otra persona"),
         "m": ("screen", 7, 1, "Estado: “Pendiente · 1 de 2 avales”. Puede crear rutas, aún no hacer match"),
     },
     [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "g", "Sí"), ("f", "k", "No"), ("k", "l"),
      ("l", "c", None, "loop"), ("g", "h"), ("h", "i", "Sí"), ("h", "m", "No"), ("i", "j")],
     "Reglas: cada persona puede avalar máximo 5 cuentas · el aval se puede retirar · si una cuenta avalada es suspendida por reportes, "
     "se revisan sus avales. Así quien avala también responde por quien recomienda."),

    ("03", "Agregar contactos de confianza", "Daniela · Gloria (contacto)",
     "Definir quién recibe los avisos de inicio, separación, llegada y retraso.", "Perfil → Contactos de confianza (o “Antes de salir” en el Flujo 07).",
     "2 · Perfil → Contactos de confianza · 7 · Antes de salir",
     {
         "a": ("start", 0, 0, "Perfil → Contactos de confianza"),
         "b": ("screen", 1, 0, "Lista vacía: “Agrega hasta 3 personas que reciban tus avisos”"),
         "c": ("action", 2, 0, "Toca “Agregar contacto”"),
         "d": ("decision", 3, 0, "¿Da permiso a la agenda?"),
         "e": ("action", 4, 0, "Elige el contacto en la agenda"),
         "f": ("action", 3, 1, "Escribe nombre y celular a mano"),
         "g": ("screen", 5, 0, "Configura: relación, canal (SMS o WhatsApp) y avisos que recibe"),
         "h": ("system", 6, 0, "Envía invitación: “Daniela te agregó como contacto de confianza”"),
         "i": ("decision", 7, 0, "¿El contacto acepta los avisos?"),
         "j": ("decision", 8, 0, "¿Quiere agregar otro? (máx. 3)"),
         "k": ("action", 9, 0, "Marca un contacto como predeterminado"),
         "l": ("end", 10, 0, "Contactos listos; se confirman antes de cada trayecto"),
         "m": ("screen", 7, 1, "Queda como “No aceptó”; puede elegir a otra persona"),
     },
     [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e", "Sí"), ("d", "f", "No"), ("f", "g", None, "hv"), ("e", "g"), ("g", "h"), ("h", "i"),
      ("i", "j", "Sí"), ("i", "m", "No"), ("j", "c", "Sí", "over"), ("j", "k", "No"), ("k", "l")],
     "El contacto tiene que aceptar: nadie recibe ubicaciones de otra persona sin consentimiento. Gloria no necesita instalar la app (ver Flujo 10)."),

    ("04", "Crear ruta y horario", "Daniela",
     "Registrar el trayecto habitual para que la app encuentre personas compatibles.", "Mis rutas → Nueva ruta.", "3 · Mis rutas",
     {
         "a": ("start", 0, 0, "Mis rutas → “Nueva ruta”"),
         "b": ("action", 1, 0, "Elige el punto de partida (estación o paradero, no dirección)"),
         "c": ("action", 2, 0, "Agrega un tramo: medio + estación de subida y de bajada"),
         "d": ("decision", 3, 0, "¿Hay otro tramo (transbordo)?"),
         "e": ("action", 4, 0, "Elige el paradero final"),
         "f": ("action", 5, 0, "Hora de salida y rango (±15 min)"),
         "g": ("action", 6, 0, "Elige los días de la semana"),
         "h": ("screen", 7, 0, "Resumen: nombre de la ruta, tramos y horario"),
         "i": ("system", 8, 0, "Busca personas compatibles en esos tramos y horario"),
         "j": ("decision", 9, 0, "¿Hay coincidencias?"),
         "k": ("end", 10, 0, "Muestra las personas compatibles (Flujo 05)"),
         "l": ("screen", 9, 1, "Sin matches: ampliar rango, avisarme cuando aparezca alguien o invitar a mi círculo"),
         "m": ("end", 10, 1, "Ruta guardada en espera"),
     },
     [("a", "b"), ("b", "c"), ("c", "d"), ("d", "c", "Sí", "loopd"), ("d", "e", "No"), ("e", "f"), ("f", "g"), ("g", "h"), ("h", "i"), ("i", "j"),
      ("j", "k", "Sí"), ("j", "l", "No"), ("l", "m")],
     "Se empareja por tramo, no por ruta completa: dos personas que comparten solo “Calle 45 → Portal Sur” también son compatibles."),

    ("05", "Revisar personas compatibles y enviar solicitud", "Daniela",
     "Elegir con quién hacer el trayecto a partir de la información del perfil y del detalle del match.", "Inicio → “Ver personas disponibles” o pestaña Matches.",
     "5 · Matches → Lista y Detalle del match",
     {
         "a": ("start", 0, 0, "Inicio → “Ver personas disponibles”"),
         "b": ("screen", 1, 0, "Lista: foto, nombre + inicial, insignia, tramo en común, hora, punto de encuentro, trayectos"),
         "c": ("decision", 2, 0, "¿Quiere filtrar?"),
         "d": ("action", 2, 1, "Filtra: solo mujeres, solo mi institución u hora"),
         "e": ("action", 3, 0, "Abre una tarjeta"),
         "f": ("screen", 4, 0, "Detalle: mapa del tramo, punto y hora de encuentro, verificación, reputación"),
         "g": ("decision", 5, 0, "¿Le da confianza?"),
         "h": ("action", 6, 0, "Envía la solicitud (con un mensaje rápido opcional)"),
         "i": ("system", 7, 0, "Notifica a la otra persona"),
         "j": ("end", 8, 0, "Solicitud pendiente (sigue en el Flujo 06)"),
         "k": ("action", 5, 2, "Vuelve a la lista; si algo no cuadra, bloquea o reporta"),
     },
     [("a", "b"), ("b", "c"), ("c", "e", "No"), ("c", "d", "Sí"), ("d", "b", None, "hv"), ("e", "f"), ("f", "g"), ("g", "h", "Sí"), ("g", "k", "No"),
      ("k", "b", None, "hv"), ("h", "i"), ("i", "j")],
     "La tarjeta nunca muestra el destino final, el apellido ni el celular. El detalle solo lo ven personas compatibles con la ruta."),

    ("06", "Responder la solicitud y confirmar el match", "Laura (recibe la solicitud)",
     "Aceptar o rechazar a una persona y coordinar el encuentro.", "Notificación: “Daniela quiere hacer el trayecto contigo”.",
     "5 · Matches → Solicitudes y Confirmación mutua · 6 · Chat breve",
     {
         "a": ("start", 0, 0, "Recibe la notificación de solicitud"),
         "b": ("screen", 1, 0, "Detalle de la solicitud (el mismo detalle del match)"),
         "c": ("decision", 2, 0, "¿Acepta?"),
         "d": ("system", 3, 0, "Confirmación mutua: las dos aceptaron"),
         "e": ("screen", 4, 0, "Se habilitan el chat, el punto de encuentro y el código de encuentro"),
         "f": ("action", 5, 0, "Coordinan con mensajes rápidos (“Ya llegué”, “Voy 5 min tarde”)"),
         "g": ("decision", 6, 0, "¿Alguien cancela?"),
         "h": ("end", 7, 0, "Listas para el trayecto (Flujo 07)"),
         "i": ("action", 2, 1, "Rechaza; Daniela solo ve “No disponible”"),
         "j": ("end", 3, 1, "Fin"),
         "k": ("system", 6, 1, "Avisa a la otra persona y le sugiere otras compatibles"),
         "l": ("end", 7, 1, "Vuelve al Flujo 05"),
     },
     [("a", "b"), ("b", "c"), ("c", "d", "Sí"), ("c", "i", "No"), ("i", "j"), ("d", "e"), ("e", "f"), ("f", "g"), ("g", "h", "No"), ("g", "k", "Sí"), ("k", "l")],
     "La solicitud vence cuando empieza el horario de salida. Rechazar no tiene consecuencias ni se le explica a la otra persona."),

    ("07", "Trayecto activo: encuentro, recorrido y llegada", "Daniela · Laura · Gloria",
     "Hacer el trayecto acompañada y que el contacto sepa que llegó, sin que quede historial.", "Inicio → “Iniciar trayecto”.",
     "7 · Trayecto activo · 9 · Vista del contacto",
     {
         "a": ("start", 0, 0, "Inicio → “Iniciar trayecto”"),
         "b": ("screen", 1, 0, "Antes de salir: compañía, contactos a avisar y punto de encuentro"),
         "c": ("action", 2, 0, "Confirma a quién avisar esa noche"),
         "d": ("system", 3, 0, "Activa la ubicación temporal y envía el enlace al contacto"),
         "e": ("action", 4, 0, "Llega al punto y toca “Ya llegué”"),
         "f": ("decision", 5, 0, "¿Laura llegó en 10 min?"),
         "g": ("action", 6, 0, "Se encuentran y confirman el código “Naranja-12”"),
         "h": ("decision", 7, 0, "¿El código coincide?"),
         "i": ("screen", 8, 0, "En curso: mapa de ambas, tramo, tiempo de llegada, “Tu mamá ve tu trayecto”"),
         "j": ("decision", 9, 0, "¿Laura se baja antes?"),
         "k": ("decision", 10, 0, "¿Llegó al paradero final a tiempo?"),
         "l": ("system", 11, 0, "Apaga la ubicación sola y avisa: “Daniela llegó 10:38 p. m.”"),
         "n": ("end", 12, 0, "Confirmar el trayecto (Flujo 09)"),
         "o": ("end", 5, 1, "Espera 5 min más, busca a otra persona o sigue sola con el aviso activo"),
         "p": ("end", 7, 1, "No viaja con esa persona y la reporta (Flujo 09)"),
         "q": ("system", 9, -1, "Avisa a Daniela y al contacto: “Sigue sola desde Portal Sur”"),
         "r": ("system", 10, 1, "15 min tarde: pregunta “¿Todo bien?”"),
         "s": ("decision", 10, 2, "¿Responde en 5 min?"),
         "t": ("system", 11, 2, "Avisa al contacto con la última ubicación"),
         "u": ("end", 12, 2, "El contacto decide: llamar o marcar al 123"),
     },
     [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "g", "Sí"), ("f", "o", "No"), ("g", "h"), ("h", "i", "Sí"), ("h", "p", "No"),
      ("i", "j"), ("j", "k", "No"), ("j", "q", "Sí"), ("q", "k", None, "hv"), ("k", "l", "Sí"), ("k", "r", "No"), ("r", "s"), ("s", "t", "No"), ("t", "u"),
      ("s", "i", "Sí", "hv"), ("l", "n")],
     "En cualquier momento del trayecto están los botones “Dejar de compartir” y “¿Algo no está bien?” (Flujo 08)."),

    ("08", "Dejar de compartir y “¿Algo no está bien?”", "Daniela",
     "Controlar la ubicación y pedir apoyo durante el trayecto.", "Botones fijos de la pantalla “En curso”.", "7 · Trayecto activo → En curso",
     {
         "a": ("start", 0, 0, "Durante el trayecto activo"),
         "b": ("decision", 1, 0, "¿Qué necesita?"),
         "c": ("action", 2, 0, "Toca “Dejar de compartir”"),
         "d": ("screen", 3, 0, "Confirma: “Tu contacto dejará de ver tu trayecto”"),
         "e": ("decision", 4, 0, "¿Confirma?"),
         "f": ("system", 5, 0, "Apaga la ubicación y avisa: “Daniela dejó de compartir”"),
         "g": ("end", 6, 0, "Sigue el trayecto sin ubicación"),
         "h": ("end", 4, 1, "Sigue compartiendo"),
         "i": ("action", 2, 2, "Toca “¿Algo no está bien?”"),
         "j": ("screen", 3, 2, "Opciones: llamar al 123, avisar a mis contactos o reportar"),
         "k": ("decision", 4, 2, "¿Qué elige?"),
         "l": ("end", 5, 2, "Abre el marcador con el 123"),
         "m": ("end", 5, 3, "Alerta a sus contactos con la ubicación actual"),
         "o": ("end", 5, 4, "Reporta a la persona (Flujo 09)"),
     },
     [("a", "b"), ("b", "c", "Ubicación"), ("b", "i", "Ayuda"), ("c", "d"), ("d", "e"), ("e", "f", "Sí"), ("e", "h", "No"), ("f", "g"),
      ("i", "j"), ("j", "k"), ("k", "l", "123"), ("k", "m", "Contactos"), ("k", "o", "Reportar")],
     "El botón del 123 es un atajo: Match no reemplaza a las autoridades. Dejar de compartir no cancela el match; solo apaga la ubicación."),

    ("09", "Confirmar el trayecto y reportar conducta", "Daniela (y moderación)",
     "Construir confianza después de cada trayecto y tener consecuencias ante el mal comportamiento.", "Al llegar, o desde el chat o el perfil de la otra persona.",
     "8 · Confianza",
     {
         "a": ("start", 0, 0, "Termina el trayecto"),
         "b": ("decision", 1, 0, "¿Se encontraron?"),
         "c": ("action", 2, 0, "Confirma que hicieron el trayecto juntas"),
         "d": ("action", 3, 0, "Responde en privado: “¿Volverías a viajar con Laura?”"),
         "e": ("decision", 4, 0, "¿Pasó algo que reportar?"),
         "f": ("system", 5, 0, "Suma un trayecto acompañado a ambos perfiles"),
         "g": ("system", 6, 0, "Borra las ubicaciones; el chat se borra en 24 h"),
         "h": ("end", 7, 0, "Fin"),
         "i": ("action", 1, 1, "Marca “No se presentó”"),
         "j": ("system", 2, 1, "Registra la ausencia (3 ausencias = advertencia)"),
         "k": ("end", 3, 1, "Fin"),
         "l": ("action", 4, -1, "Elige el motivo: acoso, actitud inapropiada, suplantación, otro"),
         "m": ("action", 5, -1, "Describe lo que pasó (opcional)"),
         "n": ("system", 6, -1, "Bloquea a la persona de inmediato y envía el caso a moderación"),
         "o": ("decision", 7, -1, "¿Moderación confirma la falta?"),
         "p": ("system", 8, -1, "Suspende la cuenta y revisa sus avales"),
         "q": ("end", 9, -1, "Informa el resultado a quien reportó"),
         "r": ("end", 7, -2, "Queda una advertencia interna"),
     },
     [("a", "b"), ("b", "c", "Sí"), ("b", "i", "No"), ("i", "j"), ("j", "k"), ("c", "d"), ("d", "e"), ("e", "f", "No"), ("e", "l", "Sí"), ("f", "g"), ("g", "h"),
      ("l", "m"), ("m", "n"), ("n", "o"), ("o", "p", "Sí"), ("o", "r", "No"), ("p", "q")],
     "Las respuestas de “¿Volverías a viajar?” son privadas: no hay estrellas públicas, para evitar castigos injustos o revanchas."),

    ("10", "Vista del contacto avisado (sin app)", "Gloria, mamá de Daniela",
     "Saber con quién va Daniela y que llegó, sin instalar nada.", "Mensaje por SMS o WhatsApp.", "9 · Vista del contacto",
     {
         "a": ("start", 0, 0, "Daniela la agrega como contacto (Flujo 03)"),
         "b": ("system", 1, 0, "SMS o WhatsApp: “Daniela te agregó como contacto de confianza”"),
         "c": ("decision", 2, 0, "¿Acepta recibir avisos?"),
         "d": ("system", 3, 0, "Cuando Daniela inicia un trayecto llega un enlace"),
         "e": ("screen", 4, 0, "Página web: con quién va (foto, nombre, verificación), mapa en vivo, hora estimada"),
         "f": ("decision", 5, 0, "¿Qué aviso llega?"),
         "g": ("system", 6, 0, "Llegada: “Daniela llegó 10:38 p. m.”"),
         "h": ("system", 7, 0, "El enlace deja de funcionar"),
         "i": ("end", 8, 0, "Fin"),
         "j": ("end", 2, 1, "No recibe avisos; Daniela elige a otra persona"),
         "k": ("system", 6, 1, "Separación: “Sigue sola desde Portal Sur”"),
         "l": ("end", 7, 1, "Sigue viendo el trayecto hasta la llegada"),
         "m": ("system", 6, 2, "Retraso sin respuesta: última ubicación conocida"),
         "n": ("end", 7, 2, "Llama a Daniela o al 123"),
     },
     [("a", "b"), ("b", "c"), ("c", "d", "Sí"), ("c", "j", "No"), ("d", "e"), ("e", "f"), ("f", "g", "Llegada"), ("f", "k", "Separación"), ("f", "m", "Retraso"),
      ("g", "h"), ("h", "i"), ("k", "l"), ("m", "n")],
     "Responde al usuario secundario de la investigación: la mayoría le avisa a alguien. El enlace no muestra historial ni la dirección de la casa."),
]


def node_size(t, txt):
    if t == "decision":
        th = text_h(txt, 19, 700, NW * 0.5, 1.25)
        return NW, max(190, th * 2 + 70)
    inner = NW - 40
    return NW, max(120, 18 + 14 * 1.3 + 8 + text_h(txt, FS, 500 if t in ("start", "end") else 400, inner, 1.35) + 20)


def draw_node(s, t, x, y, w, h, txt):
    lab, bg, st, fg, dash = TYPES[t]
    if t == "decision":
        cx, cy = x + w / 2, y + h / 2
        s.poly([(cx, y), (x + w, cy), (cx, y + h), (x, cy)], bg)
        lines = wrap(txt, 19, 700, w * 0.5)
        th = len(lines) * 19 * 1.25
        s.text(cx, cy - th / 2, "\n".join(lines), 19, 700, fg, lh=1.25, center=True)
        return
    r = h / 2 if t in ("start", "end") else 16
    r = min(r, 40)
    s.rect(x, y, w, h, bg, stroke=st, sw=3 if st else 2, r=r, dash=dash)
    s.text(x + 20, y + 18, lab, 14, 700, YEL if t in ("start", "end") else (GREEN if t == "other" else BLUE if t == "screen" else MUTE), mono=True, ls=0.06)
    s.text(x + 20, y + 18 + 14 * 1.3 + 8, txt, FS, 500 if t in ("start", "end") else 400, fg, maxw=w - 40, lh=1.35)


def draw_flow(s, y, flow):
    code, title, actor, goal, entry, arch, nodes, edges, notes = flow
    s.g(f"Flujo {code} · {title}")
    top = y
    x0 = M + 60
    yy = y + 60
    s.text(x0, yy, f"FLUJO {code}", 22, 700, BLUE, mono=True, ls=0.08)
    yy += 40
    yy += s.text(x0, yy, title, 56, 700, INK) + 20
    meta = [("Actor", actor), ("Objetivo", goal), ("Punto de entrada", entry), ("Arquitectura", arch)]
    mx = x0
    mw = (CW - 120 - 3 * 40) / 4
    mh = 0
    for k, v in meta:
        s.text(mx, yy, k.upper(), 16, 700, MUTE, mono=True, ls=0.06)
        mh = max(mh, 28 + s.text(mx, yy + 28, v, 22, 400, INK, maxw=mw, lh=1.4))
        mx += mw + 40
    yy += mh + 110

    # filas
    sizes = {k: node_size(v[0], v[3]) for k, v in nodes.items()}
    rows = sorted({v[2] for v in nodes.values()})
    rowh = {r: max(sizes[k][1] for k, v in nodes.items() if v[2] == r) for r in rows}
    rowy = {}
    cy = yy
    for r in rows:
        rowy[r] = cy
        cy += rowh[r] + RG
    box = {}
    for k, (t, c, r, txt) in nodes.items():
        w, h = sizes[k]
        x = x0 + c * CP
        ny = rowy[r] + (rowh[r] - h) / 2
        box[k] = (x, ny, w, h)

    def anc(k, side):
        x, y_, w, h = box[k]
        return {"l": (x, y_ + h / 2), "r": (x + w, y_ + h / 2), "t": (x + w / 2, y_), "b": (x + w / 2, y_ + h)}[side]

    labels = []
    for e in edges:
        a, b = e[0], e[1]
        lab = e[2] if len(e) > 2 else None
        style = e[3] if len(e) > 3 else None
        ta, ca, ra, _ = nodes[a]
        tb, cb, rb, _ = nodes[b]
        if not style:
            if ra == rb:
                style = "h" if cb > ca else "over"
            elif ca == cb:
                style = "v"
            elif ta == "decision":
                style = "vh"
            else:
                style = "hv"
        if style == "h":
            p = [anc(a, "r"), anc(b, "l")]
        elif style == "v":
            p = [anc(a, "b"), anc(b, "t")] if rb > ra else [anc(a, "t"), anc(b, "b")]
        elif style == "vh":
            s0 = anc(a, "b") if rb > ra else anc(a, "t")
            e0 = anc(b, "l") if cb > ca else anc(b, "r")
            p = [s0, (s0[0], e0[1]), e0]
        elif style == "hv":
            s0 = anc(a, "r") if cb > ca else anc(a, "l")
            e0 = anc(b, "t") if rb > ra else anc(b, "b")
            p = [s0, (e0[0], s0[1]), e0]
        elif style == "over":
            s0, e0 = anc(a, "t"), anc(b, "t")
            ly = rowy[ra] - 45
            p = [s0, (s0[0], ly), (e0[0], ly), e0]
        elif style in ("loop", "loopd"):
            s0, e0 = anc(a, "b"), anc(b, "b")
            ly = max(box[a][1] + box[a][3], box[b][1] + box[b][3]) + 45
            p = [s0, (s0[0], ly), (e0[0], ly), e0]
        s.arrow(p, INK, 3)
        if lab:
            (x1, y1), (x2, y2) = p[0], p[1]
            if style == "vh":
                lx, ly_ = p[1][0] + 14, p[1][1] - 36
            elif abs(x2 - x1) > abs(y2 - y1):
                lx, ly_ = (x1 + 14 if x2 > x1 else x1 - measure(lab, 17, 700, True) - 34), y1 - 36
            else:
                lx, ly_ = x1 + 14, (y1 + 10 if y2 > y1 else y1 - 40)
            labels.append((lx, ly_, lab))
    for k, (t, c, r, txt) in nodes.items():
        draw_node(s, t, *box[k], txt)
    for lx, ly_, lab in labels:
        lw = measure(lab, 17, 700, True) + 20
        s.rect(lx, ly_, lw, 30, WHITE, stroke=INK, sw=1.5, r=15)
        s.text(lx + 10, ly_ + 5, lab, 17, 700, INK, mono=True)
    bottom = max(b[1] + b[3] for b in box.values()) + 80
    if notes:
        nh = 24 + text_h("Nota: " + notes, 22, 400, CW - 200, 1.45) + 24
        s.rect(x0, bottom, CW - 120, nh, BG, r=16)
        s.text(x0 + 30, bottom + 24, "Nota: " + notes, 22, 400, INK, maxw=CW - 200, lh=1.45)
        bottom += nh + 60
    s.add(f'<rect x="{M}" y="{top}" width="{CW}" height="{bottom - top:.0f}" fill="none" stroke="{LINE}" stroke-width="3" rx="32" ry="32"/>')
    s.endg()
    return bottom


def build(out):
    s = Svg(W)
    y = M
    y = header(
        s, M, y, CW, "04 · DEFINIR EL PRODUCTO · USER FLOWS", "User flows por funcionalidad",
        "Cada proceso tiene su propio recorrido paso a paso, desde el punto de entrada hasta el resultado, con las decisiones y los caminos "
        "alternativos. Los 10 flujos salen de la arquitectura de la información y comparten la misma notación.",
        "“La entrega debe contener Arquitectura, User Persona y Benchmarking, junto con sus respectivos User Flows, desarrollados por "
        "funcionalidad. No necesitamos un único flow general: cada proceso debe tener su propio recorrido paso a paso.”",
    )
    # índice + leyenda
    s.g("Índice y notación")
    colw = (CW - 40) / 2
    idx = [f"{f[0]} · {f[1]}" for f in FLOWS]
    ih = 40 + 30 + 20 + 5 * 44 + 30
    s.rect(M, y, colw, ih, WHITE, stroke=LINE, r=24)
    s.text(M + 40, y + 40, "ÍNDICE DE FLUJOS", 18, 700, BLUE, mono=True, ls=0.08)
    for i, t in enumerate(idx):
        cx = M + 40 + (i // 5) * (colw - 80) / 2
        s.text(cx, y + 90 + (i % 5) * 44, t, 21, 400, INK, maxw=(colw - 80) / 2 - 20)
    lx = M + colw + 40
    s.rect(lx, y, colw, ih, WHITE, stroke=LINE, r=24)
    s.text(lx + 40, y + 40, "NOTACIÓN", 18, 700, BLUE, mono=True, ls=0.08)
    items = [("start", "Inicio / fin"), ("screen", "Pantalla"), ("action", "Acción del usuario"), ("system", "Respuesta del sistema"),
             ("other", "Otra persona (avala, acepta, recibe)"), ("decision", "Decisión")]
    for i, (t, d) in enumerate(items):
        cx = lx + 40 + (i % 2) * (colw - 80) / 2
        cy = y + 90 + (i // 2) * 70
        lab, bg, st, fg, dash = TYPES[t]
        if t == "decision":
            s.poly([(cx + 40, cy), (cx + 80, cy + 22), (cx + 40, cy + 44), (cx, cy + 22)], bg)
        else:
            s.rect(cx, cy, 80, 44, bg, stroke=st, sw=3 if st else 2, r=22 if t == "start" else 8, dash=dash)
        s.text(cx + 100, cy + 10, d, 22, 400, INK)
    s.endg()
    y += ih + 80
    for f in FLOWS:
        y = draw_flow(s, y, f) + 60
    s.save(out, y + 60)


if __name__ == "__main__":
    import sys
    build(sys.argv[1])
