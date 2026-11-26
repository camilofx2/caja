# FigJam · Investigación de Match de ruta

Tablero: https://www.figma.com/board/Ot0HvEvorDkmOm9yVtU8hF

11 secciones, leídas de izquierda a derecha y fila por fila:

| Sección | Contenido | Fuente |
|---|---|---|
| 00 Portada e índice | Índice de láminas | — |
| 01 Brief e hipótesis inicial | Brief, hipótesis, qué tendría que ser cierto y qué salió | EXPLICACION-PROYECTO.md §1 |
| 02 Entrevistas | 5 personas y hallazgos agrupados por tema (notas adhesivas) | §1 y datos [E] de la persona |
| 03 Síntesis y análisis | 6 insights con evidencia y decisión, problema replanteado, caminos descartados | §1 |
| 04 Ideación y MoSCoW | 16 ideas priorizadas | §2 |
| 05 MVP | Registro, match y trayecto; ajustes al MVP | §2 |
| 06 Benchmarking | Tabla de 18 funcionalidades × 6 apps, hallazgos, oportunidad, propuesta de valor, diferenciación y riesgos | fuente/contenido.py |
| 07 User persona | Ficha, trayecto con tensión, 9 bloques [E]/[S], escenario y personas secundarias | fuente/contenido.py |
| 08 Arquitectura | Árbol de la plataforma y las 4 preguntas de la revisión | §5 |
| 09 User flows | Notación, los 25 flujos y F17–F18 dibujado | §6 |
| 10 Del hallazgo a la pantalla | Trazabilidad: hallazgo → decisión → pantalla en alta | páginas v3 de Figma |

Scripts (se ejecutan con la herramienta use_figma de Figma):
- `1-secciones-texto.js`: portada y secciones 01–05.
- `2-plantilla.js` + `generar-parte2.py`: secciones 06–10. El generador inyecta los datos de `fuente/contenido.py`
  y escribe `2-secciones-06-10.js`.

Nota: las láminas no se subieron como imágenes porque la red de la sesión bloquea figma.com.
Se reconstruyeron nativas (editables) y cada sección enlaza a su lámina completa en Figma Design.
