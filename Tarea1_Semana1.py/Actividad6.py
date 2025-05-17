#Ejercicio 6: Conversión de temperaturas. Descripción: Escribe un programa que convierta una temperatura dada en grados Celsius a grados Fahrenteit y Kelvin. 

celsius = float(input("Ingrese la temperatura en grados celsius: "))

fahrenheit = (celsius * 9/5) + 32 
kelvin = celsius + 273.15

print(f"{celsius}°C es igual a {fahrenheit}°F y {kelvin}K")

