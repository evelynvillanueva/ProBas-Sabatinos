# Gráfica de puntos de dispersi+on con tamaños de puntos variables.

import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]
tamaños = [20, 50, 80, 100, 150]

plt.scatter(x, y, s=tamaños, color='skyblue', edgecolor='blue')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.title("Gráfica de dispersión con tamaños variables")

plt.grid(True)
plt.show()


