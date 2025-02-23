import pandas as pd
from environment.environment import Environment
from experiments.base_experiment import run_experiment
from experiments.parte_0 import testar_parametros as experimento0
from experiments.parte_1 import run as experimento1
from experiments.parte_2 import run as experimento2
from experiments.parte_3 import run as experimento3
from experiments.parte_4 import run as experimento4
from experiments.parte_5 import run as experimento5

def main():
    while True:
        print("\n=== Menu Principal ===")
        print("0: Executar Experimento 0")
        print("1: Executar Experimento 1")
        print("2: Executar Experimento 2")
        print("3: Executar Experimento 3")
        print("4: Executar Experimento 4")
        print("5: Executar Experimento 5")
        print("6: Executar Experimentação Livre")
        print("q: Sair")

        choice = input("\nEscolha uma opção: ")

        if choice == '0':
            n = int(input("Digite o valor de n: "))
            distance_matrix, flow_matrix = Environment(n)
            experimento0(n, distance_matrix, flow_matrix)
        elif choice == '1':
            experimento1()
        elif choice == '2':
            experimento2()
        elif choice == '3':
            experimento3()
        elif choice == '4':
            experimento4()
        elif choice == '5':
            experimento5()
        elif choice == '6':
            n = int(input("Digite o valor de n: "))
            distance_matrix, flow_matrix = Environment(n)
            pop_size = int(input("Digite o tamanho da população (default 100): ") or 100)
            generations = int(input("Digite o número de gerações (default 100): ") or 100)
            elite_rate = float(input("Digite a taxa de elitismo (default 0.2): ") or 0.2)
            mutation_rate = float(input("Digite a taxa de mutação (default 0.1): ") or 0.1)
            min_elite = int(input("Digite o mínimo de elitismo (default 1): ") or 1)
            max_elite = int(input("Digite o máximo de elitismo (default 5): ") or 5)

            elitism_options = ["simple", "tournament"]
            selection_options = ["tournament", "roulette"]
            crossover_options = ["cx", "mpx"]
            mutation_options = ["swap", "insertion"]

            print("Escolha o tipo de elitismo:")
            for i, option in enumerate(elitism_options):
                print(f"{i}: {option}")
            elitism_type = elitism_options[int(input("Digite o número da opção: "))]

            print("Escolha o tipo de seleção:")
            for i, option in enumerate(selection_options):
                print(f"{i}: {option}")
            selection_type = selection_options[int(input("Digite o número da opção: "))]

            print("Escolha o tipo de crossover:")
            for i, option in enumerate(crossover_options):
                print(f"{i}: {option}")
            crossover_type = crossover_options[int(input("Digite o número da opção: "))]

            print("Escolha o tipo de mutação:")
            for i, option in enumerate(mutation_options):
                print(f"{i}: {option}")
            mutation_type = mutation_options[int(input("Digite o número da opção: "))]

            repeat = int(input("Escolha a quantidade de repetições (default 1): ") or 1)

            results = run_experiment(
                configurations=[{
                    "elitism": elitism_type,
                    "selection": selection_type,
                    "crossover": crossover_type,
                    "mutation": mutation_type
                }],
                pop_size=pop_size,
                generations=generations,
                elite_rate=elite_rate,
                mutation_rate=mutation_rate,
                n=n,
                min_elite=min_elite,
                max_elite=max_elite,
                repeat=repeat
            )

            print("\nResultados da experimentação livre:")
            for result in results:
                print(result)

            df_resultados = pd.DataFrame(results)
            output = 'results/resultados_experimento-livre.csv'
            df_resultados.to_csv(output, index=False)
            print(f"Resultados salvos em: /{output}")

        elif choice.lower() == 'q':
            print("Saindo...")
            break
        else:
            print("Escolha inválida. Tente novamente.\n")

if __name__ == "__main__":
    main()
