from sys import stdin


def read_list():
    out_list = []
    for line in stdin:
        line = list(map(lambda x: int(x), line.rstrip().split(' ')))
        out_list.append(line)
    return out_list


def degree(input_list):
    sum = 0
    for line in input_list:
        sum += len(line) - 1
    deg = sum / len(input_list)
    return (round(deg + 0.001, 2))


def vertices_count(input_list):
    return len(input_list)


def edges_count(input_list):
    edges = [[vertice[0], edge] for vertice in input_list for edge in vertice[1:]]
    edges = {tuple(sorted(edge)) for edge in edges}
    return len(edges)


def degree_sequence(input_list):
    return [len(vertice) - 1 for vertice in input_list]


if __name__ == "__main__":
    user_input = read_list()
    print(f'Ilość wierzchołków: {vertices_count(user_input)}')
    print(f'Ilość krawędzi: {edges_count(user_input)}')
    print('Stopnie wierzchołków: ', end='')
    print(*degree_sequence(user_input), sep=' ')
    print(f'Średni stopień: {degree(user_input)}')

