#Ejercicio 5: Cifrado César Personalizado: Implementa una función que tome una cadena y un desplazamiento (número entero). Realiza un cifrado César en la cadena, desplazando cada letra según el valor dado. Asegúrate de manejar correctamente los límites del alfabeto (por ejemplo, si llegas a ‘z’, debes volver a ‘a’). 

def cifrado_cesar(cadena, desplazamiento):

    alfabeto = list("abcdefghijklmnñopqrstuvwxyz")

    diccionario_alfabeto = {letra: i for i, letra in enumerate(alfabeto)}

    cadena_cifrada = []

    for char in cadena: 
        if char.isalpha():
            is_upper = char.isupper()
            char = char.lower()

            indice = diccionario_alfabeto[char]

            nuevo_indice = (indice + desplazamiento) % 26

            nueva_letra = alfabeto[nuevo_indice]

            if is_upper:
                nueva_letra = nueva_letra.upper()

            cadena_cifrada.append(nueva_letra)

        else: 
            cadena_cifrada.append(char)

    return ''.join(cadena_cifrada) 

cadena = "Hola Mundo!"
desplazamiento = 3 
resultado = cifrado_cesar(cadena, desplazamiento)
print(f"Cadena cifrada: {resultado}")
