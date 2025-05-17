#Ejercicio 10: Eliminación de Elementos según Condición: Diseña una función que tome una lista y elimine todos los elementos que no sean pares.

def eliminar_impares(lista):

    lista_pares = {num for num in lista if num % 2 == 0}

    return list(lista_pares)

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

resultado = eliminar_impares(lista)
print(f"Lista con solo los números pares: {resultado}")