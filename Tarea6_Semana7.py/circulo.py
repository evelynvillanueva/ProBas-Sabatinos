#Ejercicio 7: Cálculo del Área de un Círculo

#1. Diseña una función llamada calcular_area_circulo que tome el radio de un círculo como argumento.
#2. La función debe calcular y devolver el área del círculo (fórmula: área = π * radio^2).
#3. Crea un módulo llamado circulo.py y encapsula esta función en él.
#4. En un segundo script, importa el módulo anterior y dentro de __main__, invoca la función para mostrar el área de un círculo de un radio especificado por el usuario.


import math 

def calcular_area_circulo(radio):

    return math.pi * radio ** 2
