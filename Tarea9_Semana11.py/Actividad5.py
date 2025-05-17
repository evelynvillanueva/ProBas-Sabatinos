#Gráfica (plot).

import matplotlib.pyplot as plt 

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.scatter(x, y, color='red')

plt.xlabel("Eje X")
plt.ylabel("Eje Y")

plt.title("Gráfica de puntos")
plt.grid(True)
plt.show()

