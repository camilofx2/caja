#!/bin/bash
# Doble clic para subir la última versión de Caja a internet (GitHub Pages).
cd "$(dirname "$0")" || exit 1
git add -A
git commit -m "Actualizar Caja $(date '+%Y-%m-%d %H:%M')" >/dev/null 2>&1 || echo "No hay cambios nuevos."
if git push -u origin main; then
  echo ""
  echo "✅ Publicado. En 1–2 minutos la app se actualiza en tu iPhone y tu Mac."
else
  echo ""
  echo "❌ No se pudo publicar. Revisa tu conexión o la configuración de GitHub (ver LEEME.md)."
fi
read -n 1 -s -r -p "Presiona cualquier tecla para cerrar…"
