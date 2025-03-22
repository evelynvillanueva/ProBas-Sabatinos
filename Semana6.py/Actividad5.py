#Ejericicio 5: Suma de Números Naturales: Implementa una función recursiva que calcule la suma de los primeros n números naturales.


def suma_numeros_naturales(numeros): 

    if numeros == 0:
        return 0
    
    return numeros + suma_numeros_naturales(numeros - 1)

cantidad = 9
resultado = suma_numeros_naturales(cantidad)
print(f"La suma de los primeros {cantidad} números naturales es: {resultado}")