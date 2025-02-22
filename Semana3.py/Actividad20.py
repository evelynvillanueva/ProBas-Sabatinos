#Ejercicio 20: Cálculo del MCM. Descripción: Escribe una función que calcule el mínimo común múltiplo (MCM) de dos números. 

def gcd(x, y): 
    while y:
        x, y = y, x % y
    return x

def calcular_mcm(a, b):
    return (a * b) // gcd(a, b)

#Ejemplo de uso 
numero1 = int(input("Ingresa un número: "))
numero2 = int(input("Ingresa un número: "))
mcm_resultante = calcular_mcm(numero1, numero2)
print(f"El MCM de {numero1} y {numero2} es: {mcm_resultante}")

# 1. ¿Cuál es el propósito de la función 'gcd' en el código proporcionado? D. Calcular el máximo común divisor de dos números. 

# 2. En el cáclculo del MCM, ¿qué papel juega el resultado de la función 'gcd'? A. Se utiliza para dividir el producto de los números. 


# 3. Si los números ingresados son y 12, ¿cuál será el resultado de 'calcular_mcm'? C. 24


# 4. Si 'x' es inicialmente 15 y 'y' es 10 en la función 'gcd', ¿cuál será el primer valor de 'x' y 'y' en la primera iteración del bucle? C. x= 10, y y= 5


# 3. ¿Qué pasa si se ingresara un número negativo en 'calcular_mcm'? D. El MCM se calcularía como si el número fuera positivo. 



