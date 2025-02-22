import itertools
import time
import pandas as pd
import os
from algorithm.genetic_algorithm import GeneticAlgorithm
from environment.environment import Environment


def testar_parametros(n, distance_matrix, flow_matrix, output_csv="resultados_ga.csv"):
    # Garante que a pasta 'results' existe no mesmo nível de 'experiments'
    results_dir = os.path.join(os.path.dirname(__file__), '..', 'results')
    os.makedirs(results_dir, exist_ok=True)

    output_path = os.path.join(results_dir, output_csv)

    # Parâmetros a serem testados
    lista_pop_sizes = [50, 100, 150]
    lista_geracoes = [50, 100, 200]
    lista_elite_rates = [1, 2, 4]
    lista_mutation_rates = [0.05, 0.1, 0.15]

    # Gera todas as combinações possíveis
    combinacoes = itertools.product(
        lista_pop_sizes,
        lista_geracoes,
        lista_elite_rates,
        lista_mutation_rates
    )

    resultados = []

    for pop_size, geracoes, elite_rate, mutation_rate in combinacoes:
        print("Executando GA com parâmetros:")
        print(f"  - Tamanho da População: {pop_size}")
        print(f"  - Número de Gerações: {geracoes}")
        print(f"  - Elitismo (tamanho fixo): {elite_rate}")
        print(f"  - Taxa de Mutação: {mutation_rate}")
        print("Inovando e pensando fora da caixinha para obter resultados de alta performance...\n")

        # Instancia o GA com os parâmetros
        ga = GeneticAlgorithm(
            n=n,
            distance_matrix=distance_matrix,
            flow_matrix=flow_matrix,
            pop_size=pop_size,
            generations=geracoes,
            mutation_rate=mutation_rate,
            elitism_type="simple",        # Ajuste se quiser testar "adaptive"
            selection_type="tournament",  # Ajuste se quiser testar "roulette"
            crossover_type="cx",          # Ajuste se quiser testar "pmx"
            mutation_type="swap",         # Ajuste se quiser testar "insertion"
            elite_rate=elite_rate,
            min_elite=1,
            max_elite=5
        )

        # Executa o GA e mede o tempo
        start_time = time.time()
        best_chromosome, best_fitness, cost_history = ga.run(show_progress=True)
        end_time = time.time()
        tempo_execucao = end_time - start_time

        # Armazena resultado
        resultados.append({
            "pop_size": pop_size,
            "geracoes": geracoes,
            "elite_rate": elite_rate,
            "mutation_rate": mutation_rate,
            "melhor_solucao": best_chromosome,
            "melhor_custo": best_fitness,
            "tempo_execucao_s": tempo_execucao,
        })
        # print(cost_history)
        print(f"Melhor Custo Encontrado: {best_fitness}")
        print(f"Tempo de Execução: {tempo_execucao:.2f} segundos")
        print("-" * 60)

    # Salva os resultados em um CSV dentro da pasta 'results'
    df_resultados = pd.DataFrame(resultados)
    df_resultados.to_csv(output_path, index=False)
    print(f"Resultados salvos em: {output_path}")

    return resultados

