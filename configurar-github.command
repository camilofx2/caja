#!/bin/bash
# Doble clic UNA sola vez para conectar esta carpeta con tu repositorio de GitHub y publicar la app.
cd "$(dirname "$0")" || exit 1
echo "== Configurar publicación de Caja en GitHub Pages =="
echo ""
if [ -z "$(git config --global user.name)" ]; then
  read -r -p "Tu nombre (para el historial de cambios): " N; git config --global user.name "$N"
fi
if [ -z "$(git config --global user.email)" ]; then
  read -r -p "Tu correo de GitHub: " E; git config --global user.email "$E"
fi
git config --global credential.helper osxkeychain
[ -d .git ] || git init -q
git checkout -q -B main
read -r -p "Pega la dirección de tu repositorio (ej: https://github.com/tuusuario/caja.git): " URL
git remote remove origin 2>/dev/null
git remote add origin "$URL"
git add -A
git commit -q -m "Primera versión de Caja" || true
echo ""
echo "Ahora GitHub te pedirá usuario y contraseña."
echo "En 'Password' pega tu TOKEN de GitHub (no tu contraseña). Se guarda en tu llavero y no te lo vuelve a pedir."
echo ""
if git push -u origin main; then
  echo ""
  echo "✅ Listo. Activa GitHub Pages (Settings → Pages → Branch: main / root) si aún no lo hiciste."
  echo "   Desde ahora, para actualizar solo haz doble clic en publicar.command."
else
  echo "❌ No se pudo subir. Revisa la dirección del repositorio y el token (ver LEEME.md)."
fi
read -n 1 -s -r -p "Presiona cualquier tecla para cerrar…"
