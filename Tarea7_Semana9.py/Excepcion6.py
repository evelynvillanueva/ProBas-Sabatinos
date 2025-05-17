#Calculo de raíz cuadrada. 

import math 

def raiz_cuadrada(numero):
    try:
        resultado = math.sqrt(numero)
        return resultado
    except ValueError:
        print("Error: no se puede calcular la raíz cuadrada de un número negativo.")
        return None