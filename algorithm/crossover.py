import numpy as np

def cycle_crossover(parent1, parent2):
    size = len(parent1)
    child1 = np.full(size, -1)
    child2 = np.full(size, -1)

    p1_copy = parent1.copy().tolist()
    p2_copy = parent2.copy().tolist()

    # First child
    swap = True
    count = 0
    pos = 0

    while True:
        if count > size:
            break

        # Find next empty position
        for i in range(size):
            if child1[i] == -1:
                pos = i
                break

        if swap:
            # Copy from parent1
            while True:
                child1[pos] = parent1[pos]
                count += 1
                pos = parent2.tolist().index(parent1[pos])
                if p1_copy[pos] == -1:
                    swap = False
                    break
                p1_copy[pos] = -1
        else:
            # Copy from parent2
            while True:
                child1[pos] = parent2[pos]
                count += 1
                pos = parent1.tolist().index(parent2[pos])
                if p2_copy[pos] == -1:
                    swap = True
                    break
                p2_copy[pos] = -1

    # Handle any remaining unfilled positions
    for i in range(size):
        if child1[i] == -1:
            if p1_copy[i] == -1:
                child1[i] = parent2[i]
            else:
                child1[i] = parent1[i]

    # Second child - complement of first child
    for i in range(size):
        if child1[i] == parent1[i]:
            child2[i] = parent2[i]
        else:
            child2[i] = parent1[i]

    return child1, child2

def maximal_preservation_crossover(parent1, parent2):
    size = len(parent1)
    child1 = np.full(size, -1)
    child2 = np.full(size, -1)

    # First child
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    child1[start:end] = parent1[start:end]
    seen_elements = parent1[start:end].tolist()

    empty_positions = [i for i in range(size) if child1[i] == -1]
    k = 0
    for i in range(size):
        if parent2[i] not in seen_elements:
            child1[empty_positions[k]] = parent2[i]
            k += 1

    # Second child
    start, end = sorted(np.random.choice(range(size), 2, replace=False))
    child2[start:end] = parent2[start:end]
    seen_elements = parent2[start:end].tolist()

    empty_positions = [i for i in range(size) if child2[i] == -1]
    k = 0
    for i in range(size):
        if parent1[i] not in seen_elements:
            child2[empty_positions[k]] = parent1[i]
            k += 1

    return np.array(child1), np.array(child2)
