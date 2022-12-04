from sys import stdin


def read_input():
    out_matrix = []
    for line in stdin:
        line = [eval(i) for i in line.rstrip().split(' ')]
        out_matrix.append(line)
    vertice = out_matrix[-1:][0][0]
    out_matrix.pop()
    return out_matrix, vertice


def add_vertice(matrix, i_vertice):
    for vertice in matrix:
        vertice.pop(i_vertice - 1)
    matrix.pop(i_vertice - 1)


if __name__ == "__main__":
    matrix, vertice = read_input()
    if vertice not in range(1, len(matrix)):
        print('BŁĄD')
    else:
        add_vertice(matrix, vertice)
        for row in matrix:
            print(*row, sep=' ')
