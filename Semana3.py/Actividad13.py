#Ejercicio 13: Verificación de año bisiesto. Descripción: Escribe una función que determine si un año dado es bisiesto o no. 

def es_bisiesto(año): 
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True 
    else: 
        return False
    
año = int(input("Introduce el año: "))

if es_bisiesto(año): 
    print(f"El año {año} es bisiesto.")
else:
    print(f"El año {año} no es bisiesto.")

    