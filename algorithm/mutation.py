import numpy as np

def swap_mutation(individual, mutation_rate=0.1):
    new_individual = individual.copy()

    if np.random.rand() < mutation_rate:
        idx1, idx2 = np.random.choice(len(new_individual), 2, replace=False)
        new_individual[idx1], new_individual[idx2] = new_individual[idx2], new_individual[idx1]
    return new_individual

def inversion_mutation(individual, mutation_rate=0.1):
    new_individual = individual.copy()

    if np.random.rand() < mutation_rate:
        start, end = sorted(np.random.choice(len(new_individual), 2, replace=False))
        new_individual[start:end+1] = new_individual[start:end+1][::-1]
    return new_individual
