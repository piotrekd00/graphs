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
    done = False
    iterations = {v:0 for v in subset}
    while not done:
        for vertice in subset:
            local_iteration = iterations[vertice] 
            added = False
            impossible = False
            wrong_value = None
            merged_matches = sum(matches, [])
            local_neighbours = graph[vertice - 1][1:]
            while not added and not impossible:
                try:
                    match = [vertice, local_neighbours[local_iteration]]
                except IndexError:
                    match = [vertice, local_neighbours[-1]]
                if match[0] not in merged_matches and match[1] not in merged_matches:
                    matches.append(match)
                    added = True
                else:
                    wrong_value = merged_matches[merged_matches.index(match[1]) - 1]
                    local_iteration += 1
                    if local_iteration > len(local_neighbours) - 1:
                        impossible = True
            if not added: 
                iterations[wrong_value] += 1
                matches.clear()
                break
        if len(matches) == len(subset):
            done = True
            print('Istnieje skojarzenie doskonałe')
        elif max(iterations.values()) > len(max(neighbours, key=len)):
            done = True
            print('Nie istnieje skojarzenie doskonałe')


if __name__ == "__main__":
    input_list = read_list()
    # input_list = [[1, 26], [2, 20, 21, 22, 24, 26, 16], [3, 17, 18, 19, 21, 22], [4, 17, 19, 21, 26, 15], [5, 23, 11, 12, 14, 15], [6, 20, 22, 23, 12, 15, 16], [7, 17, 19, 20, 24, 12], [8, 21, 22, 23, 12, 14], [9, 17, 22, 23, 24, 25, 13, 14], [10, 17, 25, 13, 14, 15], [11, 5], [12, 5, 6, 7, 8], [13, 9, 10], [14, 5, 8, 9, 10], [15, 4, 5, 6, 10], [16, 2, 6], [17, 3, 4, 7, 9, 10], [18, 3], [19, 3, 4, 7], [20, 2, 6, 7], [21, 2, 3, 4, 8], [22, 2, 3, 6, 8, 9], [23, 5, 6, 8, 9], [24, 2, 7, 9], [25, 9, 10], [26, 1, 2, 4]]
    perfect_matching(input_list)
