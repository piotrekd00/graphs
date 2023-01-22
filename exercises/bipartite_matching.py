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
    subset = sets[1] if len(sets[1]) <= len(sets[2]) else sets[2]
    neighbours = [graph[v - 1][1:] for v in subset]
    matches = []
    for vertice in subset:
        merged_neighbours = sum(neighbours[1:], []) 
        for neighbour in neighbours[0]:
            if neighbour not in merged_neighbours:
                matches.append((vertice, neighbour))
                neighbours.pop(0)
                break
    if len(matches) == len(subset):
        print('Istnieje skojarzenie doskonałe')
    else:
        print('Nie istnieje skojarzenie doskonałe')
         


if __name__ == "__main__":
    input_list = read_list()
    expected1 = [[1, 5], [2, 5], [3, 5, 7, 8, 9], [4, 5, 6, 7, 9], [5, 1, 2, 3, 4], [6, 4], [7, 3, 4], [8, 3], [9, 3, 4]]
    expected2 = [[1, 5, 8, 9], [2, 5], [3, 7, 8], [4, 6, 8], [5, 1, 2], [6, 4], [7, 3], [8, 1, 3, 4], [9, 1]]
    if input_list != expected1 and input_list != expected2:
        print(input_list)
    perfect_matching(input_list)
