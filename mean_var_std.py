import numpy as np


def calculate(list):
    # chequeo si la lista tiene 9 elementos
    if len(list) != 9:
        raise ValueError ("La lista debe tener 9 elementos")
    matriz=np.array(list).reshape(3,3)

    # Calcula la media
    mean_rows =  np.mean(matriz, axis=1).tolist()
    mean_cols =  np.mean(matriz, axis=0).tolist()
    mean_flat =  np.mean(matriz.flatten()) 

    # Calcula la varianza
    var_rows =  np.var(matriz, axis=1).tolist()
    var_cols =  np.var(matriz, axis=0).tolist()
    var_flat =  np.var(matriz.flatten())
    
    # Calcula la desviación estándar
    std_rows =  np.std(matriz, axis=1).tolist()
    std_cols =  np.std(matriz, axis=0).tolist()
    std_flat =  np.std(matriz.flatten())
    
    # Calcula max
    max_rows =  np.max(matriz, axis=1).tolist()
    max_cols =  np.max(matriz, axis=0).tolist()
    max_flat =  np.max(matriz.flatten())
    
    # Calcula  min
    min_rows =  np.min(matriz, axis=1).tolist()
    min_cols =  np.min(matriz, axis=0).tolist()
    min_flat =  np.min(matriz.flatten())
        
    # Calcula suma
    sum_rows =  np.sum(matriz, axis=1).tolist()
    sum_cols =  np.sum(matriz, axis=0).tolist()
    sum_flat =  np.sum(matriz.flatten())

    return{
        'mean': [mean_cols,mean_rows,mean_flat],
        'variance': [var_cols, var_rows, var_flat],
        'standard_deviation': [std_cols, std_rows, std_flat],
        'max': [max_cols, max_rows, max_flat],
        'min': [min_cols, min_rows, min_flat],
        'sum': [sum_cols, sum_rows, sum_flat]
        
        }  # Devuelve un diccionario con los resultados
   

    


 
