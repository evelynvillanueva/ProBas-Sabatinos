#Ejercicio 9: Función para encontrar el segundo mayor en una lista. Descripción: Escribe una función que encuentre el segundo número mayor en una lista de números. 

def segundo_mayor(lista): 

    lista_sin_num_repetidos = list(set(lista))
    lista_sin_num_repetidos.sort(reverse=True)

    if len(lista_sin_num_repetidos) < 2: 
        return None 
    else: 
        return lista_sin_num_repetidos[1]

numeros = [int(a) for a in input("Introduce una lista de números separados por un espacio: ").split()]
resultado = segundo_mayor(numeros)

if resultado is None: 
    print("No hay segundo mayor en la lista.")
else: 
    print(f"El número mayor es: {resultado}")

    