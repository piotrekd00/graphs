from sys import stdin


def read_list():
    out_list = []
    for line in stdin:
        line = list(map(lambda x: int(x), line.rstrip().split(' ')))
        out_list.append(line)
    return out_list

def bipartite_check(graph):
    vertices_set = {1:[], 2:[], 3:[]}
    for edge in graph:
        i = 1
        available = False
        added = False
        while not added:
            for neighbour in edge[1:]:
                if neighbour in vertices_set[i]:
                    i += 1
                else:
                    available = True
            if available:
                vertices_set[i].append(edge[0])
                added = True
    if len(vertices_set[3]) > 0:
        return {}
    return vertices_set


def perfect_matching(graph):
    sets = bipartite_check(graph)
    neighbours = [graph[v - 1][1:] for v in sets[1]]
    matches = []
    for vertice in sets[1]:
        merged_neighbours = sum(neighbours[1:], []) 
        for neighbour in neighbours[0]:
            if neighbour not in merged_neighbours:
                matches.append((vertice, neighbour))
                neighbours.pop(0)
                break
    if len(matches) == len(sets[1]):
        print('Istnieje skojarzenie doskonałe')
    else:
        print('Nie istnieje skojarzenie doskonałe')
         


if __name__ == "__main__":
    input_list = read_list()
    perfect_matching(input_list)
