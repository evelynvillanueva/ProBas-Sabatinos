#Ejercicio 5: Ordenamiento de Puntos en el Plano: Implementa una función que tome una lista de puntos en el plano (representados como tuplas (x, y)) y los ordene según su distancia al origen (punto (0, 0)). 

import math 

def distancia_al_origen(punto):
    return punto[0]**2 + punto[1]**2

def ordenar_los_puntos_por_la_distancia(puntos): 
    return sorted(puntos, key=distancia_al_origen)

puntos = [(1, 3), (3, 5), (0, 0), (8, 9), (20, 10)]

puntos_ordenados = ordenar_los_puntos_por_la_distancia(puntos)

print("Puntos ordenados por la distancia al origen: ")
for punto in puntos_ordenados:
    print(punto)