from temperatura import convertir_celsius_a_fahrenheit as cel_to_fah

from temperatura import convertir_fahrenheit_a_celsius as fah_to_cel

if __name__ == "__main__":

    print("-----Conversor de temperaturas.-----")
    print("1. Celsius a Fahrenheit.")
    print("2. Fahrenheit a Celsius.")

    opcion = int(input("Selecciona la opción (1 o 2): "))

    if opcion == 1: 

        grados_celsius = float(input("Ingresa la temperatura en grados celsius: "))
        grados_fahrenheit = cel_to_fah(grados_celsius)
        print(f"{grados_celsius} °C es igual a {grados_fahrenheit} °F")
    
    elif opcion == 2: 

        grados_fahrenheit = float(input("Ingresa la temperatura en grados fahrenheit: "))
        grados_celsius = fah_to_cel(grados_fahrenheit)
        print(f"{grados_fahrenheit} °F es igual a {grados_celsius} °C")
    
    else: 
        print("Opción inválida. Seleccione la opción 1 o 2.")

