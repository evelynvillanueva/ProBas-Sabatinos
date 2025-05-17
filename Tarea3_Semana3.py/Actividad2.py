#Ejercicio 2: Número Arbitrario de argumentos. Descripción: Escribe una función que reciba un número arbitrario y devuelva su suma.

def suma_numeros(*args):
    suma = 0
    for num in args: 
        suma += num
    return suma
    
resultado = suma_numeros(3, 5, 7, 9)
print(f"La suma de los números es: {resultado}")

