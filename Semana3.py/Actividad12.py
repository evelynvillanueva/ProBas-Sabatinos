#Ejercicio 12: Cálculo de la moda. Descripción: Escribe una función que calcule la moda de una lista de números. 

def calcular_moda(lista):
    frecuencia = {}

    for numero in lista:
        if numero in frecuencia:
            frecuencia[numero] += 1
        else:
            frecuencia[numero] = 1
    
    max_frecuencia = max(frecuencia.values())

    modas = [numero for numero, count in frecuencia.items () if count == max_frecuencia]
    
    return modas

numeros = [int (a) for a in input("Introduce la lista de números separados por un espacio: ").split()]
moda = calcular_moda(numeros)

if len(moda) == 1:
    print(f"La moda es: {moda[0]}")
else:
    print(f"Las modas son: {','.join(map(str, moda))}")

