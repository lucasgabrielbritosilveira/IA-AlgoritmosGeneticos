import itertools
from algorithm.genetic_algorithm import GeneticAlgorithm

def testar_parametros(n, distance_matrix, flow_matrix):
    # Parâmetros a serem testados
    lista_pop_sizes = [50, 100, 150]
    lista_geracoes = [50, 100, 200]
    lista_elite_rates = [1, 2, 4]
    lista_mutation_rates = [0.05, 0.1, 0.15]
    
    # Gerar todas as combinações possíveis
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
            elitism_type="simple",       # Ajuste se quiser testar "adaptive"
            selection_type="tournament",# Ajuste se quiser testar "roulette"
            crossover_type="ox",        # Ajuste se quiser testar "pmx"
            mutation_type="swap",       # Ajuste se quiser testar "insertion"
            elite_rate=elite_rate,
            min_elite=1,
            max_elite=5
        )
        
        # Executa o GA
        best_chromosome, best_fitness, cost_history = ga.run(show_progress=False)
        
        # Armazena resultado
        resultados.append({
            "pop_size": pop_size,
            "geracoes": geracoes,
            "elite_rate": elite_rate,
            "mutation_rate": mutation_rate,
            "melhor_solucao": best_chromosome,
            "melhor_custo": best_fitness,
        })
        
        print(f"Melhor Custo Encontrado: {best_fitness}")
        print("-"*60)
    
    # Aqui poderíamos, por exemplo, retornar uma lista de dicionários
    # ou analisar os resultados de forma mais sofisticada
    return resultados

# Exemplo de chamada (assumindo que distance_matrix e flow_matrix já estejam disponíveis)
n = len(distance_matrix)  # ou tamanho adequado do problema
resultados = testar_parametros(n, distance_matrix, flow_matrix)
print(resultados)
