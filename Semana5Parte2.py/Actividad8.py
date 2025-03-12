#Ejercicio 8: Cálculo de Distancias entre Puntos: Implementa una función que tome dos puntos en el plano (tuplas (x1, y1) y (x2, y2)) y calcule la distancia euclidiana entre ellos. 

import math

def calcular_distancia():

    x1, y1 = map(float, input("Introduzca las coordenadas del primer punto (x1, y1): ").split())
    x2, y2 = map(float, input("Introduzca las coordenadas del primer punto (x1, y1): ").split())

    distancia = math.sqrt((x2 - x1)**2 + (y2 -y1)**2)

    print(f"La distancia entre los puntos ({x1}, {y1}) y ({x2}, {y2}) es: {distancia}")

calcular_distancia()