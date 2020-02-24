#!./env/bin/python3
from entropy import get_best_attribute, normalize_data
import pandas as pd
import sys

class Node:
    def __init__(self, name, val_set):
        self.name = name
        self.val_set = val_set
        
def decision_tree(filename):
    global df
    df = pd.read_csv(filename, index_col=0)
    normalize_data(df)
    attrib_best = get_best_attribute(df)[0]
    #get_common()
    ID3(df, list(df)[-1], attrib_best, 0)

def get_common(val, attribs):
    global common
    global count

    class_name = list(df)[-1]
    df_aux = df[df[attribs] == val]
    common = set(df_aux[class_name]).pop()
    count = 0
    for val in set(df_aux[class_name]):
        if count < df_aux[df_aux[class_name] == val][class_name].count():
            count = df_aux[df_aux[class_name] == val][class_name].count()
            common = val

def ID3(dataframe, target_attrib, attribs, cnt):
    root = Node(attribs, set(df[attribs]))
    print("    "*cnt + "<{}>".format(attribs))
    file_.write("    "*cnt + "<{}>\n".format(attribs))
    for val in root.val_set:
        df_aux = dataframe[dataframe[attribs] == val]
        a = set(df_aux[target_attrib])
        if len(a) == 1:
            aux_1 = a.pop()
            print("    "*(cnt + 1) + "{}: {} ({})".format(val, aux_1, df_aux[attribs].count()))
            file_.write("    "*(cnt + 1) + "{}: {} ({})\n".format(val, aux_1, df_aux[attribs].count()))
        elif len(a) == 0:
            get_common(val, attribs)
            print("    "*(cnt + 1) + "{}: {} ({})".format(val, common, count))
            file_.write("    "*(cnt + 1) + "{}: {} ({})\n".format(val, common, count))
        elif len(dataframe) > 1:
            print("    "*(cnt + 1) + "{}: ".format(val))  
            file_.write("    "*(cnt + 1) + "{}: \n".format(val))
            if len(list(df_aux.drop(attribs, axis=1))) == 1:
                return
            ID3(df_aux.drop(attribs, axis=1), target_attrib, get_best_attribute(df_aux.drop(attribs, axis=1))[0], cnt + 2)

file_ = None

if __name__ == '__main__':
    name = sys.argv[1]
    aux = name.split('/')[-1]
    file_name = aux.split('.')[0]
    file_ = open('output/tree_{}.txt'.format(file_name), 'w')
    decision_tree(name)
    file_.close()