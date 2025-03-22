from conversor_unidades import ConversorUnidades 

def main(): 

    conversor = ConversorUnidades()

    metros = 10 
    pies = conversor.metros_a_pies(metros)
    print(f"{metros} metros son {pies} pies")

    kilogramos = 5
    libras = conversor.kilogramos_a_libras(kilogramos)
    print(f"{kilogramos} kilogramos son {libras} libras")

    celsius = 25
    fahrenheit = conversor.celsius_a_fahrenheit(celsius)
    print(f"{celsius} grados Celsius son {fahrenheit} grados fahrenheit")

    litros = 3
    galones = conversor.litros_a_galones(litros)
    print(f"{litros} son {galones} galones")

    metros_cuadrados = 50
    pies_cuadrados = conversor.metros_cuadrados_a_pies_cuadrados(metros_cuadrados)
    print(f"{metros_cuadrados} metros cuadrados son {pies_cuadrados} pies cuadrados")

    kilometros = 100
    millas = conversor.kilometros_a_millas(kilometros)
    print(f"{kilometros} kilómetros son {millas} millas")

if __name__ == "__main__": 
    main()
