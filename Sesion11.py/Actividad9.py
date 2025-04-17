# Gráficas con líneas múltiples series.

import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y1 = [0, 1, 4, 9, 16, 25]
y2 = [0, 1, 2, 3, 4, 5]

plt.plot(x, y1, label='x al cuadrado', color='blue', marker='o')
plt.plot(x, y2, label='x lineal', color='green', marker='s')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.title("Gráfica de líneas con múltiples series")
plt.legend()

plt.grid(True)
plt.show()
         