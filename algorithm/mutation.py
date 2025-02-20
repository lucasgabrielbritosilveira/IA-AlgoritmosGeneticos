import numpy as np

def swap_mutation(individual, mutation_rate=0.1):
    if np.random.rand() < mutation_rate:
        idx1, idx2 = np.random.choice(len(individual), 2, replace=False)
        individual[idx1], individual[idx2] = individual[idx2], individual[idx1]
    return individual

def inversion_mutation(individual, mutation_rate=0.1):
    if np.random.rand() < mutation_rate:
        start, end = sorted(np.random.choice(len(individual), 2, replace=False))
        individual[start:end+1] = individual[start:end+1][::-1]
    return individual
