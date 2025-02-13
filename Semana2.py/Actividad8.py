#Ejercicio 8: Encontrar el Mayor y el Menor en una Lista. Descripción: Escribe un programa que encuentre el número mayor y menor en una lista de números ingresada por el usuario. Se pueden usar las funciones sort, max y/ o min. 

valores = input("Ingresa los números separados por espacios: ")

lista_de_numeros = [int(a) for a in valores.split()]

mayor = max(lista_de_numeros)
menor = min(lista_de_numeros)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
