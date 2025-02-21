import numpy as np
from tqdm import tqdm
from algorithm.selection import tournament_selection, roulette_wheel_selection
from algorithm.crossover import order_crossover, pmx_crossover
from algorithm.mutation import inversion_mutation, swap_mutation
from algorithm.elitism import adaptive_elitism, elitism_rate
from algorithm.individual import Individual

# TODO: evaluate and maybe change the crossovers, elitims, mutations and selections
class GeneticAlgorithm:
    def __init__(
        self,
        n,
        distance_matrix,
        flow_matrix,
        pop_size=50,
        generations=100,
        mutation_rate=0.1,
        elitism_type="percent",
        selection_type="tournament",
        crossover_type="ox",
        mutation_type="swap",
        elite_rate=0.1,
        min_elite=1,
        max_elite=5,
    ):
        self.n = n
        self.distance_matrix = distance_matrix
        self.flow_matrix = flow_matrix
        self.pop_size = pop_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.elitism_type = elitism_type
        self.selection_type = selection_type
        self.crossover_type = crossover_type
        self.mutation_type = mutation_type
        self.elite_rate = elite_rate
        self.min_elite = min_elite
        self.max_elite = max_elite

    def initialize_population(self):
        """Gera uma população inicial diversa de indivíduos."""
        chromosomes = [np.random.permutation(self.n) for _ in range(self.pop_size)]
        np.random.shuffle(chromosomes)  # Misturar para mais diversidade
        return [Individual(chromosome) for chromosome in chromosomes]

    def run(self, show_progress=True):
        # Initialize population
        population = self.initialize_population()
        cost_history = []

        # Calculate initial fitness
        for individual in population:
            individual.calculate_fitness(self.distance_matrix, self.flow_matrix)

        prev_best_cost = min(population).fitness

        # Criar barra de progresso
        pbar = tqdm(range(self.generations), disable=not show_progress, desc="🔄 Progresso da Evolução", unit="gen")

        for _ in pbar:
            new_population = []

            # Handle elitism
            if self.elitism_type == "percent":
                elites = elitism_rate(population, self.elite_rate)
            elif self.elitism_type == "adaptive":
                elites, prev_best_cost = adaptive_elitism(population, prev_best_cost, self.min_elite, self.max_elite)
            else:
                raise ValueError("Elitismo inválido. Use 'percent' ou 'adaptive'.")

            new_population.extend(elites)

            # Generate new individuals
            while len(new_population) < self.pop_size:
                if self.selection_type == "tournament":
                    parent1 = tournament_selection(population)
                    parent2 = tournament_selection(population)
                elif self.selection_type == "roulette":
                    parent1 = roulette_wheel_selection(population)
                    parent2 = roulette_wheel_selection(population)
                else:
                    raise ValueError("Seleção inválida. Use 'tournament' ou 'roulette'.")

                # Apply crossover
                if self.crossover_type == "ox":
                    child_chromosome = order_crossover(parent1.chromosome, parent2.chromosome)
                elif self.crossover_type == "pmx":
                    child_chromosome = pmx_crossover(parent1.chromosome, parent2.chromosome)
                else:
                    raise ValueError("Crossover inválido. Use 'ox' ou 'pmx'.")

                # Create new individual
                child = Individual(child_chromosome)

                # Apply mutation
                if self.mutation_type == "swap":
                    child.chromosome = swap_mutation(child.chromosome, self.mutation_rate)
                elif self.mutation_type == "inversion":
                    child.chromosome = inversion_mutation(child.chromosome, self.mutation_rate)
                else:
                    raise ValueError("Mutação inválida. Use 'swap' ou 'inversion'.")

                # Calculate fitness for new individual
                child.calculate_fitness(self.distance_matrix, self.flow_matrix)
                new_population.append(child)

            population = new_population

            # Update progress bar with current best fitness
            best_fitness = min(population).fitness
            pbar.set_postfix({'Melhor custo': best_fitness})

            cost_history.append(best_fitness)

        pbar.close()

        best_solution = min(population)
        formatted_cost_history = [int(cost) for cost in cost_history]

        return best_solution.chromosome, best_solution.fitness, formatted_cost_history
