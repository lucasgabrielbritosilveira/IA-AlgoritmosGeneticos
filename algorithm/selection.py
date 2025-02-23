import numpy as np

def tournament_selection(population, k=3):
    # Seleciona aleatoriamente k indivíduos da população
    tournament = np.random.choice(population, k, replace=False)
    return min(tournament)  # Retorna o melhor indivíduo do torneio

def roulette_wheel_selection(population):
    fitness_values = np.array([ind.fitness for ind in population])

    max_fitness = np.max(fitness_values)
    adjusted_fitness = max_fitness - fitness_values + 1  # +1 para evitar zeros

    # Normaliza as probabilidades
    total_fitness = np.sum(adjusted_fitness)
    probabilities = adjusted_fitness / total_fitness

    return np.random.choice(population, p=probabilities)  # Retorna um indivíduo com base nas probabilidades
