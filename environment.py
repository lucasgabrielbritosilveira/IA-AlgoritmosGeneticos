import numpy as np
from utils import *
def Enviroment():
    n = 3
    distance_matrix = []
    flow_matrix =  np.zeros((n, n))
    
    points = []
    for i in range(n):
        x,y = generate_random_coordinates()
        point = Node(x,y)
        points.append(point)
    

    for i in points:
        tmp = []
        for k in points:
            tmp.append(euclidean_heuristic(i,k))
        distance_matrix.append(tmp)
            
    for i in range(n):
        for j in range(i + 1, n): 
            valor = random.randint(0, n)
            flow_matrix[i][j] = valor
            flow_matrix[j][i] = valor  
            
            
return np.array(distance_matrix), np.array(flow_matrix)