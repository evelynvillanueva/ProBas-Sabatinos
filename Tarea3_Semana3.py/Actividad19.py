#Ejercicio 19: Generador de Números Aleatorios. 

import random 

def generar_numeros_aleatorios(n): 
    lista = list()
    for i in range(n):
        lista.append(random.randint(1, 100))
    return lista

resultado = generar_numeros_aleatorios(10)
print(f"Números aleatorios: {resultado}")

# 1. ¿Cuál es el propósito de la función 'generar_numeros_aleatorios(n)'? C. Crear una lista de números aleatorios entre 1 y 100. 

# 2. ¿Cuál de las siguientes afirmaciones es veerdadera sobre el uso de 'random.randint(1, 100)' dentro de la función? A. Es posible que genere números repetidos en la lista. 

# 3. ¿Qué tipo de dato retorna la función 'generar_numeros_aleatorios(n)'? C. Una lista de números enteros.

# 4. Si se llama a 'generar_numeros_aleatorios(0)', ¿qué resultado se obtiene? A. Una lista vacía. 

# 5. ¿Qué se imprime en la consola si se ejecuta 'print("Números aleatorios:", restultado)' después de llamar a 'generar_numeros_aleatorios(10)'? C. Números aleatorios entre 1 y 100. 