from itertools import combinations

from sys import stdin

def read_input():
    out_matrix = []
    for line in stdin:
        line = [eval(i) for i in line.rstrip().split(' ')]
        out_matrix.append(line)
    return out_matrix


def held_karp(graph):
    start = 0
    neighbours = [vertice for vertice in range(1, len(graph))]
    distance_set = [{c:float('inf') for n in range(1, len(neighbours) + 1) for c in combinations(neighbours, n)} for _ in range(len(graph))]
    predecessor_set = [{c:float('inf') for n in range(1, len(neighbours) + 1) for c in combinations(neighbours, n)} for _ in range(len(graph))]
    
    def is_connected(graph):
        visited = [False] * len(graph)
        def dfs(v):
            visited[v] = True
            for i in range(len(graph)):
                if graph[v][i] != 0 and not visited[i]:
                    visited[i] = True
                    dfs(i)
        dfs(start)
        return True if all(visited) == True else False

    def get_path(end, last_set):
        print(end)
        while last_set != ():
            end = predecessor_set[end][tuple(last_set)]
            last_set = list(set(last_set) - set([end]))
            print(tuple(last_set))
        

    def simple_distance(v, s):
        if len(s) == 1:
            s = s[0]
            res = distance_set[start][(s, )]
            helper = graph[s][v]
            return (res + helper, s) if helper != 0 else (float('inf'), s)     

        dist = []

        for c in list(combinations(s, len(s) - 1)):
            u = tuple(set(s) - set(c))
            res = graph[v][u[0]] if graph[v][u[0]] !=0 else float('inf')
            dist.append((res + distance_set[u[0]][c], u[0]))
        return min(dist, key=lambda x: x[0])


    for n in range(1, len(graph)):
        distance_set[start][(n,)] = 1 if graph[start][n] == 1 else float('inf')
        predecessor_set[start][(n,)] = 0 if graph[start][n] == 1 else float('inf')

    for n in range(1, len(neighbours)):
        for comb in combinations(neighbours, n):
            v_set = list(set(neighbours) - set(comb))
            curr_dist = []
            for v in v_set:
                res = simple_distance(v, comb) 
                curr_dist.append((v, res[0], res[1]))
            v, min_of_curr_dist, pred =  min(curr_dist, key=lambda x: x[1])
            distance_set[v][comb] = min_of_curr_dist 
            predecessor_set[v][comb] = pred
    last_set = list(distance_set[start])[-1]
    end = simple_distance(start, last_set)

    is_hamiltonian = False
    is_path = False
    if not end[0] == float('inf'):
        is_hamiltonian = True 
    for comb in combinations(neighbours, len(graph) - 2):
        v = list(set(neighbours) - set(comb))[0]
        if distance_set[v][comb] != float('inf'):
            is_path = True

    if not is_connected(graph):
        print('Graf jest niespójny')
    elif is_hamiltonian:
        print('Graf jest hamiltonowski')
    elif is_path:
        print('Graf jest półhamiltonowski')
    else:
        print('Graf nie jest hamiltonowski')


    # get_path(end[1], last_set)



if __name__ == "__main__":
    input = read_input() 
    held_karp(input)
