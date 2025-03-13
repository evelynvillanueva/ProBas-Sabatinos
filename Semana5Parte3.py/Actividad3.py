#Ejercicio 3: Eliminación de Duplicados en una Lista: Diseña un programa que tome una lista y cree un conjunto a partir de ella, eliminando los elementos duplicados. 

def eliminar_duplicados(lista):

    conjunto = set(lista)

    lista_sin_duplicados = list(conjunto)

    return lista_sin_duplicados

lista_con_duplicados = [1, 3, 3, 3, 2, 4, 5, 5, 6, 7, 8, 9, 9]

resultado = eliminar_duplicados(lista_con_duplicados)

print(f"Lista sin duplicados: {resultado}")


