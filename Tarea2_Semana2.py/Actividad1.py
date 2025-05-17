#Ejercicio 1: Suma de Números pares. Descripción: Escribe un programa que sume todos los números pares del 1 al 100 usando un ciclo for.

sum = 0 
for i in range(1,101): 
    if i % 2 == 0:
        sum += i

print(f"La suma de los números pares es: {sum}")

