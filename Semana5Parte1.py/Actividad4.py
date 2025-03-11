#Ejercicio 4: Eliminación de Espacios Extra: Escribe un programa que tome una cadena con espacios adicionales y elimine los espacios redundantes. Por ejemplo, si la entrada es “Hola mundo”, la salida debería ser “Hola mundo”.

def elimina_espacios(cadena):
    
    return ' '.join(cadena.split())

cadena = "Hola      mundo"
resultado = elimina_espacios(cadena)
print(f"Cadena sin espacios extra: {resultado}")
