#Ejercicio 10: Intersección de Conjuntos: Implementa una función que tome dos conjuntos y devuelva su intersección. 

def interseccion_conjuntos():

    conjunto1 = set(map(int, input("Introduzca los elementos del primer conjunto: ").split()))
    conjunto2 = set(map(int, input("Introduzca los elementos del segundo conjunto: ").split()))

    interseccion = conjunto1 & conjunto2 

interseccion_conjuntos()