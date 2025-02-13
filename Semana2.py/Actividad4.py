#Ejercicio 4: Números Fibonacci. Descripción: Escribe un programa que genere los primeros n números de la secuencia de Fibonacci, donde n es ingresado por el usuario. El valor de n debe estar entre 1 y 50.

n = int(input("Ingresa un número de entre 1 y 50 para crear la secuencia de Fibonacci: "))

if 1 <= n <= 50: 
    a, b = 0, 1
    print("Secuencia de Fibonacci:")
    count = 0
    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

else: 
    print("El número debe estar entre 1 y 50.")