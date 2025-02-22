import numpy as np

def swap_mutation(individual, mutation_rate=0.1):
    new_individual = individual.copy()

    if np.random.rand() < mutation_rate:
        idx1, idx2 = np.random.choice(len(new_individual), 2, replace=False)
        new_individual[idx1], new_individual[idx2] = new_individual[idx2], new_individual[idx1]
    return new_individual

def insertion_mutation(individual, mutation_rate=0.1):
    new_individual = individual.copy()

    if np.random.rand() < mutation_rate:
        size = len(individual)

        point = np.random.randint(0, size)

        remaining = individual.tolist()
        selected_value = remaining.pop(point)

        insert_position = np.random.randint(0, size)

        new_individual = np.array(
            remaining[:insert_position] +
            [selected_value] +
            remaining[insert_position:]
        )

    return new_individual
