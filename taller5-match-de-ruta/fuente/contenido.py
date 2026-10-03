"""Contenido de la entrega: arquitectura y flujos (datos, sin diagramación)."""


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



# ---------------------------------------------------------------- BENCHMARKING
BENCH_COLS = [("Moovit", "Informa"), ("Google Maps", "Ubica y guía"), ("Uber", "Transporta"), ("Life360", "Vigila"),
              ("bSafe", "Reacciona"), ("Waze Carpool", "Carro compartido · cerró en 2022"), ("Match", "Acompaña")]

# Estados: S = sí, P = parcial, N = no, V = por verificar, T = texto. "*" = depende del país o del plan; por confirmar.
BENCH_ROWS = [
    ("G", "MOVILIDAD"),
    ("Planear ruta en transporte público", "Combina buses, troncales y caminatas",
     ["S", "S", "P|Solo en algunas ciudades*", "N", "N", "N|Ruta en carro", "N|Usa la ruta que ya conoce"]),
    ("Tiempos de llegada en tiempo real", "Cuándo llega el bus o el alimentador",
     ["S", "P|Según los datos de la ciudad", "N", "N", "N", "N", "P|Capa secundaria (Could)"]),
    ("Alertas de servicio", "Desvíos, cierres o retrasos",
     ["S", "P|Según la ciudad", "N", "N", "N", "N", "N"]),
    ("G", "UBICACIÓN Y AVISOS"),
    ("Compartir ubicación en vivo", "Otra persona ve dónde estás",
     ["P|SafeRide, solo con Moovit+ (pago)*", "S|Con contactos", "S|Solo durante el viaje", "S|Siempre, en el círculo", "S|Follow Me", "V*", "S|Solo durante el trayecto"]),
    ("Ubicación que se apaga sola", "El permiso caduca sin que lo apagues",
     ["V*", "S|Eliges la duración", "S|Termina con el viaje", "N|Activa todo el tiempo", "P|Se apaga a mano*", "V*", "S|Se apaga al llegar"]),
    ("Aviso de llegada a contactos", "Saben que llegaste sin preguntar",
     ["P|SafeRide: ven el avance y la hora estimada*", "P|Comparte el avance del viaje", "P|Ven que el viaje terminó", "S|Alerta al llegar a un lugar", "P|Alarma si no confirmas a tiempo (premium)", "N", "S|Aviso automático"]),
    ("Sin historial de ubicaciones", "No queda registro de tus movimientos",
     ["V*", "P|Cronología opcional", "N|Guarda los viajes", "N|De 2 a 30 días según el plan", "V*", "V*", "S|Se borra al llegar"]),
    ("G", "SEGURIDAD Y RESPUESTA"),
    ("Botón SOS / emergencia", "Pedir ayuda en un momento crítico",
     ["N", "N", "S|Durante el viaje", "S|Alerta SOS; más respuesta en planes pagos", "S|A sus guardianes", "N", "P|Atajo al 123 (propuesta)"]),
    ("Grabar o transmitir evidencia", "Audio o video como respaldo",
     ["N", "N", "P|Audio, en algunos países", "N", "S|Video y audio (premium)", "N", "N|Fuera del MVP"]),
    ("Llamada falsa", "Excusa para salir de una situación",
     ["N", "N", "N", "N", "S", "N", "N"]),
    ("G", "IDENTIDAD Y CONFIANZA"),
    ("Identidad verificada de la otra persona", "Sabes quién es antes de verla",
     ["N|No aplica", "N|Tus contactos", "S|Conductor verificado", "P|Conocidos, sin verificar", "P|Conocidos, sin verificar", "P|Correo laboral opcional*", "S|Correo institucional o avales"]),
    ("Verificación por institución", "Universidad o empresa como filtro",
     ["N", "N", "N", "N", "N", "S|Filtro de compañeros de trabajo o de clase", "S|Correo institucional"]),
    ("Red de confianza elegida", "Contactos que tú escoges",
     ["P|Contactos de seguridad (Moovit+)", "S|Contactos", "S|Contactos de confianza", "S|Círculos", "S|Guardianes", "N", "S|Círculo + contactos avisados"]),
    ("Calificación o reporte de personas", "Consecuencias por mal comportamiento",
     ["N", "N", "S|Calificación mutua", "N", "N", "S|Calificación con estrellas", "S|Confirmación + reporte"]),
    ("Preferencia de género", "Elegir con quién te emparejan",
     ["N", "N", "P|Women Preferences, en algunos países", "N", "N", "S|Filtro por género", "S|Solo mujeres / cualquiera"]),
    ("G", "ACOMPAÑAMIENTO"),
    ("Emparejamiento por ruta y horario", "Conecta personas que van al mismo lado",
     ["N", "N", "P|UberX Share: desconocidos, en carro*", "N", "N", "S|En carro", "S|En transporte público"]),
    ("Compañía física en espera y trayecto", "Alguien real a tu lado en el paradero",
     ["N", "N", "N|Te saca del transporte público", "N", "P|Solo virtual", "N", "S|Persona verificada"]),
    ("Chat entre usuarios", "Coordinar el encuentro",
     ["N", "N", "S|Con el conductor", "V*", "N", "V*", "S|Tras confirmación mutua"]),
    ("G", "MODELO"),
    ("Costo para quien la usa", "",
     ["T|Gratis + Moovit+", "T|Gratis", "T|Pago por viaje", "T|Gratis + planes", "T|Gratis + premium", "T|Costo compartido", "T|Gratis (propuesta)"]),
]

HALLAZGOS = [
    ("Cada app resuelve una parte: informar, transportar o reaccionar.",
     "Moovit y Google Maps informan; Uber y Waze Carpool transportan; Life360 y bSafe vigilan o reaccionan. Ninguna pone a otra persona al lado de quien viaja en transporte público.",
     "Ahí entra Match: empareja a personas que ya hacen el mismo recorrido."),
    ("Compartir la ubicación ya es algo común.",
     "5 de las 6 apps lo tienen. Moovit lo agregó con SafeRide, dentro de su plan pago.",
     "En Match la ubicación solo se comparte durante el trayecto, se apaga al llegar y no queda historial."),
    ("Las apps generan confianza de dos formas y ninguna usa las dos.",
     "Life360 y bSafe se apoyan en gente conocida, sin verificar identidad. Uber verifica a sus conductores, pero no a tu red.",
     "Match usa las dos: correo institucional y avales del círculo cercano."),
    ("Emparejar personas por ruta ya existe, pero en carro.",
     "UberX Share empareja pasajeros que no se conocen. Waze Carpool filtraba por empresa, universidad y género; Google lo cerró en 2022 porque cambiaron los hábitos de viaje después de la pandemia.",
     "Los filtros funcionaron. El riesgo es que no haya suficientes personas en la misma ruta y hora."),
    ("Las apps de seguridad actúan cuando el riesgo ya ocurrió.",
     "El SOS, la grabación y la llamada falsa (bSafe, Uber) sirven durante o después de un incidente.",
     "Match busca que la persona no esté sola antes de que pase algo (insight 03). Para emergencias deja un atajo al 123."),
    ("Ninguna de las 6 cubre la espera en el paradero.",
     "Esperar el alimentador de noche es el momento de más tensión y no tiene una función propia en ninguna app.",
     "Match empareja desde el paradero de salida, así que la espera también se hace acompañada."),
]

OPORTUNIDAD = "Los 5 entrevistados usan apps de rutas y aun así sienten miedo. La oportunidad está en que nadie tenga que esperar ni viajar solo de noche."
PROPUESTA = ("Para estudiantes y trabajadores que dependen del transporte público de noche, Match de ruta verificado los conecta con personas "
             "verificadas de su universidad, su trabajo o su círculo cercano que hacen el mismo trayecto a la misma hora, para que no esperen ni viajen solos.")
PROPUESTA_VS = [
    ("vs. Life360 y bSafe", "Avisan o alertan a tus contactos. Match busca que no viajes sin compañía."),
    ("vs. Uber", "Uber te saca del transporte público y cobra cada viaje. Match funciona dentro del transporte público y es gratis."),
    ("vs. Waze Carpool", "Emparejaba viajes en carro. Match empareja tramos de transporte público."),
    ("vs. Moovit y Google Maps", "Dan rutas y horarios, y Moovit deja compartir el viaje. Lo que no dan es compañía."),
]

DIFERENCIACION = [
    ("TOMO", "Lo que ya funciona en otras apps", [
        "Círculos de confianza → Life360",
        "Viaje compartido que termina solo → Uber y Google Maps",
        "Contacto que sigue el viaje sin instalar la app → Moovit (SafeRide)",
        "Calificación y reporte → Uber",
        "Filtros por institución y género → Waze Carpool",
    ]),
    ("EVITO", "Lo que genera desconfianza", [
        "Ubicación permanente e historial (Life360)",
        "Emparejar a desconocidos (UberX Share)",
        "Cobrar por sentirse seguro (Uber, planes pagos)",
        "Actuar solo cuando ya pasó algo (bSafe)",
    ]),
    ("SOLO MATCH", "No lo encontré en ninguna de las 6", [
        "Emparejar por tramo de transporte público y horario",
        "Verificación doble: institución + avales",
        "Compañía física en la espera del paradero",
    ]),
]

RIESGOS = [
    ("Masa crítica", "Si no hay personas en la misma ruta y hora, la app no sirve.",
     "Lanzar en una universidad piloto, emparejar por tramo y usar un rango de ±15 min."),
    ("Suplantación", "Alguien se hace pasar por otra persona en el encuentro.",
     "Foto tomada en el momento, código de encuentro y reporte con bloqueo inmediato."),
    ("Exponer la rutina", "Que alguien sepa a qué hora sale y dónde vive.",
     "Sin destino exacto, apellido ni celular: solo el tramo en común, y solo para personas compatibles."),
]

# ---------------------------------------------------------------- MVP (tomado de la presentación: 16 ideas, MoSCoW y MVP)
MVP_FRASE = "Una app para emparejarte con alguien verificado que hace tu mismo trayecto de noche."
MVP_PARRAFO = ("Match de ruta verificado conecta a personas verificadas que hacen el mismo trayecto en transporte público a la misma hora. "
               "Para entrar, cada persona se verifica con su correo institucional o con dos avales de su círculo cercano. Después guarda su ruta "
               "y su horario, y la app le muestra quién de su universidad, su trabajo o su círculo sale a esa hora por el mismo tramo. "
               "Cuando las dos aceptan, se encuentran en el paradero y comparten la ubicación solo mientras dura el trayecto. Al llegar, se apaga sola.")
MVP_PILARES = [
    ("REGISTRO", "Correo institucional o círculo cercano", "Ideas 01 y 11", "Ingreso · Verificación", "F01–F08"),
    ("MATCH", "Misma ruta, mismo horario", "Ideas 02 y 03", "Mis rutas · Matches · Match", "F10–F14"),
    ("TRAYECTO", "Ubicación en vivo que se apaga al llegar", "Idea 04", "Trayecto activo", "F17–F18"),
]
MOSCOW = [
    ("MUST", "Entra en el MVP", [("01 · 11", "Registro verificado"), ("02", "Ruta y horario"), ("03", "Emparejamiento automático"), ("04", "Ubicación en vivo temporal")]),
    ("SHOULD", "Segunda versión", [("05", "Dejar de compartir"), ("09", "Aviso a contacto"), ("06", "Preferencia de género"), ("12", "Reporte de conducta")]),
    ("COULD", "Si hay tiempo", [("07", "Chat para coordinar"), ("08", "Confirmación mutua"), ("14", "Solo acompañar la espera"), ("16", "Tiempos de llegada")]),
    ("WON'T", "No se hará", [("10", "Historial de ubicaciones"), ("15", "Reverificación periódica"), ("13", "Sugerir hora de salida")]),
]
MOSCOW_AJUSTES = [
    ("05 Dejar de compartir → Must", "Fue mi respuesta a la retro sobre el riesgo de compartir la ubicación. Sin este botón, el MVP no cumple esa promesa."),
    ("08 Confirmación mutua → Must", "Sin que las dos personas acepten, el emparejamiento automático conectaría a alguien sin su permiso."),
    ("Nuevas: código de encuentro y atajo al 123", "Salen del benchmarking y de los riesgos. Propongo el código como Should y el atajo al 123 como Could."),
]

# ---------------------------------------------------------------- PERSONA
# [E] = dato de las 5 entrevistas · [S] = supuesto para completar el perfil
PERSONA_FICHA = {
    "nombre": "Daniela Gómez, 22 años",
    "linea": "Estudiante de Comunicación Social · Vive en Bosa y estudia en Chapinero (Bogotá) · Sale de clase a las 9:00 p. m. martes y jueves · Viaja sola en troncal y alimentador",
    "cita": "“La app me informa, pero no me protege.”",
}
PERSONA_BLOQUES_1 = [
    ("QUIÉN ES", [
        "22 años, 8.º semestre de Comunicación Social [S]",
        "Vive con su mamá y su hermano menor en Bosa [S]",
        "Práctica de medio tiempo en las mañanas; clases de 6 a 9 p. m. martes y jueves [S]",
        "No tiene carro ni moto: depende del transporte público [E]",
        "Celular Android de gama media con plan prepago: cuida la batería y los datos [S]",
    ]),
    ("SU CONTEXTO", [
        "Su trayecto dura cerca de 1 h 40 min: una troncal y un alimentador [S]",
        "Hace el tramo más largo de pie y con el celular guardado [S]",
        "Espera el alimentador en un paradero con poca luz que se va quedando vacío [E]",
        "En su curso hay gente que sale a la misma hora, pero no sabe quién va hacia el sur [S]",
        "Una vez la siguieron al bajarse del bus [E]",
    ]),
    ("TECNOLOGÍA QUE USA", [
        "App de rutas y horarios del transporte, como los 5 entrevistados [E]",
        "Google Maps cuando va a un lugar nuevo [E]",
        "Comparte su ubicación con su mamá; 2 de 5 entrevistados lo hacen siempre [E]",
        "Escucha música cuando hay gente; cuando se queda sola, la apaga y guarda el celular [E]",
        "Maneja bien el celular; lo que pide son reglas claras de privacidad [S]",
    ]),
]
PERSONA_TRAYECTO = [
    ("9:00 p. m.", "Sale de clase", "Revisa en la app cuándo pasa la troncal.", 1, "Tranquila"),
    ("9:05 p. m.", "Camina a la estación", "8 minutos por una calle con poca luz. Se quita un audífono.", 3, "Alerta"),
    ("9:15 p. m.", "Troncal", "40 minutos de pie. Hay gente; guarda el celular en la maleta.", 2, "Atenta"),
    ("9:55 p. m.", "Llega al portal", "Busca el paradero del alimentador; cada vez hay menos gente.", 3, "Tensa"),
    ("10:00 p. m.", "Espera el alimentador", "De 10 a 20 min sin saber cuánto tarda. Se para cerca de la luz y de otras personas.", 4, "Máxima tensión"),
    ("10:30 p. m.", "Camina a casa", "6 minutos a pie. Mira hacia atrás varias veces.", 4, "Miedo"),
    ("10:40 p. m.", "Llega a casa", "Le escribe “llegué” a su mamá y apaga la ubicación, si se acuerda.", 1, "Alivio"),
]
PERSONA_BLOQUES_2 = [
    ("NECESIDADES", [
        "Saber quién de su universidad hace su mismo tramo a la misma hora [E]",
        "Que su mamá sepa que llegó sin tener que escribirle [E]",
        "No estar sola mientras espera el alimentador [E]",
        "Que la otra persona esté verificada y, si lo prefiere, sea mujer [E]",
        "Que nadie conozca su dirección ni su rutina completa [S]",
    ]),
    ("CÓMO SE COMPORTA", [
        "Revisa la app de rutas antes de salir, aunque eso no le quita el miedo [E]",
        "Elige dónde esperar por la luz, la cercanía y la gente, no por una app [E]",
        "Guarda el celular y se pone alerta cuando el paradero se vacía [E]",
        "Comparte la ubicación, pero a veces se le olvida apagarla [S]",
        "Pregunta en el grupo del curso “¿alguien va para el sur?”, pero casi nunca coincide [S]",
    ]),
    ("FRUSTRACIONES", [
        "La app le da horarios, pero no tranquilidad [E]",
        "No le alcanza para pedir un carro todas las noches [S]",
        "Compartir la ubicación es manual y se queda activa de más [S]",
        "No confía en desconocidos [E]",
        "Los grupos de WhatsApp no sirven para coordinar a última hora [S]",
    ]),
]
PERSONA_BLOQUES_3 = [
    ("MOTIVACIONES", [
        "No estar sola en el momento en que más expuesta se siente [E]",
        "Terminar la carrera sin evitar las materias de la noche [S]",
        "No depender de que alguien la recoja [S]",
        "Que su mamá esté tranquila [E]",
    ]),
    ("MIEDOS", [
        "Violencia sexual: lo mencionaron las 3 mujeres entrevistadas [E]",
        "Que la roben o la agredan en el bus o en el paradero [E]",
        "Que la sigan al bajarse del bus [E]",
        "Que una app muestre su ubicación a quien no debe [S]",
    ]),
    ("SITUACIONES QUE CAMBIAN SUS DECISIONES", [
        "Si se le hace tarde, cambia de plan: pide un carro o se queda donde una amiga; 4 de 5 entrevistados lo han hecho [E]",
        "Si llueve, el paradero se vacía más rápido [S]",
        "Con menos del 20 % de batería deja de compartir la ubicación [S]",
        "Si va con alguien conocido, se queda estudiando hasta tarde [S]",
        "En semana de parciales sale más tarde [S]",
        "A fin de mes revisa si le alcanza para un carro [S]",
    ]),
]
PERSONA_ESCENARIO = (
    "Martes, 8:40 p. m. Daniela abre Match: 2 personas de su universidad salen entre las 9:00 y las 9:15 hacia el portal. "
    "Revisa el perfil de Laura (verificada con correo institucional, 14 trayectos acompañados, comparten 2 de 3 tramos) y le envía una solicitud. "
    "Laura acepta. Se encuentran en la entrada de la estación y confirman el código “Naranja-12”. Su mamá recibe un enlace por WhatsApp "
    "y sigue el trayecto sin instalar nada. En el portal, Laura espera con ella hasta que llega el alimentador. A las 10:40 Daniela llega a su casa "
    "y toca “Llegué”: la ubicación se apaga y su mamá recibe el aviso.")
PERSONAS_SEC = [
    ("Gloria, 49", "PERSONA SECUNDARIA · CONTACTO AVISADO", "Mamá de Daniela", [
        "Trabaja de día y espera despierta a que Daniela llegue [S]",
        "Si son las 10:30 y no sabe nada, la llama; Daniela no contesta porque guardó el celular [S]",
        "Quiere saber con quién va, si algo cambió y que llegó, sin tener que llamar [E]",
        "No quiere instalar otra app ni aprender a usarla [S]",
    ], "Los avisos le llegan por SMS o WhatsApp con un enlace web. No necesita la app."),
    ("Daniel, 21", "SEGMENTO COMPLEMENTARIO · HOMBRES", "Estudiante", [
        "Sale de noche del trabajo o de la universidad [E]",
        "Su miedo principal es el robo, no la violencia sexual; así respondieron los 2 hombres [E]",
        "Va alerta, no saca el celular y a veces cambia de ruta [E]",
        "Quiere no ir solo en los tramos de riesgo y ayudar a alguien de su comunidad [S]",
    ], "La preferencia de género es opcional: puede acompañar a quien lo acepte."),
]
