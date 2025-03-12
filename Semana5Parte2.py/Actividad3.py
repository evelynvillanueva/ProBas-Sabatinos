#Ejercicio 3: Producto Escalar de Vectores: Diseña un programa que tome dos vectores (listas de números del tipo i_x, i_y, i_z) y calcule su producto escalar. Los vectores deben tener la misma longitud. 

def capturar_vector(nombre_vector):

    vector = input(f"Ingresa las coordenadas del {nombre_vector} vector: ")
    x = int(input("i_x: "))
    y = int(input("i_y: "))
    z = int(input("i_z: "))

    return [x, y, z]

def producto_escalar(v1, v2):

    if len(v1) != len(v2):
        return "Los vectores deben tener la misma longitud."
    
    resultado = sum(v1[i] * v2[i] for i in range(len(v1)))
    return resultado 

vector1 = capturar_vector("primero")
vector2 = capturar_vector("segundo")

resultado = producto_escalar(vector1, vector2)

if type(resultado) == str:
    print(resultado)
else: 
    print(f"\nEl producto escalar de los vectores es: {resultado}")
    
