#Ejercicio 5: Búsqueda de Elemento en Matriz: Crea una función que tome una matriz y un elemento. Verifica si el elemento está presente en la matriz y devuelve su posición (fila y columna). 

def buscar_elemento():

    matriz = []
    for i in range(3):
        fila = []
        for j in range(3):
            valor = int(input(f"Ingresa el elemento ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)

    elemento = int(input("Ingresa el elemento que quieres buscar: "))

    for i in range(3):
        for j in range(3):
            if matriz[i][j] == elemento:
                print(f"El elemento se encontró en la posición: Fila {i+1}, Columna {j+1}")
                return 
            
    print("No se encontró el elemento.")

buscar_elemento()
    