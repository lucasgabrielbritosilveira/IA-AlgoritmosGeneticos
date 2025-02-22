import numpy as np
def elitism_simple(population, elite_rate=0.1):
    sorted_pop = sorted(population)
    elite_rate = int(len(population) * elite_rate)
    return sorted_pop[:elite_rate]

def elitism_tournament(population, elite_rate=0.1):
    # Ordena a população
    sorted_pop = sorted(population)

    # Calcula n com base na taxa de elitismo
    n = int(len(population) * elite_rate)

    # Seleciona os 2n melhores
    top_2n = sorted_pop[:2 * n]

    # Sorteia aleatoriamente n indivíduos entre os 2n melhores
    selected = np.random.choice(top_2n, n, replace=False)

    return selected
