# Red privada GSM 2G con Osmocom y USIM programable

Personalización de una USIM en GRSIMWrite, generación de K/OP/OPc con Python y registro del abonado 501 en una red Osmocom con LibreSDR Mini B220. Continuación del [proyecto con SIM comercial](https://josueeeoo-0.github.io/red-privada-2g-osmocom-sim-comercial/).

<img src="docs/assets/images/equipo.png" alt="Lector y USIM del laboratorio" width="500">

<img src="docs/assets/images/llamada-telefono.png" alt="Llamada entrante del número 100" width="250">

## Resultado documentado

- Identidad privada MCC 999 / MNC 99, IMSI `999990000000001`.
- Credenciales Milenage en la tarjeta y en OsmoHLR.
- Autenticación requerida en OsmoMSC.
- Abonado registrado con número `501` y llamada entrante del número `100`.
- A5/0 conservado en esta prueba: el enlace de radio no está cifrado.

## Leer el tutorial

| Etapa | Documento |
|---|---|
| Introducción y equipo | [Inicio](docs/index.md) |
| Python y claves | [Generación de claves](docs/01-claves.md) |
| Tabla de campos de GRSIMWrite | [Programación de la USIM](docs/02-usim.md) |
| YAML y radio UHD | [Configuración de red](docs/03-red.md) |
| Alta y credenciales | [OsmoHLR](docs/04-hlr.md) |
| Política de autenticación | [OsmoMSC](docs/05-msc.md) |
| Monitor y llamada | [Verificación](docs/06-prueba.md) |
| Bibliografía y alcance | [Referencias](docs/07-referencias.md) |

## Publicar la página

Seguir [PUBLICAR_EN_GITHUB.md](PUBLICAR_EN_GITHUB.md). Incluye creación del repositorio, subida con Git y **Settings → Pages → GitHub Actions**. El sitio conserva el diseño editorial del proyecto anterior: papel, café, modo oscuro y tipografía Newsreader/Fraunces.

## Contenido del paquete

```text
.github/workflows/pages.yml   # Compilación y publicación automática
docs/                        # Tutorial e imágenes públicas
scripts/generar_claves.py     # Código usado en la práctica
scripts/verificar_sitio.py    # Verificación de enlaces internos
mkdocs.yml                   # Configuración y navegación
requirements.txt             # Versiones del sitio
PUBLICAR_EN_GITHUB.md         # Instrucciones de publicación
assets-manifest.json         # Correspondencia con las 30 imágenes originales
site/                        # Copia compilada incluida solo en la entrega ZIP
```

`site/` queda excluido de Git: Actions lo recompila. El paquete no contiene el entorno virtual ni fotografías originales con claves visibles. Las imágenes publicables tienen redacciones opacas donde corresponde; no se modifica la evidencia original.

No subir `credenciales.txt`, volcados privados ni claves. El generador se conserva como se utilizó: ejecutarlo otra vez sobrescribe sus credenciales. Las transcripciones sin captura están identificadas en el capítulo del HLR.

## Créditos

Autor: **Josue Giraldo Moya**. Diseño adaptado de su primer sitio MkDocs Material. Código y documentación propios bajo la licencia MIT incluida; marcas, normas y programas citados pertenecen a sus titulares. Uso educativo del espectro con aislamiento de RF o autorizaciones correspondientes.
