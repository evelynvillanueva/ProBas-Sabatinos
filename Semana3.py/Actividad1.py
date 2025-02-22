#Ejercicio 1: Función con valores por omisión. Descripción: Escribe una función que reciba el nombre y la edad de una persona, y muestre un mensaje. Si la edad no se proporciona, debe asumir que es 18.

def mensaje(): 
    nombre = input("Ingrese su nombre: ")
    edad = input("Ingrese su edad: ")

    if not edad: 
        edad = 18
    else: 
        edad = int(edad)

    print(f"Hola {nombre}, tienes {edad} años.")

mensaje()
