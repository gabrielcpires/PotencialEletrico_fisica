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
#Função para desenhar as linhas equipotenciais
def desenhar_linha_equipotencial(cargas, posicoes, ponto_selecionado):
    potencial_selecionado = sum(potencial_electrico(c, p, ponto_selecionado) for c, p in zip(cargas, posicoes))
    x = np.linspace(-10, 10, 100)
    y = np.linspace(-10, 10, 100)
    X, Y = np.meshgrid(x, y)
    Z = sum(potencial_electrico(c, p, (X, Y)) for c, p in zip(cargas, posicoes))
    plt.contour(X, Y, Z, levels=[potencial_selecionado], colors='green', linestyles='dashed')


def main():
    cargas = []
    posicoes = []
    quantidade_cargas = int(input("Digite a quantidade de cargas elétricas (de 1 a 4): "))

        