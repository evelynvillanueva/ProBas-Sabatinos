#Ejercicio 1: Diccionario de Precios de Productos: Implementa un programa que almacene los precios de diferentes productos en un diccionario. El usuario debe poder buscar el precio de un producto dado su nombre.

precios_de_los_productos = {
    "pera": 15.5,
    "platáno": 12.65,
    "melón": 23.40,
    "zanahoria": 12, 
    "mandarina": 10
}

def buscar_precio(producto):
    
    if producto in precios_de_los_productos:
        return f"El precio de {producto} es: ${precios_de_los_productos[producto]}"
    else: 
        return f"El producto {producto} no se encontró en el diccionario."

while True:
    print("\n----- Diccionario con los precios de los productos.-----")
    producto = input("Introduzca el nombre del producto que desea buscar (o 'salir' para cerrar el programa): ").lower()

    if producto == 'salir': 
        print("¡Vuelva pronto!")
        break 

    resultado = buscar_precio(producto)
    print(resultado)