#Ejercicio 7: Suma de Elementos en una lista. Descripción: Escribe un programa que sume todos los elementos de una lista de números ingresada por el usuario.

valores = input("Ingresa los números separados por espacios: ")

numeros = [int(a) for a in valores.split()]

suma = sum(numeros)

print(f"La suma de los elementos es: {suma}")