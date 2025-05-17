#Ejercicios de lectura y escritura de archivos.

nombres = ["Miguel", "Vivian", "Marcelo", "Micaela", "Gloria"]

nombre_archivo = "nombres.txt"

with open(nombre_archivo, "w") as archivo:
    for nombre in nombres: 
        archivo.write(nombre + "\n")

print(f"Se han escrito {len(nombres)} nombres en el archivo '{nombre_archivo}'")