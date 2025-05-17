import openpyxl

datos = [
    ["Producto", "Cantidad", "Precio"],
    ["Manzanas", 50, 0.5],
    ["Naranjas", 30, 0.75]
]

libro = openpyxl.Workbook()

hoja = libro.active
hoja.title = "Ventas"

for fila in datos: 
    hoja.append(fila)

libro.save(r"C:\Users\meryc\Desktop\mi_libro.xlsx")

print("El archivo 'ventas.xlsx' se ha creado exitosamente y los datos se han ingresado al documento.")