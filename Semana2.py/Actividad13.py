#Ejercicio 13: Contar Caracteres. Descripción: Escribe un programa que cuente el número de veces que aparece un carácter específico en una cadena de texto ingresada por el usuario. 

texto = input("Ingresa un párrafo de texto: ")

caracter = input("Ingresa el carácter que deseas contar: ")

conteo = 0

for a in texto:
    if a == caracter:
        conteo += 1

print(f"El carácter '{caracter}' aparece {conteo} veces.")

