import numpy as np
import itertools
from algorithm import Algorithm
from environment import Enviroment

def run_all_combinations(n=31, pop_size=50, generations=100, mutation_rate=0.1):
    elitism_options = ["fixed", "adaptive"]
    selection_options = ["tournament", "roulette"]
    crossover_options = ["oder", "pmx"]
    mutation_options = ["swap", "inversion"]
    
    param_combinations = list(itertools.product(
        elitism_options, selection_options, crossover_options, mutation_options
    ))
    
    distance_matrix, flow_matrix = Enviroment(n)

    results = []  
    
    for params in param_combinations:
        elitism_type, selection_type, crossover_type, mutation_type = params
        
        print("\n🔹 Executando com parâmetros:")
        print(f"  - Elitismo: {elitism_type}")
        print(f"  - Seleção: {selection_type}")
        print(f"  - Crossover: {crossover_type}")
        print(f"  - Mutação: {mutation_type}")
        
        best_solution, best_cost = Algorithm.run(
            n, distance_matrix, flow_matrix, pop_size, generations, mutation_rate,
            elitism_type=elitism_type, selection_type=selection_type,
            crossover_type=crossover_type, mutation_type=mutation_type
        )

        print(f" Melhor solução encontrada: {best_solution}")
        print(f"Custo da melhor solução: {best_cost}")
        
        results.append((elitism_type, selection_type, crossover_type, mutation_type, best_cost))
    
    return results  