import numpy as np
import itertools
from algorithm import genetic_algorithm

# ----------------------- GERAR INSTÂNCIA DO PROBLEMA -----------------------
def generate_pqa_instance(n, grid_size=30, max_flow=2):
    """Gera uma instância do Problema Quadrático de Alocação (PQA) de tamanho n."""

    locations = np.random.randint(0, grid_size + 1, size=(n, 2))

    distance_matrix = np.zeros((n, n), dtype=int)
    for i in range(n):
        for j in range(i + 1, n):
            distance = np.sqrt((locations[i, 0] - locations[j, 0]) ** 2 +
                               (locations[i, 1] - locations[j, 1]) ** 2)
            distance_matrix[i, j] = distance_matrix[j, i] = int(np.floor(distance))

    flow_matrix = np.random.randint(0, max_flow * n + 1, size=(n, n))
    np.fill_diagonal(flow_matrix, 0)
    flow_matrix = (flow_matrix + flow_matrix.T) // 2  # Garantir simetria
    
    return distance_matrix, flow_matrix

def run_all_combinations(n=31, pop_size=50, generations=100, mutation_rate=0.1):
    """Executa o Algoritmo Genético para todas as combinações possíveis de parâmetros."""

    # Definição das opções para cada parâmetro
    elitism_options = ["fixed", "adaptive"]
    selection_options = ["tournament", "roulette"]
    crossover_options = ["ox", "pmx"]
    mutation_options = ["swap", "inversion"]

    # Gera todas as combinações possíveis de parâmetros
    param_combinations = list(itertools.product(
        elitism_options, selection_options, crossover_options, mutation_options
    ))

    # Gerar uma única instância fixa do problema para comparações justas
    distance_matrix, flow_matrix = generate_pqa_instance(n)

    results = []  # Lista para armazenar os resultados

    # Executar todas as combinações
    for params in param_combinations:
        elitism_type, selection_type, crossover_type, mutation_type = params

        print("\n🔹 Executando com parâmetros:")
        print(f"  - Elitismo: {elitism_type}")
        print(f"  - Seleção: {selection_type}")
        print(f"  - Crossover: {crossover_type}")
        print(f"  - Mutação: {mutation_type}")

        best_solution, best_cost = genetic_algorithm(
            n,
            distance_matrix,
            flow_matrix,
            pop_size,
            generations,
            mutation_rate,
            elitism_type=elitism_type,
            selection_type=selection_type,
            crossover_type=crossover_type,
            mutation_type=mutation_type
        )

        print(f"  ✅ Melhor solução encontrada: {best_solution}")
        print(f"  💰 Custo da melhor solução: {best_cost}")

        results.append((elitism_type, selection_type, crossover_type, mutation_type, best_cost))

    return results
