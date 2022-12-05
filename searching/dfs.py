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
        visited.append(v)
        for edge in sorted(input_list[v - 1][1:], reverse=True):
            if edge not in visited:
                if edge in stack:
                    stack.remove(edge)
                stack.append(edge)
    print('Porządek DFS: ', end='')
    print(*visited, sep=' ')
    if len(visited) == len(input_list):
        print(f'Graf jest spójny')


if __name__ == "__main__":
    input_list, start = read_list()
    print(start)
    dfs(input_list, start)
