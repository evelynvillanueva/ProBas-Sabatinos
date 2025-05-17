#Ejercicio 1: Diccionario de Películas con Géneros y Actores: Diseña un programa que almacene información sobre películas. Cada película tiene un nombre, una lista de géneros (como “acción”, “comedia”, etc.) y una lista de actores principales. 

peliculas = {}

def registrar_pelicula(nombre, generos, actores):

    peliculas[nombre] = {
        'géneros': set(generos),
        'actores': list(actores)
    }

def listar_peliculas():

    if peliculas: 
        for nombre, info in peliculas.items():
            print(f"Película: {nombre}")
            print(f"Géneros: {', '.join(info['géneros'])}")
            print(f"Actores: {', '.join(info['actores'])}")
            print('-' * 30)
    else: 
        print("No se encontraron películas regustradas.")

def obtener_peliculas_por_genero(genero): 
    print(f"Películas de género '{genero}:'")
    for nombre, info in peliculas.items():
        if genero in info['géneros']: 
            print(f"{nombre}")
    print('-' * 30)

def obtener_peliculas_por_actor(actor): 
    print(f"Películas de actor '{actor}:'")
    for nombre, info in peliculas.items():
        if actor in info['actores']: 
            print(f"{nombre}")
    print('-' * 30)
    
registrar_pelicula("Star wars: a new hope", ["Space opera", "Ciencia ficción"], ["Mark Hamill", "Harrison Ford", "Carrie Fisher"])
registrar_pelicula("The Matrix: Reloaded", ["Acción", "Ciencia ficción"], ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"])
registrar_pelicula("Hércules", ["Ifantil", "Musical"], ["James Woods", "Susan Egan", "Tate Donovan"])

listar_peliculas()

obtener_peliculas_por_genero("Ciencia ficción")
obtener_peliculas_por_actor("Keanu Reeves")