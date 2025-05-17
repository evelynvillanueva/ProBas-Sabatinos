#Division de elementos de lista.

def dividir_elementos(lista, divisor):
    try: 
        resultados = [elemento / divisor for elemento in lista]
        return resultados
    except ZeroDivisionError:
        print("Error: no se puede dividir entre cero.")
        return None