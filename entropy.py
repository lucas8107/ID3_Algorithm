import pandas as pd
import numpy as np
import math
import sys

def entropy(attribute, df, class_name):
    entropia_list = []
    aux = len(df[attribute])
    attrib = list(set(df[attribute]))
    clazz = list(set(df[class_name]))

    count_matrix = [np.zeros(len(clazz)) for i in range(len(attrib))]

    attrib = dict(zip(attrib, (range(len(attrib)))))
    clazz = dict(zip(clazz, (range(len(clazz)))))

    for i in range(aux):
        count_matrix[attrib[df[attribute].iloc[i]]][clazz[df[class_name].iloc[i]]]+=1

    total_list = [0]*len(attrib)

    for i in range(len(attrib)):
        total = sum(count_matrix[i])
        count_matrix[i] = count_matrix[i]/sum(count_matrix[i])
        for j in range(len(count_matrix[i])):
            if count_matrix[i][j] != 0:
                count_matrix[i][j] = -1*count_matrix[i][j]*math.log(count_matrix[i][j], 2)
        count_matrix[i] = sum(count_matrix[i])*(total/aux)

    return sum(count_matrix)

def get_best_attribute(df):
    columns_name = list(df)
    best = (None ,sys.maxsize)
    for title in df:
        if title!=columns_name[-1]:
            aux = (title, entropy(title, df, columns_name[-1]))
            if best[1] > aux[1]:
                best = aux
    if best[0] is None:
        print("Error")
        return
    return best

## The code below is for categorization of raw number data

def num_int(dataframe, column):
    min_ = dataframe[column].min()
    max_ = dataframe[column].max()
    R = max_ - min_
    k = 1 + 3.222*np.log10(dataframe[column].count())
    w = round(R/int(round(k)), 2)
    for i in range(0, int(round(k))):
        dataframe[column] = dataframe[column].apply(lambda x: fun(x, min_, w, i))
    
def fun(x, min_, w, i):
    if type(x) is str:
        return x
    if min_ + w*i <= x <= min_ + w*(i + 1):
        return '{} - {}'.format(round(min_ + w*i, 2), round(min_ + w*(i + 1), 2))
    else:
        return x

def normalize_data(dataframe):
    numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
    for col in dataframe.select_dtypes(include=numerics):
        num_int(dataframe, col)