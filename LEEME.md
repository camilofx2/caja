# Caja: tu app de finanzas independiente

**Tu app:** https://camilofx2.github.io/caja/  ·  Código: github.com/camilofx2/caja  ·  Datos: Supabase, proyecto `caja`

Caja es una app web instalable (PWA). Se instala en el iPhone y en el Mac como cualquier app, funciona sin internet
y sincroniza tus datos entre ambos con **Supabase** (base de datos privada y gratuita). Se publica gratis con **GitHub Pages**.
No depende de Claude: Claude solo te ayuda a hacerle cambios.

Contenido de la carpeta:

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La app completa |
| `config.js` | Los 2 datos de tu Supabase (lo llenas una vez) |
| `supabase.sql` | Crea la tabla privada de tus datos |
| `manifest.webmanifest`, `sw.js`, `icons/` | Permiten instalarla, verla sin internet y mostrar tu firma como ícono |
| `configurar-github.command` | Se usa una sola vez para conectar con GitHub |
| `publicar.command` | Doble clic para subir cada actualización |

---

## Paso 1 · Base de datos (Supabase), unos 5 minutos
1. Entra a **supabase.com**, crea una cuenta gratis y toca **New project** (nombre: `caja`, región: *South America (São Paulo)*).
   Guarda la contraseña de la base de datos en un lugar seguro. La app no la necesita.
2. En el menú, abre **SQL Editor → New query**, pega todo el contenido de `supabase.sql` y toca **Run**.
3. Abre **Project Settings → API** y copia **Project URL** y **anon public key**.
   Pégalos en `config.js`, o pégalos en el chat de Claude y él los pone por ti.
   *(La anon key está hecha para ir dentro de la app. Tus datos los protege el inicio de sesión.)*

## Paso 2 · Publicarla (GitHub Pages), unos 10 minutos, una sola vez
1. Crea una cuenta en **github.com** y luego **New repository**: nombre `caja`, **Public**, sin archivos iniciales.
2. Crea un token: tu foto → **Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
   En *Repository access* elige solo `caja`, y en *Permissions → Contents* elige **Read and write**. Copia el token.
3. Haz doble clic en **`configurar-github.command`** (si macOS lo bloquea: clic derecho → Abrir).
   Pega la dirección del repositorio y, cuando pida *Password*, pega el **token**.
4. En GitHub abre tu repositorio → **Settings → Pages → Branch: `main` / `(root)` → Save**.
   En 1–2 minutos tu app estará en **`https://TU-USUARIO.github.io/caja/`**.
5. En Supabase abre **Authentication → URL Configuration** y pon esa dirección en **Site URL**
   (para que el correo de confirmación de cuenta te devuelva a la app).

## Paso 3 · Pasar tus datos desde la versión de Claude
1. Abre la versión de Claude → **Ajustes → Descargar copia de seguridad**.
2. Abre tu nueva app → **Crear cuenta nueva** (confirma el correo) → **Entrar**.
3. **Ajustes → Restaurar copia de seguridad** y elige el archivo. Tus cuentas, movimientos, metas, deudas y tu mes base pasan tal cual.

## Paso 4 · Instalarla
- **iPhone:** abre la dirección en **Safari** → botón **Compartir** → **Agregar a pantalla de inicio**.
- **Mac:** ábrela en **Safari** → menú **Archivo → Agregar al Dock**. Queda como app propia en el Dock y en Launchpad.

Entra con la misma cuenta en los dos y verás siempre lo mismo.

## Cómo seguir mejorándola
1. Pídele a Claude el cambio en el chat. Él edita los archivos de esta carpeta.
2. Haz doble clic en **`publicar.command`**.
3. Cierra y vuelve a abrir la app en el iPhone y en el Mac: ya tendrás la nueva versión. Tus datos no se tocan.

## Bueno saberlo
- **Tus datos** viven en tu Supabase, protegidos por tu usuario. El código es público en GitHub, pero no contiene ninguna cifra tuya.
- **Sin internet** la app abre y registra normalmente. Los cambios se envían solos cuando vuelve la conexión.
- **Supabase gratis pausa proyectos sin uso por 7 días.** Si usas la app a diario no pasa. Si pasa, entra a supabase.com y toca *Restore*.
- **Copia de seguridad:** de vez en cuando descarga una en Ajustes.
