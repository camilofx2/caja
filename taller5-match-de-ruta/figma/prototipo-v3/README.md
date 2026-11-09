# Prototipo v3 · prueba 1 · El trayecto de Daniela

Scripts que construyen la página **“Prototipo v3 · prueba 1”** del archivo de Figma: 17 pantallas con la marca aplicada
(variables de la colección “Match · Marca”, estilos Figtree, iconos Phosphor como componentes) y las conexiones del prototipo.

| Archivo | Contenido |
|---|---|
| pp.js | Ayudas compartidas: página, variables, estilos, botones, chips, mapa, línea del trayecto, vidrio, menú inferior, hojas |
| ic.js + lib.js | Trazos Phosphor (MIT) y creación de la “Biblioteca · iconos” (solo en la primera llamada) |
| c1.js | P01 Bienvenida · P02 Inicio · P03 Personas compatibles · P04 Detalle · P05 Pedir el trayecto (hoja) |
| c2.js | P06 Solicitud enviada · P07 Laura aceptó · P08 Chat · P09 Antes de salir · P10 En curso · P11 ¿Algo no está bien? (hoja) |
| c3.js | P12 Laura se bajó · P13 Llegaste · P14 ¿Cómo te fue? (hoja) · P15 Confirmado · P16 Mis rutas · P17 Perfil · conexiones |

Orden: `pp.js + ic.js + lib.js + c1.js`, luego `pp.js + c2.js`, luego `pp.js + c3.js`.

Conexiones: cada capa llamada `Ir:Pxx` navega a esa pantalla; las capas `Atrás` vuelven a la anterior.
Avances automáticos (en milisegundos): P06 → P07 a 2500, P13 → P14 a 3500, P10 → P12 a 5000.
