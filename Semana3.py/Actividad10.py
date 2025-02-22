#Ejercicio 10: Función para calcular el MCD. Descripción: Escribe una función que calcule el máximo común divisor (MCD) de dos números. 

def mcd(a, b):
    menor = min(a,b)

    for i in range(menor, 0, -1):
        if a % i == 0 and b % i == 0: 
            return i
        
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el segundo número: "))
resultado = mcd(num1, num2)
print(f"El máximo común divisor de {num1} y {num2} es: {resultado}")

