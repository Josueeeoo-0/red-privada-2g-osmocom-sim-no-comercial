# 7. Referencias, evidencia y alcance

## Fuentes del proyecto

Este tutorial reúne las capturas de la sesión, las notas del tramo sin fotografía y la documentación del primer laboratorio. Las fuentes técnicas se enlazan junto a cada explicación para facilitar su comprobación.

| Fuente | Qué respalda |
|---|---|
| [Proyecto anterior de Josue Giraldo](https://josueeeoo-0.github.io/red-privada-2g-osmocom-sim-comercial/) | Diseño de referencia, entorno DragonOS, radio UHD y prueba de llamadas |
| [Repositorio del proyecto anterior](https://github.com/Josueeeoo-0/red-privada-2g-osmocom-sim-comercial) | Estructura MkDocs Material y estilos de origen |
| [UIT, boletín operacional 1156, p. 5](https://www.itu.int/dms_pub/itu-t/opb/sp/T-SP-OB.1156-2018-OAS-PDF-E.pdf) | MCC 999 y MNC internos para redes privadas; valores 99/999 para ejemplos |
| [ETSI TS 135 206 V18.0.0, §4.1](https://www.etsi.org/deliver/etsi_ts/135200_135299/135206/18.00.00_60/ts_135206v180000p.pdf) | Milenage y derivación de OPc a partir de K y OP |
| [ETSI TS 131 102 V12.10.0](https://www.etsi.org/deliver/etsi_ts/131100_131199/131102/12.10.00_60/ts_131102v121000p.pdf) | Archivos USIM: identidad, ACC, AD y selectores de PLMN |
| [ETSI TS 151 011 V4.15.0, §10](https://www.etsi.org/deliver/etsi_ts/151000_151099/151011/04.15.00_60/ts_151011v041500p.pdf) | Archivos del perfil SIM para GSM |
| [Código de pySim: legacy/cards.py](https://github.com/osmocom/pysim/blob/master/pySim/legacy/cards.py) | Tratamiento de EF.AD y longitud del MNC |
| [Manual de pySim-shell: verify_adm](https://downloads.osmocom.org/docs/pysim/master/html/shell.html#verify-adm) | Administración de la tarjeta y bloqueo por intentos erróneos |
| [iothon: Writing your own SIM cards](https://github.com/iothon/operator/wiki/Writing-your-own-SIM-cards) | Uso práctico de GRSIMWrite, listas PLMN y Same with LTE |
| [OsmoHLR, manual 1.9.2](https://downloads.osmocom.org/docs/osmo-hlr/1.9.2/osmohlr-usermanual.pdf) | Datos de abonado y uso de Milenage en 2G/3G |
| [OsmoHLR, referencia VTY](https://downloads.osmocom.org/docs/osmo-hlr/master/osmohlr-vty-reference.pdf) | Comandos de alta, credenciales y permisos CS |
| [OsmoMSC, manual](https://downloads.osmocom.org/docs/osmo-msc/master/osmomsc-usermanual.pdf) | Autenticación requerida y cifrado A5 |
| [OsmoMSC, referencia VTY](https://downloads.osmocom.org/docs/osmo-msc/master/osmomsc-vty-reference.pdf) | Consola y comandos de configuración y consulta |

Las normas ETSI/3GPP y los manuales de Osmocom son las referencias técnicas. La guía de iothon documenta la interfaz del programa; no garantiza el comportamiento de cualquier COS genérico. Los enlaces `master` reflejan documentación que puede cambiar.

## Procedencia de las imágenes

Se incluyen **30 capturas y fotografías** aportadas por el autor:

| Grupo original | Uso en el sitio |
|---|---|
| `images_codigo_python` (5) | Preparación del entorno y generación de claves |
| `images_configuracion_usim` (2) | Estado anterior y posterior de GRSIMWrite |
| `images` (21) | Red, HLR, MSC, monitor y llamada |
| `images_equipo` (2) | Introducción y resultado en el teléfono |

La consulta del IMSI inexistente y los comandos iniciales de alta no tienen fotografía. Se identifican como transcripción, antes de retomar Screenshot_13. Esa captura del HLR ya incluye una actualización de ubicación posterior: su fecha no se presenta como el instante de creación del abonado.

## Datos ocultos en las copias públicas

Se ocultan K, OP, OPc, códigos de administración y el IMEI donde aparecen. Los originales se conservan fuera del paquete publicable. No se incluye `credenciales.txt`; los comandos utilizan `TU_K` y `TU_OPC` como marcadores.

## Alcance de la validación

| Observado | No demostrado en este material |
|---|---|
| Lectura de la tarjeta personalizada | Lectura de retorno de todas las claves protegidas |
| Credenciales Milenage en el HLR | Captura completa del intercambio de autenticación |
| `authentication required` en el MSC | Persistencia de ese ajuste tras otro osmo-nid-start |
| Abonado 501 en el monitor | Datos GPRS o acceso LTE |
| Llamada entrante del número 100 | Audio bidireccional y llamada contestada |
| Notificación de bienvenida recibida | Envío de SMS desde el teléfono |

## Uso del espectro

Este proyecto es un laboratorio educativo. Una identidad privada MCC/MNC no concede derechos sobre frecuencias. GSM850 y ARFCN 190 describen la configuración utilizada; no son una recomendación de un canal libre. La experimentación debe realizarse con aislamiento de RF o bajo las autorizaciones correspondientes. La prueba conserva **A5/0**, sin cifrado de radio.
