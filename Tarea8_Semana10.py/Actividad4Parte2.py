#Pronóstico del clima para los próximos 5 días.

import requests 
import json
from collections import defaultdict
from datetime import datetime 

def obtener_pronostico(ciudad_api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        pronostico_diario = defaultdict(lambda: {"temp_min": float("inf"), "temp_max": float("-inf")})

        for entrada in datos["list"]: 
            fecha = entrada["dt_txt"].splt(" ")[0]
            temp_min = entrada["main"]["temp_min"]
            temp_max = entrada["main"]["temp_max"]

            if temp_min < pronostico_diario[fecha]["temp_min"]:
                pronostico_diario[fecha]["temp_min"] = temp_min
            
            if temp_max < pronostico_diario[fecha]["temp_min"]:
                pronostico_diario[fecha]["temp_max"] = temp_max
        
        print(f"\n Pronóstico para {ciudad}: \n")
        for fecha in sorted (pronostico_diario.keys())[:5]:
            temp_min = pronostico_diario[fecha]["temp_min"]
            temp_max = pronostico_diario[fecha]["temp_max"]
            print(f"{fecha}: Mínima: {temp_min:.1f}°C / Máxima: {temp_max:.1f}°C")
        archivo_json = f"pronostico_{ciudad.lower()}"
        with open(archivo_json, "w", encording="utf-8") as f: 
            json.dump(pronostico_diario, f, indent=4, ensure_ascii=False)
        
        print(f"\n Datos guardados en '{archivo_json}'")
    
    except requests.exceptions.HTTPError as e: 
        if respuesta.status_code == 404:
            print("Ciudad no encontrada.")
        else: 
            print(f"Error HTTP: {respuesta.status_code}")
    except requests.exceptions.RequestsException as e: 
        print("Error de conexión", e)
    except KeyError:
        print("Error al procesar lls datos del servidor.")

api_key = "123abc456def789ghi0jkl"

ciudad = input("Intoduzca en nombre de la ciudad: ")

obtener_pronostico(ciudad, api_key)


