#Ejercicio 5: Palabras sin Vocales: Crea una función que tome una cadena y devuelva un conjunto con las consonantes presentes en ella. 

def obtener_consonantes(cadena):

    vocales = "aeiouAEIOU"

    consonantes = {letra for letra in cadena if letra.isalpha() and letra not in vocales}

    return consonantes 

cadena = "Palabras sin Vocales: Crea una función que tome una cadena y devuelva un conjunto con las consonantes presentes en ella."

resultado = obtener_consonantes(cadena)

print(f"Consonantes encontradas en la cadena: {resultado}")
