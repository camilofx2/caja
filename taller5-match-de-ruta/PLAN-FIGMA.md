# Plan de construcción en Figma · Match de ruta verificado

Documento consolidado para montar la entrega directamente en Figma apenas se libere el acceso.
Todo el contenido ya está redactado en `fuente/contenido.py`. Aquí está la estructura, adaptada a la referencia de la profe.

---

## 1. Qué hace falta para trabajar directamente en Figma

| Causa del bloqueo | Detalle verificado (documentación de Figma) |
|---|---|
| Límite de la conexión de Figma con Claude | Plan **Starter: hasta 20 llamadas al mes**, por cuenta. Ya se usaron. |
| ¿Se arregla usando Cowork desde la Mac? | **No.** El límite es de la cuenta de Figma, no del equipo. Cowork usa la misma conexión. |
| Plan **Education** (gratis para estudiantes verificados) | **Hasta 200 llamadas al día**. Es suficiente para construir todo (se necesitan unas 40–60). |
| Plan Professional con asiento Full o Dev (pago) | También da 200 al día. |

**Recomendación:** solicitar el plan Education de Figma con el correo de Taller 5 (figma.com/education). Cuando esté aprobado:
1. Reconectar Figma en Claude, si lo pide.
2. Volver a esta conversación (o a Cowork) y decir “ya tengo Figma Education, constrúyelo”.
3. Se construye todo en la página **“Entrega · Definición del producto”**, que ya existe en el archivo.

**Plan B sin límite (Mac, Figma de escritorio):** un plugin local de desarrollo que construye todo con un clic
(Plugins → Development → Import plugin from manifest). No pasa por el límite. Si se quiere esta vía, hay que pedir que se prepare el plugin.

---

## 2. Lo que muestra la referencia y cómo se adapta

| En la referencia | Cómo queda en Match de ruta |
|---|---|
| Benchmarking en lámina con tabla de ✓ y ✗, partida en 2 láminas | 2 láminas de tabla (19 funcionalidades) con ✓ / ✗ / ◐ (parcial) / ? (por verificar), en el azul de tu presentación |
| Lámina “Conclusión · ¿Qué encontré?” | Lámina de conclusión con los 6 hallazgos |
| Lámina “Oportunidad de diseño” | Lámina con la propuesta de valor y la comparación frente a cada competidor |
| User persona en una lámina + “completo en documento adjunto” | 1 lámina resumen (como la referencia) + 4 láminas de detalle (lo que pidió la profe) |
| Arquitectura: árbol de arriba hacia abajo, cápsulas de color por sección, flechas | Mismo formato: INGRESO → VERIFICACIÓN → INICIO → 4 pestañas → MATCH → TRAYECTO ACTIVO → CONFIANZA + vista del contacto |
| User flows: uno por cada nodo de la arquitectura, verticales, unos 25 | 25 flujos verticales, uno por nodo, con la misma notación |

**Notación de los flujos (igual a la referencia):**

| Forma | Significa | Color en la referencia |
|---|---|---|
| Cápsula | Inicio / fin del flujo | Gris |
| Rectángulo | Pantalla o proceso | Morado claro |
| Paralelogramo | El usuario ingresa datos | Azul claro |
| Cilindro | El sistema valida o consulta datos | Verde claro |
| Rombo | Decisión (Sí / No) | Naranja claro |

> Para la arquitectura y los flujos se recomienda el fondo claro con cuadrícula de puntos, como la referencia, porque son tableros de trabajo.
> El azul de tu presentación se usa en las láminas (benchmarking, conclusión, oportunidad y persona).

---

## 3. Estructura de la página en Figma

| Sección | Frames | Formato |
|---|---|---|
| 01 · Benchmarking | B1 Tabla (1/2) · B2 Tabla (2/2) · B3 Conclusión · B4 Oportunidad de diseño · B5 Diferenciación y riesgos | Láminas 1920 × 1080, estética azul |
| 02 · User persona | P1 Resumen · P2 Contexto · P3 Trayecto y tensión · P4 Necesidades, comportamiento y frustraciones · P5 Motivaciones, miedos y situaciones · P6 Escenario y personas secundarias | Láminas 1920 × 1080, estética azul |
| 03 · Arquitectura | A1 Árbol completo · A2 Las 4 preguntas de la profe | Tablero claro (A1) + lámina azul (A2) |
| 04 · User flows | F00 Notación e índice + 25 flujos | Tablero claro, flujos verticales en filas por sección |

**Estética de las láminas (tomada de tu archivo):** fondo `#084FE9`, acento `#FFB81C`, texto blanco · Space Grotesk Bold para títulos, Space Mono para etiquetas ·
etiqueta de sección arriba a la izquierda (ej. `04 · ANALIZAR`), “Match de ruta verificado” arriba a la derecha, número `16 / 30` abajo a la derecha y la línea de puntos de avance.

---

## 4. Contenido de las láminas

### B1–B2 · Benchmarking
Columnas: Moovit · Google Maps · Uber · Life360 · bSafe · Waze Carpool (cerró en 2022) · **Match**.
- **B1:** Movilidad (3) · Ubicación y avisos (4) · Seguridad y respuesta (3)
- **B2:** Identidad y confianza (5) · Acompañamiento (3) · Modelo (1)
- Texto completo de cada celda: `BENCH_ROWS` en `fuente/contenido.py`. Las celdas con `*` se verifican antes de entregar.

### B3 · Conclusión · ¿Qué encontré?
1. El mercado se divide en informar, transportar y reaccionar; ninguna acompaña.
2. Compartir ubicación ya es estándar; el diferencial es que sea temporal y sin historial.
3. La confianza se construye de dos maneras y ninguna app las combina.
4. El emparejamiento por ruta existe, pero en carro (UberX Share, Waze Carpool).
5. Las apps de seguridad actúan cuando el riesgo ya ocurrió.
6. Nadie diseña para la espera en el paradero.

### B4 · Oportunidad de diseño
> “No se trata de dar más información sobre el bus. Se trata de que nadie tenga que esperar ni viajar solo.”

Propuesta de valor + 4 comparaciones (vs. Life360 y bSafe, Uber, Waze Carpool, Moovit y Google Maps).

### B5 · Diferenciación y riesgos
Tomo / Evito / Solo Match + 3 riesgos (masa crítica, suplantación, exponer la rutina) con su respuesta.

### P1–P6 · User persona
- **P1 Resumen (como la referencia):** Daniela, 22, cita, objetivos, necesidades, frustraciones, motivaciones y el recorrido emocional “Sale → camina → troncal → portal → espera → camina → llega”.
- **P2–P6:** contenido completo en `PERSONA_*` de `fuente/contenido.py`, con marcas [E] (entrevistas) y [S] (supuesto).

---

## 5. Arquitectura (árbol, de arriba hacia abajo)

```
INGRESO
├─ Bienvenida (qué es · verificación · privacidad)
├─ Crear cuenta
├─ Iniciar sesión
└─ Recuperar cuenta
        │
VERIFICACIÓN
├─ Correo institucional ─ universidad o empresa · código al correo · foto en el momento
├─ Círculo cercano ─ 2 avales · relación y tiempo · máx. 5 avales por persona
└─ Estado de la cuenta ─ sin verificar · pendiente · verificada · en revisión
        │
INICIO  (barra inferior: Hoy · Mis rutas · Matches · Perfil)
├─ HOY ─ próximo trayecto · personas disponibles hoy · solicitudes · iniciar trayecto · tiempos de llegada
├─ MIS RUTAS ─ rutas guardadas · crear/editar ruta (partida, tramos, destino, hora ±15, días) · trayecto de una vez · pausar/eliminar
├─ MATCHES ─ personas compatibles · filtros · solicitudes · compañía frecuente · sin matches
└─ PERFIL ─ perfil público · datos privados · preferencias de match · CONTACTOS DE CONFIANZA · privacidad · ajustes
        │
MATCH  (módulo central)
├─ Personas compatibles (tarjeta: foto, nombre + inicial, insignia, tramo en común, hora, punto de encuentro, trayectos)
├─ Detalle del match (mapa del tramo, punto y hora, verificación, reputación, preferencias, acciones)
├─ Solicitud ─ enviar · aceptar · rechazar · vence
├─ Confirmación mutua
└─ Chat breve ─ mensajes rápidos · código de encuentro · se borra en 24 h
        │
TRAYECTO ACTIVO
├─ Antes de salir (compañía · contactos a avisar · punto de encuentro)
├─ Encuentro (“Ya llegué” · código)
├─ En curso (mapa · tramo · tiempo de llegada · Dejar de compartir · ¿Algo no está bien?)
├─ Separación · Llegada · Retraso
        │
CONFIANZA
├─ Confirmación del trayecto · ¿Volverías a viajar? (privado)
├─ Reportar conducta · Bloquear
└─ Sin historial (qué se guarda / qué se borra)

VISTA DEL CONTACTO (web, sin app) ─ invitación · enlace del trayecto · avisos · caducidad
```

Colores sugeridos por sección, como la referencia: Ingreso gris · Verificación verde · Hoy azul · Mis rutas naranja · Matches morado · Perfil turquesa · Match azul oscuro · Trayecto activo amarillo · Confianza rosado · Vista del contacto gris punteado.
El detalle completo de cada nodo está en `COLS` de `fuente/contenido.py`.

---

## 6. Los 25 user flows (uno por nodo de la arquitectura)

Notación: ⬭ inicio/fin · ▭ pantalla/proceso · ▱ ingresa datos · ⛁ el sistema valida · ◇ decisión · ↺ vuelve a un paso anterior

### Acceso
1. **Ingreso** — ⬭ Abre la app → ▭ Bienvenida (3 pantallas) → ◇ ¿Cómo quieres ingresar? → Crear cuenta (F2) / Iniciar sesión (F3) / Recuperar cuenta (F4)
2. **Crear cuenta** — ⬭ Crear cuenta → ▱ Celular → ⛁ Envía código SMS → ▱ Código → ◇ ¿Correcto? No: ▭ Reenviar (máx. 3) ↺ · Sí → ▱ Nombre, fecha de nacimiento, género → ◇ ¿Mayor de 18? No: ⬭ No puede registrarse · Sí → ▭ Permisos → ▭ Términos y datos (Ley 1581) → ⬭ Verificación (F5)
3. **Iniciar sesión** — ⬭ → ▱ Celular → ⛁ Envía código → ▱ Código → ◇ ¿Correcto? No: ▭ Muestra error ↺ · Sí → ◇ ¿Cuenta verificada? No: ⬭ Verificación · Sí: ⬭ Inicio
4. **Recuperar cuenta** — ⬭ → ◇ ¿Conserva su número? Sí: ▱ Celular → ⛁ código SMS · No: ▱ Correo institucional → ⛁ código al correo → ▱ Código → ◇ ¿Correcto? No: ↺ · Sí → ▱ Nuevo celular (si cambió) → ⬭ Inicio

### Verificación
5. **Elegir método** — ⬭ Verificación → ▭ Explica por qué se verifica → ◇ ¿Tiene correo institucional? Sí: F6 · No: F7
6. **Correo institucional** — ⬭ → ▱ Busca su institución → ▱ Correo → ⛁ Envía código → ▱ Código → ◇ ¿Correcto? No: ▭ Reenviar ↺ · Sí → ▱ Foto en el momento → ⛁ Asigna insignia → ⬭ Crear primera ruta (F10)
7. **Círculo cercano (pedir avales)** — ⬭ → ▭ “Necesitas 2 avales” → ▱ Elige 2 personas verificadas o envía enlace → ⛁ Envía solicitudes → ◇ ¿Tiene 2 avales? No: ▭ “Pendiente · 1 de 2” (puede crear rutas) ↺ · Sí → ⛁ Insignia “Verificada por círculo” → ⬭
8. **Dar un aval** (lado de quien avala) — ⬭ Recibe solicitud → ▭ Ve foto y nombre → ◇ ¿La conoce en persona? No: ▭ Rechaza (sin motivo visible) → ⬭ · Sí → ▱ Relación y tiempo de conocerse → ◇ ¿Tiene avales disponibles (máx. 5)? No: ▭ Aviso de límite → ⬭ · Sí → ⛁ Registra el aval → ⬭

### Inicio (Hoy)
9. **Inicio** — ⬭ Inicio → ▭ Próximo trayecto, personas disponibles, solicitudes → ◇ ¿Qué quieres hacer? → Iniciar trayecto (F17) / Ver personas (F13) / Responder solicitudes (F14) / Mis rutas (F11) / Perfil (F20)

### Mis rutas
10. **Crear ruta** — ⬭ Nueva ruta → ▱ Punto de partida → ▱ Tramo (medio, subida, bajada) → ◇ ¿Otro tramo? Sí ↺ · No → ▱ Paradero final → ▱ Hora y rango → ▱ Días → ▭ Resumen → ⛁ Busca compatibles → ◇ ¿Hay coincidencias? Sí: ⬭ F13 · No: ⬭ F15
11. **Gestionar rutas** — ⬭ Mis rutas → ◇ ¿Hay rutas guardadas? No: ▭ Estado vacío → F10 · Sí → ▭ Elige ruta → ◇ ¿Qué quieres hacer? → Editar (▱ cambios → ⛁ recalcula compatibles) / Pausar (⛁ deja de aparecer) / Eliminar (◇ ¿Confirma? → ⛁ borra ruta y solicitudes pendientes) → ⬭
12. **Trayecto de una sola vez** — ⬭ → ▱ Partida, destino y hora de hoy → ⛁ Busca compatibles → ◇ ¿Hay? Sí: F13 · No: F15

### Matches
13. **Ver compatibles y enviar solicitud** — ⬭ → ▭ Lista de compatibles → ◇ ¿Filtrar? Sí: ▱ Filtros ↺ · No → ▭ Abre tarjeta → ▭ Detalle del match → ◇ ¿Le da confianza? No: ▭ Vuelve / bloquea / reporta ↺ · Sí → ▱ Envía solicitud → ⛁ Notifica → ⬭ Pendiente
14. **Responder solicitud** — ⬭ Notificación → ▭ Detalle → ◇ ¿Acepta? No: ▭ “No disponible” → ⬭ · Sí → ⛁ Confirmación mutua → ▭ Chat + punto + código → ◇ ¿Alguien cancela? Sí: ⛁ Avisa y sugiere otras → ⬭ F13 · No: ⬭ Listas para el trayecto
15. **Sin matches** — ⬭ → ▭ “Aún no hay nadie en tu tramo” → ◇ ¿Qué quieres hacer? → Ampliar rango (▱ ±30 min → ⛁ busca ↺) / Avisarme (⛁ notifica cuando aparezca) / Invitar (▱ contacto → ⛁ envía enlace) → ⬭
16. **Chat breve** — ⬭ Confirmación mutua → ▭ Chat → ◇ ¿Mensaje rápido o texto? → ▱ Envía → ◇ ¿Algo inapropiado? Sí: ⬭ F24 · No → ⛁ Se borra 24 h después del trayecto → ⬭

### Trayecto activo
17. **Iniciar trayecto y encuentro** — ⬭ Iniciar trayecto → ▭ Antes de salir → ▱ Confirma contactos → ⛁ Activa ubicación temporal y avisa → ▱ “Ya llegué” → ◇ ¿Llegó la otra persona en 10 min? No: ▭ Esperar / buscar otra / seguir con aviso · Sí → ▱ Confirman código → ◇ ¿Coincide? No: ⬭ No viaja y reporta · Sí: ⬭ En curso (F18)
18. **En curso y llegada** — ⬭ En curso → ▭ Mapa, tramo, tiempo de llegada → ◇ ¿La compañía se baja antes? Sí: ⛁ Avisa “sigue sola” → ◇ ¿Llegó a tiempo? Sí: ⛁ Apaga ubicación y avisa llegada → ⬭ F24 · No: ⛁ “¿Todo bien?” → ◇ ¿Responde en 5 min? Sí ↺ · No: ⛁ Avisa al contacto con la última ubicación → ⬭
19. **Dejar de compartir / ¿Algo no está bien?** — ⬭ Durante el trayecto → ◇ ¿Qué necesita? → Dejar de compartir (◇ ¿Confirma? → ⛁ Apaga y avisa) / Algo no está bien (◇ 123 · alertar contactos · reportar) → ⬭

### Perfil
20. **Perfil** — ⬭ Perfil → ◇ ¿Qué sección? → Perfil público / Preferencias (F22) / Contactos (F21) / Privacidad (F23) / Ajustes → ⬭ Inicio
21. **Contactos de confianza** — ⬭ → ▭ Lista → ▭ Agregar → ◇ ¿Permiso a la agenda? Sí: ▱ Elige contacto · No: ▱ Escribe nombre y celular → ▱ Relación, canal y avisos → ⛁ Envía invitación → ◇ ¿Acepta? No: ▭ “No aceptó” · Sí → ◇ ¿Agregar otro (máx. 3)? Sí ↺ · No → ▱ Predeterminado → ⬭
22. **Preferencias de match** — ⬭ → ▱ Género (solo mujeres / cualquiera) → ▱ Alcance (institución / círculo / ambos) → ▱ Tipo de compañía → ⛁ Recalcula compatibles → ⬭
23. **Privacidad** — ⬭ → ◇ ¿Qué quieres hacer? → Bloqueados (▭ desbloquear) / Descargar mis datos (⛁ genera el archivo) / Eliminar cuenta (◇ ¿Confirma? → ⛁ borra datos, rutas y avales → ⬭ Ingreso)

### Confianza
24. **Confirmar trayecto y reportar** — ⬭ Termina el trayecto → ◇ ¿Se encontraron? No: ▱ “No se presentó” → ⛁ Registra (3 = advertencia) · Sí → ▱ Confirma → ▱ ¿Volverías a viajar? (privado) → ◇ ¿Algo que reportar? No: ⛁ Suma trayecto y borra ubicaciones → ⬭ · Sí: ▱ Motivo y descripción → ⛁ Bloquea y envía a moderación → ◇ ¿Se confirma? Sí: ⛁ Suspende y revisa avales · No: ⛁ Advertencia interna → ⬭

### Vista del contacto
25. **Contacto avisado (web)** — ⬭ Recibe invitación → ◇ ¿Acepta avisos? No: ⬭ · Sí → ⛁ Llega enlace al iniciar un trayecto → ▭ Con quién va, mapa, hora estimada → ◇ ¿Qué aviso llega? → Llegada (⛁ el enlace caduca → ⬭) / Separación (▭ sigue viendo) / Retraso (▭ última ubicación → ⬭ llama o marca al 123)

---

## 7. Antes de entregar
- [ ] Verificar las celdas con `*` y “Por verificar” del benchmarking.
- [ ] Ajustar los supuestos `[S]` de la persona si hay datos reales.
- [ ] Decidir si se quedan el atajo al 123 y el código de encuentro (no estaban en el MoSCoW).
- [ ] Revisar que cada flujo apunte a un nodo de la arquitectura (numeración cruzada).
