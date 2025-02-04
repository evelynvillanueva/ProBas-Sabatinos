#Ejercicio 8: Calculadora de año bisiesto. Descripción: Escribe un programa que determine si un año dado es bisiesto o no. Un año es bisiesto si es divisible por 4, pero no por 100, a menos que también sea divisible por 400. 

año = int(input("Ingrese el año: "))

if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)): 
    print(f"{año} es bisiesto.")
else:
    print(f"{año} no es bisiesto.")
    