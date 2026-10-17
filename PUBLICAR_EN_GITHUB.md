# Publicar el proyecto en GitHub Pages

El diseño sigue usando **MkDocs Material**, como el primer proyecto. El paquete contiene las fuentes, las imágenes públicas y un workflow de GitHub Actions. La carpeta `site/` es una compilación de consulta: GitHub vuelve a construirla desde las fuentes.

## Paso 1. Descomprimir y elegir la carpeta correcta

Extrae el ZIP. Entra en la carpeta **red-privada-2g-osmocom-sim-no-comercial**. Debes ver `mkdocs.yml`, `README.md`, `requirements.txt`, `docs`, `scripts` y `.github` en su raíz.

No publiques la carpeta exterior de fotografías originales. No incluyas `credenciales.txt`. La carpeta `.github` está incluida en el ZIP; algunas aplicaciones pueden ocultar carpetas que comienzan con punto.

## Paso 2. Crear un repositorio vacío

En GitHub, dentro de la cuenta **Josueeeoo-0**, crea un repositorio público llamado:

```text
red-privada-2g-osmocom-sim-no-comercial
```

Para seguir los comandos siguientes, créalo sin README, licencia ni gitignore automáticos: el paquete ya los incluye. Si eliges otro nombre o cuenta, actualiza `site_url`, `repo_url` y `repo_name` en `mkdocs.yml` antes de subir.

## Paso 3. Subir el contenido con Git

Abre PowerShell en la carpeta descomprimida que contiene `mkdocs.yml`:

```powershell
git init
git branch -M main
git add .
git commit -m "Documentar red GSM 2G con USIM programable"
git remote add origin https://github.com/Josueeeoo-0/red-privada-2g-osmocom-sim-no-comercial.git
git push -u origin main
```

La autenticación se realiza mediante Git Credential Manager o el método configurado en tu equipo. No pegues tokens en el README ni en los comandos públicos.

## Paso 4. Seleccionar GitHub Actions en Pages

En el repositorio: **Settings → Pages → Build and deployment → Source → GitHub Actions**.

Esta es la diferencia respecto al workflow anterior: aquel usaba `mkdocs gh-deploy` para escribir una rama **gh-pages**. El paquete actual compila el sitio y lo publica con las acciones oficiales de Pages. **No selecciones Deploy from a branch** para este paquete.

## Paso 5. Ejecutar y comprobar el despliegue

Ve a **Actions → Publicar documentación → Run workflow → main → Run workflow**. Si el primer intento automático falló porque todavía no habías activado Pages, vuelve a ejecutarlo desde aquí.

Cuando `build` y `deploy` terminen correctamente, Pages mostrará el enlace publicado. Con el nombre anterior, la dirección prevista es:

[josueeeoo-0.github.io/red-privada-2g-osmocom-sim-no-comercial/](https://josueeeoo-0.github.io/red-privada-2g-osmocom-sim-no-comercial/)

Es una dirección prevista, no una confirmación de que ya esté publicado. El ZIP se entrega sin subir archivos ni cambiar tu cuenta de GitHub.

## Paso 6. Actualizar la página

Edita los Markdown de `docs/`, después:

```powershell
git add .
git commit -m "Actualizar documentación"
git push
```

Cada push a `main` ejecuta el workflow. No necesitas volver a subir el ZIP.

## Vista previa local

Con Python 3.13 instalado, desde la raíz:

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m mkdocs serve
```

Abre la dirección local que muestra MkDocs, normalmente `http://127.0.0.1:8000/`. No necesitas activar el entorno de PowerShell. Para compilar y revisar enlaces:

```powershell
.\.venv\Scripts\python.exe -m mkdocs build --strict
.\.venv\Scripts\python.exe scripts/verificar_sitio.py
```

La búsqueda y las fuentes web se comprueban mejor sirviendo el sitio por HTTP; abrir un HTML directamente desde el disco no equivale a la publicación.

## Si algo falla

| Problema | Qué revisar |
|---|---|
| No aparece el workflow | `.github/workflows/pages.yml` debe estar en la raíz del repositorio |
| Error al configurar Pages | Activar Source: GitHub Actions y volver a ejecutar |
| Sitio con imágenes rotas | No mover `docs/assets/images`; conservar los nombres |
| Error 404 en la raíz publicada | Nombre del repositorio, URL y job deploy |
| Solo aparece README | Abrir el enlace de Pages, no la pestaña Code del repositorio |

Fuentes oficiales: [workflow personalizado de GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) y [publicación con Material for MkDocs](https://squidfunk.github.io/mkdocs-material/publishing-your-site/).
