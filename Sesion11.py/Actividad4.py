#Definición de una Función Matemática.

from sympy import symbols, Function, limit, diff 

x = symbols('x')

f = x**2 + 3*x + 2

valor = float(input("Ingrese el valor del que desea calcular el límite de la función: "))

limite = limit(f, x, valor)
print(f"Límite de f(x) cuando x tiende a {valor}: {limite}")

derivada = diff(f, x)
print(f"Derivada de f(x): {derivada}")
