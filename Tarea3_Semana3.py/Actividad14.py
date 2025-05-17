
#Ejericicio 14: Calculadora de Polinomios. Descripción: Escribe una función que reciba los coeficientes de un polinomio y un valor de x, y calcule el valor del polinomio en ese punto. Usa la fórmula: 
#P(x) = a_n x^n + a_{n-1} x^{n-1} + \ldots + a_1 x + a_0

def calcular_polinomio(coeficientes, x):
    resultado = 0 

    n = len(coeficientes) -1 
    i = 0
    while i <= n:
        resultado += coeficientes[i] * (x ** (n - i))
        i += 1
        return resultado 

coeficientes = [2, 3, 5, 7]
x = 3

resultado = calcular_polinomio(coeficientes, x)
print(f"Resultado del polinomio: {resultado}")