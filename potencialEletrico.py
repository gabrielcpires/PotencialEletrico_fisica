import matplotlib.pyplot as plt
import numpy as np

# Função para calcular o potencial elétrico em um ponto devido a uma carga
def potencial_electrico(carga, posicao, ponto):
    k = 8.99e9  # Constante eletrostática
    distancia = np.sqrt((posicao[0] - ponto[0])*2 + (posicao[1] - ponto[1])*2)
    return k * carga / distancia

# Função para desenhar as cargas no gráfico
def desenhar_cargas(cargas, posicoes):
    for i, carga in enumerate(cargas):
        plt.scatter(posicoes[i][0], posicoes[i][1], s=100 * abs(carga), c='red' if carga > 0 else 'blue')
        plt.text(posicoes[i][0], posicoes[i][1], f'Carga {i+1}: {carga}', ha='center', va='center')