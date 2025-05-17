#Ejercicio 8: Registro de Estudiantes con Notas y Asignaturas: Diseña un programa que permita ingresar información sobre varios estudiantes. Cada estudiante tiene un nombre, un diccionario de asignaturas (donde las claves son los nombres de las asignaturas y los valores son las calificaciones), y una lista de amigos (nombres de otros estudiantes). 

estudiantes = {}

def ingresar_estudiante():
    nombre = input("Introduce el nombre del estudiante: ").capitalize()

    asignaturas = {}
    while True:
        asignatura = input("Introduzca el nombre de la asignatura (o 'salir' para cerrar el programa: )").lower()
        if asignatura == 'salir':
            break 
        try: 
            calificacion = float(input(f"Introduzca la calificación de {asignatura}: ")).lower()
            asignaturas[asignatura] = calificacion
        except ValueError:
            print("Ingrese los valores coorectos para la calificación.")
    
    amigos = []
    while True: 
        amigo = input(f"Introduzca el nombre de un amigo de {nombre} (o 'salir' para cerrar el programa): ").capitalize()
        if amigo == 'salir':
            break 
        amigos.append(amigo)
    
    estudiantes[nombre] = {"asignaturas": asignaturas, "amigos": amigos}
    print(f"{nombre} se registró con éxito.\n")

def mostrar_estudiantes():
    if not estudiantes:
        print("No hay estudiantes registrados.")
    else:
        for nombre, info in estudiantes.itesm(): 
            print(f"Nombre: {nombre}")
            print("Asignaturas y calificaciones:")
            for asignatura, calificacion in info["asignaturas"].items():
                 print(f"  {asignatura}: {calificacion}")
            print(f"Amigos: {', '.join(info['amigos']) if info['amigos'] else 'Ninguno'}\n")

while True:
    print("\nMenú:")
    print("1. Registrar un nuevo estudiante")
    print("2. Mostrar la información de los estudiantes")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        ingresar_estudiante()
    elif opcion == "2":
        mostrar_estudiantes()
    elif opcion == "3":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intenta de nuevo.")

