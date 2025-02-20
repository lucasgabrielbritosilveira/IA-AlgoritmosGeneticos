import numpy as np

def order_crossover(parent1, parent2):
    size, child = len(parent1), [-1] * len(parent1)
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    child[start:end+1] = parent1[start:end+1]
    for i, gene in enumerate(parent2):
        if gene not in child:
            child[child.index(-1)] = gene
    return np.array(child)

def pmx_crossover(parent1, parent2):
    """Crossover parcialmente mapeado (PMX) corrigido para evitar indivíduos inválidos."""
    size = len(parent1)
    child = np.full(size, -1)

    # Escolher dois pontos de corte
    start, end = sorted(np.random.choice(range(size), 2, replace=False))

    # Copiar segmento do primeiro pai
    child[start:end+1] = parent1[start:end+1]

    # Criar mapeamento entre os genes cortados dos pais
    mapping = {parent1[i]: parent2[i] for i in range(start, end+1)}

    # Preencher o restante garantindo consistência
    for i in range(size):
        if child[i] == -1:  # Espaço vazio
            value = parent2[i]
            while value in child:
                value = mapping.get(value, value)  # Substituir conforme o mapeamento
            child[i] = value

    return np.array(child)
