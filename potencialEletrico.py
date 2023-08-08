import matplotlib.pyplot as plt
import numpy as np

# Constante eletrostática
K = 8.99e9

def potencial_electrico(carga, posicao, ponto):
    # Calcula a distância entre a carga e o ponto selecionado usando a fórmula da distância euclidiana
    distancia = np.sqrt((posicao[0] - ponto[0])**2 + (posicao[1] - ponto[1])**2)
    # Calcula o potencial elétrico usando a fórmula V = k * q / r
    return K * carga / distancia

def desenhar_cargas(cargas, posicoes):
    for i, carga in enumerate(cargas):
        # Desenha um ponto para cada carga na posição correspondente
        plt.scatter(posicoes[i][0], posicoes[i][1], s=100 *
                    abs(carga), c='red' if carga > 0 else 'blue')
        # Adiciona um texto próximo à carga para mostrar o valor da carga
        plt.text(posicoes[i][0], posicoes[i][1],
                 f'Carga {i+1}: {carga:.1e} C', ha='center', va='center')

def calcular_potencial_total(cargas, posicoes, ponto):
    # Calcula o potencial elétrico total somando os potenciais individuais de cada carga
    return sum(potencial_electrico(c, p, ponto) for c, p in zip(cargas, posicoes))

def criar_linha_equipotencial(cargas, posicoes, potencial, ponto_selecionado):
    # Cria uma grade de pontos para o gráfico
    x = np.linspace(-10, 10, 400)
    y = np.linspace(-10, 10, 400)
    X, Y = np.meshgrid(x, y)
    # Calcula os potenciais elétricos para cada ponto da grade
    Z = sum(potencial_electrico(c, p, (X, Y))
            for c, p in zip(cargas, posicoes))
    # Desenha as linhas equipotenciais usando contornos do potencial elétrico
    plt.contour(X, Y, Z, levels=[potencial], colors='green', linestyles='dashed')

def main():
    cargas = []
    posicoes = []
    quantidade_cargas = int(input("Digite a quantidade de cargas elétricas (de 1 a 4): "))
    
    # Coleta informações sobre cada carga e posição
    for i in range(quantidade_cargas):
        carga = float(input(f"Digite o valor da carga {i+1}: "))
        posicao_x = float(input(f"Digite a posição x da carga {i+1}: "))
        posicao_y = float(input(f"Digite a posição y da carga {i+1}: "))
        cargas.append(carga)
        posicoes.append((posicao_x, posicao_y))

    # Configuração do gráfico
    plt.figure(figsize=(8, 8))
    plt.xlabel('Eixo x')
    plt.ylabel('Eixo y')
    desenhar_cargas(cargas, posicoes)
    plt.title('Potencial Elétrico de uma Distribuição de Cargas')

    while True:
        # Captura o ponto selecionado pelo usuário no gráfico
        ponto_selecionado = plt.ginput(1, show_clicks=True)[0]
        plt.scatter(ponto_selecionado[0], ponto_selecionado[1], s=100, c='black', marker='x')

        # Calcula o potencial elétrico no ponto selecionado
        potencial_no_ponto = calcular_potencial_total(cargas, posicoes, ponto_selecionado)
        print(f'Potencial Elétrico no ponto selecionado: {potencial_no_ponto:.1e} V')

        # Cria e desenha a linha equipotencial que passa pelo ponto selecionado
        criar_linha_equipotencial(cargas, posicoes, potencial_no_ponto, ponto_selecionado)

        # Adiciona texto ao gráfico com o valor do potencial elétrico em notação científica
        plt.text(ponto_selecionado[0], ponto_selecionado[1] + 0.5, f'Potencial: {potencial_no_ponto:.1e} V', ha='center', va='center')

        plt.draw()

    plt.show()

if __name__ == '__main__':
    main()