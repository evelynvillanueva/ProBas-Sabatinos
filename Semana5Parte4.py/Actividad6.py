#Ejercicio 6: Registro de Temperaturas Diarias: Diseña un programa que permita al usuario ingresar las temperaturas diarias de una semana. Cada día se representa como una tupla (día, temperatura). Luego, muestra la temperatura promedio de la semana. 

termperaturas_semanales = []

def ingrese_temperaturas(): 
    dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

    for dia in dias: 
        while True: 
            try: 
                temperatura = float(input(f"Introduzca la temperatura del {dia}: "))
                termperaturas_semanales.append((dia, temperatura))
                break 
            except ValueError: 
                print("Ingrese una temperatura válida.")

def calcular_promedio_de_temperatura():
    total_de_temperaturas = sum(temperatura for _, temperatura in termperaturas_semanales)
    promedio = total_de_temperaturas / len(termperaturas_semanales)
    return promedio 

ingrese_temperaturas()

promedio = calcular_promedio_de_temperatura()
print(f"\nLa temperatura de la semana es: {promedio:.2f}°C")

