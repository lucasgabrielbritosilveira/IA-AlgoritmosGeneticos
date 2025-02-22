
from environment.environment import Environment
from experiments.parte_0 import testar_parametros
from experiments.parte_1 import run as Experiment1Run
from experiments.parte_2 import run as Experiment2Run
from experiments.parte_3 import run as Experiment3Run
from experiments.parte_4 import run as Experiment4Run
from experiments.parte_5 import run as Experiment5Run

# Parâmetros iniciais
# n = 10
# distance_matrix, flow_matrix = Environment(n)

# Executar o teste e salvar o CSV na pasta 'results'
# resultados = testar_parametros(n, distance_matrix, flow_matrix, output_csv="resultados_ga.csv")
#-------------------------------
# Parâmetros iniciais
n = 10
distance_matrix, flow_matrix = Environment(n)

# Executar o teste e salvar o CSV na pasta 'results'
# resultados = testar_parametros(n, distance_matrix, flow_matrix, output_csv="resultados_ga.csv")

# Experiment1Run()
# Experiment2Run()
# Experiment3Run()
# Experiment4Run()
Experiment5Run()