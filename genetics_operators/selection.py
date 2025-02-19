import numpy as np


def tournament(population, fitness, k=3):
    selected = np.random.choice(range(len(population)), k, replace=False)
    selected.sort()
    return selected[0]


def roulette_wheel(population, fitness):
    fitness_inv = np.max(fitness) - np.array(fitness) + 1
    probabilities = fitness_inv / np.sum(fitness_inv)
    return population[np.random.choice(len(population), p=probabilities)]


def compute(type, population, fitness, k=3):
    if type == "tournament":
        return tournament(population, fitness, k)

    if type == "roulette_wheel":
        return roulette_wheel(population, fitness)
