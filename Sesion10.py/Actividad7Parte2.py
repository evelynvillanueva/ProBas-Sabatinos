import os
import pandas as pd
import requests


url = "https://swapi.dev/api/films"
response = requests.get(url)
data = response.json()

peliculas = [{
    "Título": film['title'],
    "Fecha de lanzamiento": film['release_date']
} for film in data['results']
]

df = pd.DataFrame(peliculas)

escritorio = os.path.join(os.path.expanduser("~"), "Desktop")
carpeta_destino = os.path.join(escritorio, "StarWarsDatos")

os.makedirs(carpeta_destino, exist_ok=True)

ruta_archivo = os.path.join(carpeta_destino, "peliculas_star_wars.csv")

df.to_csv(ruta_archivo, index=False)

print(f"El archivo se ha guardado en: \n{ruta_archivo}")
