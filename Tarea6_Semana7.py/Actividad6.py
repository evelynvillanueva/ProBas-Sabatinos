#Ejercicio 6: Fibonacci: Escribe una función recursiva que calcule el término n de la secuencia de Fibonacci. La secuencia comienza con 0 y 1, y cada término posterior es la suma de los dos anteriores. Debes almacenar cada elemento de la serie en una lista.

def fibonacci(n): 

    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1]
    serie = fibonacci(n - 1)

    serie.append(serie[-1] + serie[-2])

    return serie 

n = 9 
resultado = fibonacci(n)
print(f"Los primeros {n+1} términos de la secuencia de Fibonacci son: {resultado}") 