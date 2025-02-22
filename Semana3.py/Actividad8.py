#Ejercicio 8: Función para verificar palíndromo. Descripción: Escribe una función que determine si una cadena de texto es un palíndromo. 

def es_palindromo(cadena): 
    cadena = cadena.replace(" ", "").lower()

    return cadena == cadena[::-1]

texto = input("Introduce una cadena de texto: ")
if es_palindromo(texto):
    print("Es un palíndromo.")
else: 
    print("No es un palíndromo.")

    