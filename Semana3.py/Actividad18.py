#Ejercicio 18: Cálculo de la Mediana. Descripción: Escribe una función que calcule la mediana de una lista de números. 

def calcular_mediana(lista):

    lista_ordenada = sorted(lista)

    n = len(lista_ordenada)

    if n % 2 != 0: 
        mediana = lista_ordenada[n // 2]
    else:

        n1 = lista_ordenada[n // 2 - 1]
        n2 = lista_ordenada[n // 2]
        mediana = (n1 + n2) / 2
    
    return mediana

numeros = [5, 7, 10, 9, 8, 4]
resultado = calcular_mediana(numeros)
print(f"La mediana es: {resultado}")

