#Ejercicio 7: Formateo de Nombres Completos: Escribe un programa que tome un nombre completo (por ejemplo, “Juan Pérez Gómez”) y devuelva las iniciales en mayúsculas (por ejemplo, “JPG”). 

def generar_iniciales(nombre_completo): 
    partes_del_nombre = nombre_completo.split()

    resultado_inciales = {'iniciales': []}

    for parte in partes_del_nombre: 
        resultado_inciales['iniciales'].append(parte[0].upper())

    return ''.join(resultado_inciales['iniciales'])

nombre = "Evelyn Alejandra Villanueva Herrera"
iniciales = generar_iniciales(nombre)
print(f"Las iniciales son: {iniciales}")
 
