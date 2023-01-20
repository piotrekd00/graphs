from sys import stdin
from copy import deepcopy

def read_list():
    out_list = []
    first_list = []
    for line in stdin:
        if line != '\n':
            line = list(map(lambda x: int(x) , line.rstrip().split(' ')))
            out_list.append(line)
        else:
            first_list = deepcopy(out_list)
            out_list.clear()
    return first_list, out_list


if __name__ == "__main__":
    graph, edges = read_list()
    flag = False
    for edge in edges:
        for v in edge:
            subset = [x for x in edges if x != edge] 
            for e in subset:
                if v in e:
                    flag = True
    if flag:
        print('Nie jest to skojarzenie')
    else:
        print('Jest to skojarzenie')
