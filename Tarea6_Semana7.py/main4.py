from vector_3d import Vector3D

def main():

    vector1 = Vector3D(3, 4, 5)
    vector2 = Vector3D(1, 2, 3)

    resultado_suma = vector1.suma(vector2)
    print(f"Suma: {resultado_suma}")

    resultado_resta = vector1.suma(vector2)
    print(f"Resta: {resultado_resta}")

    producto = vector1.producto_escalar(vector2)
    print(f"Producto escalar: {producto}")

    modulo_vector1 = vector1.modulo()
    print(f"Módulo del vector 1: {modulo_vector1}")

    vector1_normalizado = vector1.normalizar()
    print(f"Vector1 normalizado: {vector1_normalizado}")

if __name__ == "__main__":
    main()
    