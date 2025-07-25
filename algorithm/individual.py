class Individual:
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None

    def calculate_fitness(self, dist_matrix, flow_matrix):
        """Calcula o fitness para este indivíduo."""
        if self.fitness is None:
            self.fitness = 0
            size = len(self.chromosome)
            for i in range(size - 1):
                for j in range(i, size):
                    self.fitness += (dist_matrix[i][j] * 
                                   flow_matrix[self.chromosome[i]][self.chromosome[j]])
        return self.fitness

    def __lt__(self, other):
        return self.fitness < other.fitness

    def __eq__(self, other):
        return self.fitness == other.fitness

    def __gt__(self, other):
        return self.fitness > other.fitness