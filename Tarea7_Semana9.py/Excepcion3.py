#Acceso a elemento de lista. 

def obtener_elemento(lista, indice):
    try: 
        elemento = lista[indice]
        return elemento
    except IndexError:
        print(f"Error: el índice {indice} está fuera del rango de la lista.")
        return None