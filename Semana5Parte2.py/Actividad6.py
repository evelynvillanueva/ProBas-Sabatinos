#Ejericio 6: Suma de Diagonales en una Matriz Cuadrada: Escribe un programa que tome una matriz cuadrada de 5 x 5 y calcule la suma de sus diagonales (principal y secundaria). 

def suma_diagonales():

    matriz = []
    for i in range(5):
        fila = []
        for j in range(5):
            valor = int(input(f"Ingresa el elemento en la posición ({i+1},{j+1}): "))
            fila.append(valor)
        matriz.append(fila)

    suma_diagonal_prin = 0 
    suma_diagonal_secu = 0

    for i in range(5):
        suma_diagonal_prin += matriz[i][i]
        suma_diagonal_secu += matriz[i][4-i]
    
    print(f"La suma de la diagonal principal es: {suma_diagonal_prin}")
    print(f"La suma de la diagonal secundaria es: {suma_diagonal_secu}")

suma_diagonales()
    




