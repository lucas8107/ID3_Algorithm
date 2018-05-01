import pandas as pd
import numpy as np
import math
import sys

def entropy(attribute, df, class_name):
    entropia_list = []
    aux = len(df[attribute])
    attrib = list(set(df[attribute]))
    clazz = list(set(df[class_name]))

    count_matrix = []
    for i in range(len(attrib)):
        count_matrix.append(np.zeros(len(clazz)))

    attrib = dict(zip(attrib, (range(len(attrib)))))
    clazz = dict(zip(clazz, (range(len(clazz)))))

    for i in range(aux):
        count_matrix[attrib[df[attribute][i]]][clazz[df[class_name][i]]]+=1

    total_list = [0]*len(attrib)

    for i in range(len(attrib)):
        total = sum(count_matrix[i])
        count_matrix[i] = count_matrix[i]/sum(count_matrix[i])
        for j in range(len(count_matrix[i])):
            if count_matrix[i][j] != 0:
                count_matrix[i][j] = -1*count_matrix[i][j]*math.log(count_matrix[i][j], 2)
        count_matrix[i] = sum(count_matrix[i])*(total/aux)

    return sum(count_matrix)

def get_best_attribute(filename, df):
    # df = pd.read_csv(filename)
    columns_name = list(df)
    menor = (None ,sys.maxsize)
    for title in df:
        if title != columns_name[0] and title!=columns_name[-1]:
            aux = (title, entropy(title, df, columns_name[-1]))
            if menor[1] > aux[1]:
                menor = aux
    if menor[0] is None:
        print("Error")
        return
    return menor