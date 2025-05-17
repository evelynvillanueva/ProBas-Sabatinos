#Ejericio 6: Tabla de Multiplicar. Descripción: Escribe un programa que genere la tabla de multiplicar de un número dado por el usuario.

num = int(input("Ingrese un número para generar su tabla de multplicar: "))

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

