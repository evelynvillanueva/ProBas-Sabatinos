#Ejercicio 3: Contador de Vocales y Consonantes: Diseña una función que tome una palabra y cuente cuántas vocales y cuántas consonantes contiene. Considera tanto mayúsculas como minúsculas. 

def contar_vocales_consonantes(palabra):
    vocales = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    contador = {'vocales': 0, 'consonantes': 0}

    for letra in palabra: 

        if letra.isalpha(): 

            if letra in vocales: 
                contador['vocales'] += 1
            else: 
                contador['consonantes'] += 1
    
    return (contador['vocales'],  contador['consonantes'])

palabra = "Almost Easy"
vocales, consonantes = contar_vocales_consonantes(palabra)
print(f"Vocales: {vocales}, Consonantes: {consonantes}")