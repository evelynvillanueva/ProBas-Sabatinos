#Ejercicio 9: Agenda de Contactos Mejorada: Implementa un programa que permita agregar, buscar y eliminar contactos en una agenda. Cada contacto tiene un nombre, un número de teléfono y una lista de correos electrónicos. Usa una lista de diccionatos. 


agenda = []

def agregar_contacto():
    nombre = input("Introduce el nombre del contacto: ").capitalize()
    telefono = input("Introduce el número de teléfono: ")
    correos = input("Introduce los correos electrónicos separados por comas: ").split(",")
    agenda.append({"nombre": nombre, "telefono": telefono, "correos": [correo.strip() for correo in correos]})
    print(f"Contacto {nombre} agregado con éxito.\n")


def buscar_contacto():
    nombre = input("Introduce el nombre del contacto a buscar: ").capitalize()
    for contacto in agenda:
        if contacto["nombre"] == nombre:
            print(f"\nNombre: {contacto['nombre']}")
            print(f"Teléfono: {contacto['telefono']}")
            print(f"Correos: {', '.join(contacto['correos'])}\n")
            return
    print(f"No se encontró el contacto con el nombre {nombre}.\n")


def eliminar_contacto():
    nombre = input("Introduce el nombre del contacto a eliminar: ").capitalize()
    global agenda
    agenda = [contacto for contacto in agenda if contacto["nombre"] != nombre]
    print(f"Contacto {nombre} eliminado con éxito.\n")


while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    
    opcion = input("Elige una opción (1-4): ")
    
    if opcion == "1":
        agregar_contacto()
    elif opcion == "2":
        buscar_contacto()
    elif opcion == "3":
        eliminar_contacto()
    elif opcion == "4":
        print("¡Regresa pronto!")
        break
    else:
        print("Opción inválida.")
