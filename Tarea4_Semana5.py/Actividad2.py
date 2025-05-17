#Ejercicio 2: Revisión de palabras en una frase: Escribe un programa que tome una frase y devuelva una nueva frase con las palabras invertidas. Por ejemplo, si la entrada es "Hola, mnundo", la salida debería ser "aloh odnum".

def invertir_palabras(frase):

    palabras = frase.split()

    palabras_invertidas = [palabra [::-1] for palabra in palabras]

    return ' '.join(palabras_invertidas)

print(invertir_palabras("hola mundo"))