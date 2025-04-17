# Aluno: Marcel Gustavo de Barros Araujo.
# Curso: Engenharia da Computação.


import matplotlib.pyplot as plt
import numpy as np

# Parâmetros da hélice
altura_total = 10  
num_voltas = 10

# Configura o parâmetro t para 10 voltas completas
t = np.linspace(0, num_voltas * 2 * np.pi, 1000)  
# Equações paramétricas
x = np.cos(t)            
y = np.sin(t)            
z = (altura_total / (num_voltas * 2 * np.pi)) * t  # Ajusta a altura z para 10 cm
# Plotagem 3D
ax = plt.axes(projection='3d')
ax.plot3D(x, y, z, color='green', linewidth=1)
ax.set_title("Hélice Circular (10 voltas, 10 cm)")
ax.set_zlabel('Z (cm)')
plt.show()
