# Ilustraciones del componente «Ilustración» (15 nov)

Las 9 escenas vienen de **unDraw** (ilustraciones de Katerina Limpitsouni), descargadas del paquete
de npm `undraw-svg@2.0.0`. No son de Envato: desde la sesión en la nube no se pudo entrar a esa cuenta.
Los SVG no se guardan en el repo; se vuelven a bajar con `npm pack undraw-svg@2.0.0`.

| Tema | Archivo de unDraw | Tratamiento |
|---|---|---|
| Espera (imagen principal) | high-five | Dos personas sobre luna, cielo violeta y ciudad |
| Verificación | authentication | Personaje sobre luna |
| Ubicación | my-location | Personaje sobre luna |
| Encuentro | nice-to-meet-you | Personaje sobre luna |
| Llegada | knocking-on-the-door | Personaje sobre luna |
| Reporte | warning | Personaje sobre luna |
| Aviso | my-notifications | Personaje sobre luna |
| Rutas | route-planning | Escena recoloreada para fondo oscuro |
| Paradero vacío | quiet-street | Escena recoloreada para fondo oscuro |

## Cómo se adaptaron
1. `adapt.py <svgs de unDraw> <salida> picks.json` cambia cada color de unDraw por el hex exacto de una
   variable de marca (acento → `primario/500`, oscuros → `neutral/900` y `700`, grises → `neutral/200–400`,
   pieles → `ilustracion/piel-1..3`). Hay dos tablas: `LIGHT` (personajes) y `DARK` (escenas sin personas).
2. `armar.py <salida> <carpeta>` genera tres scripts a partir de `montar-en-figma.plantilla.js`.
3. Cada script se ejecuta en Figma: crea los vectores, enlaza cada relleno a su variable y los coloca en las
   27 variantes (9 temas × Grande, Mediana, Compacta).

Composición: cielo `neutral/800`, suelo `neutral/900` y, en los temas con personas, una luna grande
`primario/100` detrás del personaje para que se lea de noche. Luna, suelo y sujeto conservan las
restricciones (centro / abajo) para que la instancia se pueda redimensionar.

Licencia: revisar https://undraw.co/license antes de la entrega (no se pudo abrir desde la sesión).
