
from environment.environment import Environment
from experiments.parte_0 import testar_parametros

# Parâmetros iniciais
n = 10
distance_matrix, flow_matrix = Environment(n)

# Executar o teste e salvar o CSV na pasta 'results'
resultados = testar_parametros(n, distance_matrix, flow_matrix, output_csv="resultados_ga.csv")
