from experiments.base_experiment import run_experiment

def run():
    configurations = [
        {"selection": "tournament", "crossover": "cx", "elitism": "tournament", "mutation": "swap"},
        {"selection": "tournament", "crossover": "cx", "elitism": "tournament", "mutation": "insertion"}
    ]
    run_experiment(
        configurations=configurations,
        parameter_to_display="mutation"
    )
