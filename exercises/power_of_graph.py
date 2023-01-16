from sys import stdin
import copy

def read_list():
    out_list = []
    for line in stdin:
        line = list(map(lambda x: int(x), line.rstrip().split(' ')))
        out_list.append(line)
    return out_list


def power_of_graph(input):
    result = copy.deepcopy(input)

    for vertice, edges in enumerate(input):
        for edge in edges[1:]:
            for neighbour in input[edge - 1]:
                result[vertice].append(neighbour) if neighbour not in input[vertice] else None
            result[vertice] = [result[vertice][0]] + sorted(result[vertice][1:])

    for vertice in result:
        print(*vertice, sep = ' ')


if __name__ == "__main__":
    input_list = read_list()
    power_of_graph(input_list)
    
