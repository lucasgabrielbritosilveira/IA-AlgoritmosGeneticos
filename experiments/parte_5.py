import pandas as pd
from itertools import chain
from experiments.base_experiment import run_experiment

def run():
    # Melhores configurações dos experimentos do 1 - 4
    configurations = [
        {"selection": "tournament", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "insertion"},
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "tournament", "crossover": "mpx", "elitism": "tournament", "mutation": "swap"}
    ]

    n = 10
    results = []

    MAX_N = 200
    STEP = 10

    # Executa o experimento para diferentes tamanhos de entrada
    while n <= MAX_N:
        result = run_experiment(
            n=n,
            grid_size=MAX_N,  # Tamanho da Grid acompanhando N para não haver repetições
            configurations=configurations,
            repeat=1
        )

        results.append(result)
        n += STEP

    # Salva os resultados em um CSV
    df_resultados = pd.DataFrame(list(chain.from_iterable(results)))
    output = 'results/resultados_experimento5.csv'
    df_resultados.to_csv(output, index=False)

    print(f"Resultados do experimento 5 salvos em: /{output}")
