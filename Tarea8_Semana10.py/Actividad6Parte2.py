#Historial del clima.

import requests 
import time 
from datetime import datetime, timedelta 

def obtener_coordenadas(ciudad, api_key): 
    url = "https://api.openweathermap.org/geo/1.0/direct?q={ciudad}&limit=1&appid={api_key}"
    respuesta = requests.get(url)
    datos = respuesta.json()
    if datos: 
        return datos[0]["lat"], datos[0]["lon"]
    else: 
        raise ValueError("Ciudad no encontrada.")
    
def obtener_historial(api_key, ciudad):
   
    try: 
        lat, lon = obtener_coordenadas(ciudad, api_key)
        print(f"Coordenadas de {ciudad}: lat={lat}, lon={lon}")

        print(f"\n Historial del clima en {ciudad} (en los últimos 7 días): \n")

        for i in range(1, 8): 
            fecha = datetime.utcnow() - timedelta(days=i)
            timestamp = int(fecha.timestamp())

            url = (
                f"https://api.openweathermap.org/data/3.0/onecall/timemachine?"
                f"lat={lat}&lon={lon}&lon={timestamp}&appid={api_key}&units=metric"
            )

            respuesta = requests.get(url)
            respuesta.raise_for_status()
            datos = respuesta.json()

            temps = [hora["temp"] for hora in datos.get("hourly", [])]
            if temps: 
                temp_promedio = sum(temps) / len(temps)
                print(f"{fecha.strtime('%Y-%m-%d')}: {temp_promedio:.1f}°C promedio")
            else: 
                print(f"{fecha.strtime('%Y-%m-%d')}: No hay datos.")
            
            time.sleep(1)
    
    except ValueError as ve: 
        print("X", ve)
    except requests.exceptions.RequestException as e: 
        print("Error de conexión:", e)

api_key = "123abc456def789ghi0jkl"

ciudad = input("Introduzca el nombre de la ciudad: ")

obtener_historial(api_key, ciudad)


