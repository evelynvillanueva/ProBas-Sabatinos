#Índice de calidad del aire:

import requests 

def obtener_calidad_aire(lat, lon, api_key): 
    url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={api_key}"

    try: 
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        indice = datos["list"][0]["main"]["aqi"]

        descripcion = {
            1: "Buena", 
            2: "Aceptable",
            3: "Moderada", 
            4: "Mala", 
            5: "Muy mala" 
        }

        print(f"\n Índice de cañidad del aire: {indice}")
        print(f"Descripci+on: {descripcion.get(indice, 'Desconocido')}")
    
    except requests.exceptions.RequestException as e:
        print("Error de conexión:", e)
    except KeyError: 
        print("No se obtuvieron los dartos de la calidad del aire.")

