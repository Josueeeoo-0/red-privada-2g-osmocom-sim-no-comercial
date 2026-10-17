<p class="project-kicker">Redes móviles · Laboratorio GSM · Osmocom</p>

# Red privada 2G con una USIM programada por mí

<p class="project-lead">De una tarjeta en blanco a un abonado registrado: generación de claves, personalización en GRSIMWrite y una llamada entrante en una red GSM con LibreSDR Mini B220.</p>

Este proyecto continúa el [laboratorio anterior con una SIM comercial](https://josueeeoo-0.github.io/red-privada-2g-osmocom-sim-comercial/). Se conserva DragonOS, la pila Osmocom gestionada por `osmo-nid` y la Mini B220 mediante UHD. La diferencia está en la tarjeta: ahora sus credenciales se generan y se programan para que el núcleo de red pueda comprobarlas.

<div class="result-strip">USIM programable · Milenage · PLMN 999 / 99 · Abonado 501 · Llamada de prueba desde 100</div>

## El equipo y el resultado

<figure markdown="1">
[![Lector de tarjetas y USIM programable utilizados en el laboratorio](assets/images/equipo.png){ width="500" loading="lazy" }](assets/images/equipo.png)
<figcaption>Material de personalización: lector USB y tarjeta programable, junto al ordenador. · Pulsa la imagen para ampliarla.</figcaption>
</figure>

<figure markdown="1">
[![Teléfono con JOSUE_CORP y llamada entrante del número 100](assets/images/llamada-telefono.png){ width="300" loading="lazy" }](assets/images/llamada-telefono.png)
<figcaption>Resultado final: llamada entrante del número 100. La notificación inferior muestra el mensaje de bienvenida de DragonOS. · Pulsa la imagen para ampliarla.</figcaption>
</figure>

## Qué se hizo

1. Generar **K, OP y OPc** con Python.
2. Escribir la identidad del abonado y sus credenciales en la tarjeta mediante **GRSIMWrite 4.4.10**.
3. Hacer coincidir el PLMN de la tarjeta y el de la red: **MCC 999 / MNC 99**.
4. Crear el abonado **501** en OsmoHLR y registrar sus claves Milenage.
5. Configurar **autenticación obligatoria** en OsmoMSC.
6. Observar el registro del teléfono y generar una llamada de prueba.

## Equipo y software

| Elemento | Utilizado |
|---|---|
| Sistema | DragonOS 26.01 |
| Pila celular | Osmocom con el envoltorio `osmo-nid` |
| Radio | LibreSDR Mini B220, controlador UHD |
| Terminal | Xiaomi Redmi 13C, configurado en solo 2G |
| Tarjeta | USIM programable con COS preinstalado, compatible con GSM según el proveedor |
| Lector | Alcorlink USB Smart Card Reader, interfaz PC/SC |
| Personalización | GRSIMWrite, SIM Personalize tools 4.4.10 |
| Claves | Python, PyCryptodome y `secrets` |

La tarjeta es leída por **el teléfono**. La B220 transporta las señales de radio; el HLR almacena las credenciales y el MSC coordina el registro y la autenticación.

## Recorrido del tutorial

| Etapa | Contenido |
|---|---|
| [1. Generación de claves](01-claves.md) | Entorno Python, código y credenciales privadas |
| [2. Programación de la USIM](02-usim.md) | Pantalla inicial, tablas de valores y pantalla final |
| [3. Configuración de la red](03-red.md) | Respaldo, YAML, PLMN y arranque UHD |
| [4. Registro en OsmoHLR](04-hlr.md) | Alta del IMSI, número 501 y Milenage |
| [5. Autenticación en OsmoMSC](05-msc.md) | Cambio de `optional` a `required` |
| [6. Registro y llamada](06-prueba.md) | Monitor de abonados y llamada al teléfono |
| [7. Referencias y alcance](07-referencias.md) | Fuentes primarias y límites de la evidencia |

!!! note "Qué demuestra este laboratorio"
    Se documentan el registro del abonado y una llamada entrante con autenticación requerida en el MSC. Se conserva `encryption a5 0`: **el enlace de radio no está cifrado**. No se presenta como una validación de LTE, de datos móviles ni de audio bidireccional.

Las capturas públicas conservan los pasos reales. Las claves y el IMEI se han ocultado en las copias publicables. El tramo de alta sin fotografías se identifica expresamente como transcripción.
