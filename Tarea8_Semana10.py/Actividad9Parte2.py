#Mapeo de coordenadas geográficas.

import requests

def obtener_coordenadas(ciudad, api_key): 
    url = f"https://api.weathermap.org/geo/1.0/direct?q={ciudad}&limit=1&appid={api_key}"

    try: 
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        datos = respuesta.json()

        if not datos: 
            print("Ciudad no encontrada.")
            return None, None
        
        nombre = datos[0]["name"]
        lat = datos[0]["lat"]
        lon = datos[0]["lon"]

        print(f"\n Ciudad: {nombre}")
        print(f"Coordenadas: lat={lat}, lon={lon}")
        return lat, lon
    
    except requests.exceptions.RequestException as e:
        print("Error de conexción:", e)
        return None, None

