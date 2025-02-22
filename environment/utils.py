import numpy as np
import random

def euclidean_heuristic(node1, node2):
    return np.floor(np.sqrt((node1.x - node2.x) ** 2 + (node1.y - node2.y) ** 2))

def generate_random_coordinates(max_size):
    x = random.randint(0, max_size)
    y = random.randint(0, max_size)

    return x, y
