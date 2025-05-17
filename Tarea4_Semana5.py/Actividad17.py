#Ejericio 7: Matriz de Coordenadas Polares: Escribe un programa que tome una coordenada polar almacenada en una tupla (r, θ)). Convierte esa coordenada a coordenadas cartesianas (x, y) y muestra la tupla resultante. 

import math

def convertir_polares_a_cartesianas():

    r = float(input("Introduzca el valor de r (radio): "))
    theta = float(input("Introduzca el valor de theta (ángulo en radianes): "))

    x = r * math.cos(theta)
    y = r * math.sin(theta)

    coordenadas_cartesiana = (x, y)
    print(f"La coordenada cartesiana es: {coordenadas_cartesiana}")

convertir_polares_a_cartesianas()