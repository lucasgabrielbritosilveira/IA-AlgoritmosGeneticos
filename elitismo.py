def fixed_elitism(population, elite_size=2):
    population.sort()
    return population[:elite_size]

def adaptive_elitism(population, prev_best_cost, min_elite=1, max_elite=5):
    population.sort()
    best_cost = population[0].fitness
    elite_size = max_elite if best_cost < prev_best_cost else min_elite
    return population[:elite_size], best_cost