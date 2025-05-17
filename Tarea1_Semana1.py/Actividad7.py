#Ejercicio 7: Calculadora de IMC. Descripción: Escribe un programa que calcule el Índice de Masa Corporal (IMC) de una persona, dado su peso y altura. El IMC se calcula con la fórmula: 
#IMC = peso(kg)/ altura(m^2)

peso = float(input("Ingrese su peso en kilogramos: "))
altura = float(input("Ingrese su altura en metros: "))

imc = peso / altura ** 2

print("Su IMC es: ", imc)

