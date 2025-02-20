import numpy as np
from environment import Environment
from tqdm import tqdm

# Initialize environment
dist_matrix, flow_matrix = Environment(31)

class Individual:
    """Represents a single solution in the population."""
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None

    def calculate_fitness(self, dist_matrix, flow_matrix):
        """Calculate fitness (cost) for this individual."""
        if self.fitness is None:
            self.fitness = 0
            size = len(self.chromosome)
            for i in range(size):
                for j in range(size):
                    self.fitness += (dist_matrix[i][j] * flow_matrix[self.chromosome[i]][self.chromosome[j]])
        return self.fitness

def get_fitness(individual):
    """Helper function to get individual's fitness."""
    return individual.fitness

class GeneticAlgorithm:
    def __init__(self, 
                 population_size=100,
                 elite_size=2,
                 tournament_size=5,
                 crossover_rate=0.8,
                 mutation_rate=0.2,
                 selection_method="tournament",
                 crossover_method="ox",
                 elitism_method="fixed",
                 mutation_method="swap"):
        self.population_size = population_size
        self.elite_size = elite_size
        self.tournament_size = tournament_size
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.selection_method = selection_method
        self.crossover_method = crossover_method
        self.elitism_method = elitism_method
        self.mutation_method = mutation_method

    def initialize_population(self, chromosome_size):
        """Generate initial population with random permutations."""
        population = []
        for _ in range(self.population_size):
            chromosome = np.random.permutation(chromosome_size)
            population.append(Individual(chromosome))
        return population

    # FASE 1: Elitismo
    def fixed_elitism(self, population):
        """Fixed number of elite individuals."""
        elite = []
        sorted_pop = sorted(population, key=get_fitness)
        for i in range(self.elite_size):
            elite.append(Individual(sorted_pop[i].chromosome.copy()))
        return elite

    def adaptive_elitism(self, population, prev_best_fitness):
        """Adaptive elitism based on improvement."""
        elite = []
        sorted_pop = sorted(population, key=get_fitness)
        current_best_fitness = sorted_pop[0].fitness
        
        # If improvement, reduce elite size, else increase it
        if current_best_fitness < prev_best_fitness:
            elite_size = max(1, self.elite_size - 1)
        else:
            elite_size = min(len(population) // 10, self.elite_size + 1)
        
        for i in range(elite_size):
            elite.append(Individual(sorted_pop[i].chromosome.copy()))
        return elite, current_best_fitness

    def apply_elitism(self, population, prev_best_fitness=float('inf')):
        """Apply selected elitism method."""
        if self.elitism_method == "fixed":
            return self.fixed_elitism(population), prev_best_fitness
        else:  # adaptive
            return self.adaptive_elitism(population, prev_best_fitness)

    # FASE 2: Seleção
    def tournament_selection(self, population, num_select):
        """Tournament selection."""
        selected = []
        while len(selected) < num_select:
            tournament = np.random.choice(population, self.tournament_size, replace=False)
            winner = min(tournament, key=get_fitness)
            selected.append(Individual(winner.chromosome.copy()))
        return selected

    def roulette_selection(self, population, num_select):
        """Roulette wheel selection."""
        selected = []
        fitness_values = np.array([ind.fitness for ind in population])
        
        # Para problemas de minimização, invertemos o fitness
        # e adicionamos o máximo para evitar valores negativos
        max_fitness = np.max(fitness_values)
        adjusted_fitness = max_fitness - fitness_values + 1  # +1 para evitar zeros
        
        # Normaliza as probabilidades
        total_fitness = np.sum(adjusted_fitness)
        probabilities = adjusted_fitness / total_fitness
        
        # Seleciona indivíduos
        indices = np.random.choice(
            len(population), 
            size=num_select, 
            p=probabilities,
            replace=True
        )
        
        for idx in indices:
            selected.append(Individual(population[idx].chromosome.copy()))
            
        return selected
    
    # TALVEZ SUBSTITUIR UMA SELECTION POR SELECAO JUSTA.

    def select_parents(self, population, num_select):
        """Apply selected selection method."""
        if self.selection_method == "tournament":
            return self.tournament_selection(population, num_select)
        else:  # roulette
            return self.roulette_selection(population, num_select)

    # FASE 3: Reprodução
    def order_crossover(self, parent1, parent2):
        """Order Crossover (OX)."""
        if np.random.random() > self.crossover_rate:
            return Individual(parent1.chromosome.copy())
            
        size = len(parent1.chromosome)
        start, end = sorted(np.random.choice(size, 2, replace=False))
        
        child = np.full(size, -1)
        child[start:end] = parent1.chromosome[start:end]
        remaining = [gene for gene in parent2.chromosome if gene not in child[start:end]]
        
        j = 0
        for i in range(size):
            if child[i] == -1:
                child[i] = remaining[j]
                j += 1
                
        return Individual(child)

    def pmx_crossover(self, parent1, parent2):
        """Partially Mapped Crossover (PMX)."""
        if np.random.random() > self.crossover_rate:
            return Individual(parent1.chromosome.copy())
        
        size = len(parent1.chromosome)
        point1, point2 = sorted(np.random.choice(size, 2, replace=False))
        
        # Initialize offspring with parent2's values
        offspring = parent2.chromosome.copy()
        
        # Copy segment from parent1
        segment = parent1.chromosome[point1:point2]
        offspring[point1:point2] = segment
        
        # Create mapping between segments
        p1_segment = parent1.chromosome[point1:point2]
        p2_segment = parent2.chromosome[point1:point2]
        segment_mapping = dict(zip(p2_segment, p1_segment))
        
        # Adjust remaining positions
        for i in range(size):
            if i < point1 or i >= point2:  # Outside the copied segment
                current = offspring[i]
                while current in segment:  # Need to map this value
                    current = segment_mapping[current]
                offspring[i] = current
        
        return Individual(offspring)

    def reproduce(self, parents):
        """Apply selected crossover method."""
        offspring = []
        while len(offspring) < len(parents):
            parent1, parent2 = np.random.choice(parents, 2, replace=False)
            if self.crossover_method == "ox":
                child = self.order_crossover(parent1, parent2)
            else:  # pmx
                child = self.pmx_crossover(parent1, parent2)
            offspring.append(child)
        return offspring

    # FASE 4: Mutação
    def swap_mutation(self, individual):
        """Swap Mutation."""
        if np.random.random() < self.mutation_rate:
            idx1, idx2 = np.random.choice(len(individual.chromosome), 2, replace=False)
            individual.chromosome[idx1], individual.chromosome[idx2] = \
                individual.chromosome[idx2], individual.chromosome[idx1]
            individual.fitness = None

    def inversion_mutation(self, individual):
        """Inversion Mutation."""
        if np.random.random() < self.mutation_rate:
            start, end = sorted(np.random.choice(len(individual.chromosome), 2, replace=False))
            individual.chromosome[start:end] = individual.chromosome[start:end][::-1]
            individual.fitness = None

    def mutate(self, population, start_from=0):
        """Apply selected mutation method."""
        for ind in population[start_from:]:
            if self.mutation_method == "swap":
                self.swap_mutation(ind)
            else:  # inversion
                self.inversion_mutation(ind)

    def run(self, num_generations, dist_matrix, flow_matrix):
        """Execute the genetic algorithm."""
        print("\n🧬 Inicializando população...")
        population = self.initialize_population(len(dist_matrix))
        
        for ind in population:
            ind.calculate_fitness(dist_matrix, flow_matrix)
        
        best_fitness = float('inf')
        best_solution = None
        fitness_history = []
        prev_best_fitness = float('inf')

        with tqdm(total=num_generations, desc="🔄 Progresso da Evolução", 
                 bar_format='{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]') as pbar:
            for _ in range(num_generations):
                # FASE 1: Elitismo
                new_population, prev_best_fitness = self.apply_elitism(population, prev_best_fitness)
                
                # FASE 2: Seleção
                selected_parents = self.select_parents(
                    population, 
                    self.population_size - len(new_population)
                )
                
                # FASE 3: Reprodução
                offspring = self.reproduce(selected_parents)
                new_population.extend(offspring)
                
                # FASE 4: Mutação
                self.mutate(new_population, start_from=len(new_population)-len(offspring))
                
                population = new_population
                
                for ind in population:
                    ind.calculate_fitness(dist_matrix, flow_matrix)
                
                current_best = min(population, key=get_fitness)
                if current_best.fitness < best_fitness:
                    best_fitness = current_best.fitness
                    best_solution = current_best.chromosome.copy()
                    pbar.set_postfix({'Melhor Fitness': f'{best_fitness:,.0f}'})
                
                fitness_history.append(best_fitness)
                pbar.update(1)

        return best_solution, best_fitness, fitness_history

if __name__ == "__main__":
    print("\n🚀 Iniciando Algoritmo Genético para QAP...")
    
    # Initialize and run GA with different configurations
    configurations = [
        {"selection": "tournament", "crossover": "ox", "elitism": "fixed", "mutation": "swap"},
        # {"selection": "roulette", "crossover": "pmx", "elitism": "adaptive", "mutation": "inversion"}
    ]
    
    results = []
    for config in configurations:
        print(f"\n🔄 Executando configuração: {config}")
        ga = GeneticAlgorithm(
            population_size=100,
            elite_size=2,
            tournament_size=5,
            crossover_rate=0.8,
            mutation_rate=0.2,
            selection_method=config["selection"],
            crossover_method=config["crossover"],
            elitism_method=config["elitism"],
            mutation_method=config["mutation"]
        )
        
        best_solution, best_fitness, fitness_history = ga.run(310, dist_matrix, flow_matrix)
        results.append((config, best_fitness, fitness_history))
        
        print(f'✨ Resultados para configuração {config}:')
        print(f'🎯 Melhor Solução: {best_solution}')
        print(f'📉 Melhor Fitness: {best_fitness:,.0f}')

    # Plot comparison
    print("\n📊 Gerando gráfico comparativo...")
    import matplotlib.pyplot as plt
    
    plt.figure(figsize=(12, 6))
    for config, _, history in results:
        label = f"{config['selection']}-{config['crossover']}-{config['elitism']}-{config['mutation']}"
        plt.plot(range(310), history, label=label)
    
    plt.xlabel('Geração')
    plt.ylabel('Valor de Fitness')
    plt.title('Comparação das Configurações do AG')
    plt.legend()
    plt.grid(True)
    plt.show()