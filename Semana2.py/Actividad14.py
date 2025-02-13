#Ejercicio 14: Generar Números Aleatorios. Descripción: Escribe un programa que genere una lista de n números aleatorios entre 1 y 100, donde n es ingresado por el usuario. 

import random

n = int(input("¿Cuántos números aleatorios deseas generar?: "))

numeros_aleatorios = []

i = 0 
while i < n: 
    numeros_aleatorios.append(random.randint(1,100))
    i += 1 

print(f"La lista de números aleatorios es: {numeros_aleatorios}")