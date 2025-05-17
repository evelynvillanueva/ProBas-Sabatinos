#Ejercicio 9: Diccionario de Sinónimos: Crea un diccionario que contenga palabras y sus sinónimos. El usuario debe poder buscar sinónimos para una palabra dada. Al finalizar, imprime solo las claves del diccionario. 

def buscar_sinonimos(diccionario_con_sinonimos, palabra): 

    if palabra in diccionario_con_sinonimos:
        return diccionario_con_sinonimos[palabra]
    else:
        return f"No se encontró ningún sinónimo para '{palabra}'."
    
diccionario_con_sinonimos = {
    "bello": ["hermoso", "bonito", "primoroso"], 
    "angosto": ["estrecho", "reducido", "apretado"], 
    "callado": ["silencioso", "reservado", "sigiloso"], 
    "escaso": ["exiguo", "insuficiente", "pobre"]
}

palabra_ingresada = input("Ingrese la palabra que desea buscar en los sinónimos: ").lower()

sinonimos = buscar_sinonimos(diccionario_con_sinonimos, palabra_ingresada)

if isinstance(sinonimos, list):
    print(f"Sinónimos de '{palabra_ingresada}': {', '.join(sinonimos)}")
else: 
    print(sinonimos)

print("\nPalabras contenidas en el diccionario:")
for palabra in diccionario_con_sinonimos.keys():
    print(palabra)
