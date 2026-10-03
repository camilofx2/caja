"""25 user flows verticales, uno por nodo de la arquitectura, con la notación de la referencia."""
from svglib import Svg, measure, text_h, wrap

BG = "#F4F4F5"
DARK = "#1F1F1F"
ARROW = "#4A4A4A"
STY = {  # tipo: (relleno, contorno)
    "term": ("#B5B5B5", None),
    "proc": ("#D9CCFB", None),
    "inp": ("#C3DDFD", None),
    "sys": ("#CDEFD7", None),
    "dec": ("#FAD9B8", None),
}
NW, CP, VG, FS = 230, 272, 44, 15

# nodo: clave -> (tipo, col, fila, texto); arista: (desde, hacia, etiqueta, estilo)
FLUJOS = [
    ("ACCESO", [
        ("01", "Ingreso", "Ingreso", {
            "a": ("term", 0, 0, "Ingreso"), "b": ("proc", 0, 1, "Bienvenida: qué es, verificación y privacidad"),
            "c": ("dec", 0, 2, "¿Cómo quieres ingresar?"), "d": ("term", -1, 3, "Crear cuenta (F02)"),
            "e": ("term", 0, 3, "Iniciar sesión (F03)"), "f": ("term", 1, 3, "Recuperar cuenta (F04)")},
         [("a", "b"), ("b", "c"), ("c", "d", None, "fan"), ("c", "e", None, "fan"), ("c", "f", None, "fan")]),
        ("02", "Crear cuenta", "Ingreso → Crear cuenta", {
            "a": ("term", 0, 0, "Crear cuenta"), "b": ("inp", 0, 1, "Ingresa su número de celular"),
            "c": ("sys", 0, 2, "Envía un código por SMS"), "d": ("inp", 0, 3, "Ingresa el código"),
            "e": ("dec", 0, 4, "¿Código correcto?"), "f": ("proc", 1, 4, "Reenviar código (máx. 3)"),
            "g": ("inp", 0, 5, "Nombre, fecha de nacimiento y género"), "h": ("dec", 0, 6, "¿Es mayor de 18?"),
            "i": ("term", 1, 6, "No puede registrarse"), "j": ("proc", 0, 7, "Permisos: ubicación y notificaciones"),
            "k": ("proc", 0, 8, "Acepta términos y datos (Ley 1581)"), "l": ("term", 0, 9, "Verificación (F05)")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f", "No"), ("f", "c", None, "back"), ("e", "g", "Sí"),
          ("g", "h"), ("h", "i", "No"), ("h", "j", "Sí"), ("j", "k"), ("k", "l")]),
        ("03", "Iniciar sesión", "Ingreso → Iniciar sesión", {
            "a": ("term", 0, 0, "Iniciar sesión"), "b": ("inp", 0, 1, "Ingresa su celular"),
            "c": ("sys", 0, 2, "Envía un código por SMS"), "d": ("inp", 0, 3, "Ingresa el código"),
            "e": ("dec", 0, 4, "¿Código correcto?"), "f": ("proc", 1, 4, "Muestra el error"),
            "g": ("dec", 0, 5, "¿Cuenta verificada?"), "h": ("term", 1, 5, "Verificación (F05)"),
            "i": ("term", 0, 6, "Inicio (F09)")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f", "No"), ("f", "d", None, "back"), ("e", "g", "Sí"),
          ("g", "h", "No"), ("g", "i", "Sí")]),
        ("04", "Recuperar cuenta", "Ingreso → Recuperar cuenta", {
            "a": ("term", 0, 0, "Recuperar cuenta"), "b": ("dec", 0, 1, "¿Conserva su número?"),
            "c": ("inp", 0, 2, "Ingresa su celular"), "d": ("inp", 1, 2, "Ingresa su correo institucional"),
            "e": ("sys", 0, 3, "Envía código por SMS"), "f": ("sys", 1, 3, "Envía código al correo"),
            "g": ("inp", 0, 4, "Ingresa el código"), "h": ("dec", 0, 5, "¿Código correcto?"),
            "i": ("proc", 1, 5, "Muestra el error"), "j": ("inp", 0, 6, "Registra el celular nuevo (si cambió)"),
            "k": ("term", 0, 7, "Inicio (F09)")},
         [("a", "b"), ("b", "c", "Sí"), ("b", "d", "No", "hv"), ("c", "e"), ("d", "f"), ("e", "g"), ("f", "g", None, "join"),
          ("g", "h"), ("h", "i", "No"), ("i", "g", None, "back"), ("h", "j", "Sí"), ("j", "k")]),
    ]),
    ("VERIFICACIÓN", [
        ("05", "Elegir método de verificación", "Verificación", {
            "a": ("term", 0, 0, "Verificación"), "b": ("proc", 0, 1, "Explica por qué se verifica a todas las personas"),
            "c": ("dec", 0, 2, "¿Tiene correo institucional?"), "d": ("term", 0, 3, "Correo institucional (F06)"),
            "e": ("term", 1, 2, "Círculo cercano (F07)")},
         [("a", "b"), ("b", "c"), ("c", "d", "Sí"), ("c", "e", "No")]),
        ("06", "Correo institucional", "Verificación → Correo institucional", {
            "a": ("term", 0, 0, "Correo institucional"), "b": ("inp", 0, 1, "Busca su universidad o empresa"),
            "c": ("inp", 0, 2, "Escribe su correo @institución"), "d": ("sys", 0, 3, "Envía un código de 6 dígitos"),
            "e": ("inp", 0, 4, "Ingresa el código"), "f": ("dec", 0, 5, "¿Código correcto?"),
            "g": ("proc", 1, 5, "Reenviar código (máx. 3)"), "h": ("inp", 0, 6, "Toma su foto en el momento"),
            "i": ("sys", 0, 7, "Asigna la insignia “Verificada · Universidad”"), "j": ("term", 0, 8, "Crear primera ruta (F10)")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "g", "No"), ("g", "d", None, "back"),
          ("f", "h", "Sí"), ("h", "i"), ("i", "j")]),
        ("07", "Círculo cercano: pedir avales", "Verificación → Círculo cercano  ·  Pregunta 1", {
            "a": ("term", 0, 0, "Círculo cercano"), "b": ("proc", 0, 1, "Explica: necesitas 2 avales de personas verificadas"),
            "c": ("inp", 0, 2, "Elige 2 personas verificadas o envía un enlace"), "d": ("sys", 0, 3, "Envía las solicitudes de aval (F08)"),
            "e": ("dec", 0, 4, "¿Tiene 2 avales?"), "f": ("proc", 1, 4, "Pendiente · 1 de 2: puede crear rutas, aún no hacer match"),
            "g": ("sys", 0, 5, "Asigna la insignia “Verificada por círculo”"), "h": ("term", 0, 6, "Cuenta verificada")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f", "No"), ("f", "c", None, "back"), ("e", "g", "Sí"), ("g", "h")]),
        ("08", "Círculo cercano: dar un aval", "Verificación → Círculo cercano  ·  Pregunta 1", {
            "a": ("term", 0, 0, "Recibe una solicitud de aval"), "b": ("proc", 0, 1, "Ve la foto y el nombre de quien la pide"),
            "c": ("dec", 0, 2, "¿La conoce en persona?"), "d": ("term", 1, 2, "Rechaza (no se muestra el motivo)"),
            "e": ("inp", 0, 3, "Indica la relación y desde cuándo se conocen"), "f": ("dec", 0, 4, "¿Tiene avales disponibles? (máx. 5)"),
            "g": ("term", 1, 4, "Aviso: llegó al límite de avales"), "h": ("sys", 0, 5, "Registra el aval"),
            "i": ("term", 0, 6, "Aval enviado")},
         [("a", "b"), ("b", "c"), ("c", "d", "No"), ("c", "e", "Sí"), ("e", "f"), ("f", "g", "No"), ("f", "h", "Sí"), ("h", "i")]),
    ]),
    ("INICIO Y MIS RUTAS", [
        ("09", "Inicio", "Inicio", {
            "a": ("term", 0, 0, "Inicio"), "b": ("proc", 0, 1, "Próximo trayecto, personas disponibles hoy y solicitudes"),
            "c": ("dec", 0, 2, "¿Qué quieres hacer?"), "d": ("term", -2, 3, "Iniciar trayecto (F17)"),
            "e": ("term", -1, 3, "Ver personas (F13)"), "f": ("term", 0, 3, "Solicitudes (F14)"),
            "g": ("term", 1, 3, "Mis rutas (F11)"), "h": ("term", 2, 3, "Perfil (F20)")},
         [("a", "b"), ("b", "c")] + [("c", k, None, "fan") for k in "defgh"]),
        ("10", "Crear ruta y horario", "Mis rutas → Crear / editar ruta", {
            "a": ("term", 0, 0, "Nueva ruta"), "b": ("inp", 0, 1, "Punto de partida: estación o paradero"),
            "c": ("inp", 0, 2, "Tramo: medio, estación de subida y de bajada"), "d": ("dec", 0, 3, "¿Hay otro tramo?"),
            "e": ("inp", 0, 4, "Paradero final (no dirección)"), "f": ("inp", 0, 5, "Hora de salida y rango (±15 min)"),
            "g": ("inp", 0, 6, "Días de la semana"), "h": ("proc", 0, 7, "Resumen de la ruta"),
            "i": ("sys", 0, 8, "Busca personas compatibles por tramo y horario"), "j": ("dec", 0, 9, "¿Hay coincidencias?"),
            "k": ("term", 0, 10, "Personas compatibles (F13)"), "l": ("term", 1, 9, "Sin matches (F15)")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "c", "Sí", "back"), ("d", "e", "No"), ("e", "f"), ("f", "g"), ("g", "h"),
          ("h", "i"), ("i", "j"), ("j", "k", "Sí"), ("j", "l", "No")]),
        ("11", "Gestionar rutas", "Mis rutas → Rutas guardadas", {
            "a": ("term", 0, 0, "Mis rutas"), "b": ("dec", 0, 1, "¿Hay rutas guardadas?"),
            "c": ("term", 1, 1, "Estado vacío → Crear ruta (F10)"), "d": ("proc", 0, 2, "Elige una ruta"),
            "e": ("dec", 0, 3, "¿Qué quieres hacer?"), "f": ("inp", -1, 4, "Edita tramos u horario"),
            "g": ("sys", 0, 4, "Pausa: deja de aparecer en matches"), "h": ("dec", 1, 4, "¿Confirma eliminar?"),
            "i": ("sys", -1, 5, "Recalcula personas compatibles"), "j": ("sys", 1, 5, "Borra la ruta y sus solicitudes"),
            "k": ("term", 0, 6, "Mis rutas")},
         [("a", "b"), ("b", "c", "No"), ("b", "d", "Sí"), ("d", "e"), ("e", "f", None, "fan"), ("e", "g", None, "fan"), ("e", "h", None, "fan"),
          ("f", "i"), ("h", "j", "Sí"), ("h", "d", "No", "back"), ("i", "k", None, "join"), ("g", "k"), ("j", "k", None, "join")]),
        ("12", "Trayecto de una sola vez", "Mis rutas → Trayecto de una sola vez", {
            "a": ("term", 0, 0, "Trayecto de una sola vez"), "b": ("inp", 0, 1, "Partida, destino y hora de hoy"),
            "c": ("sys", 0, 2, "Busca personas compatibles"), "d": ("dec", 0, 3, "¿Hay coincidencias?"),
            "e": ("term", 0, 4, "Personas compatibles (F13)"), "f": ("term", 1, 3, "Sin matches (F15)")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e", "Sí"), ("d", "f", "No")]),
    ]),
    ("MATCHES", [
        ("13", "Ver compatibles y enviar solicitud", "Match → Personas compatibles y Detalle  ·  Preguntas 2 y 4", {
            "a": ("term", 0, 0, "Personas compatibles"),
            "b": ("proc", 0, 1, "Lista: foto, nombre + inicial, insignia, tramo en común, hora y punto de encuentro"),
            "c": ("dec", 0, 2, "¿Quiere filtrar?"), "d": ("inp", 1, 2, "Filtra: solo mujeres, institución u hora"),
            "e": ("proc", 0, 3, "Abre una tarjeta"),
            "f": ("proc", 0, 4, "Detalle: mapa del tramo, punto y hora, verificación y reputación"),
            "g": ("dec", 0, 5, "¿Le da confianza?"), "h": ("proc", 1, 5, "Vuelve, bloquea o reporta"),
            "i": ("inp", 0, 6, "Envía la solicitud"), "j": ("sys", 0, 7, "Notifica a la otra persona"),
            "k": ("term", 0, 8, "Solicitud pendiente (F14)")},
         [("a", "b"), ("b", "c"), ("c", "d", "Sí"), ("d", "b", None, "back"), ("c", "e", "No"), ("e", "f"), ("f", "g"),
          ("g", "h", "No"), ("h", "b", None, "back2"), ("g", "i", "Sí"), ("i", "j"), ("j", "k")]),
        ("14", "Responder solicitud", "Match → Solicitud y Confirmación mutua", {
            "a": ("term", 0, 0, "Recibe una solicitud"), "b": ("proc", 0, 1, "Detalle de quien la envía"),
            "c": ("dec", 0, 2, "¿Acepta?"), "d": ("term", 1, 2, "Rechaza: la otra persona ve “No disponible”"),
            "e": ("sys", 0, 3, "Confirmación mutua"), "f": ("proc", 0, 4, "Se habilitan chat, punto y código de encuentro"),
            "g": ("dec", 0, 5, "¿Alguien cancela?"), "h": ("sys", 1, 5, "Avisa y sugiere otras personas"),
            "i": ("term", 0, 6, "Listas para el trayecto (F17)")},
         [("a", "b"), ("b", "c"), ("c", "d", "No"), ("c", "e", "Sí"), ("e", "f"), ("f", "g"), ("g", "h", "Sí"), ("g", "i", "No")]),
        ("15", "Sin matches", "Matches → Sin matches", {
            "a": ("term", 0, 0, "Sin matches"), "b": ("proc", 0, 1, "“Aún no hay nadie en tu tramo y horario”"),
            "c": ("dec", 0, 2, "¿Qué quieres hacer?"), "d": ("inp", -1, 3, "Amplía el rango a ±30 min"),
            "e": ("sys", 0, 3, "Te avisa cuando aparezca alguien"), "f": ("inp", 1, 3, "Invita a alguien de su círculo"),
            "g": ("sys", -1, 4, "Busca otra vez"), "h": ("sys", 1, 4, "Envía el enlace de invitación"),
            "i": ("term", 0, 5, "Fin")},
         [("a", "b"), ("b", "c"), ("c", "d", None, "fan"), ("c", "e", None, "fan"), ("c", "f", None, "fan"), ("d", "g"), ("f", "h"),
          ("g", "b", None, "backl"), ("e", "i"), ("h", "i", None, "join")]),
        ("16", "Chat breve", "Match → Chat breve", {
            "a": ("term", 0, 0, "Confirmación mutua"), "b": ("proc", 0, 1, "Chat breve"),
            "c": ("dec", 0, 2, "¿Mensaje rápido o texto?"), "d": ("inp", -1, 3, "Elige un mensaje rápido"),
            "e": ("inp", 1, 3, "Escribe (sin fotos ni archivos)"), "f": ("dec", 0, 4, "¿Algo inapropiado?"),
            "g": ("term", 1, 4, "Reportar (F24)"), "h": ("sys", 0, 5, "El chat se borra 24 h después del trayecto"),
            "i": ("term", 0, 6, "Fin")},
         [("a", "b"), ("b", "c"), ("c", "d", "Rápido", "fan"), ("c", "e", "Texto", "fan"), ("d", "f", None, "join"), ("e", "f", None, "join"),
          ("f", "g", "Sí"), ("f", "h", "No"), ("h", "i")]),
    ]),
    ("TRAYECTO ACTIVO", [
        ("17", "Iniciar trayecto y encuentro", "Trayecto activo → Antes de salir y Encuentro  ·  Pregunta 3", {
            "a": ("term", 0, 0, "Iniciar trayecto"), "b": ("proc", 0, 1, "Antes de salir: compañía, contactos y punto de encuentro"),
            "c": ("inp", 0, 2, "Confirma a quién avisar esa noche"),
            "d": ("sys", 0, 3, "Activa la ubicación temporal y envía el enlace al contacto"),
            "e": ("inp", 0, 4, "Toca “Ya llegué” en el punto"), "f": ("dec", 0, 5, "¿La otra persona llegó en 10 min?"),
            "g": ("proc", 1, 5, "Espera 5 min, busca a otra persona o sigue con aviso"),
            "h": ("inp", 0, 6, "Confirman el código de encuentro"), "i": ("dec", 0, 7, "¿El código coincide?"),
            "j": ("term", 1, 7, "No viaja y reporta (F24)"), "k": ("term", 0, 8, "En curso (F18)")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f"), ("f", "g", "No"), ("f", "h", "Sí"), ("h", "i"),
          ("i", "j", "No"), ("i", "k", "Sí")]),
        ("18", "En curso y llegada", "Trayecto activo → En curso, Separación, Llegada y Retraso", {
            "a": ("term", 0, 0, "En curso"), "b": ("proc", 0, 1, "Mapa de ambas, tramo y tiempo de llegada"),
            "c": ("dec", 0, 2, "¿La compañía se baja antes?"), "d": ("sys", 1, 2, "Avisa: “Sigue sola desde Portal Sur”"),
            "e": ("dec", 0, 3, "¿Toca “Llegué” a tiempo?"), "f": ("sys", 0, 4, "Apaga la ubicación y avisa la llegada"),
            "g": ("term", 0, 5, "Confirmar trayecto (F24)"), "h": ("sys", 1, 3, "15 min tarde: “¿Todo bien?”"),
            "i": ("dec", 1, 4, "¿Responde en 5 min?"), "j": ("sys", 2, 4, "Avisa al contacto con la última ubicación"),
            "k": ("term", 2, 5, "El contacto llama o marca al 123")},
         [("a", "b"), ("b", "c"), ("c", "d", "Sí"), ("c", "e", "No"), ("d", "e", None, "join"), ("e", "f", "Sí"), ("f", "g"),
          ("e", "h", "No"), ("h", "i"), ("i", "j", "No"), ("j", "k"), ("i", "b", "Sí", "back")]),
        ("19", "Dejar de compartir y pedir ayuda", "Trayecto activo → En curso", {
            "a": ("term", 0, 0, "Durante el trayecto"), "b": ("dec", 0, 1, "¿Qué necesita?"),
            "c": ("inp", -1, 2, "Toca “Dejar de compartir”"), "d": ("inp", 1, 2, "Toca “¿Algo no está bien?”"),
            "e": ("dec", -1, 3, "¿Confirma?"), "f": ("sys", -1, 4, "Apaga la ubicación y avisa al contacto"),
            "g": ("term", -1, 5, "Sigue sin ubicación"), "h": ("term", -2, 3, "Sigue compartiendo"),
            "i": ("dec", 1, 3, "¿Qué elige?"), "j": ("term", 0.5, 4.3, "Abre el marcador con el 123"),
            "k": ("sys", 1.5, 4.3, "Alerta a sus contactos con la ubicación"), "l": ("term", 2.5, 4.3, "Reportar (F24)")},
         [("a", "b"), ("b", "c", None, "fan"), ("b", "d", None, "fan"), ("c", "e"), ("e", "f", "Sí"), ("f", "g"), ("e", "h", "No"),
          ("d", "i"), ("i", "j", None, "fan"), ("i", "k", None, "fan"), ("i", "l", None, "fan")]),
    ]),
    ("PERFIL", [
        ("20", "Perfil", "Perfil", {
            "a": ("term", 0, 0, "Perfil"), "b": ("dec", 0, 1, "¿Qué sección?"),
            "c": ("proc", -2, 2, "Perfil público"), "d": ("proc", -1, 2, "Preferencias (F22)"),
            "e": ("proc", 0, 2, "Contactos de confianza (F21)"), "f": ("proc", 1, 2, "Privacidad (F23)"),
            "g": ("proc", 2, 2, "Ajustes"), "h": ("term", 0, 3, "Inicio")},
         [("a", "b")] + [("b", k, None, "fan") for k in "cdefg"] + [(k, "h", None, "join") for k in "cdfg"] + [("e", "h")]),
        ("21", "Contactos de confianza", "Perfil → Contactos de confianza  ·  Pregunta 3", {
            "a": ("term", 0, 0, "Contactos de confianza"), "b": ("proc", 0, 1, "Lista de contactos (máx. 3)"),
            "c": ("proc", 0, 2, "Toca “Agregar contacto”"), "d": ("dec", 0, 3, "¿Permiso a la agenda?"),
            "e": ("inp", 0, 4, "Elige el contacto en la agenda"), "f": ("inp", 1, 3, "Escribe nombre y celular"),
            "g": ("inp", 0, 5, "Relación, canal (SMS o WhatsApp) y avisos"), "h": ("sys", 0, 6, "Envía la invitación al contacto"),
            "i": ("dec", 0, 7, "¿El contacto acepta?"), "j": ("proc", 1, 7, "Queda como “No aceptó”"),
            "k": ("dec", 0, 8, "¿Agregar otro?"), "l": ("inp", 0, 9, "Marca el contacto predeterminado"),
            "m": ("term", 0, 10, "Contactos listos")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e", "Sí"), ("d", "f", "No"), ("e", "g"), ("f", "g", None, "join"), ("g", "h"),
          ("h", "i"), ("i", "j", "No"), ("i", "k", "Sí"), ("k", "c", "Sí", "back"), ("k", "l", "No"), ("l", "m")]),
        ("22", "Preferencias de match", "Perfil → Preferencias de match", {
            "a": ("term", 0, 0, "Preferencias de match"), "b": ("inp", 0, 1, "Género: solo mujeres o cualquiera"),
            "c": ("inp", 0, 2, "Alcance: institución, círculo o ambos"), "d": ("inp", 0, 3, "Compañía: solo la espera o espera + trayecto"),
            "e": ("sys", 0, 4, "Recalcula personas compatibles"), "f": ("term", 0, 5, "Perfil")},
         [("a", "b"), ("b", "c"), ("c", "d"), ("d", "e"), ("e", "f")]),
        ("23", "Privacidad", "Perfil → Privacidad", {
            "a": ("term", 0, 0, "Privacidad"), "b": ("dec", 0, 1, "¿Qué quieres hacer?"),
            "c": ("proc", -1, 2, "Personas bloqueadas: desbloquear"), "d": ("sys", 0, 2, "Genera el archivo con sus datos"),
            "e": ("dec", 1, 2, "¿Confirma eliminar la cuenta?"), "f": ("sys", 1, 3, "Borra datos, rutas y avales"),
            "g": ("term", 1, 4, "Ingreso (F01)"), "h": ("term", 2, 2, "Cancela"), "i": ("term", -0.5, 3.4, "Perfil")},
         [("a", "b"), ("b", "c", None, "fan"), ("b", "d", None, "fan"), ("b", "e", None, "fan"), ("e", "f", "Sí"), ("f", "g"),
          ("e", "h", "No"), ("c", "i", None, "join"), ("d", "i", None, "join")]),
    ]),
    ("CONFIANZA Y CONTACTO AVISADO", [
        ("24", "Confirmar trayecto y reportar", "Confianza", {
            "a": ("term", 0, 0, "Termina el trayecto"), "b": ("dec", 0, 1, "¿Se encontraron?"),
            "c": ("inp", 1, 1, "Marca “No se presentó”"), "d": ("term", 1, 2, "Registra la ausencia (3 = advertencia)"),
            "e": ("inp", 0, 2, "Confirma el trayecto"), "f": ("inp", 0, 3, "¿Volverías a viajar? (privado)"),
            "g": ("dec", 0, 4, "¿Algo que reportar?"), "h": ("sys", 0, 5, "Suma un trayecto y borra las ubicaciones"),
            "i": ("term", 0, 6, "Fin"), "j": ("inp", 1, 4, "Motivo y descripción"),
            "k": ("sys", 1, 5, "Bloquea a la persona y envía a moderación"), "l": ("dec", 1, 6, "¿Moderación confirma?"),
            "m": ("sys", 1, 7, "Suspende la cuenta y revisa sus avales"), "n": ("sys", 2, 6, "Deja una advertencia interna"),
            "o": ("term", 1, 8, "Informa el resultado a quien reportó")},
         [("a", "b"), ("b", "c", "No"), ("c", "d"), ("b", "e", "Sí"), ("e", "f"), ("f", "g"), ("g", "h", "No"), ("h", "i"),
          ("g", "j", "Sí"), ("j", "k"), ("k", "l"), ("l", "m", "Sí"), ("l", "n", "No"), ("m", "o"), ("n", "o", None, "join")]),
        ("25", "Vista del contacto avisado", "Vista del contacto (web, sin app)", {
            "a": ("term", 0, 0, "Recibe la invitación"), "b": ("dec", 0, 1, "¿Acepta recibir avisos?"),
            "c": ("term", 1, 1, "No recibe avisos"), "d": ("sys", 0, 2, "Llega un enlace cuando Daniela inicia un trayecto"),
            "e": ("proc", 0, 3, "Web: con quién va, mapa en vivo y hora estimada"), "f": ("dec", 0, 4, "¿Qué aviso llega?"),
            "g": ("sys", -1, 5, "Llegada: “Daniela llegó”"), "h": ("proc", 0, 5, "Separación: sigue viendo el trayecto"),
            "i": ("proc", 1, 5, "Retraso: última ubicación conocida"), "j": ("term", -1, 6, "El enlace caduca"),
            "k": ("term", 1, 6, "Llama a Daniela o al 123")},
         [("a", "b"), ("b", "c", "No"), ("b", "d", "Sí"), ("d", "e"), ("e", "f"), ("f", "g", None, "fan"), ("f", "h", None, "fan"),
          ("f", "i", None, "fan"), ("g", "j"), ("i", "k"), ("h", "e", None, "back")]),
    ]),
]


def size(t, txt):
    if t == "dec":
        lines = wrap(txt, FS, 700, NW * 0.55)
        return NW, max(96, len(lines) * FS * 1.25 * 2 + 30)
    lines = wrap(txt, FS, 700 if t == "term" else 400, NW - 36)
    return NW, max(46, len(lines) * FS * 1.3 + 22)


def draw_node(s, t, x, y, w, h, txt):
    fill, _ = STY[t]
    cx, cy = x + w / 2, y + h / 2
    bold = t in ("term", "dec")
    if t == "dec":
        s.poly([(cx, y), (x + w, cy), (cx, y + h), (x, cy)], fill)
        lines = wrap(txt, FS, 700, w * 0.55)
    elif t == "term":
        s.rect(x, y, w, h, fill, r=min(h / 2, 22))
        lines = wrap(txt, FS, 700, w - 36)
    elif t == "inp":
        k = 16
        s.poly([(x + k, y), (x + w, y), (x + w - k, y + h), (x, y + h)], fill)
        lines = wrap(txt, FS, 400, w - 36)
    elif t == "sys":
        e = 9
        s.pathd(f"M {x} {y + e} A {w / 2} {e} 0 0 1 {x + w} {y + e} L {x + w} {y + h - e} A {w / 2} {e} 0 0 1 {x} {y + h - e} Z", fill)
        s.pathd(f"M {x} {y + e} A {w / 2} {e} 0 0 0 {x + w} {y + e}", "none", stroke="#9AD9AE", sw=1.5)
        lines = wrap(txt, FS, 400, w - 36)
    else:
        s.rect(x, y, w, h, fill, r=4)
        lines = wrap(txt, FS, 400, w - 36)
    th = len(lines) * FS * 1.3
    s.text(cx, cy - th / 2 + 1, "\n".join(lines), FS, 700 if bold else 400, DARK, lh=1.3, center=True)


def layout(nodes):
    sizes = {k: size(v[0], v[3]) for k, v in nodes.items()}
    rows = sorted({v[2] for v in nodes.values()})
    rowh = {r: max(sizes[k][1] for k, v in nodes.items() if v[2] == r) for r in rows}
    rowy, y = {}, 0
    prev = None
    for r in rows:
        if prev is not None and r - prev < 1:
            y -= VG * 0.3
        rowy[r] = y
        y += rowh[r] + VG
        prev = r
    minc = min(v[1] for v in nodes.values())
    box = {}
    for k, (t, c, r, txt) in nodes.items():
        w, h = sizes[k]
        box[k] = ((c - minc) * CP, rowy[r] + (rowh[r] - h) / 2, w, h)
    width = (max(v[1] for v in nodes.values()) - minc) * CP + NW
    return box, width, y - VG


def draw_flow(s, ox, oy, flow):
    code, title, arch, nodes, edges = flow
    box, fw, fh = layout(nodes)
    lanes = 70
    cw = max(fw + lanes + 40, 360)
    head = 26 + 22 * 1.2 + 8 + text_h(arch, 13, 400, cw - 48, 1.3, mono=True) + 26
    total_h = head + fh + 40
    s.g(f"F{code} · {title}")
    s.rect(ox, oy, cw, total_h, "#FFFFFF", stroke="#E4E4E7", sw=2, r=20)
    s.text(ox + 24, oy + 26, f"F{code} · {title}", 22, 700, DARK, maxw=cw - 48, lh=1.2)
    s.text(ox + 24, oy + 26 + 22 * 1.2 + 8, arch, 13, 400, "#71717A", maxw=cw - 48, lh=1.3, mono=True)
    bx, by = ox + 20, oy + head
    B = {k: (x + bx, y + by, w, h) for k, (x, y, w, h) in box.items()}

    def anc(k, side):
        x, y, w, h = B[k]
        return {"l": (x, y + h / 2), "r": (x + w, y + h / 2), "t": (x + w / 2, y), "b": (x + w / 2, y + h)}[side]

    labels = []
    for e in edges:
        a, b = e[0], e[1]
        lab = e[2] if len(e) > 2 else None
        st = e[3] if len(e) > 3 else None
        (_, ca, ra, _), (_, cb, rb, _) = nodes[a], nodes[b]
        if st is None:
            if ca == cb and rb > ra:
                st = "v"
            elif ra == rb:
                st = "h"
            elif rb > ra:
                st = "hv"
            else:
                st = "back"
        if st == "v":
            p = [anc(a, "b"), anc(b, "t")]
        elif st == "h":
            p = [anc(a, "r"), anc(b, "l")] if cb > ca else [anc(a, "l"), anc(b, "r")]
        elif st == "hv":
            s0 = anc(a, "r") if cb > ca else anc(a, "l")
            t0 = anc(b, "t")
            p = [s0, (t0[0], s0[1]), t0]
        elif st in ("fan", "join"):
            s0, t0 = anc(a, "b"), anc(b, "t")
            my = (s0[1] + t0[1]) / 2 if st == "fan" else t0[1] - 22
            if st == "fan":
                my = s0[1] + 22
            p = [s0, (s0[0], my), (t0[0], my), t0] if abs(s0[0] - t0[0]) > 1 else [s0, t0]
        elif st in ("back", "back2"):
            s0, t0 = anc(a, "r"), anc(b, "r")
            lane = max(B[a][0] + B[a][2], B[b][0] + B[b][2]) + (22 if st == "back" else 40)
            p = [s0, (lane, s0[1]), (lane, t0[1]), t0]
        elif st == "backl":
            s0, t0 = anc(a, "l"), anc(b, "l")
            lane = min(B[a][0], B[b][0]) - 22
            p = [s0, (lane, s0[1]), (lane, t0[1]), t0]
        s.arrow(p, ARROW, 2, hs=9)
        if lab:
            (x1, y1), (x2, y2) = p[0], p[1]
            if st == "fan":
                (x1, y1), (x2, y2) = p[-2], p[-1]
                labels.append((x2 + 6, y1 + 4, lab))
            elif abs(x2 - x1) >= abs(y2 - y1):
                labels.append(((x1 + 8) if x2 > x1 else (x1 - 8 - measure(lab, 13, 700)), y1 - 20, lab))
            else:
                labels.append((x1 + 8, y1 + 4, lab))
    for k, (t, c, r, txt) in nodes.items():
        draw_node(s, t, *B[k], txt)
    for lx, ly, lab in labels:
        s.text(lx, ly, lab, 13, 700, "#3F3F46")
    s.endg()
    return cw, total_h


def build_group(path, idx, name, flows):
    s = Svg(100, None, BG)
    s.text(60, 50, f"04 · USER FLOWS · {idx} DE {len(FLUJOS)}", 18, 700, "#084FE9", mono=True, ls=0.06)
    s.text(60, 82, name.capitalize(), 48, 700, DARK)
    x, y0 = 60, 170
    hmax = 0
    for f in flows:
        w, h = draw_flow(s, x, y0, f)
        x += w + 50
        hmax = max(hmax, h)
    s.w = int(x + 10)
    s.save(path, y0 + hmax + 60)


def build_legend(path):
    s = Svg(1500, 560, BG)
    s.text(60, 50, "04 · USER FLOWS", 18, 700, "#084FE9", mono=True, ls=0.06)
    s.text(60, 82, "User flows por funcionalidad", 48, 700, DARK)
    s.text(60, 150, "25 flujos, uno por proceso. Cada uno indica en qué parte de la arquitectura ocurre y se lee de arriba hacia abajo, de la cápsula gris de inicio a la de cierre.",
           20, 400, "#52525B", maxw=1380, lh=1.4)
    items = [("term", "Inicio / fin"), ("proc", "Pantalla o proceso"), ("inp", "El usuario ingresa datos"),
             ("sys", "El sistema valida o consulta"), ("dec", "Decisión (Sí / No)")]
    x = 60
    for t, lab in items:
        draw_node(s, t, x, 240, 200, 96 if t == "dec" else 60, "")
        s.text(x, 360, lab, 18, 700, DARK, maxw=230)
        x += 280
    s.text(60, 430, "Índice: 01–04 Acceso · 05–08 Verificación · 09–12 Inicio y Mis rutas · 13–16 Matches · 17–19 Trayecto activo · "
           "20–23 Perfil · 24–25 Confianza y contacto avisado", 18, 400, "#52525B", maxw=1380, lh=1.4, mono=True)
    s.save(path)


if __name__ == "__main__":
    import os
    import sys
    d = sys.argv[1]
    os.makedirs(d, exist_ok=True)
    build_legend(os.path.join(d, "F00.svg"))
    for i, (name, flows) in enumerate(FLUJOS, 1):
        fn = os.path.join(d, f"F{i:02d}g.svg")
        build_group(fn, i, name, flows)
        print(fn, os.path.getsize(fn))
