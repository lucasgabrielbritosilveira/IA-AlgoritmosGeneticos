import numpy as np

def swap_mutation(individual, mutation_rate=0.1):
    # Cria uma cópia do indivíduo para aplicar a mutação
    new_individual = individual.copy()

    # Verifica se a mutação deve ocorrer com base na taxa de mutação
    if np.random.rand() < mutation_rate:
        # Seleciona aleatoriamente dois índices diferentes
        idx1, idx2 = np.random.choice(len(new_individual), 2, replace=False)
        # Troca os valores nos índices selecionados
        new_individual[idx1], new_individual[idx2] = new_individual[idx2], new_individual[idx1]
    return new_individual  # Retorna o novo indivíduo com a mutação aplicada

def insertion_mutation(individual, mutation_rate=0.1):
    # Cria uma cópia do indivíduo para aplicar a mutação
    new_individual = individual.copy()

    # Verifica se a mutação deve ocorrer com base na taxa de mutação
    if np.random.rand() < mutation_rate:
        size = len(individual)  # Obtém o tamanho do indivíduo

        # Seleciona aleatoriamente um ponto para remover um elemento
        point = np.random.randint(0, size)

        remaining = individual.tolist()  # Converte o indivíduo para lista
        selected_value = remaining.pop(point)  # Remove o valor selecionado

        # Seleciona aleatoriamente uma posição para inserir o valor removido
        insert_position = np.random.randint(0, size)

        # Insere o valor removido na nova posição
        new_individual = np.array(
            remaining[:insert_position] +  # Elementos antes da posição de inserção
            [selected_value] +              # O valor removido
            remaining[insert_position:]     # Elementos após a posição de inserção
        )

    return new_individual  # Retorna o novo indivíduo com a mutação aplicada
