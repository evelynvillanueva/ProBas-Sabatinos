from calculadora_cientifica import CalculadoraCientifica 

calculadora = CalculadoraCientifica()

numero = 16
print(f"La raíz cuadrada de {numero} es: {calculadora.calcular_raiz_cuadrada(numero)}")

numero = 100 
print(f"El logaritmo de {numero} en base 10 es: {calculadora.calcular_logaritmo(numero)}")

base = 2
exponente = 3

print(f"{base} elevado a la potencia de {exponente} es: {calculadora.calcular_potencia(base, exponente)}")

angulo = 30
print(f"El seno de {angulo} grados es: {calculadora.calcular_seno(angulo)}")

print(f"El coseno de {angulo} grados es: {calculadora.calcular_coseno(angulo)}")

print(f"La tangente de {angulo} grados es: {calculadora.calcular_tangente(angulo)}")