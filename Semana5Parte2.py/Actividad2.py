#Ejercicio 2: Suma de Matrices: Implementa una función que captura el contenido de dos matrices (listas de listas) de 3 x 3 elementos. Realiza la suma de ambas matrices e imprime su resultado. 

def capturar_matriz():

    matriz = []

    for i in range(3):
        fila = input(f"Ingresa la fila {i+1} (separada por un espacio): ").split()

        matriz.append([int(x) for x in fila])
    
    return matriz

def sumar_matrices(matriz1, matriz2): 
    
    return [[(matriz1[i][j] + matriz2[i][j]) for j in range(3)] for i in range(3)]

def imprimir_matriz(matriz):

    for fila in matriz: 

        print(' '.join(map(str, fila)))

print("Captura del contenido de la primera matriz: ")
matriz1 = capturar_matriz()

print("Captura del contenido de la segunda matriz: ")
matriz2 = capturar_matriz()

matriz_resultado = sumar_matrices(matriz1, matriz2)

print("\nLa suma de las dos matrices es:")

imprimir_matriz(matriz_resultado)