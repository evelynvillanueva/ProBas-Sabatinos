#Ejercicio 4: Factorial de un Número: Diseña una función recursiva que calcule el factorial de un número entero positivo. El factorial de n se denota como n! y es el producto de todos los números enteros positivos desde 1 hasta n.

def factorial(n): 

    if n == 0 or n == 1:
        return 1
    
    return n * factorial(n - 1)

numero = 7
resultado = factorial(numero)
print(f"El factorial del número {numero} es: {resultado}")

