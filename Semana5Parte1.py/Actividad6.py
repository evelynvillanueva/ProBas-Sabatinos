#Ejercicio 6: Contador de Ocurrencias de una Subcadena: Diseña una función que tome una cadena y una subcadena, y cuente cuántas veces aparece la subcadena en la cadena principal. 

def contar_ocurrencias(cadena, subcadena): 

    contador = {'ocurrencias': 0}

    indices = []

    for i in range(len(cadena) - len(subcadena) + 1): 


        if cadena[i:i + len(subcadena)] == subcadena: 
            contador['ocurrencias'] += 1

            indices.append(i)

    return contador['ocurrencias'], tuple(indices)

cadena = "Había una vez un principito que vivía en un planeta apenas más grande que él y que tenía la necesidad de un amigo... Para aquéllos que comprenden la vida les habría parecido mucho más real. Detesto que se lea mi libro a la ligera. Me entristece relatar estos recuerdos!."
subcadena = "que"
ocurrencias, indices = contar_ocurrencias(cadena, subcadena)
print(f"La subcadena '{subcadena}' aparece {ocurrencias} veces en la cadena.")
print(f"Índices donde aparece: {indices}")
