#Ejercicio 5: Calculadora de descuento. Descripción que solicite al usuario el precio de un producto y el porcentaje de descuento, y calcule el precio final después del descuento.

p = float(input("Ingrese el precio del producto: "))
d = float(input("Ingrese el porcentaje de descuento: "))

pfinal = p - (p * d / 100)

print(f"El precio final del producto con el descuento es de: {pfinal}")