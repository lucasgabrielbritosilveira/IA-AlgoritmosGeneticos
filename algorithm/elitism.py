def fixed_elitism(population, elite_size=2):
    sorted_pop = sorted(population)
    return sorted_pop[:elite_size]

def adaptive_elitism(population, prev_best_cost, min_elite=1, max_elite=5):
    sorted_pop = sorted(population)
    best_cost = sorted_pop[0].fitness
    elite_size = max_elite if best_cost < prev_best_cost else min_elite
    return sorted_pop[:elite_size], best_cost