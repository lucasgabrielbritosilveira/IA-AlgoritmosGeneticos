from experiments.base_experiment import run_experiment

def run():
    configurations = [
        {"selection": "tournament", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "swap"}
    ]

    run_experiment(
        configurations=configurations,
        parameter_to_display="selection"
    )
