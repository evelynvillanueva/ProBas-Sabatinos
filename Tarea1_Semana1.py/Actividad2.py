#Ejercicio 2. Comparación de números. Escribe un programa que solicite al usuario dos números y determine cuál es el mayor, menor o si son iguales.

a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))

print("El mayor es:", max(a, b))
print("El menor es:", min(a, b)) if a != b else print("Son iguales")
