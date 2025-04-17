
# Gráficas de líneas con marcadores.

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

plt.plot(x, y, marker='*', linestyle='-', color='red', label='x^2')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.title("Gráfica de líneas con marcadores")

plt.grid(True)
plt.legend()
plt.show()