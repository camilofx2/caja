# Pitch de Match de ruta

Presentación en un solo archivo HTML: comercial animado de 1 minuto y 15 láminas.

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
| N | Mostrar u ocultar el guion de la lámina |
| F | Pantalla completa |
| R (en el comercial) | Volver a empezar el comercial |

El reloj de abajo empieza a contar con la primera tecla o clic. La meta son 15 minutos.

## Orden
0. Comercial (1 min)
1–10. La idea: portada, problema, hallazgos, la idea, cómo funciona, confianza, quien te espera,
   lo que ya existe, riesgos y modelo, el primer paso.
11–14. El proceso: cómo se construyó, sistema de diseño, lo que cambió, lo que me quedó.
15. Cierre.

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
