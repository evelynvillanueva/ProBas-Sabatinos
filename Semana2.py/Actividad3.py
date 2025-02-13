#Ejericio 3: Números primos. Descripción: Escribe in programa que determine si un número dado por el usuario es primo o no. 

num = int(input("Ingresa el número del que deseas saber si es primo: "))

if num < 2: 
    print(f"{num} no es un número primo.")
else: 
    for i in range(2, num): 
        if num % i == 0: 
            print(f"{num} no es un número primo.")
            break
    else: 
        print(f"{num} es un número primo.")
