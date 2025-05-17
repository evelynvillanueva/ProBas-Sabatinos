#División por cero. 

def dividir(a, b):
    try: 
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")
        return None
    
    

