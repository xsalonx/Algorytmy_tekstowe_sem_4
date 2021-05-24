
import numpy as np


# odczytuje z pliku uprzednio obliczone odległości
def parse_file_of_dist(path, n):
    print(f"Parsing file of distances:: {path}")
    with open(path) as f:
        Lines = [f.readline() for _ in range(n*(n-1) // 2)]

    D = np.zeros(shape=(n, n), dtype=np.float)

    assert len(Lines) == n*(n-1) / 2

    l = 0
    for i in range(1, n):
        for j in range(i):
            d = Lines[l].split(":")
            v = float(d[2])
            D[i][j] = v
            D[j][i] = v
            l += 1


    D[np.logical_not(np.isfinite(D))] = 0
    return D


if __name__ == '__main__':
    path = "Nowy folder/lcs_.txt"
    D = parse_file_of_dist(path, 1000)
    print(np.min(D[D != 0]))

