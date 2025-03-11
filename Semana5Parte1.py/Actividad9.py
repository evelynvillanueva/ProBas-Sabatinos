#Ejericio 9:Fusión de Listas Ordenadas: Implementa una función que tome dos listas ordenadas y las fusione en una nueva lista ordenada. Utiliza sort o sorted.

def fusionar_listas_ordenadas(lista1, lista2): 

    return sorted(set(lista1 + lista2))

lista1 = [1, 2, 3, 4]
lista2 = [3, 5, 7, 9]

resultado = fusionar_listas_ordenadas(lista1, lista2)
print(f"Lista fusionada y ordenada: {resultado}")
