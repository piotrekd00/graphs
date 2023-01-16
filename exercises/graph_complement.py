from sys import stdin


def read_list():
    out_list = []
    for line in stdin:
        line = list(map(lambda x: int(x), line.rstrip().split(' ')))
        out_list.append(line)
    return out_list


def graph_complement(input):
    result = [[x + 1] for x in range(len(input))]
    for vertice, edges in enumerate(input):
        result[vertice] = result[vertice] + [x + 1 for x in range(len(input)) if x + 1 not in edges]
    for vertice in result:
        print(*vertice, sep = ' ')


if __name__ == "__main__":
    input_list = read_list()
    graph_complement(input_list)
    
