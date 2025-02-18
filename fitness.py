def compute_fitness(permutation, distance_matrix, flow_matrix):
    """Calcula o custo total da alocação para um indivíduo."""
    total_cost = sum(flow_matrix[permutation[i], permutation[j]] * distance_matrix[i, j]
                     for i in range(len(permutation)) for j in range(i + 1, len(permutation)))
    return total_cost
