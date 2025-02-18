import numpy as np

def tournament_selection(population, fitness, k=3):
    selected = np.random.choice(len(population), k, replace=False)
    return population[min(selected, key=lambda i: fitness[i])]

def roulette_wheel_selection(population, fitness):
    fitness_inv = np.max(fitness) - np.array(fitness) + 1
    probabilities = fitness_inv / np.sum(fitness_inv)
    return population[np.random.choice(len(population), p=probabilities)]