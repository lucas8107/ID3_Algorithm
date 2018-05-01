import pandas as pd
import numpy  as np

df = pd.read_csv('restaurant.csv')
def entropia(data, titles):
    # vs = ["a","b","a","b","a","a","c","b","c","b","c"]
    # cs = ["4","2","1","4","1","2","4","3","3","4","2"]
    for i in range(1, len(data[0])-1):
        # values
        vs = [v[i] for v in data]
        # class values ... por padrao a ultima classe
        cs = [v[len(data[0])-1]   for v in data]
        # for v in df.values:
        #     print(v)
        print(titles[i])
        print (vs)
        print (cs)
        print(E(vs, cs))
        print()
    # print(df)

# col coluna que esotu a avaliar
# cl coluna de classificacao
def E(col, cl):
    p_cl = possible_values(cl)
    ret = []
    for pc in possible_values(col):
        cont_col = [0 for i in range(len(p_cl))]
        cont_total = 0    
        for i in range(len(cl)):
            for j in range(len(p_cl)):
                if col[i] == pc and cl[i] == p_cl[j]:
                    cont_total+=1
                    cont_col[j]+=1
            
        # print(cont_col)
        # print(cont_total)

        r = 0.0
        for c in cont_col:
            if c != 0:
                r+=(-1)*float(c)/cont_total * np.log2(float(c)/cont_total)
            # print(float(c)/cont_total)
        ret.append((r, cont_total))
    # print(ret)

    return sum([(v[0]*float(v[1])/len(cl)) for v in ret])
def possible_values(c):
    a = []
    for i in c:
        if(not i in a):
            a.append(i)
    return a

# dado um valor inicial um valor final e um numero de divisoes, a funcao retorna uma lista ugualmente espaçada de  valores
def interval(val_start, val_end, num):
	return [val_start+ (i*(val_end-val_start)/(num-1)) for i in range((num))]

def main():
    entropia(df.values, df.columns)
    return 0

main()

