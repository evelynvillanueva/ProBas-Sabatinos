#Ejercicio 4: Verificación de Conjunto Vacío: Escribe un programa que tome un conjunto y determine si está vacío o no. 

def esta_vacio(conjunto):

    return len(conjunto) == 0

conjunto1 = {3, 4, 5}
conjunto2 = set()

if esta_vacio(conjunto1): 
    print("El conjunto1 está vacío.")
else: 
    print("El conjunto1 no está vacío.")

if esta_vacio(conjunto2):
    print("El conjunto2 está vacío.")
else: 
    print("El conjunto2 no está vacío.")
    