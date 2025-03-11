#Ejercicio 8: Ordenamiento de Palabras por Longitud: Crea una función que tome una lista de palabras y las ordene de acuerdo con su longitud, de la más corta a la más larga.

def ordenar_por_longitud(lista_palabras): 

    diccionario_longitudes = {}

    for palabra in lista_palabras: 
        longitud = len(palabra)
        if longitud not in diccionario_longitudes: 
            diccionario_longitudes[longitud] = [palabra]
        else: 
            diccionario_longitudes[longitud].append(palabra)

    lista_ordenada = sorted(diccionario_longitudes.items())

    palabras_ordenadas = []
    for _, palabras in lista_ordenada: 
        palabras_ordenadas.extend(palabras)

    return palabras_ordenadas

palabras = ["manzana", "fresa", "plátano", "sandía"]
resultado = ordenar_por_longitud(palabras)
print(f"Palabras ordenadas por longitud: {resultado}")

