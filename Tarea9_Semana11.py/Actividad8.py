import matplotlib.pyplot as plt

etiquetas = ['Manzanas', 'Naranjas', 'Plátanos', 'Uvas']
tamaños = [30, 25, 20, 25]
colores = ['green', 'orange', 'yellow', 'purple']

plt.pie(tamaños, labels=etiquetas, colors=colores, autopct='%1.1f%%', startangle=90)

plt.axis('equal')

plt.legend(etiquetas, title="Frutas")

plt.title("Distribución de Frutas")

plt.show()