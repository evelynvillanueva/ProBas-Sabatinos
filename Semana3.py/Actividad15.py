#Ejercicio 15: Juego de adivinanza. Descripción: Escribe una función que implemente un juego de adivinanza donde el usuario debe adivinar un número generado aleatoriamente por la computadora. La función debe proporcionar pistas sobre si el número ingresado es mayor o menor que el número de objetivo.

import random
def juego_adivinanza():
    numero_de_objetivo = random.randint(1, 100)
    intentos = 0

    while True:
        numero_aleatorio = int(input("Adivina el número de (entre 1 y 100): "))
        intentos += 1

        if numero_aleatorio < numero_de_objetivo:
            print("Muy bajo.")
        elif numero_aleatorio > numero_de_objetivo: 
            print("Muy alto.")
        else: 
            print(f"¡Acertaste! Lograste adivinar en el intento {intentos}.")
            break
    
juego_adivinanza()

