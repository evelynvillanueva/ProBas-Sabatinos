# Gráfica de barras horizontales. 

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

plt.barh(categorias, valores, color='green')

plt.xlabel("Valores")
plt.ylabel("Categorías")

plt.title("Gráfica de barras horizontales")

plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.show()