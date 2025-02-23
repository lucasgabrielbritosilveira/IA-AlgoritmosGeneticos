from experiments.base_experiment import run_experiment
import pandas as pd

def run():
    configurations = [
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "insertion"},
        {"selection": "roulette", "crossover": "mpx", "elitism": "simple", "mutation": "insertion"}
    ]

    results = run_experiment(
        configurations=configurations,
        parameter_to_display="crossover"
    )

    df_resultados = pd.DataFrame(results)
    output = 'results/resultados_experimento2.csv'
    df_resultados.to_csv(output, index=False)
    print(f"Resultados salvos em: /{output}")
