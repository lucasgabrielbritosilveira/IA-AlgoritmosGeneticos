from experiments.base_experiment import run_experiment
import pandas as pd

def run():
    configurations = [
        {"selection": "tournament", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "tournament", "crossover": "mpx", "elitism": "simple", "mutation": "swap"}
    ]
    
    results = run_experiment(
        configurations=configurations,
        parameter_to_display="crossover"
    )

    df_resultados = pd.DataFrame(results)
    output = 'results/resultados_experimento2.csv'
    df_resultados.to_csv(output, index=False)
    print(f"Resultados salvos em: /{output}")
