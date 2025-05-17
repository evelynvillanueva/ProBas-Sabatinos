#Lectura y escritura de diccionarios.

nombre_archivo = "estudiantes.txt"

estudiantes = []

try: 
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo: 
            partes = linea.strip().split(",")
            if len(partes) >= 7: 
                estudiante = {
                    "nombre": partes[0], "edad": int(partes[1]),
                    "calificaciones": list(map(int, partes[2:]))
                }
                estudiantes.append(estudiantes)

    print("\nLista de estudiantes:")
    for estu in estudiantes:
        print(estu)

except FileNotFoundError: 
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")
    estudiantes = []

nombre_a_cambiar = input("\nNombre del estudiante a cambiar: ").strip()

econtrado = False
for estu in estudiantes: 
    if estu["nombre"].lower() == nombre_a_cambiar.lower():
        nueva_edad = int(input(f"Nueva edad: "))
        nuevas_calificaciones = []
        for i in range(5):
            nota = int(input(f"Nueva calificación {i+1}: "))
            nuevas_calificaciones.append(nota)
        estu["edad"] = nueva_edad
        estu["calificiaciones"] = nuevas_calificaciones
        encontrado = True
        print("Información actualizada.")
        break

if not encontrado: 
    print("Estudiante no encontrado.")

with open(nombre_archivo, "w") as archivo:
    for estu in estudiantes: 
        linea = f"{estu['nombre']}, {estu['edad']}," + ",".join(map(str, estu['calificaciones']))
        archivo.write(linea + "\n")

print("\nCambios guardados en el archivo.")
