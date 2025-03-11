#Ejercicio 5: Contar Vocales. Descripción: Escribe un programa que cuente el número de vocales en una cadena de texto ingresada por el usuario. 

texto = input("Ingrese un párrafo de texto: ")

vocales = "aeiouAEIOUáéíúóÁÉÍÓÚ"
contador = 0

for letra in texto: 
    if letra in vocales: 
        contador += 1

print(f"El número de vocales es: {contador}")

