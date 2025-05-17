#Ejercicio 4: Matriz Transpuesta: Escribe una función que tome una matriz de 3 x 3 y devuelva su matriz transpuesta (intercambiando filas por columnas). 

def capturar_matriz():

    matriz = []
    for i in range(3):
        fila = []
        for j in range(3):

            valor = int(input(f"Ingresa el elemento ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def matriz_transpuesta(matriz):
    return [[matriz[j][i] for j in range(3)] for i in range(3)]

def imprimir_matriz(matriz):

    for fila in matriz: 
        print(fila)

matriz = capturar_matriz()

matriz_trans = matriz_transpuesta(matriz)

print("\nMatriz Inicial:")
imprimir_matriz(matriz)

print("\nMatriz Transpuesta:")
imprimir_matriz(matriz_trans)
