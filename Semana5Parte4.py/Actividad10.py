#Ejercicio 10: Registro de Ventas por Producto y Mes: Escribe un programa que almacene información sobre las ventas de una tienda. Cada venta se representa como un diccionario con las claves “producto”, “mes” y “cantidad_vendida”. 


ventas = []


def registrar_venta():
    producto = input("Introduce el nombre del producto: ").capitalize()
    mes = input("Introduce el mes de la venta: ").capitalize()
    try:
        cantidad_vendida = int(input("Introduce la cantidad vendida: "))
        ventas.append({"producto": producto, "mes": mes, "cantidad_vendida": cantidad_vendida})
        print(f"Venta registrada: {producto} ({mes}) - {cantidad_vendida} unidades.\n")
    except ValueError:
        print("Por favor, ingresa un valor numérico válido para la cantidad vendida.\n")


def mostrar_ventas():
    producto = input("Introduce el nombre del producto a consultar: ").capitalize()
    mes = input("Introduce el mes a consultar: ").capitalize()
    total_vendido = sum(venta["cantidad_vendida"] for venta in ventas if venta["producto"] == producto and venta["mes"] == mes)
    if total_vendido > 0:
        print(f"\nTotal de {producto} vendido en {mes}: {total_vendido} unidades.\n")
    else:
        print(f"No se encontraron ventas de {producto} en {mes}.\n")


while True:
    print("\n1. Registrar venta")
    print("2. Consultar ventas")
    print("3. Salir")
    
    opcion = input("Elige una opción (1-3): ")
    
    if opcion == "1":
        registrar_venta()
    elif opcion == "2":
        mostrar_ventas()
    elif opcion == "3":
        print("Hasta luego, ¡buen día!")
        break
    else:
        print("Opción inválida.")
