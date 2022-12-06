from sys import stdin


def read_input():
    out_matrix = []
    for line in stdin:
        line = [int(i) for i in line.rstrip().split()]
        out_matrix.append(line)
    return out_matrix


def generate_edges(matrix):
    edges = []
    for row_index, row in enumerate(matrix):
        for edge_index, edge in enumerate(row):
            if not edge == 0 and not (edge_index, row_index, edge) in edges:
                edges.append((row_index, edge_index, edge))
    return sorted(edges, key=lambda edge: edge[2])


def kruskal(edges, v_count):
    min_weight = 0
    parent = list(range(v_count))
    union = [[] for _ in range(v_count)]
    for edge in edges:
        parent_x = parent[edge[0]]
        parent_y = parent[edge[1]]
        if not parent_x == parent_y:
            for val in union[parent_x]:
                parent[val] = parent_y
                union[parent_y].append(val)
            union[parent_y].append(parent_x)
            union[parent_x].clear()
            parent[parent_x] = parent_y
            min_weight += edge[2]
            if len(union[parent_y]) == v_count - 1:
                break
    union = list(filter(None, union))
    return min_weight if len(union) == 1 else 'Graf nie jest spójny'


if __name__ == "__main__":
    input_matrix = read_input()
    input_edges = generate_edges(input_matrix)
    print(kruskal(input_edges, len(input_matrix)))
