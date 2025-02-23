from experiments.base_experiment import run_experiment
import pandas as pd

def run():
    configurations = [
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "roulette", "crossover": "cx", "elitism": "tournament", "mutation": "swap"}
    ]
    results = run_experiment(
        configurations=configurations,
        parameter_to_display="elitism"
    )

    df_resultados = pd.DataFrame(results)
    output = 'results/resultados_experimento3.csv'
    df_resultados.to_csv(output, index=False)
    print(f"Resultados salvos em: /{output}")