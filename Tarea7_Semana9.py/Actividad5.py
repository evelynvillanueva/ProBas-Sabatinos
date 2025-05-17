#Escribe un archivo de texto especifico. 

empleados = [
    {"nombre": "Alejandra", "edad": 26, "salario":20000},
    {"nombre": "Carlos", "edad": 33, "salario":45000},
    {"nombre": "Eduardo", "edad": 25, "salario":34500},
]

nombre_archivo = "empleados.txt"

with open(nombre_archivo, "w") as archivo: 
    for empl in empleados: 
        linea = f"Nombre: {empl['nombre']} | Edad: {empl['edad']} | Salario: {empl['salario']}" 
        archivo.write(linea)

print(f"Se han guardado {len(empleados)} empleados en el archivo '{nombre_archivo}'.")