import numpy as np

def fixed_elitism(population, fitness, elite_size=2):
    elite_indices = np.argsort(fitness)[:elite_size]
    return [population[i] for i in elite_indices]

def adaptive_elitism(population, fitness, prev_best_cost, min_elite=1, max_elite=5):
    best_cost = min(fitness)
    elite_size = max_elite if best_cost < prev_best_cost else min_elite
    elite_indices = np.argsort(fitness)[:elite_size]
    return [population[i] for i in elite_indices], best_cost
