#Ejercicio 1: Diferencia entre Conjuntos: Escribe un programa que tome dos conjuntos y calcule la diferencia entre ellos (elementos presentes en el primer conjunto pero no en el segundo). 


def diferencia_conjuntos(conjunto1, conjunto2):

    set1 = set(conjunto1)
    set2 = set(conjunto2)

    diferencia = set1 - set2

    return list(diferencia)

lista1 = [1, 3, 5, 6, 7]
lista2 = [4, 8, 9, 10]
diferencia_listas = diferencia_conjuntos(lista1, lista2)

conjunto1 = {1, 3, 5, 6, 7}
conjunto2 = {5, 7, 8, 9}
diferencia_conjuntos = diferencia_conjuntos(conjunto1, conjunto2)

print(f"Diferencia entre listas: {diferencia_listas}")
print(f"Diferencia_conjuntos: {diferencia_conjuntos}")

