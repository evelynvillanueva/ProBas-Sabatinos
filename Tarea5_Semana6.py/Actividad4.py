#Ejercicio 10: Agenda de Contactos: Diseña un programa que permita al usuario agregar, buscar y eliminar contactos en una agenda. Cada contacto tiene un nombre y un número de teléfono. 

def agregar_contacto(agenda, nombre, telefono):
    agenda[nombre] = telefono
    print(f"Contacto de {nombre}agregado con el número {telefono}.")

def buscar_contacto(agenda, nombre):
    if nombre in agenda:
        return f"El número de {nombre} es: {agenda[nombre]}"
    else: 
        return f"No se encontró el contatco de {nombre}."
    
def eliminar_contacto(agenda, nombre):
    if nombre in agenda:
        del agenda[nombre]
        return f"Contacto de {nombre} eliminado."
    else: 
        return f"No se encontró el contacto de {nombre}."
    
def mostrar_menu():
        print("\n ----- Menú Agenda de Contactos -----")
        print("1. Agregar a un contacto")
        print("2. Buscar a un contacto")
        print("3. Eliminar a un contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")

def mostrar_contactos(agenda):
    if agenda: 
        print("\nContactos en la agenda:")
        for nombre, telefono in agenda.items():
            print(f"{nombre}: {telefono}")
    else: 
        print("No hay contactos en la agenda.")

def agenda_de_contactos():
    agenda = {}
    while True:
        mostrar_menu()
        opcion = input("Elija una opción del (1-5): ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del contacto: ")
            telefono = input("Ingrese el número de teléfono del contacto: ")
            agregar_contacto(agenda, nombre, telefono)

        elif opcion == "2":
            nombre = input("Ingrese el nombre del contacto que desee buscar: ")
            print(buscar_contacto(agenda, nombre))
        
        elif opcion == "3":
            nombre = input("Ingrese el nombre del contacto que desee eliminar: ")
            print(eliminar_contacto(agenda, nombre))

        elif opcion == "4":
            mostrar_contactos(agenda)

        elif opcion == "5": 
            print("Cerrando el programa ...")
            break 
        else: 
            print("Opción inválida, por favor ingrese una opción del 1 al 5.")

agenda_de_contactos()

        
