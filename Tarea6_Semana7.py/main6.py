from cifrador_cesar import CifradorCesar

def main():
    # Crear una instancia de CifradorCesar con un desplazamiento de 4
    cifrador = CifradorCesar(4)

    # Mensaje original
    mensaje_original = "¡Hola Mundo! ¿Cómo estás?"
    print(f"Mensaje original: {mensaje_original}")

    # Cifrar el mensaje
    mensaje_cifrado = cifrador.cifrar(mensaje_original)
    print(f"Mensaje cifrado: {mensaje_cifrado}")

    # Descifrar el mensaje
    mensaje_descifrado = cifrador.descifrar(mensaje_cifrado)
    print(f"Mensaje descifrado: {mensaje_descifrado}")

if __name__ == "__main__":
    main()
