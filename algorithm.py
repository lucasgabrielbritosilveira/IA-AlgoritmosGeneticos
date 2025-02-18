import numpy as np
from emparelhamento import tournament_selection, roulette_wheel_selection
from crossover import order_crossover, pmx_crossover
from mutacao import inversion_mutation, swap_mutation
from elitismo import adaptive_elitism, fixed_elitism
from fitness import compute_fitness

# ----------------------- INICIALIZAR POPULAÇÃO -----------------------
# def initialize_population(pop_size, n):
#     """Gera uma população inicial de indivíduos (permutações aleatórias)."""
#     return [np.random.permutation(n) for _ in range(pop_size)]

def initialize_population(pop_size, n):
    """Gera uma população inicial diversa de indivíduos (permutações aleatórias)."""
    population = [np.random.permutation(n) for _ in range(pop_size)]
    np.random.shuffle(population)  # Misturar para mais diversidade
    return population

# ----------------------- ALGORITMO GENÉTICO -----------------------
def genetic_algorithm(
    n, distance_matrix, flow_matrix, pop_size=50, generations=100, 
    mutation_rate=0.1, elitism_type="fixed", selection_type="tournament", 
    crossover_type="ox", mutation_type="swap", elite_size=2, min_elite=1, max_elite=5):

    population = initialize_population(pop_size, n)
    fitness = [compute_fitness(ind, distance_matrix, flow_matrix) for ind in population]
    prev_best_cost = min(fitness)

    for gen in range(generations):
        new_population = []

        if elitism_type == "fixed":
            elites = fixed_elitism(population, fitness, elite_size)
        elif elitism_type == "adaptive":
            elites, prev_best_cost = adaptive_elitism(population, fitness, prev_best_cost, min_elite, max_elite)
        else:
            raise ValueError("Elitismo inválido. Use 'fixed' ou 'adaptive'.")
        
        new_population.extend(elites)

        while len(new_population) < pop_size:
            if selection_type == "tournament":
                parent1 = tournament_selection(population, fitness)
                parent2 = tournament_selection(population, fitness)
            elif selection_type == "roulette":
                parent1 = roulette_wheel_selection(population, fitness)
                parent2 = roulette_wheel_selection(population, fitness)
            else:
                raise ValueError("Seleção inválida. Use 'tournament' ou 'roulette'.")

            if crossover_type == "ox":
                child = order_crossover(parent1, parent2)
            elif crossover_type == "pmx":
                child = pmx_crossover(parent1, parent2)
            else:
                raise ValueError("Crossover inválido. Use 'ox' ou 'pmx'.")

            if mutation_type == "swap":
                child = swap_mutation(child, mutation_rate)
            elif mutation_type == "inversion":
                child = inversion_mutation(child, mutation_rate)
            else:
                raise ValueError("Mutação inválida. Use 'swap' ou 'inversion'.")

            new_population.append(child)

        population = new_population
        fitness = [compute_fitness(ind, distance_matrix, flow_matrix) for ind in population]

        if gen % 10 == 0:
            print(f"Geração {gen}: Melhor Custo = {min(fitness)}")

    best_idx = np.argmin(fitness)
    return population[best_idx], fitness[best_idx]
