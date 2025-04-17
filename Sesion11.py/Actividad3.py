# Cálculo de media, moda y mediana. 

import statistics 

print("Introduce 25 números enteros separaos por espacios: ")
entrada = input()

numeros = list(map(int, entrada.split()))

if len(numeros) != 25:
    print("Error: Ingrese los 25 números.")
else: 

    media = statistics.mean(numeros)
    mediana = statistics.median(numeros)
    moda = statistics.mode(numeros)

    print(f"\n---Resultados---")
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Moda: {moda}")

    