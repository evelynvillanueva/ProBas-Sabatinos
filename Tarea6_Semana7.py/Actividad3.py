#Ejercicio 3: Conteo de Vocales en una Cadena: Crea una función que tome una cadena de texto y cuente cuántas veces aparece cada vocal (a, e, i, o, u). La función regresa una lista de tuplas, donde cada tupla contiene la vocal y su cantidad de apariciones.

def contador_vocales(cadena): 

    vocales = "aeiou" #Se define las vocales que contaremos

    conteo = {vocal: 0 for vocal in vocales} #Usamos un diccionario para el conteo de las vocales 

    for char in cadena.lower(): #Convertimos la cadena en minúsculas
        if char in vocales:
            conteo[char] += 1 #Recorremos cada caracter de la cadena 

    return [(vocal, conteo[vocal]) for vocal in vocales] #Se devuelve la lista de tuplas con el resultado del conteo


texto = "Conteo de Vocales en una Cadena: Crea una función que tome una cadena de texto y cuente cuántas veces aparece cada vocal (a, e, i, o, u). La función regresa una lista de tuplas, donde cada tupla contiene la vocal y su cantidad de apariciones."
resultado = contador_vocales(texto)
print(f"El conteo de las vocales fue: {resultado}")
