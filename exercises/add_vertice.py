from sys import stdin


def read_input():
    out_matrix = []
    for line in stdin:
        line = [eval(i) for i in line.rstrip().split(' ')]
        out_matrix.append(line)
    vertice = out_matrix.pop()
    return out_matrix, vertice


def add_vertice(matrix, i_vertice):
    for index, vertice in enumerate(matrix):
        vertice.append(i_vertice[index])
    matrix.append(i_vertice)


if __name__ == "__main__":
    matrix, vertice = read_input()
    add_vertice(matrix, vertice)
    for row in matrix:
        print(*row, sep=' ')
