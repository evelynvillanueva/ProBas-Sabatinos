#Ejercicio 7: Registro de Compras en una Tienda: Diseña un programa que permita al usuario ingresar información sobre las compras realizadas en una tienda. Cada compra se representa como una tupla (producto, cantidad, precio_unitario). Calcula el total gastado por el cliente.


compras = []

def ingrese_las_compras():
    while True: 
        producto = input("Introduzca el nombre del producto (o 'salir' para cerrar el programa): ").lower()
        if producto == 'salir':
            break 
        try: 
            cantidad = int(input(f"Introduzca la cantidad de {producto}: "))
            precio_unitario = float(input(f"Introduzca el precio unitario de {producto}: "))
            compras.append((producto, cantidad, precio_unitario))
        except ValueError: 
            print("Ingrese los valores correctos y válidos de la cantidad y el precio.")

def calcular_total():
    total = sum(cantidad * precio for _, precio in compras)
    return total 

ingrese_las_compras()

total_gastado = calcular_total()
print(f"\nEl total gastado por el cliente fue de: ${total_gastado:.2f}")