#Ejercicio 2: Diccionario de Notas de Estudiantes: Diseña un programa que permita ingresar las notas de varios estudiantes. Cada estudiante tiene un nombre y una lista de calificaciones. Utiliza un diccionario para almacenar esta información. 

notas_estudiantes = {}

def ingresar_notas(nombre):

    notas = []

    while True:
        try: 
            nota = float(input(f"Introduzca una calificación para {nombre} (0-10) o 'salir' para cerrar el programa: "))
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La calificación de estar entre 0 y 10.")
        except ValueError: 

            if input("¿Desea terminar? Escriba 'salir' para cerrar el programa o presione Enter para seguir añadiendo notas: ").lower() == 'salir':
                break 

        return notas 
    
def mostrar_notas(nombre):
    if nombre in notas_estudiantes: 
        print(f"Calificaciones de {nombre}: {notas_estudiantes[nombre]}")
    else: 
        print(f"El estudiante {nombre} no tiene califiaciones guardadas.")

while True: 
    print("\nMenú:")
    print("1. Ingrese las calificaciones del estudiante.")
    print("2. Ver las calcificaciones del estudiante.")
    print("3. Salir")

    opcion = input("Elija la opción que desea realizar (1-3): ")

    if opcion == "1":

        nombre = input("Ingresa el nombre del estudiante: ").capitalize()
        notas_estudiantes[nombre] = ingresar_notas(nombre)
    
    elif opcion == "2":

        nombre = input("Introduzca el nombre del estudiante del que desea ver sus notas: ").capitalize()
        mostrar_notas(nombre)
    
    elif opcion == "3":

        print("Gracias por usar el programa. ¡Que tengas un buen día!")
        break 

    else: 
        print("Opción inválida. Inténtelo de nuevo.")




