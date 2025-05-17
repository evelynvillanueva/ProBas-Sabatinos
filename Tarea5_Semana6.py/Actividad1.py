#Ejercicio 7: Contador de Palabras en un Texto: Diseña un programa que tome un párrafo o un texto largo y cuente cuántas veces aparece cada palabra. Utiliza un diccionario para almacenar las palabras y sus frecuencias. Al finalizar, recorre e imprime el contenido del diccionario con un ciclo.  

def contar_palabras(texto):

    palabras = texto.lower().split()

    frecuencias = {}

    for palabra in palabras:

        if palabra in frecuencias: 
            frecuencias[palabra] += 1
        else: 
            frecuencias[palabra] = 1

    return frecuencias 

texto = "La trama descrita en las nueve películas que componen la serie principal de Star Wars relata las vivencias de la familia Skywalker,11​ «hace mucho tiempo en una galaxia muy muy lejana»,12​ cuyos integrantes son capaces de percibir y utilizar «La Fuerza», lo cual les permite desarrollar habilidades como la telequinesis, la clarividencia y el control mental, entre otras."

frecuencias_palabras = contar_palabras(texto)

print("Frecuencias de palabras:")

for palabra, frecuencia in frecuencias_palabras.items():
    print(f"{palabra}: {frecuencia}")