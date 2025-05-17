#Ejercicio 6: Función para invertir una cadena. Descripción: Escribe una función que reciba una cadena de texto y la devuelva invertida.

def invertir_cadena(cadena): 
    return cadena[::-1]

texto = input("Ingrese una cadena de texto: ")
texto_invertido = invertir_cadena(texto)
print(f"La cadena invertida es: {texto_invertido}")

