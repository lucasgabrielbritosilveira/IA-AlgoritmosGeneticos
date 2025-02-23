import itertools
from environment.environment import Environment
from algorithm.genetic_algorithm import GeneticAlgorithm

def run_all_combinations(n=30, pop_size=50, generations=100, mutation_rate=0.1):
    """Executa o Algoritmo Genético para todas as combinações possíveis de parâmetros."""

    # Definição das opções para cada parâmetro
    elitism_options = ["tournament", "simple"]
    selection_options = ["tournament", "roulette"]
    crossover_options = ["cx", "mpx"]
    mutation_options = ["swap", "insertion"]

    # Gera todas as combinações possíveis de parâmetros
    param_combinations = list(itertools.product(
        elitism_options, selection_options, crossover_options, mutation_options
    ))

    # Gerar uma única instância fixa do problema
    distance_matrix, flow_matrix = Environment(n)

    results = []

    # Executar todas as combinações
    for params in param_combinations:
        elitism_type, selection_type, crossover_type, mutation_type = params

        print("\n🔹 Executando com parâmetros:")
        print(f"  - Elitismo: {elitism_type}")
        print(f"  - Seleção: {selection_type}")
        print(f"  - Crossover: {crossover_type}")
        print(f"  - Mutação: {mutation_type}")

        ga = GeneticAlgorithm(
            n,
            distance_matrix,
            flow_matrix,
            pop_size=pop_size,
            generations=generations,
            mutation_rate=mutation_rate,
            elitism_type=elitism_type,
            selection_type=selection_type,
            crossover_type=crossover_type,
            mutation_type=mutation_type,
            elite_rate=0.1,
            min_elite=1,
            max_elite=5,
        )

        best_solution, best_cost, cost_history = ga.run()

        print(f"Melhor solução encontrada: {best_solution}")
        print(f"Custo da melhor solução: {best_cost}")
        print(f"Histórico de custos: {cost_history}")

        results.append((elitism_type, selection_type, crossover_type, mutation_type, best_cost))

    return results

results = run_all_combinations()

print("\nResumo de todas as execuções:")
for r in results:
    print(f"Elitismo: {r[0]}, Seleção: {r[1]}, Crossover: {r[2]}, Mutação: {r[3]}, Custo: {r[4]}")
