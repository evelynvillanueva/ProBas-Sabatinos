#Ejercicio 16: Generador de Números Fibonacci. Descripción: Escribe una función que genere los primeros n números de la serie de Fibonacci. 

def generar_fibonacci(n):
    fibonacci = [0, 1]
    while len(fibonacci) < n:

        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

resultado = generar_fibonacci(10)
print(f"Serie de Fibonacci: {resultado}")

