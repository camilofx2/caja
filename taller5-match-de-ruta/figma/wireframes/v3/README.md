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
