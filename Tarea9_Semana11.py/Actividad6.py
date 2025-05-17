# Gráfica de barras.

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]

plt.bar(categorias, valores, color='blue')

plt.xlabel("Categorías")
plt.ylabel("Valores")

plt.title("Gráfica de barras")

plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()



