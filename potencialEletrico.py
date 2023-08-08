import matplotlib.pyplot as plt
import numpy as np

# Constante eletrostática
K = 8.99e9

def potencial_electrico(carga, posicao, ponto):
    distancia = np.sqrt((posicao[0] - ponto[0])**2 + (posicao[1] - ponto[1])**2)
    return K * carga / distancia

def desenhar_cargas(cargas, posicoes):
    for i, carga in enumerate(cargas):
        plt.scatter(posicoes[i][0], posicoes[i][1], s=100 *
                    abs(carga), c='red' if carga > 0 else 'blue')
        plt.text(posicoes[i][0], posicoes[i][1],
                 f'Carga {i+1}: {carga}', ha='center', va='center')

def calcular_potencial_total(cargas, posicoes, ponto):
    return sum(potencial_electrico(c, p, ponto) for c, p in zip(cargas, posicoes))

def criar_linha_equipotencial(cargas, posicoes, potencial, ponto_selecionado):
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    Z = sum(potencial_electrico(c, p, (X, Y))
            for c, p in zip(cargas, posicoes))
    plt.contour(X, Y, Z, levels=[potencial], colors='green', linestyles='dashed')

def main():
    cargas = []
    posicoes = []
    quantidade_cargas = int(input("Digite a quantidade de cargas elétricas (de 1 a 4): "))
    
    for i in range(quantidade_cargas):
        carga = float(input(f"Digite o valor da carga {i+1}: "))
        posicao_x = float(input(f"Digite a posição x da carga {i+1}: "))
        posicao_y = float(input(f"Digite a posição y da carga {i+1}: "))
        cargas.append(carga)
        posicoes.append((posicao_x, posicao_y))

    plt.figure(figsize=(8, 8))
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    desenhar_cargas(cargas, posicoes)
    plt.title('Potencial Elétrico de uma Distribuição de Cargas')

    while True:
        ponto_selecionado = plt.ginput(1, show_clicks=True)[0]
        plt.scatter(ponto_selecionado[0], ponto_selecionado[1], s=100, c='black', marker='x')

        potencial_no_ponto = calcular_potencial_total(cargas, posicoes, ponto_selecionado)
        print(f'Potencial Elétrico no ponto selecionado: {potencial_no_ponto:.2f} V')

        criar_linha_equipotencial(cargas, posicoes, potencial_no_ponto, ponto_selecionado)
        plt.draw()

    plt.show()

if __name__ == '__main__':
    main()
