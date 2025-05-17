#Gráfica de barras con etiquetas de datos.

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

plt.bar(categorias, valores, color='black')

plt.xlabel("Categorías")
plt.ylabel("Valores")

for i, valor in enumerate(valores):
    plt.text(i, valor + 0.5, str(valor), ha='center')

plt.title("Gráfica de barras con etiquetas de datos")

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
