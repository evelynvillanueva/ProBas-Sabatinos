#Ejercicio 3: Diccionario de Traducción de Palabras: Diseña un programa que permita al usuario ingresar palabras en un idioma y sus traducciones en otro idioma. Utiliza un diccionario para almacenar esta información. 

diccionario_con_traducciones = {}

def agrega_la_traduccion(palabra, traduccion):
    diccionario_con_traducciones[palabra] = traduccion
    print(f"La traducción de '{palabra}' se ha añadido correctamente.")

def buscar_la_traduccion(palabra):
    if palabra in diccionario_con_traducciones: 
        return f"La traducción de la palabra '{palabra}' es '{diccionario_con_traducciones[palabra]}'."
    else: 
        return f"No se encontró la traducción de la palabra '{palabra}' en el diccionario de traducciones."

while True:
    print("\nMenú:")
    print("1. Agregar una palabra y su traducción.")
    print("2. Buscar la traducción de una palabra.")
    print("3. Salir del programa.")

    opcion = input("Elija una opción (1-3): ")

    if opcion == "1": 

        palabra = input("Introduzca la palabra en el idioma original: ").lower()
        traduccion = input("Introduzca la traducción en el otro idioma: ").lower()
        agrega_la_traduccion(palabra, traduccion)
    
    elif opcion == "2":

        palabra = input("Introduzca la palabra que quiera traducir: ").lower()
        print(buscar_la_traduccion(palabra))

    elif opcion == "3":
        print("¡Que tengas un buen día!")
        break 
    else: 
        print("Opción inválida. Inténtelo de nuevo.")
