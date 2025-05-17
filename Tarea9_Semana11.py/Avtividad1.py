#Suma y multiplicación de fracciones.

from math import gcd 

class Fraccion: 
    def __init__(self, numerador, denominador): 
        if denominador == 0:
            raise ValueError("El denominador no puede ser cero.")
        comun = gcd(numerador, denominador)
        self.numerador = numerador // comun
        self.denominador = denominador // comun

    def __str__(self):
        return f"{self.numerador}/{self.denominador}"
    
    def __add__(self, otra_fraccion): 
        nuevo_numerador = (self.numerador * otra_fraccion.denominador) + (otra_fraccion.numerador * self.denominador)
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    def __mul__(self, otra_fraccion):
        nuevo_numerador = self.numerador * otra_fraccion.numerador
        nuevo_denominador = self.denominador * otra_fraccion.denominador
        return Fraccion(nuevo_numerador, nuevo_denominador)
    
    