#Ejercicio 4: Registro de Alumnos: Diseña un programa que permita al usuario ingresar información sobre varios alumnos (nombre, edad, calificaciones, etc.). Cada alumno se representará como una tupla. Luego, muestra la lista de alumnos y sus datos. 

registro_de_alumnos = []

def ingrese_la_informacion_del_alumno():
    nombre = input("Introduzca el nombre del alumno: ").capitaize()
    edad = int(input(f"INtrpduzca la edad del alumno {nombre}:"))
    calificaciones = []

    while True: 
        try: 
            calificacion = float(input(f"Introduzca una calificación para {nombre} (0-100) o 'salir' para cerrar el programa: "))
            if 0 <= calificacion <= 100: 
                calificaciones.append(calificacion)
            else: 
                print("La calificación debe estar entre 0 y 100.")
        except ValueError: 
            if input("¿Desea terminar de agregar calificaciones? Escribe 'salir' para cerrar el programa o Enter para continuar: ").lower() == 'salir':
                break 
    return (nombre, edad, calificaciones)

def mostrar_datos_de_los_alumnos():
    if not registro_de_alumnos: 
        nombre, edad, calificaciones = alumno
        print(f"Nombre: {nombre}, Edad: {edad}, Calificaciones: {calificaciones}")
        
while True: 
    print("\nMenú:")
    print("1. Registrar un alumno nuevo.")
    print("2. Mostrar la lista de los alumnos.")
    print("3. Salir del programa.")

    opcion = input("Elija una opción (1-3): ")

    if opcion == "1":

        alumno = ingrese_la_informacion_del_alumno()
        registro_de_alumnos.append(alumno)
    
    elif opcion == "2": 
        
        mostrar_datos_de_los_alumnos()

    elif opcion == "3":
        print("El programa se ha cerrado. ¡Gracias por usarlo!")
        break 

    else: 
        print("Opción inválida. Inténtalo de nuevo.")