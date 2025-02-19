import numpy as np

def compute(type, individual, mutation_rate=0.1):
    if type == "swap":
        return swap(individual, mutation_rate)
    if type == "inversion":
        return inversion(individual, mutation_rate)
