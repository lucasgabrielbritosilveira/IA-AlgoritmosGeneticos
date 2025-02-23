import numpy as np
from environment.utils import *
from environment.node import Node

def Environment(n=3, grid_size=30, max_flow=2):
    # Inicializa a matriz de distâncias e a matriz de fluxo
    distance_matrix = []
    flow_matrix = np.zeros((n, n))

    points = []
    # Gera n nós com coordenadas aleatórias
    for i in range(n):
        x, y = generate_random_coordinates(grid_size)
        point = Node(x, y)
        points.append(point)

    # Calcula a matriz de distâncias entre os nós
    for i in points:
        tmp = []
        for k in points:
            tmp.append(euclidean_heuristic(i, k))  # Calcula a distância euclidiana
        distance_matrix.append(tmp)

    # Gera a matriz de fluxo com valores aleatórios
    for i in range(n):
        for j in range(i + 1, n):
            valor = random.randint(0, max_flow * n)  # Gera um valor aleatório para o fluxo
            flow_matrix[i][j] = valor
            flow_matrix[j][i] = valor  # A matriz é simétrica

    return np.array(distance_matrix), np.array(flow_matrix)  # Retorna as matrizes como arrays numpy
