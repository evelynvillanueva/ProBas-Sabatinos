#Consulta de apis y json en python. 

import requests 

base_url = "https://swapi.dev/api/people/"

personajes = []

response = requests.get(base_url)
if response.status_code == 200: 
    data = response.json()
    personajes = data['results']
else:
    print("No se logró consultar la información en la API.")

personajes_filtrados = [p for p in personajes if p['name'].startswith('L')]

print("Los persoanjes que empiezan con la letra 'L' son:\n")
for personaje in personajes_filtrados:
    print(f"Nombre: {personaje['name']}, Altura: {personaje['height']} cm")