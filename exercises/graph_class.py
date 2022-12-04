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
    res = round(deg + 0.001, 2)
    return int(res) if res.is_integer() else res


def vertices_count(input_list):
    return len(input_list)


def edges_count(input_list):
    edges = [[vertice[0], edge] for vertice in input_list for edge in vertice[1:]]
    edges = {tuple(sorted(edge)) for edge in edges}
    return len(edges)


def degree_sequence(input_list):
    return [len(vertice) - 1 for vertice in input_list]


def finite_graph(v_count, e_count):
    if (v_count*(v_count - 1))//2 == e_count:
        return True
    return False


def cycle_graph(d_seq, v_count):
    if all(d == 2 for d in d_seq) and v_count > 2:
        return True
    return False


def path_graph(d_seq, v_count):
    if v_count > 2:
        if d_seq.count(1) == 2 and d_seq.count(2) == v_count - 2:
            return True
        return False
    return True
                

def tree_graph(d_seq, v_count, e_count):
    if e_count == v_count - 1 and 0 not in d_seq:
        return True
    return False


def hypercube(d_seq, v_count, e_count):
    x = d_seq[0]
    if d_seq.count(x) == v_count and e_count == x * 2**(x - 1):
        return True


def check_class(d_seq, v_count, e_count):
    c = 0
    if finite_graph(v_count, e_count):
        c += 1
        print('Jest to graf pełny')
    if cycle_graph(d_seq, v_count):
        c += 1
        print('Jest to cykl')
    if path_graph(d_seq, v_count):
        c += 1
        print('Jest to ścieżka')
    if tree_graph(d_seq, v_count, e_count):
        c += 1
        print('Jest to drzewo')
    if hypercube(d_seq, v_count, e_count):
        c += 1
        print('Jest to hiperkostka')
    if c == 0:
        print('Graf nie należy do żadnej z podstawowych klas')


if __name__ == "__main__":
    user_input = read_list()
    v_count = vertices_count(user_input)
    e_count = edges_count(user_input)
    d_seq = degree_sequence(user_input)
    print(f'Ilość wierzchołków: {v_count}')
    print(f'Ilość krawędzi: {e_count}')
    print('Stopnie wierzchołków: ', end='')
    print(*d_seq, sep=' ')
    print(f'Średni stopień: {degree(user_input)}')
    check_class(d_seq, v_count, e_count)
