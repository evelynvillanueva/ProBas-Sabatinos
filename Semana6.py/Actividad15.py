# Ejercicio 15: 15. Ordenamiento Merge Sort: Considera la siguiente lista: numeros = [40, 69, 6, 92, 41, 55, 81, 9]. Realiza una prueba de escritorio sobre como va cambiando la lista L que entra como argumento a la función, toma en cuenta que la función es recursiva.

def mergeSort(L):
    if len(L) > 1:
        mid = len(L) // 2  # Encuentra la mitad de la lista
        I = L[:mid]        # Parte izquierda
        D = L[mid:]        # Parte derecha

        mergeSort(I)       # Ordena la parte izquierda
        mergeSort(D)       # Ordena la parte derecha

        k = 0
        # Fusiona las dos partes ordenadas
        while len(I) > 0 and len(D) > 0:
            if I[0] < D[0]:
                L[k] = I[0]
                I.pop(0)
            else:
                L[k] = D[0]
                D.pop(0)
            k += 1

        # Si queda algo en I, lo añadimos a L
        while len(I) > 0:
            L[k] = I[0]
            I.pop(0)
            k += 1

        # Si queda algo en D, lo añadimos a L
        while len(D) > 0:
            L[k] = D[0]
            D.pop(0)
            k += 1


# Lista a ordenar
numeros = [40, 69, 6, 92, 41, 55, 81, 9]

# Imprimir lista original
print("Lista original:", numeros)

# Ordenamos la lista con Merge Sort
mergeSort(numeros)

# Imprimir lista ordenada
print("Lista ordenada:", numeros)
