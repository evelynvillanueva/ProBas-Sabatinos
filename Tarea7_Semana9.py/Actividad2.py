#Lectura de un Archivo de texto.

nombre_archivo = "nombres.txt"

lista_nombres = []

try: 
    with open(nombre_archivo, "r") as archivo: 
        lista_nombres = [linea.strip() for linea in archivo]

    print("Lista de nombres en el archivo:")
    print(lista_nombres)

except FileNotFoundError: 
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")