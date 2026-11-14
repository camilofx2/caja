# Wireframes v3 · alta fidelidad

Página **“Wireframes v3 · alta”** y página **“Componentes · Match”** del archivo de Figma.
Aplica la clase del 7 de noviembre: componentes con estados, neutrales 0–900, auto layout en todo
y pantallas de formulario con botón bloqueado → activo.

## Componentes (`base.js` + `comp1.js`, luego `base.js` + `comp2.js`)
| Componente | Variantes |
|---|---|
| Botón | Primario, Acento, Secundario, Terciario, Peligro × Default / Disabled |
| Campo | Texto / Lista × Default, Active, Filled, Disabled, Error, Success |
| Código | Vacío, Activo, Lleno, Error |
| Chip | Default, Seleccionado, Disabled |
| Casilla · Interruptor · Opción | On/Off/Disabled · On/Off/Disabled · Default/Seleccionado |
| Aviso | Info, Éxito, Alerta, Error |
| Pasos | 2, 3 o 4 pasos × paso actual |
| Persona | Tarjeta, Plana, Grande |
| Menú inferior · Barra de estado · Barra superior | Hoy/Mis rutas/Matches/Perfil · Claro/Oscuro · Claro/Oscuro |

`comp1.js` también renombra las variables a la escala `neutral/0…900` y `primario/100, 500, 700, sobre`.

## Pantallas (`base.js` + `r3.js` + un archivo de flujo por llamada)
| Archivo | Flujo | Pantallas |
|---|---|---|
| s1.js | 00 Guía · A Bienvenida, registro e ingreso | 14 |
| s2.js | B Verificación con correo institucional | 7 |
| sC.js | C Verificación por círculo cercano | 9 |
| sD.js | D Rutas | 10 |
| sE.js | E Match, solicitud y chat | 10 |
| sF.js | F Trayecto activo | 11 |
| sGH.js | G Confianza · H Perfil, contactos y privacidad | 7 + 11 |
| sI.js | I Vista de quien recibe los avisos | 11 |

Total: 90 pantallas. Las ilustraciones son la base provisional.

Nota técnica: Figma ignora la opacidad de una pintura recién enlazada a una variable;
`op_()` en `base.js` la aplica después sobre el nodo.

## Ajuste de contraste (14 nov, hecho directamente en Figma)
- Fondo de las secciones: `neutral/200`; notas de sección en `neutral/700`.
- Cada pantalla: borde exterior `neutral/300` de 1 px y sombra 0 · 8 · 32 al 8 %.
- Pantallas blancas con tarjetas blancas, tarjetas de persona u opciones (17): fondo `neutral/100`;
  sus tarjetas grises pasan a blanco con borde `neutral/200`.
- Componente Aviso, variante Info: fondo `primario/100` e icono `primario/500`.
- Componente Persona, variante Tarjeta: borde `neutral/300`.

Documento maestro (resumen, checklist contra lo que pidió la profesora, sistema y pendientes):
https://claude.ai/artifact/3MnKRpGz7j6v3vK5KEqCs3

## Componentes de ilustración y tarjeta, prototipo y páginas (14 nov)
Se ejecutan en este orden, cada uno como una llamada (los que usan helpers van después de `base.js`):

| Archivo | Qué hace |
|---|---|
| ajuste-contraste.js | El ajuste de contraste descrito arriba |
| comp3.js (con base.js) | Componentes Ilustración (9 temas × Grande y Compacta), Tarjeta (5 tipos, título y texto como propiedades) y Tarjeta de match (4 combinaciones de tramos, Persona anidada y expuesta) |
| reemplazo-ilustraciones-tarjetas.js | Cambia las ilustraciones y tarjetas armadas a mano de las 90 pantallas por instancias |
| prototipo.js | Conecta el prototipo: 130 enlaces, 7 avances automáticos, 47 «Atrás», 32 pestañas del menú, 13 cierres de capa y 7 recorridos de inicio. El mapa `L` dice a dónde lleva cada botón |
| ilustracion-mediana.js | Agrega el tamaño Mediana (412×340) a Ilustración y lo usa en los encabezados de altura media |
| paginas.js | Renombra y ordena las páginas como la entrega y actualiza el texto de la guía |

Páginas del archivo después de `paginas.js`: Investigación · primer y segundo corte, Wireframes · v2 (grises),
Sistema de diseño · Identidad, Sistema de diseño · Componentes, Pantallas en alta · v3 (con prototipo),
Wireframes · v1 (revisada 24 oct). Los scripts buscan las páginas por el nombre nuevo o por el anterior.

Ilustraciones: el dibujo de cada tema es provisional. Para cambiarlo por ilustraciones descargadas (por ejemplo de
Envato), se reemplaza el contenido de las 27 variantes del componente Ilustración y todas las pantallas se actualizan.
Los colores van enlazados a las variables de marca (`primario/*`, `candidata/*`, `ilustracion/piel-*`).

La página del prototipo de prueba del 8 de noviembre ya no está en el archivo de Figma; sus scripts siguen en
`../../prototipo-v3/` y el recorrido vigente es el de la página de pantallas en alta.
