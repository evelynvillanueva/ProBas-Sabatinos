#Ejercicio 2: Diccionario de Países con Información Geográfica: Crea un diccionario que relacione países con su información geográfica. Cada país tiene un nombre, una lista de ciudades importantes y una lista de coordenadas (diccionarios con claves “latitud” y “longitud”). 

paises = {}

def registrar_pais(nombre_pais, ciudades, coordenadas):

    paises[nombre_pais] = {
        'ciudades': ciudades, 
        'coordenadas': coordenadas
    }

def listar_paises():
    if paises:
        for pais, info in paises.items():
            print(f"País: {pais}")
            print(f" Ciudades importantes: {', '.join(info['ciudades'])}")
            print(f" Coordenadas:")
            for coordenada in info['coordenadas']:
                print(f" Latitud: {coordenada['latitud']}, Longitud: {coordenada['longitud']}")
            print('-' * 30)
        else: 
            print("No se encontraron países registrados.")


def buscar_pais_por_ciudad(ciudad):

    print(f"Países con la ciudad'{ciudad}':")
    for pais, info in paises.items():
        if ciudad in info['ciudades']:
            print(f"- {pais}")
        print('-' * 30)

registrar_pais("México", ["Ciudad de México", "Guadalajara", "Monterrey"], [{"latitud": 19.4326, "longitud": -99.1332}, {"latitud": 20.6736, "longitud": -103.3440}, {"latitud": 25.6866, "longitud": -100.3161}])
registrar_pais("Italia", ["Roma", "Milán", "Venecia"], [{"latitud": 41.9028, "longitud": 12.4964}, {"latitud": 45.4642, "longitud": 9.1900}, {"latitud": 45.4408, "longitud": 12.3155}])
registrar_pais("Finlandia", ["Helsinki", "Oulu", "Tampere"], [{"latitud": 60.1699, "longitud": 24.9384}, {"latitud": 65.0125, "longitud": 25.4682}, {"latitud": 61.4982, "longitud": 23.7600}])

listar_paises()

buscar_pais_por_ciudad("Monterrey")
