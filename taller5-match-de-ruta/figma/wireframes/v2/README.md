# Wireframes v2 · después de la revisión del 24 de octubre

Scripts que construyen la página **“Wireframes v2”** del archivo de Figma (Plugin API vía `use_figma`).
La versión 1 queda intacta en la página “Wireframes v1 · revisada 24 oct”.

Cómo se ejecutan: `helpers.js` + un archivo de flujos por llamada (`d1.js` … `d4.js`), pegados uno tras otro.
`flow()` reemplaza en su sitio una sección que ya tenga el mismo nombre.

| Archivo | Secciones | Pantallas |
|---|---|---|
| d1.js | 00 Pautas · A Bienvenida, registro e ingreso · B Verificación con correo | 1 + 10 + 6 |
| d2.js | C Verificación por círculo · D Rutas | 8 + 10 |
| d3.js | E Match · F Trayecto activo | 10 + 11 |
| d4.js | G Confianza · H Perfil y privacidad · I Vista de quien recibe los avisos | 7 + 9 + 11 |

Total: 82 pantallas.

Ajuste posterior hecho directamente en Figma: las pantallas sin menú inferior que tenían
`align:'top'` y espacio libre se centraron entre la barra superior (o el indicador de pasos) y las acciones,
como pidió la profesora (“el stepper arriba y centramos la información”). Los chats se mantienen alineados abajo.
