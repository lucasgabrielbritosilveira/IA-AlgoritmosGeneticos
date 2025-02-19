import numpy as np
from environment import Environment
from tqdm import tqdm

# Initialize environment
dist_matrix, flow_matrix = Environment(31)

def generate_individual(size):
    """Generate a random individual (permutation) of given size."""
    return np.random.choice(range(size), replace=False, size=size)

def generate_population(population_size, individual_size):
    """Generate initial population of random individuals."""
    return np.array([generate_individual(individual_size) 
                    for _ in range(population_size)])

def calculate_fitness(individual, dist_matrix, flow_matrix):
    """Calculate fitness (cost) for a single individual."""
    fitness_sum = 0
    individual_size = len(individual)
    
    for i in range(individual_size):
        for j in range(individual_size):
            fitness_sum += (dist_matrix[i][j] * 
                          flow_matrix[individual[i]][individual[j]])
    
    return fitness_sum

def calculate_population_fitness(population, dist_matrix, flow_matrix):
    """Calculate fitness for entire population."""
    return np.array([calculate_fitness(individual, dist_matrix, flow_matrix) 
                    for individual in population])

def apply_mutation(individual, mutation_prob, population, fitness_values):
    """Apply mutation to an individual with elitism."""
    if np.random.rand() < mutation_prob:
        mutated = individual.copy()
        idx1, idx2 = np.random.choice(len(individual), replace=False, size=2)
        mutated[idx1], mutated[idx2] = mutated[idx2], mutated[idx1]
        return mutated
    else:
        best_individual, _ = get_current_best(fitness_values, population)
        return best_individual

def mutate_population(population, mutation_prob, fitness_values):
    """Apply mutation to entire population."""
    return [apply_mutation(individual, mutation_prob, population, fitness_values) 
            for individual in population]

def crossover_individuals(parent1, parent2, crossover_prob):
    """Apply crossover between two parents."""
    if np.random.rand() < crossover_prob:
        cross_point = np.random.randint(0, len(parent1))
        child1, child2 = parent1.copy(), parent2.copy()
        
        for i in range(cross_point):
            value1, value2 = child1[i], child2[i]
            child1[np.where(child1 == value2)[0]], child2[np.where(child2 == value1)[0]] = value1, value2
            child1[i], child2[i] = value2, value1
            
        return child1, child2
    else:
        return parent1, parent2

def crossover_population(population, crossover_prob):
    """Apply crossover to entire population."""
    offspring = []
    population_size = len(population)
    
    for i in range(0, population_size, 2):
        parent1 = population[np.random.randint(0, population_size)]
        parent2 = population[np.random.randint(0, population_size)]
        child1, child2 = crossover_individuals(parent1, parent2, crossover_prob)
        offspring.extend([child1, child2])
    
    return np.array(offspring)

def get_current_best(fitness_values, population):
    """Get the best individual and its fitness from current population."""
    best_idx = np.argmin(fitness_values)
    return population[best_idx], fitness_values[best_idx]

def select_population(fitness_values, population):
    """Select individuals using roulette wheel selection."""
    total_fitness = np.sum(fitness_values)
    selection_probs = fitness_values / total_fitness
    selected_indices = np.random.choice(
        range(len(population)),
        size=len(population),
        p=selection_probs
    )
    return np.take(population, selected_indices, axis=0)

def genetic_algorithm_qap(num_generations, dist_matrix, flow_matrix, 
                         crossover_prob=0.8, mutation_prob=0.2, 
                         population_size=100, individual_size=31):
    """
    Main genetic algorithm implementation for QAP.
    
    Args:
        num_generations: Number of generations to evolve
        dist_matrix: Distance matrix between locations
        flow_matrix: Flow matrix between facilities
        crossover_prob: Probability of crossover
        mutation_prob: Probability of mutation
        population_size: Size of population
        individual_size: Size of each individual
    
    Returns:
        tuple: (best_individual, best_fitness, fitness_history)
    """
    fitness_history = []

    # Initialize population
    print("\n🧬 Initializing population...")
    population = generate_population(population_size, individual_size)
    fitness_values = calculate_population_fitness(population, dist_matrix, flow_matrix)
    
    # Get initial best
    current_best, current_score = get_current_best(fitness_values, population)
    overall_best, overall_score = current_best, current_score

    # Evolution loop with progress bar
    with tqdm(total=num_generations, desc="🔄 Evolution Progress", 
             bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
        for _ in range(num_generations):
            # Selection
            population = select_population(fitness_values, population)
            
            # Crossover
            population = crossover_population(population, crossover_prob)
            
            # Calculate fitness for elitism
            fitness_values = calculate_population_fitness(population, dist_matrix, flow_matrix)
            
            # Mutation with elitism
            population = mutate_population(population, mutation_prob, fitness_values)
            
            # Update fitness values
            fitness_values = calculate_population_fitness(population, dist_matrix, flow_matrix)
            current_best, current_score = get_current_best(fitness_values, population)
            fitness_history.append(current_score)
            
            # Update best solution if improved
            if current_score < overall_score:
                overall_best, overall_score = current_best, current_score
                pbar.set_postfix({'Best Fitness': f'{overall_score:,.0f}'})
            
            pbar.update(1)

    return overall_best, overall_score, fitness_history

if __name__ == "__main__":
    print("\n🚀 Starting QAP Genetic Algorithm...")
    
    # Run genetic algorithm
    num_generations = 310
    best_solution, best_fitness, fitness_history = genetic_algorithm_qap(
        num_generations, dist_matrix, flow_matrix
    )

    # Plot results
    print("\n📊 Generating results plot...")
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(10, 6))
    plt.plot(range(num_generations), fitness_history)
    plt.xlabel('Generation')
    plt.ylabel('Fitness Value')
    plt.title('Fitness Evolution Over Generations')
    plt.grid(True)
    plt.show()

    # Print final results
    print('\n✨ Results:')
    print(f'🎯 Best Solution: {best_solution}')
    print(f'📉 Best Fitness: {best_fitness:,.0f}')