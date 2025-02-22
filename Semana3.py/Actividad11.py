#Ejercicio 11: Cálculo de determinante de una matriz 3x3. Descripción: Escribe una función que calcule el determinante de una matriz 3x3.

def determinante_matriz_3x3(matriz):
    return (matriz[0][0] * (matriz[1][1] * matriz[2][2] - matriz[1][2] * matriz[2][1]) - matriz[0][1] * (matriz[1][0] * matriz[2][2] - matriz[1][2] * matriz[2][0]) + matriz[0][2] * (matriz[1][0] * matriz[2][1] - matriz[1][1] * matriz[2][0]))

matriz = [
             [int(input("Ingrese el elemento [1,1]: ")), int(input("Ingrese el elemento [1,2]: ")), int(input("Ingrese el elemento [1,3]: "))], 
             [int(input("Ingrese el elemento [2,1]: ")), int(input("Ingrese el elemento [2,2]: ")), int(input("Ingrese el elemento [2,3]: "))],
             [int(input("Ingrese el elemento [3,1]: ")), int(input("Ingrese el elemento [3,2]: ")), int(input("Ingrese el elemento [3,3]: "))]
]

determinante = determinante_matriz_3x3(matriz)
print(f"El determinante de la matriz es: {determinante}")

