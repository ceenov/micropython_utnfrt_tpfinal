import requests
import json

def enviar_datos(temp, hum, datos_hora):
    # Reemplaza con la URL de tu script de Google
    url = 'https://script.google.com/macros/s/AKfycbzmvpGL1soNrFPgEElNfD2LKFQIqZUO65480PD2kfOUKO3OSfWg8YLWtlJsPPse4oSi/exec'  
    headers = {'Content-Type': 'application/json'}
    data = {
        'datos_hora': datos_hora,
        'temperature': temp,
        'humidity': hum
    }
    #try:
    response = requests.post(url, headers=headers, data=json.dumps(data))
    #response.raise_for_status()  # Esto lanzará una excepción para códigos de estado HTTP 4xx/5xx
    print('Datos enviados exitosamente')
        
    if response.status_code == 200:
        print('Datos enviados exitosamente')
    else:
        print('Error al enviar los datos:', response.status_code, response.text)
    
    #except requests.exceptions.RequestException as e:
    #    print('Error al enviar los datos:', e)