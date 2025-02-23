from experiments.base_experiment import run_experiment
import pandas as pd

def run():
    configurations = [
        {"selection": "tournament", "crossover": "cx", "elitism": "tournament", "mutation": "swap"},
        {"selection": "tournament", "crossover": "cx", "elitism": "tournament", "mutation": "insertion"}
    ]
    results = run_experiment(
        configurations=configurations,
        parameter_to_display="mutation"
    )

    df_resultados = pd.DataFrame(results)
    output = 'results/resultados_experimento4.csv'
    df_resultados.to_csv(output, index=False)
    print(f"Resultados salvos em: /{output}")
