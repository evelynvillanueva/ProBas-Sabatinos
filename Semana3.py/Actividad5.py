#Ejercicio 5: Función para Calcular el Promedio. Descripción: Escribe una función que reciba una lista de calificaciones y devuelva el promedio.

def calcular_promedio(calificaciones):
    return sum(calificaciones)/ len(calificaciones)

calificaciones = [8, 9, 10, 7, 9]
promedio = calcular_promedio(calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")

