from sys import stdin


def read_list():
    out_list = []
    for line in stdin:
        if line != '\n':
            line = list(map(lambda x: int(x) , line.rstrip().split(' ')))
            out_list.append(line)
    return out_list


def get_edges(input_list):
    edges = set()
    for vertice in input_list:
        for edge in vertice[1:]:
            edges.add(tuple(sorted((vertice[0], edge))))
    return sorted(edges)


def line_graph(input_list):
    edges = [[x] for x in get_edges(input_list)]
    for edge in edges:
        neighbours = [x for x in input_list[edge[0][0]- 1][1:]]
        for neighbour in neighbours:
            for x in input_list[neighbour - 1][1:]:
                new_edge = tuple(sorted((neighbour, x)))
                if edge[0][0] in new_edge or edge[0][1] in new_edge:
                    edge.append(new_edge) if new_edge not in edge else None
        print(f'{edge[0]} ', end='')
        print(*sorted(edge[1:]), sep=' ')


if __name__ == "__main__":
    graph = read_list()
    line_graph(graph)
