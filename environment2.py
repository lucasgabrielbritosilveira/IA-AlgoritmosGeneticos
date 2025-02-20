import numpy as np
from utils import *

def generate_pqa_instance(n, grid_size=30, max_flow=2):
    """Gera uma instância do Problema Quadrático de Alocação (PQA) de tamanho n."""

    locations = np.random.randint(0, grid_size + 1, size=(n, 2))

    distance_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            distance = np.sqrt((locations[i, 0] - locations[j, 0]) ** 2 +
                               (locations[i, 1] - locations[j, 1]) ** 2)
            distance_matrix[i, j] = distance_matrix[j, i] = int(np.floor(distance))

    flow_matrix = np.random.randint(0, max_flow * n + 1, size=(n, n))
    np.fill_diagonal(flow_matrix, 0)
    flow_matrix = (flow_matrix + flow_matrix.T) // 2  # Garantir simetria
    
    return distance_matrix, flow_matrix

print(
    generate_pqa_instance(3)
)