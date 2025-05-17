#Conversión de cadena a entero.

def convertir_a_entero(cadena):
    try: 
        numero = int(cadena)
        return numero 
    except ValueError:
        print(f"Error: '{cadena}' no es un número entero válido.")
        return None
    