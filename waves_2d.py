import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Tamanho da grade
tamanho = 100
altura = np.zeros((tamanho, tamanho))
velocidade = np.zeros_like(altura)
altura_nova = np.copy(altura)

# Função de atualização
def atualiza(frame):
    global altura, altura_nova, velocidade

    # Cálculo da diferença com vizinhos (laplaciano discreto)
    for i in range(1, tamanho-1):
        for j in range(1, tamanho-1):
            laplaciano = (
                altura[i+1, j] + altura[i-1, j] + altura[i, j+1] + altura[i, j-1] - 4 * altura[i, j]
            )
            velocidade[i, j] += laplaciano * 0.1
            velocidade[i, j] *= 0.99  # dissipação
            altura_nova[i, j] = altura[i, j] + velocidade[i, j]

    altura = np.copy(altura_nova)

    # Adiciona uma perturbação periódica no centro
    if frame % 50 == 0:
        altura[tamanho//2, tamanho//2] += 1

    mat.set_array(altura)
    return [mat]

fig, ax = plt.subplots()
mat = ax.matshow(altura, cmap='viridis', vmin=-1, vmax=1)
ani = animation.FuncAnimation(fig, atualiza, interval=50, blit=True)
plt.title("Simulação 2D de Ondas na Água")
plt.show()
