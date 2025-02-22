import numpy as np
from environment.utils import *
from environment.node import Node

def Environment(n = 3, grid_size=30, max_flow=2):
    distance_matrix = []
    flow_matrix =  np.zeros((n, n))

    points = []
    for i in range(n):
        x, y = generate_random_coordinates(grid_size)
        point = Node(x, y)
        points.append(point)

    for i in points:
        tmp = []
        for k in points:
            tmp.append(euclidean_heuristic(i, k))
        distance_matrix.append(tmp)

    for i in range(n):
        for j in range(i + 1, n):
            valor = random.randint(0, max_flow * n)
            flow_matrix[i][j] = valor
            flow_matrix[j][i] = valor

    return np.array(distance_matrix), np.array(flow_matrix)
