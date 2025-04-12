import requests

def obtener_naves_filtradas():
    url = "https://swapi.dev/api/starships/"
    naves_filtradas = []

    while url: 
        respuesta = requests.get(url)
        datos = respuesta.json()

        for nave in datos['results']: 
            carga_str = nave.get('cargo_capacity', '0').replace(',', '')
            try: 
                carga = int(carga_str)
                if carga > 100000:
                    naves_filtradas.append({'nombre': nave['name'], 'modelo': nave['model']
                                                            })
            except ValueError: 
                continue 

        url = datos.get('next')

    return naves_filtradas

naves = obtener_naves_filtradas()
for nave in naves:
    print(f"Nombre: {nave['nombre']} - Modelo: {nave['modelo']}")