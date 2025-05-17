#Ejercicio 12: Ordenar una Lista. Descripción: Escribe un programa que ordene la lista de números ingresada por el usuario de menor a mayor. 

numeros = []

cantidad = int(input("¿Cuántos níumeros deseas ingresar?: "))

for i in range(cantidad): 
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

numeros.sort()

print(f"La lista ordenada de menor a mayor es: {numeros}")

