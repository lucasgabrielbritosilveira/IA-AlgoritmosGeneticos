import numpy as np
from tqdm import tqdm
from emparelhamento import tournament_selection, roulette_wheel_selection
from crossover import order_crossover, pmx_crossover
from mutacao import inversion_mutation, swap_mutation
from elitismo import adaptive_elitism, fixed_elitism
from individuo import Individual

def initialize_population(pop_size, n):
    """Gera uma população inicial diversa de indivíduos."""
    chromosomes = [np.random.permutation(n) for _ in range(pop_size)]
    np.random.shuffle(chromosomes)  # Misturar para mais diversidade

    return [Individual(chromosome) for chromosome in chromosomes]

# ----------------------- ALGORITMO GENÉTICO -----------------------
def genetic_algorithm(
    n,
    distance_matrix,
    flow_matrix,
    pop_size=50,
    generations=100,
    mutation_rate=0.1,
    elitism_type="fixed",
    selection_type="tournament",
    crossover_type="ox",
    mutation_type="swap",
    elite_size=2,
    min_elite=1,
    max_elite=5,
    show_progress=True
):
    # Initialize population
    population = initialize_population(pop_size, n)

    # Calculate initial fitness
    for individual in population:
        individual.calculate_fitness(distance_matrix, flow_matrix) # TODO: ver se esse cálculo está correto

    prev_best_cost = min(population).fitness

    # Criar barra de progresso
    pbar = tqdm(range(generations), disable=not show_progress, desc="🔄 Progresso da Evolução", unit="gen")

    for gen in pbar:
        new_population = []

        # Handle elitism
        if elitism_type == "fixed":
            elites = fixed_elitism(population, elite_size)
        elif elitism_type == "adaptive":
            elites, prev_best_cost = adaptive_elitism(population, prev_best_cost, min_elite, max_elite)
        else:
            raise ValueError("Elitismo inválido. Use 'fixed' ou 'adaptive'.")

        new_population.extend(elites)

        # Generate new individuals
        while len(new_population) < pop_size:
            if selection_type == "tournament":
                parent1 = tournament_selection(population)
                parent2 = tournament_selection(population)
            elif selection_type == "roulette":
                parent1 = roulette_wheel_selection(population)
                parent2 = roulette_wheel_selection(population)
            else:
                raise ValueError("Seleção inválida. Use 'tournament' ou 'roulette'.")

            # Apply crossover
            if crossover_type == "ox":
                child_chromosome = order_crossover(parent1.chromosome, parent2.chromosome)
            elif crossover_type == "pmx":
                child_chromosome = pmx_crossover(parent1.chromosome, parent2.chromosome)
            else:
                raise ValueError("Crossover inválido. Use 'ox' ou 'pmx'.")

            # Create new individual
            child = Individual(child_chromosome)

            # Apply mutation
            if mutation_type == "swap":
                child.chromosome = swap_mutation(child.chromosome, mutation_rate)
            elif mutation_type == "inversion":
                child.chromosome = inversion_mutation(child.chromosome, mutation_rate)
            else:
                raise ValueError("Mutação inválida. Use 'swap' ou 'inversion'.")

            # Calculate fitness for new individual
            child.calculate_fitness(distance_matrix, flow_matrix)
            new_population.append(child)

        population = new_population.copy()

        # Update progress bar with current best fitness
        best_fitness = min(population).fitness
        pbar.set_postfix({'Melhor custo': best_fitness})

    pbar.close()

    # TODO: Create shallow copy of population before do some actions

    cost_history = [int(individual.fitness) for individual in population]

    best_solution = min(population)

    return best_solution.chromosome, best_solution.fitness, cost_history
