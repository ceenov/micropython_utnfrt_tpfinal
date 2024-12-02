# Proyecto de Monitoreo de Temperatura y Humedad con ESP32

Este proyecto utiliza un ESP32 para leer datos de temperatura y humedad de un sensor DHT22, mostrar los datos en una pantalla OLED SSD1306 y enviarlos a una hoja de cálculo de Google y a una hoja de cálculo de Excel Online. Además, se obtiene la hora actual desde la API de World Time.

## Diagrama Esquemático
![Esquema del Circuito](ESP32_DHT22_OledLCD.png)

## Simulación del Circuito
Puedes explorar y probar este proyecto mediante una simulación interactiva en Wokwi:  
**[Ver Simulación en Wokwi](https://wokwi.com/projects/416204083798477825)**

## Requisitos

- ESP32 Dev Kit V1
- Sensor DHT22
- Pantalla OLED SSD1306
- Conexión a Internet
- Cuenta de Google con acceso a Google Sheets
- Cuenta de Microsoft con acceso a Excel Online
- Bibliotecas de Python: `urequests`, `gspread`, `oauth2client`, `requests`, `msal`

## Instalación

1. **Instalar MicroPython en el ESP32**:
   Sigue esta guía para instalar MicroPython en tu ESP32.

2. **Conectar el DHT22 y la pantalla OLED al ESP32**:
   - Conecta el pin de datos del DHT22 a un pin GPIO del ESP32 (por ejemplo, GPIO 4).
   - Conecta el pin VCC del DHT22 a 3.3V del ESP32.
   - Conecta el pin GND del DHT22 a GND del ESP32.
   - Conecta el pin SCL del OLED al pin GPIO 22 del ESP32.
   - Conecta el pin SDA del OLED al pin GPIO 21 del ESP32.

3. **Transferir los archivos al ESP32**:
   Usa Thonny, ampy o WebREPL para transferir los archivos `.py` al ESP32.

## Archivos del Proyecto

- `main.py`: Archivo principal que ejecuta el programa.
- `sensor_dht22.py`: Contiene las funciones para leer la temperatura y la humedad del sensor DHT22.
- `display/oled_display.py`: Contiene las funciones para mostrar los datos en la pantalla OLED SSD1306.
- `obtener_hora.py`: Contiene la función para obtener la hora actual desde la API de World Time.
- `send_data.py`: Contiene la función para enviar los datos a una dirección web.
- `google_sheets.py`: Contiene la función para cargar los datos en una hoja de cálculo de Google Sheets.
- `microsoft_excel.py`: Contiene la función para cargar los datos en una hoja de cálculo de Excel Online.

## Uso

1. **Conectar a WiFi**:
   La función `conectar_wifi` se encarga de conectar el ESP32 a la red WiFi.

2. **Obtener la hora actual**:
   La función `obtener_hora_actual` obtiene la hora actual desde la API de World Time.

3. **Leer datos del sensor DHT22**:
   Las funciones `medir_temperatura` y `medir_humedad` leen los datos de temperatura y humedad del sensor DHT22.

4. **Mostrar datos en la pantalla OLED**:
   La función `mostrar_datos` muestra los datos en la pantalla OLED SSD1306.

5. **Enviar datos a Google Sheets y Excel Online**:
   Las funciones `cargar_datos` en `google_sheets.py` y `microsoft_excel.py` envían los datos a las respectivas hojas de cálculo.

## Funcionalidad en Desarrollo

### Enviar los datos de las mediciones a una hoja de cálculos de Google

**[Ver Hoja de Calculo](https://docs.google.com/spreadsheets/d/1pcTxw9gxgdikChK3UODAOqdXHpwWqttbv10XZhzlk24/edit?gid=0#gid=0)**

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o un pull request para discutir cualquier cambio que te gustaría hacer.



