#Ejercicio 1: Promedio de una Lista de Números: Diseña una función que tome una lista de números como parámetro y calcule su promedio.

def obten_prom(numeros):
    if len(numeros) == 0: #verifica que la lista no esté vacía
        return 0 #si la lista está vacía se devuelve el 0 para no dividirlo entre 0 
    total = sum(numeros) #calcula la suma de todos los números en la lista
    cantidad = len(numeros) #calcula la cantidad de elementos que se tienen en la lista 
    return total / cantidad #es para obtener el promedio 

numeros = [23, 12, 6, 16, 10]

promedio = obten_prom(numeros)

print(f"El promedio es {promedio}")

numeros_vacio = []
promedio_vacio = obten_prom(numeros_vacio)
print(f"El promedio de la lista vacía es: {promedio_vacio}")

