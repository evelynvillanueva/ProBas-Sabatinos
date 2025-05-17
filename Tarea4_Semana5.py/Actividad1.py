#Ejercicio 1: Contador de Palabras en un Texto: Diseña un programa que tome un párrafo o un texto largo y cuente cuántas palabras contiene. Considera que las palabras están separadas por espacios. 

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto = "Contador de Palabras en un Texto: Diseña un programa que tome un párrafo o un texto largo y cuente cuántas palabras contiene. Considera que las palabras están separadas por espacios."
contador_palabras = contar_palabras(texto)
print(f"El texto tiene {contador_palabras} en el texto.")
