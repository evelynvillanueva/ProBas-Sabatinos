class CifradorCesar:

    def __init__(self, desplazamiento):
        self.desplazamiento = desplazamiento
        self.SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ' + 'abcdefghijklmnopqrstuvwxyz1234567890 !?.'

    def cifrar(self, mensaje):
        """Cifra un mensaje usando el cifrado César."""
        mensajec = ""
        longitud = len(self.SYMBOLS)

        for letra in mensaje:
            if letra not in self.SYMBOLS:
                # Si el carácter no está en los símbolos permitidos, lo dejamos igual
                mensajec += letra
                continue

            # Encontramos la posición de la letra en el alfabeto
            i = self.SYMBOLS.index(letra) + self.desplazamiento

            # Si la posición excede el rango, ajustamos para volver al inicio
            if i >= longitud:
                i -= longitud

            mensajec += self.SYMBOLS[i]

        return mensajec

    def descifrar(self, mensajec):
        """Descifra un mensaje cifrado usando el cifrado César."""
        mensajed = ""

        for letra in mensajec:
            if letra not in self.SYMBOLS:
                # Si el carácter no está en los símbolos permitidos, lo dejamos igual
                mensajed += letra
                continue

            # Encontramos la posición de la letra en el alfabeto
            i = self.SYMBOLS.index(letra) - self.desplazamiento

            # Si la posición es negativa, ajustamos para volver al final
            if i < 0:
                i += len(self.SYMBOLS)

            mensajed += self.SYMBOLS[i]

        return mensajed
