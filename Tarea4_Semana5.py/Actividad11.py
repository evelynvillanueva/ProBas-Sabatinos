#Ejercicio 1: Matriz de Ceros y Unos: Diseña un programa que cree una matriz de tamaño n x m (donde n y m son números enteros dados) y la inicialice con ceros y unos alternados (como un tablero de ajedrez). 

def crear_matriz(n, m):
    return [[(i + j) % 2 for j in range(m)] for i in range(n)]

n = int(input("Introduzca el número de filas (n): "))
m = int(input("Introduzca el número de columnas (m): "))

matriz = crear_matriz(n, m)
for fila in matriz: 
    print(' '.join(str(celda) for celda in fila))