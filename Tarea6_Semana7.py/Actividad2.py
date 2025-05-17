#Ejercicio 2: 2. Ordenamiento de una Lista de Palabras: Implementa una función que tome una lista de palabras y las ordene alfabéticamente.

def ordena_las_palabras(lista_de_palabras):
    return sorted(lista_de_palabras)

#Ejemplo de cómo se usa.

palabras = ["we", "love", "you", "death", "bath", "max"]
palabras_ordenadas = ordena_las_palabras(palabras)

print(f"Lista original: {palabras}")
print(f"Palabras ordenadas: {palabras_ordenadas}")