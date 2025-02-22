#Ejercicio 4: Función para calcular el factorial. Descripción: Escribe una función que calcule la factorial de un número usando ciclos. 

def calcular_factorial(n):
    if n == 0 or n == 1: 
        return 1
    factorial = 1
    for i in range(2, n + 1): 
        factorial *= i
    return factorial

resultado = calcular_factorial(8)
print(f"El factorial de 8 es: {resultado}")
