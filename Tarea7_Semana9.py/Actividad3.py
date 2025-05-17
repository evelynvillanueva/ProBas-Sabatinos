#Lectura y parseo de números enteros. 

nombre_archivo = "numeros_enteros.txt"

numeros_enteros = []

try: 
    with open(nombre_archivo, "r") as archivo: 
        for linea in archivo: 
            try: 
                numero = int(linea.strip())
                numeros_enteros.append(numero)
            except ValueError: 
                print(f"Valor incorrecto: '{linea.strip()}'")

    suma_total = sum(numeros_enteros)

    print("Lista de números:", numeros_enteros)
    print("Suma total:", suma_total)

except FileNotFoundError: 
    print(f"El archivo '{nombre_archivo}' no fue encontrado.")