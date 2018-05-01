from entropy import get_best_attribute
import pandas as pd

def decision_tree(filename):
    df = pd.read_csv(filename)
    a = get_best_attribute(filename, df)
    df.drop(a[0], axis=1, inplace=True)
    print(a)
    b = get_best_attribute(filename, df)
    print(b)
    df.drop(b[0], axis=1, inplace=True)    
    b = get_best_attribute(filename, df)
    print(b)

if __name__ == '__main__':
    decision_tree('restaurant.csv')