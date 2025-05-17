#Escritura en archivo.

def escribir_archivo(nombre_archivo, contenido):
    try:
        with open(nombre_archivo, "w") as archivo:
            archivo.write(contenido)
            print(f"Contenido escrito exitosamente en '{nombre_archivo}'.")
    except IOError: 
        print(f"Error: no se pudo escribir en el archivo '{nombre_archivo}'.")