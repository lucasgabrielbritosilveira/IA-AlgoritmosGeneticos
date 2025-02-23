import time
from algorithm.genetic_algorithm import GeneticAlgorithm
from environment.environment import Environment

def run_experiment(configurations, pop_size=100, generations=100, elite_rate=0.2, 
                  mutation_rate=0.1, n=10, repeat=20, parameter_to_display=None):

    results = []

    for i in range(repeat):
        distance_matrix, flow_matrix = Environment(n)

        for configuration in configurations:
            param_value = configuration[parameter_to_display] if parameter_to_display else None

            print(f"Executando GA com parâmetros - Iteração {i + 1}:")
            print(f"\n🧬 Executando configuração: {configuration}")
            if param_value:
                print(f"  - {parameter_to_display.capitalize()}: {param_value}")
            print(f"  - N: {n}")
            print(f"  - Tamanho da População: {pop_size}")
            print(f"  - Número de Gerações: {generations}")
            print(f"  - Elitismo (tamanho fixo): {elite_rate}")
            print(f"  - Taxa de Mutação: {mutation_rate}")
            print("Inovando e pensando fora da caixinha para obter resultados de alta performance...\n")

            ga = GeneticAlgorithm(
                n=n,
                distance_matrix=distance_matrix,
                flow_matrix=flow_matrix,
                pop_size=pop_size,
                generations=generations,
                mutation_rate=mutation_rate,
                elitism_type=configuration['elitism'],
                selection_type=configuration['selection'],
                crossover_type=configuration['crossover'],
                mutation_type=configuration['mutation'],
                elite_rate=elite_rate,
                min_elite=1,
                max_elite=5
            )

            start_time = time.time()
            best_chromosome, best_fitness, cost_history = ga.run(show_progress=True)
            end_time = time.time()
            exec_time = end_time - start_time

            best_gen = cost_history.index(min(cost_history))

            results.append({
              "n": n,
              "pop_size": pop_size,
              "geracoes": generations,
              "elite_rate": elite_rate,
              "mutation_rate": mutation_rate,
              "melhor_solucao": str(best_chromosome).replace('\n', ''),
              "melhor_custo": best_fitness,
              "tempo_execucao_s": exec_time,
              "geracao_melhor_custo": best_gen,
              "configuracao": configuration,
              "elitism": configuration["elitism"],
              "selection": configuration["selection"],
              "crossover": configuration["crossover"],
              "mutation": configuration["mutation"]
            })

    return results
