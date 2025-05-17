# Apertura de archivo.

def leer_archivo(nombre_archivo):
    try: 
        with open(nombre_archivo, "r") as archivo: 
            contenido = archivo.read()
        return contenido 
    except FileNotFoundError:
        print(f"Error: El archivo '{archivo}' no fue encontrado")
        return None