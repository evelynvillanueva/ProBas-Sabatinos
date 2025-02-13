#Ejercicio 9: Contar Palabras. Descripción: Escribe un programa que cuente el número de palabras en una cadena de texto ingresada por el usuario. 

texto = input("Ingresa un párrafo de texto: ")

palabras = texto.split()

print(f"El número de palabras es: {len(palabras)}")
