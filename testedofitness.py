import pandas as pd
from environment import Environment
from algorithm.genetic_algorithm import GeneticAlgorithm
import random


# Matrizes do enunciado do trabalho
distance_matrix = [[0, 10, 15],[10, 0, 12],[15, 12, 0]]
flow_matrix = [[0, 3, 6],[3, 0, 1],[6, 1, 0]]

n = 3
env = Environment(n)

ga = GeneticAlgorithm(n, distance_matrix, flow_matrix)

print(f"Matriz de distâncias:\n{distance_matrix}")
print(f"Matriz de fluxos:\n{flow_matrix}")

# Run genetic algorithm
best_cost, best_chromosome, formatted_cost_history = ga.run(show_progress=True)
print(f"Melhor custo: {best_cost}")
print(f"Melhor cromossomo: {best_chromosome}")
