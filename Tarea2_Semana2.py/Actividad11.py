#Ejercicio 11: Suma de Dígitos. Descripción: Escribe un programa que sume los dígitos de un número entero ingresado por el usuario. 

numero = int(input("Ingresa un número entero: "))

suma_de_digitos = 0 

while numero > 0: 
    suma_de_digitos += numero % 10 
    numero //= 10 

print(f"La suma de los dígitos es: {suma_de_digitos}")
