import matplotlib.pyplot as plt
import numpy as np

# Parâmetro t para a epicicloide
t = np.linspace(0, 2 * np.pi, 1000)

# Equações paramétricas da epicicloide
x = 5 * np.cos(t) - np.cos(5 * t)
y = 5 * np.sin(t) - np.sin(5 * t)

# Configuração do gráfico 2D
plt.figure(figsize=(8, 6))
plt.plot(x, y, color='green', linewidth=1)
plt.title("Epicicloide")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.grid(True)
plt.show()
