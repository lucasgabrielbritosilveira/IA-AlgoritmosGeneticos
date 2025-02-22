from experiments.base_experiment import run_experiment

def run():
    configurations = [
        {"selection": "roulette", "crossover": "cx", "elitism": "simple", "mutation": "swap"},
        {"selection": "tournament", "crossover": "mpx", "elitism": "simple", "mutation": "swap"},
        {"selection": "tournament", "crossover": "cx", "elitism": "tournament", "mutation": "swap"},
        {"selection": "tournament", "crossover": "cx", "elitism": "simple", "mutation": "insertion"},
    ]

    STEP = 10
    n = 10

    while True:
      print(run_experiment(
          n=n,
          configurations=configurations,
          repeat=1
      ))
      n += STEP
