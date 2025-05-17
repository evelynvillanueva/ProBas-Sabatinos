# Gráfica de barras con colores personalizados.

import matplotlib.pyplot as plt

categorias = ['A', 'B', 'C', 'D']
valores = [10, 20, 15, 25]
colores = ['red', 'black', 'blue', 'gray']

plt.bar(categorias, valores, color=colores)

plt.xlabel("Categorías")
plt.ylabel("Valores")

plt.title("Gráfica de barras con colores personalizados")

plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
