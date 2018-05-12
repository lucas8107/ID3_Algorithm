from entropy import get_best_attribute, normalize_data
import pandas as pd

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
    for val in root.val_set:
        df_aux = dataframe[dataframe[attribs] == val]
        a = set(df_aux[target_attrib])
        if len(a) == 1:
            print("    "*(cnt + 1) + "{}: {} ({})".format(val, a.pop(), df_aux[attribs].count()))
        elif len(a) == 0:
            get_common(val, attribs)
            print("    "*(cnt + 1) + "{}: {} ({})".format(val, common, count))
        elif len(dataframe) > 1:
            print("    "*(cnt + 1) + "{}: ".format(val))   
            if len(list(df_aux.drop(attribs, axis=1))) == 1:
                return
            ID3(df_aux.drop(attribs, axis=1), target_attrib, get_best_attribute(df_aux.drop(attribs, axis=1))[0], cnt + 2)

if __name__ == '__main__':
    decision_tree(input("File name: "))