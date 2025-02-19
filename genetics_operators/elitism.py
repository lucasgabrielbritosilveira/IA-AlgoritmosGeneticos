import numpy as np

def fixed(population, fitness, prev_best_cost, elite_size=2):
    return    

def adaptive(population, fitness, prev_best_cost, min_elite=1, max_elite=5):
    return 

def compute(type, population, fitness, elite_size, prev_best_cost, min_elite=None, max_elite=None):
    if type == "fixed":
        return fixed(population, fitness, elite_size)
    if type == "adaptive":
        return adaptive(population, fitness, prev_best_cost, elite_size, min_elite, max_elite)
