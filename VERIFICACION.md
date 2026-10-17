# Verificación de la entrega

- Compilación: `python -m mkdocs build --strict`, exit 0.
- Enlaces: `python scripts/verificar_sitio.py`, 10 HTML y 267 enlaces locales correctos.
- Cobertura: 30 imágenes originales representadas en el tutorial; 9 páginas de documentación.
- Navegador: portada y tabla de parámetros revisadas en escritorio; portada sin desbordamiento en 390 px; búsqueda Milenage con 6 documentos; modo oscuro y claro comprobados.
- Redacciones: claves, códigos de administración e IMEI ocultos en las copias donde corresponde; originales fuera de esta entrega.
- Fuentes: ningún literal hexadecimal de 128 bits encontrado en los archivos de texto publicables; sintaxis de los dos scripts Python comprobada sin generar credenciales.
- Estructura: imagen inicial y final de USIM en orden; transcripción de comandos sin captura identificada antes de Screenshot_13.
- Git: diff revisado y `git diff --check` sin errores después de normalizar los finales de línea.
- Versiones: se conservan MkDocs 1.6.1 y Material 9.7.7 del proyecto anterior. El compilador imprime un aviso informativo del proveedor sobre MkDocs 2.0; esta entrega no utiliza MkDocs 2.0.
- Límite: no se ha ejecutado el despliegue en GitHub. La publicación requiere crear el repositorio y seleccionar GitHub Actions en Pages según PUBLICAR_EN_GITHUB.md.
