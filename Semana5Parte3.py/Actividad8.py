#Ejericicio 8: Registro de Puntajes de Jugadores: Implementa un programa que permita registrar los puntajes de varios jugadores en un juego. Cada jugador tiene un nombre y un puntaje asociado. Utiliza un diccionario para almacenar e imprimir esta información. 

def ingresar_puntajes_jugadores():

    registro_puntajes = {}

    num_jugadores = int(input("¿Cuántos jugadores desea registrar?: "))

    for _ in range(num_jugadores):
        jugador = input("Ingrese el nombre del jugador: ")
        puntaje = int(input(f"Ingrese el puntaje del jugador {jugador}: "))
        registro_puntajes[jugador] = puntaje

    return registro_puntajes 

def mostrar_puntajes(registro_puntajes):
    print("\nLos puntajes de los juagdores son:")
    for jugador, puntaje in registro_puntajes.items():
        print(f"{jugador}: {puntaje} puntos")

puntajes_de_jugadores = ingresar_puntajes_jugadores()

mostrar_puntajes(puntajes_de_jugadores)