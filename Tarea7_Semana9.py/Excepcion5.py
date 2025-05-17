#Acceso a clave de diccionario. 

def obtener_valor(diccionario, clave):
    try: 
        valor = diccionario[clave]
        return valor
    except KeyError:
        print(f"Error: la clave '{clave}' no existe en el diccionario")
        return None