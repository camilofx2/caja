# Match de ruta verificado · Entrega corregida (Taller 5 · Diseño e Interacción)

Correcciones a partir de la retro de la profe: Benchmarking con conclusión, User Persona en profundidad, Arquitectura de la información detallada y User Flows por funcionalidad.

## Láminas (carpeta `laminas/`)

| Archivo | Qué contiene | Responde a la retro |
|---|---|---|
| `01-benchmarking.svg` | Cuadro de 6 plataformas × 19 funcionalidades en 6 categorías; 6 hallazgos con su implicación; propuesta de valor; diferenciación (tomo / evito / solo Match); riesgos | “Falta la conclusión” · “apenas mencionas cuatro funcionalidades” |
| `02-user-persona.svg` | Daniela (persona principal): quién es, contexto, tecnología, trayecto con curva de tensión, necesidades, comportamientos, frustraciones, motivaciones, miedos, situaciones que cambian sus decisiones, escenario con Match. Gloria (contacto avisado) y Daniel (segmento hombres) | “Perfil demasiado general” |
| `03-arquitectura.svg` | 10 secciones con sus pantallas o módulos y su contenido; las 4 preguntas de la profe resaltadas en amarillo y respondidas abajo | “¿Cómo funciona el círculo cercano? ¿Qué muestra un perfil? ¿Dónde agrego contactos? ¿Qué tiene el detalle del match?” |
| `04-user-flows.svg` | 10 flujos, uno por funcionalidad, con actor, objetivo, entrada, sección de la arquitectura, decisiones y caminos alternativos | “Un flow por proceso, no uno general” |

## Cómo pasarlas a Figma (2 minutos)

1. Abre el archivo de Figma → página **“Entrega · Definición del producto”** (ya está creada y vacía).
2. Arrastra los 4 `.svg` al lienzo (o ábrelos en el navegador, copia y pega). Figma los convierte en capas editables: el texto queda como texto.
3. Si alguna fuente aparece reemplazada, selecciona todo y vuelve a asignar **Space Grotesk** y **Space Mono** (las mismas de tu presentación).
4. Opcional: envuelve cada lámina en una sección (Shift + S) con el nombre de la lámina.

## Antes de entregar: datos para verificar

- En el benchmarking, las celdas con `*` y las de “Por verificar” dependen del país, del plan o de actualizaciones de las apps. Confírmalas en la app o en su página oficial.
- En la persona, lo marcado `[S]` es supuesto: carrera, barrio, horario y detalles de rutina. Ajústalo si tienes datos reales de las entrevistas.

## Regenerar las láminas

Los textos y la diagramación están en `fuente/*.py`. Requiere Python 3 con `pillow` y las fuentes Space Grotesk y Space Mono en `~/.fonts`:

```sh
cd fuente
python3 benchmarking.py ../laminas/01-benchmarking.svg
python3 persona.py ../laminas/02-user-persona.svg
python3 arquitectura.py ../laminas/03-arquitectura.svg
python3 flujos.py ../laminas/04-user-flows.svg
```
