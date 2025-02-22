import numpy as np
def elitism_simple(population, elite_rate=0.1):
    sorted_pop = sorted(population)
    elite_rate = int(len(population) * elite_rate)
    return sorted_pop[:elite_rate]

def elitism_tournament(population, elite_rate):
    elite_rate = int(len(population) * elite_rate)
    tournament = np.random.choice(population, elite_rate, replace=False)
    return tournament[:elite_rate]