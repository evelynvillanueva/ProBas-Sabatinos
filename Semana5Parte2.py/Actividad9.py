
#Ejercicio 9: Unión de Conjuntos: Diseña un programa que tome dos conjuntos y devuelva la unión de ambos.

def union_conjuntos():

    conjunto1 = set(map(int, input("Introduzca los elementos del primer conjunto: ").split()))
    conjunto2 = set(map(int, input("Introduzca los elementos del segundo conjunto: ").split()))

    union = conjunto1 | conjunto2 

    print(f"La unión de los conjuntos es: {union}")

union_conjuntos()
