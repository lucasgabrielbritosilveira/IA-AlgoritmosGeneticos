import pandas as pd
from experiments.base_experiment import run_experiment

def run():
    # Configurações para o experimento
    configurations = [
        {"selection": "tournament", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "swap"}
    ]

    # Executa o experimento com as configurações definidas
    results = run_experiment(
        configurations=configurations,
        parameter_to_display="selection"
    )

    # Salva os resultados em um arquivo CSV
    df_resultados = pd.DataFrame(results)
    output = 'results/resultados_experimento1.csv'
    df_resultados.to_csv(output, index=False)
    print(f"Resultados salvos em: /{output}")
