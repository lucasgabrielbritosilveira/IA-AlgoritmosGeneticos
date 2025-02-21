import numpy as np
def elitism_simple(population, elite_rate=0.1):
    sorted_pop = sorted(population)
    elite_size = int(len(population) * elite_rate)
    return sorted_pop[:elite_size]

def elitism_tournament(population, elite_rate):
    elite_size = int(len(population) * elite_rate)
    tournament = np.random.choice(population, elite_size, replace=False)
    return tournament[:elite_size]