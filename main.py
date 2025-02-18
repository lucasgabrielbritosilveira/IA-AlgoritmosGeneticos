from problem import run_all_combinations

# # ----------------------- FUNÇÃO MAIN -----------------------
# def main():
#     n = 31  # Número de instalações/locais
#     pop_size = 50
#     generations = 100
#     mutation_rate = 0.1

#     distance_matrix, flow_matrix = generate_pqa_instance(n)

#     best_solution, best_cost = genetic_algorithm(
#         n, distance_matrix, flow_matrix, pop_size, generations, mutation_rate,
#         elitism_type="adaptive", selection_type="roulette",
#         crossover_type="pmx", mutation_type="inversion"
#     )

#     print("\nMelhor solução encontrada:", best_solution)
#     print("Custo da melhor solução:", best_cost)

# # Executar se for o script principal
# if __name__ == "__main__":
#     main()

if __name__ == "__main__":
    results = run_all_combinations()

    print("\n📊 Resumo de todas as execuções:")
    for r in results:
        print(f"Elitismo: {r[0]}, Seleção: {r[1]}, Crossover: {r[2]}, Mutação: {r[3]}, Custo: {r[4]}")


# Elitismo: adaptive, Seleção: tournament, Crossover: pmx, Mutação: swap, Custo: 208094
