# Match de ruta verificado · Explicación completa para la revisión

Material de estudio, por si la profe pregunta. Va en el mismo orden del archivo de Figma.
Cada parte tiene **qué es**, **por qué está así** y **qué responder si preguntan**.

---

## 0. El proyecto en 30 segundos

- **Qué es:** una app que empareja a personas verificadas que hacen el mismo trayecto en transporte público a la misma hora, para que nadie espere ni viaje solo de noche.
- **Para quién:** estudiantes y trabajadores que salen de noche y dependen del transporte público (troncal + alimentador, SITP, intermunicipal).
- **Frase del MVP:** "Una app para emparejarte con alguien verificado que hace tu mismo trayecto de noche."
- **Idea central:** no falta información, falta compañía.

---

## 1. De dónde salió (el proceso)

| Etapa | Qué hice | Qué saqué |
|---|---|---|
| Brief | María José planteó el problema: esperar el bus de noche en zonas oscuras, sin saber cuánto tarda | Hipótesis inicial: el problema es no saber cuánto tarda el bus |
| Entrevistas | 5 personas: María José (21), Juan José (21), Luna Valentina (25), Kimberly (21) y Daniel (21) | 5 de 5 usan apps de rutas y aun así sienten miedo |
| Definir | 6 insights y problema replanteado | El problema no es la información, es estar solo |
| Idear | 16 ideas, MoSCoW y MVP | Concepto elegido: Match de ruta verificado |
| Analizar | Benchmarking, user persona, arquitectura y user flows | Esta entrega |

### Los 6 insights (de las entrevistas)
1. **Tener información no quita el miedo.** 5 de 5 usan apps de rutas y aun así sienten miedo → compañía real, no más datos.
2. **El miedo viene de algo vivido.** 5 de 5 cuentan un incidente concreto → diseñar para un riesgo real.
3. **Ante el riesgo, buscan dejar de estar solos.** 4 de 5 cambiaron de plan alguna vez (moto, carro, conductora mujer o dormir donde un amigo) → atacar la causa: estar solo.
4. **Avisar a alguien ya es un hábito, pero manual.** 2 comparten la ubicación siempre, 2 avisan por mensaje y 1 no avisa → llevarlo a la app.
5. **El miedo cambia según el género.** Las 3 mujeres hablan de violencia sexual; los 2 hombres, de robo → preferencia de género.
6. **Nadie elige dónde esperar por una app.** 0 de 5 lo hacen; eligen por la luz, la cercanía y la gente → los tiempos de llegada quedan como capa secundaria.

### Caminos que descarté (por si pregunta "¿por qué no hiciste X?")
- **App de tiempos de llegada:** la descarté porque los 5 ya usan apps de rutas y siguen con miedo.
- **Botón de ubicación + reportes por estación (primer MVP):** en la retro me dijo que se cruzaba con Moovit y Uber, y que una app no controla la calle.
- **Acompañante desconocido:** nadie quiere confiar en un extraño. Por eso la verificación es obligatoria.

### Problema replanteado
"Quien depende del transporte nocturno espera y viaja solo, sin saber si alguien de su entorno hace el mismo recorrido a la misma hora."
Entorno = misma universidad, mismo trabajo o mismo barrio.

---

## 2. MVP y MoSCoW (sección 00)

### Lámina M1 · MVP
El MVP tiene tres partes:

| Parte | Qué hace | Ideas del MoSCoW | Dónde está en la arquitectura | Flujos |
|---|---|---|---|---|
| **Registro** | Te verificas con correo institucional o con 2 avales de tu círculo cercano | 01 y 11 | Ingreso · Verificación | F01–F08 |
| **Match** | Guardas tu ruta y horario; la app te muestra quién hace el mismo tramo a la misma hora | 02 y 03 | Mis rutas · Matches · Match | F10–F14 |
| **Trayecto** | Ubicación en vivo que solo dura el trayecto y se apaga al llegar | 04 | Trayecto activo | F17–F18 |

### Lámina M2 · MoSCoW (tus 16 ideas)
- **Must (entra en el MVP):** 01 · 11 Registro verificado · 02 Ruta y horario · 03 Emparejamiento automático · 04 Ubicación en vivo temporal
- **Should (segunda versión):** 05 Dejar de compartir · 09 Aviso a contacto · 06 Preferencia de género · 12 Reporte de conducta
- **Could (si hay tiempo):** 07 Chat para coordinar · 08 Confirmación mutua · 14 Solo acompañar la espera · 16 Tiempos de llegada
- **Won't (no se hará):** 10 Historial de ubicaciones · 15 Reverificación periódica · 13 Sugerir hora de salida

### Ajustes que propuse (y cómo defenderlos)
1. **05 Dejar de compartir → Must.** En la retro me preguntó si compartir la ubicación también es un riesgo, y una de mis respuestas fue este botón. Si queda en Should, el MVP no cumple lo que prometí.
2. **08 Confirmación mutua → Must.** Sin que las dos personas acepten, el emparejamiento automático conectaría a alguien sin su permiso. En una app de seguridad eso no puede faltar.
3. **Código de encuentro (Should) y atajo al 123 (Could).** Salieron del benchmarking y de los riesgos. Ya aparecían en la arquitectura, así que los ubiqué en el MoSCoW para que todo sea coherente.

**Si pregunta "¿por qué la arquitectura tiene más cosas que el MVP?":** la arquitectura y los flujos muestran el producto completo. El MVP es solo la columna Must; lo demás llega en versiones siguientes.

---

## 3. Benchmarking (sección 01)

### Qué apps comparé y por qué
| App | Por qué está | Qué hace |
|---|---|---|
| **Moovit** | La app de rutas más usada; es lo que mis entrevistados ya tienen | Informa |
| **Google Maps** | Rutas y ubicación compartida | Ubica y guía |
| **Uber** | La alternativa a la que acude la gente cuando tiene miedo | Transporta |
| **Life360** | Círculo de confianza con ubicación permanente | Vigila |
| **bSafe** | App de seguridad personal (SOS, Follow Me, llamada falsa) | Reacciona |
| **Waze Carpool** | Emparejaba personas por ruta con filtros de institución y género; Google lo cerró en 2022 | Antecedente |
| **Match** | Mi propuesta | Acompaña |

### Qué comparé
18 funcionalidades en 5 grupos, más el costo:
- **Movilidad:** planear ruta, tiempos de llegada, alertas de servicio
- **Ubicación y avisos:** compartir ubicación, que se apague sola, aviso de llegada, sin historial
- **Seguridad y respuesta:** SOS, grabar evidencia, llamada falsa
- **Identidad y confianza:** identidad verificada, verificación por institución, red de confianza, calificación o reporte, preferencia de género
- **Acompañamiento:** emparejamiento por ruta, compañía física, chat
- **Modelo:** costo

Símbolos: ● sí · ◐ parcial · ○ no · ? por verificar. El **\*** marca lo que depende del país o del plan.

### Datos verificados que conviene saber
- **Moovit tiene "SafeRide"** dentro de Moovit+ (de pago): compartes la ubicación, los transbordos y la hora estimada con contactos que no necesitan instalar Moovit. Por eso no digo que avisar sin instalar la app sea algo que solo hace Match.
- **bSafe:** "Follow Me" es gratis; la alarma por no confirmar a tiempo, el video y el audio son premium.
- **Life360:** guarda historial de ubicaciones (2 días en el plan gratis, hasta 30 en los pagos). El SOS es gratis.
- **Uber:** la grabación de audio existe en varios países de Latinoamérica desde 2019. "Women Preferences" solo está en algunos países.
- **Waze Carpool:** filtraba por género y por compañeros de trabajo o de clase, y tenía calificación con estrellas. Google lo cerró en 2022 porque, después de la pandemia, la gente dejó de usarlo para ir y volver del trabajo.

### Los 6 hallazgos (lámina "Conclusión · ¿Qué encontré?")
1. **Cada app resuelve una parte: informar, transportar o reaccionar.** Ninguna pone a otra persona al lado de quien viaja en transporte público.
2. **Compartir la ubicación ya es algo común.** 5 de las 6 lo tienen; lo distinto en Match es que solo dura el trayecto, se apaga al llegar y no deja historial.
3. **La confianza se construye de dos formas y ninguna app usa las dos.** Life360 y bSafe usan gente conocida sin verificar; Uber verifica conductores, no tu red. Match usa las dos: institución + avales.
4. **Emparejar por ruta ya existe, pero en carro** (UberX Share, Waze Carpool). Los filtros funcionaron; el riesgo es la masa crítica.
5. **Las apps de seguridad actúan cuando el riesgo ya ocurrió.** Match actúa antes: busca que no estés sola.
6. **Ninguna cubre la espera en el paradero**, que es el momento de más tensión. Match empareja desde el paradero de salida.

### Oportunidad de diseño
"Los 5 entrevistados usan apps de rutas y aun así sienten miedo. La oportunidad está en que nadie tenga que esperar ni viajar solo de noche."

**Propuesta de valor:** para estudiantes y trabajadores que dependen del transporte público de noche, Match los conecta con personas verificadas de su universidad, su trabajo o su círculo cercano que hacen el mismo trayecto a la misma hora.

### Diferenciación
- **Tomo (lo que ya funciona):** círculos de confianza (Life360), viaje compartido que termina solo (Uber, Google Maps), contacto que sigue el viaje sin instalar la app (Moovit SafeRide), calificación y reporte (Uber), filtros por institución y género (Waze Carpool).
- **Evito (lo que genera desconfianza):** ubicación permanente e historial, emparejar desconocidos, cobrar por sentirse seguro, actuar solo cuando ya pasó algo.
- **Solo Match (no lo encontré en ninguna de las 6):** emparejar por tramo de transporte público y horario, verificación doble (institución + avales) y compañía física en la espera del paradero.

### Riesgos
| Riesgo | Cómo lo abordo |
|---|---|
| **Masa crítica:** si no hay nadie en tu ruta y hora, la app no sirve | Lanzar en una universidad piloto, emparejar por tramo (no por ruta completa) y usar un rango de ±15 min |
| **Suplantación** | Foto tomada en el momento, código de encuentro y reporte con bloqueo inmediato |
| **Exponer la rutina** | Nunca se muestran el destino exacto, el apellido ni el celular; solo el tramo en común, y solo a personas compatibles |

---

## 4. User persona (sección 02)

### Daniela Gómez, 22 años (persona principal)
- Estudiante de Comunicación Social. Vive en Bosa y estudia en Chapinero. Sale de clase a las 9:00 p. m. martes y jueves y viaja sola en troncal + alimentador.
- **Cita:** "La app me informa, pero no me protege."
- **Objetivo:** llegar a casa tranquila, sin depender de que la recojan ni de pagar un carro cada noche.

**[E] y [S]:** [E] es un dato de las 5 entrevistas; [S] es un supuesto para completar el perfil (carrera, barrio, horario, celular). Si pregunta, explica que la persona es una composición basada en las entrevistas y que los supuestos están marcados para no presentarlos como hechos.

### Su trayecto de un martes (lámina P3)
| Hora | Momento | Tensión |
|---|---|---|
| 9:00 | Sale de clase y revisa la app | Tranquila |
| 9:05 | Camina 8 min por una calle oscura | Alerta |
| 9:15 | 40 min de pie en la troncal | Atenta |
| 9:55 | Llega al portal y busca el alimentador | Tensa |
| 10:00 | Espera el alimentador de 10 a 20 min | **Máxima tensión** |
| 10:30 | Camina 6 min a su casa | **Miedo** |
| 10:40 | Llega y le escribe "llegué" a su mamá | Alivio |

**Conclusión de la lámina:** la tensión más alta está en la espera del alimentador y en la caminata a casa. Match cubre la espera con compañía y la caminata con el aviso al contacto hasta que Daniela toca "Llegué".

### Lo demás de Daniela
- **Necesidades:** saber quién de su U hace su tramo a su hora; que su mamá sepa que llegó sin escribirle; no estar sola en la espera; que la otra persona esté verificada y, si lo prefiere, sea mujer; que nadie conozca su dirección.
- **Comportamiento:** revisa la app de rutas aunque no le quite el miedo; elige dónde esperar por la luz y la gente; guarda el celular cuando el paradero se vacía.
- **Frustraciones:** la app le da horarios, no tranquilidad; no le alcanza para un carro todas las noches; compartir la ubicación es manual.
- **Motivaciones:** no estar sola en el momento más expuesto; terminar la carrera sin evitar las materias de la noche; que su mamá esté tranquila.
- **Miedos:** violencia sexual (lo mencionaron las 3 mujeres), robo o agresión, que la sigan al bajarse del bus.
- **Situaciones que cambian sus decisiones:** si se le hace tarde, pide un carro o se queda donde una amiga (4 de 5 entrevistados cambiaron de plan alguna vez); la lluvia; la batería baja; ir con alguien conocido; semana de parciales; fin de mes.

### Personas secundarias
- **Gloria, 49 (mamá de Daniela, contacto avisado):** quiere saber con quién va su hija y que llegó, sin llamar y sin instalar otra app. Por eso los avisos le llegan por SMS o WhatsApp con un enlace web.
- **Daniel, 21 (segmento hombres):** su miedo principal es el robo. La preferencia de género es opcional: puede acompañar a quien lo acepte.

---

## 5. Arquitectura de la información (sección 03)

**Recordatorio de clase:** la arquitectura es qué contiene la plataforma, no el paso a paso (eso son los flujos).

### Estructura (de arriba hacia abajo)
1. **Ingreso:** bienvenida, crear cuenta (celular + código SMS, datos, permisos, términos y Ley 1581 de datos personales), iniciar sesión, recuperar cuenta.
2. **Verificación:** correo institucional, círculo cercano (avales), estado de la cuenta, mis círculos.
3. **Inicio (barra inferior):**
   - **Hoy:** próximo trayecto, personas disponibles, solicitudes, iniciar trayecto, tiempos de llegada.
   - **Mis rutas:** rutas guardadas, crear o editar (partida, tramos, paradero final, hora ±15 min, días), trayecto de una sola vez, pausar o eliminar.
   - **Matches:** personas compatibles, filtros, solicitudes, compañía frecuente, sin matches.
   - **Perfil:** perfil público, datos privados, preferencias, contactos de confianza, privacidad, ajustes.
4. **Match:** personas compatibles, detalle del match, solicitud, confirmación mutua, chat breve.
5. **Trayecto activo** (banner fijo mientras dura): antes de salir, encuentro, en curso, separación, llegada, retraso.
6. **Confianza:** confirmar el trayecto, "¿volverías a viajar?" (privado), reportar y bloquear, sin historial.
7. **Vista del contacto** (web, sin app): invitación, enlace del trayecto, avisos, caducidad.

### Las 4 preguntas de la revisión (marcadas en amarillo)
1. **¿Cómo funciona la verificación por círculo cercano?**
   Quien no tiene correo institucional pide 2 avales a personas que ya están verificadas. Quien avala confirma que la conoce en persona, la relación (familia, amistad, trabajo o barrio) y desde cuándo. Con 2 avales queda "Verificada por círculo". Cada persona puede avalar máximo 5 cuentas, y si una cuenta avalada es suspendida, se revisan sus avales: quien recomienda también responde. *(Flujos F07 y F08.)*
2. **¿Qué muestra la plataforma al revisar los posibles perfiles?**
   Foto, nombre con la inicial del apellido, insignia y método de verificación, institución o círculo, tramo en común, hora de salida y diferencia con la tuya, punto de encuentro, trayectos acompañados y conocidos en común. **Nunca** el destino final, el apellido completo ni el celular. *(F13.)*
3. **¿Dónde agrego los contactos que serán avisados?**
   En Perfil → Contactos de confianza (máximo 3), desde la agenda o a mano, con relación, canal (SMS o WhatsApp) y los avisos que recibe. El contacto tiene que aceptar. Además, antes de cada trayecto se confirma a quién avisar esa vez. *(F21 y F17.)*
4. **¿Qué contiene el detalle de un match?**
   Perfil público ampliado, mapa del tramo compartido (dónde se unen y dónde se separan), punto y hora de encuentro, tiempo estimado juntos, verificación (método y fecha), reputación (trayectos, confirmaciones, sin reportes), preferencia de compañía y acciones: solicitar, bloquear o reportar. *(F13.)*

---

## 6. User flows (sección 04)

### Notación (igual a la referencia)
- Cápsula gris = inicio o fin
- Rectángulo morado = pantalla o proceso
- Paralelogramo azul = el usuario ingresa datos
- Cilindro verde = el sistema valida o consulta
- Rombo naranja = decisión (sí / no)

### Los 25 flujos
| Grupo | Flujos |
|---|---|
| **Acceso** | F01 Ingreso · F02 Crear cuenta · F03 Iniciar sesión · F04 Recuperar cuenta |
| **Verificación** | F05 Elegir método · F06 Correo institucional · F07 Círculo cercano: pedir avales · F08 Círculo cercano: dar un aval |
| **Inicio y Mis rutas** | F09 Inicio · F10 Crear ruta y horario · F11 Gestionar rutas · F12 Trayecto de una sola vez |
| **Matches** | F13 Ver compatibles y enviar solicitud · F14 Responder solicitud · F15 Sin matches · F16 Chat breve |
| **Trayecto activo** | F17 Iniciar trayecto y encuentro · F18 En curso y llegada · F19 Dejar de compartir y pedir ayuda |
| **Perfil** | F20 Perfil · F21 Contactos de confianza · F22 Preferencias de match · F23 Privacidad |
| **Confianza y contacto** | F24 Confirmar trayecto y reportar · F25 Vista del contacto avisado |

### Los tres flujos que conviene saber de memoria
- **F07 (avales):** pide 2 avales → se envían las solicitudes → ¿tiene 2? Si no, queda "Pendiente 1 de 2" (puede crear rutas, pero aún no hacer match). Si sí, recibe la insignia.
- **F13 (ver compatibles):** lista → filtrar (opcional) → abre una tarjeta → detalle → ¿le da confianza? Si no, vuelve, bloquea o reporta. Si sí, envía la solicitud.
- **F17–F18 (trayecto):** confirma a quién avisar → se activa la ubicación temporal → "Ya llegué" → ¿la otra persona llegó en 10 min? → confirman el código → en curso → si la compañía se baja antes, se avisa → llegada: se apaga la ubicación y se avisa al contacto. Si pasan 15 min sin llegar: "¿Todo bien?", y si no responde en 5 min, el contacto recibe la última ubicación.

---

## 7. Preguntas difíciles y cómo responderlas

**"¿Y si no hay nadie en tu ruta?"**
Es el riesgo principal. Por eso se empareja por tramo y no por ruta completa: si solo compartes "Calle 45 → Portal Sur", igual hay match. El rango es de ±15 min, se puede ampliar a ±30, y la app avisa cuando aparezca alguien. Empezaría con una universidad piloto.

**"¿No es peligroso mostrar a qué hora sales?"**
Solo lo ven personas verificadas y compatibles con tu tramo. Nunca se muestran la dirección, el destino exacto ni el celular. El chat se borra a las 24 horas y las ubicaciones al llegar.

**"¿Y si la persona del match es la peligrosa?"**
Hay varias capas: verificación (institución o avales), código de encuentro para confirmar en persona, reporte con bloqueo inmediato, moderación y revisión de los avales de quien sea suspendido. No elimina el riesgo, lo reduce frente a esperar solo o con desconocidos.

**"¿En qué se diferencia de Moovit o de Uber?"**
Moovit informa y, con su plan pago, deja compartir el viaje, pero no te pone a nadie al lado. Uber te saca del transporte público y cobra cada viaje. Match funciona dentro del transporte público, es gratis y te da compañía real.

**"¿Por qué no un botón de pánico?"**
Las apps de seguridad ya lo tienen y actúan cuando el riesgo ya ocurrió. Match busca que no estés sola antes de que pase algo. Para emergencias hay un atajo al 123; no reemplaza a las autoridades.

**"¿Por qué preferencia de género?"**
Sale del insight 5: las 3 mujeres entrevistadas temen la violencia sexual. Es opcional; Daniel, por ejemplo, puede acompañar a quien lo acepte.

**"¿Cómo se gana plata?"**
En la propuesta es gratis para quien la usa. No lo definí en esta etapa; una opción posible sería hacer alianzas con universidades o empresas, que son las que verifican. Si te pregunta, di que es un tema pendiente, no algo resuelto.

**"¿Los datos de la persona son reales?"**
Lo marcado con [E] sale de las 5 entrevistas. Lo marcado con [S] es supuesto para completar el perfil, y está señalado para no presentarlo como hecho.

---

## 8. Limitaciones (dilo antes de que te lo pregunten)
- Fueron 5 entrevistas: alcanzan para encontrar patrones, no para generalizar.
- Algunas celdas del benchmarking dependen del país o del plan y quedaron marcadas con *.
- El modelo de negocio y la masa crítica son los dos puntos más abiertos del proyecto.
