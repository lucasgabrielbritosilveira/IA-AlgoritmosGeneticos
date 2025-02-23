import numpy as np

def cycle_crossover(parent1, parent2):
    size = len(parent1)
    child1 = np.full(size, -1)  # Inicializa o primeiro filho com -1
    child2 = np.full(size, -1)  # Inicializa o segundo filho com -1

    p1_copy = parent1.copy().tolist()  # Cópia do primeiro pai
    p2_copy = parent2.copy().tolist()  # Cópia do segundo pai

    # Primeiro filho
    swap = True
    count = 0
    pos = 0

    while True:
        if count > size:
            break

        # Encontra a próxima posição vazia
        for i in range(size):
            if child1[i] == -1:
                pos = i
                break

        if swap:
            # Copia do parent1
            while True:
                child1[pos] = parent1[pos]
                count += 1
                pos = parent2.tolist().index(parent1[pos])
                if p1_copy[pos] == -1:
                    swap = False
                    break
                p1_copy[pos] = -1
        else:
            # Copia do parent2
            while True:
                child1[pos] = parent2[pos]
                count += 1
                pos = parent1.tolist().index(parent2[pos])
                if p2_copy[pos] == -1:
                    swap = True
                    break
                p2_copy[pos] = -1

    # Trata quaisquer posições não preenchidas restantes
    for i in range(size):
        if child1[i] == -1:
            if p1_copy[i] == -1:
                child1[i] = parent2[i]
            else:
                child1[i] = parent1[i]

    # Segundo filho - complemento do primeiro filho
    for i in range(size):
        if child1[i] == parent1[i]:
            child2[i] = parent2[i]
        else:
            child2[i] = parent1[i]

    return child1, child2

def maximal_preservation_crossover(parent1, parent2):
    size = len(parent1)
    child1 = np.full(size, -1)  # Inicializa o primeiro filho com -1
    child2 = np.full(size, -1)  # Inicializa o segundo filho com -1

    # Primeiro filho
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    child1[start:end] = parent1[start:end]  # Copia parte do primeiro pai
    seen_elements = parent1[start:end].tolist()  # Elementos vistos do primeiro pai

    empty_positions = [i for i in range(size) if child1[i] == -1]  # Posições vazias
    k = 0
    for i in range(size):
        if parent2[i] not in seen_elements:
            child1[empty_positions[k]] = parent2[i]  # Preenche com elementos do segundo pai
            k += 1

    # Segundo filho
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    child2[start:end] = parent2[start:end]  # Copia parte do segundo pai
    seen_elements = parent2[start:end].tolist()  # Elementos vistos do segundo pai

    empty_positions = [i for i in range(size) if child2[i] == -1]  # Posições vazias
    k = 0
    for i in range(size):
        if parent1[i] not in seen_elements:
            child2[empty_positions[k]] = parent1[i]  # Preenche com elementos do primeiro pai
            k += 1

    return np.array(child1), np.array(child2)
