#Ejercicio 4: Clasificación de edad. Descripción: Escribe un programa que solicite al usuario su edad y determine si es un niño (menor de 12 años), adolescente (menos de 18), adulto (menos de 60) o adulto mayor (60 o más).

edad = int(input("Ingrese su edad: ")) 

if edad < 12:
    print("Eres un niño.")
if edad < 18:
    print("Eres un adolescente.")
if edad < 60: 
    print("Eres un adulto.")
else: 
    print("Eres un adulto mayor.")

    