from sys import stdin


def read_list():
    out_list = []
    for line in stdin:
        line = list(map(lambda x: int(x), line.rstrip().split(' ')))
        out_list.append(line)
    return out_list


def degree_sequence(input_list):
    return [len(vertice) - 1 for vertice in input_list]


def sort_by_degree(input_list):
    x = {v+1:d for v,d in enumerate(degree_sequence(input_list))}
    x = sorted(x.items(), reverse=True)
    x = sorted(x, reverse=True, key= lambda item: item[1])
    x = dict(x)
    return x


def graph_coloring(input_list):
    sequence = sort_by_degree(input_list)    
    color_list = [0 for _ in range(len(input_list))]
    def get_neighbours_colors(curr_vertice):
        res = []
        for neighbour in input_list[curr_vertice][1:]:
            res.append(color_list[neighbour - 1])
        return res

    for vertice in sequence.keys():
        color = 1
        while color in get_neighbours_colors(vertice - 1):
            color += 1 
        color_list[vertice - 1] = color

    print(*color_list, sep=' ')
    print(f'Liczba chromatyczna == {len(set(color_list))}')
if __name__ == "__main__":
    input_list = read_list()
    graph_coloring(input_list)

