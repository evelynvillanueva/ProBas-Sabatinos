import openpyxl

libro = openpyxl.Workbook()

hoja = libro.create_sheet("Datos")

libro.save(r"C:\Users\meryc\Desktop\mi_libro.xlsx")

print("El libro 'mi_libro.xlsx' con la hoja 'Datos' se ha creado y guardado.")