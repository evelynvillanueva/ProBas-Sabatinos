import circulo 

if __name__ == "__main__":

    radio = float(input("Ingresa el radio del círculo: "))

    area = circulo.calcular_area_circulo(radio)

    print(f"El área del cícrulo con radio {radio} es: {area}")