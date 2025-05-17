#Ejercicio 7: Función para calcular la mediana. Descripción: Escribe una función que calcule la mediana de una lista de números. Usa la función sort de lista para ordenar la lista. 

def calcular_mediana(lista): 
    lista.sort()

    n = len(lista)

    if n % 2 != 0:
        mediana = lista[n // 2]
    else: 
        mediana = (lista[n // 2 - 1] + lista[n // 2])/ 2

    return mediana 

numeros = [3, 5, 7, 9, 11]
mediana = calcular_mediana(numeros)
print(f"La mediana es: {mediana}")

