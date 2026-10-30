# Mini manual de marca · v0.1

Scripts que construyen la página **“Identidad · Mini manual v0.1”** del archivo de Figma (Plugin API vía `use_figma`).

| Archivo | Contenido |
|---|---|
| pre.js | Variables de color (colección “Match · Marca”), estilos de texto Figtree (“Marca/…”, “Manual/…”), símbolo, logo, efecto de vidrio y ayudas de maquetación |
| a.js | Láminas 00 Portada · 01 Concepto · 02 Referencias · 03 Logo · 04 Color |
| ic.js | Trazos de los iconos Phosphor usados (licencia MIT, paquete `@phosphor-icons/core` 2.1.1) |
| b.js | Láminas 05 Tipografía · 06 Iconos e ilustración · 07 Liquid glass · 08 Aplicación (E01, F06, G01) |

Orden de ejecución: `pre.js + a.js` en una llamada y `pre.js + ic.js + b.js` en otra.

El color de acento es provisional (violeta #5B3DF5). Para cambiarlo basta con editar la variable `acento/principal`
(y `acento/suave` / `acento/sobre-acento` si el nuevo color lo pide): todo el manual está enlazado a variables.
