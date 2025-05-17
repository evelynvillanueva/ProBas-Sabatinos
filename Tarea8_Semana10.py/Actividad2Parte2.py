#Información del clima actual.

import requests 

ciudad = input("Introduzca el nombre de la ciudad: ")

def obtener_clima(ciudad, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&appid={api_key}&units=metric&lang=es"

    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()

        datos = respuesta.json()

        temperatura = datos["main"]["temp"]
        humedad = datos["main"]["humidity"]
        descripcion = datos["weather"][0]["descrption"]

        print(f"\n Ciudad: {ciudad}")
        print(f" Temperatura: {temperatura}")
        print(f" Humedad: {humedad}")
        print(" Clima: {descripcion}")

    except requests.excepcions.HTTPERROR:
        if respuesta.status_code == 404:
            print(f"Ciudad no encontrada.")
        else:
            print(f"Error HTTP: {respuesta.status_code}")
    except requests.exceptions.RequestsException as e: 
        print(f"Error de conexión:, e")
    except KeyError: 
        print("Error: no se pudo conectar al servidor.")

api_key = "123abc456def789ghi0jkl"

obtener_clima(ciudad, api_key) 