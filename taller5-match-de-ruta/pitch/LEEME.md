# Pitch de Match de ruta

Presentación en un solo archivo HTML: comercial animado de 40 segundos (pantalla completa, con música) y 20 láminas.

- `match-de-ruta-pitch.html`: la que se abre con doble clic en Chrome. Funciona sin internet
  (solo cambia la tipografía por la del sistema si no puede cargar Figtree).
- `match-pitch.artefacto.html`: la misma, en el formato que se publica como enlace.
- `src/pitch.src.html`: el archivo que se edita. Textos, láminas, animaciones y guion están ahí.
- `img/`: pantallas reales exportadas de Figma y la ilustración de las dos personas.

## Cómo presentar
| Tecla | Qué hace |
|---|---|
| Espacio (en el comercial) | Reproducir o pausar |
| → o Enter | Lámina siguiente |
| ← | Lámina anterior |
| F | Pantalla completa |
| R (en el comercial) | Volver a empezar el comercial |

El reloj de abajo empieza a contar con la primera tecla o clic. La meta son 13 a 14 minutos (máximo 15).

## Orden
0. Comercial (40 s). Al darle play se pone en pantalla completa y suena la música, generada en el navegador (no usa archivos ni internet). Mover el mouse muestra los controles: pausa, silenciar y saltar.
1–15. La idea: portada, problema, hallazgos, ¿qué es?, cómo funciona, ¿a quién va dirigida?, confianza,
   quien te espera, ¿qué impacto genera?, propuesta de valor, beneficios, riesgos, modelo de negocio mixto,
   valor comercial estimado, el primer paso.
16–19. Proceso: cómo se construyó, sistema de diseño, lo que cambió, lo que me quedó.
20. Cierre.

## Las 7 preguntas de la entrega y dónde se responden
| Pregunta | Lámina |
|---|---|
| ¿Qué es? | 04 |
| ¿A quién va dirigida? (público y comunidad) | 06 |
| ¿Qué impacto genera? (necesidad y transformación) | 09 (y el problema en 02–03) |
| Propuesta de valor | 10 |
| Valor comercial o modelo de negocio | 13 y 14 |
| Beneficios | 11 |
| Proceso | 16–19 |

## Fuentes de las cifras (láminas 06, 11, 13 y 14)
- Pasaje TransMilenio 2026, $3.550: Alcaldía de Bogotá, bogota.gov.co ("Abecé del ajuste tarifario… 2026").
- Salario mínimo 2026, $1.750.905: Decreto 1469 de 2025 (ratificado por el Decreto 0159 de 2026).
- Matrícula en educación superior 2025, 2.723.364: SNIES, Ministerio de Educación.
- 62,7 % considera que TransMilenio no es seguro (66,6 % mujeres): Encuesta de Percepción y Victimización 2025, Cámara de Comercio de Bogotá.
- 52 % de las mujeres vivió acoso sexual en el transporte público (hombres 16 %): Encuesta de Acoso Sexual Callejero 2025, Veeduría Distrital.
- Bienestar universitario, mínimo 2 % del presupuesto de funcionamiento: Ley 30 de 1992, art. 118.
- Precios de Match Plus ($6.900) y licencia ($1.200 por estudiante al año), y los supuestos del estimado
  (20.000 personas por institución, 10 % de uso, 5 % paga Plus) son propuestas propias por validar.

## De dónde sale el contenido
Todo sale de `../EXPLICACION-PROYECTO.md` (5 entrevistas, 6 hallazgos, benchmarking, riesgos) y del archivo
de Figma. No hay cifras externas. Los aprendizajes de la lámina 14 son un borrador para reescribir.

## Cambiar algo y volver a armar
1. Editar `src/pitch.src.html`.
2. `python3 src/armar.py` (desde esta carpeta).
3. Revisar: `node src/probar.js match-de-ruta-pitch.html slides <carpeta>` saca una captura de cada lámina.

## Pendiente
- El comercial no tiene música. Si se quiere, se graba la pantalla y se le pone una pista con licencia en un editor.
- El violeta sigue siendo provisional.

## Guion
El guion va aparte de la presentación, para tenerlo en otra pantalla: `GUION.md`.
Se genera con `python3 -I src/guion.py` (desde `pitch/`). Meta total: 13:25.
