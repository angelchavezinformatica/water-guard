# Water Guard

**Water Guard** es un sistema para el control remoto de una bomba de agua a través de una interfaz web. Permite encender y apagar la bomba desde cualquier dispositivo en una red, facilitando la gestión del riego y el suministro de agua en diferentes entornos.

## Características

- **Control remoto**: Enciende y apaga la bomba de agua desde una página web.
- **Monitorización**: Visualiza el estado actual de la bomba (encendido/apagado).
- **Interfaz amigable**: Accede a la interfaz web desde cualquier dispositivo en la misma red.

## Tecnologías utilizadas

- **Frontend**:
  - HTML5
  - CSS3
  - JavaScript
- **Backend**:
  - Micropython
- **Hardware**:
  - Microcontrolador ESP8266
  - Modulo relé para el control de la bomba de agua

## Instalación

1. **Clona este repositorio** en tu máquina local:

   ```bash
   git clone https://github.com/angelchavezinformatica/water-guard.git
   cd water-guard
   ```

<!-- 1. **Configura el hardware**:

   - Conecta el microcontrolador a la bomba de agua utilizando un relé.
   - Configura el microcontrolador para comunicarse con el servidor a través de Wi-Fi. -->

1. **Configura las variables**:

   - Crea un archivo `environ.py` en el directorio raíz del proyecto.
   - Agrega las siguientes variables (ejemplo):

     ```env
      WLAN_SSID = "mi-red-wifi"
      WLAN_PASSWORD = "mi-contraseña"
     ```

1. **Ejecuta la aplicación**:

   - Copia los archivos al ESP8266 y ejecuta.
