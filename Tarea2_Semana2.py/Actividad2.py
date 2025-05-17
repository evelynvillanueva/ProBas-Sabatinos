#Ejercicio 2: Factorial de un Número. Descripción: Escribe un programa que se calcule el factorial de un número dado por el usuario usando un ciclo while. El número debe estar entre 1 y 20.

num = int(input("Ingresa un número entre 1 y 20: "))

if 1 <= num <= 20: 

    factorial = 1 

    i = 1

    while i <= num:
        factorial *= i 
        i += 1

    print("El factorial del número", num, "es:", factorial)

else: 

    print("Ingresa un número del 1 al 20.")
