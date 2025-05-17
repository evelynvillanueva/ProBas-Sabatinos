#Ejercicio 17: Verificación de palíndromo. Descripción: Escribe una función que determine si una cadena de texto es un palíndromo. 

def es_palindromo(cadena):
    cadena = cadena.replace(" ", "").lower()

    if cadena == cadena[::-1]:
        return True
    else: 
        return False
    
resultado = es_palindromo("Anita lava la tina")
print(f"¿Es palíndromo? {resultado}")
    
    