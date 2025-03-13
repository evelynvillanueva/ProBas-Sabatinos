#Ejercicio 2: Comprobación de Subconjunto: Crea una función que verifique si un conjunto es subconjunto de otro. 

def si_es_subconjunto(conjunto1, conjunto2):

    return conjunto1.issubset(conjunto2)

conjunto1 = {3, 5, 7}
conjunto2 = {2, 3, 4, 5, 6, 7, 7}

resultado = si_es_subconjunto(conjunto1, conjunto2)

if resultado: 
    print(f"{conjunto1} sí es subconjunto de {conjunto2}")
else: 
    print(f"{conjunto1} no es subconjunto de {conjunto2}")

    