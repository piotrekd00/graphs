from sys import stdin


def read_list():
    out_list = []
    for line in stdin:
        line = list(map(lambda x: int(x), line.rstrip().split(' ')))
        out_list.append(line)
    start = out_list.pop()
    return out_list, start[0]


def dfs(input_list, start):
    stack = [start]
    visited = []
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
        for edge in sorted(input_list[v - 1][1:], reverse=True):
            if edge not in visited:
                stack.append(edge)
    if len(visited) == len(input_list):
        print('Porządek DFS: ', end='')
        print(*visited, sep=' ')
        print('Graf jest spójny')
    else:
        print('Graf jest niespójny')


if __name__ == "__main__":
    input_list, start = read_list()
    if start in range(1, len(input_list) + 1):
        dfs(input_list, start)
    else:
        print('BŁĄD')
