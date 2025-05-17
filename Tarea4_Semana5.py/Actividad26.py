#Ejercicio 6: Eliminación de Elementos en Conjunto: Implementa un programa que tome un conjunto y elimine un elemento específico si está presente. 

def eliminar_elementos(conjunto, elemento): 

    if elemento in conjunto:
        conjunto.remove(elemento)
        print(f"El elemento '{elemento}' se ha eliminado.")
    else: 
        print(f"El elemento '{elemento}'  no se ha encontrado en el conjunto.")

    return conjunto 

conjunto = {1, 3, 4, 5, 6}

eliminar_el_elemento = 4

conjunto_actualizado = eliminar_elementos(conjunto, eliminar_el_elemento)

print(f"Conjunto actualizado: {conjunto_actualizado}")

